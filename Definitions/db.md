# DB

- 의문
- General
  - Transaction
  - Isolation level
    - Read uncommitted
    - Read committed
    - Repeatable read
    - Serializable
  - Connection pool
  - MySQL vs PostgreSQL vs SQLite
  - MVCC
  - MVCC와 lock의 관계
  - DML vs DDL vs DCL

## 의문

## General

### Transaction

- 정의
  - **information processing s.t. indivisible individual operation**
  - information processing s.t. ACID조건을 만족
- 특징
  - 각 transaction은 success or fail(Atomicity)
    - partially complete는 없음
  - data-oriented resources는 transactional unit속의 모든 operation이 성공적으로 끝나야만, 영구적으로 변경 사항이 반영됨(Durability)
  - 애플리케이션을 reliable하게 만드는 효과가 있음
  - programming model을 simplify하기 위해서 사용됨
    - ignore partial error
- ACID 기준
  - **Atomicity**
    - transaction은 더 이상 분리가 불가능(원자)
      - 부분 성공(x), 모든 것이 일어났거나 아무것도 일어나지 않거나
  - **Consistency**
    - DB상의 불변량이 항상 참이 되도록 하는 것
      - e.g
        - 회계 시스템에서 credits와 debits는 항상 밸런스가 맞아야 함
        - constraints, cascades, triggers 에 대해서 새로 삽입하는 데이터는 항상 valid해야 함
      - DB에서 걸 수 있는 제한만으로는 달성하기 힘듬
      - 엄밀히 말하면 ACID에서 C는 빠져야 함(DB 자체에만 의존하는게 아니므로)
    - Application의 영역
      - Atomicity, Isolation, Durability는 DB의 영역
    - A transaction is a correct transformation of the state.
    - The actions taken as a group do not violate any of the integrity constraints associated with the state.
    - *구체적으로 무엇인지?*
  - **Isolation**
    - 하나의 transaction은 다른 transaction에 영향을 주지 않음
      - transaction은 내부 구현적으로는 concurrent하지만, 논리적으로는 순차적으로(serial) 실행되는 것 처럼 보임(**serializability**)
      - 성능이슈로 인하여 이 부분의 조건을 유연하게 설정 가능함
    - 다수의 DB client들이 하나의 row에 접근할 때 문제가 생기는 것을 방지(논리적으로 순차적으로 실행되는 것 처럼 보이므로)
      - race conditions
      - e.g)
        - 게시판 글의 뷰 수를 증가시키는 경우
    - DB는 isolation level을 갖음
      - `1. READ UNCOMMITED`
        - 개요
          - 다른 transaction에서 COMMIT 되지 않은 데이터를 읽어올 수 있음(dirty read)
        - 문제
          - INSERT만 진행되고, ROLLBACK될 수 있는, 한 번도 COMMIT되지 않은 데이터를 읽을 수 있음
      - `2. READ COMMITTED`
        - 개요
          - COMMIT이 완료된 데이터만 SELECT시에 보이는 수준을 보장하는 Level
        - 문제
          - 하나의 트랜잭션 안에서, SELECT를 수행 할 때마다 데이터가 동일하다는 보장을 해주지 못함(다른 트랜젝션에서 해당 데이터를 COMMIT했을 경우, COMMIT된 데이터를 반환하므로)
          - Non-repeatable Read
            - A non-repeatable read occurs when, during the course of a transaction, a row is retrieved twice and **the values within the row** differ between reads.
              - **행의 값이 변경되는 경우**
          - Phantom Read
      - `3. REPEATABLE READ`
        - 개요
          - 한 트랜잭션 안에서 반복해서 SELECT를 수행해도 읽어 들이는 값이 변화하지 않음
            - 처음으로 SELECT를 수행한 시간을 기록한 뒤, 그 이후에는 모든 SELECT마다 해당 시점을 기준으로 Consistent Read를 수행(스냅샷을 읽음)
              - 나중에 SELECT했을 때, 정합성 보장
            - UPDATE한 데이터 정합성 보장
              - INSERT/DELETE는 보장하지 않음(중간에 시행 된 경우)
        - 문제
          - Phantom Read
            - A phantom read occurs when, in the course of a transaction, **new rows are added or removed by another transaction** to the records being read.
              - **행 자체가 추가 / 제거**
            - e.g) 하나의 트랜잭션안에서 두 range query중간에 다른 트랜잭션의 insert가 존재하는 경우
      - `4. SERIALIZABLE`
        - 개요
          - 가장 높은 고립수준
          - Phantom read 방지
          - 성능 이슈로 거의 사용 안됨
        - 문제
          - DEADLOCK이 생길 수 있음
    - c.f) Consistent Read
      - 개요
        - SELECT 연산을 수행할 때, 현재의 DB의 값이 아닌, 특정 시점의 DB snapshot을 읽어오는 것
    - c.f) Lock
      - S(Shared) Lock
        - 개요
          - 자원을 다른 사용자가 동시에 읽을 수 있지만, 변경은 불가능하게 함
        - SQL
          - `SELECT ... FOR SHARE`
      - X(Exclusive) Lock
        - 개요
          - 해당 락이 걸리면, 해당 트랜잭션이 완료될 때 까지 해당 테이블 혹은 레코드를 다른 트랜잭션에서 읽거나 쓰지 못하게 함
        - SQL
          - `SELECT ... FOR UPDATE/DELTE`
  - **Durability**
    - transaction이 성공적으로 commit되면, 해당 변화는 DBMS failure에도 변함이 없음
      - hardware fault, database crash가 발생해도
    - 종류
      - single-node db의 경우
        - disk가 corrupt되어도 회복할 수 있는 것
      - repliocated db의 경우
        - data가 다른 노드들에게 성공적으로 복사된 다음에 transaction이 성공적으로 commit되었다고 보고하는 것
    - 완벽한 durability는 존재하지 않음
      - 모든 하드디스크와 모든 백업이 전부 망가지면 답이없음
      - 경우의 수
        - 데이터를 disk에 작성하는데, 머신이 죽음 => 데이터는 잃지 않으나, 회복할 때 까지 접근 불가능(복제된 시스템은 사용 가능)
        - correlated fault(전원이 나가거나, 특정 input에 의한 모든 노드가 크래시되는 경우) => 모든 replicas를 한번에 죽일 수 있음, 메모리에 있는 데이터도 다 날라감
        - 비동기 replicated system의 경우, leader가 사용 불가능 해짐 => 최신 데이터 작성은 잃어버릴 가능성 존재
        - 하드웨어 전원이 갑자기 꺼짐 => SSD의 경우 *`fsync`* 가 제대로 동작하지 않을 수 있음
        - storage engine과 filesystem 구현 사이의 사소한 상호작용이 트래킹이 힘든 버그를 생성할 수 있으며, 디스크의 파일을 오염시킬 수 있음
          - *구체적인 예시?*
        - 디스크에 있는 데이터가 점진적으로 아무런 detecting없이 corrupt되는 경우가 존재함
          - historical backup으로 다시 회복시켜야 함
        - SSD의 경우에는 30% ~ 80%의 드라이브가 첫 사용 4년동안 적어도 하나의 bad block을 생성한다고 함. 하드디스크는 bad sector의 비율은 낮으나, 전체적인 failure가 발생할 확률이 높음
