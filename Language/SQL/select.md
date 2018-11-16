# SELECT문

- 처리 순서 및 예시

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
