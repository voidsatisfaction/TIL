# The Basic of Scala

스칼라의 기초에 관한 요약을 [Scala School](https://twitter.github.io/scala_school/ko/basics.html)에 기초하여 만들어 보았다.

## 기초

### 식

스칼라는 식(결과를 반환하는 문장) 중심의 언어이다. `if/else`역시도 식이다.

```scala
1 + 1
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

### 함수

```
def addOne(m: Int): Int = m + 1

def timesTwo(i: Int): Int = {
  println("hello world")
  i * 2
}
```

매개변수가 없는 함수의 경우, 호출시 괄호를 생략할 수 있다.

```
def three() = 1 + 2

three() // 3
three // 3
```

#### 람다함수

```
val addOne = (x: Int) => x + 1 // 리턴값의 타입을 쓰지 않는다?
addOne(1) // 2

val timesTwo = { i: Int =>
  println("hello world")
  i * 2
}
```

#### 부분 적용(Partial application)

함수 호출시 밑줄(_)을 이용해 일부만 적용할 수 있다. 그렇게 하면 새로운 함수를 얻는다.

```
def adder(m: Int, n: Int) = m + n

val add2 = adder(2, _:Int)
add2(3) // 5
```

#### 커리 함수(Curried functions)

```
def multiply(m: Int)(n: Int): Int = m * n
multiply(2)(3) // 6

val timesTwo = multiply(2) _
timesTwo(3) // 6

(adder _).curried // 커리화
```

#### 가변 길이 매개변수

```
def capitalizeAll(args: String*) = {
  args.map { arg =>
    arg.capitalize
  }
}

capitalizeAll("rarity", "applejack")
```

### 클래스

클래스 안에서 메소드는 `def`로, 필드는 `val`로 정의한다. 메소드는 단지 클래스(객체)의 상태에 접근할 수 있는 함수에 지나지 않는다. `immutable`

```
calss Calculator {
  val brand: String = "HP"
  def add(m: Int, n: Int): Int = m + n
}

val calc = new Calculator
calc.add(1, 2) // 3
calc.brand // "HP"
```

#### 생성자

생성자가 특별한 메소드로 따로 존재하지 않느다. 클래스 몸체에서 메소드 정의 부분 밖의 모든 코드가 생성자 코드가 된다.

```
class Calculator(brand: String) {
  val color: String = if (brand == "TI") {
    "blue"
  } else if (brand == "HP") {
    "black"
  } else {
    "white"
  }

  // 인스턴스 메소드
  def add(m: Int, n: Int): Int = m + n
}
```

#### Function vs Method

Function은 값이나, Method는 그자체가 값이 아니다.

### 상속

```
class ScientificCalculator(brand: String) extends Calculator(brand) {
  def log(m: Double, base: Double) = math.log(m) / math.log(base)
}
```

### 메소드 중복정의(Overloading)

```
class EvenMoreScientificCalculator(brand: String) extends ScientificCalculator(brand) {
    def log(m: Int): Double = log(m, math.exp(1))
}
```

### 추상 클래스(abstract class)

메소드 정의는 있지만 구현은 없는 클래스. 대신 이를 상속한 하위 클래스에서 메소드를 구현.

```
abstract class Shape {
  def getArea():Int
}

class Circle(r: Int) extends Shape {
  def getArea():Int = { r * r * 3 }
}
```

### 트레잇(Traits)

다른 클래스가 확장 하거나 섞어 넣을 수 있는(Mix in) 필드와 동작의 모음.

```
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

```
class BMW extends Car with Shiny {
  val brand = "BMW"
  val shineRefraction = 12
}
```

인터페이스 역할을 하는 타입을 설계할 때는 `생성자 매개변수`가 필요한 상황을 제외하면 트레잇을 사용하는 것이 낫다.

`trait vs abstract class`

### 타입

일반적(generic)인 함수를 만들 수 있다. 이럴때에는 각괄호`([])`안에 타입 매개변수를 추가한다.

```
trait Cache[K, V] {
  def get(key: K): V
  def put(key: K, value: V)
  def delete(key: K)
}

def remove[K](key: K)
```
