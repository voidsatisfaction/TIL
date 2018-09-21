# Trait

## 장점

- 여러개의 트레잇을 하나의 클래스나 트레잇에 믹스인 할 수 있음
- 직접 인스턴스화 할 수 없음
- 클래스 매개변수를 받을 수 없음
- 메서드 뿐 아니라 값도 갖을 수 있음

```scala
new Trait {} // 이는 가능. 왜냐하면, trait을 계승한 이름이 없는 클래스를 만들어서 그 인스턴스를 생성했기 때문
```

```scala
triat A {
  val foo: String
}

trait B extends A {
  val bar = foo + "World"
}

class C extends {
  val foo = "Hello"
} with B {
  def printBar(): Unit = println(bar) // HelloWorld
}
```
