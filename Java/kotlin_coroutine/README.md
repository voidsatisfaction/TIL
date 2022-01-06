# Kotlin Coroutine

- 의문
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
    val token = requestToken()
    val post = createPost(token, item)
    processPost(post)
}

// Continuation인터페이스
interface Continuation<in T> {
  val context: CoroutineContext
  fun resume(value: T)
  fun resumeWithException(exception: Throwable)
}
```

- 컴파일러가 suspend funtion을 CPS Transformation시킴
  - e.g) `suspend fun createPost(token: Token, item: Item): Post {...}`
    - `Object createPost(Token token, Item item, Continuation<Post> cont) { ... }`
      - 여기있는 `Continuation<Post>`가 callback임(CPS(Continuation Passing Style))

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
