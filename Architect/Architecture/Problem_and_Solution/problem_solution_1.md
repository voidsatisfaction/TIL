# 문제와 해결

실제 코드를 작성하거나 설계할 때에 나타난 문제를 알아보고 어떻게 해결했는지 적는 코너

## 목차

- DDD / Scala편
  - Scala로 구현한 DDD기반 애플리케이션에서, 애플리케이션 층을 구현할 때, 애플리케이션 층의 에러와 도메인층의 에러가 나타나는 경우, 어떻게 해야하는가?
- JS / TS편
  - js에서 null체크 if중첩의문제 해결?

## DDD Scala 편

### Problem1: Scala로 구현한 DDD기반 애플리케이션에서, 애플리케이션 층을 구현할 때, 애플리케이션 층의 에러와 도메인층의 에러가 나타나는 경우, 어떻게 해야하는가?

다음과 같은 코드를 보자.

```scala
import my.application.error.NotFound

trait MyAppComponent {
  self: my.domain.super.LoaderComponent
      with my.domain.user.ActionComponent
      with ...
      with ...

  def myApplication(): MyApplication = MyApplication

  class MyApplication {
    def someMethod(): Either[whatError, Unit] = {
      user = ...
      for {
        sth <- Loader.find().toRight(NotFound).right // 이 코드의 에러는 애플리케이션 층에서 정의됨
        sth2 <- user.EditSth() // 이 코드는 이미 에러 처리가 도메인에서 되어있음. 즉, 에러 자체도 도메인에서 타입이 정의됨
      } yield {
        ...
      }
    }
  }
}
```

- 위와 같은 코드의 경우, `MyAppComponent`의 `MyApplication`의 `someMethod`의 Either속의 whatError의 타입을 정하기가 난감하다.
- 내가 이 문제를 해결한 방식은 다음과 같다
  - 도메인 층의 에러를 애플리케이션 층으로 끄집어 내는것은 불합리적이므로, 애플리케이션 층의 에러를 도메인층으로 내려보낸다.
  - 즉, `NotFound`라는 에러를 도메인 층에서 정의하여, `whatError`역시 도메인 층에서 정의하는 것으로 타입의 레이어를 맞춰준다.
- 하테나의 타라오씨(부서의 리드 엔지니어)는 application층과 domain층 둘다 같은 에러를 정의하는 것을 추천하셨다.
  - 이름은 같아도 레이어에 따라서 의미가 다를 수 있기 때문에
  - 원래 DDD는 레이어 사이의 데이터 타입의 차이를 밸런스 있게 잘 조정해야 한다.
    - Domain층의 Entity를 단순히 application에서 사용하기 보다는 또 다른 application층 에서 다루기 쉬운 case class를 정의하여 만들어서 사용한다던지
  - 결국 레이어나 컴포넌트 사이의 의존관계가 더러워지지 않는 선에서 관리하는 것이 중요

## JS / TS편

### Problem1: js에서 null체크 if중첩의문제 해결?

- 배경
  - 자기자신이 작성하는 코드가 아니라 라이브러리나 애플리케이션을 사용하여 외부에 피치못할 의존성이 생기는 경우
  - JS나 Python과 같이 타입 안전성을 보장하기 힘든 언어의 경우
- 문제
  - if문이 엄청나게 중복 될 수 있음 왜냐하면 null 체크를 일일이 다 해줘야 하니까.

해결 방법은 `if문을 엄청나게 꼼꼼하게 써서 잘 한다`외에도 다음 방법이 존재한다. 결국, scala에서의 for comprehension과 Option타입과 비슷한 방식으로 해결이 가능하면 최상의 결과라고 생각하기 때문에 다음과 같은 방법이 현재로서는 좋아보인다.

```ts
s: string? = ...
if (s === null) return;
s.split(" ")

try {
  s: string? = ...
  if (s === null) throw `error!!!!`; // 직접 명시적으로 null체크를 해주면 이 뒤에서는 s가 반드시 문자열이라는 것을 보장
  s.split(" ")
} catch {
  ...
}
```
