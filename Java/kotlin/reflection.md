# Reflection

- 의문
- 개요
- 참조
  - Class 참조
  - Callable 참조

## 의문

## 개요

- 정의
  - 런타임에 프로그램의 구조를 참조하는 것을 가능케하는 기능의 집합
    - e.g) 함수나 프로퍼티의 이름, 타입을 런타임에 파악하는 것
- 특징
  - *functional, reactive 스타일의 코드에서 필수적임*
    - 왜?

## 참조

- Class 참조
- Callable 참조

### Class 참조

- 개요
  - 런타임에 코틀린 클래스를 참조하기
    - KClass 타입 값을 반환
    - `MyClass::class`
  - 런타임에 자바 클래스를 참조하기
    - `MyClass::class.java`
  - 인스턴스에서 클래스 참조하기
    - `instance::class`
      - exact class를 반환

### KClass

- 개요
  - introspection을 할 수 있는 클래스

### Callable 참조

```kotlin
fun isOdd(x: Int) = x & 2 != 0

val numbers = listOf(1,2,3)
println(numbers.filter(::isOdd))

// ::isOdd는 함수 타입의 값, 즉, 함수에 대한 참조
```
