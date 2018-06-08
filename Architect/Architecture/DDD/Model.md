# 모델

- 목차
  - 값의 표현
    - 값 오브젝트
    - 태그 붙은 단순 값
  - 엔티티
    - ID
    - 엔티티의 표현
    - 서브엔티티
    - 복합ID를 갖는 엔티티
    - 작성갱신일시를 갖는 엔티티
  - 모델에 대한 조작
  - 요약

## 모델의 정의

유저나 URL, 북마크 아이템을 나타내는 모델을 예로, 값 오브젝트나 엔티티를 정의하는 방법을 보자.

### 값의 표현

어떠한 "것"을 값으로 표현할 때에는 단순한 값(내장 타입)이나 값 오브젝트로 표현함

#### 값 오브젝트

값 오브젝트는 "어떠한 것의 내용"을 자세하게 나타내기 위한 속성을 갖는 오브젝트로, "그것"이 실제로 존재하는가는 신경쓰지 않고, 내용이 같다면 같은 것으로 취급합니다. 예를들어, 단순한 수치를 "어떠한 것의 내용"으로 다루는 경우는 당연한 것으로, "어떠한 것의 내용"을 나타내는 자세한 속성을 갖는다고 해도 동일합니다.

일반적으로는 값 오브젝트의 속성의 내부도 또 단순한 값이나 값 오브젝트로 되어있습니다. 스칼라의 `case class`는 `==`가 동일성이 아닌, 동치성(同値性)을 확인하는 것으로 되어 있으며, 네스팅되어 있는 구조의 동치성도 판정할 수 있으므로 값 오브젝트를 표현하기 위해서 매우 적절하다고 할 수 있습니다.

예를들면, 유저를 나타내는 `User`와 어떠한 URL을 갖는 장소(웹 페이지 등)를 나타내는 `Location`을 정의해 봅시다. 이러한 인스턴스는 속성 값이 같다면 인스턴스 그 자체도 같다고 여길 수 있는 오브젝트 입니다.

```scala
case class User(name: String, privacy: User.Privacy = 'public) {
  def isPublic(): Boolean = privacy == 'public
}
object User {
  type Status = Symbol
}

case class Location(url: String)
```

```scala
// 사용 예
val user1 = User("tarao")
val user2 = User("ikura", 'private)
val user3 = User("tarao", 'public)

user1 == user2 // false
user1 == user3 // true
```

`isPublic()`과 같이, 속성값 만으로 계산가능한 단순한 메서드도 값 오브젝트에 갖게 할 수 있습니다. 반대로, DB조작을 동반하는 처리등, 값 그 자체의 표현의 범주를 넘는 메서드를 추가하는 것은 좋지 못합니다.

```scala
user1.isPublic // true
user2.isPublic // false
```

#### 태그가 붙은 단순한 값

`User`와 `Location`은 어느쪽이든, 속성으로서는 단순한 값 만을 갖고 있으며, 그 타입은 어느쪽이든 내장 타입입니다만, 단순한 값에 독자적으로 정의한 타입을 사용하고 싶은 경우도 있습니다. 독자적으로 정의한 타입이 `case class`로 충분하다면 다음과 같이 정의하면 됩니다만, 이것만으로는 URL을 사용할 때마다 오브젝트가 하나씩 생성되어 버려, `String`을 그대로 사용한 경우에 비교하여 메모리 효율이 매우 나빠 집니다.

여기서는, 실체는 `String`이기는 하나, 독자적으로 정의한 타입으로서 사용할 수 있는 새로운 타입을 **타입 태그** 를 사용해서 정의 합니다. 이 프로젝트에서는 `domain.model.Value[]`를 사용하면 태그가 붙은 값을 간단히 정의 가능합니다. `Value[]`는 두개의 타입 매개변수를 받으며, 첫번째로 실체의 타입, 두번째로는 독자 정의한 타입으로 호출 가능한 확장 메서드를 정의한 클래스를 지정합니다.

```scala
type URL = Value[String, ops.URL]

val URL: String => URL = Value.apply _
```

이와같이, 독자적으로 정의한 단순한 값의 타입은 실체의 타입(URL의 경우는 String)에 정의되어있는 메서드를 포함하여, 어떠한 조작도 불가능한 타입이 되어 버립니다(예외는 Any에 대해서 할 수 있는 것들만). 그 자체에는 어떠한 조작도 정의되지 않아있기 때문에, 독자 정의의 타입에 대해서 조작하는 것은 확장 메서드로서 제공할 필요가 있습니다.

