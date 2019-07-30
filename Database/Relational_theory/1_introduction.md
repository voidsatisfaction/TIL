# 관계 대수학 이론

- 참고
- 의문
- 개요
- Terminology
- Princple, Not Products
- Original Model
- Model vs Implementation
- Properties of Relations
- Relations vs Relvars
- Values vs Variables

## 참고

- Database In Depth(Oreilly)

## 의문

- *애초에 관계란 무엇인가? / 그리고 모델은 무엇인가? / 데이터 모델?*
  - 원문을 찾아보거나 위키를 보거나

## 개요

**결국 관계 대수가 이론적 배경이므로, 관계라는 대수의 성질과 연산을 설명하는 것이다. 마치 벡터와 행렬을 이해하는 것과 같다.**

## terminology

- relation ≠ table
- tuple ≠ row
- attribution ≠ column

## Principles, Not Products

- relational model
  - principle임
    - 변하지 않음
  - 현실과 trade-off 할 때에 자기 자신이 무엇을 하는지 완벽하게 파악을 한 뒤에 그 행위를 해야 함

> Those who are enamored of practice without theory are like a pilot who goes into a ship without rudder or compass and never has any certainty where he is going. Practice should always be based on a sound knowledge of theory

## Original Model

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
          - 테이블 <= 대응 => 관계
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
  - integrity feature(constraint)
    - `TRUE`로 평가 되어야 하는 불린 식
    - two integrity rules
      - **entity integrity**
        - primary key 속성은 null을 허용하면 안됨
          - null은 값이 아니라, 값이 알려지지 않았다는 표식
        - **DDD에서도 entity라는 표현을 쓰는데, 관련이 있을 듯 싶다**
      - **referential integrity**
        - foreign key의 값은 반드시 매치되어야 함
  - manipulative feature
    - consists of
      - 관계 연산의 집합(관계 대수 라고도 불림)
      - 관계 할당 연산
        - 관계 모델에서 갱신(`INSERT, UPDATE, DELTE` 등)이 행해지는 방법
        - 관계 식의 결과값 `r MINUS s(r, s는 관계)`을 다른 관계로 할당할 수 있게 함
        - 각각의 연산자는 적어도 하나의 관계를 입력으로 받고 다른 관계를 출력함
          - **출력한것은 또 다른 관계(closure 속성 - 관계 연산은 관계계에 닫혀있음)**
          - 결국 출력한 것을 계속해서 활용 가능
    - 관계 연산의 예시
      - `Restrict`
        - 특정 조건을 만족하는 특정 관계로부터 모든 튜플들을 포함하는 한 관계를 반환
        - `≒ WHERE`
      - `Project`
        - 특정 속성들을 제거한 관계의 모든 튜플들을 포함하는 관계를 반환
        - `≒ SELECT 뒤에 특정 칼럼만 선택`
      - `Product`
        - 두 서로다른 관계들에 각각 포함된, 두 튜플의 콤비네이션인 모든 가능한 튜플들을 포함하는 관계를 반환
        - cartesian product, cross product, cross join, cartesian join 이라고 불림
          - join의 특별한 케이스
      - `Intersect`
        - 어떠한 두 관계에 중복해서 나타나는 모든 튜플들을 포함하는 관계를 반환
        - join의 특별한 케이스
      - `Union`
        - 어떠한 두 관계에 하나만 혹은 둘다 나타나는 모든 튜플들을 포함하는 관계를 반환
      - `Difference`
        - 어떠한 두 관계에서 첫번째 관계에만 나타나고 두번째 관계에는 나타나지 않는 모든 튜플들을 포함하는 관계를 반환
      - `Join`
        - 두 관계의 공통 속성의 공통 값을 갖는 두 튜플의 조합인 모든 가능한 튜플들을 포함하는 관계를 반환(공통 값은 결과 유플에서 단 한번만 출현)
        - natural join
      - `Divide`
        - 하나는 binary이고, 나머지 하나는 unary인 두 관계를 받아들여 unary 관계에 있는 모든 값들에 일치하는 binary relation의 한 속성의(일치하는 속성이 아닌 다른 속성) 모든 값들을 포함하는 관계를 반환
    - 관계 대수라고 할 뿐 아니라 관계 미적분학이라고도 함(relational calculus)

