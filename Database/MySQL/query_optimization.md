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

## 11.8 쿼리 성능 테스트
