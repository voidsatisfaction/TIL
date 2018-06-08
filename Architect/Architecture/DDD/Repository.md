# 리포지토리의 정의와 구현

시스템 안에서 오브젝트의 영속화(永続化)를 추상한 서비스가 리포지토리 입니다. 리포지토리는 외견상은 컬렉션 처럼 동작하여, 인터페이스 정의는 도메인 층에, 구현은 인프라스트럭처 층에 놓여집니다.

- 목차
  - 리포지토리의 분류
  - 인터페이스
    - 부트스트랩과 액션
    - 로더
  - 구현

## 리포지토리의 분류

리포지토리의 역할을 더욱 세분화 하면 부트스트랩(Bootstrap), 액션(Action), 로더(Loader)로 나눈 것이 가능합니다.

- 부트스트랩
  - 오브젝트를 시스템안에 새로 생성하는 조작을 위한 인터페이스
  - 전형적으로는 `findOrCreateBy*()`를 갖음
- 액션
  - 오브젝트를 갱신 / 삭제 조작을 위한 인터페이스
  - 전형적으로는 `add()`나 `delete()`를 갖음
- 로더
  - 오브젝트의 취득조작을 위한 인터페이스
  - 전형적으로는 `find()`나 `findBy*()`, `findAllBy*()`를 갖음

액션과 로더를 합치면 추가 / 취득 / 삭제가 가능한 컬렉션 타입이라고 생각할 수 있다는 것을 알 수 있습니다. 필연적으로, 액션의 매개변수나 로더의 반환값은 엔티티(그 자체나 그 리스트 등)로 되게 됩니다.

여기서 리포지토리 인터페이스를 호출하는 장소에 대해서 주목해 봅시다. 부트스트랩과 액션의 메서드는 시스템의 상태를 바꾸는 조작으로, 비지니스 로직으로서 애플리케이션층으로부터 호출하는 것은 자연스럽지만, 도메인층에서는 주의가 필요합니다. 예를들면, 모델의 내용을 읽는 메서드의 안에 부트스트랩이나 액션을 조작하는 것은 명백하게 이상하죠. 도메인 서비스가 갖는 도메인의 상태변경을 표현한 메서드의 내부에서 호출하는 것은 부자연스럽지 않지만, 그 경우는 이 도메인 서비스의 메서드가 기본적으로는 애플리케이션층에서 호출되도록 해야하며, 도메인층에서 호출하는 것은 주의가 필요합니다. 즉, 도메인층 에서는 도메인의 상태를 변경하는 메서드와, 그렇지 않은 메서드를 명확히 구분해야만 합니다. 이 프로젝트에서는 부트스트랩과 액션에 관해서는 도메인층에서 자유롭게 호출할 수 없으며, 부작용을 발생시킨다는 것을 명시하지 않으면 안되도록 합니다. 도메인쪽에서 이러한 움직임을 구현하기 위해서 는 도메인 액션 에서 자세히 다룹니다.

반면, 로더는 보통 인프라스트럭처 층에서 데이터베이스 등을 사용하여 부작용이 있는 처리로서 구현됩니다만, 인터페이스로서 추상화 해서 생각하면, 혹은 인프라스트럭처층 에서의 구현이 메모리상에서 완결될 수 있도록 작성되어있는 경우를 생각하면, 부작용이 없는 읽기 전용 조작으로서 간주할 수 있습니다. 이는 가변 컬렉션의 취득조작이 불변 조작에서 실현 가능하며, 갱신 조작은 부작용을 불러일으키는 것(Unit을 반환)에 대응합니다. 다시 말하자면, 로더에는 도멘에의 부작용이 없다는 것입니다.

부트스트랩과 액션은 어느쪽도 부작용이 있는데도 따로 나누는 이유는, 이 분리가 CQS(Command Query SeParation)을 하고 있기 때문입니다. CQS데서의 커맨드는 원칙으로서 값을 반환하지 않는 부작용만으로 구성된 조작입니다. 그렇기 때문에, 부작용과 값의 취득을 동시에 할 필요가 있는 부트스트랩은 커맨드와는 다른 특별한 존재가 됩니다. 그에 반하여 액션과 로더는 CQS원칙에 따른 커맨드와 쿼리 그 자체로 되어있습니다.

이와같이 커맨드와 쿼리의 분리를 하는것은, 보다 큰 시스템레벨에서의 CQRS(Command Query Responsibility Segregation)에 대응하기 위함도 있습니다.

