# Go Concurrency Pattern

## 참고

- [Go Concurrency Pattern Slides - Rob Pike(Google)](https://talks.golang.org/2012/concurrency.slide#1)

- [Go Concurrency Pattern Video - Rob Pike(Google)](https://www.youtube.com/watch?v=f6kdp27TYZs)

## Basic Questions

1. concurrency의 지원 이유
2. concurrency의 정의
3. concurrency의 아이디어의 원천
4. concurrency의 장점
5. concurrency의 활용

## 1. Concurrency의 지원 이유

세상은 복잡한 상호작용으로 이루어져 있기 때문에, 이를 구현하기 위해서는 단순한 절차지향적 프로그래밍으로는 한계가 있다. 그래서 세상의 행동 모델을 제대로 구현하기 위해 지원한다.

## 2. Concurrency의 정의

Concurrency란, 개별적으로 실행되는 계산들의 구성이다.

또한, 소프트웨어를 구성하는 하나의 방식이며, 특히 실제의 세상과 잘 상호작용 하는 깔끔한 코드를 작성하는 하나의 방식이라고 할 수 있다.

Parallelism과는 다르다. 하나의 processor는 concurrent할 수는 있지만 parallel할 수 는 없다. 반면, 잘 쓰여진 concurrent program은 parallel multiprocessor에서 효과적으로 작동할 수 있다.

> Concurrency is about dealing with lots of things at once. Parallelism is about doing lots of things at once.

## 3. Concurrency의 아이디어 원천

### 소프트웨어 공학을 위한 모델

1. Easy to understand.
2. Easy to use.
3. Easy to reason about.
4. You don't need to be an expert.

### 역사

Occam, Erlang, Newsqueak, Concurrent ML, Alef, Limbo ...

### 특징

Go는 Newsqueak-Alef-Limbo 계열의 최신형 concurrency를, `first-class-channel`를 사용하여 지원한다.

Erlang은 오리지널 CSP와 비슷. channel이 아닌 process name으로 상호작용한다.

## *. concurrency의 예시

다음과 같은 함수가 있다고 하자.

```go
func boring(msg string) {
    for i := 0; ; i++ {
        fmt.Println(msg, i)
        time.Sleep(time.Duration(rand.Intn(1e3)) * time.Millisecond)
    }
}
```

위의 함수는 `main()`에서 실행된다면 무작위 시간(1초내)마다 메시지를 출력할 것이다. `main()`은 위의 `boring()`이 끝나기까지 기다릴 것이다.

---

`go`라는 statement를 사용해보자.

```go
func main() {
    go boring("boring!")
    fmt.Println("I'm listening.")
    time.Sleep(2 * time.Second)
    fmt.Println("You're boring; I'm leaving.")
}
```

위의 코드는, `go boring()`에 의하여 boring함수에 대한 gorutine이 만들어져, 호출한 쪽이 기다리지 않도록 한다.

### goroutine이란

결국 goroutine은 `go` statement로 시작되는 독립적으로 실행되는 함수이다.

- goroutine만의 call stack이 따로 존재한다.
- 매우 저렴하다. 수천 수십만 go routine을 실제로 운영할 수 있다.
- 스레드가 아니다. 따라서 하나의 스레드에 수천개의 goroutine이 존재할 수 있다. 대신 많은 스레드에서 동적 + 동시다발적으로 운용될 수 있다.
- 값싼 스레드라고 생각해도 나쁘지 않다.

Communication은 Channel을 통해서 이루어진다.

### Channel이란

채널은 두 고루틴이 상호작용할 수 있도록 connection을 제공한다.

```go
func main() {
    c := make(chan string)
    go boring("boring!", c)
    for i := 0; i < 5; i++ {
        fmt.Printf("You say: %q\n", <-c) // Receive expression is just a value.
    }
    fmt.Println("You're boring; I'm leaving.")
}

func boring(msg string, c chan string) {
    for i := 0; ; i++ {
        c <- fmt.Sprintf("%s %d", msg, i) // Expression to be sent can be any suitable value.
        time.Sleep(time.Duration(rand.Intn(1e3)) * time.Millisecond)
    }
}
```

위의 코드에서 `main()`은 `<-c`를 실행하고 이는 c라는 채널에서 값이 오길 기다린다.

이와 마찬가지로 `boring()`이 `c<-value`를 실행할때, 이는 receiver가 준비될때까지 기다린다.

sender와 receiver는 communication의 주체가 될 수 있도록 준비되었을때만 데이터를 주고받을 수 있다. 그렇지 않으면 계속 기다린다.

이러한 속성으로, channel은 communicate하며, synchronized된다.

#### buffered channel

buffering은 synchronization을 제거한다. 그러나 대개는 단순한 channel이 사용됨.

### Don't communicate by sharing memory, share memory by communicating.
