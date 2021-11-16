# Reactor

- 의문
- 1] Reactive Programming의 소개
  - 1.2 Asynchronicity to the Rescue?
- 2] Reactive Streams의 특징
- 3] Reactor Core Features
  - 3.1 Flux: an Asynchronous Sequence of 0-N Items
  - 3.2 Mono: an Asynchronous 0-1 Result
  - 3.3 Flux, Mono의 간단한 사용 예시
  - 3.4 sequence를 프로그래밍 방식으로 생성하기(generate, create, push)

## 의문

## 1. Reactive Programming의 소개

- Reactive programming
  - 개요
    - 변화의 propagation과 데이터 스트림과 관련된 비동기 프로그래밍 패러다임
  - 특징
    - OOP에서 Observer 디자인 패턴의 확장
      - iterator는 pull-based
      - reactive streams는 push-based
    - publisher / subscriber
    - push된 값은 선언적으로 표현됨
    - 에러 핸들링
      - publisher의 새 값 push
        - `onNext`
      - publisher의 에러 시그널링
        - `onError`
      - publisher의 완료 시그널링
        - `onComplete`
- Reactive Streams
  - 개요
    - JVM에서의 reactive 라이브러리들을 위한 인터페이스와 상호작용의 룰의 집합을 정의하는 스펙
    - 해당 인터페이스는 Java9에서 `Flow`클래스로 통합됨
- Reactor
  - 개요
    - Reactive Programming 패러다임의 구현체
      - Reactive Streams의 구현체

### 1.2 Asynchronicity to the Rescue?

```java
// reactor version
userService.getFavorites(userId)
           .flatMap(favoriteService::getDetails)
           .switchIfEmpty(suggestionService.getSuggestions())
           .take(5)
           .publishOn(UiUtils.uiThreadScheduler())
           .subscribe(uiList::show, UiUtils::errorPopup);

// callback hell equivalent to reactor version
userService.getFavorites(userId, new Callback<List<String>>() {
  public void onSuccess(List<String> list) {
    if (list.isEmpty()) {
      suggestionService.getSuggestions(new Callback<List<Favorite>>() {
        public void onSuccess(List<Favorite> list) {
          UiUtils.submitOnUiThread(() -> {
            list.stream()
                .limit(5)
                .forEach(uiList::show);
            });
        }

        public void onError(Throwable error) {
          UiUtils.errorPopup(error);
        }
      });
    } else {
      list.stream()
          .limit(5)
          .forEach(favId -> favoriteService.getDetails(favId,
            new Callback<Favorite>() {
              public void onSuccess(Favorite details) {
                UiUtils.submitOnUiThread(() -> uiList.show(details));
              }

              public void onError(Throwable error) {
                UiUtils.errorPopup(error);
              }
            }
          ));
    }
  }

  public void onError(Throwable error) {
    UiUtils.errorPopup(error);
  }
});
```

- JVM에서의 async 코드 생성 방법
  - callbacks
    - callback으로 result가 사용가능할 때 작업을 처리
  - futures
    - async 메서드는 `Future<T>`를 즉시 반환함
    - 비동기 프로세스가 T값을 계산하지만, `Future`오브젝트가 해당 값의 접근을 래핑함
      - 값은 바로는 접근 못함
      - 값은 접근 가능할때 가져올 수 있음

## 2. Reactive Streams의 특징

- JVM위의 classic async 접근 방식을 다음과 같은 추가적인 측면에 집중해서 단점을 해결하려 함
  - **Composability / Readability**
  - **Data as a flow**
    - rich voca of operators
      - 사실 오퍼레이터는 Reactive Streams spec에 포함되지 않으나, reactive library들은 다양한 오퍼레이터 지원
    - source(publisher) to consumer(subscriber)
      - publisher로부터 시작된 데이터가 subscriber에서 그 프로세스를 끝냄
  - **subscribe 하기전까지 아무일도 일어나지 않음**
    - subscribing을 하면서 전체 체인에서의 데이터 흐름을 시작하게 함
      - subscriber가 publisher로 하나의 요청 시그널을 보내면서 내부적으로 동작하게 함
  - **Backpressure**
    - consumer가 producer에게 rate of emission이 너무 높다고 신호를 보낼 수 있음
    - subscriber의 모드(push-pull hybrid)
      - unbounded mode
        - publisher가 실현가능한 가장 빠른 속도로 데이터를 push하도록 함
      - request mechanism
        - publisher에게 요청을 보내서 n개의 요소를 가공할 준비가 되었다고 알려주면, 그만큼만 보냄
  - **concurrency-agnostic한 high level but high value 추상화**
  - **Hot vs Cold**
    - Cold sequence
      - 각각의 Subscriber마다 새로 시작
    - Hot sequence
      - late subscriber들은 subscribe한 이후의 시그널을 수신함
        - 몇몇 reactive streams는 캐시해서 과거의 이벤트를 리플레이가능
      - subscriber가 없어도 이벤트를 방출할 수 있음

## 3. Reactor Core Features

- reactor-core
  - 개요
    - Reactive Streams 스펙에 초점을 맞추는 reactive library (자바8 타겟)
    - Publisher를 구현하는 합성가능한 리액티브 타입을 소개하면서, `Flux`, `Mono`와 같은 rich voca도 제공
  - `Flux` object
    - 개요
      - 0..N 아이템의 리액티브 시퀀스를 나타냄
  - `Mono` object
    - 개요
      - (0..1) 결과를 나타냄

### 3.1 Flux: an Asynchronous Sequence of 0-N Items

Flux diagram

![](./images/flux1.png)

