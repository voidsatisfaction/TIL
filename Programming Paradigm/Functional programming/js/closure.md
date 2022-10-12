# Closure and HOC

## Understanding Closure

### 클로저의 정의

함수가 선언될 당시의 환경(environment(스코프를 포함한 개념))을 기억했다가 나중에 호출되었을 때 원래의 환경에 따라 수행되는 함수이다.

내부함수는 외부함수의 scope(스코프 체인)에 접근할 수 있는데, 이것을 lexical scope로 부르고 이러한 lexical scope를 함수 선언시에 포섭(closure)하여 실행되기 때문에 클로저라 한다.

기술적으로 클로저는 다음과 같은 스코프에 접근할 수 있다.

1. 자기 자신의 스코프의 변수들
2. 글로벌 변수들
3. 외부 함수의 변수들

예시

```js
let global = "global";
function outer() {
  let outer = "outer"
  function inner() {
    let a = 5;
    console.log(outer); // outer
  }
  inner();
}
```

### Remembering where it is born

```js
const fn (arg) => {
  const outer = "visible";
  const inner = () => {
    console.log(outer);
    console.log(arg);
  }
  return inner;
}

const closureFn = fn(5);
closureFn()

// visible
// 5
```

위의 코드 해석

1. `closureFn = fn(5)`가 실행되면, `fn`가 5의 인수를 갖고 실행된다. 그리고 이는 `innerFn`을 반환한다.
2. `innerFn`이 반환되면, js실행 엔진은 `innerFn`을 클로저로 보고 이것의 scope를 그에 따라 설정한다. 여기에서는 **3 scope level(chain)이 설정되며 반환**되는 것이다. 반환된 함수의 reference는 `closureFn`에 저장된다. 그래서 closureFn는 `arg`, `outer`를 scope chains을 통하여 기억할 수 있게 된다.
3. 그리고 원하는 결과를 출력한다.

결국 클로저는 자신의 context(scope chains)을 기억한다고 보면 된다.

### HOC in real world

```js
export const unary = (fn) => {
  return fn.length === 1 ? fn : (arg) => fn(arg);
};

export const once = (fn) => {
  let done = false;
  return () => (
    done ? undefined : ((done = true), fn.apply(this, arguments))
  );
}

export const memoized = (fn) => {
  const lookupTable = {};

  return (arg) => (lookupTable[arg] || (lookupTable[arg] = fn(arg)));
}

// factorial with memoization
const fastFactorial = lib.memoized((n) => {
  if (n === 0) {
    return 1;
  }

  return n * fastFactorial(n-1);
});

expect(fastFactorial(3)).to.equal(6);
expect(fastFactorial(5)).to.equal(120);

// memoizedMultiple
export const memoizedMultiple = (fn) => {
  const lookupTable = {};

  return (...args) => {
    return (lookupTable[String(args)] || (lookupTable[String(args)] = fn(...args)));
  };
};

// multiple arguments plus memoization
const fastPlus = lib.memoizedMultiple((...args) => {
  return args.reduce((a,b) => a+b);
});

expect(fastPlus(1,2,3,4)).to.equal(10);
expect(fastPlus(9,9,8,1,9,9,9)).to.equal(54);
```