## 인터페이스

로케이션의 리포지토리를 예를 들어서 실제 인터페이스 정의를 봅시다.

### Bootstrap과 액션

부트스트랩이나 액션의 인터페이스는 같은 파일에 기술되어있어도 상관 없습니다(물론 길어지면 나눠도 좋습니다) 인터페이스의 구현은 인프라스트럭처층에 배치됩니다만, 도메인층으로부터 인프라층에 의존해서는 안되므로, 의존 관계 역전 원칙에 따라서 인프라층에서 도메인층에 의존하도록 합니다. 레이어를 넘나드는 큰 의존성을 주입하는 것이므로 케이크 패턴을 사용하게 됩니다.

```scala
package boston
package domain
package repository

import model.location.{LocationEntity, LocationId}
import model.url.URL

trait LocationComponent { // (1)
  def locationBootstrap: LocationBootstrap // (1)
  def locationAction: LocationAction // (1)

  trait LocationBootstrap {
    def findOrCreateByURL(url: URL)(implicit // (2)
      runner: domain.action.Runner // (4)
    ): LocationEntity
  }

  trait LocationAction {
    def add(location: LocationEntity)(implicit // (3)
      runner: domain.action.Runner // (4)
    ): Unit
  }
}
```

케이크 패턴에 따라서, 리포지토리 인터페이스를 컴포넌트로 감싸, 인터페이스를 만족하는 리포지토리 인터페이스를 돌려주는 메서드를 준비해 둡니다.(1) **(나중에 교체하기 쉽게 하기 위해서 이렇게 컴포넌트 랩퍼를 사용함)**

부트스트랩의 인터페이스에서는 `findOrCreateBy*()`메서드가 엔티티를 반환하도록 합니다. 이 메서드를 호출하기 까지 엔티티는 존재하지 않으므로, 매개변수에는 엔티티를 구성하는 프로퍼티를 지정하게 되어있습니다(2) 기본적으로는 인자로 주어지는 것이 그대로 엔티티의 값으로 구성되므로,  **`findOrCreateBy*()`의 가장 중요한 역할은 엔티티의 ID를 새로 붙여주는 것** 입니다.

액션의 인터페이스에서는, 인자로는 엔티티를 지정하여, 부작용을 발생시키는 컬렉션 조작으로서 표현하고싶으므로 반환값은 `Unit`타입이 됩니다(3) `add()`는 지정된 엔티티가 어찌되었든 그 값을 갖도록 하는 조작이며, 과거에 같은 ID의 엔티티가 있다면 값을 덮어쓰며, 아직 시스템상에 없다면 신규로 작성합니다. 부트스트랩의 `findOrCreateBy*()`와의 차이는 `add()`하기 위해서는 엔티티의 ID를 이미 알고있지 않으면 안된다는 점 입니다. 서브엔티티의 경우에도 주된 엔티티로부터 차용한 ID만 필요한 경우에는, ID는 처음부터 알고있으므로 Bootstrap의 `findOrCreateBy*()`는 필요없으므로, 즉시 `add()`가 가능하게 됩니다. 주 엔티티의 경우는, ID를 부여가능한것은 `findOrCreateBy*()`뿐 이므로 `add()`는 항상 갱신 조작으로 됩니다.

부트스트랩, 액션 전부 도메인에의 부작용을 수반하므로, 그것을 `domain.action.Runner`타입의 암묵 매개변수에 의하여 명시합니다 (4) `domain.action.Runner`의 인스턴스는 도메인층에는 의존하지 않으므로, 이러한 메서드를 호출하는 메서드가 도메인층에 있다고 하면, 그 메서드도 역시 `domain.action.Runner`를 인자로 받게 됩니다. 자세히는 또, 도메인 액션 장에서 다룰 것이므로, 여기서는 부트스트랩이나 액션 메서드는 `domain.action.Runner`타입의 암묵 인자를 받아야만 한다는 것을 기억합시다.

### 로더

다음으로는 로더의 정의 입니다. 부트스트랩이나 액션과 같은 파일에 배치되어 있어도 상관은 없습니다만, 알기 쉽게 하기 위해서 다음의 예에서는 로더에 대해서만 작성합니다. 구현은 역시 인프라스트럭처 층에 놓이므로 케이크패턴을 사용합니다.

