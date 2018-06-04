# 의존성 주입(Dependency injection)

## 의존성 주입

소프트웨어 컴포넌트는 상호 의존하고 있으므로, 의존관계가 밀접하고 복잡한 것이 되면 컴포넌트 모듈성의 성질이 엷어지고, 소프트웨어 전체를 거대한 하나의 덩어리 모듈로 다룰 수 밖에 없게 됨

그러나, 레이어 아키텍처의 계층간의 의존관계에서 봤듯, 웹 애플리케이션은 어떠한 의미로는 떼어낼 수 없는 거대한 하나의 덩어리가 될 수 밖에 없으며, 레이어나 컴포넌트는 그 덩어리의 안에서 구별되는 것을 구별한 것이며, 레이어나 컴포넌트는 그것 하나 만으로 기능을 하지 않음. 결국, 웹 애플리케이션과 같은 거대한 소프트웨어의 안에 나타나는 컴포넌트의 모듈성이라는 것은 다음과 같은 성질을 말함

- 은폐성
  - 컴포넌트는 다른 컴포넌트의 기능을 그 자세한 구현을 알지 못해도 이용함
- 교환가능성
  - 컴포넌트는 다른 컴포넌트의 변경 없이 교체 가능

이러한 조건을 만족해야만, 아무리 복잡하게 의존해있다고 하더라도, 각 컴포넌트를 적절한 교환가능한 부품으로 유지하는 것이 가능함. 물론, 마구잡이로 구현하는 것은 안되며, 이러한 성질을 만족하기 위해서는 일정한 방법으로 **컴포넌트 사이의 의존의 방법을 제어** 할 필요가 있음.

컴포넌트가 상호 의존하는 것을 허락하면서 교환가능성을 유지하는 방법의 하나는 **의존성의 주입(dependency injection; DI)** 임. DI의 기본적인 발상은, 의존하는 컴포넌트의 구체적인 구현을 나중에 주입할 수 있도록 하는 것임. 주입하는 구체적인 구현이 다르면, 교환 된 것과 같은 것임. 주입이라고 표현하는 것은, 주입된 컴포넌트를 이용하는 장소가, 주입하는 장소로부터 봤을때, 호출 계층의 매우 깊이 숨겨져 있는 경우를 포함하기 때문임

DI를 구현하는 방법은 여러가지 있으나, 스칼라의 불변 스타일과 잘 맞아떨어지지 않는 모델은 회피해야 함. 또한, 도메인 기반 설계를 진행하는데에 있어서, DI를 위해 도메인층의 인터페이스를 왜곡하는 것도 피하고 싶음. 그 해법으로 **Cake패턴** 을 소개함. 레이어 사이를 포함해서 큰 의존성의 표현으로서 이 방법은 매우 유용함

## 왜 DI가 필요한 것인가?

먼저, DI가 필요한 장면을 구체적인 예로 보자. 구체적인 예시로서는 테스트를 작성하는 경우를 새각함. DI가 효과를 발휘하는 것은 테스트를 작성하는 경우만 한정되는 것이 아니라, 단순히 알기 쉬운 예시를 들기 위해서.

### 간단한 목(mock)

예를들면, `bookamrkApplication.add()`에서 유저의 북마크가 추가되어, `entryApplication.get()`에서 시스템 상에 존재하는 웹 페이지 엔트리 정보를 얻어, 누군가가 어떠한 URL을 북마크 했을 경우는 그 URL을 정규화 한 것을 갖는 엔트리가 생성된다고 하자. 북마크의 추가로 엔트리가 생성되는 것, 혹은 그 엔트리를(정규화 전의)URL을 단서로 취득 가능한것, 취득된 엔트리에 이어지는 URL은 정규화된 것이라는 것을 테스트하기 위해서는 다음과 같은 테스트코드를 작성하게 됨. 이 예시는 `http://example.com/1?foo=bar`은 `http://example.com/1`로 정규화 되는것이라고 하자.

