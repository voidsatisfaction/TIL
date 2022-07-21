# 도메인 서비스의 정의

도메인 모델은 "어떠한 것(물건)" 중심으로 생각했습니다만, "어떠한 것"에 대한 조작으로서는 어떻게해도 표현할 수 없는 "어떠한 행위"도 있습니다. 또한, "어떠한 것"으로서의 모델의 불변성을 유지하기 위해서, 조작을 모델로부터 떨어뜨리는 경우도 있습니다. 이러한 경우에 정의하는 것이 도메인 서비스입니다. 이제까지 봐 왔던 리포지토리, 관계해결, 도메인액션도 넓은 의미의 도메인 서비스라고 생각해도 좋습니다만, 이 프로젝트에서는 이러한 것들에 해당되지 않는것을 도메인 서비스로 부릅니다.

- (부작용이 없는)불변의 서비스
  - "어떠한 것"에 대한 조작
  - "어떠한 행위"에 대한 조작
- 부작용을 동반하는 서비스
  - "어떠한 것"에 대한 조작
  - "어떠한 행위"에 대한 조작
- 인프라 층에서 구현된 서비스
- 모델의 조작, 서비스 개념의 정리

## (부작용이 없는)불변의 서비스

### "어떠한 것"에 대한 조작

리포지토리에의 읽기 엑세스 등, (도메인이 아니라 프로그램 의미론상의)부작용이 있는 조작이 필요 없는 "어떠한 것"의 조작은 `domain.model`안의 엔티티나 값 오브젝트의 정의와 함께, 직접 메서드나 확장 메서드로 정의 합시다.

### "어떠한 행위"에 대한 조작

불변의 조작 밖에 하지 않으며, "어떠한 것"의 조작으로서 표현하는것은 부적절한 것, "어떠한 행위"로 표현하는 것이 타당한 것은, 평범한 메서드나 필요에 의한 확장 메서드 등으로 정의합니다. 케이크 패턴을 사용하지 않고 구현합시다. 이는 부작용이 전혀 없는 평범한 스칼라 코드가 되기 때문에, 예시는 생략합니다.

## 부작용을 동반하는 서비스

### "어떠한 것"에 대한 조작

리포지토리의 읽기 액세스등, (도메인이 아닌 프로그램의 의미론 상에서의)부작용이 있는 조작이 필요없는 "어떠한 것"의 조작, 즉 메모리상에서 계산이 완결하는 것과 같은 조작은 `domain.model`안의 엔티티나 값 오브젝트의 정의와 함께, 직접 메서드나 확장 메서드로 정의 합시다. 이는 도메인 서비스가 아니라 모델의 메서드라고 부릅니다.

예를들면 리포지토리에의 접근을 동반하기 때문에, 모델의 메서드로서는 부적절한 경우에는, 도메인 서비스의 하나의 종류로서 "어떠한 것"에 대한 조작의 확장 메서드를 정의 합니다.

- (1) 리포지토리등에 의존하므로 Cake패턴에 따름
- (2) 확장 메서드로서 구현함
- (3) 실제의 조작 내용은 직접 작성하지 않고 서비스 취득 메서드를 경유함
  - 이렇게 해두면 테스트할 때 목업하기 쉬움
  - 서비스의 구현이 전부 인프라층에 있는 경우도 이 메서드를 인프라 층에다 두면 됨

```scala
// domain/service/Canonicalization.scala
package boston
package domain
package service

import domain.model.url.{CanonicalURL, URL}

trait CanonicalizationComponent {                                  // (1)
  self: SomeDependingComponent =>                                  // (1)

  def canonicalizationService(): CanonicalizationService =         // (3)
    CanonicalizationService

  trait CanonicalizationService {
    def canonicalize(url: URL): CanonicalURL
  }

  object CanonicalizationService extends CanonicalizationService {
    def canonicalize(url: URL) = ...
  }

  implicit class Canonicalizer(url: URL) {                         // (2)
    def canonicalized: CanonicalURL =                              // (2)
      canonicalizationService.canonicalize(url)                    // (3)
  }
}
```

### 어떠한 "행위"에 대한 조작

"어떠한 행위"에 대한 조작으로 표현하는 것이 부적절하며, 리포지토리 접근 등 부작용을 동반하는 경우는 Cake패턴을 사용한 서비스로서 정의합니다. 핫 엔트리를 취득 / 추가 하는 서비스를 예를 들어서 정의 하는 법을 봅시다.

- (1) 리포지토리등에 의존하므로 케이크 패턴에 따름
- (2) 리포지토리의 경우와 같이, 어노테이션은 지정함
- (3) 도메인에의 부작용이 없는 메서드는 평범하게 정의 함
- (4) 도메인에의 부작용이 있는 메서드는 `domain.action.Action[]`타입을 반환값으로 함

```scala
// domain/service/Hotentry.scala
package boston
package domain
package service

import domain.action.Action
import domain.model.entry.EntryEntity

trait HotentryComponent {                                          // (1)
  self: SomeDependingComponent =>                                  // (1)

  def hotentryService(): HotentryService = HotentryService

  class HotentryService {
    @order("score DESC")                                           // (2)
    def listAll(): Seq[EntryEntity] = ...                          // (3)

    def add(entry: EntryEntity): Action[Unit] =                    // (4)
      Action { implicit runner =>
        ...
      }
  }
  object HotentryService extends HotentryService
}
```