## Model vs Implementation

- 데이터 모델
  - 정의
    - **데이터 구조와 연산등의 추상적이고, 자기 완전(self-contained)적이고, 논리적인 정의**
      - 관계 모델임
      - theoretical
    - 기업의 특정 영구적인 데이터의 모델
      - ≒ 데이터베이스 디자인
      - practical(문제 해결)
  - *관계*
    - 관계는 모델의 일부
      - 유저는 관계가 무엇이고, 어떤 튜플과 속성을 갖으며 어떻게 해석해야 하는지 알아야 함
    - 모델과 구현은 독립적
      - 데이터가 물리적으로 어떻게 저장되고 접근되는지는 관계모델과 관계가 없음
- 구현
  - *주어진 데이터 모델의 구현이란 그 모델을 함께 구성하는 추상 기계의 컴포넌트의 실제기계에 물리적으로 실제화 시킨것*
  - An implementation of a given data model is a physical realization on a real machine of the components of the abstract machine that together constitute that model
  - 예시
    - 물리적으로 디스크에 어떻게 저장되고 어떻게 각각의 데이터 값이 물리적으로 encoded 되거나 indexes path가 존재하는지 알지 못해도 됨
    - 특정 연산의 퍼포먼스 비교

## Properties of Relations

- 모든 관계는 heading과 body를 갖음
  - 관계의 구성
    - heading
      - set of attributes(`attribute-name:type-name` 보통은 type-name은 생략)
      - heading에서 속성의 개수는 degree(arity)라고 함
    - body
      - heading에 따르는 set of tuples
      - 튜플의 개수는 cardinality라고 함
        - 집합론의 기수!
  - **관계는 heading과 body를 포함하고 heading은 attributes를 포함하고 body는 tuples를 포함함, 관계가 직접적으로 tuples를 포함하는 것이 아님**
- 관계는 중복 튜플을 결코 포함하지 않음
  - 왜냐하면 body의 정의가 set of tuples 이기 때문
    - SQL의 실패
- 관계의 튜플들은 순서가 없음
  - body는 집합이기 때문
  - `ORDER BY`는 관계 연산과 전혀 상관이 없음
  - 마찬가지로 heading도 set of attributes 이므로, 순서는 전혀 상관이 없음
- 관계는 항상 정규화 됨(1NF)
  - 하나의 row-column 교차하는 곳에는 올바른 타입의 하나의 값만 존재
- base vs derived 관계
  - 관계대수의 관계연산은 주어진 관계를 기반해서 새로운 관계를 생성할 수 있음
  - base
    - 처음으로 주어진 관계
    - 관계시스템은 명백하게 base relation들을 처음에 제공해야 함
      - SQL에서는 `CREATE TABLE SP ...`
    - 오해
      - 이론적으로 base relation은 derived relation 보다 더 physical 하다는 것은 거짓
      - 오히려 관계 모델은 구현과는 전혀 상관없음(그러므로 구현은 자유롭게 해도 됨)
        - 대수적 추상화이기 때문
  - derived(views)
    - 처음으로 주어진 관계를 기반으로 연산의 결과 새로 나온 관계
    - 이름지을 수 있음

## Relations vs Relvars

- Relations
  - Relation values와 같은 의미
  - **수학의 세계는 immutable의 세계**
- Relvars
  - 정의한 테이블들 `CREATE TABLE T ...`
    - `INSERT / DELETE / UPDATE` 연산을 수행하면 해당 테이블의 값이 변화함 즉, 테이블 자체는 값이 아닌, 관계 변수임
    - `INSERT / DELETE / UPDATE`는 관계 할당

## Values vs Variables

- Values
  - 각각의 상수(constant)
    - immutable
- Variables
  - 값의 표현을 갖는 대상
    - 값과 다르게 갱신될 수 있음
    - 현재의 값은 다른 값으로 대체 가능
