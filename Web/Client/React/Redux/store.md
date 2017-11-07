# Store

- Actions: 무엇이 일어났는가 묘사
- Reducers: 액션에 있는 묘사에 따른 state 업데이트

## Store
1. 어플리케이션 state를 담음
2. state에의 접근 허가 `getState()`
3. state가 업데이트 되도록 허가 `dispatch(action)`
4. listeners를 기록 `subscribe(listener)`
5. listeners를 함수를 이용해서 기록하지 않음 `unsubscribe()`

## Store초기화

```js

import { createStore } from 'redux'
import todoApp from './reducers' // combineReducers(함수)를 가져옴
let store = createStore(todoApp) // 그 함수를 넣어서 Store를 작성

let store = createStore(todoApp, window.STATE_FROM_SERVER) // 클라이언트와 서버의 state를 동기화 시켜줄 수 있다.
```