- 방법론
  - **Rollback**
    - db integrity를 중간 상태를 저장하면서 확보함
    - 이러한 중간 상태를 활용해서 원래 상태로 복원
    - 수정 이전의 데이터 이미지의 상태를 저장
    - transaction 도중에 실패하는 경우, 원래 이미지를 이용하여 롤백함
  - **Rollforward**
    - DB는 transaction log(journal)를 저장 -> DBMS의 failure -> Rollback을 사용한 기존 이미지 복원 -> transaction log(journal)에 기록된 최신 transaction을 기반으로 해당 연산 다시 실행 -> DBMS failure당시 실행되었던 transaction까지 반영된 consistent db 생성
  - **Deadlocks**
    - 두 transaction이 DB의 같은 부분에 접근 할 경우, 발생할 가능성
    - Transaction processing system에서는 이러한 deadlock을 탐지하고, 두 transaction을 cancel후 rollback후 다시 진행시킴
      - 혹은, 하나만 cancel시키고 나머지는 잠시 뒤에 다시 시작하도록 함
  - **Compensating transaction**
    - commit and rollback 매커니즘이 사용불가능하거나, 좋지 못한 선택지일 경우, 실패한 transaction을 undo하고 시스템을 이전 상태로 restore하는 것

### Isolation level

