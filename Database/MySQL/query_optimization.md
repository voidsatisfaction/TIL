# 쿼리 최적화

- 의문
- 11.1 쿼리 작성과 연관된 시스템 변수
- 11.2 매뉴얼의 SQL 문법 표기를 읽는 방법
- 11.3 MySQL 연산자와 내장 함수
- 11.4 SELECT
  - JOIN
- 11.5 INSERT
- 11.6 UPDATE & DELETE
- 11.7 스키마 조작(DDL)
- 11.8 쿼리 성능 테스트

## 의문

- JOIN을 하면, 항상 임시 테이블이 생성되는건가?
  - *애초에 임시 테이블이 뭐지?*
- *JOIN시에는 다음과 같은 동작이 맞는가?*
  - driving table, driven table 둘다 인덱스가 걸린 경우, driving table의 index range scan을 함
  - driving table의 index scan하면서, driven table에서 driving table의 인덱스 값에 대응하는 index를

## 11.1 쿼리 작성과 연관된 시스템 변수

## 11.2 매뉴얼의 SQL 문법 표기를 읽는 방법

## 11.3 MySQL 연산자와 내장 함수

### COUNT

- 개요
  - 결과 레코드의 건수를 반환
  - `COUNT(* | 표현식 | 칼럼)`
    - `*`
      - 레코드 자체
    - `표현식 | 칼럼`
      - 표현식이나 칼럼의 값이 NULL이 아닌 레코드 건수 반환
- 주의
  - `COUNT`가 매우 느릴 수 있음
    - 여러가지 필터 조건이 들어가면, 커버링인덱스로만 처리가 안되는 부분이 존재하기 마련인데, 그렇게 되면 결국은 테이블 데이터를 읽어야만 하는 경우가 대부분

## 11.4 SELECT

- 개요
  - 웹 서비스에서 사용되는 비율 높음
  - 어떻게 읽는가에 주의 필요

### SELECT 절의 처리 순서

위: 일반적인 SELECT 쿼리 실행 순서
아래: 예외적으로 ORDER BY가 조인보다 먼저 실행되는 경우

![](./images/ch11/query_execution_order1.jpg)

- 일반적인 경우
  - FROM, WHERE -> GROUP BY -> DISTINCT -> HAVING -> ORDER BY -> LIMIT
- 예외적으로 ORDER BY가 조인보다 먼저 실행되는 경우
  - FROM, WHERE -> ORDER BY -> JOIN -> LIMIT
    - `GROUP BY`없이 `ORDER BY`만 사용된 쿼리
- 실행 순서를 벗어나는 쿼리
  - 인라인 뷰 사용 필요
    - e.g) LIMIT먼저 적용하고, ORDER BY실행
    - 대신 임시 테이블이 사용됨

### WHERE 절과 GROUP BY 절, ORDER BY 절의 인덱스 사용

- 인덱스를 사용하기 위한 기본 규칙
  - 1 인덱스된 칼럼의 값 자체를 변환하지 않고 그대로 사용해야 함
    - 복잡한 연산 or 해시값을 만들어서 비교하려면, 미리 계산된 값을 저장하도록 가상 칼럼을 추가하고, 그 칼럼에 인덱스를 생성하거나 함수 기반의 인덱스를 사용해야 함
  - 2 WHERE절의 비교 조건에서 연산자 양쪽의 두 비교 대상 값이 데이터 타입이 일치해야 함
    - 칼럼을 옵티마이저가 주어진 값의 타입으로 변환한뒤에 비교
- WHERE 절의 인덱스 사용
  - 개요
    - **WHERE 조건절의 순서는 실제 인덱스의 사용 여부와 무관**
      - 옵티마이저가 알아서 잘해줌
    - 범위 비교 조건으로 인덱스가 사용된 이후에는, 또 범위 비교 조건으로 사용되지 못하고, 체크조건으로 사용됨
      - e.g) `col1 = ?`, `col2 = ?`, `col3 > ?`, `col4 < ?`
        - col4는 체크 조건이 됨
          - *왜 스킵 인덱스 사용이 안된걸까*

