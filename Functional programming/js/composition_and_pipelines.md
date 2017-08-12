# Composition and Pipelines

함수적 합성.

## Composition in General Terms

### Unix Philosophy

> Make each program do one thing well. To do a new job, build afresh rather than complicate old programs by adding new features.
> Export the output of every program to become the input to another, as yet unknown program.

이하는 위의 사상에 대한 예시.

```bash
cat test.txt | grep 'world' | wc
# Hello world
```

`cat test.txt`에 대한 반환값을 `grep` 함수의 인자로 사용하였다. 그리고 그 결과에서 world라는 단어의 개수를 세어주었다.

### Base Function

base함수란, 인자를 받아서 데이터를 반환하는 함수이다. 마치 Unix/Linux에서의 |(파이프)와 같은 역할을 하는 함수.

함수 합성의 진정한 장점은, base function을 기반으로 현실의 문제를 **새로 함수를 정의하지 않고** 해결하는데에 있다.

## Functional Composition

두 함수를 합성하는 compose함수의 정의

```js
export const compose = (a, b) =>
  (c) => a(b(c));
```

이 `compose`함수는 하나의 인자만을 받는 두 함수를 합성할 수 있다. 하지만 모든 함수가 하나의 인자만을 받지 않으므로, `curry`와 `partial` function을 적절하게 이용해준다.

예시

```js
export const compose = (a, b) =>
  (c) => a(b(c));

const filterGoodBooks = (book) => book.rating[0] > 4.5;
const projectTitleAndAuthor = (book) => ({ title: book.title, author: book.author });

const queryGoodBooks = partial(arrayUtils.filter, undefined, filterGoodBooks); // queryGoodBooks함수는 아직 array를 알지 못한다.(앞으로 array만 받으면 됨)
const mapTitleAndAuthor = partial(arrayUtils.map, undefined, projectTitleAndAuthor); // mapTitleAndAuthor함수는 아직 array를 알지 못한다.

const titleAndAuthorForGoodBooks = lib.compose(mapTitleAndAuthor, queryGoodBooks);

const got = titleAndAuthorForGoodBooks(apressBooks); // [{ title: 'C# 6.0', author: 'ANDREW TROELSEN' }];
```

작은 함수 유닛을 만들고 그것을 `compose`함수를 이용해서 새로운 함수를 만들어나간다.

### Compose many function

아주 아름다운 코드가 등장한다.

```js
export const compose = (...fns) => (
  (value) => fns.reverse().reduce((acc, fn) => fn(acc), value)
);

```

보기만해도 매력적인 코드다.

## Pipelines / Sequence

`Pipe(Sequence)`는 `compose`함수와 완전히 같은 역할이면서, 데이터플로가 반대이다.

```js
export const pipe = (...fns) => (
  (value) => (
    fns.reduce((acc, fn) => fn(acc), value)
  )
);
```

### Implementing pipe

```js
const splitIntoSpaces = (string) => string.split(' ');
const count = (array) => array.length;
const oddOrEven = (num) => (num % 2 === 0 ? 'even' : 'odd');
const countWords = lib.pipe(splitIntoSpaces, count, oddOrEven); // 순서가 compose의 반대다.
const got2 = countWords('hello world my name'); // even
```

### Odds on Composition

1. composition is associative
2. how we debug when we compose many functions

### 1. Composition is associative

```js
const countWords1 = compose(compose(oddOrEven, count), splitIntoSpaces);
const countWords2 = compose(oddOrEven, compose(count, splitIntoSpaces));
```

위의 두 함수는 결국 같은 함수이다.

compose는 생각해보면 합성함수의 개념이다. 그래서 f | (g | h) === (f | g) | h 와 같다. 즉 associative하다.

### 2. Debugging Using tap Function

```js
const identity = (it) => {
  console.log(it);
  return it;
}
```

위의 identity함수를 정의하자.

```js
compose(oddOrEven, count, splitIntoSpaces); // 만약 count함수에서 ERROR가 나왔다면 다음과 같은 함수로 다시 compose한다.

compose(oddOrEven, count, identity, splitIntoSpaces);
```

위 코드에서 identity를 count함수 이전에 넣는것으로 인해, count함수의 인자로 무엇이 들어가게 되는지 파악할 수 있게 된다. 이는 디버깅에 큰 도움이 된다.
