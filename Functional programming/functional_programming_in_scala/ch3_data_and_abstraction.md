# Data and Abstraction

## 3.1 Class Hierarchies

- 평가 모델이 중요
- 실재 메서드는 해당 메서드의 리시버의 런타입 타입에 따라 달라짐(동적 바인딩)

### 추상 클래스

```scala
abstract class IntSet {
  def incl(x: Int): IntSet
  def contains(x: Int): Boolean
}
```

- 추상 클래스
  - 구현이 없는 멤버를 포함할 수 있음
  - 결국 어떠한 오브젝트도 추상 클래스로부터 생성 불가능(`new`키워드 사용 불가)

### 클래스 확장

- 집합을 구현을 이진트리로 한다고 생각하자
- 두가지의 가능한 트리의 형태가 존재
  - 빈 집합을 위한 트리
  - 정수로 구성된 트리와 그것의 두개의 서브트리

```scala
class Empty extends IntSet {
  def contains(x: Int): Boolean = false
  def incl(x: Int): IntSet = new NonEmpty(x, new Empty, new Empty)
}
```

![](./images/persistant_data_structure.png)

- 영구 데이터 구조(Persistant data structure)
  - 변경할때도 데이터 구조의 예전 버전은 유지되고 없어지지 않음

```scala

abstract class IntSet {
  def contains(x: Int): Boolean
  def incl(x: Int): IntSet
}

class NonEmpty(elem: Int, left: IntSet, right: IntSet) extends IntSet {
  def contains(x: Int): Boolean =
    if (x < elem) left contains x
    else if (x > elem) right contains x
    else true

  def incl(x: Int): IntSet =
    if (x < elem) new NonEmpty(elem, left incl x, right)
    else if (x > elem) new NonEmpty(elem, left, right incl x)
    else this

  override def toString = "{" + left + elem + right + "}"
}

class Empty extends IntSet {
  def contains(x: Int): Boolean = false
  def incl(x: Int): IntSet = new NonEmpty(x, new Empty, new Empty)
  override def toString = "."
}

```

### 용어

- `Empty`와 `NonEmpty`는 둘다 `IntSet`을 상속한 것
  - 타입 `Empty` 와 `NonEmpty` 는 타입 `IntSet`을 따르게 됨
  - InSet타입의 오브젝트가 필요한 곳에 어디든지 `Empty`와 `NonEmpty`가 사용될 수 있음
- InSet은 Empty와 NonEmpty의 **수퍼 클래스임**
- Empty와 NonEmpty는 IntSet의 **서브 클래스**
- 스칼라에서는 유저가 정의한 클래스는 어떠한 다른 클래스를 상속함
  - 수퍼 클래스가 주어지지 않으면, 표준 클래스 자바의 패키지 java.lang안에 있는 `Object` 클래스(모든 자바 클래스의 루트 클래스)를 상속한다고 추정
  - 클래스 C의 직접적인 / 직접적이지 않은 수퍼클래스는 **C의 베이스 클래스** 라고 함
  - e.g NonEmpty의 베이스 클래스는 IntSet과 Object임

### 구현과 오버라이딩

- Empty와 NonEmpty클래스의 메서드 contains와 incl의 정의는 베이스 트레잇 IntSet에서의 추상 함수를 구현한 것임
- 오버라이딩을 사용해서 수퍼클래스에 현존하는 non-abstract 정의를 재정의 할 수 있음

### 오브젝트 정의

- IntSet의 예시에서는 하나의 empty IntSet만 사실상 필요함
- 이를 오브젝트 정의를 활용해서 더 효율적으로 나타낼 수 있음
- 이는 **싱글톤 오브젝트**
  - 다른 `Empty`라는 이름을 가진 오브젝트는 생성될 수 없음
  - 싱글톤 오브젝트는 값임
  - Empty는 자기자신을 평가

```scala
object Empty extends IntSet {
  def contains(x: Int): Boolean = false
  def incl(x: Int): IntSet = new NonEmpty(x, Empty, Empty)
}
```

### 프로그램

- 이제까지는 REPL로만 스칼라 코드를 실행시킴
- 독자적인 스칼라 애플리케이션을 만드는 것도 가능
  - 모든 그러한 애플리케이션은 main메서드를 갖고있는 오브젝트를 포함함

### 동적 바인딩(Dynamic Binding)

![](./images/dynamic_binding_1.png)

![](./images/dynamic_binding_2.png)

- 객체지향 언어들은 동적 메서드 호출 방식을 구현함
  - 그 메서드를 포함하고 있는 객체의 런타임 타입에 기반하여 해당 메서드에 관한 코드가 실행됨
  - **대체 모델에 기반해서 적용됨**
- 생각해볼 것
  - **동적 호출은 고차함수와 매우 유사**
  - Q 하나의 컨셉을 다른 컨셉으로 구현할 수 있는가?
    - 고차함수로 오브젝트를 구현할 수 있는가?
    - 오브젝트로 고차함수를 구현할 수 있는가?