```scala
class EntrySpec extends FunSpec with Matchers {
  def generateTestUser(): UserEntity = ...

  describe("bookmarked entry") {
    it("should have a canonicalized URL") {
      val user = generateTestUser()
      val url = URL("http://example.com/1?foo=bar")
      bookmarkApplication.add(user, url)

      val entry = entryApplication.get(url)
      entry.url shouldBe CanonicalURL("http://example.com/1")
    }
  }
}
```

실제의 URL정규화 처리는 암묵 클래스 `Canonicalizer`에 의해서 확장 메서드로서 제공되어있으며, `bookmarkApplication`과 `entryApplication`의 각각 구현에서 이용되고 있다고 하자

```scala
implicit class Canonicalizer(url: URL) {
  def canonicalized: CanonicalURL = ...
}
```

```scala
object BookmarkApplication {
  def add(user: UserEntity, url: URL): Unit = {
    val canonicalUrl = url.canonicalized

    // - canonicalUrl에 연결된 엔트리가 없는 경우, 리포지토리를 퉁해서 작성
    // - user가 url을 북마크했음을 알리는 정보를 넘김
  }
}

def bookmarkApplication = BookmarkApplication
```

```scala
object EntryApplication {
  def get(url: URL): EntryEntity = {
    val canonicalUrl = url.canonicalized

    // 리포지토리에서 canonicalUrl에 연결된 엔트리를 취득함
  }
}
def entryApplication = EntryApplication
```

`Canonicalizer.canonicalized`가 언제나 정해진 값을 반환하면 문제가 없으나, 데이터페이스에 보존 된 데이터에 의해서 정규화 방법이 달라지도록 되어있거나, 애초에 정규화의 룰이 시간과 함꼐 추가 / 변경 되어가는 경우, `Canonicalizer.canonicalized`의 동작이 변할 때 마다 테스트를 변경해야 할 필요가 생김

원래 테스트 하고 싶었던 것은 `Canonicalizer.canonicalized`의 구현이 어떻든, 정규화전과 정규화 후의 URL이 다르게 되는 예시에 대해서 의도한 동작이 되도록 하는 것이었다. 이 경우, 원래 하고 싶었던 것은 `Canonicalizer.canonicalized`의 동작을 목업한 다음 테스트를 하는 것이다.

```scala
class EntrySpec extends FunSpec with Matchers {
  def generateTestUser(): UserEntity = ...

  implicit class MockCanonicalizer(url: URL) {
    def canonicalized: CanonicalURL = url match {
      case URL("http://example.com/1?foo=bar") => CanonicalURL("http://example.com/1")
      case _ => sys.error("unexpected")
    }
  }

  describe("bookmarked entry") {
    it("should have a canonicalized URL") {
      val user = generateTestUser()
      val url = URL("http://example.com/1?foo=bar")
      bookmarkApplication.add(user, url)

      val entry = entryApplication.get(url)
      entry.url shouldBe CanonicalURL("http://example.com/1")
    }
  }
}
```

하지만, 이와 같은 목업된 암묵 클래스 `MockCanonicalizer`를 테스트클래스 안에 정의한다 한들, `bookmarkApplication.add()`나 `entryApplication.get()`의 안의 동작에까지 영향을 주는 것은 불가능함

**혹시 `bookmarkApplication`이나 `entryApplication`이 의존하고 있는 `Canonicalizer`의 구체적인 구현을 나중에 주입하는 것이 가능하면, 테스트의 경우에만 목업판을 교체하는 것도 가능하게 됨.** 이것이 바로 DI로 하고 싶은 것

