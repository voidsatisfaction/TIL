# Software Development

- 의문
- General
  - Sandbox

## 의문

## General

### Sandbox

- 정의
  - production 환경이나 리포지토리와는 격리된 테스팅 환경
    - live service와 그 데이터를 보호
  - untested, untrusted 프로세스를 호스트 자원과 격리하는 보안 기법
    - guest 프로그램에게 타이트한 자원의 집합만을 제공
    - virtualization과 연계되는 경우가 많음
    - 예시
      - Online judge
      - JVM의 sandbox
        - untrusted code의 액션을 제한함
- 특징
  - sandbox는 여러 의미로 사용될 수 있음
    - working directory
    - test server
    - development server
  - 웹 서비스 개발
    - production 환경의 미러링
