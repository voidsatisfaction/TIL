# Reactor

- 의문
- 1] Reactive Programming의 소개
  - 1.2 Asynchronicity to the Rescue?
- 2] Reactive Streams의 특징

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
