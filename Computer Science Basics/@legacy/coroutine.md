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
  - 개요
  - Frame object
  - 코루틴의 바이트 코드 이해
  - Event Loop for non-preemptive multitasking
  - Making Custom Event Loop
  - 부록1: yield from

## 의문

## 개요

- Coroutine의 구성품
  - suspend function
  - context
    - dispatcher
    - job
    - coroutine name
    - coroutine exception handler
  - coroutine scope
  - withContext
  - coroutine scheduler

### 코루틴이란

- 정의
  - *non-preemptive multitasking* 을 위한 subroutine의 일반화 버전의 컴퓨터 프로그램 컴포넌트
- 구성
  - Suspend function
    - 언제든지 멈추고 재개할 수 있는 함수
      - Stack Pointer, Variables이 있어야 함
  - Context
    - 개요
      - 코루틴의 행동을 정의하는 요소들의 컬렉션
    - 구성
      - **Dispatcher**
        - 어떤 스레드에서 동작할지 관리
        - 종류
          - 코틀린에서 기본적으로 제공하는 디스패쳐
            - `Dispatchers.Default`
              - `Dispatchers.IO`와 같은 스레드 풀 공유
              - CPU 코어에 개수가 제한되어 있음(CPU intensive work할때 유용)
            - `Dispatchers.IO`
              - `Dispatchers.Default`와 같은 스레드 풀 공유
              - default로 64개의 스레드 존재
            - `Dispatchers.Unconfined`
          - 커스텀
            - `Executor.asCoroutineDispatcher()`
      - **Job**
        - 코루틴의 라이프 사이클을 다룸
      - **Coroutine Name**
        - 코루틴의 이름(디거빙하기 편함)
      - **CoroutineExceptionHandler**
        - 캐치되지 않은 익셉션을 다룸
    - 특징
      - `+`로 컨택스트 끼리 결합할 수 있음
        - `(Dispatchers.Main + CoroutineName("context")) + (Dispatchers.IO)`
  - CoroutineScope
    - 개요
      - **해당 스코프가 생성한 모든 코루틴을 추적**
        - `scope.cancel()`하면 어느때나 진행중인 작업들 멈추게 할 수 있음
      - 앱의 특정 레이어에 CoroutineScope를 생성해야지만 코루틴들의 라이프사이클을 조절하거나 코루틴을 시작할 수 있음
        - `val scope = CoroutineScope(Dispatchers.Default)`
    - *그럼 scope가 Global인거랑 Coroutine인거랑 차이는 뭐지?*
  - `withContext(context) { ... }`
    - 주어진 context로 suspending 블록을 호출하는데에 사용
  - CoroutineScheduler
    - 개요
      - JVM 구현에서 디폴트로 사용되는 스레드 풀
      - 알아서 가장 효율적으로 워커에게 코루틴을 넘겨줌
    - 특징
      - `Dispatchers.Default`, `Dispatchers.IO`는 같은 스레드 풀
- 메타포
  - Stack Pointer, Variables
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
- 특징
  - 함수를 실행되는데에 사용됨
  - Call stack
  - Value stack
  - Local variables
  - 마지막에 실행된 바이트코드의 인덱스가 존재
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

제너레이터의 이해

```py
def generator():
    recv = yield 1
    return recv

# 0 LOAD_CONST 1 (1)
# 2 YIELD_VALUE
# 4 STORE_FAST 0 (recv)

# 6 LOAD_FAST 0 (recv)
# 8 RETURN_VALUE

gen = generator()
gen.send(None) # 1
gen.send(2) # 2

gen = generator()
gen.send(None) # 1

lasti = gen.gi_frame.f_lasti
lasti # 2 -> YIELD_VALUE를 의미(어디까지 제너레이터가 진행되었는지)
```

- 코루틴
  - 특징
    - 제너레이터 기반
    - thread state와 유사하게, frame 오브젝트를 갖고 있음
    - frame 오브젝트
      - 코루틴이 어디까지 실행되었는지 알고 있음
      - 지역 변수들의 상태 저장(함수 일시정지 후 재개 가능)
- `yield from == await`
  - 기능
    - **제너레이터 내부에서 또 다른 제너레이터(subgenerator)를 사용하기 위함**
      - 따라서 코루틴을 이해하기 위해서는 제너레이터를 이해하는 것이 중요함
