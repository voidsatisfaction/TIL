# 서버 장애문서

- DB
  - online ddl시, 메타데이터 락으로 인한 서비스 다운 이슈
  - foreign key 제약 추가시 table level lock으로 인한 서비스 다운 이슈

## DB

- 1 online ddl시, 메타데이터 락으로 인한 서비스 다운 이슈
- 2 foreign key 제약 추가시 table level lock으로 인한 서비스 다운 이슈

### online ddl시, 메타데이터 락으로 인한 서비스 다운 이슈

- 현상
  - 2022-11-14 15:56 ~ 16:01 Online ddl을 실행하는 동안 rideReservation관련 쿼리가 동작하지 않는 문제가 발생하였습니다.
  - AWS performance insights를 보아하니 rideReservation 테이블에 인덱스를 추가하는 DDL쿼리가 Meta Data Lock(MDL)에 걸려있었습니다.
  - 그리고 해당 online DDL쿼리가 MDL로 인해서 waiting함으로 인하여 다른 rideReservation 테이블을 조회하는 쿼리들도 전부 blocking되어있었습니다.
- 대응
  - 원래는 쿼리를 kill했어야 하는데, ddl 쿼리가 알아서 끝나서 문제는 일단락되었습니다
    - *사실 애초에 왜 ddl쿼리가 알아서 끝났는지 원인이 불명입니다*
- 원인
  - 다음과 같은 사항이 원인이라고 추정됨
  - tx1에서 rideReservation에 대한 plain 혹은 S-lock select를 실행
  - tx2(liquibase)에서 rideReservation에 인덱스를 추가
  - tx3에서 다른 어떠한 테이블에 s-lock이나 x-lock을 걸음
  - tx1에서 tx3이 락을 건 다른 테이블에 s-lock이나 x-lock을 걸어서 뭔가를 행하려고 했는데, tx3이 이미 락을 가지고 있으므로 waiting
  - tx3에서 rideReservation에 대한 plain select나 s-lock이나 x-lock을 걸어서 뭔가 하려고 했는데, tx2에 의해서 rideReservation에 어떠한 조작을 가할 수 없지만 데드락은 아닌 상태가 됨
  - tx1, tx2, tx3이 꼬이고, rideReservation테이블은 접근이 불가능한채로 되어서 다른 rideReservation에 접근하는 쿼리들도 블로킹됨
- 조치
  - (대응) online-ddl을 사용할시에는, 반드시 모니터링을 진행하여서, 테이블이 블로킹되는 현상을 목격한다면, 즉각적으로 ddl을 진행하는 쿼리를 kill해줍니다

### foreign key 제약 추가시 table level lock으로 인한 서비스 다운 이슈

- 현상
  - 2022-10-19 12:07 ~ 12:52 동안 드라이버 서버의 startWorking, dropOff 등이 동작하지 않는 문제가 발생하였습니다.
    - 동작하여도 레이턴시가 매우 컸음
- 대응
  - 일단 데드락을 발생시키는 mysql connection 스레드를 kill하고, 팟도 삭제하였습니다.
- 원인
  - 원인은 liquibase로 인한 이미 존재하는 테이블(`taxi_settlement_info`, `tmoney_settlement_record`)에 foreign key 제약 추가로 인한 table level lock 때문입니다. (즉 driver_api_server 때문이 아닙니다)
  - 장애가 크게 두번으로 나뉘는데요
    - [12:07 ~ 12:15] taxi_settlement_info에 liquibase 작업으로 인한 테이블 락이걸렸고, taxi_settlement_info를 insert할때 테이블락이 풀리길 기다리고, 그럼 정산 관련 트랜잭션에서 driver에 s-lock을 걸어놓으므로 해당 드라이버는 state변경이 불가능해집니다 (출근도 안됨)
    - [12:25 ~ 12:52] 리퀴베이스 팟이 CI abortion와는 별개로 계속 살아있어서 컨테이너가 죽지 않은 상태로 taxi_settlement_info테이블락을 계속 잡고 있었습니다. 해당 작업이 끝나고 이번에는taxi_settlement_record에 liquibase 작업으로 인한 테이블 락이걸렸고, (나머지는 위의 시나리오와 동일)
- 조치
  - (예방) 데이터 사이즈가 큰 테이블인 경우(100만 row 이상), 외래키 제약을 걸지 않습니다.
  - (예방) DB 스키마 추가나 변경에 대한 PR은 꼼꼼하게 리뷰합니다
