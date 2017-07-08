# 버추얼 돔

## 버추얼 돔의 포인트

1. virtual DOM은 실제 DOM의 임의의 형식의 구현체이다.
2. virtual DOM을 수정하면 old virtual tree와 new virtual tree를 비교하여 차이를 확인하고 real DOM의 필요최소한의 부분만 바꾼다.

## DOM Tree의 구현

DOM Tree를 메모리에 올려둬야할 필요가 있다. 그리고, 그러한 것은 plain JS objects로 가능.

```html
<ul class="list">
  <li>item 1</li>
  <li>item 2</li>
</ul>
```

위를 plain js objects로 나타냄

```js
{ type: 'ul', props: { 'class': 'list' }, children: [
    { type: 'li', props: {}, children: ['item 1'] },
    { type: 'li', props: {}, children: ['item 2'] }
] }
```

하지만 이와같이 모든 복잡한 DOM트리를 만드는건 힘들다.

그래서 helper function을 준비한다.

```js
function h(type, props, ...children) {
  return { type, props, children };
}

h('ul', { 'class': 'list' },
  h('li', {}, 'item 1'),
  h('li', {}, 'item 2'),
);

/* 위와 같이 나타낼 수 있다. */
```

## DOM 구현체의 적용

여기서 다음과 같은 제약을 두자

1. real DOM nodes(elements, text nodes)는 $표시와 함꼐 시작하자. e.g) `$parent`
2. Virtual DOM은 `node`라는 변수로 표현된다.
3. React처럼, 우리는 하나의 `one root node `가 있고, 다른 노드들은 다 그 속에 존재한다.

```js
/** @jsx h */
if (module.hot) {
  module.hot.accept();
}

function h(type, props, ...children) {
  return { type, props, children };
}

function createElement(node) {
  if (typeof node === 'string') {
    return document.createTextNode(node);
  }
  const $el = document.createElement(node.type);
  node.children
    .map(createElement)
    .forEach($el.appendChild.bind($el));
  return $el;
}

const a = (
  <ul className="list">
    <li>item 1</li>
    <li>item 2</li>
  </ul>
);

const $root = document.getElementById('root');
$root.appendChild(createElement(a));
```

## 변화 적용

이제까지는 virtual DOM을 real DOM으로 변화시키는 과정이었다.

이제는 old virtual Tree와 new virtual Tree를 비교해서 적용하는 "변화 적용"부분을 구현하자.

변화의 정의

1. appendChild
2. removeChild
3. replaceChild
4. different node types