이번에는 `bookmarkApplication`이나 `entryApplication`이 `Canonicalizer`의 직접적 이용자 이므로, 애플리케이션 서비스의 취득 메서드에 `Canonicalizer`의 인스턴스를 건네주는 간단한 방법으로도 의존성을 주입하는 것이 가능하나, 일반적으로는 보다 깊은 곳까지 의존성을 주입해줄 필요가 있거나, 주입 해야하는 의존 컴포넌트의 수나, 같은 컴포넌트에 의존하고 있는 컴포넌트의 수가 증가하는 것으로 점점 복잡하게 되어감

### 횡단적인 구현의 교체

다른 하나의 예를 보자. 시스템의 광범위하게 넘겨져서 이용되고 있는 컴포넌트, 예를들면 데이터베이스 핸들러의 구현을 테스트 때에만 바꾸고 싶은은 경우가 있다.

예를들어, `bookmarkApplication`에 모든 유저가 붙인 북마크의 총 수를 계산하는 메서드 `countUpAllBookmarks()`가 정의되어 있다고 하자. 북마크를 전부 추가하지 않은 단계(서비스 운용 개시 전)에서는 총 수는 0이므로, 북마크를 추가할 때마다 증가해 나가는 것을 확인하고 싶을 것이다.

```scala
class BookmarkSpec extends FunSpec with Matchers {
  def generateTestUser(): UserEntity = ...

  describe("Bookmark application") {
    it("should be able to count up all the bookmarks in the system") {
      bookamrkApplication.countUpAllBookmarks() shouldBe 0

      val user1 = generateTestUser()
      val user2 = generateTestUser()
      val url1 = URL("http://example.com/1")
      val url2 = URL("http://example.com/2")

      bookamrkApplication.add(user1, url1)
      bookmarkApplication.countUpAllBookmarks() shouldBe 1

      bookamrkApplication.add(user1, url2)
      bookmarkApplication.countUpAllBookmarks() shouldBe 2

      bookamrkApplication.add(user2, url1)
      bookmarkApplication.countUpAllBookmarks() shouldBe 3

      bookamrkApplication.add(user2, url1)
      bookmarkApplication.countUpAllBookmarks() shouldBe 4
    }
  }
}
```

이러한 테스트를 올바르게 동작하게 하기 위해서는, 적어도 테스트 클래스마다 데이터베이스의 내용을 제거해 둘 필요가 있습니다. 그렇지 않으면, 이 테스트 보다 먼저 북마크 추가를 하는 테스트가 있는경우, 이 테스트는 실패하게 됩니다.

사실은, 테스트 클래스마다 데이터베이스 내용을 삭제하는 것 만으로는 부족할 가능성이 있습니다. 예를들면, 테스트클래스마다 다른 프로세스에서 테스트를 작동시키는 것으로 병렬도를 높여서 효율화 하는 경우 입니다. 이 경우, `BookmarkSpec`이 작동하는 반대편에 `EntrySpec`이 작동하면 북마크 총 수가 맞지 않게 됩니다.(이러한 경우는 테스트의 실행 그 자체는 직렬이어도, CI서버상에서 복수의 브랜치의 테스트가 동시에 작동하여, 테스트용의 데이터베이스 서버는 공통화 되어있는 상황에서도 발생합니다.)

멀티 프로세스 환경에서의 테스트의 문제에 올바르게 대처하기 위해서는, 테스트 프로세스마다 사용하는 데이터베이스를 격리하는 방법 밖에 없습니다. 테스트 프로세스마다 다른 데이터베이스 서버를 시작하는 것은 리소스의 관점에서 그다지 현실적이지 못하지만, 다른 데이터베이스 이름(예를들어 (원래 데이터베이스 이름)_(테스트프로세스ID) 와 같은 이름)에 대해서 읽기 쓰기를 하게 된다면 잘 될 것입니다.

당연히, production환경의 웹 애플리케이션에는 이러한 로직은 불필요하므로, 테스트를 할 때에만 데이터베이스 핸들러의 구현을 프로세스마다의 데이터베이스 이름을 사용하므로써 변경하면 좋을 것입니다.