```scala
// domain/repository/Location.scala
package boston
package domain
package repository

import model.location.{LocationEntity, LocationId}
import model.url.URL
import types.collection.{NonEmpty, Unordered}

trait LocationComponent {             // (1)
  def locationLoader: LocationLoader  // (1)

  trait LocationLoader {              // (2)
    def find(locationId: LocationId): Option[LocationEntity]
    def findByURL(url: URL): Option[LocationEntity]
    def findAll(locationIds: Option[NonEmpty[LocationId]]): Unordered[LocaitonEntity]
    def findAllByURLs(urls: Option[NonEmpty[URL]]): Unordered[LocaitonEntity]
  }
}
```

케이크 패턴에 따라서, 리포지토리 인터페이스를 컴포넌트로 감싸, 인터페이스를 만족하는 리포지토리 인터페이스를 반환하는 메서드를 준비해둡니다(1)

로더의 인터페이스 정의(2)에서는, 엔티티를 반환하는 `find*()`메서드를 정의해 둡니다. 단일 요소를 반환하는 경우는(발견되지 않는 경우를 고려하여)보통 `Option[]`으로 감싼 엔티티 타입을 반환합니다. 복수의 요소를 리스트 등의 컬렉션으로 반환하는 경우는, 발견되지 않는 요소는 포함하지 않도록 하면 좋으므로, `Option[]`일 필요는 없습니다.

인자는 엔티티를 특정할 수 있는 것이라면 무엇이든 상관없습니다만, `By`가 붙지않은 `find()`는 엔티티의 아이디 타입을 요구하도록 합니다. 인자로서의 리스트를 요구하는 경우, 빈 리스트와 그렇지 않은 경우를 분명히 구별할 수 있도록 `Option[NonEmpty[]]`를 요구하도록 하면 편리합니다. 예를들면, `Option[NonEmpty[URL]]`에 `Seq(URL("http://example.com"))`을 반환하면 자동적으로 `Some(NonEmpty(URL("http://example.com")))`으로 변환되어 인자로 넘겨져, `Seq.empty`를 넘겨주면 `None`으로 변환되어 넘겨지게 됩니다.

로더는 도메인에의 부작용이 없는 리포지토리 인터페이스이므로, `find*()`메서드는 `domain.action.Runner`타입의 인자를 필요로 하지 않습니다.

반환값이 컬렉션인 경우, 순서에 의미가 있는가에 따라서 컬렉션 타입을 이하와 같이 나눕니다.

- `Seq[], Stream[], Vector[]`
  - 순서가 있고 중복 허용 컬렉션 타입
- `SeqSet[]`
  - 순서가 있고 중복은 허용하지 않는 컬렉션 타입
- `Unordered[]`
  - 순서에 의미가 없는 경우 사용
- `Set[]`
  - 순서에 의미가 없고, 요소에 중복을 허용하지 않는 경우

인자와 반환값의 관계를 나타내기 위해서 다음과 같은 어노테이션을 사용합시다.

- `@total`
  - 메서드가 전역함수일 경우(`map()`과 같은 동작) 사용
- `@order(how)`
  - 반환값의 컬렉션이 어떤 순서로 되어있는가
  - e.g
    - `@order("preserved")`
      - 인자의 컬렉션의 순서를 보존
    - `@order("created DESC")`
      - created필드를 기준으로 내림차순
    - `@order("created DESC, locationId DESC")`
      - created필드를 기준으로 내림차순으로 하고 같은 값이 있는경우는 `locationId`의 내림차순

## 구현

리포지토리의 구현은, 디비나 엘라스틱서치등 사용하는 미들웨어 마다 나눠서 인프라스트럭처 층에 둡니다. 하나의 리포지토리 인터페이스에 대응하여 내부에서 복수의 미들웨어를 나눠서 사용하는 경우는, `infrastructure`이름공간 바로 밑에 모든것을 통괄하는 리포지토리 컴포넌트를 두어, 그 컴포넌트가 각 미들웨어마다의 컴포넌트(`infrastructure/db`나 `infrastructure/es`에 두어진 것)에 의존하는 형태로 합니다. 단일 미들웨어만 사용하는 경우는 직접 그 미들웨어의 이름공간에 둡니다.

부트스트랩, 액션, 로더는 각각의 컴포넌트/리포지토리 클래스에서 구현하는 것도 가능합니다만, 예를들면 부트스트랩안에서 로더의 메서드를 호출하는 등, 구현상 서로 강하게 관련될 것이므로, 코드가 너무 길어지게 된다면 모두를 하나의 컴포넌트 / 리포지토리에 구현 해버리는 것도 좋겠죠

