# js의 RORO(Receive an Object, return an object)패턴

## 참고

- [https://taegon.kim/archives/8058](https://taegon.kim/archives/8058)

## 명명된 인수

```js
// define
function addNewControl({
  title,
  xPosition,
  yPosition,
  width,
  height,
  drawingNow
}) { ... }

// call

addNewControl({
  title: 'Title',
  xPosition: 20,
  yPosition: 50,
  width: 100,
  height: 50,
  drawingNow: true,
});
```

- 인자의 순서가 달라도 됨
- 인자가 어떠한 것이 있는지 가시성이 좋아짐(호출시)

## 더 명료한 기본 인수값

```js
function addNewControl({
  title,
  width: w = 100, // 함수 내부에서는 w로 인자를 사용
  height: 100, // 인자값에 기본값을 설정
  xPosition,
  yPosition,
  drawingNow,
} = {}) { // 아무런 인자가 없을 때는 빈 오브젝트 할당
  // ...
}
```

## 더 많은 정보 반환

```js
const { control, showing, parent } = addNewControl({ title: 'Title', width: 300, height: 150 });
```

## 함수 합성의 용이함

```js
// 가장 왼쪽에 위치한 함수부터 param을 인자로 넣어서 오른쪽 끝까지 실행해나감
function pipe(...fns) {
  return param => fns.reduce((result, fn) => fn(result), param);
}

// 합성함수 있는 경우
const saveUser = pipe(validate, normalize, persist);
saveUser(userInfo);

// 합성함수 없는 경우
persist(normalize(validate(userInfo)));
```

- 알아 보기 쉬움
- 모든 함수가 객체를 인수로 받고 객체로 반환한다는 규칙이 있으면, 각 함수는 인자로 전달되는 객체에서 자신에게 필요한 값만 취한 다음 나머지 값은 그대로 반환할 수 있다.

```js
function validate({
  id,
  firstName,
  lastName,
  email = requiredParam(),
  username = requiredParam(),
  pass = requiredParam(),
  address,
  ...rest
}) {
  // 유효성 검사를 여기에서 함
  return {
    id,
    firstName,
    lastName,
    email,
    username,
    pass,
    address,
    ...rest
  }
}

function normalize({ email, username, ...rest }) {
  // 정규화 동작을 여기서 실행
  return {
    email,
    username,
    ...rest
  };
}

function persist({ upsert = true, ...info }) {
  return {
    operation,
    status,
    saved: info
  };
}

function saveUser(userInfo) {
  return pipe(
    validate,
    normalize,
    persist
  )(userInfo);
}
```

## 필수 인수

- 인자 기본값에 함수 실행 결과도 넣을 수 있다는 점 활용
- 바벨 컴파일러는 삼항연산자를 사용해서 인자가 주어지지 않으면 기본 값 사용
  - `width = _ref$width === undefined ? getDefaultWidth() : _ref$width`

```js
function requiredParam(param) {
  const requiredParamError = new Error(
    `Required parameter, "${param}" is missing.`
  )

  if (typeof Error.captureStackTrace === 'function') {
    Error.captureStackTrace(
      requiredParamError,
      requiredParam
    );
  }

  throw requiredParamError;
}

function addNewControl({
  title = requiredParam('title'),
  width = getDefaultWidth(),
  height = getDefaultHeight(),
  xPosition,
  yPosition,
  drawingNow,
} = {}) {
  // ...
}
```


## 결론

- 편리하나, 만능은 아님
- 필요에 따라서만 사용하도록
- 함수 실행 부하가 조금이라도 커짐
