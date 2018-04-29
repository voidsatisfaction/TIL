# 아마존 RDS에서 데이터 가져오기

- 데이터 분석을 하려면은 로컬에 데이터를 가져오고 싶어지는데, 그 때 사용하는 방법(csv파일로)

```sh
mysql -u유저이름 -h 호스트명 --database=데이터베이스이름 -e "select concat(칼럼1, ',', 칼럼2, ',', 칼럼3, ',', 칼럼4, ',', 칼럼5, ',', 칼럼6) from 테이블" > emailConfirms.csv
```

```sql
select unix_timestamp(createdAt) as createdAt, unix_timestamp(completedAt) as completedAt from EmailConfirms WHERE createdAt is not null AND completedAt is not null;

select concat(id, ',', createdAt, ',', completedAt) from (select id, unix_timestamp(createdAt) as createdAt, unix_timestamp(completedAt) as completedAt from EmailConfirms WHERE createdAt is not null AND completedAt is not null) t;
```

- from부분에 데이터베이스의 테이블 명이 아니더라도 서브쿼리를 넣을 수 있음
  - 서브쿼리 뒤에는 테이블 별칭이 들어가야함(alias)
- 유닉스 시간을 가져오려면 `unix_timestamp`함수를 사용
- `as`키워드는 각각의 칼럼 뒤에 두어야 함
- `null`값이 들어있는 행을 배제 하기 위해서는 `is not null`이 필요
- `concat`함수로 칼럼들을 결합함(csv파일 만들기)
