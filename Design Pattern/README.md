# 디자인 패턴

- 목차
  - 디자인 패턴이란
    - 정의
    - 역사
  - 디자인 패턴과 언어
  - 디자인 패턴의 분류
  - UML 표기 소개
  - 대표적인 디자인 패턴(Head first)
    - Creational Pattern
    - Structural Pattern
    - Behavioral Pattern

## 디자인 패턴이란

- 정의
  - 설계 문제에 대한 해답을 문서화하기위해 고안된 형식 방법
  - **과거의 소프트웨어 개발 과정에서 발견된 설계의 노하우를 축적하여 이름을 붙여, 이후에 재이용하기 좋은 형태로 특정의 규약을 묶어서 정리한 것**
- 역사
  - 크리스토퍼 알렉산더가 제안한, 건축의 여러 기법을 틀로 고안한 아이디어. 기존의 작은 패턴을 묶어서 조합하여 건물 / 도시를 설계
  - 각각의 패턴은 **패턴 언어**를 통해 기술 / 정리
    - 건축가가 아닌 사람도 원하는 설계를 전문가에게 정확히 전달할 수 있게 도와줌

## 런타임 오브젝트 디자인 패턴과 컴파일 타임 클래스 디자인 패턴

- 런타임 오브젝트 디자인 패턴
  - 오브젝트의 커뮤니케이션이나, polymorphism, DI 등을 이용해서 구현
  - 런타임에 동작이 확정되고, 구현보다 추상화에 의존하기 때문에 컴파일 타임 클래스 디자인 패턴보다 보다 loose한 속박
  - 대신 코드 실행에 있어서는 다소 오버헤드 발생
- 컴파일 타임 클래스 디자인 패턴
  - 상속을 이용해서 구현
  - 컴파일 타임에 동작이 확정되기 때문에 런타임 오브젝트 디자인 패턴보다 tight한 속박
  - 대신 코드 실행에 있어서는 보다 나은 최적화

## 디자인 패턴과 언어

- 디자인 패턴에서 나온 다양한 패턴들을 언어 자체가 언어의 명세로서 구현하는 경우도 있다.
  - e.g
    - OOP 지향 언어의 오브젝트의 컨스트럭터
    - 루비의 `module` 키워드(mixin)

## [디자인 패턴의 분류](https://en.wikipedia.org/wiki/Software_design_pattern)

이미 알고있는 것은 기울기가 없는 글자로 표현

- Gang of Four patterns
  - Creational
    - *Abstract factory / Builder / Factory method / Prototype / Singleton*
  - Structural
    - *Adapter / Bridge / Composite / Decorator / Facade / Flyweight / Proxy*
  - Behavioral
    - Strategy / Observer / Template method
    - *Chain of responsibility / Command / Interpreter / Iterator / Mediator / Memento / State / Template method / Visitor*
- Concurrency patterns
  - *Active object / Balking / Binding properties / Double-checked locking / Event-based asynchronous / Guarded suspension / Join / Lock / Monitor / Proactor / Reactor / Read write lock / Scheduler / Thread pool / Thread-local storage*
- Architectural patterns
  - Inversion of control
  - *Front controller / Interceptor / MVC / MVP / MVVM / ECS / n-tier / Specification / Publish-subscribe / Naked objects / Service locator / Active record / Identity map / Data access object / Data transfer object / Model 2*
- Other patterns
  - Dependency injection
  - *Blackboard / Business delegate / Composite entity / Intercepting filter / Lazy loading / Mock object / Null object / Object pool / Servant / Twin / Type tunnel / Method chaining / Dlegation*

---

또 다른 분류 방법

- Creational pattern
  - 오브젝트 생성 매커니즘을 다룸
  - 각 상황에 맞도록 오브젝트를 생성하도록 도와줌
- Structural pattern
  - 엔티티들 사이의 관계를 쉽게 확인할 수 있는 방법을 구현
    - 엔티티의 관계 구조를 명확히 할 수 있도록 하는 패턴
