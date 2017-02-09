# Reducers

**Must be pure**

## Designing the State Shape

```js
{
  visibilityFilter: 'SHOW_ALL',
  todos: [
    {
      text: 'Consider using Redux',
      completed: true,
    },
    {
      text: 'Keep all state in a single tree',
      completed: false
    }
  ]
}
```

## Handling Actions

`(previousState, action) => newState`

- Things you should never do inside a reducer:

It's called a reducer because it's the type of function you would pass to Array.prototype.reduce(reducer, ?initialValue). It's very important that the reducer stays pure. 

1. Mutate its arguments;
2. Perform side effects like API calls and routing transitions;
3. Call non-pure functions, e.g. Date.now() or Math.random().

## 1

가장 처음에는 Redux가 undefined state로 reducer를 호출한다.
여기서 store의 initial state를 지정.

```js
// Do not mutate state

const todoApp(state = initialState, action) { 
  switch (action.type) {
    case SET_VISIBILITY_FILTER:
      return Object.assign({}, state, {
        visibilityFilter: action.filter
      })
      //
      /*
      return { ...state, ...{visibilityFilter: action.filter} }
      */
    default:
      return state
  }
  return state;
}

```

## Handling More Actions

```js

function todoApp(state = initialState, action) {
  switch (action.type) {
    case SET_VISIBILITY_FILTER:
      return Object.assign({}, state, {
        visibilityFilter: action.filter
      })
    case ADD_TODO:
      return Object.assign({}, state, {
        todos: [
          ...state.todos,
          {
            text: action.text,
            completed: false
          }
        ]
      })
    case TOGGLE_TODO:
      return Object.assign({}, state, {
        todos: state.todos.map((todo, index) => {
          return Object.assign({}, todo, {
            completed: !todo.completed
          })
        })
      })
    default:
      return state
  }
}

```

```js

const todos = (state = [], action) => {
  switch (action.type) {
    case ADD_TODO:
      return [
        ...state,
        {
          text: action.text,
          completed: false
        }
      ]
    case TOGGLE_TODO:
      return state.map((todo, index) => {
        if (index === action.index) {
          return Object.assign({}, todo, {
            completed: !todo.completed
          })
        }
        return todo
      })
    default:
      return state
  }
}

const visibilityFilter = (state = SHOW_ALL, action) => {
  switch (action.type) {
    case SET_VISIBILITY_FILTER:
      return action.filter
    default:
      return state
  }
}

const todoApp = (state = {}, action) => ({
  visibilityFilter: visibilityFilter(state.visibilityFilter, action),
  todos: todos(state.todos, action)
});

// 위의 todoApp은 아래와 같음

import { combineReducers } from 'redux'

const todoApp = combineReducers({
  visibilityFilter,
  todos
})

export default todoApp

// key를 줄 수도 있음.

const reducer = combineReducers({
  a: doSomethingWithA,
  b: processB,
  c: c
})

```

각각의 reducers는 store의 일부분만 제어한다.
각각의 reducer마다 state가 각각 다르다는 얘기이다.

앱의 규모가 커지면, reducers들을 각각의 파일로 분리해서 다른 데이터 영역과 완전히 독립적으로 사용가능.

`combineReducers()`는 의의 todoApp과 같은 함수를 출력한다.