```scala
package ops {
  case class URL(url: String) extends AnyVal {
    // 여기에 정의한 메서드가 URL타입에서 사용 할 수 있음
    def host(): String = ???
  }

  object URL {
    // 이는 마법의 주문(ops.URL에 정의된 조작을 유효화 하기 위해서 필요)
    implicit val stringToUrlOps: String => URL = apply _
    implicit val urlToOps: model.url.URL => URL = Value.toOps _

    // 이하는 URL을 String으로서 다루고 싶을 때에만 필요
    implicit val unwrapURL: model.url.URL => String = Value.unwrap _
  }
}
```

이 확장 메서드를 이용하기 위해서는 명시적인 `import`가 필요합니다.

```scala
val location: Location = ...
// val host = location.url.host // 컴파일 에러

import ops.URL._
val host = location.url.host
val len = location.url.length // unwrapURL이 정의된 경우에만 가능
```

- `implicit`의 값의 이름은 다른 이름들과 겹치지 않도록 주의
  - 다른 `Value[]`용의 `implicit`이 같은 스코프에 `import`될 가능성이 있음
  - 너무나도 일반적인 이름을 붙이면 `import`하는 곳에서의 메서드등을 숨겨버릴 위험성이 있음

### 엔티티

엔티티는 실제로 시스템상에 존재하는 "무엇인가"을 표현합니다. "그 무엇"을 표현하는 값(단순한 값 혹은 값 오브젝트)를 시스템 안에서 식별 가능하도록 한 것입니다. 엔티티로서 각각의 것은 그 내용이 우연히 일치해도 다른 것으로 생각합니다. 또한 엔티티로서 동일한 것은, 그 상태가 변화하기 전과 후에 메모리상의 표현이 다르다고 해도, "그 무엇"으로서는 동일하게 취급됩니다. 이는 즉, 엔티티는 값과 그 유일함을 나타내는 일관적인 ID와의 짝으로 표현되는 것입니다.

#### ID

엔티티의 ID를 예를들면 단순한 수치로서 다루게 되면, 전혀 관계없는 수치(예를들면 무엇인가의 개수)를 엔티티의 ID로 오해하여 사용할 수 있으므로, ID는 그 엔티티의 값의 유일함을 표현할 수 있는 전용의 것을 정의 합니다.

보통 엔티티의 ID는 DB의 레이어에서는 주키(primary key)에 대응됩니다. DB의 주 키가 `BIGINT`일 경우에는 이 프로젝트에서는 `domain.model.UUID`를 사용하면 되도록 되어있으므로, 이 타입을 지금 정의하려고 하는 엔티티(의 값)의 타입에 특화한 것으로 되도록 태그를 붙입니다. 이는 `domain.model.Entity.Id[]`로 간단히 가능합니다. `Entity.Id[]`는 두개의 매개변수를 받으며, 첫번째는 실체의 타입, 두번쨰는 특화하고 싶은 값의 타입을 지정합니다. `type`으로 ID타입을, `val`로 ID타입의 팩토리를 만듭니다.

#### 엔티티의 표현

엔티티는 여기까지 봐 왔던 ID와 값(단순한 값 혹은 값 오브젝트)를 사용하여 `domain.model.Entity[]`를 통하여 정의합니다. `Entity[]`는 두개의 타입 인자를 받아, 첫번째에 ID타입, 두번째에 값 타입을 지정합니다. ID의 경우와 같이, type에서 엔티티 타입을 `val`로 엔티티타입의 팩토리를 만듭니다.

```scala
type UserEntity = Entity[UserId, User] // 엔티티 타입
val UserEntity = Entity[UserId, User] // 팩토리

type LocationEntity = Entity[LocationId, Locaiton]
val LocationEntity = Entity[LocationId, Location]
```

```scala
// 사용 예
val user = UserEntity(UserId(12345L), User(name = "tarao", privacy = 'private))
```

엔티티의 ID타입은 엔티티의 값의 타입과 호환성이 있는 것이어야 만 합니다. 즉, 다음과 같은 것은 컴파일 에러가 납니다.

```scala
type LocationEntity = Entity[Long, Location] // 컴파일 에러
type LocationEntity = Entity[UserId, Location]
```

Entity.Id[]를 사용해서 정의한 ID타입은, 값의 타입이 일치하는 엔티티의 ID타입으로서만 사용할 수 있습니다.

#### 서브엔티티

엔티티의 ID타입과 값의 타입은 평소에는 1대1 대응입니다만, 가끔씩은 같은 ID타입에 다른 값의 타입을 대응하는 엔티티를 만들고 싶어지는 경우가 있습니다.

이것은 DB레이어에서는 같은 주키를 갖은 다른 테이블을 정의하고 싶은 경우에 대응합니다. 이러할 경우, DB레이어에서는 나중에 생긴 테이블에서는(실제로는 그렇게 되는지는 별개로 논리적으로는) 외부키로서 다른 테이블의 주 키를 사용하는 것으로 됩니다.

