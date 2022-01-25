# Kotlin Coroutine

- 의문
- 개요개요
  - 코루틴이란
    - 정의
    - 구성
- 원리
- 개요
  - Coroutine Context
  - Coroutine Builder
  - 중단했다가 재개하는 방법
  - 실행 흐름 예시

## 의문

- *coroutine scope?*
- *coroutine builder?*
- *coroutine?*
  - suspend function 자체가 코루틴인가?
    - 아니다. 코루틴은 실행 흐름을 의미
    - suspend function은 코루틴속에서 yield할 수 있는 함수
- 코루틴에서 `delay`를 사용하는 경우, 특정시간이 지났는지는 어떻게 파악하지? 이벤트 루프를 사용하는건가?

## 개요개요

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

## 원리

suspend 함수와 direct style함수의 코드 비교

```kotlin
// direct style의 함수

fun postItem(item: Item) {
    val token = requestToken()
    val post = createPost(token, item)
    processPost(post)
}

// suspend 함수
suspend fun postItem(item: Item) {
    val token = requestToken() // continuation
    val post = createPost(token, item) // continuation
    processPost(post) // continuation
}

// Continuation인터페이스 (callback과 본질적으로 같음)
interface Continuation<in T> {
  val context: CoroutineContext
  fun resume(value: T)
  fun resumeWithException(exception: Throwable)
}
```

suspend 함수의 컴파일러로 인한 CPS Transformation(State Machine을 사용함)

```kotlin
// suspend 함수
suspend fun postItem(item: Item) {
    val token = requestToken() // continuation
    val post = createPost(token, item) // continuation
    processPost(post) // continuation
}

// 1. Labels
// 컴파일러가 switch 코드(아래는 수도코드)로 변경
suspend fun postItem(item: Item) {
    val sm = object : CoroutineImpl { ... }
    switch (sm.label) {
      case 0:
        val token = requestToken()
      case 1:
        val post = createPost(token, item)
      case 2:
        processPost(post)
    }
}

// 2. State & Callback
// 컴파일러가 switch 코드(아래는 수도코드)로 변경
suspend fun postItem(item: Item) {
    val sm = object : CoroutineImpl {
      fun resume(...) {
        // callback으로 다시 멈췄던 곳에서 시작할 수 있도록 함
        // 그럼, 이 콜백을 등록하고 실행하는 이벤트 루프가 필요하겠네?!
        postItem(null, this)
      }
    }
    switch (sm.label) {
      case 0:
        sm.item = item
        sm.label = 1
        // State Machine as Continuation
        val token = requestToken(sm)
      case 1:
        val post = createPost(token, item, sm)
      case 2:
        processPost(post)
    }
}

// 3. Restore state
suspend fun postItem(item: Item) {
    val sm = object : CoroutineImpl {
      fun resume(...) {
        // callback으로 다시 멈췄던 곳에서 시작할 수 있도록 함
        // 그럼, 이 콜백을 등록하고 실행하는 이벤트 루프가 필요하겠네?!
        postItem(null, this)
      }
    }
    switch (sm.label) {
      case 0:
        sm.item = item
        sm.label = 1
        // State Machine as Continuation
        val token = requestToken(sm)
      case 1:
        val item = sm.item
        val token = sm.result as Token
        sm.lavel = 2
        val post = createPost(token, item, sm)
      case 2:
        processPost(post)
    }
}
```

- 대전제
  - 모든 asynchronous 라이브러리들(futures, ...)은 callback 기반임
    - 다만 그것을 어떻게 이쁘게 추상화했는지가 각 라이브러리의 포인트
    - 그렇기 때문에 어떤 라이브러리던, 코틀린 코루틴에 편입가능(jdk8, guava, nio, reactor, rx1, rx2)
