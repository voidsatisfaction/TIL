# EAS

- 의문
- 개요

## 의문

## 개요

- 개요
  - app바이너리를 빌드해주는 호스팅 서비스
    - eas.json에 각종 설정을 통해서 test, staging, prod배포(프로파일링)를 할 수 있음
- 각종 빌드
  - emulator / device 빌드
    - `"developmentClient": true`
      - `expo-dev-client`를 의존함
  - app store 빌드
    - `eas build --platform android`
    - developer account가 존재해야 함