그러나, 데이터베이스 핸들러를 이용하고 있는 것은 인프라스트럭처층의 리포지토리 구현부분으로, 애플리케이션 서비스로부터 보면 호출 계층이 매우 깊이 있습니다. 또한, 애플리케이션 서비스의 구현을 보는 것 만으로는 그 안에 이용되고 있는 데이터 베이스에 접근하는 리포지토리 클래스의 모두를 파악하는 것은 어려울 수 있습니다. 이러한 조건하에서 데이터베이스 핸들러의 동작을 일괄하여 변경하기 위해서는 데이터베이스 핸들러의 컴포넌트로서의 테스트용 구현을 애플리케이션 전체에 주입하는 방법이 필요하겠지요.

## 안티패턴

### Java에서의 전통적인 방법

### 생성자 전달

### 메서드 전달

### Reader 모나드

## Cake 패턴

### 하나의 덩어리로서의 애플리케이션

웹 애플리케이션은 어떠한 의미에서는 분리할 수 없는 거대한 하나의 덩어리 라는 발상을 받아들여서, 컴포넌트를 분리하지 않고 하나의 애플리케이션 오브젝트 안에 모두 구현해봅시다.

```scala
trait App {
  def bookmarkApplication = BookmarkApplication
  def entryApplication = EntryApplication
  def canonicalizationService: CanonicalizationService = CanonicalizationService
  def entryRepository: EntryRepository = EntryDB
  def db: DB = new DB(...)

  implicit class Canonicalizer(url: URL) {
    def canonicalized: CanonicalURL = canonicalizationService.canonicalize(url)
  }

  implicit class BookmarkRelation(bookmark: BookmarkEntity) {
    def toEntry(): Option[EntryEntity] = {
      val canonicalUrl = bookmark.url.canonicalized // (1)
      entryRepository.findByUrl(canonicalUrl) // (2)
    }
  }

  object BookmarkApplication {
    def add(user: UserEntity, url: URL): Unit = ...
  }

  object EntryApplication {
    def get(url: URL): EntryEntity = ...
  }

  trait CanonicalizationService {
    def canonicalize(url: URL): CanonicalURL = ...
  }
  object CanonicalizationService extends CanonicalizationService

  trait EntryRepository {
    def findByUrl(url: URL): Option[EntryEntity]
  }

  object EntryDB extends EntryRepository {
    def findByUrl(url: URL): Option[EntryEntity] = db.run { ... }
  }
  ...
}
object App extends App
```

각 컴포넌트는 다른 컴포넌트를 자유롭게 참조할 수 있습니다. 예를들면, `BookmarkRelation`의 안에서는 (1)에서 확장 메서드 `canonicalized`를, (2)에서 `entryRepository`를 참조하고 있습니다. `EntryDB`의 안에서는 (3)에서 데이터베이스 핸들러를 참조하고 있습니다.

이러한 방법이라면, 테스트 등의 목적으로 컴포넌트를 교체하는 것도 매우 간단합니다.

```scala
trait TestableApp extends App {
  override def db(): DB = new TestableDB(...)
}
```

이것만으로도 `new TestableApp {}`에서는 모든 컴포넌트에 걸쳐서 데이터베이스 핸들러가 테스트용으로 교체되어 집니다. 또한, 테스트용의 데이터베이스 핸들러로 교체됐을 뿐 아니라, `CanonicalizationService`를 목업하는 것도 간단히 할 수 있습니다.

