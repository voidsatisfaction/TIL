# 관계의 정의

"어떠한 것"을 리포지토리에 의해서 가져오는 것은 가능합니다만, 그것만으로는 단순히 "어떠한 것"이 있는것을 나타내는 것에 지나지 않습니다. 실제의 "어떠한 것"은 다른 "어떠한 것"과 서로 관계를 갖고 있습니다. 도메인 모델을 제대로 표현하기 위해서는, 이 "어떠한 것"사이의 관계도 코드로 표현 해야만 합니다.

예를들면, 복수의 북마크의 URL을 취득하는 다음과 같은 코드를 생각해봅시다.

```scala
val bookmarks: Seq[BookmarkEntity] = ...
val bookmarksWithUrl: Seq[(BookmarkEntity, URL)] =
  bookmarks.flatMap { b =>
    locationLoader.find(b.id.locationId).map((b, _.url))
  }
```

만일 위의 코드가 도메인의 밖, 예를들어 애플리케이션 서비스의 코드라고 하면, 그다지 좋지 못한 코드가 됩니다. 가장 큰 문제는, "북마크의 URL이란, 공통하는 로케이션ID를 갖는 로케이션 URL필드 이다"라는, 북마크와 로케이션의 두 모델이 관계하는 것에 의하여 정의되는 모델상의 개념이, 애플리케이션층에 유출되어 버리는 것 입니다. 원래는, 북마크와 로케이션 및 로케이션의 URL이 어떻게 관계하고 있는가 아는 것은, 도메인층 만으로, 애플리케이션층 에서는 "북마크에 대응하는 URL을 알고싶다"고 도메인층에 문의하는 것 만으로 끝나도록 해야 합니다.

이 코드에는 또 하나 간과할 수 없는 문제가 있습니다. `locationLoader.find()`을 `bookmarks.map()`안에서 매번 호출하고 있으므로, 인프라 층에서는 북마크의 개수만큼 SQL의 `SELECT`가 발행되어 버리는 것 입니다. 원래는, `locationLoader.findAll()`로 모든 북마크의 대응하는 로케이션을 모아서 취득하면 `SELECT`는 1번으로 끝나는데 말이죠.

이러한 포인트를 염두에 두어, "어떠한 것"과 "어떠한 것"의 관계를 도메인층에서 어떻게 잘 추상화하여, 효율 좋은 구현으로 만들어가는가를 봅시다.

- 이제까지의 문제
  - N+1쿼리 문제
  - 비대화한 모델
- 해결책
  - 해결의 대상의 타입을 한정함
  - 관계 해결의 확장 메서드
- 구현
  - 관계하는 "어떠한 것"을 취득함
  - 관계하는 "어떠한 것"을 이어줌
    - 짝으로 이어줌
    - 필드를 확장함
  - 관계하는 "어떠한 것"이 반드시 있는 경우

## 이제까지의 문제

이제까지도 "어떠한 것"(모델)사이의 관계를 추상적으로 정의한 시도는 많이 있었습니다. 예를들면, Ruby on Rails의 Active Record에는 어소시에이션의 기능이 있습니다. 사내에서는 과거 이용되어온 `DBIx::MoCo`에 닮은 기능이 있습니다. 이러한 방법들은 모델의 관계를 손쉽게 다루는 수단을 제공하고 있습니다만, 몇가지 문제를 갖고 있었습니다.

### N+1 쿼리 문제

관계형 데이터베이스를 사용하여 관계를 해결하는 경우에 공통하는 문제로서 "N+1쿼리 문제"라고 불리는 것이 있습니다. 앞서 말한 예에 있었던 필요 없는 `SELECT`가 발행되어 버리는, 문제가 바로 그것입니다.

앞서의 예에서, 발행되는 SQL의 쿼리를 작성해 봅시다.

