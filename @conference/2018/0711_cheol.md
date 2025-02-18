# 철사부와의 미팅

- 진정한 문제 해결이란
- 차익 거래의 본질
  - 차익 거래의 레벨
- 모델을 잘 짜기 위해서
- 실제 거래보다 중요한 것은 시뮬레이터
- 앙상블 전략을 사용

## 진정한 문제 해결이란

어떠한 문제가 존재할 때, 그것을 못본 척 하는게 아니라 `~~ 하면 될 것 같은데` 라는 생각을 갖고, 즉 가설을 세워서 그것을 검증하고 적용하는 것.

이제까지 나는 프로그래밍에 관해서만 `~~ 하면 될 것 같은데` 라는 생각을 갖았으나, 현실세계의 문제에서도, 아이디어의 관점에서 적용할 수 있는 생각이다.

사실, 프로그래밍도 현실 세계의 문제해결을 위한 도구이기 때문에, 오늘 철이와의 얘기에서 들었던 통계학도 같은 맥락으로 현실 세계의 문제해결을 위한 도구라고 생각할 수 있다. 그러한 도구를 잘 갖추어 놓으면 문제를 잘 해결할 수 있는 사람이 될 수 있을 것이다.

## 차익 거래의 본질

- 결국은 싸게 사서 비싸게 파는게 요지
  - 내가 초점을 두는 숫자는 따로 정해져 있고, 나머지는 전부 노이즈
  - 어떻게 내가 원하는 숫자로만 거래를 할 수 있을까?
  - 어떻게 노이즈를 제거할 수 있을까?
  - 어떻게 변동성을 제거할 수 있을까?

### 차익 거래의 레벨

- 레벨1
  - 하나의 물건을 서로 다른 시장에서 다른 가격으로 무조건 더 비싼 경우에 판다.
- 레벨2
  - 하나의 물건을 사고 파는데, 두 개의 시장에서 거의 대부분 한 시장이 더 비싼 경우에도 이득을 보며 사고 팔 수 있다.
- 레벨3
  - 서로 다른 시장에서 서로 다른 물건을 사고 팜. 이때에, 다른 물건끼리의 상관관계를 파악함 평균을 벗어나는 가격의 경우는 특이값임. 그때에 행동 개시

## 모델을 잘 짜기 위해서

금융 상품의 모델링을 잘 하기 위해서는 직접 노가다를 해보는 수 밖에 없다.

자기자신이 여러가지 모델을 시험하면서 감각을 찾는 수 밖에 없다.

모델을 짜면 검증을 해야하는데, 이는 시뮬레이터로 해야한다.

## 실제 거래보다 중요한 것은 시뮬레이터

데이터를 잘 축적하는 이유는 데이터를 바탕으로 시뮬레이터를 돌리기 위해서다.

시뮬레이터를 중시하는 이유는 다음과 같다.

1. 자신이 만든 프로그램이 정말로 잘 동작하고 있는지 확인하기 위해서(실제 거래기록과 시뮬레이터터의 결과와의 대조)
2. 자신의 모델을 검증하기 위해서

## 앙상블 전략을 사용

모델 하나만으로 프로그램을 돌린다면, 그 모델에 어긋난 움직임이 있을 때에 손해가 불가피하다. 그러므로, 실전 모델은 앙상블 전략을 사용해서 여러 모델을 잘 조합할 수 있도록 한다.

기초적인 통계적 지식 이후는 아이디어 싸움. 그리고 실행력.
