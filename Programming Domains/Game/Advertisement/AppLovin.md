# App Lovin

## 의문

## 개요

- 광고 플랫폼

## 라인업

### Ad Review

- 개요
  - 광고에 관련된 UX를 관리하는 기능
- 기능
  - 광고 컨텐츠의 자동 탐지
    - 광고 컨텐츠 필터링 가능(성인, 폭력, 정치적, 도박 등)
  - 광고 모니터링 기능
    - 광고주, creative ID, 위치 파악 가능
  - 문제 광고 신고 기능

### Mediation

- 개요
  - MAX이외의 다른 애드네트워크를 연결하고 각 광고를 비교하여 가장 매출이 많이 나오도록 지면과 광고주를 이어주는 작업
- 작업 순서
  - mediated network의 계정 생성및, 앱 생성 및 광고 생성
  - 광고와 관련된 정보(앱ID, 광고 키)를 MAX플랫폼 ad units에 등록하기
  - unity의 sdk를 붙이기
    - 이 부분에서 gradle등으로 꽤나 고생을 할 수 있음
- 디버거
  - MAX이외의 adnetwork를 붙인 이후에, 정말로 광고가 잘 나오는지 확인하기 위한 디버거
    - https://dash.applovin.com/documentation/mediation/unity/testing-networks/mediation-debugger#within-the-app
