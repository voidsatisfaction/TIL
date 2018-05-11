# Option Either

## Option의 정의

```scala
// Option의 추상클래스. 갖을 수도 있을 값의 타입을 파라미터로 갖음
sealed abstract class Option[+A] extends Product

// Some은 Option을 계승한 값이 있는 경우를 표현함
// 생성자에 실제로 값을 갖음
final case class Some[+A](x: A) extends Option[A]

// None은 값이 없는 경우를 나타냄. Option타입 파라미터는 공변이므로
// Option[Nothing]은 모든 Option[A]타입의 서브타입이 됨. 그러므로 싱글톤
case object None extends Option[Nothing]
```

### 패턴매칭으로 예외 처리 하는 경우

- Option타입의 `get`메서드를 이용해서 값을 추출할 수 있지만 `None`에서는 에러가 나므로 이는 바람직하지 않음
- 패턴매치 사용

```scala
val map = Map("a" -> 1, "b" -> 2)

map.get("a") match { // Option타입은 sealed로 지정되어 있으며, Some[A]는 케이스 클래스 이므로 Option타입에 대한 패턴 매칭을 작성할 수 있음
  case Some(n) => println(n) // 1
  case None => println("Nothing")
}

map.get("c") match {
  case Some(n) => println(n)
  case None => println("Nothing") // Nothing
}
```

### Option대신 null을 사용할 때에 문제점

- 해시 맵에서 키 자체가 없는 경우 `null`이 반환되는데 이것이 `null`인지 아닌지를 항상 확인해야 함
  - 이러한 확인을 컴파일러가 제대로 하고 있는지 판단하지 못함
  - 사람의 인지에 의존해서 반드시 `null`을 체크해줘야 함
- 해시 맵에서 키 자체가 없으면 `null`을 반환해야 하는데, 키는 존재해도 값이 `null`인 경우도 `null`을 반환하므로 구별이 되지 않음
  - js는 그래서 `undefined`가 있는건가부다

### 스칼라에서는 `Option`으로 해결가능

- 강제적으로 Some혹은 None을 사용하도록 함
- 빠트린 경우는 컴파일 에러
- 값 자체가 없으면 None 이고, null 값이 들어가 있으면 null
- **스칼라에서 `null`이 등장하는 경우는 `Option`으로 치환해야 하는 곳**

### Option을 고개함수를 이용해서 다루자

#### Map

- `Option#Map[B](f: (A) => B): Option[B]`
- Some의 경우는 인자의 `f:(A) => B`타입의 함수 오브젝트에 이미 보유하고 있는 값을 넘겨서 변환한 결과를 `Some[B]`로 반환, `None`이면 `None`인채로 둠

#### getOrElse

- `Option#getOrElse[B >: A](default: => B): B`
- Some인 경우에는 갖고 있는 값을 반환, None이면 인자에 준 값을 반환
- 디폴트 값을 지정할 떄 사용

```scala
val map = Map("foo" -> "bar", "hoge" -> null)

def valueLength(key: String) = map.get(key) match {
  case Some(v) if v == null => "key %s value is null" format(key)
  case Some(v) => "key %s value's length is %d" format(key, v.length)
  case None => "key %s is not contains." format(key)
}
```

#### `foreach`에 의한 처리

- `Option#foreach[U](f: (A) => U): Unit`
- Some이면 가지고 있는 값을 인자인 함수 오브젝트에 넘겨줘서 처리를 호출, None이면 아무것도 하지 않음
  - List등의 foreach와 같음

#### `orElse`에 의한 처리

- `Option#orElse[B >: A](alternative: => Option[B]): Option[B]`
- Some에 대해서 호출하면 자기자신을 반환, None에 대해서 호출하면 Option을 반환

```scala
verbose orElse deprecation foreach{ v => throw new IllegalArgumentException } // verbose가 none이면 deprecation을 반환, deprecation이 none이면 foreach는 실행되지 않음
```

#### `collect`에 의한 처리

- `collect[B](pf: PartialFunction[A, B]): Option[B]`
- 인자에 PartialFunction을 넘겨주어, PF가 적용 가능한 경우에만 map함

