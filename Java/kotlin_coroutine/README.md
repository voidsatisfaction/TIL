# Kotlin Coroutine

## 의문

- coroutine scope?
- coroutine?

## 개요

```kotlin
fun main() = runBlocking {
  launch {
    delay(1000L)
    println("World!")
  }
  println("Hello")
}
```

- 정의
  - suspendable computation의 하나의 인스턴스
  - non-preemptive multitaking을 하기 위한 subroutine의 일반화
- 개요
  - `kotlinx.coroutines`에 코루틴을 위한 다양한 라이브러리가 준비
- 특징
  - 스레드의 개념에 종속되지 않음, 한 스레드에서 작업 후 suspend되었다가 다른 스레드에서 재개할 수 있음
- 구성 요소
  - `launch`
    - 코루틴 빌더이며, concurrent하게 블록 내부의 코드로 새 코루틴을 독립적으로 동작하게 시작함
    - CoroutineScope에서만 선언되어 있음
  - `delay`
    - 특정 시간동안 코루틴을 suspend하고, 해당 스레드를 블로킹하지 않으며, 다른 코루틴들이 동작하고 주어진 스레드를 사용할 수 있게 하는 suspending function
  - `runBlocking`
    - 일반 `fun main()`과 `runBlocking`의 블록 내부에 있는 코루틴을 이어주는 코루틴 빌더
    - 해당 코드가 실행되는 스레드가 호출되는 동안 블로킹됨
      - 바람직한 것은 아님