- 컴파일
  - 컴파일러가 suspend funtion을 State Machine을 사용하여 CPS Transformation시킴
    - e.g) `suspend fun createPost(token: Token, item: Item): Post {...}`
      - => `Object createPost(Token token, Item item, Continuation<Post> cont) { ... }`
        - 여기있는 `Continuation<Post>`가 callback임(CPS(Continuation Passing Style))
- 런타임
  - 모든 suspension마다 다음을 수행
    - state(local variables)를 저장
    - 레이블 저장
    - restore state(sm에 있는 필요한 로컬 변수 꺼내옴)
    - suspended function을 callback과 함께 호출(`sm.resume`)
- 장점
  - State Machine으로 상태 관리하므로, 콜백이 클로저를 계속 생성하는데에 반해 클로저를 재사용하므로 효율적
  - 코드가 읽기 쉬움
    - `suspend`키워드로 어디서 I/O를 기다리는지 쉽게 파악 가능
  - 기존 async 라이브러리 쉽게 코루틴으로 편입 가능(jdk8, guava, nio, reactor, rx1, rx2)
    - 모두 콜백 기반이기 때문에 가능

### Coroutine Context

ContinuationInterceptor

```kotlin
interface ContinuationInterceptor : CoroutineContext.Element {
    companion object Key : CoroutineContext.Key<ContinuationInterceptor>

    fun <T> interceptContinuation(continuation: Continuation<T>): Continuation<T> {
        // continuation의 커스텀 래핑이 가능함
        ...
    }
}
```

DispatchedContinuation

```kotlin
class DispatchedContinuation<in T>(
    val dispatcher: CoroutineDispatcher,
    val continuation: Continuation<T>
): Continuation<T> by continuation {
    override fun resume(value: T) {
        // 다른 스레드 / 스레드풀에 실행을 디스패칭
        dispatcher.dispatch(context, DispatchTask(...))
    }
}
```

- 질문
  - 코루틴이 suspend function을 resume할때, 다른 스레드(e.g UI 스레드)에서 할 수 있도록 하기 위해서는 어떻게 해야할까?
    - `Continuation Interceptor`
- Coroutine Context
  - 개요
    - map
      - job, interceptor 등을 가지고 있음
- `Continuation Interceptor`
  - 개요
    - context의 일부, map of elements
  - 특징
    - continuation의 커스텀 래핑이 가능함
- `DispatchedContinuation`
  - 개요
    - Continuation의 wrapper
      - resume전에 다른 스레드로 dispatching 가능

## 개요

```kotlin
fun main() = runBlocking { // this: CoroutineScope
    launch { // launch a new coroutine and continue
        delay(1000L) // non-blocking delay for 1 second (default time unit is ms)
        println("World!") // print after delay
    }
    println("Hello") // main coroutine continues while a previous one is delayed
}
// Hello
// World!

fun main() = runBlocking { // this: CoroutineScope
    launch { doWorld() }
    println("Hello")
}

// this is your first suspending function
suspend fun doWorld() {
    delay(1000L)
    println("World!")
}
```

- 정의
  - suspendable computation의 하나의 인스턴스
  - c.f) 위키피디아 정의
    - non-preemptive multitaking을 하기 위한 subroutine의 일반화
- 특징
  - 스레드의 개념에 종속되지 않음
    - **한 스레드에서 작업 후 suspend되었다가 다른 스레드에서 재개할 수 있음**
  - `kotlinx.coroutines`에 코루틴을 위한 다양한 라이브러리가 준비
