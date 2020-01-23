# Redux

- 의문
- 리덕스의 3가지 원칙
- 구성 요소
- 데이터 흐름

## 의문

## 리덕스의 3가지 원칙

- ① 진실은 하나의 소스로부터
  - 애플리케이션의 모든 상태는 하나의 스토어 안에 하나의 객체 트리 구조로 저장
- ② 상태는 읽기 전용
  - 상태를 변화시키는 유일한 방법은 무슨 일이 벌어지는 지를 묘사하는 액션 객체를 전달하는 방법 뿐
    - 액션은 그저 평범한 객체
- ③ 변화는 순수 함수로 작성되어야 함
  - 액션에 의해 상태 트리가 어떻게 변화하는 지를 지정하기 위해 프로그래머는 순수 리듀서를 작성해야 함

## 구성 요소

- 액션
  - 무엇이 일어날지를 나타냄
  - 형태
    - plain object
      - `{ type: ~~, parameter1: ..., paramters2: ... }`
- 리듀서
  - 해당 액션에 따라서 상태를 수정
  - 형태
    - 순수함수
      - `function todoApp(prevState = initialState, action) { switch(action.type) case ... }`
- 스토어
  - 애플리케이션 상태 저장
  - `getState()`를 통하여 상태에 접근 가능
  - `dispatch(action)`을 통하여 상태를 수정할 수 있게 함
  - `subscribe(listener)`리스너 등록

## 데이터 흐름

- 4단계의 생명주기
  - ① `store.dispatch(action)`를 호출
    - `{ type: 'LIKE_ARTICLE', articleId: 42 }`
    - `{ type: 'FETCH_USER_SUCCESS', response: { id: 3, name: 'Megan' } }`
  - ② Redux 스토어가 우리가 지정한 리듀서 함수들을 호출
    - 스토어는 (combined) 리듀서에 현재 상태 트리와 액션 두 가지 인수를 넘김
      - `let nextState = todoApp(prevState, action)`
  - ③ 루트 리듀서가 각 리듀서의 출력을 합쳐서 하나의 상태 트리로 만듬
    - redux는 루트 리듀서를 각각이 상태 트리의 가지 하나씩을 다루는 함수들로 나눌 수 있도록 `combineReducers()`핼퍼 함수를 제공
    - `combineReducers()`의 동작 방식
      - `let todoApp = combineReducers({ todo, visibleTodoFilter })`
      - 액션을 dispatch하면 `combineReducers`가 반환한 `todoApp`은 두 리듀서를 모두 호출
        - `let nextTodos = todos(state.todo, action)`
        - `let nextVisibleTodoFilter = visibleTodoFilter(state.visibleTodoFilter, action)`
      - 두 결과를 합쳐서 하나의 상태 트리로 만듬
        - `return { todos: nextTodos, visibleTodoFilter: nextVisibleTodoFilter }`
  - ④ Redux 스토어가 루트 리듀서에 의해 반환된 상태 트리를 저장
    - 이 새 트리가 앱의 다음 상태가 됨
    - `store.subscribe(listener)`를 통해 등록된 모든 리스너가 불러내지고, 이들은 현재 상태를 얻기 위해 `store.getState()`를 호출
    - 새로운 상태를 반영하여 UI가 변경
      - react redux로 바인딩을 했을 경우, 이 시점에 `component.setState(newState)`가 호출됨
