# Currying and Partial application

## A Few Telminologies

- Unary Function: 인자를 하나만 받는 함수
- Binary Function: 인자를 두개만 받는 함수
- Variadic Function: 넘겨받는 인자의 개수만큼을 받는 함수(arguments이용)
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

커링의 일반화

```js
export const curry = (fn) => {
  if (typeof fn !== 'function') {
    throw Error('No function provided');
  }

  return function curriedFunction(...args) {
    if (fn.length > args.length) {
      return function() {
        return curriedFunction.apply(null, (args.concat( [].slice.call(arguments) )));
      };
    }
    return fn(...args);
  };
};
```

### Currying in Action

## Data Flow

### Partial Application

애초에 `unary function`과 전혀관계가 없고, 맨 앞에 실행하고 싶은 함수를 넣고, 그 함수에 인수를 넣어주는데, 인수가 지금 상황에서는 undefined되어있는 것들도 미리 정의해 두었다가 나중에 호출하면서 undefined였던 인자에 대한 인수를 넣어줘서 함수를 실행하는 방법(예를 보는게 더 이해하기 쉽다)

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

const delayTenMs = lib.partial(setTimeout, undefined, 10); // 현재 상황에서는 setTimeout에 어떠한 함수인자로 넘길지 미정
delayTenMs(() => 'Do Y task'); // 지금 setTimeout에 어떠한 함수인자로 넘길지 정함(바로 실행)

// 위의 lib.partial(setTimeout, undefined, 10);를 보면, 가운데의 인자가 undefined이다.
// (만약, currying이라면 가운데에 undefined를 두는 것이 불가능하다. 그래서 인자의 순서를 wrapper function을 이용해서 바꿔야 하는데 이는 오버헤드)
```

위에서 보면, `partial(fn, ...partialArgs)`이므로, fn에 원래 사용하려던 함수가 들어가고, partialArgs는 인자로서 **순서대로** 삽입된다. 위의 예에서 undefined가 나오는 것은, `setTimeout`함수가 차례로 함수인자를 받고 숫자인자를 받는데, 아직 함수가 정의되지 않았다는 것이다.

*위의 partial함수는 함정이 있으므로 주의(args의 클로저에 관한...)*

## 어떨때 currying, 어떨때 partial application?

API가 어떻게 정의되었느냐에 따라서 다르다. 만약, API가 `map`, `filter`과 같이 정의되어있다면 쉽게 curry함수를 도입하면 된다.

하지만, `setTimeout`과같은 경우에는 partial functions를 이용하는 것이 좋다.

결국에 둘다 함수를 쉽게 구성하고 강력하게 하는것이 목표다.

커링은 **nested unary functions**를 반환한다.

커링과 partial중 둘중에 하나를 선택한다.
