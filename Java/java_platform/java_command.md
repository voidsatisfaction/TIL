# JAVA command

- 의문
- 개요
  - 시스템 프로퍼티 vs 환경 변수

## 의문

## 개요

### 시스템 프로퍼티 vs 환경 변수

- 시스템 프로퍼티
  - 개요
    - 자바 프로그램을 실행할 때, 해당 프로그램만 접근할 수 있도록 하는 설정값
      - 자바 커맨드라인에서 `java -Dpropname=value` 형태의 문법으로 사용됨
      - e.g) `-Delastic.apm.service_name=gryphon-{{ template "self.name" . }} -Delastic.apm.server_urls={{ .Values.elasticApm.serverUrl }}`
  - 특징
    - 가져오기
      - `System.getProperties().load()`
      - `System.getProperty(String key)`
    - 설정하기
      - `System.setProperty(String key, String value)`
- 환경 변수
  - 개요
    - 특정 OS레벨에서 모든 프로그램이 immutable하게 접근할 수 있도록 하는 설정값
  - 특징
    - 가져오기
      - `System.getenv(String name)`
