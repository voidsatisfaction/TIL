# Reinforce Learning

- 의문
- 강화학습 프레임워크(생각)
- 다양한 Learning 방법과 Environment들

## 의문

- 슈퍼마리오의 경우, 몇 프레임마다 행위나 상태를 저장하는지?

## 강화학습 프레임워크(생각)

![](./images/reinforce_learning1.jpeg)

- Marcov Decision Process
  - 구성 요소
    - Agent
      - environment속에서 action을 행함
    - Environment
      - action에 대한 다음 state와 reward(punishment)를 agent로 제공
  - 목표
    - **\*long-term reward 최대화**
      - exploration
        - 현재의 최선의 판단은 아니지만, 탐험해보는 것
      - exploitation
        - 현재 상황에서 가장 좋아보이는 액션 선택

## 다양한 Learning 방법과 Environment들

- learning의 종류
  - curriculum learning
    - 쉬운 문제부터 차근차근 풀도록 학습구조를 설정
  - imitation learning
    - 선생님을 붙여두고 학습
    - 초기 학습시간 단축
