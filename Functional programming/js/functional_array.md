# Functional programming with arrays

## Working Functionally on Arrays

### Projection function

projection(transforming) function이란, map과 같이 주어진 배열의 값에 함수를 적용시켜 새로운 배열을 반환하는 함수를 말한다.

### map

map함수는 배열의 요소 하나하나를 받아서 그것을 projection function의 인자로 넘겨주고 그 결과를 원래 있던 요소의 자리에 새 배열로서 바꿔치기해서 리턴해준다.

```js
export const map = (array, fn) => {
  const result = [];
  for (const value of array) {
    result.push(fn(value));
  }
  return result;
};
```

### filter

filter함수는 배열의 요소를 하나하나 받아서 그것을 projection function의 인자로 넘겨주고 그 값이 true라면 새 배열에 추가, false라면 추가하지 않고 리턴해준다.

```js
const filter = (array, fn) => {
  const result = [];
  for (const value of array) {
    fn(value) ? result.push(value) : undefined;
  }
  return result;
};
```

### concatAll

concatAll함수는 배열을 인자로 받아서, 배열 안의 배열의 요소를 끄집어 낸다. 원래 배열이 아니었던 경우에는 에러가 발생하므로 주의.

c.f `apply`함수는 메소드의 `this`의문맥을 변경하면서, **배열**을 함수에 넘겨주는 인자로서 받는다. (그리고 작동은 평범하게 여러 인자를 건네주는 것 처럼 함)

```js
const concatAll = (array) => {
  const result = [];
  for (const value of array) {
    result.push.apply(result, value);
  }
  return result;
};
```

### reduce

reduce함수는 배열과 함수와 초기값(선택)을 인자로 받아서, 초기값(정의되지 않으면 가장 첫 값)을 `accumulator`로하여 accumulator에 인자로 받은 함수를 사용하여 값을 넣어 나간다. 그리고 배열이 더이상 없게 되면 accumulator를 반환한다.

```js
const reduce = (array, fn, initVal) => {
  let accumlator;

  if (initVal === undefined) {
    accumlator = array[0];
    for (var i = 1; i < array.length; i++) {
      accumlator = fn(accumlator, array[i]);
    }
  } else {
    accumlator = initVal;
    for (const value of array) {
      accumlator = fn(accumlator, value);
    }
  }
  return accumlator;
};
```

### zip

zip함수는 배열 두개와 함수를 인자로 받아서, 두개의 배열을 맨 앞 원소부터 순차적으로 인자로 받은 함수에 적용하여 그 결과를 하나의 배열의 결과로 리턴해준다. 만일, 처음 받은 두개의 배열의 크기가 다르다면, 더 작은 크기까지만 함수를 적용한 값을 하고 그 뒤는 자른다.

```js
const zip = (arr1, arr2, fn) => {
  const result = [];
  for (var i = 0; i < Math.min(arr1.length, arr2.length); i++) {
    result.push(fn(arr1[i],arr2[i]));
  }
  return result;
};
```
