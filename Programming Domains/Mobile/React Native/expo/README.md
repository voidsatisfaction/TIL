# Expo

- 의문
- 개요
  - 툴
- 용어

## 의문

## 개요

### 툴

- Expo CLI
  - 프로젝트를 개발하고 배포하기 위한 CLI툴
- Expo Go
  - Android, iOS 플랫폼에서 프로젝트를 열기위한 모바일 클라이언트 앱
    - 로컬에서 빌드하지 않아도, 직접 앱을 테스트 기기에서 사용가능하게 함
    - EAS Update로 publish하면 다른 구성원들과 프로젝트를 공유하고 실행 가능
  - Manifest
    - Manifest 파일을 expo dev server가 반환하고, 내부의 bundleUrl 필드에 있는 프로젝트 스크립트 코드 url을 이용해서 다운로드 받음
    - 다운 받은 코드는 js engine으로 실행

## 용어

- Expo Config
  - `app.json`, `app.config.json`, `app.config.js`, `app.config.ts`인 파일
  - Expo cli 관련 설정 & EAS update시에 프로젝트 manifest를 생성
  - Expo config plugin과 `npx expo prebuild`가 네이티브 코드를 어떻게 생성하는지 내용 포함