- `await`
  - 기능
    - **제너레이터 안에서 서브제너레이터를 실행하는 것과 거의 유사 ~ yield from**
- `send`함수의 내부
  - 스레드의 state를 가져옴
    - `PyThreadState *tstate = PyThreadState_GET();`
  - generator의 gi_frame을 가져옴
    - `PyFrameObject *f = gen->gi_frame;`
  - argument 처리를 해줌
    - `*(f->f_stacktop++) = result;`
    - 프레임의 value stack의 top에 argument를 넣어줌
      - 그래서 generator안으로 값을 넘겨줄 수 있었음
  - 스레드 state의 현재 실행중인 frame을 generator의 f_back으로 넘겨줌(콜스택)
    - `f->f_back = tstate->frame;`
      - generator의 실행이 끝나면 tstate의 frame으로 다시 돌아옴
  - **`result = PyEval_EvalFrameEx(f, exc);`**
    - 프레임을 실행하는 함수
    - 바이트의 OP코드는 이 함수 내부에서 실행됨
  - `Py_CLEAR(f->f_back);`

### Event Loop for non-preemptive multitasking

`asyncio.sleep()`에 대한 설명(완전히 같은 구현은 아님)

- *이 부분이 잘 이해가 안된다. 특히, `await`가 `yield from`이며, `send`와 같다는게 무슨 뜻인지?*
  - coroutine사이의 bidirectional communication이 가능하게 해주는 역할?
- await가 yield from이라면, `await coro`가 호출되었을 때, 일단은 `coro`에게 실행 흐름을 넘겨 준 뒤에, `coro` 내부에서, 어떤 경우에 다시 메인 event loop로 실행 흐름을 넘겨주는가?
  - *`coro`내부에 또 다른 `await coro2`가 존재하면, 그 `await`에 의하여 실행 흐름이 `coro`에서 `coro2`로 넘어가게 되고, 그러면 언제 어떻게 코루틴 안에서 메인 event loop로 실행 제어권을 넘겨주는것인지*
  - *네트워크 IO에서 코루틴을 사용할 경우, 어떠한 방식으로 request를 보내면 메인 이벤트 루프로 실행 제어권을 보내고, 어떻게 response를 받았을 때, 다시 실행 제어권을 받아올 수 있는지 궁금함*
    - 이벤트 루프가 처리하는것인가?
- `await coro`은 결국, 실행 흐름을 `coro`로 넘겨주어서 실행하다가, `coro`속의 어떠한 IO연산이 있는 곳에서 *어떠한 흑마법* 을 부려서 그 때에는 main event loop로 실행흐름을 넘겨줌. 그리고 그러한 IO연산이 다 끝나면 event loop가 *그것을 감지하고?* 나머지 `coro`의 연산을 수행(?)
  - *코루틴 오브젝트 자체가 task의 요소로 들어가는듯??*

