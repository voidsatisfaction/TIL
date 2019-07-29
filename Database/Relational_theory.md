# 관계 이론

## 참고

- Database In Depth(Oreilly)

## 의문

## 1. Introduction

### terminology

- relation ≠ table
- tuple ≠ row
- attribution ≠ column

### Principles, Not Products

- relational model
  - principle임
    - 변하지 않음
  - 현실과 trade-off 할 때에 자기 자신이 무엇을 하는지 완벽하게 파악을 한 뒤에 그 행위를 해야 함

> Those who are enamored of practice without theory are like a pilot who goes into a ship without rudder or compass and never has any certainty where he is going. Practice should always be based on a sound knowledge of theory

### Original Model

- Relational model은 수학의 작은 한 가지
  - 시간에 따라서 내용이 변함 / 발전
- Original model의 구성
  - structural feature
    - relation
      - relation은 types(domains)위에 정의됨
      - type
        - 개념적인 값들의 모임
      - n-ary relation
        - n개의 칼럼을 갖는 하나의 테이블
          - 칼럼 <=> 속성
          - 행 <=> 튜플
        - 종류
          - `1-ary = unary`
          - `2-ary = binary`
          - `3-ary = ternary`
          - ...
      - key
        - 관계 모델은 다양한 종류의 키를 지원
        - candidate key
          - 모든 relational model(정확히는 relvar)은 적어도 하나의 candidate key를 갖음
            - candidate key는 tuple의 unique identifier이다
            - attributes의 combination이 되는 경우도 있음(물론 하나의 attribution도 가능)
          - candidate key는 sets(combinations)으로 나타내짐
            - `{ENO}`와 같은 식으로 나타냄
        - primary key
          - 특별한 조치를 취하기 위하여 선정된 candidate key 들중 하나
        - foreign key
          - 그 값들이 다른 relation의 candidate key의 값들과 일치해야 하는 한 relation의 attributes의 집합(혹은 같은 relation에도 적용)
          - foreign key에 해당하는 값은 반드시 그것에 대응하는 값이 대응하는 다른 relation에도 존재해야함
            - faithful model of reality지향
  - integrity
  - manipulation