```scala
val bookmarks: Seq[BookmarkEntity] = ...
// SELECT * FROM bookmark WHERE ...

val bookmarksWithUrl: Seq[(BookmarkEntity, URL)] =
  bookmarks.flatMap { b =>
    locationLoader.find(b.id.locationId).map((b, _.url))
    // SELECT * FROM location WHERE location_id = $locationId (x N)
  }
```

가장 먼저 북마크의 리스트 취득을 위해서 1회 쿼리가 발행되어, 그 위에 로케이션을 가져오고 있습니다만, 이는 `bookmarks.map()`안에서 실행되는 것이므로 `bookmarks`의 사이즈 N횟수 만큼 반복되어, 결국 쿼리의 발행횟수는 N+1이 됩니다.

로케이션을 가져오는 부분은 원래 다음의 쿼리로 전부 가져올 수 있었으므로, 전체 쿼리의 발행수는 2번으로 끝났어야 합니다

```sql
SELECT * FROM location WHERE location_id IN ($locationIds)
```

RoR의 Active Record나 `DBIx::MoCo`등과 같은 높은 레이어의 OR맵퍼를 사용하면, 실제 쿼리가 너무나도 은폐되어 버려서 이러한 문제를 발견하기 힘들게 됩니다. 특히, 모델에 대한 메서드가 루프 속에서 호출되어 되는지 안되는지, 겉으로 봐서는 구별이 불가능하게 됩니다.

### 비대화 하는 모델

`DBIx::MoCo`등의 이제까지의 방법으로는, 관계의 해결을 위한 메서드를 모델 자신이 갖게 됩니다. 이는 "어떤 관계인지 아는 것은 도메인층"이라는 사상에는 맞습니다만, 그와 동시에 모델으로부터 리포지토리에의 직접 접근을 허용하는 것으로되어, 적어도 두가지의 문제를 낳을 위험이 있습니다.

- 원래 서비스가 행해야 할 역할을 모델이 짊어지게 되는 것에 대한 방지책이 없어짐
- 모델이 상태나 부작용을 갖으며 단독 테스트가 힘들어짐

모델로부터 리포지토리에의(읽기/쓰기) 접근이 가능하게 되면, 그 모델을 인자로 둔 도메인 서비스, 애플리케이션 서비스의 메서드로 구현 해야만 하는 처리를 무엇이든 모델의 메서드로서 구현해버리는 것이 가능하게 됩니다. 이를 방지하기 위해서는, 무엇인가 모델의 메서드가 되어야만 하고, 무엇인가 도메인 서비스나 애플리케이션 서비스의 메서드야 하거나 항상 주의 하여, 잘못된 추상화를 피하지 못하면 리뷰에서 지적할 필요가 있습니다. 그러나 모델은 원래부터 리포지토리 접근을 동반하고 있으므로, 모델이 해도 되는 조작의 구분은 애매하게 되어, 애매한 기준으로 우연히 리뷰를 통과해버려서, 그 뒤의 개발이 파탄나 버리게 됩니다.

- (예시) 매우 거대하게 된 모델
  - 무려 4404줄......

또한, 모델 그 자체가 읽고 쓰기 둘다 조작을 하게 되면, 단독 테스트가 매우 어렵게 됩니다. 예를들면, 어떤 서비스 A의 메서드의 안에 다른 서비스 B에 모델을 넘겨줄 때, A의 단독 테스트를 할 때 B의 안에서 모들의 상태가 변화할 수 있는지 어떤지 주의를 할 필요가 있게 되어버립니다. 혹은, 어떠한 모델을 테스트하기 위해서 테스트 데이터를 넣어두고 싶은경우, 그 모델의 메서드로부터 줄줄이 소세지 식으로 참조될 가능성이 있는 다른 여러가지 모델을 위해서 데이터도 넣어둘 필요가 생겨버려, 대체 어디까지의 범위의 데이터를 준비해 두어야 제대로 테스트가 가능한지 파악하는 것이 곤란하게 됩니다.

- (예시) 광범위한 데이터를 고려로 둔다

