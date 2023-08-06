# 안드로이드

- 의문
- 개요

## 의문

## 개요

- Activity
  - 개요
    - 안드로이드 앱에서 하나의 화면을 나타냄
- Fragment
  - 개요
    - 하나의 activity안에서 독립적으로 관리되는 UI fragment
    - activity내에서 화면을 구성하는 작은 모듈
- Lifecycle Listener
  - 개요
    - 앱의 activity나 fragment등의 수명 주기 이벤트를 감지하고 처리하는 인터페이스 또는 콜백 메서드들
  - 종류
    - `onCreate()`
      - activity나 fragment가 생성될 때 호출
    - `onStart()`
      - ...가 사용자에게 보여지기 시작할 때 호출
        - 상호작용을 하지 않고, 보여질 때 호출
    - `onResume()`
      - ...가 사용자와 상호작용할 수 있을때 호출
    - `onPause()`
      - ...가 다른 ...에 의해 가려질 때 호출
    - `onStop()`
      - ...가 더 이상 사용자에게 보여지지 않을때 호출
        - activity가 다른 activity로 전환되거나, 앱이 홈버튼을 통해 미리보기로 들어갈 때 해당됨
    - `onDestroy()`
      - ...가 소멸될 때 호출
