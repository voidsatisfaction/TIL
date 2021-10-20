# Real MySQL 8.0

- 의문
- Ch1. 소개
- Ch2. 설치와 설정
  - MySQL 서버 업그레이드
  - 서버 설정

## 의문

- 데이터 딕셔너리란(시스템 카탈로그)?
  - MySQL의 Information Schema, DB속의 데이터의 메타 데이터
  - 특징
    - 읽기전용
  - 구성
    - TABLES
      - 테이블에 대한 정보
    - TRIGGERS
      - 트리거에 대한 정보
    - USER_PRIVILEGES
      - 유저 권한
    - ...

## Ch1. 소개

- DB고르는 기준
  - 안정성
  - 성능 / 기능
  - 커뮤니티나 인지도
- MySQL 특징
  - 오픈 코어 모델
    - 엔터프라이즈 에디션
      - 특정 부가 기능들만 엔터프라이즈 버전에 포함됨
    - 커뮤니티 에디션

## Ch2. 설치와 설정

### MySQL 서버 업그레이드

- In-Place Upgrade
  - 개요
    - MySQL 서버의 데이터 파일을 그대로 두고 업그레이드를 하는 방법
  - 장점
    - 시간이 별로 안걸림
  - 단점
    - 여러 가지 제약사항이 존재
      - 마이너 버전 간 업그레이드는 건너뛰어서 업그레이드 가능
      - 메이저 버전 간 업그레이드는 데이터 파일의 패치가 필요
        - e.g) MySQL 5.1 -> MySQL 5.5 -> MySQL 5.6 -> MySQL 5.7 -> MySQL 8.0
      - 메이저 버전 업그레이드가 특정 마이너 버전에서만 가능한 경우도 존재
        - GA(서버의 안정성이 확인된 버전) 버전은 지나서 15 ~ 20번 이상의 마이너 버전을 선택
- Logical Upgrade
  - 개요
    - mysqldump 도구 등을 이용해 MySQL 서버의 데이터를 SQL 문장이나 텍스트 파일로 덤프한 후, 새로 업그레이드 된 버전의 MySQL 서버에서 덤프된 데이터를 적재하는 방법
  - 장점
    - 버전간 제약 사항이 거의 없음
  - 단점
    - 시간이 매우 오래걸림

### 서버 설정

my.cnf의 예시

```
/* 각 프로그램 */
[mysqld]
socket = /usr/local/mysql/tmp/mysql.sock
port = 3306

/* 각 프로그램 */
[mysqldump]
default-character-set = utf8mb4
socket = /usr/local/mysql/tmp/mysql.sock
port = 3305
```

- `my.cnf`
  - 개요
    - 설정 파일
    - 어느 디렉터리에서 읽는지는 `mysql --help`로 확인
    - 시스템 변수로 저장
  - 예시
- 시스템 변수
  - `SHOW GLOBAL VARIABLES;`
  - Var Scope
    - 시스템 변수의 적용 범위
      - Global
        - 전역
        - e.g)
          - innodb_buffer_pool_size
          - key_buffer_size
      - Session
        - 서버와 클라이언트 간의 하나의 커넥션
        - e.g)
          - autocommit
      - Both
        - my.cnf에 명시해 초기화가 가능한 변수이고, MySQL 서버가 기억만 해두고, 클라이언트와의 커넥션이 생성되는 순간에 해당 커넥션의 기본값으로 사용
        - 글로벌 시스템 변수의 값을 바꿔도, 이미 존재하는 세션 변숫값은 변경되지 않고 유지
  - Static Var vs Dynamic Var
    - Static Var
      - 서버가 재시작될때만 변경될 수 있는 변수
      - `my.cnf`파일에 정의된 케이스가 많은 변수
        - 실행되고 나면 변경해도 반영이 안됨
    - Dynamic Var
      - 시스템 변수를 `SET`을 이용해서 변수 값을 바꿀 수 있음
      - `SET PERSIST max_connections=5000;`
        - dynamic하게 변수의 값을 바꾸고, 파일에도 적용 가능(별도의 파일이 생기고, 그걸 재부팅할때 읽어서 적용)
        - 세션 변수에는 적용되지 않음
      - `RESET PERSIST IF EXISTS max_connections;`
        - PERSIST로 설정한 변수 삭제