하테나 에픽 이후의 프로젝트 에서는, 이러한 문제를 해결하기 위해서 모델을 단순한 불변 오브젝트로서 다루는 수법을 채용 했습니다. 이 프로젝트에서의 엔티티나 값 오브젝트도 이 발상에 따르고 있다고 말할 수 있습니다. 그렇다고는 하나, 모델을 단순한 불변 오브젝트로 하는 것 만으로는, 모델 사이의 관계등 원래 도메인 모델로서 추상화 되어야 하는 것을 방치해버리는 것으로 됩니다.

## 해결책

이 프로젝트에서는 위의 문제들을 대처하기 위해서 두가지 수법을 조합하여 모델 관계의 정의에 이용하고 있습니다.

- 해결 대상의 타입을 한정함
- 확장 메서드에 의한 구현

### 1. 해결 대상의 타입을 한정한다

모델의 단일 인스턴스에 대해서의 관계해결의 메서드를 준비하게 되면, 그것을 루프 안에서 사용하는 것을 막을 수 없으며, 또한, 복수의 인스턴스의 관계해결을 합친 쿼리를 호출하는 것도 당연히 불가능 합니다.*1.

복수의 인스턴스(모델의 인스턴스 리스트등)에 대하여 관계해결만을 생각한다면, 예를들면 다음과 같이 하여, `SELECT ~ WHERE ~ IN`에서 한번에 복수의 로케이션을 갖고오는 `locationLoader.findAll()`메서드를 사용하여, N+1문제를 발생시키지 않고 관계를 해결할 수 있습니다.

```scala
def resolveUrls(bookmarks: Seq[]): Seq[(BookmarkEntity, URL)] = {
  val locations = locationLoader.findAll(bookmarks.map(?.id.locationId))
  // SELECT * FROM location WHERE location_id IN ($locationIds)

  val urlOf: Map[LocationId, Option[URL]] =
    locations.map(l => l.id -> l.url).toMap.lift
  bookmarks.flatMap(b => (b, urlOf(b.id.locationId)))
}

val bookmarks = ...
// SELECT * FROM bookmark WHERE ...

val bookmarksWithUrl: Seq[(BookmarkEntity, URL)] =
  resolveUrls(bookmarks)
```

여기서, 이 프로젝트에서는, **원칙적으로 단일 인스턴스용의 관계 해결의 메서드를 준비하지 않기** 라는  방침을 갖고 있습니다. 이 방침 아래에서는, 단일(개수가 1개) 인스턴스에 대하여 관계 해결하고 싶은 경우는 `Seq()`로 감싸거나 해서, 복수의 인스턴스용 메서드를 호출하게 됩니다.

```scala
val bookmark: BookmarkEntity = ...
val bookmarkWithUrl: Option[(BookmarkEntity, URL)] =
  resolveUrls(Seq(bookmark)).headOption
```

이 방침을 취하고 있는 것에 한해서, N+1쿼리 문제가 생길 것 같은 코드를 작성한 경우는(적어도 국소적인 범위에서는) 다음과 같이 매우 장황한 작성법이 되어서, 잘못된 코드라는 것을 매우 알기 쉬울 것 입니다.

```scala
val bookmarks: Seq[BookmarkEntity] = ...
val bookmarksWithUrl: Seq[(BookmarkEntity, URL)] =
  bookmarks.flatMap { b =>
    resolveUrls(Seq(b))
  }
```

만약 어떻게 해서든 단일 인스턴스에 대하여 관계 해결을 하고 싶으면(복수의 인스턴스용의 효율 좋은 호출 방법이 존재 하지 않으며, 사용할 수도 없는) 경우는, 대상의 타입을 `Seq[]`로 하는 대신에 적어도 `Option[]`으로 해두면 좋겠죠. 이 경우도, 루프 안에서 사용하면 무의미하게 `Option[]`타입으로 할 필요가 생기므로, 잘못된 코드라는 것을 어느정도 알기 쉽습니다.

```scala
val list = ...
list.flatMap { item =>
  resolveSomething(Some(item))
}
```

