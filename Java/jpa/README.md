# JPA

- 영속성
- SQL Mapper와 ORM
- 각종 기술

## 영속성(Persistence)

- 개요
  - 데이터를 생성한 프로그램이 종료되더라도 사라지지 않는 데이터 특성
- Persistence Layer
  - 프로그램의 아키텍처에서, 데이터에 영속성을 부여해주는 계층
- Persistence Framework
  - SQL Mapper
  - ORM

## SQL Mapper와 ORM

- ORM
  - 개요
    - SQL을 자동 생성
    - 데이터베이스 관계를 자바 객체로 매핑
      - 객체를 통해 간접적으로 데이터베이스 데이터를 다룸
  - 예시
    - Hibernate
- SQL Mapper
  - 개요
    - SQL을 명시해줘야 함
    - 단순히 필드를 매핑하는 것이 목표
  - 예시
    - Mybatis, JdbcTemplates

## 각종 기술

- JDBC
  - DB에 접근할 수 있도록 Java에서 제공하는 API
  - 모든 persistence framework는 jdbc API를 사용
- JPA
  - 자바 ORM 기술에 대한 API 표준 명세, Java에서 제공하는 API
  - 사용자가 원하는 JPA 구현체를 선택해서 사용 가능
    - Hibernate, ...
- Hibernate
  - JPA의 구현체 중 하나
  - JDBC API를 당연하게도 사용
  - HQL(Hibernate Query Language)라고 불리는 매우 강력한 쿼리 언어 포함
- Mybatis
  - SQL Mapper
