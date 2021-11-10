# Execution plan

- 의문
- 개요
- 10.1 통계 정보
- 10.2 실행 계획 확인
- 10.3 실행 계획 분석
  - id
  - select_type
  - table
  - partitions
  - type

## 의문

## 개요

## 10.1 통계 정보

## 10.2 실행 계획 확인

## 10.3 실행 계획 분석

실행 계획 쿼리 결과의 예시

```
+------+-------------+---------------------------------+--------+-----------------+---------------+---------+---------------------------------+------+-----------+
| id   | select_type | table                           | type   | possible_keys   | key           | key_len | ref                             | rows | Extra     |
+------+-------------+---------------------------------+--------+-----------------+---------------+---------+---------------------------------+------+-----------+
|    1 | SIMPLE      | sites                           | index  | PRIMARY,user_id | PRIMARY       | 4       | NULL                            |  858 | Using temporary; Using filesort |
|    1 | SIMPLE      | sites_options                   | ref    | site_id         | site_id       | 4       | service.sites.id                |    1 |           |
|    1 | SIMPLE      | sites_taxes                     | ref    | site_id         | site_id       | 4       | service.sites.id                |    1 |           |
|    1 | SIMPLE      | sites_users                     | eq_ref | PRIMARY         | PRIMARY       | 4       | service.sites.user_id           |    1 |           |
|    1 | SIMPLE      | sites_orders_products           | ref    | site_id         | site_id       | 4       | service.sites.id                | 4153 |           |//
+------+-------------+---------------------------------+--------+-----------------+---------------+---------+---------------------------------+------+-----------+
```

- **id**
  - 개요
    - 단위 SELECT 쿼리별로 부여되는 식별자
      - SELECT를 포함하는 서브쿼리의 경우 다른 식별자 값을 갖음
      - JOIN의 경우, JOIN되는 테이블마다 레코드가 출력되지만, 동일한 id값이 부여 됨
  - 특징
    - id값이 테이블의 접근 순서를 의미하지 않음
      - `EXPLAIN FORMAT=TREE` 명령으로 확인하면 인덴트가 많이 된 곳이 더 먼저 실행된 것(쿼리 실행 순서 파악 명확히 가능)
- **select_type**
  - 개요
    - SELECT 쿼리가 어떤 타입의 쿼리인지 표시
  - 종류
    - SIMPLE
      - UNION, 서브쿼리를 사용하지 않는 단순한 SELECT 쿼리인 경우
        - 일반적으로 제일 바깥쪽에 있는 단위 쿼리가 SIMPLE이 됨
    - PRIMARY
      - UNION이나 서브쿼리를 가지는 SELECT 쿼리의 실행 계획에서 가장 바깥쪽에 있는 단위 쿼리
    - UNION 계열
      - UNION
        - UNION으로 결합하는 단위 SELECT 쿼리 가운데 두번쨰 이후 단위 SELECT 쿼리
          - 첫번째는 쿼리 결과들을 모아서 저장하는 임시 테이블(DERIVED)가 select_type으로 표시 됨
      - DEPENDENT UNION
        - UNION 쿼리인데, 내부의 쿼리가 외부의 값을 참조해서 처리될 때
      - UNION RESULT
        - UNION 결과를 담아두는 테이블
          - 단위 쿼리가 아니라서 id가 부여되지 않음
        - `UNION ALL`을 사용하면, 임시 테이블을 버퍼링하지 않아서, UNION RESULT라인이 필요치 않게 됨
- **table**
  - 개요
    - 테이블의 이름
  - 특징
    - 테이블을 사용하지 않는 경우 `NULL`
    - <>로 둘러싸인 이름
      - 임시테이블
      - 뒤에 숫자는 단위 SELECT 쿼리의 id값
        - e.g) <drived N>, <union M,N>
- **partitions**
- **type**
  - 개요
    - 테이블의 접근 방법
      - MySQL 매뉴얼에는 '조인 타입'이라고 함
  - 종류
    - 인덱스 미사용
      - ALL
        - 풀 테이블 스캔
    - 인덱스 사용
      - 단일 인덱스 사용
        - const(UNIQUE INDEX SCAN)
          - 프라이머리 키 or 유니크 키 칼럼을 이용하는 `WHERE`조건절 + 반드시 1건을 반환
          - 옵티마이저가 쿼리를 상수로 대체
        - eq_ref
        - ref
        - fulltext
        - ref_or_null
        - unique_subquery
        - index_subquery
        - range
        - index
      - 복수 인덱스 사용
        - index_merge