### 2. 관계 해결의 확장 메서드

관계를 해결하는 메서드를 모델 그 자체의 메서드로 해버리면, 모델의 비대화를 야기 합니다. 애초에, 앞서 봤다시피 복수의 인스턴스를 한꺼번에 해결하는 메서드로 한 경우, 해결의 대상이 모델 그 자체가 아니라 모델의 리스트가 되므로, 모델 그 자체의 메서드를 구현해도 어쩔 수 없다는 사정도 있습니다.

그러므로, 확장 메서드를 사용하는 것으로, 모델이나 그 리스트는 단순한 불변 오브젝트인 특성을 유지하면서, 마치 모델(의 리스트)에 리포지토리 엑세스를 위한 메서드가 추가된 것과 같이 동작 시키는 것이 가능합니다. 이 확장 메서드(의 클래스)는 도메인 서비스의 일종으로 간주하는 것이 가능하며, Cake패턴을 사용하여 도메인 리포지토리나 다른 도메인 서비스에 접근하는 것도 가능합니다.

```scala
package domain
package relation

import types.collection.Unordered

trait BookmarkLocationComponent {
  self: repository.LocationComponent =>

  implicit class BookmarkSeqLocationsRelation(
    bookmarks: Seq[BookmarkEntity]
  ) {
    def toLocations(): Unordered[LocationEntity] =
      locationLoader.findAll(bookmarks.map(_.id.locationId))
  }
}
```

이렇게 해두면, 관계 해결을 위한 리포지토리 접근을 동반하는 곳에서는, `domain.relation.BookmarkLocationComponent`에 의존하고 있는(자기 타입 어노테이션)것이 보증되므로, 관계의 해결이 어디에서 이용되는지가 명확하게 됩니다.

```scala
trait SomeComponent {
  self: domain.relation.BookmarkLocationComponent =>

  def someMethod() = {
    val bookmarks = ...
    val locations = bookmarks.toLocations
  }
}
```

## 구현

### 1. 관계하는 "어떠한 것"을 취득한다

모델 A에 관계하는 모델 B를 취득하는 경우(모델 A가 갖고 있는 모델B를 취득)`toSomething`라는 이름의 메서드를 구현합니다.

- (1) 관계를 정의하는 경우는 컴포넌트를 나눠 둠
  - (이유) 그 편이 유닛 테스트에 필요한 의존이 적게 끝남
- (2) 내부에서는 도메인 리포지토리에 접근하므로 Cake패턴에 따름
- (3) 관계해결의 확장 메서드는
  - `implicit class`에서 정의
  - 이름은 `모델ASeq모델BsRelation`으로 함
    - (이유) `implicit`은 이름이 충돌하면 모호성 해결이 실패하기 때문
- (4) 해결대상의 모델 타입은 `Seq[]`등으로 해 둠
- (5) 관계 해결의 메서드는
  - `to모델Bs`라는 이름으로 함
  - 순서나 전역성을 타입이나 어노테이션에서 명시

```scala
package domain
package relation

import domain.model.bookmark.BookmarkEntity
import domain.model.location.LocationEntity
import types.collection.Unordered

trait BookmarkLocationComponent { // (1)
  self: repository.LocationComponent => // (2)

  implicit class // (3) BookmarkSeqLocationsRelation( // (4)
    bookmarks: Seq[BookmarkEntity]
  ) {
    def toLocations: Unordered[LocationEntity] = // (5)
      locationLoader.findAll(bookmarks.map(_.id.locationId))
  }
}
```

순서나 전역성의 명시 방법은 기본적으로는 리포지토리의 경우와 같습니다. 주의점으로서는, 예를들면 이 예시의 경우, `locationLoader.findAll()`이 데이터베이스에서 갖고 오는 것이라고 하여, "로케이션 테이블에 결손이 없으면 전역함수가 될 것"이라는 전제가 있다고 하더라도, 애플리케이션 코드의 범위 만으로는 논리적으로 전역이라는 것이 확정하지 않으므로, `@total`을 붙여서는 안됩니다(당연히 `locationLoader.findAll()`의 경우도`@total`없이 되어있어야 합니다). 발견되지 않았을 때에 초기값을 반환하고 있는 경우 등, 코드 상에서 전역성이 확실한 경우는 `@total`을 붙입시다.

