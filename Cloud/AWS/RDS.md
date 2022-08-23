# AWS RDS

## 의문

## Aurora MySQL 튜닝

분류는 cpu, io, synchronization 이렇게 세가지로 나눔

- 대기 이벤트
  - **cpu**
    - 이 이벤트는 스레드가 CPU에서 활성 상태이거나 CPU에 대해 대기 중일 때 발생합니다.
      - 활성 연결 수가 vCPU 수보다 일관되게 높게 유지되는 경우에 인스턴스에 CPU 경합이 발생하고, cpu대기 이벤트 발생
    - 일반적인 원인
      - 분석 쿼리
      - 많은 동시 트랜잭션 수
      - 장기 실행 트랜잭션
      - 연결 수의 급격한 증가(로그인 스톰)
      - 컨텍스트 전환 증가
    - 해결
      - CPU 용량 늘리기
      - CPU를 많이 사용하는 쿼리 식별
        - 식별 이후 `CALL mysql.rds_kill(processID)` 로 연결 종료
          - 이는 긴 롤백을 트리거할 수 있음(언두로그의 정리)
        - 쿼리 최적화
          - `EXPLAIN`, `SHOW PROFILE`, `ANALYZE TABLE`
      - 읽기 전용 워크로드를 리더 노드로 리다이렉션
  - **io/aurora_redo_log_flush**
    - 이 이벤트는 세션이 Aurora 스토리지에 영구 데이터를 쓸 때 발생합니다.
    - 리두 로그를 disk에 flush할 때
  - io/aurora_respond_to_client
    - 이 이벤트는 스레드가 결과 집합을 클라이언트에 반환하기 위해 대기 중일 때 발생합니다.
      - *커널의 네트워크 시스템을 이용하기 전?*
      - *전송해야 하는 네트워크 양이 많을때 순차적 처리를 대기해야해서 그런가?*
  - io/file/innodb/innodb_data_file
    - 이 이벤트는 스토리지의 I/O 작업에 대기 중인 스레드가 있을 때 발생합니다.
  - io/socket/sql/client_connection
    - 이 이벤트는 스레드가 새 연결을 처리하는 과정에 있을 때 발생합니다.
  - **io/table/sql/handler**
    - 이 이벤트는 작업이 스토리지 엔진에 위임된 경우에 발생합니다.
  - synch/cond/mysys/my_thread_var::suspend
    - 이 이벤트는 특정 조건에서 스레드가 대기 중이어서 해당 스레드가 일시 중지되는 경우 발생합니다.
  - synch/cond/sql/MDL_context::COND_wait_status
    - 이 이벤트는 테이블 메타데이터 잠금에 대기 중인 스레드가 있는 경우 발생합니다.
  - **synch/mutex/innodb/aurora_lock_thread_slot_futex**
    - 이 이벤트는 한 세션이 업데이트에 대해 행을 잠그고 다른 세션에서 동일한 행을 업데이트하려고 하는 경우 발생합니다.
  - synch/mutex/innodb/buf_pool_mutex
    - 이 이벤트는 스레드가 메모리의 페이지에 액세스하기 위해 InnoDB 버퍼 풀에서 잠긴 경우 발생합니다.
  - synch/mutex/innodb/fil_system_mutex
    - 이 이벤트는 세션이 테이블스페이스 메모리 캐시에 액세스하기 위해 대기 중일 때 발생합니다.
  - synch/mutex/innodb/trx_sys_mutex
    - 이 이벤트는 트랜잭션 수가 많은 데이터베이스 작업이 많을 때 발생합니다.
  - synch/rwlock/innodb/hash_table_locks
    - 이 이벤트는 버퍼 캐시를 매핑하는 해시 테이블을 수정할 때 경합이 있는 경우 발생합니다.
  - synch/sxlock/innodb/hash_table_locks
    - 이 이벤트는 버퍼 풀에 없는 페이지를 파일에서 읽어야 할 때 발생합니다.
