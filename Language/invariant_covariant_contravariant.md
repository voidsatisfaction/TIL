# 무공변성(nonvariant) 공변성(covariant) 반공변성(contravariant)

## Polymorphism

- 서로 다른 타입의 엔티티에 대한 하나의 인터페이스의 제공 또는 다양한 서로 다른 타입을 표현하기 위한 하나의 심볼의 사용
- 종류
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

## Subtype

서브 타이핑(inclusion polymorphism)이란 타입 다형성(polymorphism)의 한 형태로서 한 서브 타입은 하나의 데이터 타입인데 그 타입은 다른 데이터 타입(수퍼 타입)과 대체성의 관점에서 관련이 있으며, 이는 수퍼 타입의 구성요소에서 동작하도록 작성 프로그램 구성요소들(주로 서브루틴 혹은 함수들)이 서브타입의 구성요소에서도 동작할 수 있도록 하는 것을 의미한다.

In programming language theory, subtyping (also subtype polymorphism or inclusion polymorphism) is a form of type polymorphism in which a subtype is a datatype that is related to another datatype (the supertype) by some notion of substitutability, meaning that program elements, typically subroutines or functions, written to operate on elements of the supertype can also operate on elements of the subtype.

Subtyping should not be confused with the notion of (class or object) inheritance from object-oriented languages;[1] subtyping is a relation between types (interfaces in object-oriented parlance) whereas inheritance is a relation between implementations stemming from a language feature that allows new objects to be created from existing ones. In a number of object-oriented languages, subtyping is called interface inheritance, with inheritance referred to as implementation inheritance.

## Variance

복잡한 타입들 사이의 서브 타이핑과 그 복잡한 타입을 이루는 간단한 타입들 사이의 서브타이핑과의 관계.
Variance refers to how subtyping between more complex types relates to subtyping between their components.

Depending on the variance of the type constructor, the subtyping relation of the simple types may be either preserved(covariant), reversed(contravariant), or ignored(invariant) for the respective complex types.

- 예시
  - 간단한 타입들(S, T)이 다음과 같은 관계(서브타입에 관한)를 갖음
    - `S <: T`
  - 복잡한 타입들(L[S], L[T])의 관계는 어떻게 되는가?
    - `L[S] ? L[T]`

## 표기법

- `A <: B`
  - A가 B의 서브타입
- `A -> B`
  - 함수 타입으로, 함수의 인자 타입은 A이며 반환 타입은 B

## 공변성(Covariance)

- `S <: T => L[S] <: L[T]`
- `Greyhound <: Dog <: Animal`
  - `Greyhound`는 `Dog`의 서브타입
  - `Dog`는 `Animal`의 서브타입
- `Dog -> Dog`의 서브타입이 될 수 있는 경우는?
  - 1: `Greyhound -> Greyhound`
  - 2: `Greyhound -> Animal`
  - 3: `Animal -> Animal`
  - 4: `Animal -> Greyhound`
  - 어떤 함수가 Dog -> Dog를 type safe하게 대체할 수 있는가?

## 반공변성(Contravariance)

- `S <: T => L[S] :> L[T]`
- 프로그래밍 언어에 있어서, 함수의 인자는 반공변성의 성질을 띔
  - type safe를 유지하기 위해서는, 함수의 인자로 가능한 집합의 범위가 더 넓어야 함

## 무공변성(Invariance)

- `S <: T => L[S]와 L[T]는 서로가 서로의 서브타입이 될 수 없음`
- 어떠한 참조와 수정을 할 수 있는 타입(e.g 스칼라에서는 배열)은 무공변성의 성질을 띄어야만 함
  - 내용의 수정 가능 성질에 의하여 covariant는 될 수 없음
  - 내용의 참조 가능 성질에 의하여 contravariant는 될 수 없음
    - `L[T] l = new L[T]`
    - `l.S에만 존재하고 T에는 존재하지 않는 어떤 메서드 호출 -> 에러`
