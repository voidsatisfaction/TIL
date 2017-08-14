# Monad

모나드는 functor의 한 종류.

`chain`메소드(value값을 변경하면서 추상레이어를 한커풀 벗기는 메소드)가 있는 `functor`를 모나드라고 한다.

## Getting reddit comments for our search query

레딧 홈페이지에 get request를 보내서 response를 받아오고 그 데이터를 가공한다고 하자.

## Problem

너무나도 많이 MayBe functor의 map을 사용한다.

특히 마지막에 `mergeViaMayBe("functional programming")`을 실행한뒤에 데이터 구조를 변환시키는데에만 엄청나게 많은 코드를 써야한다.

## Solvint the Problem via join

### join Implementation

```js
export const MayBe = function(val) {
  this.value = val;
};

MayBe.of = function(val) {
  return new MayBe(val);
};

MayBe.prototype.isNothing = function() {
  return (this.value === undefined || this.value === null);
};

MayBe.prototype.map = function(fn) {
  return this.isNothing() ? MayBe.of(null) : MayBe.of(fn(this.value));
};

MayBe.prototype.join = function() {
  return this.isNothing() ? MayBe.of(null) : this.value;
};
```

### chain Implementation

```js
MayBe.prototype.chain = function(fn) {
  return this.map(fn).join();
};
```
