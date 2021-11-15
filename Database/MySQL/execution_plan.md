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

- id
- select_type
- tables
- partitions
- type

실행 계획 쿼리 결과의 예시

```SQL
SELECT site_options.domain, sites_users.user, site_taxes.monthly_statement_fee, site.name, AVG(price) AS average_product_price
  FROM sites_orders_products, site_taxes, site, sites_users, site_options
    WHERE site_options.site_id = site.id
      AND sites_users.id = site.user_id
      AND site_taxes.site_id = site.id
      AND sites_orders_products.site_id = site.id
    GROUP BY site.id
    ORDER BY site.date_modified desc
    LIMIT 5;
```

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

### **id**

- 개요
  - 단위 SELECT 쿼리별로 부여되는 식별자
    - SELECT를 포함하는 서브쿼리의 경우 다른 식별자 값을 갖음
    - JOIN의 경우, JOIN되는 테이블마다 레코드가 출력되지만, 동일한 id값이 부여 됨
- 특징
  - id값이 테이블의 접근 순서를 의미하지 않음
    - `EXPLAIN FORMAT=TREE` 명령으로 확인하면 인덴트가 많이 된 곳이 더 먼저 실행된 것(쿼리 실행 순서 파악 명확히 가능)

### **select_type**

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

### **table**

- 개요
  - 테이블의 이름
- 특징
  - 테이블을 사용하지 않는 경우 `NULL`
  - <>로 둘러싸인 이름
    - 임시테이블
    - 뒤에 숫자는 단위 SELECT 쿼리의 id값
      - e.g) <drived N>, <union M,N>

### **partitions**

### **type**

eq_ref의 예시

```sql
EXPLAIN
SELECT * FROM dept_emp de, employees e
WHERE e.emp_no=de.emp_no AND de.dept_no='d005';

-- dept_emp 테이블을 먼저 읽어서 필터링 후
-- employees 테이블을 검색
```

index_merge의 예시

```sql
EXPLAIN
SELECT * FROM employees
WHERE emp_no BETWEEN 10001 AND 11000
  OR first_name='Smith';

-- 1, index_merge, [PRIMARY, ix_firstname], Using union(PRIMARY, firstname); Using where
```

- 개요
  - 테이블의 접근 방법
    - MySQL 매뉴얼에는 '조인 타입'이라고 함
- 종류
  - 인덱스 사용
    - 단일 인덱스 사용
      - 동등 비교 연산자(`=`)
        - const(UNIQUE INDEX SCAN)
          - 프라이머리 키 or 유니크 키 칼럼을 이용하는 `WHERE`조건절 + 반드시 1건을 반환
          - 옵티마이저가 쿼리를 상수로 대체
        - eq_ref
          - 조인에서 처음 읽은 테이블의 칼럼값을, 그 다음 읽어야 할 테이블의 프라이머리 키나 유니크 키 칼럼의 검색조건에 사용
            - 조인에서 두번째 이후에 읽는 테이블에서 반드시 1건만 존재한다는 보장이 있어야 사용할 수 있는 접근 방법
              - 유니크 인덱스는 NOT NULL이어야 함
              - 다중 칼럼 인덱스면, 인덱스의 모든 칼럼이 비교 조건에 사용되어야 함
        - ref
          - 인덱스의 종류와 관계없이 동등 조건으로 검색
            - 조인의 순서와 관계 없음, 프라이머리 키 유니크 키 제약 없음
            - 레코드가 반드시 1건이라는 보장은 없음
      - fulltext
        - MySQL 서버의 전문 검색 인덱스를 사용해 레코드를 읽는 접근 방식
        - 일반적으로 `const`, `eq_ref`, `ref` 다음의 우선순위
      - ref_or_null
        - ref 접근방법과 같은데, NULL 비교가 추가됨
        - 나쁘지 않은 접근 방법
      - unique_subquery
        - `WHERE`조건절에서 사용될 수 있는 `IN(subquery)` 형태의 쿼리를 위한 접근 방법
          - 서브쿼리에서 중복되지 않는 유니크한 값만 반환할 때 이 접근 방법사용
      - index_subquery
        - `WHERE`조건절에서 사용될 수 있는 `IN(subquery)` 형태의 쿼리를 위한 접근 방법
          - 서브쿼리에서 중복되는 값을 반환할 수도 있음
          - 대신, 서브쿼리의 결과의 중복된 값을 인덱스를 이용해서 제거할 수 있을 때 사용되는 방법
      - range
        - 인덱스 레인지 스캔 형태의 접근 방법(`<`, `>`, `IS NULL`, `BETWEEN`, `IN`, `LIKE`)
        - 우선순위는 상당히 낮지만, 이 접근방법도 상당히 빠르며, 최적의 성능을 보장
          - c.f) 일반적으로 인덱스 레인지 스캔 = `const`, `ref`, `range`세 가지 접근 방식을 모두 묶어서 이야기 하는 것
    - 다중 인덱스 사용
      - index_merge
        - 2개 이상의 인덱스를 이용해 각각의 검색 결과를 만들어낸 후, 그 결과를 병합해서 처리하는 방식
          - 여러 인덱스를 읽어야 하므로, range 접근 방법보다 효율성이 떨어짐
          - 전문 검색 인덱스를 사용하는 쿼리에서는 index_merge가 적용되지 않음
          - index_merge 접근 방법으로 처리된 결과는 항상 2개 이상의 집합이 되기 때문에 그 두 집합의 교집합이나 합집합, 또는 중복 제거와 같은 부가적인 작업이 더 필요함
      - index
  - 인덱스 미사용
    - ALL
      - 풀 테이블 스캔
