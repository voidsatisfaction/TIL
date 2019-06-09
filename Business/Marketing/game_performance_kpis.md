# How Do I Know I Have a Healthy Game?

- 참고
  - https://www.gamasutra.com/blogs/TrevorMcCalmont/20130228/187460/
- Engagement
  - Sessions/DAU
  - DAU/MAU
- Retention
  - 방법1
  - 방법2
- Monetization
  - ARPDAU
  - ARPU
  - ARPPU
    - ARPDAU, ARPU, ARPPU 를 구할 때, 광고수익도 포함일까?
  - eCPI
  - LTV
  - Conversion Rate

## Engagement

### Sessions/DAU

- DAU가 하루 평균 얼마나 많이 게임에서 세션을 시작했는지
- 게임 마다 수치 해석이 다름
  - RPG는 세션 길이가 기므로, 보다 적은 수치 기록
- 보통은 3이 높은 수치

### DAU/MAU

- 게임이 얼마나 sticky한지 나타내는 지표
  - 과거 한달간 접속했던 유저들중 오늘도 세션을 시작한 유저들의 수
- 보통은 0.2를 계속 유지하면 높은 수치
- 주의
  - 타 게임과 비교할 때에는, UA캠페인 중에는 보통 이 값이 매우 편향되게 뛸 수 있음을 항상 기억해야 함

## Retention

### 방법1

- 다운로드를 받은 날은 Day0
- Day1에 유저가 세션을 시작하면 retained된 거로 간주
- 언제든 세션 시작하지 않으면 그 날은 retained된 것이 아님
- 같은 날짜에 게임을 다운로드한 cohort 유저들에게 이러한 계산 방식이 적용
- 높은 수치 예시
  - Day1: 35 ~ 40%
  - Day3: 20 ~ 25%
  - Day7: 15%
  - Day30: 5%
- 보통 이 방식을 채택
  - 표본의 크기가 크면 극단적인 경우를 배제할 수 있음

### 방법2

주단위 리텐션의 예

- 다운로드를 받은 날은 Day0
- Day1에 유저가 세션을 시작하면 retained된 거로 간주
- Day2에서 5까지 유저가 쉼
- Day6에서 유저가 돌아와서 세션을 시작함
  - 이 때, Day2 ~ Day5을 retained라고 간주함
- 결국은 한 세션에서 7일 전후로 유저가 retained 되었다고 기록함
- lifetime retention
- 높은 수치 예시
  - Day1: 60 ~ 65%
  - Day3: 50 ~ 55%
  - Day7: 40 ~ 45%
  - Day30: 20%

## Monetization

### ARPDAU

- Average Revenue Per Daily Active User (ARPDAU)
  - 모바일에서 가장 흔히 쓰이는 monetization 관련 지표
- 높은 수치 기준
  - 0.05 달러가 좋은 벤치마크 기준
  - 0.15 ~ 0.25 매우 바람직한 ARPDAUs

### ARPU

- Average Revenue Per User (ARPU)
  - 한 유저당 게임이 얼마나 돈을 버는지
  - 평균적으로 한 유저의 전체 수익성 측정
- 미래에 새로 획득된 유저가 수익을 거둘지에 대한 예측값을 주지는 않음

### ARPPU

- Average Revenue Per Paying User
- 모든 paying user에 대한 평균 수익
- 값의 편차가 큼

#### ARPDAU, ARPU, ARPPU 를 구할 때, 광고수익도 포함일까?

- ARPPU
  - 광고 수익 제외
- ARPDAU, ARPU
  - 광고 수익 포함 따로 제외 따로
  - IAP 비중이 높은 게임인 경우,

### eCPI

- 오가닉 유저를 포함한 게임을 인스톨한 모든 유저들에서, 그러한 유저 한명당 획득하는데에 쓴 비용

### LTV

- LTV는 유저가 애플리케이션을 다운로드한 이후로 해왔던것을 고려 + 앞으로 어떻게 소비할것인지 추측
- 추측 방식
  - 선형 추측
  - 다른 복잡한 방식

### Conversion Rate

- 어떠한 중요한 사건을 일으킨 비율
  - UA에서는 다운로드
  - 유저수익화 관점에서는 첫 IAP
- IAP를 기준으로는
  - 3-6% 에 가까움
  - 10% 이상은 거의 없음
    - 보통은 niche audience를 노림
