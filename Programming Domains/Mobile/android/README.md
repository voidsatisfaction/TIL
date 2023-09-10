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

### API version vs compileSdkVersion vs targetSdkVersion vs minSdkVersion

Q) 만약, compileSdkVersion이 34이고, targetSdkVersion이 33이면, 기존 코드에서 34version에서만 사용가능한 API를 도입했을 경우, 코드가 어떻게 backwardCompatible하게 동작하는가?

A) backwardCompatible하게 동작하지 않으므로, targetSdkVersion과 compileSdkVersion을 매칭시키는 것이 바람직함

- API version
  - 안드로이드 OS의 버전을 나타내는 숫자
  - e.g)
    - android10 -> API version 29
    - android11 -> API version 30
- compileSdkVersion
  - 컴파일 시 사용되는 Android API 버전
- targetSdkVersion
  - 앱이 기기에서 동작하는 런타임에 사용되는 Android API 버전
  - targetSdkVersion > OS version
    - 이 경우엔 OS 버전 베이스로 동작하게 됨
- minSdkVersion
  - 해당 앱을 구동할 수 있는 최소 커트라인
  - 플랫폼의 OS 버전이 minSdkVersion보다 낮을 경우 앱이 설치되지 않음
