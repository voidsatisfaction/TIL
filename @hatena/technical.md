# 하테나에서 근무하면서 깨달은 기술적인 사실

- 상태와 무상태성
- 1차원 추상화, 2차원 추상화, 다차원 추상화
- 프록시
- 반드시 공부하자 리스트
- 어떠한 레이어에 어떠한 처리를 할 지 생각하라
- 메서드나 변수의 이름은 알기 쉽게 해놓자. 너무 길게는 말고
- DDD를 팀 내에 도입하는 것은 엔지니어가 충분히 공부를 해야 한다는 코스트가 생기게 되는데 어떻게 대처할 것인가?
- 스칼라의 타입 엘리어스
- 마이크로 서비스의 단점
- 수직적 구성 / 수평적 구성
- 함수형 프로그래밍과 불변성과 효율
- 에러에 대한 마음가짐2
- 타입을 이용한 추상화를 잘 하는 방법은 무엇인가?

## 상태와 무상태성(state, stateless)

Go언어나 여타 오브젝트지향 언어로 프로그래밍을 하다보면, 디자인 패턴으로 `constructor`패턴을 많이 사용하게 됨. 그러나 정말 `constructor`패턴이 필요한가?에 대한 의문을 갖을 필요가 있음.

`constructor`패턴을 사용해서 인스턴스를 초기화 한다는 것의 의미 중 하나는, 그 인스턴스가 **상태** 를 갖는 것과 동등한 말이다. 즉, 상태가 필요 없는 행위(데이터 베이스에서 단순히 값을 가져옴, 외부 서버에 리소스 요청 등)를 할 때에는 굳이 상태를 갖을 필요가 없으며, 오히려 상태를 갖음으로 인해서 프로그래밍의 복잡도를 증가시킬 수 있다.

예를들면 데이터 베이스나 다른 API서버에서 데이터를 갖고오는 행위는 단순히 데이터만 갖고 오기 때문에 상태가 굳이 필요하지 않다.

사실 컴퓨터과학에서의 논리게이트에도 상태와 무상태성을 구분된다. 플립 플롭이나 레지스터는 상태를 갖는 순차 논리이다. 하지만, 단순 논리 연산 `OR AND NAND`혹은 `ALU`등은 상태를 갖지 않는 조합 논리이다. 이는 또, 오토마톤과 튜링머신으로 이야기가 이어지는데 이는 나중에 공부해보고 싶은 테마이기도 하다.

함수형 프로그래밍은 상태를 되도록 적게 가지려는 프로그래밍 패러다임이라고 할 수 있다. 함수형 프로그래밍은 상태를 적게 갖기 때문에 순수함수적 성격(부작용이 없음)을 띄고 있으며, 테스트하기 쉬운 특징이 있다.

## 1차원 추상화, 2차원 추상화, 다차원 추상화

- MVC프레임웍의 추상화와 nand-to-tetris의 추상화의 차이
  - nand-to-tetris에 있어서의 추상화는 일차원적임.
    - 고수준 언어 => 바이트 코드 => 어셈블리어 => 기계어 => CPU/Memory => Register => 논리게이트
  - MVC프레임웍 같은 경우는 컨트롤러가 모델 덩어리(내부는 추상화 되어있음)와 뷰 덩어리(내부는 추상화 되어있음)를 중제해주는 역할이다.
    - 컨트롤러 => 부모뷰 => 자식뷰 => 자식뷰 ...
    - 컨트롤러 => 모델(외부서버?) => ...
- 컴퓨터 과학의 거의 대부분의 복잡도 문제는 레이어를 하나 더 추가하는 것으로 해결 가능하다.
- Small is Beautiful
- Make program one thing well
- **Unix사상!!**

## 프록시

- 하테나와 프록시
  - 포워드 프록시
    - 요청을 보내는 쪽에서 모든 응답에 대해서 결과를 캐시해두는 프록시
  - 리버스 프록시
    - 요청을 받는 쪽에서 자신에 대한 요청으로 부터의 특정 응답의 결과를 캐시해두는 프록시
  - 프록시는 캐시의 기능으로 많이 사용 / 아이피 세탁
  - 프록시 서버는 리퀘스트데이터를 보존하고 그 리퀘스트 데이터에 매칭하는 리스폰스를 캐시해서 돌려줌(심볼 테이블 같은 느낌)

