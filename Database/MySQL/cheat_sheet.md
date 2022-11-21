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

### 프로세스 삭제

- mysql
  - `KILL (프로세스id)`
- aurora mysql
  - `mysql.rds_kill_query(queryID)`

## 테스트

### 테스트용 데이터베이스 만들기

### 테이블 만들기

```sql
create table parent(
  id int not null,
  c1 int,
  primary key (id)
);

create table child(
  id int not null,
  parent_id int,
  primary key (id),
  foreign key (parent_id) references parent(id)
);

insert into parent values (1, 10);
insert into parent values (2, 15);
insert into parent values (3, 22);

insert into child values (1, 3);
insert into child values (2, 2);
```

### 인덱스 만들기

```sql
create index test1_idx1 on test1 (c1);

ALTER TABLE Orders ADD FOREIGN KEY (PersonID) REFERENCES Persons(PersonID);
```

### 칼럼 타입 바꾸기

### 테이블 구조 보기

```sql
show create table test1 \G;
```

### 큰 데이터셋 만들기

- information schema를 이용한 방법
  - https://stackoverflow.com/a/60841951
