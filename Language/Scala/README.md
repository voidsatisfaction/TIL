# The Basic of Scala

스칼라의 기초에 관한 요약을 [Scala School](https://twitter.github.io/scala_school/ko/basics.html)에 기초하여 만들어 보았다.

## 실행

```sh
sbt
run
```

- scala 처리계(jar파일)이 인스톨됨
- jar파일
  - 클래스 파일이나 리소스 파일(사진 데이터)가 들어있는 zip아카이브
  - 메타데이터가 들어있으므로, 어떠한 클래스가 실행될 수 있는지를 작성할 수 있음

### 간단히 스칼라 코드 작성하기

- sbt로 console커멘드를 실행하면 Scala의 repl에 넣어짐
- 여러가지 실행해볼 수 있어서 편리함

## 기초

### 식

스칼라는 식(결과를 반환하는 문장) 중심의 언어이다. `if/else`역시도 식이다. 함수 정의도 식으로 함

```scala
1 + 1

val result = if (i % 3 == 0 && i % 5 == 0) {
  "FizzBuzz"
} else if (i % 3 == 0) {
  "Fizz"
} else if (i % 5 == 0) {
  "Buzz"
} else {
  i.toString
}
```

### 값

```scala
val two = 1 + 1 // Int = 2
```

변경 불가능

#### 변수

```scala
var name = "steve"
name = "marius"
```

변경 가능

### 패턴 매칭(식)

- 엄청나게 편리한 `switch`문과 비슷한 것이 존재
- 최근의 언어는 거의 다 들어있음

#### 정수로 매칭

- `match`식을 사용함
- 식이므로 값을 반환함
- 엄청나게 강력함

```scala
val msg = x match {
  case 0 | 1 => "is 0 or 1"
  case n if n < 100 => "is under 100"
  case _ => "else"
}
println(msg)
```

### 컬렉션

#### 편리한 컬렉션

- 여러가지 컬렉션의 종류가 있음
  - List/Array/Map/Set
  - 이외에 더 있음
- 컬렉션에는 편리한 메서드가 여러가지 있음
  - `map / filter / flatMap / find / findAll / reduce`
  - `take / drop / exists / sort / sortBy / zip / partition`
  - `grouped / groupBy`
  - ...

#### 리스트

```scala
val list = List(1,2,3,4,5,6,7,8,9)
list.map { n =>
  n * n
}.filter { n =>
  n % 2 == 0
}.sum

list.groupBy(2).foreach { ns => println(ns) }
/*
List(1, 2)
List(3, 4)
List(5, 6)
List(7, 8)
List(9)
*/

val result2 = list.groupBy { n => if (n % 2 == 0) "even" else "odd" }
// Map(odd -> List(1, 3, 5, 7, 9), even -> List(2, 4, 6, 8))

result2("even")
// List(2, 4, 6, 8)
```

#### 함수 리터럴

```scala
val addOne = (x: Int) => x + 1 // 리턴값의 타입을 쓰지 않는다?
addOne(1) // 2

val timesTwo = { i: Int =>
  println("hello world")
  i * 2
}

list.reduce { (x, y) => // 매개변수 리스트
  10 * x + y // 마지막 값이 반환값
}

List("apple", "banana", "grape").map(_.length)
```

#### Map

- 키(key)에 대해서 값을 갖는 컬렉션
- 여러가지 편리한 메서드가 존재
- 일단은 소개만

```scala
val usrs = Map(
  "www"  -> "http://www.hatena.ne.jp",
  "b"    -> "http://b.hatena.ne.jp",
  "blog" -> "http://hatenablog.com"
)
urls.get("b") // -> some("http://b.hatena.ne.jp")
urls.get("v") // -> None
```

### Option타입

- Option타입이란
  - 값이 있는지 없는지 표현 할 수 있는 타입
  - `undef`체크를 까먹지 않게 해주는 좋은 것
  - Option[+A]타입
    - Some(x)이라는 값
      - x는 +A타입의 값(Option[Int]타입 이라면 Int타입)
    - None이라는 값
  - Some의 내용을 사용하려면 명시적으로 꺼내는 작업이 필요함

#### Option타입 값을 생성

- 값이 있을 때는 `Some`에 값을 감싸줌
- 없을 경우 `None`

```scala
Some("hello")
Some(1)
Some({ () => 5 * 3 })
None
```

#### Option타입에 감싸진 값을 추출

```scala
val urls = Map(
  "www" -> "http://www.hatena.ne.jp",
  "b"   -> "http://b.hatena.ne.jp",
  "blog"-> "http://hatenablog.com"
)

val bUrl = urls.get("b") // Some("http://b.hatena.ne.jp")
val vUrl = urls.get("v") // None

// way1(bad)
bUrl.get // Some가None인지를 무시해서 추출 / 기본적으로 사용하지 않음
vUrl.get // runtime error!

// way2
bUrl.getOrElse("no url") // Some이면 내용의 값
vUrl.getOrElse("no url") // None이면 초기값

// way3
bUrl match {
  case Some(url) =>
    "URL of b is $url"
  case None =>
    "no url"
}
```

- `get`은 절대 사용 금지
- 특별한 조작없이는 값을 사용할 수 없음
  - 값을 제대로 추출했는지 어땠는지는 타입으로 체크됨

#### 다시 한 번 패턴매칭

- 값의 구조로 매칭
- `Some`의 경우 내부의 값이 `url`에 해당함
- 대상이 `unapply`메서드를 구현하면, 이러한 패턴 매치가 가능함
  - `case class`라는 것을 사용하면 간단하게 만들 수 있음

```scala
val bUrl = Some("http://b.hatena.ne.jp")
bUrl match {
  case Some(url) =>
    "URL of b is $url"
  case None =>
    "no url"
}
```

#### 불완전한 패턴 매칭

- 반드시 `undef`체크 가능하다고는 하지만 `None`의 `case`를 까먹을 수 있음

```scala
bUrl match {
  case Some(url) =>
    "url is $url"
}
// match may not be exhausive
// It would fail on the following input: None
```

#### Option타입의 여러가지 메서드

```scala
val bUrl = Some("http://b.hatena.ne.jp")

bUrl.filter { url => isHatenaUrl(url) } // True이면 그대로, false이면 None이 됨
bUrl.exists { url => isHatenaUrl(url) } // Some이면 조건식의 결과, None이면 false
bUrl.map { url => getContent(url) } // Some이면 값을 변환, None이면 그대로 둠
```

- `List`가 갖고 있는 많은 메서드를 사용할 수 있음
  - **요소수가 0이나 1밖에 없는 `List`라고 간주할 수 있음**

#### flatMap

- `map`과 `flatten`의 합성
- 내포 리스트에 적용할 수 있는 함수를 중첩된 리스트 안의 각 리스트에 적용해서 나온 결과를 하나의 리스트로 합쳐줌

```scala
findEntryBy(entryId) // Option[Entry]
findUserBy(userId) // Option[User]
```

- entry의 author의 값을 얻고 싶음
- entry가 `Some`일때만 author를 찾아서, author가 있다면 `Some`을 반환하고 싶음
- 어느쪽도 찾을 수 없다면 `None`을 반환

```scala
findEntryBy(entryId).flatMap { entry =>
  findUserBy(entry.authorId)
}
```

- `flatMap`을 사용하면 `Option`을 반환하는 메서드를 차례차례 연결할 수 있음
  - 전부가 `Some`일때의 처리를 작성할 수 있음
  - 네스트(nest)하기 시작하면 읽기 힘들어짐
  - 그러나 읽기 쉽게하는 방법이 있음

```scala
findEntryBy(entryId).flatMap { entry =>
  findUserBy(entry.authorId).flatMap { user =>
    findUserOptionBy(user.id).flatMap { userOption =>
      findUserStatusBy(user.id).map { userStatus =>
        // 全部見つかった時の処理を書ける
        makeResult(entry, user, userOption, userStatus)
      }
    }
  }
}
```

### for식

- for문이 아니라, for식 즉, 값을 리턴함
- `foreach`, `map`, `flatMap`, `filter`, `withFilter`등의 신텍스 슈거

#### 간단한 for

```scala
for (i <- (1 to 9)) {
  println(i)
}
```

- foreach를 사용하면 다음과 같은 코드가 되고 위와 같음

```scala
(1 to 9).foreach { i =>
  println(i)
}
```

#### 값을 반환하는 for

```scala
val pows = for (i <- (1 to 9)) yield i * i
```

- 위의 코드는 `map`을 사용한 아래의 코드와 같음

```scala
val pows = (1 to 9).map{ i => i * i }
```

#### 가드가 있는 for

```scala
for (i <- (1 to 9) if i % 2 == 0) {
  println(i)
}
```

- `withFilter`를 사용한 아래의 코드와 같음
- `withFilter`를 사용할 수 없는 경우 `filter`로 fallback됨

```scala
(1 to 9).withFilter { i =>
  i % 2 == 0
}.foreach { i =>
  println(i)
}
```

#### 중첩된 for

```scala
for {
  i <- (1 to 9)
  j <- (1 to 9)
} {
  print((i * j).toString + " ")
}
```

- `foreach`를 사용한 아래의 코드와 같음

```scala
(1 to 9).foreach { i =>
  (1 to 9).foreach { j =>
    print((i*j).toString + " ")
  }
}
```

#### 값을 생성하는 중첩된 for

```scala
val kuku = for {
  i <- (1 to 9)
  j <- (1 to 9)
} yield i * j
```

- `flatMap`과`map`을 사용하여 다음과 같이 작성할 수 있음

```scala
val kuku = (1 to 9).flatMap { i =>
  (1 to 9).map { j =>
    i * j
  }
}
```

- `flatMap`을 중첩시킨 것(네스트)과 같음

```scala
val kukuku = for {
  i <- (1 to 9)
  j <- (1 to 9)
  k <- (1 to 9)
} yield i * j * k

// 위는 다음과 같음

val kukuku = (1 to 9).flatMap { i =>
  (1 to 9).flatMap { j =>
    (1 to 9).map { k =>
      i * j * k
    }
  }
}
```

#### Option타입을 for문으로 사용하기

- 다음과 같이 `Option`을 반환하는 함수를 `flatMap`으로 계속 연결 할 수 있었다.(Option은 리스트와 비슷한 성질을 갖기 때문)

```scala
val result = findEntryBy(entryId).flatMap { entry =>
  findUserBy(entry.authorId).flatMap { user =>
    findUserOptionBy(user.id).flatMap { userOption =>
      findUserStatusBy(user.id).map { userStatus =>
        // 全部見つかった時の処理を書ける
        makeResult(entry, user, userOption, userStatus)
      }
    }
  }
}
```

- 위를 `for`식을 사용하면 다음과 같이 쓸 수 있음

```scala
val result = for {
  entry <- findEntryBy(entryId)
  user <- findUserBy(entry.authorId)
  userOption <- findUserOptionBy(user.id)
  userStatus <- findUserStatusBy(user.id)
} yield makeResult(entry, user, userOption, userStatus)
```

- 읽기 쉬움
- 값이 전부 `Some`이면 `Some(makeResult(entry, user, userOption, userStatus))`
- 어느 하나라도 `None`이면 `None`
- `for`식을 사용하면 어떠한 타입의 값도 연결해서 처리해서 이쁘게 코드를 짤 수 있음
  - 어떻게 연결할 것인지는 `flatMap`의 구현에 따름
  - `Option`타입의 경우, `Some`의 경우에는 처리가 이어져도 `None`의 경우에는 멈춤

#### 모나드

- Option이나 List는 모나드
- 모나드가 요구하는 함수
  - `return`
    - 값을 `Option`이나 `List`에 감싸는 함수 => Some(10), List(10)
  - `bind`
    - `Option`또는`List`를 반환하는 함수를 조합하는 함수 => `flatMap`
  - 이러한 것이 모나드쪽을 만족함
- `for`식은 하스켈의 `do`식에 해당함
- `Option`이나 `List`이외에도 강력한 추상화 매커니즘을 모나드로서 사용 가능
- 자세히는 [すごいHaskellたのしく学ぼう！](http://www.amazon.co.jp/gp/product/4274068854)를 읽어보자
- [Scalaz](https://github.com/scalaz/scalaz)라는 것을 사용하면 강력한 모나드나 기법을 사용할 수 있게 됨

### 함수

```scala
def addOne(m: Int): Int = m + 1

def timesTwo(i: Int): Int = {
  println("hello world")
  i * 2
}
```

매개변수가 없는 함수의 경우, 호출시 괄호를 생략할 수 있다.

```scala
def three() = 1 + 2

three() // 3
three // 3
```

#### 부분 적용(Partial application)

함수 호출시 밑줄(_)을 이용해 일부만 적용할 수 있다. 그렇게 하면 새로운 함수를 얻는다.

```scala
def adder(m: Int, n: Int) = m + n

val add2 = adder(2, _:Int)
add2(3) // 5
```

#### 커리 함수(Curried functions)

```scala
def multiply(m: Int)(n: Int): Int = m * n
multiply(2)(3) // 6

val timesTwo = multiply(2) _
timesTwo(3) // 6

(adder _).curried // 커리화
```

#### 가변 길이 매개변수

```scala
def capitalizeAll(args: String*) = {
  args.map { arg =>
    arg.capitalize
  }
}

capitalizeAll("rarity", "applejack")
```

### 클래스

클래스 안에서 메서드는 `def`로, 필드는 `val`로 정의한다. 메서드는 단지 클래스(객체)의 상태에 접근할 수 있는 함수에 지나지 않는다. `immutable`

```scala
class Cat(n: String) { // 컨스트럭터
  val name = n // 필드

  def say(msg: String) : String = {
    name + ": " + msg + "desu"
  }
}

println(new Cat("tama").say("hi"))

class Tiger(n: String) extends Cat(n) {
  override def say(msg: String): String = {
    name + ": " + msg + "dagao-"
  }
}

println(new Tiger("tora").say("mello"))
```

#### object

- 클래스의 정의에 대해서 1개밖에 존재하지 않는 오브젝트를 간단히 정의 할 수 있음
- 클래스에서 정의한 클래스와 같은 이름으로 `object`를 정의하면, 동료오브젝트가 됨(companion object)
  - 동료 오브젝트
    - 서로가 비공개 멤버에 접근 가능
    - `implicit`매개변수의 해결에 사용되는 경우가 존재

```scala
object CatService {
  val serviceName = "cat maker"
  def createByName(name: String): Cat = new Cat(name)
}
val mike = CatService.createByName("mike")

object Tama extends Cat("tama") {
  override def say(msg: String): String = "tamanya-"
}

object Cat { // 이미 있는 클래스의 이름과 같은 이름이면
  // 정의된 메서드는 클래스메서드와 같은 역할을 함
  def create(name: String): Cat = new Cat(name)
}
val hachi = Cat.create("hachi")
```

#### case 클래스

- 클래스와 닮음
- 데이터 구조를 정의 하기 쉽게 커스터마이징 되어있음
- 몇가지 메서드가 좋은 느낌으로 있음
  - toString/hashCode
  - apply/unapply(동료 오브젝트에)

```scala
case class Cat(name: String) { // name은 그 자체로 field가 됨
  def say(msg: String): String = ????
}
val buchi = Cat("buchi") // even without new it can be created
buchi match {
  case Cat(name) => // 패턴 매칭에 사용 가능
    "name of buchi is " = name
}
```

#### trait

- 구현을 추가할 수 있는 인터페이스
- 스칼라에서는 설계의 베이스가 되는 클래스의 구조를 구축하기 위해서 사용됨
- 루비의 모듈에 거의 해당하는 개념

```scala
class Cat(n: String) {
  val name = n
}

trait Flyable {
  def fly: String = "I can fly"
}

// with로 갱신 / 중복 계승
class FlyingCat(name: String) extends Cat(name) with Flyable
new FlyingCat("chatora").fly

// 스칼라로 정의되어 있는Ordered trait을 구현하면 비교가능하게 됨
class OrderedCat(name: String) extends Cat(name) with Ordered[Cat] {
  def compare(that: Cat): Int = this.name.compare(that.name)
}
new OrderedCat("tama") > new OrderedCat("mike")
new OrderedCat("tama") < new OrderedCat("mike")
```

#### sealed trait

`trait`을 `mixin`하고 있는 `case class`등을 패턴 매칭으로 판정하는 경우, 모든 케이스 클래스에 대하여 빠진 것을 검사하고 싶을 때, `sealed`를 사용

`sealed`수식자는 "동일 파일내의 클래스로부터는 계승할 수 있으나, 다른 파일 내에서 정의된 클래스에서는 계승할 수 없음"이라는 계승의 관계의 스코프를 제한하기 위한 것이나, `match식`의 빠진 케이스를 검사하는 용도로도 사용됨

```
sealed trait HatenaService
case class HatenaBlog(name: String) extends HatenaService
case class HatenaBookmark(name: String) extends HatenaService
case class JinrikiKensakuHatena(name: String) extends HatenaService
case class Mackerel(name: String) extends HatenaService

val service: HatenaService = HatenaBlog("blog")

service match {
  case HatenaBlog(name) => name
  case HatenaBookmark(name) => name
  case JinrikiKensakuHatena(name) => name
}

<console>:16: warning: match may not be exhaustive.
It would fail on the following input: Mackerel(_)
              service match {
              ^
```

### trait의 마름모 계승에 대하여

- 클래스 A, B, C, D가 존재
- B, C는 A를 계승
- D는 B, C를 계승
- B, C는 각각 A의 메서드(혹은 필드)를 오버라이드 하고 있음
- D는 어떻게 A의 메서드를 갖고 있을까?

```scala
trait A {
  val value = "A"
}

trait B extends A {
  override val value = "B"
}

trait C extends A {
  override val value = "C"
}

class D extends B with C

scala> (new D).value
res0: String = C
```

정답은 C이다. extends하는 순서를 바꾸면 B가 됨

#### Function vs Method

Function은 값이나, Method는 그자체가 값이 아니다.

### 상속

```scala
class ScientificCalculator(brand: String) extends Calculator(brand) {
  def log(m: Double, base: Double) = math.log(m) / math.log(base)
}
```

### 메소드 중복정의(Overloading)

```scala
class EvenMoreScientificCalculator(brand: String) extends ScientificCalculator(brand) {
    def log(m: Int): Double = log(m, math.exp(1))
}
```

### 추상 클래스(abstract class)

메소드 정의는 있지만 구현은 없는 클래스. 대신 이를 상속한 하위 클래스에서 메소드를 구현.

```scala
abstract class Shape {
  def getArea():Int
}

class Circle(r: Int) extends Shape {
  def getArea():Int = { r * r * 3 }
}
```

### 트레잇(Traits)

다른 클래스가 확장 하거나 섞어 넣을 수 있는(Mix in) 필드와 동작의 모음.

```scala
trait Car {
  val brand: String
}

trait Shiny {
  val shineRefraction: Int
}

class BMW extends Car {
  val brand = "BMW"
}
```

클래스는 여러 트레잇을 `with`키워드를 사용해 확장할 수 있다.

```scala
class BMW extends Car with Shiny {
  val brand = "BMW"
  val shineRefraction = 12
}
```

인터페이스 역할을 하는 타입을 설계할 때는 `생성자 매개변수`가 필요한 상황을 제외하면 트레잇을 사용하는 것이 낫다.

`trait vs abstract class`

### 타입

일반적(generic)인 함수를 만들 수 있다. 이럴때에는 각괄호`([])`안에 타입 매개변수를 추가한다.

```scala
trait Cache[K, V] {
  def get(key: K): V
  def put(key: K, value: V)
  def delete(key: K)
}

def remove[K](key: K)
```