`Action[]`타입을 반환값으로 하는경우, 작성법은 도메인 액션과 비슷하게 됩니다. 이러할 떄, `Actionp[]`타입을 반환하는 메서드가 내부에서 도메인 액션을 호출하는 경우도 있겠죠. 이러한 경우는 `Action[]`의 `map()`이나 `flatMap`등의 모나딕한 조작으로 `Action[]`을 결합하여 반환합니다.

```scala
def fooAction(): Action[Foo] = ???
def barAction(): Action[Bar] = ???

def myAction(): Action[(Foo, Bar)] = for {
  foo <- fooAction()
  bar <- barAction()
} yield Action(_ => (foo, bar))
```

이 경우에 `runner`는 사용하지 않으므로 `Action(_ => ...)`의 부분은 `Action.unit(...)`로 작성해도 같습니다.

## 인프라층에 구현되는 서비스

도메인 서비스의 구현내용의 거의 대부분이 인프라층에서의 처리가 되는 경우가 있습니다. 이는 데이터베이스나 엘라스틱서치등의 미들웨어에 극도로 의존한 처리를 하는 경우 뿐 아니라, API에 의한 리모트 접근을 수반하는 경우도 포함합니다. 이 경우, `domain.service`에는 인터페이스만 두고, 구현은 모두 인프라스트럭처층에 두는 것이 좋겠죠. 도메인이 인프라에 의존해서는 안된다는 Cake패턴으로 구현합니다.

- (1) 레이어를 넘나드는 의존관계이므로 케이크 패턴에 따름
- (2) 도메인층에서는 인터페이스만 구현해놓음
- (3) 리포지토리의 경우와 같이, 어노테이션은 지정함
- (4) 인프라층에서는 의존하는 미들웨어등을 사용할 수 있음
- (5) 인프라층에서 구체적인 구현을 부여
- (6) 인프라층에는 미들웨어 등에 특화한 처리가 작성됨

```scala
// domain/service/BookmarkSearch.scala
package boston
package domain
package service

import domain.model.bookmark.BookmarkEntity
import domain.model.tag.TagEntity
import domain.model.user.UserId
import types.annotation.order

trait BookmarkSearchComponent {                                    // (1)
  def bookmarkSearchService(): BookmarkSearchService               // (1)

  trait BookmarkSearchService {                                    // (2)
    @order("created DESC")                                         // (3)
    def searchByTags(userId: UserId, tags: Seq[TagEntity]): Seq[BookmarkEntity]
  }
}
```

```scala
// infrastructure/es/BookmarkSearch.scala
package boston
package infrastructure
package es

import com.hatena.{es => common}
import model.bookmark.BookmarkEntity
import model.tag.TagEntity
import model.user.UserId

trait BookmarkSearchComponent                                      // (1)
    extends domain.service.BookmarkSearchComponent {
  self: common.InstanceProvider                                    // (4)
      with domain.repository.BookmarkComponent =>

  def bookmarkSearchService: BookmarkSearchService =               // (5)
    BookmarkSearch

  trait BookmarkSearch extends Handler
      with BookmarkSearchService {
    @order("created DESC")                                         // (3)
    def searchByTags(userId: UserId, tags: Seq[TagEntity]): Seq[BookmarkEntity] = {
      val hits = es.run { ... tags ... }                           // (6)
      val locationIds = ... hits ...                               // (6)
      bookmarkLoader.findAllByUserIdAndLocationIds(userId, locationIds)
    }
  }
  object BookmarkSearch extends BookmarkSearch
}
```

물론, 같은 서비스 안에서도 인프라층에 의존하지 않는 처리는 도메인층에 작성해도 상관 없습니다.

## 모델의 조작, 서비스 개념의 정리


|操作の種類                                 |置く場所         |「モノ」の操作|不変|ドメインへの副作用|エンティティを返す|
|:------------------------------------------|:----------------|:------------:|:--:|:----------------:|:----------------:|
|[値オブジェクトのメソッド][model-operation]|`domain/model`   |yes           |yes |no                |no                |
|[モデルの拡張メソッド][model-operation]    |`domain/model`   |yes           |yes |no                |yes               |
|[Cakeな拡張メソッド][caked-model-operation]|`domain/service` |yes           |no  |no                |maybe             |
|[関係解決][relation]                       |`domain/relation`|yes           |no  |no                |maybe             |
|[ドメインアクション][action]               |`domain/action`  |yes           |no  |yes               |maybe             |
|[不変サービス][immutable-service]          |`domain/service` |no            |yes |no                |maybe             |
|[Cakeなサービス][caked-service]            |`domain/service` |no            |no  |maybe             |maybe             |

케이크한 확장 메서드로 해야하는가, 관계해결로 해야하는가 고만하는 경우도 있을 수 있습니다. 이러한 경우의 결정 기준은, 정의하려고하는 조작이 관계를 정의하고 있는가, 입니다.
