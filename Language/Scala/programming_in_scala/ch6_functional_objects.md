# 함수형 오브젝트

- 변경 불가능한 상태를 갖는 오브젝트
- 이번 챕터에서는 클래스 Rational을 만들면서 스칼라의 OOP에 대해서 공부

## 불변 오브젝트의 장단점

- 장점
  - 가변 오브젝트보다 쉽게 다룰 수 있음
  - 가변 오브젝트보다 쉽게 다른곳에 넘겨줄 수 있음
    - 가변 오브젝트는 항상 안전한 복사에 신경써야 함
  - 멀티 스레드에서 동시에 불변의 오브젝트에 접근해도 상태가 오염되지 않음
  - 안전한 해시 테이블 키를 만들 수 있음
- 단점
  - 단지 조금의 변경에도 매우 큰 오브젝트 그래프가 복사될 가능성이 있음
    - 그래서 특정 상황에서 사용할 수 있도록 가변 오브젝트를 준비

## 클래스 Rational의 명세

- 실수(rational number)는 n/d로 표현됨
  - n은 `numerator` 분자
  - d는 `denominator` 분모
  - n,d는 정수, 단 d는 0이아니어야 함
- `+ - * /`가 가능해야 함
- 기약분수 형태로 출력
- 실수는 변경 가능한 상태가 아님
  - 언제나 연산뒤에는 새로운 값이 생성

## Rational클래스의 생성

```scala
class Rational(n: Int, d: Int)
```

- 클래스 선언
  - n, d는 클래스 매개변수(class parameter)라고 함
  - 클래스 매개변수는 클래스 필드와는 다름
- 스칼라 컴파일러는 클래스 내부에 있는 **필드나, 메서드가 아닌 모든 코드** 를 컴파일 할 것임

## toString메서드를 다시 구현하기

- 클래스를 단순히 출력하면 `Rational@90110a`이런 값이 나옴
- 클래스 내부의 값을 알고 싶으면 `toString`메서드를 오버라이드 해야함

```scala
class Rational(n: Int, d: Int) {
  override def toString = n + "/" + d
}
```

## 선행 조건 확인하기(Checking preconditions)

- 데이터를 캡슐화 해서 데이터가 계속해서 유효하다는 것을 보증할 수 있는것이 OOP의 장점중 하나
- 앞서의 Rational클래스는 d에 0이와도 유효

```scala
class Rational(n: Int, d: Int) {
  require(d != 0)
  override def toString = n + "/" + d
}
```

- `require`메서드는 하나의 불린 매개변수를 받음
  - 인자의 값이 참이면 오브젝트가 생성돼서 돌아옴

## 필드 만들기

- `add`메서드 만들기
  - 기존의 필드를 변경시키지 않고 완전히 새로운 Rational오브젝트를 돌려줘야 함

```scala
class Rational(n: Int, d: Int) {
  require(d != 0)
  override def toString = n + "/" + d
  def add(that: Rational): Rational = new Rational(n * that.d + that.n * d, d * that. d)
}1
```

- 위의 `add`메서드는 컴파일 에러
  - **`that.d, that.n`을 참조할 수 없음(add의 메서드가 실행된 그 오브젝트 자체가 아니기 때문)**
  - **val이나 var선언 없이 클래스 매개변수를 지정하는 경우는 `private`취급이 됨**
- 위의 경우, class밖에서 필드에 접근할 수 없음
- 사실 위의 코드에서 Rational클래스를 case 클래스로 바꾸면 잘 됨

```scala
class Rational(n: Int, d: Int) {
  require(d != 0)
  val numer: Int = n
  val denom: Int = d
  override def toString = numer + "/" + denom
  def add(that: Rational): Rational = new Rational(numer * that.denom + that.numer * denom, denom * that.denom)
}
```

## 자기 참조

- `this`
  - 현재 실행하고 있는 메서드의 오브젝트 인스턴스를 참조하는 키워드
  - 스칼라에서는 생략가능
    - 하지만 이하의 코드에서는 생략 불가

```scala
def max(that: Rational) =
  if (this.lessThan(that)) that else this
```

두번쨰 `this`는 생략 불가

## 보조 생성자(Auxiliary constructors)

- 주 생성자(primary constructor)이외의 생성자
- 예시
  - `Rational(5, 1)`보다 `Rational(5)`가 더 쓰기 쉽고 알기 쉬움
- 방식
  - `this`라는 메서드로 정의
  - 주 생성자인 `this`에 인자를 고정시킴 혹은 다른 보조 생성자를 이용해서 정의
- **결국 어떠한 보조 생성자도 주 생성자를 호출하는 것으로 오브젝트 인스턴스를 생성함**
- 보조 생성자는 부모 클래스의 생성자를 호출할 수 없음

```scala
class Rational(n: Int, d: Int) {
  require(d != 0)

  val numer: Int = n
  val denom: Int = d

  def this(n: Int) = this(n, 1) // auxiliary constructor
  override def toString = numer + "/" + denom
  def add(that: Rational): Rational = new Rational(
    numer * that.denom + that.numer * denom,
    denom * that.denom
  )
}
```

