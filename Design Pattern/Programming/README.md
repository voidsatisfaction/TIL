# Programming Design Pattern

## 인터페이스 vs 클래스

- 인터페이스는 행위(메서드)를 일반화 한 것
- 클래스는 오브젝트가 갖는 데이터를 일반화 한 것

클래스에 의하여 생성된 오브젝트들을 인터페이스를 이용해서 즉, 같은 동작(메서드)를 갖는 오브젝트로 묶어서 사용. 다형성을 구현(Polymorphism)

루비와 같은 타입이 없는 언어에서는 인터페이스가 필요가 없음. 그냥 그 메서드를 갖으면 사용 가능(덕타이핑)

고와 같은 타입이 있는 언어에서는 타입이 다르면 애초에 메서드를 불러낼 수 없으므로 인터페이스를 이용해서 또 다른 묶음을 제공할 필요가 있다.

## Composition over inheritance

클래스의 상속(inheritance)은 다중상속이 일어나 죽음의 다이아몬드가 형성될 수 있다. 그러므로 상속보다는 인터페이스를 이용한 Composition을 사용해야 한다는 오브젝트지향 프로그래밍의 디자인 패턴이다.

- 장점
  - 보다 큰 유연성
  - 비 계층적인 구조
- 단점
  - 인터페이스 구현을 모든 타입에서 다 똑같이 같은 코드를 써야한다.
  - e.g golang의 sort의 경우...
  - 대신 이는 delegate패턴으로 극복 가능

c.f delegate패턴이란, 인터페이스의 적용을 위해서, 메소드의 정의를 대표(delegate)해주는 오브젝트를 직접 넘겨주므로써, 대표되는 오브젝트의 메소드 정의를 대신 해주는 것을 말한다.

```Kotlin
class Rectangle(val width: Int, val height: Int) {
    fun area() = width * height
}

class Window(val bounds: Rectangle) {
    // Delegation
    fun area() = bounds.area()
}
```