```scala
class EntrySpec extends FunSpec with Matchers {
  def generateTestUser(): UserEntity = ...

  def appWithMockCanonicalization(): App =
    new TestableApp {
      override def canonicalizationService: CanonicalizationService =
        new CanonicalizationService() {
          override def canonicalization(url: URL): CanonicalURL = url match {
            case URL("http://example.com/1?foo=bar") => CanonicalURL("http://example.com/1")
            case _ => sys.error("unexpected")
          }
        }
    }

    describe("Bookmarked entry") {
      it("should have a canonicalized URL") {
        val app = appWithMockCanonicalization()

        val user = generateTestUser()
        val url = URL("http://example.com/1?foo=bar")
        app.bookmarkApplication.add(user, url)

        val entry = app.entryApplication.get(url)
        entry.url shouldBe CanonicalURL("http://example.com/1")
      }
    }
}
```

### 컴포넌트의 분할

애플리케이션은 어떠한 의미로 하나의 덩어리이므로, 컴포넌트는 반드시 그 하나가 완전한 동작을 할 필요는 없지만, 정말로 하나의 오브젝트 안에 모든 것을 넣어버리면 불편한 점도 많이 있다.

- 하나의 파일이 매우 길게되어서 편집 하기 힘들고 읽기 힘들다
- 편집할 때마다 모든 컴포넌트를 컴파일 하기 때문에 시간이 걸린다
- 하나의 컴포넌트를 테스트하는데에 애플리케이션 전체가 필요하다

여기서, 기본적인 발상은 그대로, 우직하게 `App`트레잇을 분할해보자. 일단은 `EntryRepository`만 잘라내보자

```scala
trait EntryRepositoryComponent {
  def entryRepository: EntryRepository

  trait EntryRepository {
    def findByUrl(url: URL): Option[EntryEntity]
  }
}
```

훌륭하게 인터페이스만으로 구현해냈습니다. `entryRepository`는 실제로는 인프라 스트럭처에 놓여야 하는 `EntryDB`를 반환하고 싶으므로, 여기서는 인터페이스를 정의 할 뿐입니다. 이러한 방식으로 `BookmarkRelation`도 분할 해봅시다

```scala
trait BookmarkRelationComponent {
  implicit class BookmarkRelation(bookmark: BookmarkEntity) {
    def toEntity(): Option[EntryEntity] = {
      val canonicalUrl = bookmark.url.canonicalized // (1)
      entryRepository.findByUrl(canonicanonicalUrl) // (2)
    }
  }
}
```

이번에는 위와 같은 코드로는 (1)과 (2)의 메서드를 호출 할 수 없으므로 좋지 않습니다. (1)의 `canonicalized`는 `CanonicalizationComponent`로서 분할 할것으로 생각되는 것에, (2)의 `entryRepository`는 `EntryRepositoryComponent`에 의존 합니다.

이러한 의존 컴포넌트를 계승해야 할까요? 컴포넌트로서는 이러한 코드는 독립하고 있으므로 상속하는 것도 이상한 이야기 입니다. 그러나 의존하고 있는 것은 의심할 여지가 없기 때문에, `BookmarkRelationComponent`가 인스턴스화 될 때는, `CanonicalizationComponent`와 `EntryRepositoryComponent`도 믹스인 되는 것을 강제해야 하고, 또한, `BookmarkRelationComponent`의 안에서 `canonicalized`나 `entryRepository`가 호출될 수 있도록 하는 것이 이상적입니다. 스칼라에서는 이러한 것을 실현할 수 있도록 자기타입 어노테이션이 존재합니다(self type annotation)

```scala
trait BookmarkRelationComponent {
  self: CanonicalizationComponent with EntryRepositoryComponent =>

  implicit class BookmarkRelation(bookmark: BookmarkEntity) {
    def toEntry(): Option[EntryEntity] = {
      val canonicalUrl = bookmark.url.canonicalized
      entryRepository.findByUrl(canonicalUrl)
    }
  }
}
```

이것은 실제로 매우 잘 컴포넌트가 분리됩니다. 이 컴포넌트의 안에서는 암묵 클래스 `BookmarkRelation`만이 정의되어, 그 내부의 처리가 의존하는 `CanonicalizationComponent`와 `EntryRepositoryComponent`가 명시적으로 의존 컴포넌트로서 지정되어있습니다. 컴포넌트로서 모듈성을 유지하면서, 필요최소한의 의존관계 만을 갖고 있습니다.