### JOIN

- 주의
  - MySQL에서는 `JOIN`, `CROSS JOIN`, `INNER JOIN`은 전부 동의어
    - 즉, 위의 세가지 모두 ON절, WHRERE절에 driving table, driven table을 연결해주면 `INNER JOIN`을 의미함.
      - 하지만 표준 SQL은 `CROSS JOIN`, `INNER JOIN`이 구분되어있음
    - 대신, driving table, driven table을 연결해주지 않으면 `CARTESIAN PRODUCT`이 적용
      - 단순 필터도 어김없이 CARTESIAN PRODUCT 적용
    - 예시(같은 실행 계획)
      - `explain select * from User as u inner join ProgressionLog as pl on u.id = pl.userId where u.id = 'voidsatisfaction';`
      - `explain select * from User as u cross join ProgressionLog as pl on u.id = pl.userId where u.id = 'voidsatisfaction';`
  - ON vs WHERE
    - ON으로 driving table, driven table을 연결하는 경우 vs WHERE로 연결하는 경우
      - ON
        - `explain select * from User as u cross join ProgressionLog as pl on u.id = pl.userId;`
        - 연결 조건을 명시하므로 SQL을 의미적으로 알기 쉬움
      - WHERE
        - `explain select * from User as u cross join ProgressionLog as pl where u.id = pl.userId;`
      - 결론
        - ON을 쓰자
    - ON으로 데이터 필터링 하는 경우 vs WHERE로 데이터 필터링 하는 경우
      - ON
        - `explain select * from User as u left join ProgressionLog as pl on u.id = pl.userId and u.id = 'voidsatisfaction';`
        - outer join시에 원하지 않는 결과가 나올 수 있음
          - 조인 자체를 할 때, on의 모든 조건이 맞아야만 driving table, driven table을 연결해준다(필터링이 아님)
      - WHERE
        - `explain select * from User as u left join ProgressionLog as pl on u.id = pl.userId where u.id = 'voidsatisfaction';`
        - 필터링
      - 결론
        - 필터링 시에는 WHERE를 쓰고, 정확히 동작을 이해하자

## 11.5 INSERT

## 11.6 UPDATE & DELETE

## 11.7 스키마 조작(DDL)

- 개요
  - 모든 오브젝트를 생성하거나 변경하는 쿼리
    - 스토어드 프로시저, 함수, DB, 테이블을 생성하거나 변경하는 대부분의 명령어

### 온라인 DDL

- 개요
  - 스키마 변경을 실행하는 도중에 DML(INSERT, UPDATE, DELETE)을 실행하기 위한 기술
    - MySQL 5.5이하의 버전에서는 테이블 구조 변경 중에는 다른 커넥션에서 DML을 실행할 수 없었음
    - 따라서 `pt-online-schema-change`도구를 많이 사용 했었었음
    - 8.0부터는 내장 온라인 DDL기능으로 처리가 가능해져서 거의 사용하지 않음
- 동작
  - inplace algorithm
    - INPLACE 스키마 변경이 지원되는 스토리지 엔진의 테이블인지 확인
    - INPLACE 스키마 변경 준비(스키마 변경에 대한 정보를 준비해서 온라인 DDL 작업 동안 변경되는 데이터 추적 준비 - `X Lock`)
    - 테이블 스키마 변경 및 새로운 DML 로깅
      - DML은 대기하지 않음
    - DML 로그 적용(`X Lock`)
      - *그럼 그전까지는 commit이 안된다는건가?*
      - 버퍼에서 알아서 처리하나 봄
    - INPLACE 스키마 변경 완료(COMMIT)
- 설정
  - `old_alter_table`시스템 변수를 이용해 ALTER TABLE 명령이 온라인 DDL로 작동할지, 아니면 예전방식(테이블 lock)으로 처리할지를 결정할 수 있음
    - MySQL 8.0이상의 버전에서는 기본값이 off이므로 자동으로 온라인 DDL이 활성화 됨
