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

**변화의 정의**

1. appendChild
2. removeChild
3. replaceChild
4. different node types

```js
/** @jsx h */

if (module.hot) {
  module.hot.accept();
}

function h(type, props, ...children) {
  return { type, props: props || {}, children };
}

/* ---------- ELEMENT ------------ */

function createElement(node) {
  if (typeof node === 'string') {
    return document.createTextNode(node);
  }
  const $el = document.createElement(node.type);
  setProps($el, node.props);
  node.children
    .map(createElement)
    .forEach($el.appendChild.bind($el));
  return $el;
}

function changed(node1, node2) {
  return typeof node1 !== typeof node2 ||
         typeof node1 === 'string' && node1 !== node2 ||
         node1.type !== node2.type
}

function updateElement($parent, newNode, oldNode, index=0) {
  if (!oldNode) {
    $parent.appendChild(
      createElement(newNode)
    );
  } else if (!newNode) {
    $parent.removeChild(
      $parent.childNodes[index]
    );
  } else if (changed(newNode, oldNode)) {
    $parent.replaceChild(
      createElement(newNode),
      $parent.childNodes[index]
    );
  } else if (newNode.type) {
    const newLength = newNode.children.length;
    const oldLength = oldNode.children.length;
    for (let i = 0; i < newLength || i < oldLength; i++) {
      updateElement(
        $parent.childNodes[index],
        newNode.children[i],
        oldNode.children[i],
        i
      );
    }
  }
}

/* ---------------------- */

const f = (
  <ul style="list-style: node;">
    <li className="item">item 1</li>
    <li className="item">
      <input type="checkbox" checked={true} />
      <input type="text" disabled={false} />
    </li>
  </ul>
);

const $root = document.getElementById('root');

$root.appendChild(createElement(f));
```

## Props의 적용

다음과 같은 동작이 필요하다.

1. setProps
2. removeProps
3. updateProps

```js
// custom prop, class prop ,boolean prop, normal prop

function isCustomProp(name) {
  return false;
}

function setBooleanProp($target, name, value) {
  if (value) {
    $target.setAttribute(name, value);
    $target[name] = true;
  } else {
    $target[name] = false;
  }
}

function setProp($target, name, value) {
  if (isCustomProp(name)) {
    return;
  } else if (name === 'className') {
    $target.setAttribute('class', value);
  } else if (typeof value === 'boolean') {
    setBooleanProp($target, name, value);
  } else {
    $target.setAttribute(name, value);
  }
}

function setProps($target, props) {
  Object.keys(props).forEach((name) => {
    setProp($target, name, props[name]);
  });
}

function removeBooleanProp($target, name) {
  $target.removeAttribute(name);
  $target[name] = false;
}

function removeProp($target, name, value) {
  if (isCustomProp($target)) {
    return;
  } else if (name === 'className') {
    $target.removeAttribute('class');
  } else if (typeof value === 'boolean') {
    removeBooleanProp($target, name);
  } else {
    $target.removeAttribute(name);
  }
}

function updateProp($target, name, newVal, oldVal) {
  if (!newVal) {
    removeProp($target, name, oldVal);
  } else if (!oldVal || newVal !== oldVal) {
    setProp($target, name, newVal);
  }
}

function updateProps($target, newProps, oldProps = {}) {
  const props = { ...newProps, ...oldProps };
  Object.keys(props).forEach((name) => {
    updateProp($target, name, newProps[name], oldProps[name]);
  });
}
```

위와 같이 정의한다. 그리고 ui로 토글 버튼을 적용한 코드는 아래와 같다.

```js
const f = (
  <ul style="list-style: none;">
    <li className="item">item 1</li>
    <li className="item">
      <input type="checkbox" checked={true} />
      <input type="text" disabled={false} />
    </li>
  </ul>
);

const g = (
  <ul style="list-style: none;">
    <li className="item item2">item 1</li>
    <li style="background: red;">
      <input type="checkbox" checked={false}/>
      <input type="text" disabled={true}/>
    </li>
  </ul>
)

const $root = document.getElementById('root');
const $reload = document.getElementById('reload');

updateElement($root, f);
$reload.addEventListener('click', () => {
  if ($reload.className == 'active') {
    $reload.className = null;
    updateElement($root, g, f);
  } else {
    $reload.className = 'active';
    updateElement($root, f, g);
  }
})
```

## Events적용

querySelector, addEventListener보다 멋진 방법으로 이벤트를 등록하자.

```js
<button onClick={() => alert('hi!')}></button>
```