위의 예시에서는 리포지토리에서 가져온 순서가 없는상태인 채로 반환하고 있으므로, 반환 값은 `Unordered[]`로 되어있습니다. `toLocations`를 사용하는 쪽에서는 순서를 묻지 않는 경우가 있으므로, 정렬하지 않는 것이 바람직합니다. 무엇인가 특별한 이유가 있어서 관계 해결의 대상(여기에서는 `bookmarks`)와 같은 순서로 할 필요가 있는 경우는 `types.collection.Implicits.IterableOps.orderBy`등을 사용합시다. 이하와 같이, 리포지토리로부터 갖고오기 위해서 넘겨준 ID열을 그대로 정렬에 사용함, 과 같은 이디엄을 이용하는 것으로 됩니다.

```scala
@order("preserved")
def toLocations: Seq[LocationEntity] =
  val locationIds = bookmarks.map(_.id.locationId)
  locationLoader.findAll(locationIds).orderBy(locationIds)
```

### 2. 관계하는 "어떠한 것"을 연결한다.

"어떠한 것"이 다른 "어떠한 것"을 갖고 있는 경우에, 그 두가지를 연결해서 취득하고 싶은 경우가 있습니다. 특히, 복수의 인스턴스를 모아서 관계 해결을 하는 경우는, 실제로 관계하고 있는 인스턴스끼리 연결할 필요가 있습니다.

#### 짝으로 연결한다.

예를들어, `BookmarkEntity`에 대응하는 `LocationEntity`를 갖고와서, 그 값(`Location`)을 `BookmarkEntity`에 연결하여 짝으로 하기 위한 메서드 `withLocations`의 정의를 봅시다.

- (1) 다른 어떠한 것과의 관계를 정의하는 경우는 컴포넌트를 분리해 둠
  - (이유) 그 편이 유닛 테스트에 필요한 의존을 적게 만들기 때문
- (2) 내부에서는 도메인 리포지토리에 접근하는 것으로 케이크 패턴에 따라 둠
- (3) 관계 해결의 확장 메서드는
  - `implicit class`로 정의
  - 이름은 `모델ASeq모델BsRelation`으로 함
    - (이유) `implicit`은 이름이 충돌하면 모호성 해결이 실패해버리기 때문
- (4) 해결 대상의 모델 타입은 `Seq[]`등으로 해 둠
- (5) `types.collection.Implicits.IterableOps.join`으로 묶어둠
  - SQL의 `INNER JOIN`에 대응
  - 내부적으로 `Map[]`을 작성
  - `on()`에 따라서 값을 연결함
- (6) `join`의 다음으로 `map()`을 하면 `Stream[]`가 반환된다.
  - `Stream[]`을 반환해두면 `withLocations`의 결과에 대해서 더욱 `join`하는 경우도 효율적

  ```scala
  package boston
  package domain
  package relation

  import domain.model.bookmark.BookmarkEntity
  import domain.model.location.Location

  trait BookmarkLocationComponent {                                  // (1)
    self: repository.LocationComponent =>                            // (2)

    implicit class BookmarkSeqLocationsRelation(                     // (3)
      bookmarks: Seq[BookmarkEntity]                                 // (4)
    ) {
      import types.collection.Implicits.IterableOps                  // (5)

      def withLocations: Stream[(BookmarkEntity, Location)] = {      // (6)
        val locations = locationLoader.findAll(bookmarks.map(_.id.locationId))
        bookmarks
          .join(locations).on(_.id.locationId, _.id)                 // (5)
          .map { case (b, l) => (b, l.value) }                       // (6)
      }
    }
  }
  ```

