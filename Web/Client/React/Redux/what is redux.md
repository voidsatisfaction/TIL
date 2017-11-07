# Motivation

- As the requirements for JavaScript single-page applications have become increasingly complicated, our code must manage more state than ever before.
- so lost control over the when, why, and how of its state.
- new requirements becoming common in front-end product development.
- blame for **mutation** / **asynchronocity**
- Redux attempts to make state mutations predictable

# Core Concepts

## Store = plain object without setters.

```js

{
  todos: [{
    text: 'Eat food',
    completed: true,
  }, {
    text: 'Exercise',
    completed: false,
  }],
  visibilityFilter: 'SHOW_COMPLETED',
}

```

## Action = the **object** that describes what happened

If something changed, we know why it changed.
Action creator can be asynchronous and have side-effect(ex AJAX)

```js
// Actions
{ type: 'ADD_TODO', text: 'Go to swimming pool' }
{ type: 'TOGGLE_TODO', index: 1 }
{ type: 'SET_VISIBILITY_FILTER', filter: 'SHOW_ALL' }

//Action Creators
// portable and easy to test
function addTodo(text) {
  return {
    type: Add_TODO,
    text
  }
}

// initiate action creator
dispatch(addTodo(texte));
dispatch(completeTodo(index));

// bound action creator
const boundAddTodo = (text) => dispatch(addTodo);
const boundCompleteTodo = (index) => dispatch(completeTodo(index));

// you can use it like
store.dispatch();

// but it is better using helper
connect();
```

## Reducer = just a function that takes state and action as arguments, and returns the next state of the app

```js

function visibilityFilter(state = 'SHOW_ALL', action) { // 파라미터 안의 할당이 뭘까?(값이 없을때에는 할당되는것을 반영, 값을 넘겨받으면 그냥 그 값으로 활용)
  if (action.type === 'SET_VISIBILITY_FILTER') {
    return action.filter;
  } else {
    return state;
  }
}

function todos(state = [], action) {
  switch (action.type) {
  case 'ADD_TODO':
    return state.concat([{ text: action.text, completed: false }]);
  case 'TOGGLE_TODO':
    return state.map((todo, index) =>
      action.index === index ?
        { text: todo.text, completed: !todo.completed } :
        todo
   )
  default:
    return state;
  }
}

// Upper functions are combined with below wrapper function

function todoApp(state = {}, action) {
  return {
    todos: todos(state.todos, action),
    visibilityFilter: visibilityFilter(state.visibilityFilter, action)
  };
}

```

# Three Principles

## Single source of truth

**whole application state === an object tree within a single store**

## State is read-only

**State change === emit an action(plain object)**

neither the views nor the network callbacks will ever write directly to the state.

## Changes are made with pure functions

**take the previous state and action => return the next state(new!!)**

# IDN
- What model exectly is
- does Array.map method return new array?
- What is parameter assignment? `function todos(state = [], action) {}`
