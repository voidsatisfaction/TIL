# SELECT문

- 처리 순서 및 예시
- 인덱스
- Explain을 이용한 쿼리 최적화

## 처리 순서 및 예시

1. FROM (어떤 테이블에서)
2. WHERE (어떤 조건으로 필터링 데이터를)
3. GROUP_BY (어떻게 묶어서)
4. HAVING (그 묶은 애들을 어떤 조건으로)
5. SELECT (어떠한 열만)
6. ORDER_BY (어떤 순서로)
7. LIMIT (몇개만)
8. 출력하지?

### 예시1

- eid를 그룹으로 해서 eid와 각 그룹의 개수와 최신 created를 table이라는 테이블에서 가져와서 latest를 기준으로 내림차순으로 정렬하고 100개를 추출

```sql
SELECT eid, COUNT(1) AS count, MAX(created) AS latest FROM table GROUP BY eid ORDER BY latest DESC limit 100;
```

- table에서 eid로 맺어진 그룹마다, eid와 개수와 latest 날짜를 latest의 내림차순으로 정렬한 뒤에 100개를 추출한다.
- ORDER BY 절에는 일반적으로 SELECT 절에 명시되지 않은 컬럼을 사용할 수 있으나 GROUP BY 절이 존재하거나 결과 집합을 그룹화하는 DISTINCT, UNION 사용 시에는 SELECT 절에 명시된 컬럼만 ORDER BY 절에 사용할 수 있습니다.

### 예시2

```sql
select sum(money) from (
  select * from Balances where createdAt in (
    select MAX(createdAt) from Balances where account != 'abc' group by account
  )
) as a;
```

- account가 'abc'가 아닌 것들만 account기준으로 그룹을 지어서 최신 createdAt만 추출한 뒤에 그것을 createdAt으로 갖는 Balances의 행들을 찾아서 그중에 money칼럼 전부 함산한 것을 추출

## 인덱스

- 하나의 테이블은 16개의 인덱스 가질수 있음
- 값 별 특징
  - CAHR, VARCHAR은 **앞쪽의 일부만** 인덱스화 할 수 있음
  - BLOB, TEXT는 앞쪽부터 값의 몇바이트를 인덱스화 할 것인지 선택해야 함
- 인덱스를 많이 붙이면 좋지 않은 경우
  - INSERT, UPDATE가 너무나도 빈번하게 일어나는 경우
    - 인서트의 갱신에 많은 시간자원을 소비

### 인덱스를 사용하는 경우와 사용하지 않는 경우

```sql
-- MySQL에서는 다음과 같은 경우에 index를 사용하여 검색을 한다.

mysql> select * from tablename where name LIKE "dino%";
mysql> select * from tablename where name LIKE "di%sf%";

-- 다음과 같은 경우에는 index가 설정이 되어 있더라도 index를 사용하지 못하고 검색을 하게 된다. (예제1 참조)

mysql> select * from tablename where name LIKE "%nos%";
mysql> select * from tablename where name LIKE id; -- // 다른 컬럼과의 비교
```

## Explain을 이용한 쿼리 최적화

### 참고자료

http://www.mysqlkorea.com/sub.html?mcode=manual&scode=01&m_no=21444&cat1=7&cat2=217&cat3=227&lang=k

### 정의

- DESCRIBE의 동의어
- SELECT명령문을 실행하는 방법에 대한 정보를 얻기 위한 수단
  - 쿼리 실행 플랜 정보를 옵티마이저에서 가져와서 출력함

### 활용

- 테이블 어느 곳에 인덱스를 추가해야지 보다 SELECT를 빠르게 할 수 있는지 확인 가능
- 옵티마이저가 최적의 조인 순서로 테이블을 조인할 수 있는지도 확인

### Explain 결과 칼럼들

- id
  - SELECT identifier로, SELECT의 순차적인 번호
- select_type
  - SELECT에 대한 타입
  - 종류
    - SIMPLE
      - UNION이나 서브쿼리 사용하지 않는 간단한 SELECT
    - PRIMARY
      - 가장 바깥의 SELECT
    - UNION
      - 안에 있는 두번째나 그 이후의 SELECT
    - DEPRENDENT UNION
      - 바깥 쿼리에 의존하는 두번째나 그 이후의 SELECT
    - UNION RESULT
      - UNION의 RESULT
    - SUBQUERY
      - 서브쿼리 속의 첫 SELECT
    - DEPENDENT SUBQUERY
      - 바깥 쿼리에 의존하는 서브쿼리 속의 첫 SELECT
    - DERIVED
      - FROM절 속에 있는 서브쿼리
- table
  - 결과 열이 참조하는 테이블
- type (join)
  - 조인의 타입
  - 종류
    - system
      - 테이블은 하나의 열만을 가지고 있다(= 시스템 테이블)
      - const 조인 타입의 특별한 경우
    - const
      - PRIMAY KEY 혹은 UNIQUE 인덱스의 모든 부분을 상수 값과 비교를 할 때 사용됨
    - eq_ref
      - 예시: `SELECT * FROM ref_table,other_table WHERE ref_table.key_column=other_table.column;`
    - ref
    - ref_or_null
    - index_merge
      - 인덱스 병합 최적화가 사용된 JOIN
    - unique_subquery
    - index_subquery
    - range
      - 주어진 범위에 들어 있는 열만을 추출하며, 열 선택은 인덱스를 사용
      - 예시: `SELECT * FROM tbl_name WHERE key_part1= 10 AND key_part2 IN (10,20,30);`
    - index
      - ALL과 동일하지만, 인덱스 트리 만을 스캔
    - ALL
      - 이전 테이블에서 읽어온 각각의 열을 조합하기 위해 전체 테이블 스캔을 실행
- possible_keys
  - 이 테이블에서 열을 찾기 위해 MySQL이 선택한 후보 인덱스를 가리킴
  - 후보이므로 사용되었다고 단정할 수 없음
- key
  - 실제로 사용할 예정인 인덱스
- key_len
  - MySQL이 사용하기로 결정한 키의 길이
  - 키로 지정이된 각 칼럼을 byte단위로 계산해서 나타낸
  - 참고
    - https://stackoverflow.com/questions/7643491/understanding-mysql-key-len-in-explain-statement
- ref
  - 테이블에서 열을 선택하기 위해 key 칼럼 안에 명명되어 있는 인덱스를 어떤 칼럼 또는 상수(constant)와 비교하는지 보여줌
  - JOIN에서는 on뒤에서 다른 테이블으 어떤 칼럼이랑 비교하는지 나타내줌
- rows
  - MySQL이 쿼리를 실행하기 위해 조사해야 하는 열의 숫자
- filtered
  - [참고](https://dba.stackexchange.com/questions/164251/what-is-the-meaning-of-filtered-in-mysql-explain)
- Extra
  - MySQL이 쿼리를 어떻게 해석하는지에 관한 추가 정보제공
  - 종류
    - Distinct
      - 매칭되는 값을 찾게되면 그 열에 대해서는 검색 중단
    - Not exists
    - Using index
      - 인덱스 트리에 있는 정보만을 가지고 테이블에서 칼럼 정보를 추출
    - Using temporary
      - 쿼리 해석을 위해서 결과를 저장할 임시 테이블 생성
      - 쿼리가 칼럼을 서로 다르게 목록화 하는 경우
        - GROUP BY
        - ORDER BY
