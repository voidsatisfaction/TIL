# Beggining Functional Programming

## 1. Functional Programming in Simple Terms

### 함수의 수학적 정의

```
y = f(x)
```

- 함수는 반드시 인자(argument)를 받는다.
- 함수는 항상 값을 반환한다.
- 함수는 outside world가 아닌 arguments에 대하여 행동해야 한다.
- 일정한 X가 argument로 주어지s면 반환값은 항상 Y이다.

> Functional programming is a paradigm in which we will be **creating functions that are going to work out its logic by depending only on its input.** This ensures that a function, when called multiple times, is going to return the same result. **The function also won't change any data in the outside world**, leading to cacheable and testable codebase.

### Referential Transparency

**언제나 같은 input(arguments)에 대해서 같은 output(value)를 반환하는 함수의 특성을 referential transparancy라고 한다.**

```js
// identity함수는 referential transparent이다.
var identity = (i) => { return i }

sum(4,5) + identity(1)
// 위의 코드는 referential transparent이기 때문에 아래와 같이 바뀔 수 있음
// 이와 같은 프로세스를 Substitution model이라고 한다.
sum(4,5) + 1
```

Substitution model은 parallel코드와 caching을 가능하게 한다.

parallel

만약, 멀티 스레드에서 이와같은 함수로 구성된 프로그램을 돌리면, synchronizing이 필요가 없으므로 locking도 필요 없어진다.

caching

`factorial`함수가 존재할 경우에, factorial(5)를 두번 계산할 필요가 없다. 한 번 계산한 뒤에 그 값을 caching하면 된다.

### Imperative, Declarative, Abstraction

FP(functional programming)은 *declarative*한 것이며, *abstracted*한 코드를 작성하는 것을 뜻한다.

Imperative(How)

컴파일러에게 **어떻게** 임무를 수행하는가를 지시한다.

```js
// Imperative codes

var array = [1,2,3];
for (var i = 0; i < array.length; i++) {
  console.log(array[i]); // prints 1, 2, 3
}

```

1. array의 길이를 구하고
2. loop를 돌면서
3. 각 원소를 출력하라

Declarative(What)

컴파일러에게 **무엇을** 수행해야하는지 나타낸다. how에 관한 것은 high-order function에 의해서 추상화된다.

```js
// Declarative codes

var array = [1,2,3];
array.forEach((e) => console.log(e)); // prints 1, 2, 3
```

추상화된 함수를 사용하여 how를 추상화시킴.

## 2. Functional Programming Benefits

대부분의 장점은 pure function을 만드는 것에서 온다.

### Pure Functions

pure function이란, 같은 input에 같은 output을 반환하는 함수를 말한다. 즉 **referential transparancy**를 만족하는 함수를 말한다.

```js
var double = (value) => value * 2;
```

### 1. Testable code

pure function은 부작용이 없다.

Pure Function shouldn't mutate any external environment variables.

Pure Function should't depend on any external variables.

### 2. Reasonable code

함수 이름에서 쉽게 함수의 동작을 유추할 수 있다.

pure functions을 사용하므로써, 타인이 나의 코드를 쉽게 읽을 수 있게 해준다. 애초에 pure function의 implementation code를 볼 필요가 없다.

```js
Math.max(3,4,5,6) // 6
```

> Function must always have a meaningful name

### 3. Parallel code

Impure

```js
let global = "something";
let function1 = (input) => {
  global = "soemthingElse"
}
let function2 = () => {
  if (global === "something") {
    // business logic
  }
}
```

Pure

```js
let function1 = (input, global) => {
  global = "somethingElse"
}
let function2 = (global) => {
  if (global === "something") {
    // business logic
  }
}
```

impure에서는 만약 병행처리를 function1 function2 의 순으로 실행하게 되면 `global`이 변하게 되면서 function2가 원하는 동작을 하지 못하게 된다.

하지만 function1, function2를 pure functions로 변화시킨 후에는 global scope를 변화시키지 않기 때문에 실행 순서를 신경쓰지 않아도 된다.

### 4. Cachable

```js
var longRunningFunction = (ip) => {
  // do long time consuming things
}

var longRunningFnBookKeeper = { 2 : 3, 4 : 5 } // object

longRunningFnBookKeeper.hasOwnProperty(ip) ?
  longRunningFnBookKeeper[ip] :
  longRunningFnBookKeeper[ip] = longRunningFunction(ip)
```

### 5. Pipelines and Composable

Pure functions should be designed as doing only one thing and doing it perfectly (Unix philosophy)

```sh
# Do one thing perfectly
cat
grep
wc

# Composable
cat jsBook | grep -i "composing" | wc
```

### 6. Pure Function is a mathematical function

> In mathematics, a function is a relation between a set of inputs and a set of permissible ouputs with the property that each input is related to exactly one output. The input to a function is called the argument and the output is called the value. The set of all permitted inputs to a given function is called the domain of the function, while the set of permissible outputs is called the domain.