#### `exists`에 의한 처리

- `exists(p: (A) => Boolean): Boolean`
- Option값에 대해서, 인자의 p가 true를 반환하는가 확인. None에 대해서는 항상 false

```scala
opts.get("d").exists { s => s == "./bin" } // true
```

#### `filter`에 의한 처리

- `filter(p: (A) => Boolean): Option[A]`
- 인자의 p가 true를 반환할경우만 `Some[A]`를 반환. false를 반환하는 경우는 None이 됨

```scala
opts.get("verbose").filter{ v => v.nonEmpty } // Option[String] = None

opts.get("classpath").filter{ v => v.nonEmpty } // Option[String] = Some(./:./lib)
```

#### `flatMap`에 의한 처리

- `flatMap[B](f: (A) => Option[B]): Option[B]`
- `(A) => Option[B]`의 결과가 Some[B]라면 Some[B]를, None이면 None을 반환
  - **collection에서의 flatMap과는 다소 다른 움직임을 보임**
  - 컬랙션에서는 map -> flat의 움직임

```scala
val res3 = map.get("a").toRight(null).right.flatMap{ a => // 앞서 결과가 Left(a+b)이므로 Left(a+b)를 반환
  map.get("b").toLeft(null).left.map{ b => // Left(a+b)반환
    a + b
  }
}
println(res3) // Left(3)

// Opts에서 값이 지정된 것만 추출
// 컬렉션에서의 flatMap호출
// map -> flatten
opts.flatMap {
  case (k, "") => None
  case (k, v) => Some(v)
}
// scala.collection.immutable.Iterable[String] = List(./:./lib, .bin)
```

#### `Option`과 `for`

```scala
for( cp <- opts.get("classpath"); d <- opts.get("d") ) {
  | println(" classpath: %s" format cp )
  | println(" dest     : %s" format d )
| }
// classpath: ./:./lib
// dest     : ./bin
```

## Option 사용법

### getOrElse로 예외 처리

```scala
val map = Map("a" -> 1, "b" -> 2)

println(map.get("a").getOrElse(null)) // 1 // 처음 get은 map에 대한 메서드(요소를 갖고옴) 두번째 getOrElse는 option타입의 내부 값을 가져올때 사용
println(map.get("c").getOrElse(null)) // null
```

### flatMap과 map을 이용

```scala
val map = Map("a" -> 1, "b" -> 2)

// val res1 = map.get("a").flatMap{ a => a }
//
// println(res1)
// [error]  found   : Int
// [error]  required: Option[?]
// [error]     val res1 = map.get("a").flatMap{ a => a }
// [error]                                           ^

val res2 = map.get("a").flatMap{ a => // 전에 래핑된 Option을 한커풀 벗김
  map.get("b").map{ b => // Option래핑 유지
    println(a + b)
    a + b
  }
}
println(res2) // Some(3)

val res3 = map.get("c").flatMap{ c =>
  map.get("a").map{ a =>
    println(a + c)
    a + c
  }
}
println(res3) // None
```

### for를 이용하는 경우

```scala
val map = Map("a" -> 1, "b" -> 2)

val res1 = for {
  a <- map.get("a")
  b <- map.get("b")
} yield {
  a + b
}

println(res1) // Some(3)

val res2 = for {
  c <- map.get("c")
  b <- map.get("b")
} yield {
  println(c + b)
  c + b
}

println(res2) // None
```

## Either 사용법

- 어떠한 에러인지도 포함해서 반환할때는 `Either`를 이용함

### 패턴매칭을 이용

```scala
val a: Either[Int, String] = Right("a")
val b: Either[Int, String] = Right("b")
val c: Either[Int, String] = Left(3)

val res1 = a match {
  case Right(str) => str + "oh"
  case Left(int) => int + 1
}

val res2 = c match {
  case Right(str) => str + "oh"
  case Left(int) => int + 1
}

println(res1) // aoh
println(res2) // 4
```

### flatMap과 map을 이용

