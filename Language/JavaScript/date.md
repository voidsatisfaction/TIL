# Javascript의 Date오브젝트

## 기본 동작

- 브라우저
  - Date 오브젝트 자체는 브라우저 로컬 시간 기준으로 동작
  - `.toString()`, `.toLocaleString()` 둘다 브라우저 로컬 시간 기준으로 잘 동작함
- nodejs
  - Date 오브젝트 자체는 UTC 시간 기준으로 동작
  - `.toLocalString()` 계열의 메서드를 이용하면 로컬 서버시간으로 지정된(OS레벨의 / 브라우저)

```js

```

## 대안

### moment.js
