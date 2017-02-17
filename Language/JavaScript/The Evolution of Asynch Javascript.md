# 비동기 자바스크립트의 진화

## 콜백

- 장점
  - async프로그래밍을 가능하게 한다.

- 단점
  - callback hell이나 스파게티코드가 되기 쉽다.
  - error handling을 까먹기 쉽게 된다.
  - `return`으로 값을 반환할 수 없어지고, `throw`도 사용하지 못하게 된다.

## async모듈

- 쓰기 불편하다.

## Promise

- 장점
  - thenable(동기적인 형태로 함수를 이어나갈 수 있다)

- 단점
  - 오직 하나의 값만 반환할 수 있다.
  - 콜백보다는 느림
  - state에 대한 제어는 불가능

## Generators / yield + Promise

> Wouldn't it be nice, that when you execute your function, you could pause it at any point, calculate something else, do other things, and then return to it, even with some value and continue?

- Generator는 iterator를 만드는 generator를 뜻한다.
- Observable(yield를 이용해서 함수의 도중의 값을 관찰할 수 있다.)

Generator함수는 단순히 함수를 실행시킨다고 해서 작동하지 않는다.
나 자신이 수동으로 iterate해야한다.
async를 위한 도구라기 보다는, hack이라고 봐야한다.

```js

function* foo() {
  let index = 0;
  while (index < 2) {
    yield index++;
  }
}
const bar = foo();

console.log(bar.next()); // { value: 0, done: false }
console.log(bar.next()); // { value: 1, done: false }
console.log(bar.next()); // { value: undefined, done: true }

```

## Async / await

- Promise를 사용한다. 그러므로, async함수는 Promise를 반환한다.

```js

async function save(something) {
  try {
    await Something.save()
  } catch (ex) {
    // error handling
  }
  console.log('success');
}

```

## IDN

non-blocking / blocking?
