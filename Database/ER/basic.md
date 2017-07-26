# ER모델

## Entity

존재하며, 구별 가능한 것.

추상적인 개념이어도 됨.

## Entity Set / Type

같은 종류의 entity를 모은 것. (e.g. 모든 학생, 모든 집 등)

Entity type에는 이름을 부여한다.(e.g. 학생 / 집 등)

## Relation

학생이 집에 산다. 여기에서 학생과 집은 **'산다' 라는 하나의 관련이 있다.**

그리고 **거주**라는 Relation type을 가지게 된다.

## Attribute

Entity가 갖는 성질. 속성값은 정의역(domain)으로 부터 결정한다(e.g. 정수, 실수, 문자열 등)

## Key

속성의 조합. 이 속성값에 의하여 Entity set의 하나의 Entity를 고유하게 식별한다.

e.g. 학생이라는 Entity set에서는 student number가 키가 될 수 있다.

# Relationship Type의 종류

1. 1:1
2. 1:多
3. 多:1
4. 多:多

cf) isa관계도 존재한다. (프로그래밍의 상속과 비슷한 맥락) 속성을 상위 Entity set으로부터 계승한다.

# 문장으로부터 ER모델의 작성

문장

- 보행자가 통행한다.
- 차고가 높은 차량이 다닌다.
- 다나카씨가 통행한다
- 차량이 보행자를 추월한다.
- 다나카씨의 차가 카가와씨를 급히 추월한다.
- 차량의 보행자 추월

ER그림

![ER예시](./assets/ER_model_example.png)

# 고차원의 Entity Type의 예所属所属

![고차원 Entity Type의 예](./assets/ER_high_level_entity_example.png)

# 표상 디자인 : 픽토그램

우선좌석의 예

일본 제약표상그림의 예