이 상태로 다른 컴포넌트도 분할 가능합니다. 참고로 데이터베이스 핸들러(DBHandlerComponent)와 엔트리 리포지토리 구현(EntryDBComponent)의 예를 작성해 두었습니다.

```scala
trait DBHandlerComponent {
  def db: DB = new DB(...)
}

trait EntryDBComponent extends EntryRepositoryComponent {
  self: DBHandlerComponent =>

  def entryRepository: EntryRepository = EntryDB

  object EntryDB extends EntryRepository {
    def findByUrl(url: URL): Option[EntryEntity] = db.run { ... }
  }
}
```

`EntryDBComponent`에서는, 이번에는 확실히 `EntryRepositoryComponent`를 보통의 의미로 구현하고 있으므로, `extends`를 사용하고 있습니다(의존 컴포넌트인 DBHandlerComponent는 자기타입 어노테이션으로 지정합니다)

### 컴포넌트의 결합

컴포넌트를 분할해 나갈 수 있다는 것을 알게 되었으므로, 분할된 컴포넌트를 결합해서 다시 하나의 덩어리 애플리케이션을 구축하는 방법을 봅시다. 컴포넌트는 단순한 트레잇으로, 자기타입 어노테이션에서 지정된 의존 컴포넌트가 믹스인 되고있는것이 이용조건이므로, 관계있는 컴포넌트를 모두 모아주면 되는 것 뿐입니다.

```scala
trait App extends DBHandlerComponent
  with EntryDBComponent
  with BookmarkRelationComponent
  with CanonicalizationComponent
  with BookmarkApplicationComponent
  with EntryApplicationComponent
  ...

object App extends App
```

매우 직관적이군요. `EntryRepositoryComponent`는 `EntryDBComponent`에 포함되어있으므로 믹스인 하지 않아도 상관 없다는 점을 주의 합시다.(믹스인 해도 됩니다)

같은 방법으로 데이터베이스 핸들러를 테스트용으로 변환한 애플리케이션을 만드는 것도 가능합니다.

```scala
trait TestableDBHandlerComponent extends DBHandlerComponent {
  override def db: DB = new TestableDB(...)
}
```

```scala
object TestableApp extends App with TestableDBHandlerComponent
```

이쪽도 매우 간단합니다. `TestableDBHandlerComponent.db`쪽을 더 우선시 하고 싶으므로, `DBHandlerComponent`보다도 나중에 믹스인 하지 않으면 안되는 점만 주의해주세요.

### 컴포넌트의 테스트

하나의 덩어리의 애플리케이션을 만들 때에 특정 컴포넌트만 교체하는 것과 같은 요령으로 테스트용 목을 적용하는 것도 가능합니다만, 하나하나 애플리케이션 전체의 인터페이스를 사용해서 테스트를 하는것보다는 컴포넌트 마다 독립해서 단독 테스트가 가능한 편이 편리 합니다.

컴포넌트를 단독 테스트하기 위해서는 테스트 클래스 그 자체에 컴포넌트의 트레잇을 믹스인 해버리는 것이 가장 알기 쉽습니다. 자기타입 어노테이션된 의존 컴포넌트도 잊지 않고 믹스인 혹은 목업 할 필요가 있는 점만 주의하면 어렵지 않습니다.

```scala
class EntryDBSpec extends FunSpec with Matchers with EntryDBComponent with TestableDBHandlerComponent {
  describe("EntryDB") {
    ...
  }
}
```

높은 레이어의 컴포넌트의 경우는, 의존 컴포넌트가 많아지므로 오히려 `App`을 믹스인해버리는 편이 간단할 지도 모릅니다. 이는 높은 레이어의 테스트일 경우 점점 결합 테스트의 측면이 되는것과 같은 것을 의미합니다.

