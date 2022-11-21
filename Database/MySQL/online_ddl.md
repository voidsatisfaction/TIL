# Online DDL

- 의문
- 개요
- 성능
- 한계

## 의문

- 단순 SELECT도 metadata lock이 걸리는건가?? 왜 블로킹이 되는건지

## 개요

## 성능

- 장점
  - In-place 알고리즘
    - 테이블 복사 방식의 디스크IO와 CPU사이클을 회피해서, 데이터베이스 부하를 줄여줌
    - 데이터를 테이블 복사보다 buffer pool로 덜 읽음

## 한계

- 온라인 DDL 작업이 끝나기 전에, 테이블에 metadata lock을 건 트랜잭션들이 커밋되거나 rollback되기를 기다려야 함
  - 온라인 DDL 실행이 시작되기 전에도 마찬가지
  - 온라인 DDL 실행 도중에 잠시 x-metadata lock이 테이블에 걸릴때도 있음
  - 마지막에는 항상 필요함
  - 즉, metadata lock을 거는 트랜잭션들은 온라인 DDL을 블로킹하게 함
  - 오래 실행되거나, 사용되지 않는 메타데이터 락을 잡는 트랜잭션은 online DDL의 타임아웃을 야기하기도 함
- 외래키 관계를 갖는 온라인 DDL은 다른 외래키 관계를 갖는 테이블이 커밋하거나 롤백하는것을 기다리지 않음
  - 업데이트 하는 테이블에는 X-메타데이터 락을 걸고, 또 다른 테이블에는 S-메타데이터 락을 검
    - 외래키 제약 체킹때문
  - S-메타데이터 락은 online DDL이 동작하도록 하나, 테이블 정의를 업데이트할때에는 X-메타데이터 락이 꼭 필요하다
    - 이 시나리오에서 데드락이 발생할 가능성이 존재함
- 온라인 DDL이 동작중일때, `ALTER TABLE`을 실행하는 스레드는 다른 스레드에서 실행된 DML의 online log를 적용함
  - 다만 online log에 기록된 DML을 적용할때, duplicate key error에 직면할 수 있음(unique constraint를 위반하는 레코드가 존재하면)
- `TEMPORARY TABLE`에 인덱스를 만들경우에는 copy 알고리즘을 사용
- `ALTER TABLE`절의 `LOCK=NONE`은 `ON...CASCADE`나 `ON...SET NULL`이 테이블에 있을때 허락되지 않음
- InnoDB의 *OPTIMIZE TABLE*은 `ALTER TABLE`작업에 매핑되어 테이블을 재구성하고 인덱스 통계를 업데이트하며 클러스터된 인덱스에서 사용되지 않는 공간을 확보함
  - 보조 인덱스는 기본 키에 표시된 순서대로 삽입되므로, 효율적으로 작성되지 않음
  - OPTIMIZE TABLE은 일반 InnoDB 테이블 및 파티션된 InnoDB 테이블을 재구성하기 위한 온라인 DDL이 지원됨
    - *`OPTIMIZE TABLE`을 ONLINE DDL로 실행할 수 있다는 얘기겠지?*
- table rebuilding을 야기하는 큰 테이블에서의 온라인 DDL의 한계
  - 온라인 DDL을 멈추는 방법이나 CPU 스로틀링을 하는 방법은 존재하지 않음
  - 온라인 DDL의 롤백은 매우 비싼연산이다
  - 오래 실행되는 온라인 DDL은 replication 지연을 유발하며, replica에서 실행되기 전에 원본에서 실행을 완료해야 함
    - 원본에서 동시에 처리된 DML은 복제본에 대한 DDL 작업이 완료된 후에만 복제본에서 처리됨
