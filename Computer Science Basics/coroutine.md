# 코루틴

- 의문
- 개요
  - 코루틴이란
  - subroutine과의 차이
  - thread와의 비교
  - generator와의 비교
  - mutual recursion과의 비교
- coroutine의 응용
- coroutine in python

## 의문

## 개요

### 코루틴이란

- *non-preemptive multitasking* 을 위한 subroutine의 일반화 버전의 컴퓨터 프로그램 컴포넌트
- 용도
  - cooperative tasks
  - *exceptions*
  - event loops(이벤트 루프를 코루틴에서 돌리고, 이벤트를 받으면 메인 함수로 이벤트와 함께 컨트롤을 돌림. 메인 작업이 끝나면 다시 이벤트 루프 코루틴에서 돌림)
  - iterators(특정 iterable의 하나의 원소들을 가져오면서 동작을 수행하고 그 수행이 끝나면 다음 원소로 넘어감)
  - infinite lists and pipes
    - infinite list의 데이터를 한번에 다 가져오는 것은 무한하므로 불가능한데, iterator에서 했던 것 처럼, 일부의 원소를 하나씩 coroutine에서 가져오도록 하고, 그것을 가지고 main 에서 작업을 하고 다시 coroutine에서 가져오도록 하는 방식으로 프로그램을 돌릴 수 있음
      - e.g) 개미수열의 예시

      ### 유용한 예시

      - consumer-producer 관계
        - 하나의 루틴이 아이템을 생성해서 큐에 넣는 역할을 담당
        - 나머지 하나의 루틴이 아이템을 큐의 아이템들을 제거하고 그것들을 사용
        - 효율성을 생각해서, 아이템들을 한번에 여러개를 넣거나 제거하는 것을 생각

```
var q := new queue

coroutine produce
  loop
    while q is not full
      create some new items
      add the items to q
    yield to consume

coroutine consume
  loop
    while q is not empty
      remove some items from q
      use the items
    yield to produce
```

### subroutine과의 차이

- subroutine은 coroutine의 special case
  - `yield`를 하지 못하는 coroutine
- 코루틴은 다른 코루틴들을 호출함으로 exit한 뒤에 나중에 다시 제어 흐름을 가져와서 동작할 수 있음
  - coroutine instance는 state를 유지하고 있음
- `yielding`으로 호출한다면 caller-callee의 관계가 아니라, 완전히 symmetric한 관계이다

### thread와의 비교

- 공통점
  - coroutine은 thread와 비슷
- 차이점
  - coroutine은 cooperatively multitasked, threads는 preemptively multitasked
    - cooperatively multitasked: context switch가 일어나지 않음. 현재 실행 흐름을 가지고 있는 쪽이 자주적으로 control을 yield함
    - preemptively multitasked: 컴퓨터 시스템이 임시적으로 context switch에 간섭함
    - 결국 coroutine은 concurrency이나 parallelism이 아님
  - coroutine은 coroutine간의 switching에 system call이나 blocking call을 포함하지 않음
    - mutexes나 semaphore를 사용할 이유가 없음. 따라서 os지원도 불필요

### generators과의 비교

- generator는 semicoroutine으로 불리고, coroutine의 부분집합
  - yield를 여러번 할 수 있고, suspending / re-entry를 여러 entry point에서 할 수 있다는 것은 동일
  - coroutine은 yield후 yield한 값을 가지고 즉각적으로 실행하는 장소를 컨트롤 할 수 있으나, generator는 그러지 못하고, 대신, control을 generator의 호출자로 이동시킴
    - 즉, generator는 주로 iterator의 작성을 간단화 하는 데에 사용되기 때문에 반환 값을 parent routine으로 넘겨줄 뿐
- generator을 사용해서 coroutine을 구현할 수 있음
  - top-level dispatcher routine(trampoline)이용
    - generator로 부터 받은 tokens을 가지고 control을 넘길 주체를 찾는 역할