PostgreSQL 기반

#### Read uncommitted

#### Read committed

- 개요
  - 한 transaction에서의 SELECT 쿼리는, **쿼리가 시작하기 전** 의 데이터만 볼 수 있음
    - uncommitted data / concurrent transaction에 의해 **쿼리 실행중** 에 commit된 변화는 결코 볼 수 없음
      - MVCC의 MGA를 생각해보면 자명
  - 자신의 transaction에서 커밋되지 않은 update의 결과는 볼 수 있음
  - 한 transaction에서의 연속된 select 쿼리는 서로 다른 결과를 볼 수 있음
    - 두번째 select전에 다른 transaction에서 변화를 commit하는 경우
- 케이스 스터디
  - `SELECT`이외의 경우
    - `UPDATE`, `DELETE`, `SELECT FOR UPDATE`, `SELECT FOR SHARE` 커맨드도 타겟 행을 찾을때, SELECT와 같은 동작을 함
      - concurrent한 transaction에 의해서, 삭제되거나 수정되는 경우가 있음
        - 그러한 경우, 해당 transaction을 기다림
      - 시나리오
        - concurrent한 transaction이 롤백되는 경우
          - 처음 찾은 row로 자신의 transaction을 실행
        - concurrent한 transaction이 커밋되는 경우
          - row가 삭제된 경우
            - 자신의 transaction 무시
          - 그 외
            - **처음 찾은 row중에서** , 서치 조건(WHERE)이 재평가되어서 이전 transaction의 커밋 후에도 서치 조건이 만족하는지 확인하여 그렇다면 진행
  - `INSERT ... ON CONFLICT DO UPDATE`
    - insert 혹은 update는 보장
    - concurrent한 transaction에 의해서 insert에서 conflict가 나면, update가 동작함
      - MGA에서 해당 version이 보이지 않아도 시행됨(내부적으로 그렇게 구현했나 봄)
- 장점
  - 빠르고 사용하기 간편함
- 단점
  - 모든 케이스를 다 제대로 다룰 수 있는것은 아님

문제가 생기는 경우

```sql
-- website 테이블에 website.hits의 값이 9 or 10인 데이터가 들어있다고 가정

BEGIN;
UPDATE website SET hits = hits + 1;
-- run from another session:  DELETE FROM website WHERE hits = 10;
COMMIT;
```

- 문제
  - 위의 경우, concurrent transaction의 DELETE가 동작하지 않을 수 있음
- 원인
  - pre-update hits값 9인 row는 스킵됨
  - 대상은 update이전에 hits값 10인 row는 delete의 대상이 되었다가, update쿼리가 끝나고나서, where조건을 다시 평가받을때, 이미 값이 11이 되므로 대상에서 제외

#### Repeatable read

- 개요
  - **한 트랜젝션이 시작하기 전** 의 커밋된 데이터만 볼 수 있음
    - 커밋 되지 않은 데이터나, concurrent transaction에 의한 커밋의 수정도 볼 수 없음
  - 자신의 transaction에서 transaction내의 커밋되지 않은 update의 결과는 볼 수 있음
  - serialization failure에 의한, retry transaction에 준비되어야만 함
- 케이스 스터디
  - `UPDATE`, `DELETE`, `SELECT FOR UPDATE`, `SELECT FOR SHARE`역시 행을 찾을 때, `SELECT`와 같은 동작을 함
    - 트랜젝션 시작하기전까지 커밋된 데이터를 탐색
    - 다른 concurrent transaction에 의해서 이미 업데이트 되었거나, 삭제되었을 수 있음
  - 시나리오
    - concurrent transaction이 rollback된 경우
      - 처음 찾은 row로 update 수행
    - concurrent transaction이 commit된 경우
      - 현재 transaction이 serialization failure 에러와 함께 롤백
- 특징
  - updating 트랜젝션만 재시도 되고, read-only 트랜젝션은 충돌이 일어나지 않음
  - 각 트랜젝션은 데이터베이스의 stable view를 항상 보지만, concurrent transaction들이 순차적으로 실행되는것과는 다름
- 구현
  - 스냅샷 isolation
    - 전통적인 locking방식보다 성능이 더 좋음

