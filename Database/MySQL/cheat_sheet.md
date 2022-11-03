# MySQL Cheat Sheet

- 모니터링용
  - 프로세스 리스트 보여주기
- 테스트용
  - 테스트용 데이터베이스 만들기
  - 테이블 만들기
  - 인덱스 만들기
  - 칼럼 타입 바꾸기

## 모니터링용

### 프로세스 리스트 보여주기

```sql
select * from information_schema.processlist;
```

## 테스트

### 테스트용 데이터베이스 만들기

### 테이블 만들기

```sql
create table test1(id int not null, c1 int, primary key (id));

insert into test1 values (1, 10);
insert into test1 values (2, 15);
insert into test1 values (3, 22);
```

### 인덱스 만들기

```sql
create index test1_idx1 on test1 (c1);
```

### 칼럼 타입 바꾸기