- 구성 요소
  - `runBlocking { }`
    - 코루틴과 관계없는 `fun main()`과 `runBlocking`의 블록 내부에 있는 코루틴들을 이어주는 코루틴 빌더
      - 코루틴 스코프의 생성
    - 해당 코드가 실행되는 스레드가 내부의 코루틴이 전부 완료되기 전까지 스레드가 블로킹됨
      - 바람직한 것은 아님
  - `launch { }`
    - *코루틴 빌더* 이며, concurrent하게 블록 내부의 코드로 새 코루틴을 독립적으로 동작하게 시작함
      - `new Thread()`와 유사한 개념
    - CoroutineScope에서만 name이 선언되어 있음
    - c.f) `Async`
      - Launch는 Job을 반환
      - Async는 Deffered를 반환
        - Deffered는 Job을 상속한 클래스이고, 타입 파라미터를 통해 코루틴의 Return Value를 받을 수 있음
  - `delay()`
    - 특정 시간동안 코루틴을 suspend하고, 해당 스레드를 블로킹하지 않으며, 다른 코루틴들이 동작하고 주어진 스레드를 사용할 수 있게 하는 suspending function
- Suspending function
  - 개요
    - 코루틴 내부에서 실행가능한 함수
  - 특징
    - 다른 suspending function을 사용하여, 코루틴의 실행을 중지할 수 있음

### Coroutine Context

- Job
  - 개요
    - 코루틴의 상태 정보를 들고 있음
      - active
      - completed
      - cancelled
    - job을 이용해 아직 끝나지 않은 job을 취소시키거나, join하거나 await가능
- Dispatcher
  - 개요
    - coroutine을 처리하기 위해 스레드에 할당하는 처리자
      - *이벤트 루프?*
  - Dispatcher Value
    - `null`
      - 부모의 Context를 상속받아 그대로 사용
    - `Dispatchers.Unconfine`
      - 백그라운드 스레드 풀을 공유
    - `Dispatchers.Default`
      - `Default Thread Pool`을 이용
    - `newSingleThreadContext` or `newFixedThreadPoolContext`
      - 코루틴 실행을 위한 스레드 풀을 별도로 만들어 사용
- Scope
  - 개요
    - *Scope내에서 컨텍스트간의 컨텍스트 요소와 cancellation 전파 전략을 담당하는 역할*

### Coroutine Builder

- 개요
  - `coroutineScope` 빌더를 사용해서 자신만의 scope를 생성할 수 있음
      - *자신만의라는 말의 의미는?*
  - 코루틴을 생성

### 중단했다가 재개하는 방법

코루틴의 컴파일

```kotlin
suspend fun plusOne(initial: Int) : Int {
  val one = 1
  var result = initial

  result += one

  return result
}

// 위의 함수가 컴파일 되면 아래와 같음

// state.label을 이용해 어디까지 실행되었는지 구분 가능하다

fun plusOne(initial: Int, countinuation: Countination) : Int {
  val state = continuation as empty ?: CoroutineImpl {…}
  switch(state.label) {
    case 0:
      state.label = 1
      val one = 1
      sm.one = one
      …
    case 1:
      val one = sm.one
      var result = initial
    case 2:
      result += one
    case 3:
      return result
  }
}
```

- 상태를 가지고 있으면 됨
  - Caller
  - PC
  - Stack
- 위 코드는 CPS 변환을 활용해서 코드를 생성

### 실행 흐름 예시

```kotlin
runBlocking {
  launch {
      println("1")
      yield()
      println("3")
      yield()
      println("5")
  }

  launch {
    println("2")
    yield()
    println("4")
    yield()
    println("6")
  }

  println("end")
}

// runBlocking 은 Coroutine Context이다. 외부의 스레드로부터 차단. (서로 간섭을 할 수 없다.)
// runblocking 된 스레드가 parent context(scope)가 되어 launch 한 2개의 코루틴을 commonPool에서 실행시킨다.
// thread 는 1개.
// 첫번째 코루틴 생성, (아직 실행 안됨- 스레드가 1개밖에 없기 때문이다. main 스레드가 양보하지 않았기 때문)
// 두번째 코루틴 생성,
// print end
// 첫번째 코루틴이 실행되고 양보를 하면 dispatcher가 다음걸 어떤걸 실행할지 결정한다.
// 두번째 코루틴이 실행되고 반복한다.
```