- `flatMap`과 `map`을 이용해서 어느쪽의 `Either`타입의 값이 전부 `Right`일 경우 처리를 어떻게 할 것인가를 기술 가능
- `Either`는 `Right`우선이 아니므로, 명시적으로 `Right`인지 `Left`인지 지정할 필요가 있음
  - 즉, `RightProjection`타입이나 `LeftProjection`타입으로 변환해야함

```scala
val a: Either[Int, String] = Right("a")
val b: Either[Int, String] = Right("b")
val c: Either[Int, String] = Left(3)

val res1 = a.right.flatMap{ a =>
  b.right.map{ b =>
    a + b
  }
}
println(res1) // Right(ab)

val res2 = c.right.flatMap{ c =>
  a.right.map{ a =>
    c + a
  }
}
println(res2) // Left(3)

val res3 = c.left.flatMap{ c =>
  a.right.map{ a =>
    c + a
  }
}
println(res3) // Right(3a)
```

### for를 이용

- 위의 `flatMap`과 `map`을 이용한 코드와 동일

```scala
val a: Either[Int, String] = Right("a")
val b: Either[Int, String] = Right("b")
val c: Either[Int, String] = Left(3)

val res1 = for {
  a <- a.right
  b <- b.right
} yield a+b
println(res1) // Right(ab)

val res2 = for {
  a <- a.right
  c <- c.right
} yield a+c
println(res2) // Left(3)

val res3 = for {
  c <- c.left
  a <- a.right
} yield c + a
println(res3) // Right(3a)
```

### Option.toRight(식)를 이용

- Option타입의 값이 `Some(값)`이면, `Right(값)`으로 변환시키고, None이면, `Left(식)`이 됨
- 에러 돌려줄떄 사용

```scala
val map = Map("a" -> 1, "b" -> 2)

val res1 = for {
  b <- map.get("b").toLeft(null).left
  a <- map.get("a").toRight(null).right
} yield {
  a + b
}
println(res1) // Right(3)

val res3 = map.get("a").toRight(null).right.flatMap{ a =>
  map.get("b").toLeft(null).left.map{ b =>
    a + b
  }
}
println(res3) // Left(3)
// map.get("a"): 키가 a인 요소 가져오기 -> 결과는 Some(1)
// map.get("a").toRight(null): Option타입이 Some의 값이면 Right(1) None의 값이면 Left(null)을 반환
// map.get("a").toRight(null).right: 주어진 Either타입의 값을 명시적으로 지정 RightProjection타입으로 지정
// map.get("a").toRight(null).right.flatMap{ a => ... }: RightProjection타입의 내부의 값인 a를 사용해서 작업을 함. 식의 결과 값은 한차원(래핑 하나) 줄어들음 그런데 그 래핑은 자기자신의 래핑임
// 그래서 위의 결과는 Left(3)
// Functional Programming In Scala 공부하자........

val res2 = for {
  c <- map.get("c").toRight(null).right
  b <- map.get("b").toRight(null).right
} yield {
  b + c
}
println(res2) // Left(null)
```

### 실제 생활에 적용

```scala
sealed trait Error {
  override def toString(): String = this match {
    case DiaryNotFoundError => "Can not find a target diary"
    case DiaryAlreadyExistsError => "Can not add diary which already exists"
    case ArticleNotFoundError => "Can not find a target article"
    case ArticleAlreadyExistsError => "Can not add article which already exists"
  }
}
final case object DiaryNotFoundError extends Error
final case object DiaryAlreadyExistsError extends Error
final case object ArticleNotFoundError extends Error
final case object ArticleAlreadyExistsError extends Error


def deleteArticle(diaryTitle: String, title: String)(implicit ctx: Context): Either[Error, Unit] = {
  val user = currentUser

  for {
    diary <- repository.Diaries.findByUserAndTitle(user, diaryTitle).toRight(DiaryNotFoundError).right
    article <- repository.Articles.findByDiaryAndTitle(diary, title).toRight(ArticleNotFoundError).right
  } yield repository.Articles.delete(article)
}
```
