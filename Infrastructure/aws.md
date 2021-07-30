# AWS

- 의문
- 종류
  - AWS Lambda
  - AWS DynamoDB

## 의문

## 종류

- AWS Lambda
- AWS DynamoDB

### AWS Lambda

- 개요
  - 서버리스 컴퓨팅 서비스
    - 서버를 신경쓰지 않아도 서비스할 수 있게 만드는 기술
- 동작 원리
  - 코드, 컨테이너 이미지 업로드 -> 컴퓨팅 자원 할당 -> request / event기반 요청 처리
- 특징
  - 외부 앱에서 직접 코드 실행 가능
  - AWS 서비스에서 코드 자동 트리거 가능
- 장점
  - 인프라 관리가 필요 없음(애플리케이션 코드에 집중 가능)
  - 자동 스케일 아웃
  - 비용 최적화
    - 컴퓨팅 시간, 호출 횟수에만 비용 지불
  - 일관된 성능
- 단점
  - DB connection pool을 사용하려면, RDS proxy라는 것을 이용해야 함
  - 디버깅이 힘듬
- 시나리오
  - 애플리케이션 개발자 두명이라는 극히 제한된 개발 자원
  - 코드와 비즈니스로직에만 집중

### AWS DynamoDB

- 개요
  - 키-값 및 문서 데이터베이스
- 장점
  - 키-값 및 문서 데이터 모델
    - 유연한 스키마를 가져서, 비즈니스 요구사항이 변경되면 테이블 쉽게 조정 가능
  - 일관된 큰 규모를 지원하는 성능
    - 10ms 미만의 응답시간
    - 인메모리 캐시
  - 서버리스
    - 오토스케일링
  - 엔터프라이즈에 사용 가능
    - ACID 트랜잭션 지원
    - 데이터 암호화
    - 특정 시점 복구 가능
- 사례
  - 광고 기술
    - 사용자 이벤트, 클릭스트림
  - 게임
    - 플레이어 데이터
    - 세션 기록
    - 순위표

#### Core Components

- Tables, Items, Attributes
  - table
    - item의 collection
  - item
    - attribute의 collection
    - 한 테이블의 item개수 제한 없음
  - attribute
- Keys
  - Primary key
    - 개요
      - 테이블에서 하나의 아이템을 특정하기 위한 키
        - 이것은 반드시 미리 정해줘야 함(schema)
    - 종류
      - Partition key
        - 하나의 attribute로 구성
        - 내부 해시 함수에 해당 키의 값을 넣어서, 물리 저장장치의 파티션을 결정
      - Partition key and sort key(composite primary key)
        - 두개의 attribute로 구성
        - 파티션 키의 값을 해시 함수에 넣어서 파티션을 결정 + 소트키 값으로 정렬
  - secondary indexes
    - 개요
      - alternate key를 이용하여, query할 수 있도록 함
    - 종류
      - Global secondary index
        - table의 partition key, sort key와는 다른 인덱스
      - Local secondary index
        - table의 partition key와는 같으나, sort key와는 다른 인덱스
- DynamoDB Streams
  - 개요
    - table의 data modification event를 수집하는 스트림
      - order, in near-real time
    - aws lambda와 연결 가능
