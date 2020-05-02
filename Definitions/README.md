# 용어 정리

어떠한 개념에 정확한 용어를 사용하는 것은 매우 중요하다. 정확한 용어를 사용하므로써, 다른 사람들과 공통인식을 갖게 해 줄 뿐 아니라 나 자신이 체계적으로 지식을 익혀나갈 수 있게 만든다.

정확한 용어의 정의가 정확한 개념의 파악을 이끈다. 수학에서도 마찬가지.

## 목차

- Type
- Argument
- Parameter
- Literal
- Interface
- Overhead
- 클로저
- 호이스팅
- 이름공간

## 용어

### Type(타입)

어떠한 값들의 집합과 그 값들에 대한 연산과 메서드로 이루어져있다(golang)

### Argument(인자)

### Parameter(매개변수)

### Literal(리터럴)

- 프로그램 안에서 계산되지 아니하고 값을 하드코딩 하는 방법

A literal is how you represent a value in your source code. A literal is not the result of a calculation or an I/O operation; it’s data that you type directly into your program.

### Interface(인터페이스)

메서드 집합을 명시한 타입. golang에서는 어떠한 타입이 주어진 인터페이스 집합을 포함하는 확대 집합에 해당하는 메서드 집합을 갖고 있는 경우 어떠한 타입의 값이든 interface 타입의 변수에 저장할 수 있다. 이러한 타입은 *인터페이스를 구현했다* 고 한다.

### Token(토큰)

프로그래밍 언어의 어휘를 형성하는 요소. 다음과 같은 내용으로 구성되어있다(go언어):

- 식별자(Identifier)
  - 변수나 타입 같은 프로그램 구성 요소에 이름을 붙임
- 예약어(Keyword)
  - 언어에서 미리 행동이 정의된 이름
- 연산자와 구두점
- 리터럴

### Path parameter vs Query string

- Path parameter
  - 필수적인 매개변수를 넘겨주는 것이 좋음
  - `GET /employee/{id}`
- Query string
  - 선택적 매개변수를 넘겨주는 것이 좋음(사이즈, 시작점)
  - 필터와 같은 느낌
  - `GET /employee?start=1&size=10`

### Overhead

특정한 목표를 달성하기 위해서 간접적 혹은 추가적으로 요구되는 시간, 메모리, 대역폭 혹은 다른 컴퓨터 자원을 말한다.

- 예시
  - 컴퓨터 프로그래밍
    - 함수 호출시 스택 프레임을 설정하고 매개변수들과 반환 주소들을 복사하기 위한 실시간 오버헤드가 발생하며, 컴파일러는 이 오버헤드를 최소화하기 위해 함수 호출을 재정렬하기도 한다.
  - 통신
    - 전송하고자 하는 payload는 실제 데이터 뿐 아니라, 신뢰성 있는 통신을 보장하기 위한 다양한 제어 및 신호 데이터를 포함한다. 이러한 제어 신호들은 모두 오버헤드로 간주

### 클로저

내부 함수가 외부 함수의 지역변수에 접근할 수 있고, 외부함수는 외부함수의 지역변수를 사용하는 내부함수가 소멸될 때까지 소멸되지 않는 특성을 의미

### 호이스팅

자바스크립트 및 액션스크립트 코드를 인터프리터가 로드할 때, 변수의 정의가 그 범위에 따라 선언과 할당으로 분리되어, 변수의 선언을 항상 최상위로 끌어 올리는 것(함수도 가능)

### 이름공간(Name space)

- In computing, a namespace is a set of symbols that are used to organize objects of various kinds, so that these objects may be referred to by name.
- 이름으로 오브젝트들을 참조할 수 있도록, 다양한 종류의 오브젝트들을 조직화하는데에 사용되는 심볼들의 집합