#### Serializable

- 개요
  - 가장 엄격한 transaction isolation
  - **transaction이 실제로는 concurrent하지만, 전부 serial하게 실행되는 것 처럼 에뮬레이트 함**
  - 반드시 serialization failure에 대비해야 함
  - repeatable read와 동일하나, serializable transaction의 concurrent set의 inconsistency를 모니터링 해야함
    - 모니터링은 블로킹은 하지 않으나, 오버헤드가 존재
    - serialization anomaly의 조건 탐색
- 구현
  - predicate locking
    - concurrent transaction으로부터 이전의 읽은 결과에 쓰기가 영향을 끼치는지 확인하기 위한 lock
    - blocking하지 않으므로, deadlock을 일으키지 않음
      - *그럼 어떻게 구현된거길래?*

```sql
-- initial state
-- class | value
-- -------+-------
--     1 |    10
--     1 |    20
--     2 |   100
--     2 |   200

-- A
BEGIN
SELECT SUM(value) FROM mytab WHERE class = 1;
-- 그 다음에 class = 2인 row를 insert
END

-- B
BEGIN
SELECT SUM(value) FROM mytab WHERE class = 2;
-- 그 다음에 class = 1인 row를 insert
END
```

- 문제
  - 위의 경우, 둘중의 하나의 transaction만 commit되고 나머지는 rollback됨
- 원인
  - concurrent 하게 A, B transaction이 실행되는 경우, SELECT의 sum에서 서로 각각 30, 300이라는 inconsistent한 결과가 나오게 됨
    - REPEATABLE READ의 구현을 그대로 따르기 때문에(snapshot)

### Connection pool

- 정의
  - 데이터 베이스와의 연결을 유지하여, 재활용할 수 있게 한 데이터베이스 연결의 캐시
    - 성능향상(커넥션 재활용)
    - 그런데 커넥션을 매번 생성하는게 그렇게 까지 비싼 연산인가?
      - PostgreSQL의 경우, 매 커넥션마다 process를 fork하므로 나름 비싸다고 할 수 있겠다
      - 단순히 fork뿐 아니라, TCP커넥션과 TLS와 login을 매번 해야하므로, 레이턴시가 발생한다

### MySQL vs PostgreSQL vs SQLite

- MySQL
  - 모토
    - The most popular Open Source SQL DBMS supported by Oracle Corporation
  - 서버
    - 멀티 스레드
  - 기능
    - JOIN
      - optimized nested-loop join
    - Isolation level
      - repeatable read
    - Case insensitive
  - 장점
    - read가 많은 경우에 빠름
  - 단점
    - 데이터 write와 concurrency문제가 중요한 경우에는 좋지 못함
- PostgreSQL
  - 모토
    - The world's most advanced open source relational database
  - 서버
    - 멀티 프로세스
  - 기능
    - JOIN
      - nested-loop join, sort merge join, hash join
        - *각 JOIN 방식은 query optimizer가 알아서 선택해주는것인가?*
    - Isolation level
      - read committed
    - Case sensitive
  - 장점
    - 데이터 무결성이 중요할 경우 적절함
      - MVCC(Multi Version Concurrency Control)
    - SQL표준을 최대한 준수하려 함
    - 지도, 기하 관련 데이터 타입
    - complex query에 빠름
  - 단점
    - 속도를 희생하여 확장성과 호환성을 염두함(읽기 작업)
- SQLite
  - 모토
    - Most widely deployed and used (embedded) database engine
      - mobile DB
  - 서버
    - in-process (client-server 모델이 아님)
  - 기능
    - self-contained
      - 외부 라이브러리 사용하지 않음
      - 다양한 OS에서 동작
    - serverless
      - 직접 파일을 읽고 씀
    - zero-configuration
    - transactional
    - SQLite의 가용 메모리가 많을수록 더 빠름
      - 작은 메모리 환경에서도 꽤나 괜찮음
      - direct file I/O보다 빠를 수 있음
  - 장점
    - 크로스 플랫폼 하나의 디스크 파일
      - `fopen()`의 대체재
    - reliable
      - millions of test cases
        - 100% 커버리지
    - 시스템 크래시나, 파워가 갑자기 나가도 트랜잭션 ACID유지
      - *어떻게?*
    - 오픈소스지만, SQLite만 풀타임으로 전담하는 팀이 존재
    - 2050년까지 서비스할 계획
  - 단점
