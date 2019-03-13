# Functions and Closures

- 프로그램을 분리하는 수단
- 메서드: 어떠한 오브젝트의 멤버인 함수
- 함수 속의 함수
- 함수 리터럴
- 함수 값

## 메서드

- 오브젝트의 함수

```scala
object Hello {
  val filesHere = (new java.io.File("./src/main/scala/example")).listFiles

  def main(args: Array[String]): Unit = {
    LongLines.processFile("./src/main/scala/example/Hello.scala", 25)
  }
}

object LongLines {
  def processFile(filename: String, width: Int): Unit = {
    val source = Source.fromFile(filename)
    for (line <- source.getLines())
      processLine(filename, width, line)
  }

  private def processLine(filename: String, width: Int, line: String): Unit = {
    if(line.length > width) {
      println(s"""$filename : $line""")
    }
  }
}

```

## 로컬 함수

- 함수형 프로그래밍 스타일
  - 프로그램은 많은, 각자의 역할을 다하는 작은 함수들로 구성되어야 함
  - 어려운 것들을 행할 수 있도록 많은 블럭을 제공
  - 단점
    - 많은 helper 함수 때문에 네임스페이스가 오염됨
    - 이러한 메서드들을 재사용 가능한 클래스나 오브젝트로 숨기는 것이 바람직
      - `private`키워드 사용
      - 로컬 함수 사용

```scala
import scala.io.Source

object LongLines {
  def processFile(filename: String, width: Int) {
    // inaccessible from outside
    def processLine(line: String) {
      if (line.length > width)
        println(filename + ": " + line)
    }
    val source = Source.fromFile(filename)
    for (line <- source.getLines())
      processLine(line)
  }
}
```

## 퍼스트 클래스 함수

- 함수를 정의하고 실행 할 수 있음
- 함수를 이름 없는 리터럴로 작성하고 그것들을 값으로서 전달 가능
- 함수리터럴과 함수 값
  - 함수 리터럴(클래스, 소스 코드)
  - 함수 값(오브젝트, 런타임, 함수리터럴이 실행됐을 경우(인스턴스))
    - 모든 함수 값은 `FunctionN`트레잇중 하나를 확장한 몇몇 클래스의 인스턴스임
    - `FunctionN`트레잇은 `apply`메서드를 갖고 있음(함수의 호출)

```scala
// 함수가 왼쪽의 임의의 정수를 오른쪽의 x+1로 변환
(x: Int) => x + 1

// 함수 값은 오브젝트이므로 변수에 저장 가능. 호출도 가능
var increase = (x: Int) => x + 1
increase(10) // 11

// 이와 같이사용
val someNumbers = List(-11, -10, -5, 0, 5, 10)
someNumbers.foreach((x: Int) => println(x))
```

## 플레이스 홀더 문법

- 언더스코어는 매개변수 하나를 뜻함(매개변수 하나에 대한 placeholder)
- 첫번째 언더스코어: 첫번째 매개변수
- 두번째 언더스코어: 두번째 매개변수

```scala
someNumbers.filter(_ > 0)

val f = _ + _ // (x) 매개변수 타입추론에서의 정보 부족
val f = (_: Int) + (_: Int)
f(5, 10) // 15
```

## 부분 적용 함수(Partially applied functions)

- 모든 매개변수의 리스트를 `_`로 대체 가능
- 스칼라에서의 인자를 넘겨주는 함수호출
  - 그 함수를 인자에 적용(apply that function to the arguments)
- 부분 적용 함수
  - `val a = sum _`
    - 스칼라 컴파일러가 `sum _`에서 자동으로 생성한 클래스의 인스턴스를 생성
    - 그 인스턴스는 `Function3`트레잇을 믹스인(매개변수가 3개)하고 `apply`메서드가 존재
    - `a(1, 2, 3)`을 함수값의 `apply`메서드 호출로 해석
  - **def(class와 비슷한 역할)를 함수값으로 변환하는 방법이라고 생각**
  - 함수 자체(def)를 변수로 네스팅 하거나, 다른 함수의 인자로 넘겨줄 수 없지만, 언더스코어를 사용해서 함수값으로 만들어주면 위의 것들을 할 수 있음
  - `sum _, println _`와 같은 함수는 다음과 같음
    - `sum, println`
    - 이는 반드시 함수가 온다고 예상된 곳에서만 사용 가능
      - `val c = sum 컴파일 에러`
      - `val d = sum _ 사용 가능`

```scala
def sum(a: Int, b: Int, c: Int): Int = a + b + c

val a = sum _ // (Int, Int, Int) => Int = <function3>
a(1, 2, 3) // Int = 6
```

```scala
val b = sum(1, _; Int, 3)

b(2) // 6 == sum(1, 2, 3)
```

## 클로저

- 함수 정의에서 정의된 매개변수 이외의 변수의 사용

```scala
(x: Int) => x + more
// more: 자유 변수(free variable)
// x: 바운드 변수(bound variable)
```
