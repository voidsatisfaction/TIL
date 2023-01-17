# Classes and Objects

- 의문
- Visibility modifiers

## 의문

## Visibility modifiers

- 종류
  - `public`
    - import하면 어느곳에서든 볼 수 있는 경우
  - `private`
    - 선언한 곳에서만 볼 수 있는 경우
  - `internal`
    - 같은 모듈에서만 볼 수 있는 경우
  - `protected`
    - private과 같지만, subclass에서도 볼 수 있음
- c.f) 모듈
  - 함께 컴파일되는 코틀린 파일의 집합
  - e.g)
    - intellij IDEA 모듈
    - maven project
    - kotlinc의 호출로 컴파일되는 파일들의 집합

## Generics: in, out, where

### Variance

```java
// Java

// covariant
// 이 메서드는 E의 오브젝트의 컬렉션 혹은 E의 서브타입의 오브젝트의 컬렉션을 파라미터로 받을 수 있음을 나타냄
interface Collection<E> ... {
    void addAll(Collection<? extends E> items);
}

// contravariant
//
List<? super String>
```

- 자바의 `?`타입
  - 개요
    - 자바의 generic 타입은 invariant
      - e.g) `List<String>`은 `List<Object>`의 서브타입이 아님
    - `? extends T` 타입은 타입 `T`에 대해서 covariant
      - 해당 타입은 읽은 순 있는데, 쓸 순 없음
        - **`List<String>`을 읽을때에는 `List<Object>`로 읽어도 상관없다**
          - 즉, 읽을때에는 추상적으로 읽어도 된다
      - 읽으려고 하는 대상은 `producer`(바깥으로부터 요청을 받아 읽기만 되니까)
    - `? super T` 타입은 타입 `T`에 대해서 contravariant
      - 해당 타입은 쓸 순 있는데, 읽은 순 없음
        - **`List<Object>`에 원소를 더할 때에는 `List<String>`의 원소를 더해줘도 상관없다**
          - 즉, 쓸(더할) 때에는 구체적으로 써도(더해도) 된다
      - 쓰려고 하는 대상은 `consumer`(더해지니까)