여기서는 디비(MySQL)을 사용한 로케이션 리포지토리를 예로, 구현방법을 봅니다. 이 리포지토리 구현에서는 세가지 리포지토리 인터페이스를 단일 클래스로 구현합니다.

- (1) `infrastructure.db`이름 공간에 둠
- (2) 케이크 패턴에 따름
  - (3) 의존하는 다른 컴포넌트를 자기타입 어노테이션으로 명시
  - (4) 리포지토리 인터페이스의 인터페이스를 반환함
- (5) 데이터베이스를 사용하는 경우는 그것 전용의 `Handler`를 사용함
  - (5) `DB()`메서드나 `TableName`이나 SQL보간자를 사용함
  - (6) 쿼리 결과로부터 타입에의 매핑 정의가 가능하게 됨
- (7) 부트스트랩을 구현
- (8) 액션을 구현
- (9) 로더를 구현

```scala

// infrastructure/db/Location.scala
package boston
package infrastructure
package db                                                         // (1)

import application.OperationFailure
import com.hatena.db.DB
import domain.model.location.{LocationEntity, LocationId, Location}
import domain.model.url.URL
import types.collection.NonEmpty

trait LocationComponent                                            // (2)
    extends domain.repository.LocationComponent {                  // (2)
  self: DB.InstanceProvider with IdGeneratorComponent =>           // (3)

  def locationAction: LocationAction = LocationDB                  // (4)
  def locationLoader: LocationLoader = LocationDB                  // (4)
  def locationBootstrap: LocationBootstrap = LocationDB            // (4)

  trait LocationDB extends Handler with Synced                     // (5)
      with LocationBootstrap                                       // (4)
      with LocationAction                                          // (4)
      with LocationLoader {                                        // (4)
    def db = DB('boston)                                           // (5)
    val table = TableName("location")                              // (5)

    implicit val getLocationResult = getResult { LocationEntity(   // (6)
      LocationId(column("location_id")),
      Location(column("url"))
    ) }

    private def create(locationId: LocationId, location: Location): Int =
      db.master.run {                                              // (5)
        sqlu"""
        | INSERT INTO $table (location_id, url)
        | VALUES ($locationId, ${location.url})
        | ON DUPLICATE KEY UPDATE location_id = location_id
        |"""
      }

    def findOrCreateByURL(url: URL): LocationEntity = {            // (7)
      val value = Location(url)
      findByURL(url).getOrElse { withReadWriteSync {
        val locationId = LocationId(idGenerator[Location])
        create(locationId, value) match {
          case 1 => LocationEntity(locationId, value)
          case _ => findByURL(url).getOrElse {
            val l = s"($locationId, $value)"
            throw new OperationFailure(s"Failed to update a location: $l")
          }
        }
      } }
    }

    def add(location: LocationEntity): Unit =                      // (8)
      create(location.id, location.value)

    def find(locationId: LocationId): Option[LocationEntity] =     // (9)
      findAll(Some(NonEmpty(locationId))).headOption

    def findByURL(url: URL): Option[LocationEntity] =              // (9)
      findAllByURLs(Some(NonEmpty(url))).headOption

    def findAll(                                                   // (9)
      locationIds: Option[NonEmpty[LocationId]]
    ): Unordered[LocationEntity] =
      locationIds match {
        case Some(locationIds) => db.run {                         // (5)
          sql"""
          | SELECT * FROM $table
          | WHERE location_id IN ($locationIds)
          |""".as[LocationEntity]
        }
        case None => Seq.empty
      }

    def findAllByURLs(                                             // (9)
      urls: Option[NonEmpty[URL]]
    ): Unordered[LocationEntity] =
      urls match {
        case Some(urls) => db.run {                                // (5)
          sql"""
          | SELECT * FROM $table
          | WHERE url IN ($urls)
          |""".as[LocationEntity]
        }
        case None => Seq.empty
      }
  }
  object LocationDB extends LocationDB                             // (4)
}

```

세가지의 인터페이스의 구현을 하나에 합쳐놓는 것으로, `create()`를 부트스트랩과 액션으로 `findByURL()`을 부트스트랩과 로더로 재사용할 수 있도록 되었다.

인프라층에서도 리포지토리 인터페이스에서 지정한 어노테이션은 동일하게 지정하도록 하자.

데이터베이스를 시작해서 각 미들웨어의 자세한 사용법은 공식 문서 참조
