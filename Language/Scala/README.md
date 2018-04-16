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

## 암묵적 형변환 / 매개변수(implicit conversion/parameter)

- 암묵적 형변환
- 암묵적 매개변수

### 일반적인 형변환

```scala
def stringToInt(s: String): Int = {
  Integer.parseInt(2, 10)
}

"20" / 5 // 타입 에러가 됨
stringToInt("20") / 5 // ok
```

### 암묵적 형변환(implicit)

```scala
implicit def stringToInt(s: String): Int = {
  Integer.parseInt(2, 10)
}

"20" / 5 // 계산가능
```

- 요구하는 타입을 얻을 수 없는 경우, **같은 스코프** 안의 `implicit`선언을 조사해서 자동으로 변환해 줌
- /의 왼쪽에는 수치타입만 나타날 수 있으나, 문자열이 나타났으므로, `implicit`에서 정의한 변환 함수가 호출됨
- 그러니 위와 같은 활용은 하지 않음

#### 활용: 기존의 타입을 확장하는 것 처럼 보여줌(pimp my library패턴)

```scala
class GreatString(val s: String) {
  def bang: String = s + "!!!!"
}
implicit def str2greatStr(s: String): GreatString = {
  new GreatString(s)
}

"hello".bang // String에 새로운 메서드가 생긴 것 처럼 보임
```

```scala
implicit class GreatString(s: String) {
  def bang: String = s + "!!!!"
}

"hello".bang
```

#### 활용: 암묵적 매개변수

- 미리 암묵적 인자를 받는 함수를 정의
- 호출시 스코프내의 `implicit`선언을 조사하여 자동적으로 인자로서 받음

```scala
def say(msg: String)(implicit suffix: String) = msg + suffix

say("hello")("!!!!!") // => hello!!!!! 일반적인 호출
implicit val mySuffix = "!?!?!!1" // 암묵적 인자를 제공
say("hello") // => hello!?!?!!1
```

- 다음과 같은 경우는?

```scala
def say(msg: String)(implicit suffix: String) = msg + suffix
implicit val superSuffix: String = "!23"
implicit val superSuffix2: String = "123$$$$$"

println(say("monokuro")) // ambiguous implicit values: Error!!!
```

##### 활용1: 컨텍스트 오브젝트(context object)를 계속해서 사용하는 경우

```scala
def findById(id: Int, dbContext: DBContext) = ???
def findByName(name: String, dbContext: DBContext) = ???

val dbContext = new DBContext()
findById(1, dbContext)
findByName("hakobe", dbContext) // 매번 컨텍스트를 넘겨줘야하므로 귀찮음
```

```scala
def findById(id: Int)(implicit dbContext: DBContext) = ???
def findByName(name: String)(implicit dbContext: DBContext) = ???

implicit val dbContext = new DBContext()
findById(1)
findByName("hakobe") // dbContext는 암묵적으로 제공되므로 귀찮을 것이 없음
```

##### 활용2

- 타입 클래스 구현
- `adhoc`다형성의 구현
  - c.f `adhoc`이란, **특별한 목적을 위해서** 라는 뜻
  - 함수 정의를 타입마다 다르게 대체할 수 있음
  - 스코프 마다 대체할 수 있음(adhoc)
  - 타입의 소스코드에 접근 권한이 없어도 구현을 제공할 수 있음(adhoc)
- 자세한 것은 다음의 url참조
  - http://nekogata.hatenablog.com/entry/2014/06/30/062342
  - http://eed3si9n.com/learning-scalaz/ja/polymorphism.html

```scala
trait FlipFlapper[T] {
  def doFlipFlap(x: T): T
}
implicit object IntFlipFlapper extends FlipFlapper[Int] {
  def doFlipFlap(x: Int) = -x
}
implicit object StringFlipFlapper extends FlipFlapper[String] {
  def doFlipFlap(x: String) = x.reverse
}

def flipFlap[T](x: T)(implicit flipFlapper: FlipFlapper[T]) = flipFlapper.doFlipFlap(x)

flipFlap(1) // => -1
flipFlap("string") // => "gnirts"
```

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

## 타입 매개변수(type parameter)

- 스칼라의 `List`등은 그 리스트의 요소가 모두 같은 타입이라면, `String`이나 `Int`와 같은 다양한 타입을 넣는 것이 가능. 이를 타입 매개변수라 함
- `List[A]`와 같이 정의되어있으며, `A`의 부분이 타입 매개변수
- `List[String]`은 그 리스트가 문자열만 다룰 수 있게 하고, `List[Int]`라고 하면 정수만 다룰 수 있게 함

```scala
val l: List[Int] = List("a", "b") // 컴파일 에러
```

- 자신이 정의한 함수의 매개변수의 타입을 임의의 타입으로 하고 싶은경우 등에 다음과 같이 정의 가능

```scala
def example[A](l: List[A]): A = l.head

example(List(1, 2)) // Int = 1
example(List("a", "b")) // String = a
```

- 타입 매개변수는 유연하게 지정하는 것이 가능해서, 예를들면 클래스의 파생 클래스만 매개변수로 받고싶은 경우에도 지정할 수 있음. 보다 자세한것은 **타입 경계**, **변위지정 어노테이션** 등의 키워드를 찾아보자

## 복수의 인자 리스트

