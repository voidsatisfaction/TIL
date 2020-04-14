# DB Modeling

- 의문
- 개요
- 실전 팁

## 의문

## 개요

## 실전 팁

- redundant한 관계는 최대한 갖지 않는 것이 좋음
  - 즉, 많은 화살표(혹은 edge)는 필요 없다
- 암묵적인 로직 보다는 명시적인 field 추가
  - 예를들어, `user_id`라는 필드에 null값이 허용되는 경우, 해당 `user_id`가 `null`이면 `is_user`가 암묵적으로 `false`라고 생각하지 말고, 명시적으로 `is_user`라는 필드를 데이터베이스 column으로 두어서 모델을 보는 사람이 쉽게 파악할 수 있도록 한다
    - column 1개 추가 vs 명시성의 tradeoff
