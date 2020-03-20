# Overview of PostgreSQL Internals

- 의문
- The Path of a Query
  - Connection
  - Parser

## 의문

## The Path of a Query

- ① \[connection\]
  - application program에서 PostgreSQL 서버로의 커넥션 확립
  - application program은 서버로 쿼리를 전달하고, 서버로 부터 받은 결과를 수신
- ② \[parser stage\]
  - correct syntax
  - query tree 생성
- ③ \[rewrite system\]
  - rewrite system이 parser stage에서 생성된 query tree를 받고, query tree에 적용할 룰(system catalogs)을 찾음
  - rule body에 주어진 변환을 수행
- ④ \[planner/optimizer\]
  - rewritten query tree를 받고, executor의 input이 되는 query plan을 생성
    - 방법
      - 같은 결과에 도달하는 모든 경로를 생성(e.g 일반적인 sequential scan, index scan)
      - 각 path에 대한 실행 cost가 추정되고, 가장 효율적인 path가 선택됨
- ⑤ \[executor\]
  - recursive하게 plan tree를 탐색하여, plan에 작성된 대로 row를 가져옴
  - relation을 scanning, sort, join 하는 동안, storage system을 사용함
  - 생성된 row들을 반환함

### ① Connection

- 개요
  - process per user client/server model
    - a client process <-> a server process
  - master process(이름: postgres)가 존재
    - 커넥션 요청이 오면 master process가 새 server process를 spawn
    - 특정 TCP/IP 포트에서 connection을 listen하고 있음
- 특징
  - 서버 프로세스
    - concurrent data access 동안, semaphore, shared memory 등을 사용하여 서버 프로세스끼리 커뮤니케이션 함
  - 클라이언트 프로세스
    - PostgreSQL protocol을 이해하면 어떠한 프로그램이라도 가능
    - c언어 라이브러리 `libq` 기반이 많음
      - JDBC 드라이버는 예외(다른 방식으로 프로토콜을 구현)
- 커넥션 후
  - plain text로 쿼리를 전송
  - 클라이언트에서 parsing이 전혀 없음

### ② Parser

- 구성
  - parser가 생성
    - Unix 툴인 bison과 flex를 사용해서 `gram.y`, `scan.l`에 정의된 파서 생성
  - transformation process
    - 파서에 의해서 반환되는 데이터 구조에 수정, 강화를 함
- Parser
  - 개요
    - query string이 valid syntax인지 체크
    - parse tree를 제작
      - parser / lexer는 bison과 flex로 구현됨
  - lexer
    - `scan.l`에 정의되어있으며, identifiers(SQL key words)를 확인하는 임무를 맡음
      - flex를 사용해서 `scan.c`로 변환
    - 각 keyword나 identifier가 발견되면, token이 생성되어 parser에게 넘어감
  - parser
    - `gram.y`에 정의되어 있고, grammer rule과 action(rule is fired될 떄 동작)의 집합으로 구성됨
      - bison을 사용해서 `gram.c`로 변환
    - action의 코드는 parse tree를 구성하는데에 사용됨
- Transformation Process
  - parse tree를 input으로 넣고, semantic interpretation을 행함(어떤 테이블, 함수, 연산자가 참조되어야 하는지 해석)
  - raw parsing과 semantic analysis를 분리하는 이유 = *system catalog lookups은 하나의 transaction에서만 시행될 수 있고, query string을 받자마자 transaction을 시작하고 싶지 않음*
    - *이게 무슨 소리*
    - The raw parsing stage is sufficient to identify the transaction control commands (BEGIN, ROLLBACK, etc), and these can then be correctly executed without any further analysis. Once we know that we are dealing with an actual query (such as SELECT or UPDATE), it is okay to start a transaction if we're not already in one. Only then can the transformation process be invoked.
  - transformation process에서 생성된 query tree는 raw parse tree와 대개 유사하나, 자세히는 많은 차이가 존재
    - `FuncCall` -> `FuncExpr` or `Aggref`
    - query tree에 칼럼과 식 결과의 actual data types 정보가 query tree로 추가됨
