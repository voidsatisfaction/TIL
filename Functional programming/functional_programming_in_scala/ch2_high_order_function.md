# 고차함수(High Order Function)

- **함수는 다른 함수의 매개변수가 될 수 있고, 반환값이 될 수 있음**
  - 함수형 언어는 함수를 퍼스트 클래스 시티즌으로 다룸
  - 프로그램을 더 유연하게 다룰 수 있게 해줌
  - 다른 함수들을 매개변수로 받거나 다른 함수들을 반환하는 함수를 고차함수라 부름

![](./images/hof_ex.png)

![](./images/hof_ex2.png)

## 2.1 고차 함수

### 함수 타입

- 타입 `A => B` 타입 A를 인자로 받고 반환 결과가 타입 B임을 뜻함
  - e.g `Int => Int` 는 정수를 정수로 매핑한 함수

### 고차 함수의 합성

```scala
def sum(f: Int => Int, a: Int, b: Int): Int =
  if (a > b) 0
  else f(a) + sum(f, a + 1, b)

def sumInts(a: Int, b: Int) = sum(id, a, b) // sum(x => x, a, b)
def sumCubes(a: Int, b: Int) = sum(cube, a, b) // sum(x => x * x * x, a, b)
def sumFactorials(a: Int, b: Int) = sum(fact, a, b)

def id(x: Int): Int = x
def cube(x: Int): Int = x * x * x
def fact(x: Int): Int = if (x == 0) 1 else fact(x-1)
```

### 익명 함수

- 함수를 매개변수로 전달하는 것이 많은 작은 함수들을 생성할 수 있게 함
  - 가끔은 매개변수로 전달하는 함수를 `def`로 정의하는 것 자체가 귀찮을 수 있음
- 문자열 처럼 함수의 **리터럴** 을 이용하여 이름 없이도 인자로 넘겨줄 수 있음
- 이를 익명 함수(anonymous function)이라 함

```scala
(x: Int) => x * x * x
// (x: Int) parameter
// x * x * x body
```

- 익명 함수는 문법 설탕
  - 모든 익명 함수는 `def`키워드로 정의 가능

## 2.2 커링(Currying)

```scala
def sum(f: Int => Int): (Int, Int) => Int = {
  def sumF(a: Int, b: Int): Int =
    if (a > b) 0
    else f(a) + sumF(a + 1, b)
  sumF
}
```

- sum은 다른 함수를 반환하는 함수
- `sumF`는 주어진 함수 파라미터인 f를 적용하여 결과를 합해줌

```
def sumInts = sum(x => x)
def sumCubes = sum(x => x * x * x)
def sumFactorials = sum(fact)
```

이 함수들은 다른 함수와 같이 적용 가능함

```scala
sumCubes(1, 10) + sumFactorials(10, 20)
```

- 중간 함수를 생략 할 수 있음
  - `sum (cube) (1, 10)`
  - `sum(cube) == sumCubes`
  - `(sum(cube))(1, 10)`

### 다중 파라미터 리스트

- 함수를 반환하는 함수는 함수형 프로그래밍에서 매우 유용하므로, 스칼라에서 특별한 문법을 내장해놓음

```scala
def sum(f: Int => Int)(a: Int, b: Int): Int =
  if (a > b) 0 else f(a) + sum(f)(a + 1, b)
```

![](./images/currying_multiple_parameter_lists1.png)

![](./images/currying_multiple_parameter_lists2.png)

### 함수 타입

```scala
def sum(f: Int => Int)(a: Int, b: Int): Int = ...
// (Int => Int) => (Int, Int) => Int
```

- 함수 타입은 오른쪽으로 묶음
  - `Int => (Int => Int)`
- 예시

```scala
def product(f: Int => Int)(a: Int, b: Int): Int = {
  if (a > b) 1
  else f(a) * product(f)(a + 1, b)
}

def fact(n: Int): Int = {
  if (n == 0) 1
  else product(x => x)(1, n)
}
```

- 위의 함수를 일반화 해보자

```scala
def mapReduce(f: Int => Int, combine: (Int, Int) => Int, zero: Int)(a: Int, b:Int): Int =
  if (a > b) zero
  else combine(f(a), mapReduce(f, combine, zero)(a+1, b))

def product(f: Int => Int)(a: Int, b: Int): Int =
  mapReduce(f, (x, y) => x * y, 1)

def fact(n: Int): Int = {
  if (n == 0) 1
  else product(x => x)(1, n)
}
```

## 2.3 Finding Fixed Points

![](./images/finding_fixed_point.png)

![](./images/ch2_summary.png)