## private 필드와 메서드

```scala
class Rational(n: Int, d: Int) {
  require(d != 0)

  private val g = gcd(n.abs, d.abs)
  val numer: Int = n / g
  val denom: Int = d / g

  def this(n: Int) = this(n, 1) // auxiliary constructor
  override def toString = numer + "/" + denom
  def add(that: Rational): Rational = new Rational(
    numer * that.denom + that.numer * denom,
    denom * that.denom
  )

  private def gcd(a: Int, b: Int): Int =
    if (b == 0) a else gcd(b, a % b)
}
```

## 연산자 정의하기

- `x + y`와 같은 형태로 메서드를 정의
- +, -, *, / 사이의 우선순위는 스칼라 내장으로 이미 되어있음

```scala
class Rational(n: Int, d: Int) {
  require(d != 0)

  private val g = gcd(n.abs, d.abs)
  val numer: Int = n / g
  val denom: Int = d / g

  def this(n: Int) = this(n, 1) // auxiliary constructor

  def +(that: Rational): Rational = new Rational(
    numer * that.denom + that.numer * denom,
    denom * that.denom
  )

  def *(that: Rational): Rational =
    new Rational(numer * that.numer, denom * that.denom)

  override def toString = numer + "/" + denom

  private def gcd(a: Int, b: Int): Int =
    if (b == 0) a else gcd(b, a % b)
}
```

## 스칼라의 식별자(Identifiers)

- 캐멀케이스
- `val vs constant`
  - val
    - 변경이 불가능해도 일단은 **변수**
    - e.g 메서드의 매개변수는 호출시에 다른 값을 가질 수 있음
  - constant
    - 패턴매칭에 쓰임
    - `XOffset`처럼 캐멀 케이스 사용

## 메서드 오버로딩

- `3 * r`과 같은 표현이 가능하도록
- 메서드 이름이 여러번 사용됨(오버로딩)

```scala
class Rational(val n: Int, val d: Int) {
  require(d != 0)
  val g: Int = gcd(n, d)
  val numer: Int = n / g
  val denom: Int = d / g

  def this(n: Int) = this(n, 1)

  override def toString = numer + "/" + denom

  def +(that: Rational): Rational =
    new Rational(
      numer * that.denom + that.numer * denom,
      denom * that.denom
    )

  def +(i: Int): Rational = new Rational(numer + i * denom, denom)

  def -(that: Rational): Rational =
    new Rational(
      numer * that.denom - that.numer * denom,
      denom * that.denom
    )

  def -(i: Int): Rational =
    new Rational(numer - i * denom, denom)

  def *(that: Rational): Rational =
    new Rational(numer * that.numer, denom * that.denom)

  def *(i: Int): Rational =
    new Rational(numer * i, denom)

  def / (that: Rational): Rational =
    new Rational(numer * that.denom, denom * that.numer)

  def / (i: Int): Rational =
    new Rational(numer, denom * i)

  private def gcd(a: Int, b: Int): Int =
    if (b == 0) a else gcd(b, a % b)
}

```

## Implicit 변환

- `2 * r`을 하는 방법?
- 자동적으로 일반 `Int`를 `Rational`로 변환시켜줌
- `implicit def intToRational(x: Int) = new Rational(x)`
- 같은 스코프에 존재해야 함
- 라이브러리 확장을 위한 매우 강력한 방법
  - 하지만 오용하면 혼란이 따름

```scala
package example

import scala.io.Source

object Hello {
  implicit def intToRational(i: Int):Rational = new Rational(i, 1)

  def main(args: Array[String]) {
    val r1 = new Rational(0, 1)
    val r2 = new Rational(1, 3)
    println(r1 + r2 * r2)
    println(r1 * r2 * r2 + 1)
    println(2 * r2 + r1 * r2)
  }
}

class Rational(val n: Int, val d: Int) {
  require(d != 0)
  val g: Int = gcd(n, d)
  val numer: Int = n / g
  val denom: Int = d / g

  def this(n: Int) = this(n, 1)

  override def toString = numer + "/" + denom

  def +(that: Rational): Rational =
    new Rational(
      numer * that.denom + that.numer * denom,
      denom * that.denom
    )

  def +(i: Int): Rational = new Rational(numer + i * denom, denom)

  def -(that: Rational): Rational =
    new Rational(
      numer * that.denom - that.numer * denom,
      denom * that.denom
    )

  def -(i: Int): Rational =
    new Rational(numer - i * denom, denom)

  def *(that: Rational): Rational =
    new Rational(numer * that.numer, denom * that.denom)

  def *(i: Int): Rational =
    new Rational(numer * i, denom)

  def / (that: Rational): Rational =
    new Rational(numer * that.denom, denom * that.numer)

  def / (i: Int): Rational =
    new Rational(numer, denom * i)

  private def gcd(a: Int, b: Int): Int =
    if (b == 0) a else gcd(b, a % b)
}
```

## 주의

- 스칼라는 쉽게 라이브러리를 간결히 구성할 수 있음. 하지만 힘에는 책임이 따름
- **간결한 코드보다, 읽기쉽고 이해하기 쉬운 코드**
