# Model-Driven Design

## 개관

## Model-Driven Design Patterns

### 1. Layered Architecture

예시

[from Domain-Driven Design Quickly](http://infoq.com/books/domain-driven-design-quickly)

> For example, a typical, the interaction of the application, domain and infrastructure could look like this. The user wants to book a flights route, and asks an application service in the application layer to do so. The application tier fetches the relevant domain objects from the infrastructure and invokes relevant methods on them, e g to check security margins to other already booked flights. Once the domain objects have made all checks and updated their status to “decided”, the application service persists the objects to the infrastructure.

#### Entities

OOP 언어들은 오브젝트를 메모리에 보유한다. 그리고 각각의 오브젝트를 참조나 메모리 주소로 연동한다. 이러한 참조는 일정 시간동안 각각의 오브젝트에 있어서 독립적이지만 언제까지나 그럴 것이라고 단정할 수 없다. 오히려 오브젝트는 메모리안에서 계속 이리저리 움직이고 변화하고 사라진다. 예를들면, 날씨 정보를 갖는 클래스가 있는데, 온도를 state로 갖는다고 하자. 하지만 별개의 다른 오브젝트가 같은 온도를 갖을 수 있다. 이 두 오브젝트들은 완벽히 같고, 서로 바꿀 수 있지만 다른 **참조(references)**를 갖는다. 그러므로 그들은 entities가 아니다.

오브젝트는 반드시 구분지을 수 있는 id를 갖아야 한다(e.g. 사람 클래스에서 주민번호의 state라던지) 그렇지 않으면, data corruption이 일어난다.

그러므로, 소프트웨어에서 entities를 도입한다는 것은 id를 만드는 것을 의미한다. 보통, id는

- an attribute of the object
- a combination of attributes
- an attribute specially created to preserve and express identity
- a behaviro

두 오브젝트가 쉽게 구분되기 위해서 시스템에 의한 다른 id를 갖는 장치가 있는것이 매우 중요하다. (그렇지 않으면 data corruption이 일어나기 때문)

[from Domain-Driven Design Quickly](http://infoq.com/books/domain-driven-design-quickly)

> When an object is distinguished by its identity, rather than its attributes, make this primary to its definition in the model. Keep the class definition simple and focused on life cycle continuity and identity. Define a means of distinguishing each object regardless of its form or history. Be alert to requirements that call for matching objects by attributes. Define an operation that is guaranteed to produce a unique result for each object, possibly by attaching a symbol that is guaranteed unique. This means of identification may come from the outside, or it may be an arbitrary identifier created by and for the system, but it must correspond to the identity distinctions in the model. The model must define what it means to be the same thing.

Entities는 도메인 모델의 중요한 오브젝트들이고, 그것들은 modeling process의 시작부터 중요하게 고려되어야 한다. 단순히 오브젝트가 entity가 되어야하는지 아닌지 판단하는것도 매우 중요하다.

#### Value Objects

Entities는 Domain model에서 매우 중요한 역할을 차지하지만, 모든 오브젝트가 반드시 entity여만 할까? 그래서 모든 오브젝트는 id를 갖고 있어야 할까?

만일 그림 그리기 어플리케이션을 만든다고 할때, 유저가 하나의 점을 찍는 것을 고려해서 Point클래스를 만들고 그 인스턴스변수로는 x좌표 y좌표를 넣을 수 있다고 할때, 과연 이 클래스의 인스턴스(오브젝트)는 id를 갖고 있어야 할까? => 그렇지 않다.

어떤 오브젝트인지는 관심없고, 어떤 속성을 갖고 있는지만 관심 있는 오브젝트 => Value Object

- Entity Objets와 Value Objects를 구분하는 것이 중요하다.
- Entity definition을 만족해야 하는 것만을 entity object로 해야한다.
- 그리고 나머지 오브젝트를 Value Objects로 한다.

위와 같은 조건은 디자인을 간단화 시킬 것이며, 다른 긍정적인 효과가 있을 것이다.

**특징**

- 쉽게 쓰이고 쉽게 버려진다.
- **Sharable & Immutable**: golden rule
  - 언제든지 복제하고 언제든지 버릴 수 있다.

### 2. Modules

### 3. Aggregates
