# Uber PostgreSQL에서 MySQL로 변경한 이유

- 의문
- 기본 지식
  - PostgreSQL
    - 값의 삽입시 어떤 일이 일어나는가?
    - Replica
- PostgreSQL의 직접적 한계
  - 1] 쓰기에 비효율적인 아키텍처
  - 2] 데이터 복사가 비효율적
  - 3] 테이블 오염 문제
  - 4] Poor replica MVCC support
  - 5] 새 버전 업그레이드의 어려움
- MySQL이 더 잘하는 것
  - 1] Buffer Pool
  - 2] Connection Handling

## 의문

## 기본 지식

- PostgreSQL
  - 값의 삽입시 어떤 일이 일어나는가?
    - 개요
      - immutable row즉, 특정 행의 값을 업데이트 하면, 그 값 자체가 변하는 것이 아니고, 새로 값을 삽입하고 새 값은 이전값을 포인터로 갖음
        - MGA(Multi Generation Architecture)
          - MVCC를 구현하는 방식 중 하나
    - 문제
      - 주기적으로 VACUUM을 해줘야 함
      - 업데이트가 있을 때 마다 디스크상의 데이터 위치 변경이 일어남
        - 인덱스 변경이 필수불가결(모든 B트리 인덱스가 리프 노드에서 ctid를 갖음(MySQL에서는 프라이머리 키를 갖음))
  - Replication
    - 개요
      - WAL(Write Ahead Log)를 이용하여 마스터 노드에서 레플리카 노드로 스트리밍하여 데이터 싱크를 맞춤
    - c.f) WAL
      - 개요
        - crash recovery목적으로 만들어진, 데이터베이스의 모든 트랜잭션을 기록하는 로그
      - 특징
        - on-disk의 로우레벨까지의 정보를 포함(row ctids)
          - e.g) disk offset 8,382,491에 바이트 XYZ를 작성하라
        - 바이트 레벨까지 마스터와 정확히 일치함
- MySQL
  - Replication
    - 특징
      - 로지컬 업데이트가 가능
        - MVCC 이용 가능
        - READ 쿼리가 replication stream을 블로킹하지 않음
      - 다양한 replication mode가 존재
        - Statement-based replication
          - SQL statement 자체를 replicate
        - Row-based replication
          - 변경된 row record를 replicate
        - Mixed replication
          - 위의 두 모드를 믹스

## PostgreSQL의 한계

### 1. 쓰기에 비효율적인 아키텍처(Write Amplification)

- 개요
  - 작은 논리적 갱신이 물리 레이어에서는 훨씬 방대하고 비싼 갱신이 되는 것
- 예시
  - 특정 행의 값을 수정
    - 새 행이 추가
    - 인덱스 변경(ctid가 변경되었으므로)
      - 프라이머리 키 인덱스 변경
      - 세컨데리 키 인덱스 변경
    - 위의 모든 변경이 WAL에 반영
- 특징
  - 인덱스가 너무 많으면 오버헤드가 너무 커짐

### 2. 데이터 복사가 비효율적

- 개요
  - 앞서의 Write Amplification 문제와 이어짐
  - WAL가 수정시 모든 절차를 전부 담아버림
    - 새 행 추가 / 모든 인덱스 변경 등
  - verbose해지기 때문에, bandwidth를 너무 많이 차지해버림
    - 데이터 센터간 replication을 수행할 경우 문제가 커짐

### 3. 테이블 오염 문제

- 개요
  - PostgreSQL 9.2에서 WAL 적용이 잘못되어서, 데이터 간 eventual consistency가 맞지 않는 경우가 있었음

### 4. Poor replica MVCC support

- 개요
  - 이미 다른 열린(open) 트랜잭션에 의해서 영향을 받는 행에 대한 동작이 필요한경우, WAL을 이용한 replica는 해당 트랜잭션이 끝날 때 까지 대기
    - replica가 너무 오래 블록되면, Postgres가 해당 트랜잭션을 kill함
  - replica는 마스터 노드와 데이터의 지연이 생길 가능성이 있음

### 5. 새 버전 업그레이드의 어려움

- 개요
  - Replication이 physical level로 행해지기 때문에, Postgres9.3은 동작하는 Postgres9.2버전의 replica에 replicate불가능
    - DB클러스터 전체가 버전을 업그레이드 해야 함

## MySQL이 더 잘하는 것

### Buffer Pool

- MySQL
  - InnoDB 버퍼 풀
    - 특징
      - 커스텀 LRU 디자인 사용 가능
        - LRU를 날려버리는 악의적인 접근을 자체적으로 막을 수 있음
      - 유저 스페이스에서 관리
        - user/kernel 컨텍스트 스위칭이 발생하지 않음
- Postgres
  - OS 페이지 캐시 사용
    - 특징
      - 시스템 콜로 데이터를 읽어야 함(유저 스페이스의 프로세스와 커널사이의 컨텍스트 스위칭이 필요)

### Connection Handling

- MySQL
  - 커넥션 당 스레드
  - 1만 커넥션도 문제없음
- Postgres
  - 커넥션 당 프로세스
    - 스레드 보다 오버헤드 있음
  - 수백개의 active 커넥션에서 문제가 생김
    - pgbouncer를 사용해야함
    - 또 다른 버그가 있음
      - idle in transaction
