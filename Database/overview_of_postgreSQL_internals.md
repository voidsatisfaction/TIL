# Overview of PostgreSQL Internals

- 의문
- The Path of a Query
  - Connection
  - Parser
  - Rewriter
  - Planner / Optimizer
  - Executor

## 의문

- *왜 tree의 형태롤 파싱의 결과물을 제공 하는 것일까?*

## The Path of a Query

- ① \[connection\]
  - application program에서 PostgreSQL 서버로의 커넥션 확립
  - application program은 서버로 쿼리를 전달하고, 서버로 부터 받은 결과를 수신
- ② \[parser stage\]
  - correct syntax
  - query tree 생성
- ③ \[rewrite system\]
  - rewrite system이 parser stage에서 생성된 query tree를 받고, query tree에 *적용할 룰(system catalogs)을 찾음*
    - *구체적으로 그 룰이라는게 무엇인지?*
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
      - *gunicorn 설정을 gevent로 했을 경우에는 process가 아닌 thread에 connection이 할당되어서 overflow 이슈가 생기는 것 아닌가?*
  - master process(이름: postgres)가 존재
    - 커넥션 요청이 오면 master process가 새 server process를 spawn
      - *커넥션 풀이 있어도?*
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
      - parser, lexer는 bison과 flex로 구현됨
        - bison과 flex는 임의의 파일 포멧을 파싱할 수 있는 unix utility
  - lexer
    - `scan.l`에 정의되어있으며, identifiers(SQL key words)를 확인하는 임무를 맡음
      - flex를 사용해서 `scan.c`로 변환
    - 각 keyword나 identifier가 발견되면, token이 생성되어 parser에게 넘어감
  - parser
    - `gram.y`에 정의되어 있고, grammer rule과 action(rule is fired될 떄 동작)의 집합으로 구성됨
      - bison을 사용해서 `gram.c`로 변환
    - action의 코드는 parse tree를 구성하는데에 사용됨
- Transformation Process
  - **parse tree를 input으로 넣고, semantic interpretation을 행함(어떤 테이블, 함수, 연산자가 참조되어야 하는지 해석)**
  - raw parsing과 semantic analysis를 분리하는 이유 = *system catalog lookups은 하나의 transaction에서만 시행될 수 있고, query string을 받자마자 transaction을 시작하고 싶지 않음*
    - *이게 무슨 소리*
    - The raw parsing stage is sufficient to identify the transaction control commands (BEGIN, ROLLBACK, etc), and these can then be correctly executed without any further analysis. Once we know that we are dealing with an actual query (such as SELECT or UPDATE), it is okay to start a transaction if we're not already in one. Only then can the transformation process be invoked.
  - transformation process에서 생성된 query tree는 raw parse tree와 대개 유사하나, 자세히는 많은 차이가 존재
    - `FuncCall` -> `FuncExpr` or `Aggref`
    - query tree에 칼럼과 식 결과의 actual data types 정보가 query tree로 추가됨

### ③ Rewriter(Rule system)

- rule system
  - views, ambiguous view update의 스펙지원
  - **query rewriting**
    - input, output은 query tree

### ④ Planner / Optimizer

- 개요
  - 최적의 execution plan을 찾아주는 역할
    - 같은 결과를 생성하더라도, 다양한 방법으로 실행될 수 있음
  - computationally feasible한 경우에, query optimizer는 가능한 실행 플랜을 각각 검사하고, 결과적으로 가장 빠른 execution plan을 선택
    - 사실 이 과정 조차도, time, memory space를 사용하게 됨. 특히 많은 수의 join operation이 포함되는 쿼리에서 더더욱 그런 경향이 있음
    - PostgreSQL에서는 reasonable query plan(best는 아님)을 reasonable amount of time에 찾기 위해서 Genetic Query Optimizer를 사용(join의 숫자가 threshhold를 넘어섰을 때)
  - Planner's search procedure
    - path라는 데이터 구조를 기반으로 planner의 search procedure가 이루어짐
  - 가장 효율 좋은 path가 선택된 뒤에, full-fledged plan tree가 만들어져서 executor로 보내짐
- 구체적인 Plan 생성 방법
  - planner/optimizer는 쿼리에서 사용되는 개별 relation(table)을 스캐닝하기 위한 plan들을 생성
  - 각 relation에 사용가능한 indexes에 기반하여 가능한 plans가 결정됨
    - sequential scan은 항상 plan에 포함
    - **ORDER BY** 절의 내용과 일치하는 인덱스에 대해서도 index scan이 행해지고, **JOIN**을 할 때 sort ordering이 필요한 경우에도 사용됨
  - JOIN의 경우
    - 종류
      - nested loop join
        - (index가 없는 경우)`O(n^2)`인 가장 쉬운 방법
        - right relation이 인덱싱 되어있으면 효율적인 방법으로 바뀜
      - merge join
        - join 전에, 각 relation을 join attribute(`JOIN on ...`)을 가지고 소팅 해둠
        - *그리고 두 relation을 병렬적으로 스캐닝하면서, 서로 매칭되는 row를 join row로 결합*
          - 구체적으로 어떻게 한다는 거지? -> 오, 가능할듯
      - hash join
        - 하나의 relation을 스캐닝해서 해시로 만들고, 다른 relation과 매칭해서 join 실행
    - When the query involves more than two relations, the final result must be built up by a tree of join steps, each with two inputs. The planner examines different possible join sequences to find the cheapest one.
    - If the query uses fewer than geqo_threshold relations, a near-exhaustive search is conducted to find the best join sequence. The planner preferentially considers joins between any two relations for which there exist a corresponding join clause in the WHERE qualification (i.e., for which a restriction like where rel1.attr1=rel2.attr2 exists). Join pairs with no join clause are considered only when there is no other choice, that is, a particular relation has no available join clauses to any other relation. All possible plans are generated for every join pair considered by the planner, and the one that is (estimated to be) the cheapest is chosen.
- finished plan tree
  - 구성
    - nodes
      - sequential or index scans of the base relations
      - nested-loop, merge, hash join nodes
      - auxiliary steps
    - 대부분의 node는 selection이 가능
      - 특정 boolean 조건을 만족하지 못하면 버리는 기능
    - projection
      - scalar expression의 평가

### ⑤ \[WIP\]Executor

https://www.postgresql.org/docs/12/executor.html

- 개요
  - planner, optimizer가 생성한 plan을 받고, 재귀적으로 필요한 rows의 집합을 추출하기 위해서 작업
    - *demand-pull pipeline mechanism*
      - plan node가 호출되면, one more row를 조달하던지, delivering rows 작업이 끝났다고 report해야 함
- 구체적인 설명(예시)
  - top node가 `MergeJoin` node라고 가정하면, merge가 실행되기 전에, 두 rows가 fetched 되어야 함