- `Flux<T>`
  - 개요
    - 비동기 sequence of 0 to N items를 발산하는 나타내는 표준 `Publisher<T>`
      - 선택적으로 completion signal 혹은 error에 의해서 제거됨
      - 이러한 시그널은 다운스트림 Subscriber의 `onNext`, `onComplete`, `onError`메서드 호출로 변환됨
  - 특징
    - Flux의 operator 처리 중간에 에러가 나도, 이는 전체 흐름의 에러가 아니라, 에러가 난 흐름의 `onError`에서 처리함

### 3.2 Mono: an Asynchronous 0-1 Result

Mono diagram

![](./images/mono1.png)

- `Mono<T>`
  - 개요
    - `onNext`를 통해서 최대 1개의 아이템을 발산하는 특수 특수한 `Publisher<T>`
      - `omComplete`시그널과 함께 제거되거나, `onError`시그널과 함께 제거됨(실패한 Mono)
  - 특징
    - 대부분의 `Mono`구현들은 `onNext`를 호출한 뒤에, `onComplete`를 즉시 호출할 것으로 기대됨
    - *`onNext`와 `onError`의 조합은 명시적으로 금지됨*
      - *그럼 에러 캐치는 어떻게 하나?*
    - 몇몇 연산자는 Mono를 Flux로 변환함
      - `Mono#concatWith(Publisher)`
      - c.f) `Mono#then(Mono)`는 또 다른 Mono를 반환

### 3.3 Flux, Mono의 간단한 사용 예시

Factory method를 사용하여 Flux, Mono 생성

```java
Flux<String> seq1 = Flux.just("foo", "bar", "foobar");

List<String> iterable = Arrays.asList("foo", "bar", "foobar");
Flux<String> seq2 = Flux.fromIterable(iterable);

Mono<String> noData = Mono.empty();

Mono<String> data = Mono.just("foo");

Flux<Integer> numbersFromFiveToSeven = Flux.range(5,3);
```

subscribe method의 활용 예시

```java
// Lambda로 subscriber 생성하기
Flux<Integer> ints = Flux.range(1,4);

ints.subscribe(i -> System.out.println(i), // 각각의 생성된 값과 함께 무엇인가를 행함
  error -> System.err.println("Error " + error), // 에러에 대한 반응
  () -> System.out.println("Done"), // sequence가 성공적으로 끝난 경우에, 코드를 실행
  sub -> sub.request(10) // 10개까지의 source의 요소를 원한다고 전달
);

// BaseSubscriber로 Lambda 대체하기
Flux.range(1, 10)
  .doOnRequest(r -> System.out.println("request of " + r))
  .subscribe(new BaseSubscriber<Integer>() {

    @Override
    public void hookOnSubscribe(Subscription subscription) {
      // demand for one full buffer
      request(1);
    }

    @Override
    public void hookOnNext(Integer integer) {
      System.out.println("Cancelling after having received " + integer);
      cancel();
    }
  })
// request of 1
// Cancelling after having received 1
```

- downstream request를 수정하는 연산자의 다른 카테고리
  - *메서드 의미가 이해가 잘 안됨*
  - `buffer(N)`
  - `prefetch`
  - `limitRate(N)`
    - 최대 N request가 업스트림으로 전파됨

### 3.4 sequence를 프로그래밍 방식으로 생성하기(generate, create, push)

publisher의 프로그래밍 방식 생성 예시: `Flux.generate`

```java
// Synchronous
Flux<String> flux = Flux.generate(
  () -> 0, // initial state
  (state, sink) -> {
    sink.next("3 x " + state + " = " + 3*state); // what to emit(sink)
    if (state == 10) sink.complete(); // when to stop
    return state + 1; // return new state
  },
  (state) -> System.out.println("state: " + state)); // state: 11 (last state value), close db connection과 같은 행동 하면 좋은 장소
```

publisher의 프로그래밍 방식 생성 예시: `Flux.create`

```java
Flux <String> bridge = Flux.create(sink -> {
  myEventProcessor.register(
    new MyEventListener<String>() {
      public void onDataChunk(List<String> chunk) {
        for (String s : chunk) {
          sink.next(s);
        }
      }

      public void processComplete() {
        sink.complete();
      }
    }
  );
});
```

publisher의 프로그래밍 방식 생성 예시: `Flux.push`

```java
Flux<String> bridge = Flux.push(sink -> {
    myEventProcessor.register(
      new SingleThreadEventListener<String>() {

        public void onDataChunk(List<String> chunk) {
          for(String s : chunk) {
            sink.next(s);
          }
        }

        public void processComplete() {
            sink.complete();
        }

        public void processError(Throwable e) {
            sink.error(e);
        }
    });
});
```

- 개요
  - Publisher인 `Flux`, `Mono`를 프로그래밍 방식으로 관련 이벤트인 `onNext`, `onError`, `onComplete`를 정의해서 생성하기
    - sink event를 트리거링 하기 위한 메서드들
- sink의 종류
  - `Flux.generate`
    - 동기 + 싱글스레딩
  - `Flux.create`
    - 비동기 + 멀티스레딩
      - 멀티스레드로부터 매 round마다 다수의 emission 가능
      - OverflowStrategy로 비동기 API들을 bridge할 수 있고, backpressure를 제어 가능
        - IGNORE
          - backpressure를 무시함
        - ERROR
          - downstream이 처리를 못하면, IllegalStateException 에러를 시그널링함
        - DROP
          - downstream이 처리를 못하면, 들어오는 시그널을 드랍함
        - LATEST
          - *downstream이 upstream으로부터 최신 시그널만 받도록 함*
        - BUFFER(default)
          - downstream이 처리를 못하면, 버퍼링함
          - OutOfMemoryError가 생길 위험 존재
  - `Flux.push`
    - 비동기 + 싱글스레딩
      - create와 유사하나, 하나의 producing thread만 next, complete, error를 호출 가능
