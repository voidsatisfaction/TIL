## OOP와 Procedural programming의 차이점

Procedural

```rb
main routine이 필요할때 마다 자신이 정의(지시)한 subroutine을 실행 항상 일정함.

정적 속박
```

OOP

```rb
Object사이의 메세지 주고받기
만약 m이라는 메세지를 보내면 m을 받는 오브젝트에 따라서 다른 동작을 할 수 있다.

동적 속박

ex) a.m != b.m
cf) duck typing
```

Class가 너무 많아지면 힘들어요 => Inheritance를 써요

## OOP의 장점

**프로그램의 구조화(복잡한 프로그램의 정리)**
1. 구조화 프로그램(다익스트라): goto대신 서브루틴, 조건문...
2. Algorithm + Data Structures = Program
3. Module, Abstract data type(데이터구조 + 그것을 조작하는 알고리즘 = 관리의 하나의 단위)
4. OOP: Data + Algorithm = Object(module단위)
5. Design pattern
cf) Aspect Oriented Programming

**프로그램의 직관성, 알기 쉬움**

**DRY**
1. Polymorphism
2. Inheritance

## 장점1: Polymorphism이란?

하나의 프로그램(메소드 등..)이 다양한 작용을 하는것.
DRY에 유용.

```
obj a
method toString()
  return ~~

obj b
method toString()
  return ~~

obj printer
method print(obj)
  s = obj.toString()  <= 동적 속박을 사용한 Polymorphism의 특성을 갖는 프로그램.

cf) Procedural Programming에서는..

method print(obj)
  if obj == a
    ...
  elsif obj == b
    ...

```

**type: 값(value)의 종류**

정적 타입언어에서의 다른 종류의 Polymorphism
- Subtype polymorphism
  - Subtype: 타입의 계층 관계(e.g int < real)
  - Subclass과 overiding을 이용해서 구현
- Parametric polymorphism
```
type지정에 변수를 지정
  addToList(e: t, l: list of t) // t는 변수
```

## 장점2: Encapsulation

객체는 내부 상태(state)를 감춘다.
다른 객체가 직접적으로 다른 객체의state를 참조할 수 없다. 반드시 메세지를 보내야지 참조할 수 있다.

인터페이스(method)로 내부 state를 숨기는 경우가 많음
