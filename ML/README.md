# Machine Learning

- 의문
- 기계학습 개요
  - 표의 이해
- 대표적 종류
  - Supervised learning
  - Unsupervised learning
  - Reinforcement learning

## 의문

## 명심해야 할 것

- **기계학습은 문제 해결을 위한 '도구'이다**
- **일단 만들어보고, 그 다음에 블랙박스를 공부하라**
  - 중요한것은 만드는것!
- 데이터 사이언티스트나 기계학습 엔지니어의 대부분의 일은 데이터 수집과 전처리에 있다.
  - 모델 짜는데에는 10%의 시간밖에 들이지 않음

## 기계학습 개요

- 개요
  - **간단한 선형 함수로 이루어진 거대하고 복잡한 함수를 과거의 방대한 데이터를 기반으로 생성**
    - *음 근데 이건 deeplearning과 관련깊은거 아닌가?*
- 의의
  - 공식의 대중화
    - 과거에는 일부 지식인들만 수학을 사용하여 함수를 정의하고 이해하는것이 가능했으나, 이제는 누구나 함수를 제작할 수 있도록 가능하게 만든 툴이 ML

### c.f) 표의 이해

인류 최대의 발명품?

- 표(데이터 셋)
  - row = instance, record, case, observed value
  - column = feature, attribute, variable, field

## 대표적 종류

- Supervised learning
- Unsupervised learning
- Reinforcement learning

### Supervised learning

Supervised learning 큰 그림

![](./images/supervised_learning1.jpg)

키워드: 역사 -> 예측

- 대표 문제
  - classification
    - 예측결과가 이산적인 값
  - regression
    - 예측결과가 숫자나 연속적인 값

### Unsupervised learning

키워드: 탐험 -> 인사이트

- 대표 문제
  - clustering
    - 비슷한 데이터를 그루핑 & 그룹에 identity부여
    - 행렬의 행을 기준으로 비슷한 그룹끼리 묶어주는 역할
  - transforming
    - *??*
  - association
    - 비슷한 특성을 그루핑 & 그룹에 identity부여
    - 행렬의 열을 기준으로 비슷한 그룹끼리 묶어주는 역할

### Reinforcement learning

강화학습 기본 모델링 도식

![](./images/reinforcement_learning1.jpg)

키워드: 경험 -> 개선
