# Functors

Functor를 사용하여 Error handling을 구현해보자.

## What is a Functor?

Functor란 함수 map을 갖고 있는 plain object(혹은, 다른 언어에서의 type class)를 말한다.

### Functor is a container

Functor란, 값을 안에 갖고 있는 컨테이너다. 그래서 Functor가 plain object라고 한 것이다.(js에서는) 그리고, map함수를 갖고 있어서 그 객체 가 갖고있는 값을 변화시켜 새로운 객체를 만들 수 있다.

```js
// Arrow function cannot be the constructor
export const Container = function(val) {
  this.value = val;
};

Container.of = function(value) {
  return new Container(value);
};

const testValue = Container.of(3); // { value: 3 }
const testObj = Container.of({ a: 1 }); // { value: { a: 1 } }
const testArray = Container.of([1,2]); // { value: [1,2] }
```

### Functor Implements Method Called map

Functor의 맵 함수는 Container로 부터의 오브젝트가 갖고 있는 값을 map함수의 함수 인자로 적용시켜서, 그 결과 값을 다시 Conatiner로 저장한다.

```js
// Arrow function cannot be the constructor
export const Container = function(val) {
  this.value = val;
};

Container.of = function(value) {
  return new Container(value);
};

Container.prototype.map = function(fn) {
  return Container.of(fn(this.value));
};

const double = (n) => n + n;
const got2 = Container.of(3).map(double).map(double).map(double).value; // 24
```

## MayBe(functor)

Maybe functor는 함수적 방식으로 에러를 헨들링하게 도와준다.

### Implementing MayBe

MayBe도 functor이므로, map함수를 갖게 될거지만, 방식이 다르다.

```js
MayBe.of = function(val) {
  return new MayBe(val);
};

MayBe.prototype.isNothing = function() {
  return (this.value === null || this.value === undefined);
};

MayBe.prototype.map = function(fn) {
  return this.isNothing() ? MayBe.of(null) : MayBe.of(fn(this.value));
};

MayBe.of('string').map((x) => x.toUpperCase()); // MayBe { value: 'STRING' }
MayBe.of(null).map((x) => x.toUpperCase()); // MayBe { value: null }

```

위의 MayBe functor는 type safe하다.

```js
const got = MayBe.of('George')
  .map((x) => x.toUpperCase())
  .map((x) => 'Mr. ' + x); // Mr. GEORGE
```

또한 위와 같이 chainable하다.

그리고, chain된 `map`은 도중에 value가 undefined가 되어도 전부 실행된다(map함수 내부에서 값에 대한 처리를 할 뿐)

### 실생활 예제

## Either Functor

MayBe Functor의 진화버전. 어디에서 에러가 났는지, 에러메세지를 파악할 수 있다.

## 사실은 이제까지 했던것들은 Pointed Functor라고 불린다.

`new` 키워드를 escape하기 위해서 우리는 `of`라는 메소드를 정의 했었다. 이는, Functor의 부분집합인 Pointed Functor이다. `of contracts`를 갖고있는.