- Behavioral pattern
  - 오브젝트 사이의 공통 커뮤니케이션 패턴을 확인하여 커뮤니케이션을 행하는데에 유연함을 제공

## UML소개

![](./images/uml_is_a_has_a.png)

- 화살표의 방향으로 **의존한다** 라는 뜻
  - A <- B
    - B는 A에 의존한다
- is_a 관계
  - `A <|- B`
  - B는 A의 종류중 하나
- has_a 관계
  - `A <- B`
  - B는 A를 갖고 있음

## 대표적인 디자인 패턴

### Creational pattern

#### 1. Factory Pattern

![](./images/uml_factory.png)

- 정의
  - 오브젝트를 생성하기 위한 인터페이스를 정의하는 것. 다만, 팩토리 메서드는 서브클래스가 어떤 클래스를 인스턴스화 하는가를 결정하게 함
  - 생성 로직을 일반화시켜서 파라미터화 하는 것

### Structural pattern

#### 1. Decorator Pattern

![](./images/example_decorator.png)

![](./images/uml_decorator.png)

**Decorator Pattern 코드 예시**

```scala
package DesignPattern

object DesignPattern extends App {
  val espressoWithCaramel: Beverage = new Caramel(new Espresso())

  println(espressoWithCaramel.cost())
}

abstract class Beverage {
  def cost(): Int
}

class Espresso extends Beverage {
  override def cost(): Int = 4
}

abstract class AddOnDecorator extends Beverage {
  def cost(): Int
}

class Caramel(val beverage: Beverage) extends AddOnDecorator {
  def cost(): Int = beverage.cost() + 2
}

```

**함수형 프로그래밍에서의 유사 Decorator Pattern**

```js
// aws lambda를 hexagonal architecture형태로 구현하기
// 오브젝트를 꾸며주는 것이 아니므로, decorator pattern이라고 할 수는 없으나, 함수를 래핑해준다는 점에서 참고할만함

// 일반적으로, application은 다음과 같은 모양을 띔(DI를 적용한 경우)
const app = (input, { dependency1, dependency2 }) => {
  // business logics
  // ...
  return output
}

// 하지만 최종적으로 lambda핸들러는 (event, context, callback) => ... 형태를 띄어야 함
const handler = (adapter) => (event, context, callback) => {
  // business 로직을 실행하기 위한 dependency들
  const createDependencies = () => ({
    dependency1: createDependency1(),
    dependency2: createDependency2()
  })
  // ....
  adapter(event, createDependencies())
}

// handler와 app의 서로 다른 인터페이스를 이어주기 위해서 adapter를 생성
const adapter = (app) => (event, { dependency1, dependency2 }) => {
  return response(app(convertToInput(event), { dependency1, dependency2 }));
}

// app의 비즈니스 로직을 handler와 adapter로 래핑
exports.handler = handler(adapter(app))
```

**Decorator Pattern vs 미들웨어(특히 서버에서)**

- Decorator Pattern
  - 가장 초기에 생성한 오브젝트를 변경하지 않음(immutability)
  - 단순히 래핑해서 responsibility가 확장
    - 특히, 오브젝트의 행위의 responsibility확장
- Middleware
  - 가장 초기에 생성한 오브젝트를 변경할 수 있음(mutability)
  - 실행의 흐름을 변경할 수 있음(부작용 존재)
    - 인증 middleware를 이용해서, 로그인상태가 아닌 유저를 login페이지로 리다이렉팅 시킴
    - https로 주소 연결을 하지 않은 클라이언트를 강제로 https로 redirect시켜줌

- 정의
  - 런타임에 특정 오브젝트를 변경시키지 않고, 어떠한 오브젝트의 속성이나 메서드의 행위를 변경 / 혹은 추가 시키는 방법
    - 동적으로(런타임에서) 특정 오브젝트의 역할을 늘려줌
  - 오브젝트의 래핑
  - 데코레이터는 컴포넌트를 갖을 뿐아니라, 자기자신이 컴포넌트다
  - 서브클래스의 extends보다 더 유연한 오브젝트 확장 방식을 제공
  - Open Close Principle를 지원
  - 상속관계에서 Interface Segregation Principle을 지킬 수 있도록 함
    - 부모클래스가 Beverage고, 자식 클래스가 Espresso인 경우에 Beverage에 있는 메서드가 Espresso에서는 필요 없는 경우가 생김.
    - Decorator Pattern은 위의 문제를 해결 가능