도메인 모델에서는, 다른 엔티티의 ID타입을 차용하는 쪽에서 서브엔티티로서 구별되어, 주종관계를 확실하게 합니다.

서브 엔티티의 정의의 방식은, ID의 정의에 `Subentity.Id[]`를 사용하는 것 이외에는 엔티티의 경우와 동일합니다.

```scala
// 주 엔티티 정의
case class Entry(url: URL)

type EntryId = Entity.Id[UUID, Entry]
val EntryId = Entity.id[UUID, Entry]

type EntryEntity = Entity[EntryId, Entry]
val EntryEntity = Entity[EntryId, Entry]

// 보조 엔트리 정의
case class Content(title: String, body: String)

type ContentId = Subentity.Id[EntryId, Content]
val ContentId = Subentity.Id[EntryId, Content]
type ContentEntity = Entity[ContentId, Content]
val ContentEntity = Entity[ContentId, Content]
```

```scala
// 사용 예
val entry: EntryEntity = ...
val content = ContentEntity(
  ContentId(entry.id),
  Content("some title", "some body")
)
```

#### 복합ID를 갖는 엔티티

ID가 다른 엔티티의 ID의 조합으로부터 될 수 있는 엔티티도, 서브엔티티의 한 종류입니다. 이는 DB레이어에서는 주키가 복합키인 경우와 같은 테이블에 대응합니다.

엔티티의 ID가 복합ID가 될 경우는, `Entity.Id[]`로 정의하는 것이 아니라, `case class`로 정의하는 편이 편리합니다. 이러한 경우, 그 ID타입이 특정 값을 위한 것을 `extends Subentity.CompoundId[값의 타입]`으로 지정합니다. `Subentity.CompoundId`를 계승한 `case class`를 ID타입으로 사용하는 점을 제외하면, 평범한 엔티티의 정의 방식이랑 같습니다.

```scala
case class Bookmark(comment: String) // 값 오브젝트

case class BookmarkId(userId: UserId, locationId: LocationId) extends Subentity.CompoundId[Bookmark]

type BookmarkEntity = Entity[BookmarkId, Bookmark]
val BookmarkEntity = Entity[BookmarkId, Bookmark]
```

```scala
// 사용예
val user: UserEntity = ...
val location: LocationEntity = ...
val id = BookmarkId(user.id, location.id)
val bookmark: BookmarkEntity = BookmarkEntity(id, Bookmark("some comment"))
```

#### 작성갱신일시를 갖는 엔티티

엔티티에 작성일시나 갱신일시의 정보를 포함하고 싶은 경우, 엔티티의 값에 포함되면 자연스럽지 않은 경우가 있습니다. 왜냐하면, 작성일시는 시스템상에 존재하는 "어떠한 것"이 생겨난 시간을 나타낸 것일뿐, 이것은 개념상의 값이 가지는 속성이 아닌 실제로 존재하는 유일하게 식별되는 "어떠한 것"으로서의 속성이기 때문입니다. 이러한 경우는, 작성 갱신일시를 갖을 수 있도록 한`Entity.Timed[]`를 `Entity[]`의 대신 사용하는 것이 가능합니다.

```scala
type BookmarkEntity = Entity.Timed[BookmarkId, Bookmark]
val BookmarkEntity = Entity.Timed[BookmarkId, Bookmark]
```

`Entity.Timed[]`를 사용한 경우, 팩토리는 ID와 값 외에 작성일시(`created`)와 갱신일시(`updated`)를 지정할 수 있습니다. 갱신일시나 작성일시는 생략 가능하며, 갱신일시를 생략한 경우는 작성일시와 같게되어, 작성일시도 생략한 경우는 어느쪽도 현재시간이 사용됩니다.

```scala
// 사용 예

val id: BookmarkId = ...
val b: Bookmark = Bookmark("some comment")

val bookmark1 = BookmarkEntity(id, b, created = DateTime.now)
val bookmark2 = BookmarkEntity(id, b) // 위와 같음
```

### 모델에 대한 조작

값 오브젝트에 대한 조작은, 케이스클래스안에 메서드를 준비하면 되는 것은 이미 본 대로입니다. 반면, 엔티티에 메서드를 갖게 하는 경우, 엔티티는 타입 에이리어스(型エイリアス)이므로 직접 메서드를 갖지 않으므로 다른 방법이 필요합니다.