- 공통점
  - RDB
    - physical files
    - logical model
      - databases, tables, views, rows, columns
  - Open Source

### MVCC

MVCC, MGA(Multi Generation Architecture) example

![](./images/db/mvcc_mga1.png)

MVCC, Rollback Segment example

![](./images/db/mvcc_rollback_segment1.png)

- 정의
  - 동시성을 제어하기 위해 사용하는 핵심적인 방법 중 하나
    - readers never block writers, and writers never block readers
- 구현 방식
  - 1 MGA(Multi Generation Architecture)
    - 개요
      - 튜플을 업데이트 할 때, 동일한 데이터 페이지 내에서 새로운 튜플을 추가하고, 이전 튜플은 유효범위를 마킹해 처리
    - e.g)
      - PostgreSQL
  - 2 Rollback(Undo) segment
    - 개요
      - 튜플을 업데이트 할 때, 새로운 버전의 데이터를 기존 데이터 블록에서 변경하고, 이전 버전을 별도의 롤백 세그먼트에 보관
        - select SCN(System Change Number(데이터베이스 내부의 타임스탬프 같은것))과 데이터 블록의 SCN을 비교해 Consistent Read가 필요하다고 판단되면, 롤백 세그먼트의 이전 버전을 읽어서 버퍼 캐시에 CR(Consistent Read)블록을 생성
          - *쿼리를 파싱해서 판단하는 것인가?*
          - *애초에 CR블록은 매번 update할때마다 생기고 지워지기는 하는건가?*
    - 목적
      - **읽기 일관성**
        - 트랜잭션이 수행되고 있을 때, 데이터베이스의 다른 사용자는 이 트랜잭션이 커밋하지 않은 변경된 데이터를 볼 수 없음
        - SELECT문이 실행된 시점에서는 그 이전에 커밋된 데이터 까지의 정보만을 볼 수 있음
          - SELECT문 수행도중 다른 사용자에 의해 변경된 데이터는 볼 수 없음
      - **트랜잭션 롤백**
        - 트랜잭션을 롤백되는 경우에 다시 데이터값을 행으로 옮겨서 원래의 값으로 복원
      - **트랜잭션 복구**
        - 트랜잭션이 수행되고 있을 때, 인스턴스가 비정상적으로 종료하면, 커밋되지 않은 변경사항을 롤백해야 함
    - e.g)
      - MSSQL
      - MySQL
- 장점
  - lock을 사용하지 않으므로, 일반적인 RDBMS보다 매우 빠르게 동작
  - 데이터를 읽기 시작할 때, 다른 사람이 그 데이터를 삭제하거나 수정하더라도 영향을 받지 않음
  - READ COMMITTED, REPEATABLE READ 둘다 가능하게 함
- 단점
  - 하나의 데이터에 대해 여러 버전의 데이터를 허용하므로, 데이터 정리 시스템 필요
    - undo 영역
  - 데이터 버전이 충돌될 수 있음
    - *예시?*

### MVCC와 lock의 관계

- MVCC
  - 읽기 일관성을 위함
    - 하나의 트랜잭션이 일정한 기준으로 데이터의 스냅샷을 보기 위함
- lock
  - 동시성을 제어하기 위함
    - e.g) UPDATE 쿼리 실행시, 락을 해서 공통자원에 대하여 concurrent한 접근을 막음

### DML vs DDL vs DCL

- DML(Data Manipulation Language)
  - 정의
    - `INSERT`, `UPDATE`, `DELETE`, `SELECT ... FOR UPDATE`를 실행하는 SQL문
  - 특징
    - InnoDB 테이블에서는 트랜잭션 컨택스트안에서 동작함
      - commit, rollback 가능
- DDL(Data Definition Language)
  - 정의
    - 테이블의 행이 아니라, 데이터베이스 자체를 조작하는 SQL문
  - 특징
    - 자동적으로 commit되고, rollback 불가능
  - 예시
    - `CREATE`, `ALTER`, `DROP`, `TRUNCATE`
- DCL(Data Control Language)
  - 정의
    - 권한을 조작하는 SQL문
  - 예시
    - `GRANT`, `REVOKE`