- 알고리즘 종류
  - INSTANT
    - 데이터 변경 없이, 메타데이터만 변경하고 작업을 완료
    - 스키마 변경 시간이 매우 짧아서 다른 커넥션의 쿼리 처리에 큰 영향을 미치지 않음
  - INPLACE + (락: None, S-Lock, X-Lock)
    - 임시 테이블로 데이터를 복사하지 않고 스키마 변경 실행
      - 내부적으로는 테이블의 리빌드를 실행할 수도 있음
    - 스키마 변경중에 읽고 쓰기 가능
      - 맨 처음과 맨 마지막만 잠깐 읽고 쓰기 불가능하지만, 시간이 매우 짧음
    - 구분
      - 리빌드가 필요한 경우
        - 테이블 레코드 건수에 따라 상당히 많은 시간이 소요될 수 있음
        - e.g) 프라이머리 키 추가
      - 리빌드가 필요하지 않은 경우
        - 매우 빨리 작업이 완료될 수 있음
        - e.g) 칼럼 이름 변경
    - **벤치마크**
      - 8Core Intel CPU(자원은 공유되는중)
        - 1100만 row inplace add column당 330초
        - **1만 row당 0.3초(0.5초라고 계산하는게 나을듯)**
  - COPY (락: X-Lock)
    - 변경된 스키마를 적용한 임시 테이블을 생성하고, 테이블의 레코드를 모두 임시 테이블로 복사한 후 최종적으로 임시 테이블을 RENAME해서 스키마 변경을 완료함
    - 읽기만 가능하고 DML(CUD) 실행 불가

### 트러블 슈팅

온라인 DDL시 Duplicate entry 에러

```
ERROR 1062 (23000) at line 1:
  Duplicate entry '1' for key 'dup_error.PRIMARY'
```

- 설명
  - Online DDL은 스토리지 엔진 수준으로 들어오는 데이터 변경 정보를 임시 버퍼 공간에 쌓았다가, 최종 시점에 버퍼의 내용을 적용하는 방식으로 진행
  - 다른 커넥션에서 중복된 레코드를 insert하는 경우, 성공 실패와 관계없이 online ddl은 최종 실패
    - 다음의 경우 모두 실패
      - `INSERT INTO ... ON DUPLICATE KEY UPDATE ...`
      - `INSERT INTO ...` 그리고 중복 에러
      - `INSERT INTO ... ON DUPLICATE KEY UPDATE ...` 그리고나서 `ROLLBACK`
      - 왜냐하면, Online DDL에서는 `INSERT`이후 `DELETE`되는 방식으로 처리됨
        - 이미 존재하는 유니크행에 INSERT를 하게되므로 실패
- 대안
  - `INSERT INTO ... ON DUPLICATE KEY UPDATE ...` 문장대신, `SELECT`해서 `INSERT`할지, `UPDATE`할지 구분해서 실행하도록 쿼리를 바꿔서 사용
  - `pt-online-schema-change`사용
- 또 다른 실패 케이스
  - 온라인 변경 로그 버퍼 공간이 부족한 경우
    - `innodb_online_alter_log_max_size`변수
  - ALTER TABLE 이전 버전의 테이블 구조에서는 ok, ALTER TABLE이후의 테이블 구조에는 적합하지 않은 레코드가 INSERT되거나 UPDATE된 경우, 마지막 과정에서 실패
  - 스키마 변경을 위해서 필요한 잠금 수준보다 낮은 잠금 옵션이 사용된 경우
  - 온라인 스키마 변경은 `LOCK=NONE`으로 실행된다고 하더라도, 변경 작업의 처음과 마지막 과정에서 잠금이 필요한데, 이 잠금을 획득하지 못하고 타임 아웃이 발생하는 경우(메타데이터 잠금)
    - `lock_wait_timeout`변수
  - 온라인으로 인덱스를 생성하는 작업의 경우 정렬을 위해, `tmpdir` 시스템 변수에 설정된 디스크의 임시 디렉터리를 사용하는데, 이 공간이 부족한 경우

## 11.8 쿼리 성능 테스트