```py
async def sleep(delay, result=None, *, loop=None):
    if delay <= 0:
        await __sleep0()
        return result

    if loop is None:
        loop = events.get_event_loop()
    future = loop.create_future()
    # event loop에 delay이후에 set_result를 호출하도록 스케쥴링 함
    # future, result는 future.set_result의 파라미터로 들어감
    h = loop.call_later(delay, future.set_result, future, result)

    # await future은 yield from이며 send와 같음
    # Q) 이 send된 값은 어디에서 받고 있는가?
    return await future

# __sleep0의 내부구현
@types.coroutine
def __sleep0():
    yield

# Future의 내부구현
class Future:
    def __await__(self):
        if not self.done():
            # This tells task to wait for completion
            # self를 yield한 값을 어디에서 받고 있는가? -> Task객체
            yield self
        # Q) 이 조건분기로는 어떻게 들어가는 것인가?
        if not self.done():
            raise RuntimeError("await wasn't used with future")
        return self.result()

    __iter__ = __await__ # yield from과 compatible하게 만들어줌


# Future를 래핑한 친구
class Task(Future):
    def _step(self):
        try:
            # coroutine을 직접 send
            # coroutine과 event loop에 관련된 부분은 대부분 이곳에 존재
            result = self.coro.send(None)
        except StopIteration as exc:
            self.set_result(exc.value)
        except Exception as exc:
            self.set_exception(exc)
        else:
            # e.g) asyncio.sleep(0)에서 yield만 했을 경우(== yield None)
            if result is None:
                # 다시 스케쥴링
                self._loop.call_soon(self._step)
            # 원래의 구현에서는 Future를 체크하는것이 아니라, 어떠한 flag값을 체크하는데, 이해에 큰 무리가 없음
            elif isinstance(result, Future):
                # Future자체에 self._step을 add_done 콜백으로 등록
                result.add_done_callback(self._step)

    def __init__(self, coro, *, loop=None):
        super().__init__(loop=loop)
        self._coro = coro
        self._loop.call_soon(self._step)


class Future:
    # Q) promise오브젝트의 then같은 느낌?
    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    # Q) promise오브젝트의 resolve 함수 같은 느낌?
    def set_result(self, result):
        self._result = result
        self._state = _FINISHED
        # 바로 callback들을 실행하는 것이 아님
        self._schedule_callbacks()

    def _schedule_callbacks(self):
        callbacks = self._callbacks[:]
        if not callbacks:
            return

        self._callbacks[:] = []
        for callback in callbacks:
            # callback함수들을 이벤트루프에 스케쥴링함(태스크 큐에 삽입)
            self._loop.call_soon(callback, self)
```

- 태스크가 생성(create_task)
- 태스크의 `_stop`이 `call_soon`에 의하여 스케쥴링 됨
- `_stop`메서드에서 coroutine을 send
  - 헤당 코루틴 내부에 값이 없을 때, `_step`이 다시한 번 스케쥴링 됨
    - *근데, 그럼 무한루프가 되는 것이 아닌가?*
  - 값이 있는 경우에는, `_stop`을 `Future`의 add_done_callback에 넘겨줌
- 추후에 Future가 완료되어서 값이 `set_result`즉, 값이 세팅되면 해당 콜백들이 이벤트루프에 스케쥴링 됨

핸들 오브젝트(함수를 래핑한 친구)

```py
class Handle:
    def __init__(self, callback, args, loop):
        self._callback = callback
        self._args = args
        self._loop = loop

    # 넘겨주었던 callback을 실행함
    def _run(self):
        self._callback(*self._args)


class TimeHandle(Handle):
    def __init__(self, when, callback, args, loop):
        super().__init__(callback, args, loop)
        self._when = when

    # 비교연산자가 있기 때문에, 정렬이 가능
    def __gt__(self, other):
        return self._when > other._when
```

### Making Custom Event Loop

Custom Evevnt loop 만들기

```py
# nodejs의 event loop와 매우 유사
class CustomEventLoop(AbstractEventLoop):
    def __init__(self):
        # timer handle를 갖음(특정 시간이 되면 실행될 친구들을 갖고 있음)
        self._scheduled = []
        # 수행할 준비가 된 handle 오브젝트들이 존재
        self._ready = deque()

    def create_future(self):
        return Future(loop=self)

    def create_task(self, coro):
        return Task(coro, loop=self)

    def time(self):
        return time.monotonic()

    # just for not making exception
    def get_debug(self):
        pass

    def _timer_handle_cancelled(self, handle):
        pass

    # many other public functions
    def call_soon(self, callback, *args):
        handle = Handle(callback, args, self)
        self._ready.append(handle)
        return handle

    def call_later(self, delay, callback, *args):
        timer = self.call_at(self.time() + delay, callback, *args)
        return timer

    # Q) 애초에 근데, 어떻게, 지금 상황이 몇초가 지난것인지 알 수 있는지?
    def call_at(self, when, callback, *args):
        timer = TimerHandle(when, callback, args, self)
        heappush(self._scheduled, timer)
        return timer

    def run_forever(self):
        while True:
            self._run_once()

    def _run_once(self):
        while self._scheduled and self._scheduled[0]._when <= self.time():
            timer = heappop(self._scheduled)
            self._ready.append(timer)

        len_ready = len(self._ready)
        for _ in range(len_ready):
            handle = self._ready.popleft()
            handle._run()

        timeout = 0
        if self._scheduled and not self._ready:
            timeout = max(0, self._scheduled[0]._when - self.time())
        time.sleep(timeout)
```