## 반드시 공부하자 리스트

하테나 코드의 어디를 봐도 항상 있는 두 친구들이 있다.

- 정규 표현식(regex)
  - [생활코딩 - 정규표현식](https://opentutorials.org/course/909/5142)
- 쉘 스크립트(shell script)

정말 진짜 너무나도 유용한 친구들이지만 너무나도 잘 모르는 친구들인데 꼭 시간내서 공부하는게 좋을 것 같다. 주말에 부트캠프처럼 공부하는 것도!

## 어떠한 레이어에 어떠한 처리를 할지 생각하자

- 결국 레이어를 나누는 것은 책임을 분담하는 것
- 하나의 레이어가 여러가지 책임을 갖고 있으면 관리하기 어려움

## 메서드나 변수의 이름은 알기 쉽게 해놓자. 너무 길게는 말고

- 김춘수 시인의 시 **꽃**

## DDD를 팀 내에 도입하는 것은 엔지니어가 충분히 공부를 해야 한다는 코스트가 생기게 되는데 어떻게 대처할 것인가?

- **일단, 팀원이 DDD를 도입하지 않은 아닌 애플리케이션에서 고생을 해서 괴로움을 공감하게 되면 DDD의 고마움을 알게되고 잘 받아들이게 된다.**
- 테크리드로서, DDD와 아키텍처에 관한 내용을 문서화 해서 다같이 공부할 수 있도록 한다.
- DDD의 사상이 팀 전체에 퍼지도록 한다.

## 스칼라의 타입 엘리어스

스칼라에는 타입 엘리어스가 존재한다. 이 타입 엘리어스는 golang의 `type`키워드와 비슷하다.

```scala
type UserId = Long
type EntryId = Long
```

## 마이크로서비스의 단점

- 역할을 제대로 분담하지 않으면, 특정한 곳에서 에러가 나도, 어느 컴포넌트가 에러의 원인이 되는지 알기 힘듬
- 반대로 얘기하면 역할을 제대로 분담 한다면 괜찮다는 이야기다.

## 수직적 구성 / 수평적 구성

- 수직적 구성
  - 상속으로 인한 추상화
  - structural subtyping
- 수평적 구성
  - composition으로 인한 추상화
  - nominal subtyping

## 함수형 프로그래밍과 불변성(immutability)과 효율

- 함수형 프로그래밍을 할 때, 불변성을 유지하기 위해서 오브젝트를 항상 새로 생성하고 없애고 하는데 이는 시간적 / 공간적 성능상 오버헤드를 야기하지 않는가?
  - 스칼라 컴파일러가 내부를 최적화 함. 캡슐화를 이용해서 내부에서는 `var`같은 상태를 갖는 변수도 많이 씀
  - **[공부를 위해서는 스칼라 코드 자체를 봐 보자](https://github.com/scala/scala/blob/2.13.x/src/library/scala/collection/immutable/List.scala)**
  - 또한, Purely Functional DataStructure이라는 책을 참조해보자

## 에러에 대한 마음가짐2

오늘(2018.10.19) 배치 스크립트(데이터 이행)를 실행하는데에, 다음과 같은 에러가 일어났다.

`SSL 관련 모듈이 존재하지 않음`

어라, 왜 이런 에러가 일어나지 해서 일단은 클라이언트 쪽 코드를 보게 되었다. 그런데 전혀 문제가 없었다.

그 다음은 서버쪽 코드를 보게 되었는데, 리퀘스트에서 받아야한다고 기대한 모든 데이터를 받고 있는 것을 확인했다.

그런데 알고보니까, 서버쪽에서 "당연히 베포판이라고 전제했던" 어떤 데이터베이스가 베포판이 아니었다. 그것도 모르고 계속 print해가면서 내용을 확인했었다. 그리고 다른데이터베이스를 참조하고 있었으므로, 리퀘스트가 리다이렉트 되어서(http에서 https로) 로컬에서 https를 다루는 모듈이 없어서 그러한 에러가 나타났었던 것이었다. 한 번에 두개의 에러가 겹쳐져서 정말 멘붕이었는데 모두 해결이 되어서 마음이 엄청 시원했다.

전에도 이와 같은 에러에 대해서 글을 쓴 적이 있었던거 같은데 결국 이번에도 같은 결론에 도달했다.

프로그램은 거짓말을 하지 않는다

그러니까 **하나하나 천천히 로직을 확인하면서 진행** 하는 것이 중요하다. (여기서 디버거를 사용할 수 있다면 더 알기 쉬울 수 있겠다)

그리고 또 하나 더 느낀 것은, **기초 지식이 정말 중요** 하다는 점이다.

사실, 에러 메시지는 단순히 생각하면 https를 다룰 모듈이 프로그램 내부에 존재하지 않아요 라는 뜻인데, 그걸 제대로 해석하지 못했다. 기초지식은 정말정말 중요하다. 그리고 이렇게 직접 부딪히고 난 뒤에 공부하면 흡수력도 남다르고 재미있기도 하다.

## 타입을 이용한 추상화를 잘 하는 방법은 무엇인가?

- 사실 차근차근 생각해보면 어렵지 않음
- 표준 라이브러리를 뜯어보면 매우 좋은 공부가 된다.
- 다음 코드는 두 Seq의 join을 추상화 한 예시

```scala
// 사용 예시
val (titleEntities, titleLogsWithCreated) = immigrationEntryTitles
  .join(locations).on(_.url, _.url)
  .join(users).on(_._1.accountId, _.accountId) // case ((entryTitles, locations), users)

// implicit

def join[B](other: Iterable[B]): Join.Inner[A, B, It] =
  new Join.Inner(it, other)

// join 내부 구조
package types
package collection
package relation

import scala.collection.{breakOut, IterableLike}
import scala.collection.generic.CanBuildFrom
import scala.language.{higherKinds, implicitConversions}

/** A class to describe a join of two sequences. */
case class Join[A, B, K, It[X] <: IterableLike[X, It[X]]](
  left: It[A],
  right: Iterable[B],
  leftKey: A => K,
  rightKey: B => K,
  default: K => Option[B]
) {
  private type R = (A, B)

  private def applyTo[It2[X] <: IterableLike[X, It2[X]], R2, That](
    f: R => R2,
    s: It2[A]
  )(implicit bf: CanBuildFrom[It2[A], R2, That]): That = {
    val m = {
      val m: Map[K, Option[B]] =
        right.map(x => rightKey(x) -> Some(x))(breakOut)
      m.withDefault(default)
    }
    s.flatMap(x => m(leftKey(x)).map(y => f((x, y))))
  }

  def into[R2](f: R => R2)(implicit
    bf: CanBuildFrom[It[A], R2, It[R2]]
  ): It[R2] = applyTo(f, left)

  def result(implicit bf: CanBuildFrom[It[A], R, It[R]]): It[R] =
    applyTo(identity, left)

  def toStream: Stream[R] = applyTo(identity, left.toStream)(breakOut)
}
object Join {
  class Inner[A, B, It[X] <: IterableLike[X, It[X]]](
    left: It[A],
    right: Iterable[B]
  ) {
    def on[K](
      leftKey: A => K,
      rightKey: B => K
    ): Join[A, B, K, It] = Join(left, right, leftKey, rightKey, _ => None)
  }

  class Left[A, B, It[X] <: IterableLike[X, It[X]]](
    left: It[A],
    right: Iterable[B]
  ) {
    def on[K](
      leftKey: A => K,
      rightKey: B => K
    ): Left.On[A, B, K, It] = Left.On(left, right, leftKey, rightKey)
  }
  object Left {
    case class On[A, B, K, It[X] <: IterableLike[X, It[X]]](
      left: It[A],
      right: Iterable[B],
      leftKey: A => K,
      rightKey: B => K
    ) {
      private def toJoin(default: K => Option[B]): Join[A, B, K, It] =
        Join(left, right, leftKey, rightKey, default)

      def apply(default: B): Join[A, B, K, It] =
        toJoin(_ => Some(default))

      def apply(default: K => B): Join[A, B, K, It] =
        toJoin(x => Some(default(x)))
    }
  }

  implicit def toStream[A, B, K, It[X] <: IterableLike[X, It[X]], Col](
    join: Join[A, B, K, It]
  ): Stream[(A, B)] = join.toStream
}
```