```scala
class EntrySpec extends FunSpec with Matchers with App with TestableDBHandlerComponent {
  def generateTestUser(): UserEntity = ...

  override def canonicalizationService: CanonicalizationService =
    new CanonicalizationService() {
      override def canonicalize(url: URL): CanonicalURL = url match {
        case URL("http://example.com/1?foo=bar") => CanonicalURL("http://example.com/1")
        case _ => sys.error("unexpected")
      }
    }

  describe("Bookmarked entry") {
    it("should have a canonicalized URL") {
      val user = generateTestUser()
      val url = URL("http://example.com/1?foo=bar")
      bookamrkApplication.add(user, url)

      val entry = entryApplication.get(url)
      entry.url shouldBe CanonicalURL("http://example.com/1")
    }
  }
}
```

일부 컴포넌트의 목업이 테스트 클래스상의 `override def`로 끝나는 것은 매우 편리하군요.

### 패턴에의 비판과 올바른 사용

Cake패턴은 애플리케이션이 구현에는 거대한 하나의 덩어리 라는 직감에 솔직히 따르면서도, 컴포넌트의 분할, 모듈화를 강력히 서포트하는 새로운 의존성주입의 방식입니다. 그러나 Cake패턴에도 결점은 있으며, 오용할 경우, 좋지 않습니다. 이에 대한 지적을 인용 하겠습니다.

> [Miles Sabin answered - What are some compelling use cases for dependent method types?](https://stackoverflow.com/questions/7860163/what-are-some-compelling-use-cases-for-dependent-method-types/7861070#7861070)

여기서 지적되고 있는것은, Cake패턴에서 정의된 컴포넌트의 타입을 Cake의 밖에서 이용하려 하면, 패스 의존 타입을 사용하는 것이 되므로, 매우 귀찮다는 것입니다.

이러한 문제가 발생하는 것은, 재사용가능한 매우 독립성이 높은 부품을 만들때에 Cake패턴을 사용하여, 또한 Cake의 안에서 정의 되어있는 타입을 그 부품의 인터페이스에 포함해 버렸기 때문입니다. 부품의 밖에 공개하는 인터페이스는 Cake의 밖에 놓여진 평범한 타입으로 할 것인지, 혹은 애초에 Cake를 사용하고있는 것이 독립성이 높은 부품이 아닌(예를들면 한 덩어리의 웹 애플리케이션)경우에는 전혀 문제가 없습니다.

Cake패턴을 사용하려면, 원래 하나의 덩어리인 애플리케이션을 분할하기 위해서 큰 컴포넌트 단독의 경우만으로 제한하여, 재사용성이 높은 범용 부품에는 다른 방법을 사용하는 것으로 합시다. 예를들면 애플리케이션에 특화한 부품이 있다고 해도, 의존성 주입의 필요가 없는 추상적인 동작을 하는 경우는 케이크 밖에 놓는 편이 좋습니다.

### 参考文献 <a name="cake-reference"></a>

- [Cake Pattern を理解する][daimatz] (daimatz)
    - 日本語によるふつうの解説
    - 素朴なCakeパターン
- [Dependency Injection in Scala: Extending the Cake Pattern][warski] (Warski)
    - この文書で用いた方法に近いもの
    - `val`ではなく`def`にした方がよい理由が書いてある
    - インタフェースと実装は完全に分けている
- [Scalable Component Abstractions][odersky05] (Odersky '05)
    - Odersky先生による原典

[layered-architecture]: ./architecture.md#layered-architecture
[cake-criticism]: http://stackoverflow.com/a/7861070
[odersky05]: http://lampwww.epfl.ch/~odersky/papers/ScalableComponent.pdf
[daimatz]: http://daimatz.net/text/2014/0128-cake-pattern.html
[warski]: http://www.warski.org/blog/2010/12/di-in-scala-cake-pattern/