- 한계
  - 위의 코드에서는 `timeout`이 0인경우 spinning(무한루프)
  - `timeout`이 무한대에 가까우면 Freezing
- **위의 한계를 극복하기 위하여 Selector를 도입**
- Selector
  - 기능
    - 운영체제의 polling함수를 설정할 수 있도록 만든 래핑 클래스
    - 각 운영체제마다 사용하는 poll이 다름
    - defualtselector는 운영체제에 맞는 selector를 가져옴

Selector 예시 코드

```py
import selectors
import socket

ssocket, csocket = socket.socketpair()
ssocket.setblocking(False)
csocket.setblocking(False)

selector = selectors.DefaultSelector()
selector.register(ssocket.fileno(), selectors.EVENT_READ)
selector.select(timeout=None) # wating here(blocking until a registered event comes)

ssocket.recv(1) # b'\0'


#####
# from other threads
#####
csocket.send(b'\0')
```

개선된 Custom Event Loop

```py
class CustomEventLoop(AbstractEventLoop):
    def __init__(self):
        self._scheduled = []
        self._ready = deque()
        self._selector = selectors.DefaultSelector()
        self._ssocket, self._csocket = socket.socketpair()
        self._ssocket.setblocking(False)
        self._csocket.setblocking(False)
        self._selector.register(self._ssocket.fileno(), selectors.EVENT_READ)

    def call_soon_threadsafe(self, callback, *args):
        handle = self.call_soon(callback, *args)
        self._csocket.send(b'\0')
        return handle

    ...

    def _run_once(self):
        while self._scheduled and self._scheduled[0]._when <= self.time():
            timer = heappop(self._scheduled)
            self._ready.append(timer)

        len_ready = len(self._ready)
        for _ in range(len_ready):
            handle = self._ready.popleft()
            handle._run()

        timeout = None
        if self._ready:
            # 바로 실행해야 하는 친구들이 있으면 실행
            timeout = 0
        elif self._scheduled:
            # 0번의 쨰와 현재 시간이 차 시간만큼 나중에 실행
            timeout = max(0, self._scheduled[0]._when - self.time())

        events = self._selector.select(timeout)
        if events:
            self._ssocket.recv(1)
```

### 부록0: asyncio.run(main, *, debug=True)

*도대체 누가 future의 `set_result()`함수를 실행시켜주는가?*

- 1 `asyncio.run(main, *, debug=False)`
  - 1-1 현재 돌고 있는 이벤트 루프가 존재하면 => 런타임 에러 발생
  - 1-2 새 이벤트 루프 생성 & 세팅
  - 1-3 `loop.run_until_complete(main)`
- 2 `loop.run_until_complete(self, future)`
  - 2-1 main이 coroutine이면 Task로 래핑해줌
  - 2-2 `tasks.ensure_future(future, loop=self)`
    - coroutine이나 awaitable을 future로 래핑
    - `task = loop.create_task(coro_or_future)`
    - `loop.create_task(coro)`
      - `task = tasks.Task(coro, loop=self, name=name)`
        - *이 부분 복습 필요*
        - `class Task(futures._PyFuture)`
          - `super().__init__(loop=loop)`
            - `class Future:`
              - `_state = _PENDING`
              - `_result`
              - `_exception`
              - `_loop`
              - `_source_traceback`
              - `_callbacks`
            - `self._coro = coro`
          - `self._loop.call_soon(self.__step, context=self._context)`
          - `_register_task(self)`
      - `return task`
  - 2-3 `future.add_done_callback(_run_until_complete_cb)`
  - 2-4 `self.run_forever()`
  - 2-5 `future.result()`
- 3 `self.run_forever()`
  - `stop()`이 호출될 때 까지 run함
  - 3-1 *`events._set_running_loop(self)`*
    - event loop가 사용하는 low level function
  - 3-2 무한 루프
    - `self._run_once()`
