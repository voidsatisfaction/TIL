---
layout: post
title: 리덕스(Redux)란 무엇인가?
categories:
  - JavaScript
  - React Native
tags:
  - Redux
---

## 참조

- 인턴 멘토 森田(모리타)씨와의 대화
- [Redux - motivation](http://redux.js.org/docs/introduction/Motivation.html)

## 핵심

리덕스는 어플리케이션의 클라이언트쪽 `state`를 관리하기 위한 거대한 이벤트루프이다.
액션 = 이벤트
리듀서 = 이벤트에 대한 반응

## Redux의 이해

리액트를 사용하는 프로그래머 입장에서는 누구나가 거쳐가는 바로 그 기술 Redux.
처음 리액트를 공부하는 사람들에게 크나큰 산과 같은 Redux는 과연 무엇일까?

### Redux의 동기

Redux공식 문서(참조)에 의하면 리덕스는 클라이언트 앱의 복잡성을 제어하기 위한 하나의 state제어 수단이라고 한다(정확히는 방법론이 맞는것 같다.)

Redux를 제안하고 개발한 Dan Abramov는 클라이언트앱의 복잡성을 증가시키는게 `Mutation`과 `Asynchronicity`라며 그 둘을 멘토스와 콜라와 같다고 한다.
`Mutation`과 `Asynchronicity`는 각각 존재할때에는 대단한 것임에 틀림없지만 같이 존재할때 크나큰 복잡성을 유도한다는 것이다.

여기서 Redux는 Mutation, 즉 클라이언트의 종합적인 State를 관리하기 위한 아키텍쳐 방법론인 것이다.

여기까지 읽은 몇몇의 독자는 "그럼 Asynchronicity는 어떻게 된건가요?"라고 의문을 갖을 수 있겠지만 간단히 얘기하자면 Redux에 Middleware를 장착하는 것으로
복잡한 비동기적인 Api처리, Action처리를 한다. 이는 나중에 후술하겠다.

### Redux의 원리

Redux의 원리는 생각보다 크게 어렵지 않다.

어플리케이션 전체에는 store라는 커다란 **하나의** state가 존재하는데 이것이 어플리케이션의 state를 총괄한다.

이 store의 state는 그 자체를 직접 변형할 수 없고, 오직 **순수 함수**인 리듀서로만 새로운 형태로 갈아치우는 것이 가능하다.

리듀서는 type과 payloads(꼭 속성이름이 이렇지 않아도 됨)를 속성으로 갖는 **단순 객체인** `action`이벤트가 발생했을 때에만 작동하며

`action`이벤트를 발생시키는 방법은 dispatch라는 함수에 단순 객체인 action을 넣는것으로 가능하게 한다.

이제 앞서 말했던 순서를 시간순으로 정리해보자.

dispatch(action) => 리듀서 작동 => store의 state변경 => 변경된 state가 state를 subscribe하고 있는 컴포넌트에 전달

이게 다다.

이렇게 application전체의 상태를 redux로 관리하면 어떤 장점이 있을까?

가장 먼저, application state의 변화가 예측가능하게 변한다는 점이다.

이는 특정 액션이벤트 발생에만 reducer가 작동하게 했기때문에 store state가 변한경우 그것이 정확히 `어떠한 액션 이벤트로 부터`변경된 것인지 알 수 있다.

또한, 정확히 어떤 액션 이벤트로 부터 변경된 것인지 알기 때문에 `Time travel debugging`이 가능해진다. 간단하게 얘기하자면 이제까지 store state가 변화해온 과정을 마치 뒤로가기 버튼이 있는것 처럼 하나하나 확인해볼 수 있는 것이다.

그리고, 리듀서가 **순수 함수**(외부에 영향을 끼치지 않는 함수. ex: api calling이 없는 함수)이기 때문에 test코드를 짤 수 있다는 장점도 존재한다.

마지막으로 선언적으로 프로그래밍을 할 수 있다는 점이다(Declarative Programming)

(물론 더 있을거라고 생각한다.)

### Redux와 Middleware

여기서 과연 우리는 클라이언트의 문제를 전부 해결했다고 할 수 있을까?

아까 멘토스가 `Mutation`이라고 했는데 이것은 state에 관한 문제이므로 redux로 어느정도 해결했다고 볼 수 있겠지만

콜라인 `Asynchronicity`는 어떻게 해결할까?

아까 설명한 단순한 Redux의 모델

dispatch(action) => 리듀서 작동 => store의 state변경 => 변경된 state가 state를 subscribe하고 있는 컴포넌트에 전달

은 action이 **단순 객체**이기 때문에 다음과 같은 행동이 불가능하다.

1. 로그인 요청을 보내며 로딩중이라는 표시를 뜨게 하기
2. 회원가입 요청을 보내는데에 만약 이미 있는 id라면 에러 메세지를 보내고 아니라면 성공시킨다.

action이 **단순 객체**라는 얘기는 조건 분기나 다른 action 이벤트를 생성할 수 없기 떄문에 우리는 `action creator`라는 action을 생성하는 **함수**를 생성한다.

action creator는 함수이기 때문에 Promise나 Callback을 적절히 조화하는 것으로 다른 action 이벤트를 생성할 수 있고, 조건 분기도 가능해진다.
사실 이름만 action creator이지 action자체를 반환하지 않아도 된다.

하지만 이 역시 그냥 맨땅에 하려면 `dispatch`를 일일이 불러와야하는 귀찮음이 생기므로 우리는 middleware로서 `redux thunk`등을 사용하는 것이다.

여기에 등장하는 `redux thunk`는 함수를 반환하는 함수인데 dispatch를 가지고 함수를 warpping하고 있으므로 일일이 dispatch를 불러와야하는 귀찮음이 경감된다.

사실 미들웨어에는 `redux thunk`이외에도 `redux saga`등등이 있으니 참고 바란다.

## 리덕스의 정체

사실 이제부터가 진짜 이야기의 시작이다.

결론부터 얘기하자면 **redux는 state관리를 위한 거대한 event loop**였던 것이다!

액션 = 이벤트
리듀서 = 이벤트에 대한 반응

즉, 액션이벤트를 발생시켜서 리듀서라는 이벤트에 대한 반응을 일으키므로서 어플리케이션의 state를 a라는 상태에서 b라는 상태로 만든다.(a is b)

이렇게 이해하면 redux는 더이상 redux monster나 뭐가뭔지 모르지만 좋다니까 그냥 쓰는 녀석에서,

우리에게 아주 친숙한 `event loop`로 바뀌는 것이다.

실제로 Dan Abramov는 공식 tutorial문서에서 이렇게 얘기하고 있다.

> Following in the steps of Flux, CQRS, and **Event Sourcing**, Redux attempts to make state mutations predictable by imposing certain restrictions on how and when updates can happen. These restrictions are reflected in the three principles of Redux.

그러니까 앞서 말한 이벤트 기반의 프로그래밍론이 redux에 사상적으로 들어가 있는 것이다.

나는 처음 tutorial을 읽었을때 전혀 눈치를 채지 못하고 있었는데 오늘 인턴의 멘토인 森田(모리타)씨가 나와 점심을 먹으며 나에게 해주신 말씀이다.

그때까지는 그냥 그렇게 무미건조하게 써왔던 redux가 내게 의미를 갖는 순간이었다.

감사합니다 모리타씨!

