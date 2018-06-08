# 애플리케이션 서비스의 구현

도메인 모델은 비즈니스로직의 문제영역을 추상적으로 표현한 것으로, 문제영역에 어떠한 것이 존재하여 어떠한 조작이 가능한지 표현한 것 이었습니다.

그에 반하여 애플리케이션층은, 비지니스로직의 개개의 유스케이스에 있어서의 구체적인 존재 방법을 표현하여, **유스 케이스 층** 이라고도 불립니다. 유스케이스란 도메인모델에 대한 가능한 조작의 구체적 예시 입니다.

애플리케이션 서비스는, 유스케이스에 있어서 등장인물을 파라미터화 한 메서드를 모은 것 입니다. 애플리케이션 서비스의 인터페이스는, 비지니스 로직으로 상정해야하는 유저 스토리를 실현하기 위해서 과부족 없도록 제공 되어있는 것이 이상적 입니다.

애플리케이션 서비스의 추상화가 잘 되어있다면, 실행의 트리거가 웹으로 부터든, 커맨드라인으로부터든 의식하지 않아도 괜찮을 것입니다. 웹 층이나 커맨드라인층에 작성하는 것은 각각 입력방식을 애플리케이션 서비스의 인터페이스에 맞추는 것에 한정하고, 비지니스 로직 그 자체는 애플리케이션 서비스의 안에 가둬 놓은 것 처럼 합시다.

비지니스로직(및 도메인 로직)과 애플리케이션 로직층의 외부의 입출력을 완전히 분리하기 위해서, 애플리케이션 서비스의 인터페이스에는 도메인 모델(엔티티 등)은 직접 사용하지 않는 것이 좋겠죠(순서가 올바르지 못한가/올바른가, 전역인가등, 반환값 제약의 타입 어노테이션에 의한 지정도 생략해도 좋습니다) 도메인 로직과는 완전히 분리하여, 비즈니스로직의 정도로 인터페이스에서 사용하는 데이터 타입을 생각한 다음으로, 그래도 엔티티나 값 오브젝트 등과 완전히 일치하는 경우는, 도메인 모델의 타입을 그대로 사용해도 괜찮습니다만, 애플리케이션층에 의하여 도메인모델을 변경하는 것이 없도록 합시다.

- 애플리케이션 서비스의 구현
- 핼퍼 컴포넌트

## 애플리케이션 서비스의 구현

- (1) 엔티티의 내용을 각 어댑터에 반환하기 위해서의 데이터 타입을 정의
  - 크고 복잡해지면 포트의 인터페이스를 별도 정의 해도 됨
  - 이 데이터 타입은 다른 컴포넌트에서도 사용가능성이 있으므로 충돌을 피한 명명으로 톱 레벨에 배치하면 좋다
- (2) 케이크 패턴의 구현
  - `ServiceComponent`는 반드시 포함됨
  - `UserAccountHelperComponent`와 같은 핼퍼컴포넌트도 지정
  - 그외 의존하는 도메인 컴포넌트를 지정
- (3) 새 엔티티의 인터페이스는 리포지토리Bootstrap이나 액션을 사용하여 준비함
- (4) 모델에 대한 조작
  - 모델의 부수정보를 얻음
  - 추가 / 삭제등의 액션
- (5) 결과의 반환

```scala
package boston
package application

import domain.model.url.URL
import domain.model.location.LocationEntity
import domain.model.user.{AccountId}
import domain.model.bookmark.{BookmarkEntity, BookmarkId}

case class BookmarkItem(                       // (1)
  userId: String,
  url: URL,
  comment: String
)

trait BookmarkComponent {
  self: ServiceComponent                       // (2)
      with UserAccountHelperComponent
      with domain.service.UserBookmarkComponent
      with domain.relation.BookmarkSubentityComponent
      with domain.action.LocationComponent
      with domain.repository.LocationComponent
      with domain.repository.UserAccountComponent =>

  def bookmarkApplication(viewerAccount: AccountId): BookmarkApplication =
    new BookmarkApplication(viewerAccount)

  class BookmarkApplication(viewerAccount: AccountId)
      extends UserAccountHelper {

    def add(url: URL, comment: String): BookmarkItem = {
      val user = ensureUserAccountExistence(viewerAccount)
      val location =                           // (3)
        LocationEntity.findOrCreateByURL(url)
      val bookmark = BookmarkEntity(
        BookmarkId(user.id, location.id),
        Bookmark().withComment(comment))
      )

      bookmark.add().run()                     // (4)

      BookmarkItem(                            // (5)
        viewerAccount.id,
        location.url,
        comment
      )
    }

    def get(bookmarkerAccount: AccountId, url: URL): Option[BookmarkItem] = {
      for {
        bookmarker <- userAccountLoader.find(bookmarkerAccount.id)
        location <- locationLoader.findByURL(url)
        bookmark <- userBookmarkService(bookmarker).bookmarkOf(location)
        bookmark <- bookmark.toSeq.withComments.headOption
                                               // (4)
      } yield {
        bookmarkItem(                          // (5)
          viewerAccount.id,
          location.url,
          bookmark.comment
        )
      }
    }
  }
}
```

## 핼퍼 컴포넌트

애플리케이션 서비스에서는, 가끔씩 비슷한 동작을 하는 경우가 있습니다. 예를들면, ID로부터 유저를 나타내는 모델을 인스턴스화 하거나, 열람 유저와 접근 리소스의 소유자가 일치하는지 체크하는 등 입니다. 이러한 조작을 각 애플리케이션 서비스마다 독자적으로 하면, 일관성을 유지하는 것이 어려워지므로, 트레잇으로 모아두면 좋습니다.

- `UserAccountHelper` / `UserAccountHelperComponent`
  - `ensureUserAccountExistence()`: 어카운트ID로부터 유저 엔티티를 얻음
- `ScopeRequested[]` / `ScopeRequestedComponent`
  - 액세스 제어가 필요한 경우에 이용하는 범용 트레잇
- `UserPermission` / `UserPermissionComponent`
  - 유저 엔티티의 접근 권한이 필요한 경우 이용하는 트레잇
