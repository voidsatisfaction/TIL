# High-Order Functions

## 정의

함수를 인자로 받거나 함수를 반환하는 함수를 말한다.

## 특징

함수 역시 데이터 이기 때문에 데이터가 있을 수 있는 곳 어디서든지 있을 수 있다. (e.g. 변수 할당, 다른 함수의 인자로 넘겨줌, 다른 함수의 리턴값)

## 추상화

추상화는 컴퓨터 시스템의 복잡도를 다루기 위한 기술이다. 복잡한 내부의 매커니즘을 낮은 단계(level)에 두고 단계와 단계 사이를 인터페이스로 연결해서 매우 복잡한 로직을 숨긴다.

## 예시

```js
// Practice
export const forEach = (array, fn) => {
  for (var i = 0; i < array.length; i++) {
    fn(array[i]);
  }
};

export const forEachObject = (obj, fn) => {
  for (var property in obj) {
    if (obj.hasOwnProperty(property)) {
      fn(property, obj[property]);
    }
  }
}

export const unless = (predicate, fn) => {
  if (!predicate) {
    fn();
  }
}

export const times = (times, fn) => {
  for (var i = 0; i < times; i++) {
    fn(i);
  }
}

// Realworld
export const every = (array, fn) => {
  let result = true;
  for (const value of array) {
    result = result && fn(value);
  }
  return result;
}

export const some = (array, fn) => {
  let result = false;
  for (const value of array) {
    result = result || fn(value);
  }
  return result;
}

export const sortBy = (property) => {
  return (a, b) => {
    return (a[property] < b[property]) ? -1 : (a[property] > b[property]) ? 1 : 0;
  }
}

```
