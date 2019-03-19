# [Polymorphism](https://en.wikipedia.org/wiki/Polymorphism_(computer_science))

- 정의
- 종류
  - 1 Ad hoc polymorphism
  - 2 Parametric polymorphism
  - 3 Subtyping
  - 4 Row polymorphism
  - 5 Polytypism
- 구현의 측면

## 정의

- 서로 다른 타입의 엔티티에 대해서 하나의 인터페이스의 제공
  - `date.toString()`, `int.toString()`
- 다양한 서로 다른 타입을 표현하기 위한 하나의 심볼의 사용

## 종류

- major
  - ad hoc
  - parametric
  - subtyping
- others
  - fuction overloading
  - operator overloading
  - double dispatch
  - multiple dispatch
  - single and dynamic dispatch
  - virtual function

### 1. Ad hoc polymorphism

- polymorphic functions
  - function(operator) overloading
- 대상
  - 함수

```Pascal
program Adhoc;

function Add(x, y : Integer) : Integer;
begin
    Add := x + y
end;

function Add(s, t : String) : String;
begin
    Add := Concat(s, t)
end;

begin
    Writeln(Add(1, 2));                   (* Prints "3"             *)
    Writeln(Add('Hello, ', 'World!'));    (* Prints "Hello, World!" *)
end.
```

### 2. Parametric polymorphism

- 정의
  - **함수** 나 **데이터 타입** 을 보다 일반적으로(generically) 작성할 수 있도록 해서, 값의 타입에 구애받지 않고 일관적으로 값을 다를 수 있게 도와줌
- 대상
  - 함수
  - 데이터 타입
- 특징
  - 정적 타입 안정성 보장
  - 함수형 언어에서 보편적
    - *람다 계산* 의 확장으로 생각할 수 있음

```c++
class List<T> {
    class Node<T> {
        T elem;
        Node<T> next;
    }
    Node<T> head;
    int length() { ... }
}

List<B> map(Func<A, B> f, List<A> xs) {
    ...
}
```

### 3. Subtyping(Inclusion polymorphism)

- 정의
  - 타입 다형성(polymorphism)의 한 형태로서 한 서브 타입은 하나의 데이터 타입인데 그 타입은 다른 데이터 타입(수퍼 타입)과 대체성의 관점에서 관련이 있으며, 이는 수퍼 타입의 구성요소에서 동작하도록 작성 프로그램 구성요소들(주로 서브루틴 혹은 함수들)이 서브타입의 구성요소에서도 동작할 수 있도록 하는 것을 의미한다.
  - OOP언어 에서는 subtype polymorphism을 subclassing(inheritance)를 이용해서 구현
    - **하지만 subtyping != 상속**
    - 상속과의 차이
      - 서브타이핑
        - 객체 지향에서의 인터페이스 개념에 가까운, 타입들 사이의 관계
        - 많은 객체 지향 언어에서는, 서브타이핑은 인터페이스 상속이라고 불림
      - 상속
        - 현재 존재하는 오브젝트로 부터 새로운 오브젝트를 생성할 수 있도록 허락하는 언어 특징에서 나온 구현들 사이의 관계
        - 구현의 상속
- 대상
  - 함수
- 특징
  - `S <: T`
    - T는 S의 수퍼 타입이다 / S는 T의 서브타입이다
  - Subtype polymorphism은 보통 동적으로 해결됨
  - Liskov substitution principle을 따름
- 구현
  - 클래스 인터페이스의 polymorphic한 부분을 구현한 함수들의 테이블인 virtual table이 있음
  - 각각의 오브젝트는 자신의 클래스의 vtable에의 포인터를 포함함
  - polymorphic 메서드가 실행이 되면 vtable에의 포인터가 참조됨
    - late binding
      - virtual 함수 호출은 직접 호출이 될 때 까지 bound되지 않는다.
    - single dispatch
      - virtual 함수 호출은 첫 인자(this 오브젝트)의 vtable을 통해서만 바인딩됨
        - 다른 인자들의 런타임 타입들은 완전히 관계가 없음

```
abstract class Animal {
    abstract String talk();
}

class Cat extends Animal {
    String talk() {
        return "Meow!";
    }
}

class Dog extends Animal {
    String talk() {
        return "Woof!";
    }
}

static void letsHear(final Animal a) {
    println(a.talk());
}

static void main(String[] args) {
    letsHear(new Cat());
    letsHear(new Dog());
}
```

### 4. Row polymorphism(Duck typing)

- 정의
  - 오브젝트의 적합성(suitability)이 오브젝트 자체의 타입이 아닌 **특정 메서드와 속성의 존재 유무로 결정됨**
- 대상
  - 함수
- 특징
  - structural types을 다룸
    - 타입 정보를 잃어버리지 않은 채로 모든 값들(그 값들의 타입이 특정한 속성을 갖음)의 사용을 허락함

### 5. Polytypism

## 구현의 측면

- 구별 기준
  - 구체적 구현이 선택되는 때
  - static(dispatch) / dynamic(dispatch) 로 나뉨
- static
  - 장점
    - 실행이 dynamic보다 빠름
    - dynamic dispatch의 overhead가 없음
    - 컴파일러, 소스코드 분석 툴, 프로그래머에 의한 보다 광범위한 정적 분석 가능
  - 단점
    - 보다 많은 컴파일러 기능 지원이 필요
  - 보편적인 예시
    - ad hoc
    - parametric
    - subtype(template metaprogramming)
- dynamic
  - 장점
    - 보다 유연함
    - duck typing지원 / 오브젝트의 전체 타입을 알지 못해도 실행가능
  - 단점
    - 느림
  - 보편적인 예시
    - subtype