- 함수를 정의할 때 복수의 인자 리스트를 만들 수 있음
- **값을 받는 매개변수와 함수를 받는 매개변수를 나누어** 두면 사용하는 사람이 편함

```scala
def example(x: Int)(y: Int) = x * y

example(2)(4)
```

```scala
def example(i: Int)(f: Int => Int) = f(i)

example(2) { i =>
  i * 2
}
```

위와 같이 `example`이라는 새로운 문(statement)를 정의한것 처럼 적을 수 있음

### 가변길이 인자

- 임의의 길이의 인자를 받음
- 함수 내부에서는 받은 인자를 `Seq`로 다룸(`foreach`를 사용할 수 있음)

```scala
def example(ss: String*): Unit = ss.foreach(println)

example("AA")
example("AA", "BB")
example("AA", "BB", "CC")

val sq = Seq("AA", "BB")
example(sq: _*) // 컬렉션을 넘겨줄 경우
// AA
// BB
```

## 문자열 보간(String interpolation)

- `s"..."`와 같이 문자열 리터럴 앞에 접두사를 붙여서, 리터럴 안의 `$name`타입으로 변수명을 지정하여 그 값을 넣을 수있음

```scala
val name = "foo"
val value = 3
s"$name is $value" // foo is 3
s"7 * 8 = ${7 * 8}" // 이와 같이 쓸 수 있음
```

## 오브젝트 지향과 함수형 프로그래밍 언어의 이야기

- 스칼라는
  - 오브젝트 지향언어
  - 함수형 프로그래밍 언어

### 오브젝트 지향

- 오브젝트 지향 언어의 특징
  - 오브젝트가 존재, 데이터를 보존하는 장소(필드)와 그러한 데이터를 조작하거나  이용해서 어떠한 행동(메서드)을 하는 것이 존재
  - 계승
  - 캡슐화
  - 다형성(polymorphism)

#### 계승

- 이미 정의가 끝난 객체의 특성을 상속하는 것
- 상속 받은 부모클래스의 메서드를 자식클래스가 사용할 수 있음

```scala
class Parent {
  def helloWorld() = println("hello world")
}

class Child extends Parent {
  def helloChild() = println("hello child")
}

new Child().helloWorld()
// hello world
```

#### 캡슐화

- 오브젝트 내부의 데이터 은폐
- 오브젝트 행위 은폐
- 오브젝트 실제의 타입을 은폐
  - 관계없는 외부의 오브젝트가 이러한 내부 데이터나 행위를 다룰 수 없게 함
  - **프로그램의 영향 범위 한정시킴**

```scala
class Capsule {
  private def secretMethod() = println("stick")

  def publicMethod() = secretMethod()
}

new Capsule().secretMethod() // error
new Catsule().publicMethod() // "stick"
```

#### 다형성

- 어떠한 오브젝트의 조작이 호출하는 쪽이 아니라, 호출 받는 쪽의 오브젝트에 의해서 정해지는 특성
- 아래의 예
  - `printHelloWorld`메서드는 `trait`을 받아들여서, 그 동작을 호출하고 있으나, 그 결과는 실제로 호출 받는 클래스에 위탁됨

```scala
trait HelloWorld {
  def HelloWorld: String
}

class En extends HelloWorld {
  def helloWorld: String = "hello world"
}

class Ja extends HelloWorld {
  def helloWorld: String = "こんにちは、世界"
}

def printHelloWorld(hw: HelloWorld) = println(hw.helloWorld)

printHelloWorld(new En)
printHelloWorld(new Ja)
```

### 함수형 프로그래밍 언어

- 스칼라는 함수평 프로그래밍 언어이기도 함
  - 함수가 제1급 오브젝트
  - 함수형 프로그래밍 스타일 추천
    - 가능한 한 부작용을 갖지 않는 식이나 함수를 조합함
    - 파괴적 대입은 피함
    - 어떠한 변수가 상태를 갖거나 일부를 변경하거나 하는 것은 하지 않음
- 참조 투명성이 항상 성립하는 언어를 순수함수형 프로그래밍 언어라고 함
  - 스칼라는 비순수함수형 프로그래밍 언어
  - 스칼라는 함수형 프로그래밍 스타일을 지원하기 위한 다양한 방법이 존재

#### 함수가 제1급 오브젝트

- 함수를 인자로 주거나
- 함수 결과를 함수로 돌려주거나
- 함수를 변수에 속박하거나 할 수 있음

```scala
val l = List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

l.filter(i => i % 2 == 0) // List(2, 4, 6, 8, 10)

val isEven = (i: Int) => i % 2 == 0

l.filter(isEven) // List(2, 4, 6, 8, 10)
```

#### 부작용

- 부작용을 갖지 않는 코드가 바람직함
  - 변수의 값을 변경하고 싶음(var 보다도 val)
  - 주변 변수의 상태에 동작을 의존하지 않음
  - 파일이나 데이터베이스의 입출력이 없음
- 이유
  - 클래스 등의 내부의 상태를 신경쓰지 않아도 되므로, 예측하기 쉬운 코드가 됨
  - 상태나 환경에 의존하지 않으므로 테스트를 쓰기 쉬움
  - 상태나 환경을 공유하지 않으므로 멀티스레드로 돌려도 문제가 없음
- 스칼라에 있어서의 부작용
  - `var`, `mutable`컬렉션
