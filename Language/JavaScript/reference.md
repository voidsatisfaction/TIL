# 쉽게 틀릴 수 있는 js reference

이 내용을 몰라서 무엇이 잘못되었나 한참을 찾았다.

## 다음과 같은 예

```js
const x = [{a: 1, b: 1}, {a: 1, b: 3}]
const y = x.filter((e) => e.b > 2)
x[1].a += 1
y // [{a: 2, b: 3}]
```

위의 코드를 원하는 대로 제어하려면 이하와 같이 써야한다.

```js
const x = [{a: 1, b: 1}, {a: 1, b: 3}]
const y = x.map((e) => Object.assign({}, e)).filter((e) => e.b > 2)
x[1].a += 1
y // [{a: 1, b: 3}]
```