- 적용

#### 2. Adapter Pattern

![](./images/uml_adapter.png)

**코드 에제**

```scala
package DesignPattern

object AdapterPattern extends App {
  val adapter: ITarget = new Adapter(new Adaptee())
  val client: Client = new Client(adapter)

  client.doSomething()
}

class Client(val target: ITarget) {
  def doSomething(): Unit = {
    // do...
    target.request()
    // ...
  }
}

trait ITarget {
  def request(): Unit
}

class Adapter(val adaptee: Adaptee) extends ITarget {
  def request(): Unit = adaptee.specificRequest()
}

class Adaptee() {
  def specificRequest(): Unit = {
    println("this is specific request")
  }
}
```

- 정의
  - 클라이언트는 특정 인터페이스를 갖고 있는데, 어떠한 어댑티는 그 인터페이스를 만족하지 못하므로, 어댑터가 클라이언트의 특정 인터페이스를 만족하도록 래핑해서 클라이언트가 어댑티를 사용할 수 있도록 래핑 함
  - Client는 request라는 메서드를 실행하고 싶은데, 그것을 실행하는 대상은 request라는 메서드 인터페이스를 따르지 않으므로, adapter를 만들어서, adapter가 request라는 메서드로 메시지를 받고 그것을 원래 실행하려던 대상에게 다시 메시지를 보내서 원하는 결과를 받음
- 특성
  - 원래의 client를 변경하지 않아도 adaptee의 인터페이스 변화를 대처할 수 있음
    - 만약 adaptee가 외부 라이브러리라면?
    - OCP
  - 원래 갖고 있던 logic을 변화시키는 것이 아님. 의존하는 모듈 / 모브젝트의 인터페이스의 변화에 OCP원칙을 지켜가며 대처하기 위함
  - 혹은 기존의 구현에다가 adapter를 씌워서 interface를 변화시키는 용도로 사용할수도 있음
    - 이 용도도, 기존 코드를 직접 변경하지 않음
- 어댑터 패턴의 종류
  - 동적 합성
  - 다중 상속

#### 3. Facade Pattern

![](./images/uml_facade_pattern.png)

- 정의
  - 서브 시스템을 쉽게 사용할 수 있도록 추상화한 통합된 인터페이스
  - 클라이언트가 내부의 복잡한 내용의 로직을 추상화한 Facade를 이용해서 쉽게 오브젝트의 로직을 사용할 수 있도록 함

#### 4. Proxy Pattern

![](./images/uml_proxy_pattern.png)

**구현 예시**

```scala
trait IBookParser {
  def getPageNumber(): Int
}

class BookParser(val filePath: String) extends IBookParser {
  val book = // really huge book, takes so long time to parse from the file path
  def getPageNumber: Int = book.getNumber()
}

class LazyBookParserProxy extends IBookParser {
  var bookParser = None
  def getPageNumber(): Int = bookParser match {
    case None => {
      // lazy instantiation
      bookParser = Some(new BookParser("filePath"))
      bookParser.getNumber()
    }
    case Some(bookParser) = bookParser.getNumber()
  }
}
```

- 정의
  - 다른 오브젝트에 대한 **접근** 을 제어하기 위해서 같은 인터페이스의 대리 오브젝트를 제공하는 것
  - 구현 오브젝트에 대한 접근(access)에 더 초점을 둔 디자인 패턴
    - 접근에 대한 제어를 목표로 함
    - 캐싱을 위해서 사용하는 경우가 있음(HTML 캐싱 등)
  - **인터페이스의 변환은 없음**
    - 캐싱이나 로깅을 위해서 사용되는 경우가 있음
    - decorator 패턴과의 차이
