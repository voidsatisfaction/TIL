# 리액트 네이티브 과거 버전 사용

## 동기

가끔가다가 모듈간의 호환문제로 과거 버전을 사용해야할 경우가 있다.
이번 경우에는 web-view-bridge라는 모듈을 사용할때 실제 앱과 같은 환경에서 테스트 하기 위해서

`react-native @0.38.0`을 사용하였다.

## 과거 버전 프로젝트 만들기

`react-native init $projectName --version react-native@0.38.0`