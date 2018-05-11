# Option Either

## Option 사용법

### 패턴매칭으로 예외 처리 하는 경우

```scala
val map = Map("a" -> 1, "b" -> 2)

map.get("a") match {
  case Some(n) => println(n) // 1
  case None => println("Nothing")
}

map.get("c") match {
  case Some(n) => println(n)
  case None => println("Nothing") // Nothing
}
```

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