- 종류
  - remote
    - 원격에 있는 요소를 접근하기 위해서 사용
    - 예시
      - 원격 서버
      - 원격 code project
  - virtual
    - 생성하는데에 많은 자원을 사용하는 요소를 접근하기 위해서 사용
    - 캐싱 / lazy evalution 과 비슷한 개념
  - protection
    - protection되고 있는 자원을 사용할 수 있는 권한이 있는 유저만 사용할 수 있도록 함

#### 5. Bridge Pattern

![](./images/uml_bridge_pattern.png)

**구현 코드 예시**

```scala
package DesignPattern

object BridgePattern extends App {
  val resource: IResource = new ArtistResource(new Artist("min"))
  val longFormView: LongForm = new LongForm(resource)

  longFormView.show
}

abstract class View {
  def show(): Unit
}

class LongForm(val resource: IResource) extends View {
  def show(): Unit = {
    println(resource.snippet)
    println(resource.title)
  }
}

trait IResource {
  def snippet(): String
  def title(): String
}

class ArtistResource(val artist: Artist) extends IResource {
  def snippet(): String = artist.bio + " snippet"
  def title(): String = artist.genre + " title"
}

class Artist(val name: String) {
  def bio(): String = "My bio " + name
  def genre(): String = "My genre is " + name
}
```

- 정의
  - 구현으로부터 추상성을 디커플링해서 서로를 독립적으로 다룰 수 있도록 함
  - 서로 다른 다형 계층(polymorphic hierarchy)을 이어주는 패턴
  - Strategy 패턴 + Adapter 패턴
  - Class들의 Cartesian Product문제 해결가능
  - e.g
    - Controller와 View의 합성
      - 물론 이 경우에는 Controller가 View를 갖고, View가 Controller를 갖게 구현할 수 있음

### Behavioral pattern

#### 1. Strategy Pattern

![](./images/uml_strategy_pattern.png)

- Defines a family of algorithms
- Encapsulate & Interchangeable
- Independent to client that uses it
  - decouple
- 나는 무엇인가 하고 싶은데, 그것이 구체적으로 어떻게 구현되는지는 관심없음
  - 그래서 외부로부터 인터페이스를 통해서 구체적인 구현을 받아들이고
  - 나는 그 인터페이스를 통해서 필요할 때 그 기능을 호출한다
- Program to Interfaces, not implementations

```scala
trait IFlyBehavior {
  def fly(): Unit
}

trait IQuackBehavior {
  def quack(): Unit
}

trait IDisplayBehavior {
  def display(): Unit
}

class Duck(
  flyingBehavior: IFlyBehavior,
  quackBehavior: IQuackBehavior,
  displayBehavior: IDisplayBehavior
) {
  def fly(): Unit =
    flyingBehavior.fly

  def quack(): Unit =
    quackBehavior.quack

  def display(): Unit =
    displayBehavior.display
}

val wildDuck: Duck = new Duck(fb, qb, db)
val mountainDuck: Duck = new Duck(fb2, qb2, db2)
```

- 적용
  - 암호화폐 자동거래 시스템의 시뮬레이터
    - 다양한 전략이 존재하기 때문에, 그전략들을 돌아가면서 검증해야 함
    - 이 떄에 strategy 패턴을 사용해서, 각각의 전략의 parameter를 Interchangeable하게 하면 검증하고 테스트하기 쉬울 듯

#### 2. Observer Pattern

![](./images/2_uml_observer_pattern.png)

- Polling vs Pushing
  - Polling
    - 관찰의 주체(관찰을 하는 엔티티)가 주기적으로 관찰의 대상의 상태를 확인
  - Pushing
    - 관찰의 대상이 자신의 상태가 변경 되었을 때, 관찰의 주체에게 그것을 알려줌
    - 리모컨 조작
- One-to-many dependency
- One object change state => all of its dependency notified / updated automatically