예를들어 다른 인스턴스나 타입의 엔티티를 돌려주는 메서드를 엔티티가 갖도록 하고싶은 경우도 있습니다. 선택 필드를 채운 엔티티 인스턴스를 돌려주거나, 다른 종류의 엔티티로 변환하거나 하는 경우 입니다. 이러한 경우, 단순히 값 오브젝트의 메서드로서 갖도록하는 것은 불가능 하도록 불변 메서드를 모델에 준비하고 싶은 경우에는 확장 메서드를 사용합니다.

유저의 이름을 변경하는 메서드 `renameTo()`를 예를 들어 봅시다. 이 메서드는 `Setter`클래스에 정의하는 것으로 합시다. 엔티티의 값을 바꾸기 위해서는 `mapValue()`메서드를 사용합니다. `mapValue()`에 전달된 블록에서는 엔티티의 원래 값을 받아, 새로운 값을 반환합니다. 여기에서는 유저 엔티티의 값은 값오브젝트에서, 케이스 클래스로서 구현되지 않으므로, `copy()`메서드로 일부 필드만 새로운 값으로 변화시킨 새로운 값 오브젝트를 만드는 것이 가능합니다.

```scala
object User {
  implicit class Setter(val user: UserEntity) extends AnyVal {
    def renameTo(name: String): UserEntity = user.mapValue(_.copy(name = name))
  }
}
```

이용하는 쪽은 유저 엔티티의 `renameTo()`메서드를 부르는 것으로 이름의 변경한 새로운 엔티티의 인스턴스를 얻는 것이 가능합니다.

```scala
val user: UserEntity = UserEntity(UserId(12345L), User(name = "tarao", privacy = 'public))
val renamedUser = user.renameTo("tarachang")
```

불변하는 메서드가 아닌, 데이터베이스 접근등 부작용을 일으키는 조작을 정의하고 싶은 경우의 방법은, 이후의 장에서 구체적으로 설명합니다.

### 결론

이상의 코드를 다 합치면, 다음과 같은 모델을 정의 가능합니다. 파일의 배치는 `domain.model`이름 공간으로하여, 하나의 개념마다 `object`로 묶읍시다(`package object`로 하면 디렉터리가 한층 깊게 되버리므로 그냥 object로 합니다)

```scala
// domain/model/User.scala
package boston
package domain
package model

object user {
  case class User(name: String, privacy: User.Privacy = 'public) {
    def isPublic(): Boolean = privacy == 'public
  }
  object User {
    type Status = Symbol

    implicit class Setter(val: user: UserEntity) extends AnyVal {
      def renameTo(name: String): UserEntity = user.mapValue(_.copy(name = name))
    }
  }

  type UserId = Entity.Id[UUID, User]
  val UserId = Entity.Id[UUID, User]

  type UserEntity = Entity[UserId, User]
  val UserEntity = Entity[UserId, User]
}
```

```scala
// domain/model/URL.scala
package boston
package domain
package model

object url { // scalastyle:ignore object.name
  type URL = Value[String, ops.URL]
  val URL: String => URL = Value.apply _
}
```

```scala
// domain/model/ops/URL.scala
package boston
package domain
package model
package ops

case class URL(url: String) extends AnyVal
object URL {
  implicit val stringToUrlOps: String => URL = apply _
  implicit val urlToOps: model.url.URL => URL = Value.toOps _
}
```

```scala
// domain/model/Location.scala
package boston
package domain
package model

import url.URL

object location { // scalastyle:ignore object.name
  case class Location(url: URL)

  type LocationId = Entity.Id[UUID, Location]
  val LocationId = Entity.Id[UUID, Location]

  type LocationEntity = Entity[LocationId, Location]
  val LocationEntity = Entity[LocationId, Location]
}
```

```scala
// domain/model/Entry.scala
package boston
package domain
package model

object entry { // scalastyle:ignore object.name
  case class Entry(url: URL)

  type EntryId = Entity.Id[UUID, Entry]
  val EntryId = Entity.Id[UUID, Entry]

  type EntryEntity = Entity[EntryId, Entry]
  val EntryEntity = Entity[EntryId, Entry]

  case class Content(title: String, body: String)

  type ContentId = Subentity.Id[EntryId, Content]
  val ContentId = Subentity.Id[EntryId, Content]
  type ContentEntity = Entity[ContentId, Content]
  val ContentEntity = Entity[ContentId, Content]
}
```

```scala
// domain/model/Bookmark.scala
package boston
package domain
package model

object bookmark { // scalastyle:ignore object.name
  case class Bookmark(comment: String)

  case class BookmarkId(userId: UserId, locationId: LocationId)
      extends Subentity.CompoundId[Bookmark]

  type BookmarkEntity = Entity.Timed[BookmarkId, Bookmark]
  val BookmarkEntity = Entity.Timed[BookmarkId, Bookmark]
}
```
