# DB

- 의문
- General
  - Transaction

## 의문

## General

### Transaction

- 정의
  - **information processing s.t indivisible individual operation**
- 특징
  - 각 transaction은 success or fail
    - partially complete는 없음
  - data-oriented resources는 transactional unit속의 모든 operation이 성공적으로 끝나야만, 영구적으로 변경 사항이 반영됨
  - 애플리케이션을 reliable하게 만드는 효과가 있음
  - programming model을 simplify하기 위해서 사용됨
    - ignore partial error
- 방법론
  - **Rollback**
    - db integrity를 중간 상태를 저장하면서 확보함
    - 이러한 중간 상태를 활용해서 원래 상태로 복원
    - 수정 이전의 데이터 이미지의 상태를 저장
    - transaction 도중에 실패하는 경우, 원래 이미지를 이용하여 롤백함
  - **Rollforward**
    - DB는 transaction log(journal)를 저장 -> DBMS의 failure -> Rollback을 사용한 기존 이미지 복원 -> transaction log(journal)에 기록된 최신 transaction을 기반으로 해당 연산 다시 실행 -> DBMS failure당시 실행되었던 transaction까지 반영된 consistent db 생성
  - **Deadlocks**
    - 두 transaction이 DB의 같은 부분에 접근 할 경우, 발생할 가능성
    - Transaction processing system에서는 이러한 deadlock을 탐지하고, 두 transaction을 cancel후 rollback후 다시 진행시킴
      - 혹은, 하나만 cancel시키고 나머지는 잠시 뒤에 다시 시작하도록 함
  - **Compensating transaction**
    - commit and rollback 매커니즘이 사용불가능하거나, 좋지 못한 선택지일 경우, 실패한 transaction을 undo하고 시스템을 이전 상태로 restore하는 것
- ACID 기준
  - **Atomicity**
    - transaction은 더 이상 분리가 불가능(원자)
      - 부분 성공(x), 모든 것이 일어났거나 아무것도 일어나지 않거나
  - **Consistency**
    - DB상의 불변량이 항상 참이 되도록 하는 것
      - e.g
        - 회계 시스템에서 credits와 debits는 항상 밸런스가 맞아야 함
        - constraints, cascades, triggers 에 대해서 새로 삽입하는 데이터는 항상 valid해야 함
      - DB에서 걸 수 있는 제한만으로는 달성하기 힘듬
      - 엄밀히 말하면 ACID에서 C는 빠져야 함(DB 자체에만 의존하는게 아니므로)
    - Application의 영역
      - Atomicity, Isolation, Durability는 DB의 영역
    - A transaction is a correct transformation of the state.
    - The actions taken as a group do not violate any of the integrity constraints associated with the state.
    - *구체적으로 무엇인지?*
  - **Isolation**
    - 하나의 transaction은 다른 transaction에 영향을 주지 않음
      - transaction은 내부 구현적으로는 concurrent하지만, 논리적으로는 순차적으로(serial) 실행되는 것 처럼 보임(**serializability**)
    - 다수의 DB client들이 하나의 row에 접근할 때 문제가 생기는 것을 방지(논리적으로 순차적으로 실행되는 것 처럼 보이므로)
      - race conditions
      - e.g)
        - 게시판 글의 뷰 수를 증가시키는 경우
    - DB는 isolation level을 갖음
  - **Durability**
    - transaction이 성공적으로 commit되면, 해당 변화는 DBMS failure에도 변함이 없음
      - hardware fault, database crash가 발생해도
    - 종류
      - single-node db의 경우
        - disk가 corrupt되어도 회복할 수 있는 것
      - repliocated db의 경우
        - data가 다른 노드들에게 성공적으로 복사된 다음에 transaction이 성공적으로 commit되었다고 보고하는 것
    - 완벽한 durability는 존재하지 않음
      - 모든 하드디스크와 모든 백업이 전부 망가지면 답이없음
      - 경우의 수
        - 데이터를 disk에 작성하는데, 머신이 죽음 => 데이터는 잃지 않으나, 회복할 때 까지 접근 불가능(복제된 시스템은 사용 가능)
        - correlated fault(전원이 나가거나, 특정 input에 의한 모든 노드가 크래시되는 경우) => 모든 replicas를 한번에 죽일 수 있음, 메모리에 있는 데이터도 다 날라감
        - 비동기 replicated system의 경우, leader가 사용 불가능 해짐 => 최신 데이터 작성은 잃어버릴 가능성 존재
        - 하드웨어 전원이 갑자기 꺼짐 => SSD의 경우 *`fsync`* 가 제대로 동작하지 않을 수 있음
        - storage engine과 filesystem 구현 사이의 사소한 상호작용이 트래킹이 힘든 버그를 생성할 수 있으며, 디스크의 파일을 오염시킬 수 있음
          - *구체적인 예시?*
        - 디스크에 있는 데이터가 점진적으로 아무런 detecting없이 corrupt되는 경우가 존재함
          - historical backup으로 다시 회복시켜야 함
        - SSD의 경우에는 30% ~ 80%의 드라이브가 첫 사용 4년동안 적어도 하나의 bad block을 생성한다고 함. 하드디스크는 bad sector의 비율은 낮으나, 전체적인 failure가 발생할 확률이 높음
