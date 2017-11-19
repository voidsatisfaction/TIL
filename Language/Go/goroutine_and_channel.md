# Goroutine과 Channel기본

## 참고

- [A Tour of Go](https://tour.golang.org/concurrency/1)

## Goroutine

Goroutine은 Go의 런타임에 의해서 관리되는 가벼운 스레드이다.

```go
go f(x, y, z)
```

위의 경우에 `f, x, y, z`의 평가는 현재 goroutine에서 일어나고, `f`의 실행은 새로운 goroutine에서 일어난다.

참고로 고루틴이 프로그램에 남아있으면 프로그램은 꺼지지 않는다(nodejs와 다른 점)

```go
func say(s string) {
	for i := 0; i < 5; i++ {
		time.Sleep(100 * time.Millisecond)
		fmt.Println(s)
	}
}

func main() {
	go say("world")
	say("hello")
}

// 아래의 실행순서는 일정하지 않다.
// world
// hello
// hello
// world
// world
// hello
// hello
```

## Channels

채널은 타입이 정해져있는 값들을 주고 받을 수 있는 통로이며, 채널 연산자를 사용한다(`<-`)

```go
ch <- v // Send v to channel ch
v := <-ch // Receive from ch, and assign value to v

// Must be created before use
ch := make(chan int)
```

기본적으로 보내고 받는 것은 한쪽이 준비가 되었을 때 까지 블록된다. 이는 goroutine이 명시적인 록이나 조건 변수들 없이 고루틴이 동기화 되는 것을 도와준다.

```go
func sum(s []int, c chan int) {
  sum := 0
  for _, v := range s {
    sum += v
  }
  c <- sum // send sum to c
}

func main() {
  s := []int{7, 2, 8, -9, 4, 0}

  c := make(chan int)
  go sum(s[:len(s)/2])
  go sum(s[len(s)/2:])
  x, y := <-c, <-c // receive from c

  fmt.Println(x, y, x+y) // -5, 17, 12
}
```

위의 코드에서는 슬라이스 속의 숫자를 더해주는데 두개의 고루틴으로 작업을 분산시킨다. 두개의 고루틴에서의 계산이 끝나면 마지막 결과를 계산한다. 하지만, **계산의 순서는 보장되지 않는다**

(먼저 `go sum(s[:len(s)/2])`이 실행되었어도 x에 그 결과가 들어간다는 보장이 없다)

## Buffered Channels

채널은 buffered될 수 있다.

```go
ch := make(chan int, 100)
```

- 채널의 버퍼가 다 차있으면 채널에 값을 보내는 것이 블록된다.
- 채널의 버퍼가 비었으면 채널로부터 값을 받는 것이 블록된다.
- 채널에 값을 보낸만 큼 값을 받아야한다(그렇지 않으면 deadlock)

```go
func main() {
	ch := make(chan int, 3)
	ch <- 1
	ch <- 2
	fmt.Println(<-ch) // 1
	ch <- 3
	fmt.Println(<-ch) // 2
	fmt.Println(<-ch) // 3
}
```

## Range and Close

channel에서 값을 보내는 쪽은 channel을 **닫을 수 있다** channel의 값을 받는쪽은 그 channel이 닫혀있는지 다음과 같이 확인할 수 있다.

```go
v, ok := <-ch // if there is no more values to receive :: ok => false
```

루프 `for i := range c`는 channel이 닫힐 때 까지 반복적으로 값들을 받는다.

1. 채널은 반드시 보내는 쪽이 닫을 수 있다.
2. 채널은 파일과 다르게 명시적으로 닫아줄 필요는 없으나, `range`루프를 없앨때와 같은 경우 반드시 명시적인 닫음이 필요하다.

```go
func fibonacci(n int, c chan int) {
  x, y := 0, 1
  for i := 0; i < n; i++ {
    c <- x
    x, y = y, x+y
  }
  close(c)
}

func main() {
  c := make(chan int, 10)
  go fibonacci(cap(c), c)
  for _, i := range c {
    fmt.Println(i) // 0 1 1 2 3 ...
  }
}
```

## Select

select는 고루틴이 multiple communication operations를 기다리게 한다.

select는 그 케이스들이 실행될 수 있을 때 까지 블록하고, 그 케이스를 실행한다. 만일 다양한 케이스가 준비되면 하나씩 무작위 순서로 실행한다.

```go
func fibonacci(c, quit chan int) {
  x, y := 0, 1
  for {
    select {
    case c <- x:
      x, y := y, x+y
    case c <- quit:
      fmt.Println("quit")
      return
    }
  }
}

func main() {
  c := make(chan int)
  quit := make(chan int)
  go func() {
    for i := 0; i < 10; i++ {
      fmt.Println(<-c) // 0 1 1 2 3 ...
    }
    quit <- 0
  }()
  fibonacci(c, quit)
}
```

## Default Selection

select속의 default케이스는 다른 케이스가 준비되지 않으면 발동된다.

블로킹 없이 데이터를 주고받을 때에는 default키워드를 이용하라.

```go
func main() {
  tick := time.Tick(100 * time.Millisecond)
  boom := time.After(500 * time.Millisecond)
  for {
    select {
    case <-tick:
      fmt.Println("tick.")
    case <-boom:
      fmt.Println("BOOM!")
      return
    default:
      fmt.Println("     .")
      time.Sleep(50 * time.Millisecond)
    }
  }
}
```

## sync.Mutex

- channels: 고루틴들의 의사소통을 도와준다.
- mutex(mutual exclusion): 의사소통이 필요 없이 충돌을 막기위해서 하나의 고루틴이 한번에 변수에 접근할 수 있도록 하는 방법 `Lock`, `Unclock`

```go
package main

import (
	"fmt"
	"sync"
	"time"
)

// SafeCounter is safe to use concurrently.
type SafeCounter struct {
	v   map[string]int
	mux sync.Mutex
}

// Inc increments the counter for the given key.
func (c *SafeCounter) Inc(key string) {
	c.mux.Lock()
	// Lock so only one goroutine at a time can access the map c.v.
	c.v[key]++
	c.mux.Unlock()
}

// Value returns the current value of the counter for the given key.
func (c *SafeCounter) Value(key string) int {
	c.mux.Lock()
	// Lock so only one goroutine at a time can access the map c.v.
	defer c.mux.Unlock()
	return c.v[key]
}

func main() {
	c := SafeCounter{v: make(map[string]int)}
	for i := 0; i < 1000; i++ {
		go c.Inc("somekey")
	}

	time.Sleep(time.Second)
	fmt.Println(c.Value("somekey"))
}

```

## 외부 API이용 함수로부터 비동기적으로 에러나 데이터를 받도록 channel 이용하기

Near-me라는 서비스의 내부 구조에서, 다양한 이벤트 사이트로부터 이벤트 데이터를 받을때 goroutine을 이용해서 비동기적으로 받는 구조를 채택하였다. 그렇게 하므로써, 시간적인 성능향상을 꾀했다.

그런데 하나의 함수에서 채널을 이용해서 데이터를 받아오는 것은 쉬우나, 에러 역시 채널을 통해서 받아와야 하기 떄문에 다소 복잡하다. 데이터를 외부 API로부터 받아올 수 있을때에는 외부 API데이터를 채널에 넘겨주고, 혹시나 그 과정에서 오류가 생기면 에러를 넘겨주어야 한다.

현재로서는 다음과 같은 아이디어가 있다.

1. 각각의 외부 API용 이벤트 채널과 각각의 API용 에러 채널을 생성해서 채널에 값을 넘겨주는 방식으로 처리 한다(select이용)
2. 각각의 외부 API용 이벤트 채널을 이용하나 에러는 하나의 채널만을 이용한다. 이 역시 select를 이용한다.
3. 채널을 하나로 통합해서 빈 인터페이스를 받을 수 있도록한다. 그리고 받은 데이터를 `reflect`를 이용하여 에러인지, 각각의 이벤트인지를 확인하여 데이터를 받는다.

지금 실제로 작성한 코드는 아래와 같다.

```go
type Events struct {
	Connpass   []api.ConnpassEvent
	Doorkeeper api.DoorkeeperEvents
}

func GetAllEvents(userLocation []string) (*Events, error) {
	// this is the number of event type
	typeNum := 2

	connpassCH := make(chan []api.ConnpassEvent)
	errCH := make(chan error)
	connpassEventNums := 100
	go api.ConnpassGetEvents(userLocation, connpassEventNums, connpassCH, errCH)

	doorkeeperCH := make(chan api.DoorkeeperEvents)
	go api.DoorkeeperGetEvents(userLocation, 0, doorkeeperCH, errCH)

	var connpassEvents []api.ConnpassEvent
	var doorkeeperEvents api.DoorkeeperEvents
	for i := 0; i < typeNum; i++ {
		select {
		case err := <-errCH:
			if err != nil {
				log.Fatal("Fetch events error!!")
				log.Fatal(err)
				return nil, err
			}
		case connpassEvents = <-connpassCH:
		case doorkeeperEvents = <-doorkeeperCH:
		}
	}
	es := &Events{
		Connpass:   connpassEvents,
		Doorkeeper: doorkeeperEvents,
	}
	return es, nil
}
```
