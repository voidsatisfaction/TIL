# Currying and Partial application

## A Few Telminologies

- Unary Function: 인자를 하나만 받는 함수
- Binary Function: 인자를 두개만 받는 함수
- Variadic Function: 넘겨받는 인자의 개수만큼을 받는 함(arguments이용)
  - ES6이후로는 Spread Operator를 이용하여 여러 인자를 받을 수 있다.

```js
// example of variadic function

const variadic = (a, ...variadic) => {
  console.log(a);
  console.log(variadic);
};

variadic(1,2,3);
// 1
// [2, 3]
```

## Currying

커링이란, n개의 인자를 갖는 하나의 함수를 **한개의 인자만 받는 함수들의 엮음으로의(nested unary function) 변환**하는 과정을 말한다.

예를들면 다음과 같다.

```js
const add = (x, y) => x + y;
// add(4,4) === 8

const addCurried = x => y => x + y;
// addCurried(4)(4) === 8

const curry = (binaryFn) => (
  (firstArg) => (
    (secondArg) => (
      binaryFn(firstArg, secondArg)
    )
  )
);

const autoCurriedAdd = curry(add);
autoCurriedAdd(2)(2) // 4
```

### Currying Use Cases

### Currying in Action

## Data Flow

### Partial Application

애초에 `unary function`과 전혀관계가 없고, 맨 앞에 함수를 넣고, 그다음 인수중에 나중에 결정되는 인수를 넣어주는 방법.

함수의 인자를 부분적으로 적용하는 방법. `partial`을 n개의 인자를 받는 어떠한 함수에도 적용할 수 있다.

예를들면 다음과 같다.

```js
export const partial = (fn, ...partialArgs) => {
  const args = partialArgs;
  return function(...fullArguments) {
    let arg = 0;
    for (var i = 0; i < args.length && arg < fullArguments.length; i++) {
      if (args[i] === undefined) {
        args[i] = fullArguments[arg++];
      }
    }
    return fn.apply(null, args);
  };
};

const delayTenMs = lib.partial(setTimeout, undefined, 10); // 가운데의 인자가 undefined이다. (만약, currying이라면 가운데에 undefined를 두는 것이 불가능하다. 그래서 인자의 순서를 wrapper function을 이용해서 바꿔야 하는데 이는 오버헤드)
delayTenMs(() => 'Do Y task');
```

## 어떨때 currying, 어떨때 partial application?

API가 어떻게 정의되었느냐에 따라서 다르다. 만약, API가 `map`, `filter`과 같이 정의되어있다면 쉽게 curry함수를 도입하면 된다.

하지만, `setTimeout`과같은 경우에는 partial functions를 이용하는 것이 좋다.

결국에 둘다 함수를 쉽게 구성하고 강력하게 하는것이 목표다.

커링은 **nested unary functions**를 반환한다.

커링과 partial중 둘중에 하나를 선택한다.
