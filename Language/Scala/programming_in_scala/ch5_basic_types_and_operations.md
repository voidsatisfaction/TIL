# Basic Types and Operations

## 5.1 기본 타입들

- integral 타입
  - Byte
  - Short
  - Int
  - Long
  - Char
- numeric 타입
  - Integral 타입
  - Float
  - Double
- String 이외의 다른 타입들은 모두 `scala`패키지 안에 존재
  - scala패키지는 모든 스칼라 소스파일에 임포트됨 그래서 그냥 단순히 이름만으로 사용 가능
- 대응하는 자바 타입들과 동일, 바로 바이트코드로 생성가능

## 5.2 리터럴

- 리터럴
  - 코드에 직접 정수값을 쓰는 방법

### 정수 리터럴

- 타입
  - Int(32), Long(64), Short(16), Byte(8)
  - 10진수, 16진수, 8진수
  - 몇진수 표현도 스칼라 인터프리터는 10진수로 출력

```scala
val hex = 0x5 // 5
val hex2 = 0x00FF // 255
val magic = 0xcafebabe // -889275714

val oct = 035 // 29
val nov = 0777 // 511
val dec = 0321 // 209

val dec1 = 31

// Long
val prog = 0XCAFEBABEL // Long = 3405691582
val tower = 35L // Long = 35
val of = 311 // Long = 31
```

### 부동소수점 리터럴

- 마지막이 f로 끝남: `Float`
- 나머지: `Double`

```scala
val big = 1.2345 // 1.2345
val bigger = 1.2345e1 // 12.345
val biggerStill = 123E45 // 1.23E47
```

### 문자(Character) 리터럴

- 단따옴표로 감싼 유니코드 문자
  - `A`
- 단따옴표로 감싼 백슬래시 포함 8진수, 16진수 숫자
  - `\101`
- 단따옴표로 감싼 백슬래시 포함 16진수 네자리 유니코드 표현
  - `\u0041`

```scala
val a = 'A' // Char = A

val c = '\101' // Octal
```

### 문자열(String) 리터럴

- 쌍따옴표로 감싼 문자들
  - `val hello = "hello"`
  - `"\\\"\'"` == \\"'
- 생 문자열(raw String)
  - """

```scala
println("""Welcome to Ultamix 3000.
           Type "HELP" for help.""") // including leading spaces

println("""|Welcome to Ultamix 3000.
          |Type "HELP" for help.""") // erase leading spaces
```

### 심볼 리터럴

- `'abc`
- `scala.Symbol`과 연결됨
- 동적 타입 언어에서의 식별자(identifier)로 사용
- 같은 심볼을 선언하면 둘은 같은 리퍼런스를 갖음

### 불린 리터럴

- `true`, `false`

## 5.3 연산자는 메서드

- 기본 타입에 다양한 연산자(메서드) 제공
  - `+`
    - 오버로딩된 메서드(같은 이름, 다른 매개변수 타입)
    - `Int`를 받고 `Int`를 반환 하는 메서드
    - `Int`를 받고 `Long`을 반환 하는 메서드
- 어떠한 메서드도 연산자 기법으로 작성할 수 있음
- 즉 어떠한 메서드도 연산자가 될 수 있음
  - 그냥 연산자 노테이션(notation)으로 작성하면 됨

```scala
val s = "Hello, world!"

s indexOf 'o' // Int = 4
s indexOf ('o', 5) // Int = 8
```

- 연산자 기법의 종류
  - infix
    - `7 + 2`
  - prefix
    - `-7`, `!found`, `~0xFF`
    - 매서드 이름을 오브젝트 앞에 둠
    - 다음과 동일
      - `(7).unary_-`
    - 오직 `+ - ! ~`에만 적용 가능
  - postfix
    - `7 toLong`
    - 메서드를 오브젝드 다음에 둠(매개변수 존재하지 않음)
    - 부작용
      - 있음: 괄호도 포함 (`println()`)
      - 없음: 과로 미포함 (`toLowerCase`)

## 5.4 수학적 연산

```scala
1.2 + 2.3 // 3.5

3 - 1 // 2

'b' - 'a' // 1

2L * 3L // Long = 6

11 / 4 // Int = 2

11.0f / 4.0f // Float = 2.75

11.0 % 4.0 // Double = 3.0
```

## 5.5 관계, 로직 연산

- numeric타입 값의 비교
  - `> < >= <=`
- 불린 값의 변경
  - `!`
- 지연평가
  - `by-name parameters`로 구현

## 5.6 비트와이즈(Bitwise) 연산

- &
- |
- ^
- ~
  - 보수 연산자
- <<
- \>\>
- \>\>\>
-  `>>, >>>, <<`
  - `a << b`
    - 왼쪽으로 b비트 이동 기존의 공간은 0으로 채움
  - `a >> b`
    - 오른쪽으로 b비트 이동 기존의 공간을 가장 높은 자리의 수로 채움
    - e.g `-1 >> 31 Int = -1`
    - -1 == 11111111111111
  - `a >>> b`
    - 오른쪽으로 b비트 이동 기존의 공간은 0으로 채움

```scala
1 & 2 // Int = 0

1 | 2 // Int = 3

1 ^ 3 // Int = 2

~1 // -2

-1 >> 31 // Int = -1 오른쪽으로 시프트 후 1을 채워넣음

-1 >>> 31 // Int = 1 오른쪽으로 시프트 후 0을 채워넣음

1 << 2 // Int 4
```

## 오브젝트 동등성

- 모든 오브젝트를 `==, !=`를 사용해서 비교할 수 있음
- 레퍼런스는 `eq, ne`를 사용해서 비교할 수 있음

```scala
List(1, 2, 3) == List(1, 2, 3) // Boolean = true
List(1, 2, 3) == List(4, 5, 6) // Boolean = false

1 == 1.0 // Boolean = true
List(1, 2, 3) == "hello" // Boolean = false

List(1, 2, 3) == null // false
null == List(1, 2, 3) // false
```

## 연산자 우선순위, 연관성

- 우선순위
  - 스칼라는 연산자가 없기 때문에 메서드로 우선순위를 정함
    - 메서드가 어떠한 문자로 시작하는지를 기준
  - 순서
    - `* / %`
    - `+ -`
    - `:`
    - `= !`
    - `< >`
    - `&`
    - `^`
    - `|`
    - (모든 문자)
    - (모든 할당 연산자)
  - 예시
    - `2 << 2 + 2`
      - 32
    - `x *= y + 1`
      - `x *= (y + 1)`
- 연관성(associativity)
  - 연자가 어떠한 문자로 끝나는지를 기준으로 정함
  - :로 끝나는 연산자는 오른쪽 오브젝트가 왼쪽 오브젝트를 인자로 받음
    - `a:::b == b.:::(a)`
  - 연관성이 어떻게 되었든 평가는 왼쪽에서 오른쪽으로 됨
    - `a:::b <==> (val x = a; b.:::(x))`
  - `a ::: b ::: c` == `a ::: (b ::: c)`
- **위의 룰보다 중요한것은 괄호를 잘 사용하는 것**

## 풍부한 래퍼(Rich wrappers)

- 스칼라 기본 타입의 메서드를 확장
- `implicit`키워드 사용
