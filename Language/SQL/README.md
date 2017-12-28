# SQL기초 강좌

- [하테나 데이터베이스 교과서](https://github.com/hatena/Hatena-Textbook/blob/master/database-programming.md)

- [宣言型プログラミング](https://ja.wikipedia.org/wiki/%E5%AE%A3%E8%A8%80%E5%9E%8B%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0)

SQL은 취득하는 집합의 성질을 선언 하는 것이며, 취득의 구체적인 방법은 기술 하지 않는다.（Declarative Programming）

## Index의 활용과 중요성

- [왜 모든 컬럼에 인덱스를 걸면 안되는가?](http://hashcode.co.kr/questions/1551/%EC%99%9C-db-%ED%85%8C%EC%9D%B4%EB%B8%94%EC%9D%98-%EB%AA%A8%EB%93%A0-%EC%BB%AC%EB%9F%BC%EC%97%90-%EC%9D%B8%EB%8D%B1%EC%8A%A4%EB%A5%BC-%EA%B1%B8%EB%A9%B4-%EC%95%88%EB%90%98%EB%82%98%EC%9A%94)

## 테이블 Join의 종류

![SQL_JOINS](./assets/sql_join.png)

테이블의 Join은 다음과 같이 크게 나뉜다.

- Inner Join
- Outer Join
  - Left Join
  - Right Join

## 트랜젝션 처리

- 트랜젝션은 실패를 허용하지 않는 데이터 엑세스 군
- ACID특성을 갖는다.
  - 원자성(atomicity)：
  - 일관성(consistency)：
  - 독립성(isolation)：
  - 내구성(durability)：
- 은행의 송금 시스템
  - 절대로 에러가 나서는 안됨.

## TIP

```SQL
-- SQL에서는 단따옴표로 둘러싸이지 않는 경우, property(column)으로 인식한다.
-- 좋지 못한 예
INSERT INTO artist (name, birthday) VALUES (kim, 2012-11-03);

-- 좋은 예
INSERT INTO artist (name, birthday) VALUES ('kim', '2012-11-03');
```