- 4 `self._run_once(self)`
  - 이벤트 루프의 한번의 full iteration
  - 현재 모든 준비된 callback들을 호출하고 -> I/O를 polling -> resulting callback들을 스케쥴링 -> `call_later` callback을 스케쥴링
  - 4-1 캔슬링된 scheduled 태스크는 `handle._scheduled = False`
  - 4-2 if) ready인 태스크가 존재 => selector timeout = 0 else => timeout = selector max timeout과 scheduled priority queue의 가장 앞요소의 when 중에서 더 최솟값을 assign
  - 4-3 `event_list = self._selector.select(timeout)` & `self._process_events(event_list)`
    - *특정 이벤트가 발생할 떄 까지 일단 blocking? fd의 이벤트 dispatch를 기다림. 그런데 무슨 이벤트일까?*
      - `BaseSelectorEventLoop(base_events.BaseEventLoop)` 에서 정의된 `selector = selectors.DefaultSelector()`
    - selector로부터 받아온 이벤트를 processing
  - 4-4 scheduled된 task를 iterate하면서, 현재 시간보다 이전에 끝난 task들을 schedule heap에서 pop하고 ready queue에 넣어줌
    - *시간과 별개로, 그냥 `set_result()`로 끝난 future를 어떻게 파악해서 ready에 넣어줄 수 있는가?*
    - *coroutine을 task로 쌓은 경우, 콜백은 무엇이고 어떻게 실행되는가?*
  - 4-5 ready로 스케쥴된 callback들을 호출
    - `handle = self._ready.popleft()`
    - `handle._run()`

### 부록1: yield from

yield from 코드의 예시1: 결과 받아오기

```py
def reader():
    for i in range(4):
        yield '<< %s' % i

def reader_wrapper(g):
    # These three codes are same
    # way1
    yield from g

    # way2
    # for i in g:
    #     yield i

    # way3
    # yield g.send(None)
    # yield g.send(None)
    # yield g.send(None)
    # yield g.send(None)

wrap = reader_wrapper(reader())
for i in wrap:
    print(i)

# Result
# << 0
# << 1
# << 2
# << 3
```

- `yield`
  - **실행 흐름과 값을 원래 스레드 state의 프레임으로 넘겨줌**
- `yield from`
  - 기능
    - **서브제너레이터로 실행흐름과 parameter를 넘겨주고, lazy하게 값을 생성하게 한 뒤에 그것을 자신의 caller로 해당 값과 실행 흐름을 넘겨줌**
      - transparent two way channel
    - caller와 sub-generator 사이에 transparent한 bidirectional connection을 establish해줌
      - transparent
        - 모든것을 올바르게 propagate하는 것(값, exceptions 등)
      - bidirectional
        - both sent from and to a generator

yield from 코드의 예시2: 파라미터 넘겨주기

```py

def writer():
    while True:
        w = (yield)
        print('>> ', w)


def writer_wrapper(coro):
    # way1
    yield from coro

    # way2
    # coro.send(None)
    # while True:
    #     sent = (yield)
    #     coro.send(sent)

    # way3
    # coro.send(None)
    # coro.send((yield))
    # coro.send((yield))
    # coro.send((yield))
    # coro.send((yield))
    # yield


w = writer()
wrap = writer_wrapper(w)
wrap.send(None)
for i in range(4):
    print(wrap.send(i))
```

- 위의 코드처럼 `yield from`은 실행 흐름과 parameter를 넘겨줌
  - sub generator로 데이터 송신 가능

yield from 코드의 예시3: 예외 처리

```py
class SpamException(Exception):
    pass

def writer():
    while True:
        try:
            w = (yield)
        except SpamException:
            print('***')
        else:
            print('>> ', w)

def writer_wrapper(coro):
    # way1
    yield from coro

    # way2
    # coro.send(None)
    # while True:
    #     try:
    #         sent = (yield)
    #     except Exception as e:
    #         coro.throw(e)
    #     else:
    #         coro.send(sent)

w = writer()
wrap = writer_wrapper(w)
wrap.send(None)
for i in [0, 1, 2, 'spam', 4]:
    if i == 'spam':
        wrap.throw(SpamException)
    else:
        wrap.send(i)

# # Expected Result
# >>  0
# >>  1
# >>  2
# ***
# >>  4
#
# # Actual Result
# >>  0
# >>  1
# >>  2
# Traceback (most recent call last):
#   ... redacted ...
#   File ... in writer_wrapper
#     x = (yield)
# __main__.SpamException
```