`withSomethings`는 만약 순서를 묻지 않는다고 해도 원리상 특히 효율화 할 여지가 없으므로, 원칙적으로 (관계 해결의 대상과 같은 순서로)정렬이 끝난 채로 반환하는게 좋겠죠. 원칙은 원래 순서를 유지하는 것이므로, 일부러 `@order`은 적지 않아도 되겠죠(반대로 `withSomethings`이라는 이름으로 다른 순서로 배열해두는 것은 알기 어려우므로 바람직하지 않습니다). 초기값으로 보완하거나 해서, 전역 함수가 되는 경우는 `@total`은 붙입시다.

이 예의 경우, `join`은 연결한 결과를 `bookmarks`와 같은 순서로 반환하므로, `withSomethings`의 순서의 원칙을 만족하고 있습니다. 또한, `join`은 연결하는 요소가 발견되지 않는 경우는 결과로부터 제외하므로, 전역 함수가 되지 못하며, `@total`이 붙지 않습니다.

#### 필드를 확장한다

연결한 것이 여러개 있을 경우, 예를들어 `BookmarkEntity`에 `Location`이나 `DisplayTags`혹은 그 둘을 연결하고 싶은 경우, 짝으로 반환하는 방법으로는 잘 되지 않습니다. 왜냐하면, `Seq[BookmarkEntity]`를 `withLocations`하여 `Seq[(BookmarkEntity, Location)]`으로 한 다음, 또 `withDisplayTags`하려 하면, `withDisplayTags`는 `Seq[(BookmarkEntity, Location)]`의 확장 메서드로서 구현할 필요가 있습니다만, 이렇게 되면 `Location`을 연결하기 전의 `BookmarkEntity`에 대한 `withDisplayTags`도 적용하고 싶어졌을 때에 별도의 확장 메서드로서 구현하지 않으면 안되며, 연결하고 싶은 것이 증가하면 그 조합이 폭발적으로 많은 확장 메서드가 필요하게 됩니다.

이러한 경우, 이 프로젝트에서는 값 오브젝트의 필드를 확장가능으로 하는 것을 권장합니다. `Bookmark`타입이 이 방밥으로 정의 되어 있다고 하면, 엔티티 타입은 어떠한 `B :> Bookmark.Detailed <: Bookmark`에 대하여 `BookmarkEntity[B]`라는 타입으로 표현되며, 이제까지의 `BookmarkEntity`는 `BookmarkEntityT[Bookmark]`에 대응합니다. 값 오브젝트에는 `withLocation()`이라는 setter가 있으며(이는 `domain.relation`상의 관계 해결과는 무관계), 이를 호출하면 `Bookmark with Location.Field`가 반환되어, 설정한 값이 `location`필드로 접근 가능하게 됩니다.

```scala
val bookmark: BookmarkEntity = ...
val location: LocationEntity = ...

// object Location { trait Field { val location: Location } }
val bookmark2: BookmarkEntityT[Bookmark with Location.Field] =
  bookmark.mapValue(_.withLocation(location.value))
bookmark2.location // OK
```

이를 사용하면 확장성이 높은 연결 정의를 구현할 수 있게 됩니다.

- (1) `Bookmark.Detailed`와 `Bookmark`사이의 타입의 엔티티에 대한 setter도 준비해 둠
- (2) 값 오브젝트에서가 아닌, 엔티티에 대한 setter도 준비해 둠
  - 이는 부작용이 없으므로 단일 엔티티에 대한 메서드로 괜찮음
- (3) 관계의 정의에서는 결과의 타입은 원래 값의 타입으로 부터의 관계하는 필드가 증가한 것이 됨

