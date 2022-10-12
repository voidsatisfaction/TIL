# Redux

- 의문
- 리덕스의 3가지 원칙
- 구성 요소
- 데이터 흐름
- 미들웨어
- 리듀서 설계

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

## 미들웨어

액션을 dispatch할 경우 로깅하는 케이스를 생각

### 1. 직접 로깅하기

코드에 직접 로깅함

```js
let action = addTodo('Use Redux');

console.log('dispatching', action);
store.dispatch(action);
console.log('next state', store.getState());
```

### 2. 디스패치 감싸기

```js
function dispatchAndLog(store, action) {
  console.log('dispatching', action);
  store.dispatch(action);
  console.log('next state', store.getState());
}

dispatchAndLog(store, addTodo('Use Redux'));
```

### 3. 디스패치 몽키패칭하기

- 스토어 인스턴스에 있는 dispatch 함수를 대체

```js
function patchStoreToAddLogging(store) {
  let next = store.dispatch;
  store.dispatch = function dispatchAndLog(action) {
    console.log('dispatching', action);
    let result = next(action);
    console.log('next state', store.getState());
    return result;
  };
}

function patchStoreToAddCrashReporting(store) {
  let next = store.dispatch;
  store.dispatch = function dispatchAndReportErrors(action) {
    try {
      return next(action);
    } catch (err) {
      console.error('Caught an exception!', err);
      Raven.captureException(err, {
        extra: {
          action,
          state: store.getState()
        }
      });
      throw err;
    }
  };
}

patchStoreToAddLogging(store);
patchStoreToAddCrashReporting(store);
```

- 문제
  - dispatch에 이런 변환을 두 개 이상 적용할 수 있으나 깔끔하지 않음

### 4. 몽키패칭 숨기기

- `dispatch` 함수를 반환

```js
function logger(store) {
  // **여기서 next는 store를 갱신할 때 마다 새로 바뀌는가? 아니면 클로저 환경에서 고정되는가?**
  // ****클로저 환경에서 고정됨(함수는 값?? 왜지?)****
  let next = store.dispatch;

  // 앞에서:
  // store.dispatch = function dispatchAndLog(action) {

  return function dispatchAndLog(action) {
    console.log('dispatching', action);
    let result = next(action);
    console.log('next state', store.getState());
    return result;
  };
}

function applyMiddlewareByMonkeypatching(store, middlewares) {
  middlewares = middlewares.slice();
  middlewares.reverse();

  // 각각의 미들웨어로 디스패치 함수를 변환합니다.
  middlewares.forEach(middleware =>
    store.dispatch = middleware(store)
  );
}
```

- 문제
  - 아직까지도 몽키패칭

### 5. 몽키패칭 제거하기 & 미들웨어 사용하기

- 위와의 차이
  - 디스패치 함수를 `store` 인스턴스에서 읽어오는 대신, 매개변수로 받을 수 있음

```js
const thunk = store => next => action =>
  typeof action === 'function' ?
    // 함수를 받을 경우, 다른 미들웨어 적용이 없이 그냥 여기서 마무리
    // 함수 내부의 dispatch의 경우에는 promise가 다 resolve되고 나서 다시 처음부터 middleware chain을 호출
    // 그러므로 동기적인 동작 보장
    action(store.dispatch, store.getState) :
    next(action);

const logger = store => next => action => {
  console.log('dispatching', action);
  let result = next(action);
  console.log('next state', store.getState());
  return result;
};

// next() 디스패치 함수를 받아서, 디스패치 함수를 반환하고, 이는 다시 왼쪽의 미들웨어에 next()로 전달
// 스토어의 getState()와 같은 메서드에 접근할 수 있으면 유용하므로, store는 최상위 인수로 남아있음
const crashReporter = store => next => action => {
  try {
    return next(action);
  } catch(err) {
    console.error('Caught an exception!', err);
    Raven.captureException(err, {
      extra: {
        action,
        state: store.getState()
      }
    });
    throw err;
  }
};

// 실제 구현과 차이가 있음
// 실제 구현에서는
// 1. store API의 일부만을 미들웨어에 노출 - dispatch, getState 함수
// 2. next(action)대신 store.dispatch(action)를 호출할 경우 액션이 현재 미들웨어를 포함한 전체 미들웨어 체인을 다시 따라가도록 함(비동기 미들웨어에서 유용)
// 3. 미들웨어를 한번만 적용하도록 하기 위해, createStore()상에서 작동하도록 함. 그래서 (...middlewares) => (createStore) => createStore
const applyMiddleware = (store, middlewares) {
  middlewares = middlewares.slice();
  middlewares.reverse();

  let dispatch = store.dispatch;
  middlewares.forEach(middleware =>
    // dispatch를 덮어쓰면서 동작
    dispatch = middleware(store)(dispatch)
  );
  store.dispatch = dispatch
}

// 미들웨어 적용은 위에서 아래 순서대로
// 즉, logger나 thunk에서 에러가 나는경우, crashReporter를 가장 위로 배치해야지 Reporter가 에러를 catch할 수 있음

// dispatch이후 lifecycle: crashReporter -> logger -> thunk
let createStoreWithMiddleware = applyMiddleware(
  crashReporter,
  logger,
  thunk,
)(createStore);
let todoApp = combineReducers(reducers);
let store = createStoreWithMiddleware(todoApp);
```

## [WIP](https://deminoth.github.io/redux/recipes/reducers/SplittingReducerLogic.html) 리듀서 설계

전형적인 앱 상태의 형태

```js
{
  domainData1 : {},
  domainData2 : {},
  appState1 : {},
  appState2 : {},
  ui : {
    uiState1 : {},
    uiState2 : {},
  }
}
```

- 애플리케이션의 데이터종류
  - Domain data
    - 애플리케이션으로 보여주거나 사용, 수정할 데이터
  - App state
    - 애플리케이션의 동착을 위한 특정 데이터
    - 예시
      - "현재 Todo #5가 선택됨", "Todos를 가져오는 요청이 있습니다"와 같은 것들
  - UI state
    - 현재 UI가 어떻게 보일 것인가에 대한 데이터
    - 예시
      - EditTodo Modal 상자가 현재 열려있음 과 같은 것들
- 상태는 UI 컴포넌트가 아닌, 도메인데이터와 앱의 상태에 따라 구성해야 함
