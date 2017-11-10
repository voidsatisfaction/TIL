# Redux-thunk란 무엇일까?

## 참조

- [Redux-thunk github](https://github.com/gaearon/redux-thunk)
- [함수형 프로그래밍의 장점](http://changsuk.me/?p=1916)

## 배경

프론트엔드를 개발하는 사람이라면 클라이언트 사이드의 규모가 커지면 커질 수록 state와 api와 같은 asynch처리의 관리가 힘들어지는 것을 느낄 것이다.

보통 React개발자는 state관리를 위해서 redux를 채용한다.

그렇다면 복잡한 로직의 Redux내의 api나 조건부 `dispatch(action)`은 어떻게 해결해야 할까?

이에 대한 해결책중의 하나로 나온 것이 바로 **Redux-thunk** 이다.

## 내용

### 1. thunk란 무엇일까?

thunk는 식(expression)을 지연평가(lazy evaluation)하기 위한 wrapper function이다.
이는 함수형 프로그래밍의 특징이다.
(함수가 first class citizen이기 때문)

```js
// ex

let x = 1 + 2; // x === 3

let foo = () => 1 + 2;

const k = foo() // k === 3

```

### 2. thunk의 동기

일반 action object가 아닌 function을 반환하는 action creator를 만들어서

자기자신 이외의 액션과 상호작용하는 액션을 생성하거나
조건에 따라서 액션을 생성하거나 하지 않는 등의 행위를 가능하게 한다.

### 3. 공식 깃허브의 코드 예제 보기

```js

import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './reducers';

// 메모: 이 API는 redux@>=3.1.0이상이 요구된다.
const store = createStore(
  rootReducer,
  applyMiddleware(thunk)
);

function fetchSecretSauce() {
  return fetch('https://www.google.com/search?q=secret+sauce');
}

// 위의 예들이 우리가 평범하게 보는 action creators들이다.
// 그것들이 return하는 actions들은 미들웨어 없이 바로 dispatched될 수 있다.
// 하지만, 그것들은 오직 `facts`들만 나타낼 뿐, `async flow`는 나타내질 못한다.

function makeASandwich(forPerson, secretSauce) {
  return {
    type: 'MAKE_SANDWICH',
    forPerson,
    secretSauce
  };
}

function apologize(fromPerson, toPerson, error) {
  return {
    type: 'APOLOGIZE',
    fromPerson,
    toPerson,
    error
  };
}

function withdrawMoney(amount) {
  return {
    type: 'WITHDRAW',
    amount
  };
}

// 미들웨어 없이도, action을 dispatch할 수 있다.
store.dispatch(withdrawMoney(100));

// 하지만 만일 비동기적인 action처리가 필요하기 시작한다면 어떨까?
// 예를들면 API호출 이나 router 변경같이?

// 그럴때는 thunks를 쓰자.
// thunks는 함수를 반환하는 함수이며 아래와 같다.

function makeASandwichWithSecretSauce(forPerson) {

  // Invert control!
  // dispatch를 인자로 받아들이는 함수를 return해서 dispatch를 나중에 할 수 있도록 하라.
  // thunk미들웨어는 thunk 비동기 actions를 actions로 바꾸는 방법을 이미 알고 있다.

  return function (dispatch) {
    return fetchSecretSauce().then(
      sauce => dispatch(makeASandwich(forPerson, sauce)),
      error => dispatch(apologize('The Sandwich Shop', forPerson, error))
    );
  };
}

// Thunk미들웨어는 thunk 비동기 actions를 그것들이 평범한 actions인것 처럼 dispatch가능 하게 해준다.

store.dispatch(
  makeASandwichWithSecretSauce('Me')
);

// 이것은 심지어 thunk의 return value까지도 신경써준다.
// 그래서 내가 그것들을 return하면 Promises chain도 가능하게 해준다.

store.dispatch(
  makeASandwichWithSecretSauce('My wife')
).then(() => {
  console.log('Done!');
});

// 사실, thunk는 다른 actions나 asynch actions를 dispatch할 수 있게 하는 action creators를 쓸 수 있게 할 뿐 아니라,
// Promises를 이용해서 control flow를 구축할 수 있게 도와준다.

function makeSandwichesForEverybody() {
  return function (dispatch, getState) {
    if (!getState().sandwiches.isShopOpen) {

      // 언제나 Promises를 return할 필요는 없으나, 이것이 간편한 관습이다.
      // 이렇게 하므로써, 언제나 .then()으로 async dispatch한 결과를 참조할 수 있기 때문이다.

      return Promise.resolve();
    }

    // We can dispatch both plain object actions and other thunks,
    // which lets us compose the asynchronous actions in a single flow.

    return dispatch(
      makeASandwichWithSecretSauce('My Grandma')
    ).then(() =>
      Promise.all([
        dispatch(makeASandwichWithSecretSauce('Me')),
        dispatch(makeASandwichWithSecretSauce('My wife'))
      ])
    ).then(() =>
      dispatch(makeASandwichWithSecretSauce('Our kids'))
    ).then(() =>
      dispatch(getState().myMoney > 42 ?
        withdrawMoney(42) :
        apologize('Me', 'The Sandwich Shop')
      )
    );
  };
}

// 이는 서버사이드 렌더링에 유용한데,
// 왜냐하면 데이터를 사용할 수 있을때 까지 기다릴 수 있기 때문이다. 그리고 그 뒤에 동기적으로 app을 렌더링 한다.

store.dispatch(
  makeSandwichesForEverybody()
).then(() =>
  response.send(ReactDOMServer.renderToString(<MyApp store={store} />))
);

// 어떠한 컴포넌트의 props가 잃어버린 데이터를 불러와 변하였을때 역시
// 그 컴포넌트로 부터 thunk async action을 dispatch할 수 있다.

import { connect } from 'react-redux';
import { Component } from 'react';

class SandwichShop extends Component {
  componentDidMount() {
    this.props.dispatch(
      makeASandwichWithSecretSauce(this.props.forPerson)
    );
  }

  componentWillReceiveProps(nextProps) {
    if (nextProps.forPerson !== this.props.forPerson) {
      this.props.dispatch(
        makeASandwichWithSecretSauce(nextProps.forPerson)
      );
    }
  }

  render() {
    return <p>{this.props.sandwiches.join('mustard')}</p>
  }
}

export default connect(
  state => ({
    sandwiches: state.sandwiches
  })
)(SandwichShop);
```

## 결론

redux thunk는 redux의 state관리에 async관리까지 한꺼번에 하기 위한 미들웨어라고 할 수 있다.

간편하게 쓸 수 있다는 장점이 있고, Promise관련 처리까지 한번에 처리할 수 있지만,

api가 위의 예제보다 복잡해질 경우 결국에는 알기 힘들다는 단점이 있다.

이를 해결하기 위해서 또 다른 middleware인 redux saga가 등장한다.
