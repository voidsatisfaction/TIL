# NextJS

- 의문
- 개요

## 의문

## 개요

## App Routing

![](./images/nextjs/component_hierarchy1.png)

- 파일 컨벤션
  - **layout**
    - children과 공유되는 UI 세그먼트
  - **page**
    - 하나의 라우트에 유니크한 UI
    - public하게 접근 가능
  - loading
    - children과 공유되는 loading UI
  - not-found
    - children과 공유되는 not found UI
  - error
    - children과 공유되는 error UI
  - global-error
    - global error UI
  - route
    - _Server-side API 엔드포인트_
      - 무슨 의미인가?
  - template
    - _?_
  - default
    - _Parallel Routes의 fallback UI_
- 위의 파일들은 렌더링 순서가 다름
