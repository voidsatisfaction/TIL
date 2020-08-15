# Architecture

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
      - 부분 성공(x)
      - 모든 것이 일어났거나 아무것도 일어나지 않거나
  - **Consistency**
    - A transaction is a correct transformation of the state.
    - The actions taken as a group do not violate any of the integrity constraints associated with the state.
    - *구체적으로 무엇인지?*
    - DB에 작성된 데이터는 모든 rules에 대해서 valid해야 함
      - constraints, cascades, triggers 들의 combination
  - **Isolation**
    - 하나의 transaction은 다른 transaction에 영향을 주지 않음
      - transaction은 내부 구현적으로는 concurrent하지만, 논리적으로는 순차적으로 실행되는 것 처럼 보임
  - **Durability**
    - transaction이 성공적으로 commit되면, 해당 변화는 DBMS failure에도 변함이 없음