```scala
trait IObserver {
  def update(): Unit
}

trait IObservable {
  def add(observer: IObserver): Unit
  def remove(observer: IObserver): Unit
  def notify(): Unit
}

class WeatherStation extends IObservable {
  private var temperature: Int = 0
  private var observers: List[IObserver] = List[IObserver]()

  def add(observer: IObserver): List[IObserver] = {
    observers = observer :: observers
  }

  def remove(observer: IObserver): Unit = {
    observers = observers.filter(_ != observer)
  }

  def notify(): Unit = {
    observers.foreach(_.update)
  }

  def getTemperature(): Int = temperature
}

class PhoneDisplay(weatherStation: WeatherStation): IObserver {
  // send data via update function's parameter
  // then, this observer does not need to have observable data
  def update(): Unit = {
    weatherStation.getTemperature

    // ...
  }
}
```

- 적용
  - 암호화폐 자동거래 시스템의 Balance 기록 시스템
    - 물론, 거래소 마다 Balance를 알아보는 것은 polling으로 밖에 할 수 없다.
    - 하지만 그것을 wrapping해서 마치 푸시할 수 있는 것 처럼 Observable로 둔다.
    - 그리고 Observer로 그것을 구독하게 하고, 변화가 있으면 update함수를 Observable에서 호출하면 Balance를 데이터베이스에 기록하게 한다.
    - 이렇게 하면 DB에 데이터를 기록하는 컴포넌트와 거래소의 Balance의 변화를 탐지하는 컴포넌트가 loosely coupled된다.

#### 3. Command Pattern

![](./images/uml_command_pattern.png)

**구현 코드**

```scala
package DesignPattern

object CommandPattern extends App {
  val invoker = new Invoker(new Command(new Receiver()))

  invoker.clickOn()
  invoker.clickOff()
}

class Invoker(val lightOnCommand: ICommand) {
  def clickOn(): Unit = lightOnCommand.execute()
  def clickOff(): Unit = lightOnCommand.unExecute()
}

trait ICommand {
  def execute(): Unit
  def unExecute(): Unit
}

// Macro command is also possible
class Command(val receiver: Receiver) extends ICommand {
  def execute(): Unit = println(receiver.on)
  def unExecute(): Unit = println(receiver.off)
}

class Receiver {
  val on = "on"
  val off = "off"
}
```

- 정의
  - 리퀘스트(command)를 오브젝트로 캡슐화 하여, 이를 파라미터화 해서 큐잉하거나 로깅하거나 undo할 수 있도록 함
  - invoker에게 command를 심어주고, command를 실행하면 receiver의 특정한 행동을 실행시킴
  - 예시
    - 리모트 콘트롤러
- 특성
  - 단순히 커맨드를 한 오브젝트에 구현하는게 아니고, Command를 래핑하므로써, undo역시 가능하게 함
  - 또한, Macro Command를 두어서, 다양한 Command를 하나의 Command가 실행할 수 있도록 함

### 4. Template Method Pattern

![](./images/uml_template_method.png)

- IOC(Inversion Of Control)과 깊은 관계가 있음
- Super class에 Template method를 정의해두고 Subclass에서 Template method에 필요한 일부 서브 로직을 구현
- 장점
  - 공통된 로직 구성을 서브 클래스를 추가하는 것으로 쉽게 재사용 할 수 있음
  - 프레임 워크 IOC를 구현하기에 용이. 서브클래스는 자기자신이 언제 호출되는지 신경쓰지 않아도 됨(복잡성이 낮아짐)
  - e.g
    - Active record
    - Validation
    - Arbitrage Executor(각각의 거래소)
- 단점
  - 상속을 이용하므로, 클래스 사이의 커플링이 심해짐.
  - 앞으로 Template method의 컨트롤 내용이 많이 변하지 않는다는 것을 전제할 때에 사용해야 함(결국 코드의 변화가 생기면 서브 클래스의 메서드를 전부 변화시켜야 할 가능성도 존재)
  - 그냥 Strategy패턴을 사용하는 것이 좋을 수도 있음
