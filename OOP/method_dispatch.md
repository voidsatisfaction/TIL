# Method dispatch & Double dispatch

- Method dispatch
  - 정의
  - 종류
  - Method signature vs Method type
- Double dispatch

## Method dispatch

### 정의

- 어떤 메서드를 호출할것인지를 결정해서 실제로 그것을 실행하는 과정

### 종류

- static dispatch
  - 컴파일 시점에 정확히 어느 메서드가 호출되는지 알 수 있는 경우
  - 이미 바이트코드에 적용됨
  - e.g
    - 메서드 오버로딩
- dynamic dispatch
  - 런타임 시점에 정확히 어느 메서드가 호출되는지 알 수 있는 경우

```scala
// dynamic method dispatch
abstract class Service {
  def run(): Unit
}

class MyService1 extends Service {
  def run(): Unit = {
    println("run1")
  }
}

class MyService2 extends Service {
  def run(): Unit = {
    println("run2")
  }
}

object Main extends App {
  val myService1: Service = new MyService1()

  myService1.run()

  val services: List[Service] = List(new MyService1(), new MyService2())
  // MyService1의 this, MyService2의 this가 리시버로 들어옴
  // 동적으로 run()호출
  services.foreach(_.run())
}
```

### Method Signature vs Method Type

- Method Signature
  - name
  - parameter types
  - 위의 둘이 같으면 오버라이딩이 가능 / 둘 이상 정의 불가능
- Method Type(method reference)
  - method type parameter
  - method parameter types
  - return type
  - exception

## Double dispatch

- 동적 디스패치를 둘 이상 적용하는 것
- 기능 추가 자유로움
- 다형성의 다형성
- c.f) multi dispatch
  - commonlisp
  - julia
  - clojure
- visitor pattern과 깊은 관계가 있음 & proxy visitor pattern
- 프록시가 되어있는 경우, instanceof를 이용해서 엔티티체크가 불가능한 경우가 있으므로, 이러한 double dispatch방식을 이용해서 내부까지 접근해서 확인하는것이 필요한 경우가 있음

```scala
trait Post {
  def postOn(sns: SNS): Unit
}

class Text extends Post {
  def postOn(sns: SNS) {
    // 올바른 구현
    // dynamic dispatch based on sns
    // parameter dynamic dispatch는 지원하지 않으므로, paramter를 receiver로 치환해서 dynamic dispatch를 구현
    sns.post(this)
  }

  // 올바르지 못한 구현
  // multiple dispatch
  // error at scala / java / etc
  // arguments(not this) cannot be bound
  def postOn(sns: Facebook): Unit = println("text -> Facebook")
  def postOn(sns: Twitter): Unit = println("text -> Twitter")
}

class Picture extends Post {
  def postOn(sns: SNS) {
    // dynamic dispatch based on sns
    sns.post(this)
  }
}

trait SNS {
  def post(post: Text): Unit
  def post(post: Picture): Unit
}

class Facebook extends SNS {
  def post(post: Text): Unit = println("text -> Facebook")
  def post(post: Picture): Unit = println("picture -> Facebook")
}

class Twitter extends SNS {
  def post(post: Text): Unit = println("text -> Twitter")
  def post(post: Picture): Unit = println("picture -> Twitter")
}

class GooglePlus extends SNS {
  def post(post: Text): Unit = println("text -> GooglePlus")
  def post(post: Picture): Unit = println("picture -> GooglePlus")
}

object Main extends App {
  val posts: List[Post] = List(new Text(), new Picture())
  val sns: List[SNS] = List(new Facebook(), new Twitter(), new GooglePlus)

  posts.foreach((post: Post) => {
    sns.foreach((sns: SNS) => {
      // dynamic dispatch based on post
      post.postOn(sns)
    })
  })
}
```
