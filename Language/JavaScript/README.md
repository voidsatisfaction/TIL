# JavaScript기초

## 프론트엔드 아키텍처

### MVC

- 모델
  - 컬렉터를 생성(데이터를 담는 그릇)
    - 컬렉터가 push, forEach메서드를 오버라이드
    - push메서드가 발동되면 데이터 추가 후 view에 이벤트 던져줌(데이터의 변화)
  - state를 여기서 관리
- 뷰
  - 컨트롤러에 유저의 이벤트를 송신
  - 모델의 변화에 따른 이벤트를 수신해서 `render`함수를 자체적으로 실행
- 컨트롤러
  - 모델과 뷰를 연결
  - 컬렉터 데이터와 뷰를 둘다 관리(직접적으로 각각의 메서드가 실행되는 곳은 여기)
- 이벤트의 관리가 굉장히 중요하게 됨.
  - 그래서 대부분 프레임워크 사용

### MVP

- 모델
  - 단순히 넘겨주는 데이터의 타입을 정해줌(entity class역할)
- 프레젠터(Presenter)
  - 데이터 초기화, 뷰에서의 이벤트 감지
  - 뷰에서 넘어오는 이벤트와 데이터를 받고, 받은 이벤트를 기반으로  뷰를 갱신
  - 뷰의 `render`함수를 프레젠터가 실행
  - 애플리케이션의 state를 관리하는 주체

- 프론트엔드에서의 모델
  - entity class
  - 서버와의 api

## this

- 런타임에 정해짐
- this를 래핑한 함수를 실행하는 리시버(receiver, 즉 오브젝트)라고 생각하면 됨
  - 결국 **어떤 오브젝트가 this를 포함하는 함수를 실행**하느냐가 중요
  - 그러한 명시적인 오브젝트가 없으면 글로벌 객체가 해당
- 애로우 함수는 정의할때 this의 스코프를, 정의하는 범위에서의 this로 고정함
- bind 역시 this의 스코프를 bind함수를 실행할떄의 범위에서의 this로 고정함
- call, apply는 함수를 호출하면서 this를 동적으로 고정하는 방법

```js
// call, apply, bind를 이용한 this의 고정
var nodes = document.querySelectorAll('div');

// nodes에는 slice라는 메소드가 없으므로 배열 오브젝트의 slice메소드를 this만 변환 시켜서 사용
// call과 apply는 this를 변환시켜서 실행
[].slice.call(nodes, 0, 3);
[].slice.apply(nodes, [0, 3]);

// bind를 사용
var sliceNodes = [].slice.bind(nodes);
sliceNodes(0, 3);
```

## page가 바뀌면 `addEventListener`로 등록한 이벤트들은 어떻게 되는가?

- 이벤트들은 사라짐
- 그러나 SPA는 새로고침이 없으므로 수동으로 이벤트를 없애줘야함
