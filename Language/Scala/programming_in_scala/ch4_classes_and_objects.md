# Classes and Objects

## 클래스, 필드, 메서드

### 클래스

- 오브젝트의 청사진
- `new`키워드로 오브젝트 생성
- 클래스 정의
  - 필드: 오브젝트의 상태
  - 메서드: 오브젝트의 계산 행위
- 필드는 외부에서 접근하지 않는경우 `private`으로
  - 그 클래스 안에 정의된 메서드에서만 접근 가능
  - 상태를 갱신하는 코드는 클래스 내로 한정됨
- 메서드
  - **메서드 매개변수는 모두 val이다**
  - `return`을 명시적으로 나타내지말고, 메서드 자체를 하나의 값을 반환하는 식이라고 생각하라
    - 보다 작은 메서드를 만들 수 있게 함
  - 하나의 결과 식만 계산하면 중괄호 생략가능
  - `Unit`타입의 결과를 내는 메서드는 부작용을 위해서 작성됨(프로시저)
    - 외부 세계의 상태를 변경, I/O 작용을 함
    - 함수의 내용 앞에 `=`가 없으면 이는 `Unit`함수임
    - 반환될 식이 있어도 `Unit`으로 타입 변환
    - **무엇인가 반환할때는 항상 `=`가 존재해야함**

## 세미콜론 추론

- 다양한 문(statement)을 하나의 줄에 쓰려면 세미콜론 필요

## 싱글톤 오브젝트

- 스칼라의 클래스는 정적 멤버를 갖을 수 없음(no static member)
- 대신 싱글톤 오브젝트를 갖음
- 클래스와 싱글톤 오브젝트가 같은 이름을 갖으면, 이를 클래스의 **동료 오브젝트**라 함
  - 반드시 같은 파일에 정의해야함
  - 클래스와 싱글톤 오브젝트는 서로서로의 프라이빗 멤버에 접근 가능
  - 정적 멤버들의 고향이라고 생각하면 편함
- 새로운 변수가 생긴것이 아니라, 같은 이름의 타입이 싱글톤 오브젝트에 의해서 정의된것
- `superclass`확장과 trait의 `mix-in`가능
- 매개변수로 줄 수 없음
  - `new`로 초기화 불가능
- 동료 오브젝트로 사용되지 않으면, **독자 오브젝트(standalone object)**로 불림

```scala
import scala.collection.mutable.Map

object ChecksumAccumulator {
  private val cache = Map[String, Int]()
  def calculate(s: String): Int = {
    if (cache.contains(s)) {
      cache(s)
    } else {
      val acc = new ChecksumAccumulator
      for (c <- s)
        acc.add(c.toByte)
      val cs = acc.checksum()
      cache += (s -> cs)
      cs
    }
  }
}
```

## 스칼라 애플리케이션

- 스칼라 애플리케이션 실행
  - `Array[String]`를 인자로 받고 `Unit`을 반환하는 `main`메서드를 갖는 독자 싱글톤 오브젝트가 존재해야함
  - 스칼라는 암묵적으로 `java.lang`과 `scala`라는 패키지와  `Predef`라는싱글톤 오브젝트를 임포트
    - `Predef`에 `println`과 같은 유용한 메서드 포함(사실은 `Console.Predef`를 래핑)

```scala
import ChecksumAccumulator.calculate

object Summer {
  def main(args: Array[String]) {
    for (arg <- args)
      println(arg + ": " + calculate(arg))
  }
}
```

## 애플리케이션 트레잇

```scala
import ChecksumAccumulator.calculate

object FallWinterSpringSummer extends Application {
  for (season <- List("fall", "winter", "spring"))
    println(season + ": " + calculate(season))
}
```

- 위와같이 `Application`이라는 트레잇을 적용시키는 것으로 메인 애플리케이션을 만들 수 있음
  - 하지만 커맨드라인 인자는 받을 수 없음
  - 멀티스레딩 프로그램도 작성 불가
  - 가끔 작동할 수 없는 JVM도 있음