```
var q := new queue

generator produce
  loop
    while q is not full
      create some new items
      add the items to q
    yield consume

generator consume
  loop
    while q is not empty
      remove some items from q
      use the items
    yield produce

subroutine dispatcher
  var d := new dictionary(generator -> iterator)
  d[produce] := start produce
  d[consume] := start consume
  // generator는 직접 coroutine호출을 못하니까, dispatcher가 top-level에서 control을 넘겨주는 역할을 함
  var current := produce
  loop
    current := next d[current]
```

### mutual recursion과의 비교

- coroutine을 state machines or concurrency 를 위해서 사용하는 것은 tail calls를 사용하는 mutual recursion과 유사함
- coroutine이 더 flexible하고 efficient함
  - `return`대신 `yield`하고, `restart`대신 `resume`하기 때문에, state를 가지고 있을 수 있고(변수와 execution point), yields는 tail poisition에 의존하지 않는다
  - coroutine은 state를 parameter로 건네줄 필요가 없음

## [coroutine의 응용](https://en.wikipedia.org/wiki/Coroutine)

- *State machine*
- Actor model
  - 각 actor는 각자의 procedures를 갖고 있으나, 그것들은 자원해서 control을 포기해서 central scheduler에게 컨트롤을 넘겨줌(cooperative multitasking)
- Generator
  - streams에 유용 - input/output - generic traversal of data structures
- Communicating sequential processes
- *Reverse communication*
  - mathematical software

## coroutine in python

### 개요

```py
import asyncio

async def coroutine1():
    # 1. 이벤트루프에서 첫번째 태스크인 coroutine1을 실행
    print('coro1 first entry point')
    # 2. 실행 시점이 이벤트루프로 복귀
    await asyncio.sleep(0.1)
    # 5. 1초 뒤 프린트
    print('coro1 second entry point')

async def coroutine2():
    # 3. 이벤트루프에서 두번째 태스크인 coroutine2를 실행
    print('coro2 first entry point')
    # 4. 실행 시점이 이벤트루프로 복귀
    await asyncio.sleep(0)
    # 6. 2초 뒤 프린트
    print('coro2 second entry point')

loop = asyncio.get_eveny_loop()
loop.create_task(coroutine1())
loop.create_task(coroutine2())
loop.run_forever()
```

위의 코드를 완전히 이해하는 것이 목표!

### Frame object

파이썬 바이트 코드의 이해1

![](./images/coroutine/python_byte_code1.png)

파이썬 바이트 코드의 이해2

![](./images/coroutine/python_byte_code2.png)

- 정의
  - 함수를 실행할 때 필요한 정보를 갖고 있는 오브젝트
- 속성
  - `frame.f_locals`
    - 지역 변수의 상태를 나타냄
  - `frame.f_back`
    - 자신을 호출한 프레임을 가리킴
      - 자신이 실행하는 함수가 종료되면, `f_back`프레임으로 다시 돌아감
      - 스택 프레임들은 f_back들로 연결된 것임
    - 인터프리터 내부에는 `ThreadState`라는 오브젝트를 갖고 있는데, 이는 현재 실행하고 있는 프레임을 멤버로 가지고 있음
      - 따라서, 함수 내부에서 함수가 실행되면 새로운 프레임 객체가 만들어지고, 새롭게 생성된 frame의 f_back은 자신을 호출한 함수를 가리키고, `ThreadState`가 현재 실행중인 frame으로 갱신을 함
  - `frame.f_lasti`
    - 해당 함수가 가장 최근에 실행한 가장 최근에 실행한 바이트코드의 인덱스(위의 예시에서는 리턴 함수)
  - `frame.f_code`
    - 코드 객체(`== func.__code__`)
    - 속성
      - `func.__code__.co_code`
        - 함수의 바이트코드 바이너리(opcode, operand 등)
      - `func.__code__.co_consts`
        - 함수 내에서 사용된 상수들
      - `func.__code__.co_varnames`
        - 함수에서 사용된 지역변수 이름들
      - `func.__code__.co_names`
        - 함수내에서 사용된 전역변수 이름들

### 코루틴의 바이트 코드 이해