```scala
package domain
package relation

import domain.model.bookmark.{Bookmark, BookmarkEntityT}
import domain.model.location.Location

trait BookmarkLocationComponent {
  self: repository.LocationComponent =>

  implicit class BookmarkLocationRelation[B >: Bookmark.Detailed <: Bookmark](
    bookmark: BookmarkEntityT[B]                                   // (1)
  ) {
    def withLocation(                                              // (2)
      location: Location
    ): BookmarkEntityT[B with Location.Field] =
      bookmark.mapValue(_.withLocation(location))
  }

  implicit class BookmarkSeqLocationsRelation[B >: Bookmark.Detailed <: Bookmark](
    bookmarks: Seq[BookmarkEntityT[B]]                             // (1)
  ) {
    import types.collection.Implicits.IterableOps

    def withLocations: Stream[BookmarkEntityT[B with Location.Field]] = {
                                                                   // (3)
      val locations = locationLoader.findAll(bookmarks.map(_.id.locationId))
      bookmarks
        .join(locations).on(_.id.locationId, _.id)
        .map { case (b, l) => b.withLocation(l.value) }            // (2)
    }
  }
}
```

```scala
package domain
package relation

import domain.model.bookmark.{Bookmark, BookmarkEntityT, DisplayTags}

trait BookmarkDisplayTagsComponent {
  self: repository.BookmarkComponent =>

  implicit class BookmarkDisplayTagsRelation[B >: Bookmark.Detailed <: Bookmark](
    bookmark: BookmarkEntityT[B]                                   // (1)
  ) {
    def withDisplayTags(                                           // (2)
      displayTags: DisplayTags
    ): BookmarkEntityT[B with DisplayTags.Field] =
      bookmark.mapValue(_.withDisplayTags(displayTags))
  }

  implicit class BookmarkSeqDisplayTagsRelation[B >: Bookmark.Detailed <: Bookmark](
    bookmarks: Seq[BookmarkEntityT[B]]                             // (1)
  ) {
    def withDisplayTags: Stream[BookmarkEntityT[B with DisplayTags.Field]] =
      ...                                                          // (3)
  }
}
```

위의 코드를 사용하면 `withLocations`와 `withDisplayTags`의 어느쪽을 먼저 호출해도 같은 타입의 엔티티가 반환됩니다.
(Bookmark with Location.Field with DisplayTags.Field)와 (Bookmark with DisplayTags.Filed with Location.Field는 구별되지 않습니다)

```scala
val bookmarks: Seq[BookmarkEntityT[Bookmark]] = ...

val bookmarks1: Seq[BookmarkEntityT[Bookmark with Location.Field with DisplayTags.Field]] = bookmarks.withLocations.withDisplayTags
val bookmarks2: Seq[BookmarkEntityT[Bookmark with DisplayTags.Field with Location.Field]] =
  bookmarks.withDisplayTags.withLocations
```

### 3. 관계하는 "어떠한 것"이 반드시 있는 경우

기점으로 되는 "어떠한 것"으로 부터 관계하는 "어떠한 것"을 얻을 수 없을경우, 초기 값을 주는 것으로 관계 해결을 전역함수로 하는 것이 가능합니다. 이제까지 `orderBy()`나 `join()`을 사용하고 있었던 곳을 `totallyOrderBy`나 `leftJoin`을 사용하도록 하면, 초기값을 지정하여 간단히 전역 함수로 작성하는 것이 가능합니다.

```scala
@total
def withDisplayTags: Stream[BookmarkEntity[B with DisplayTags.Field]] = {
  val tags = BookmarkDisplayTagsLoader.findAllByBookmarks(bookmarks)
  val default = DisplayTagsEntity.default
  bookmarks
    .leftJoin(tags).on(_.id, _.id.parentId)(default)
    .map { case (b, t) => b.withDisplayTags(t.value) }
}
```

*1 : 一つのインスタンスに対する関係解決のメソッドをふつう通り使ったまま複数インスタンス用の効率的なクエリを発行する目的で, 以前は関係解決の部分をモナド(bullet-scala)にしていました. このモナドでは, クエリの発行がループを抜けるまで遅延させられるので, N+1問題が解決できました. しかし, モナドの扱いが難しく, 関係の定義も煩雑になるため廃止されました.
