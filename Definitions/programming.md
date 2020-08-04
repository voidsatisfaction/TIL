# Programming 용어

- General
  - coroutine
  - generator
  - iterator
  - asynchronous iterator, generator
  - promise
  - future
  - event loop
  - argc vs argv
- Data
  - stream

## General

- coroutine
- generator
- iterator
- promise
- future

### coroutine

- 정의
  - non-preemptive인 multitasking을 위한 subroutine의 일반화 버전의 컴퓨터 프로그램 컴포넌트

### generator

참고

- [이터레이터와 제너레이터](https://mingrammer.com/translation-iterators-vs-generators/)

Generator, Iterator relation diagram

![](./images/programming/generator_iterator1.png)

- 정의
  - *루프의 iteration 행위를 컨트롤하는데에 사용될 수 있는 (서브)루틴*
    - 정확히 이게 무슨 뜻일까?
    - lazy value producer
    - iterator를 generate한다는 것 보다는, 값을 lazy하게 generate한다고 해석하는것이 바람직해 보임
- 특징
  - 값의 수열을 생성하나, 모든 값을 전부 포함하는 array를 생성해서 한번에 반환하는 대신, 한 번에 하나의 값을 반환
    - 메모리를 덜 차지함
    - lazy producing
  - 함수처럼 보이나, 행동은 iterator
    - 단순 iteration뿐 아니라, 값을 기존 스테이트(프레임) 기반으로 동적으로 필요할 때 생성 및 반환
  - vs coroutine
    - generator(semi-coroutine)
      - caller에게 컨트롤을 yield
    - coroutine
      - 컨트롤을 yield할 대상을 지정 가능

### iterator

- 정의
  - 프로그래머가 container(특히 리스트)를 traverse할 수 있게 하는 object
    - `next()`를 호출할 때 다음값을 생성해내는 상태를 가진 헬퍼 객체
- 종류
  - **Internal Iterators**
    - 정의
      - `map`, `reduce`와 같은 high order function들
        - 컨테이너를 traverse하면서 인자로 주어진 함수를 모든 원소에 적용하는 것을 구현함
  - **External iterators and the iterator pattern**
    - Iterator pattern
      - 정의
        - iterator 구현을 위한 디자인 패턴
        - 컨테이너의 내부 구조를 유저와 격리시키면서, 컨테이너의 모든 원소를 프로세싱할 수 있도록 함
    - Generator
      - 정의
        - generator를 이용하여 iterator를 구현할 수 있음
        - tree traversal과 같은 비교적 복잡한 stateful iterator를 생성 가능
      - 언어에 따른 차이
        - 파이썬
          - iterator를 반환하는 iterator constructor를 의미
  - **Implicit iterators**
    - 정의
      - 몇몇 객체지향 언어에서, 명시적인 iterator object를 사용하지 않고, iterating을 하는 것
        - 실제로 iterator object가 존재할 수 있으나, 언어의 소스코드 내부에 있으며, 노출되지 않음
- 참고
  - Streams
    - 개요
      - iterator는 input stream의 유용한 추상화가 될 수 있음
      - infinite iterable object를 제공 가능(not necessarily indexable)
    - 파이썬
      - **iterator = 데이터의 stream을 나타내는 오브젝트**
  - Contrasting with indexing

### asynchronous iterator, generator

- asynchronous iterator
  - 의미
    - iterator가 container원소를 traverse할 때, IO bound 동작과 같은 비동기적인 동작도 함께 할 때, 그러한 iterator를 말함
- asynchronous generator
  - 의미
    - generator가 lazy하게 값을 produce하는 경우 IO bound 동작과 같은 비동기적인 동작도 함께 할 때, 그러한 generator를 말함

### promise

https://en.wikipedia.org/wiki/Futures_and_promises

### future

### event loop

- 정의
  - 하나의 프로그램 안에서, 이벤트나 메시지를 wait하거나 dispatch해주는 프로그래밍 구조물
  - event provider, event handler와 함께 조합되어 동작함
  - 동의어
    - message dispatcher, message loop, message pump, run loop
- 특징
  - 하나의 프로그램의 central control flow를 event loop가 구성할 경우(nodejs), main loop 혹은 main event loop라 불림
- 사용

```
function main
    initialize()
    while message != quit
        message := get_next_message()
        process_message(message)
    end while
end function
```

### argc vs argv

- `argc`
  - 정의
    - argument count
    - 프로그램으로 전달되어진 인자의 개수
- `argv`
  - 정의
    - argument vector
    - 스트링 인자 벡터

## Data

### stream

- 정의
  - **시간의 경과에 따라서 사용가능하게 만들어진 데이터 요소의 sequence**
    - codata(potentially infinite) 라고 불림
      - data(finite)
- 특징
  - 큰 batch 대신에, 한 번에 하나씩 처리되는 아이템과 유사
  - filter
    - 스트림을 반환하며, 스트림을 제어하는 함수
  - pipelines
    - 필터들을 연결하는 대상
- 예시
  - **Stream editing**
    - `sed`, `awk`, `perl`
    - 파일이나 파일들을 in-place로, user interface에 파일을 load하지 않은채로 processing함
    - 예시
      - 커맨드라인으로부터 디렉터리에 들어있는 모든 파일을 찾아서 바꾸는 작업
  - **Unix와 C언어 기반의 시스템에서, 개별적인 바이트 혹은 문자인 데이터의 source 혹은 sink**
    - **파일을 읽거나 쓰거나 network socket위에서 상호작용 할 때 사용되는 추상화**
    - **standard stream은 모든 프로그램이 사용 가능한 3가지 스트림**
      - stdin
      - stdout
      - stderr
  - I/O 장비
    - 시간의 경과에 따라서 잠재적으로 끝 없는 데이터를 produce하거나 consume할 수 있기 때문
  - OOP에서는 input stream을 iterator로 구현함
  - Scheme 언어 등에서는 스트림을 lazily evaluated 혹은 데이터 요소의 delayed sequence로 정의함
    - 리스트와 비슷하나, 뒤의 요소들은 필요할 때 calculated 됨
    - Stream은 무한 수열과 급수를 나타낼 수 있음
  - Smalltalk standard library나 다른 프로그래밍 언어에서는 stream이 external iterator
  - Stream processing
    - 병렬 프로세싱, 특히 그래픽 프로세싱에서는 stream이라는 말이 소프트웨어 뿐 아니라 하드웨어에도 적용됨
    - There it defines the quasi-continuous flow of data that is processed in a dataflow programming language as soon as the program state meets the starting condition of the stream.
