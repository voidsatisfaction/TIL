# 다차원 확률 변수

## 동시확률분포와 주변확률분포

### 동시확률분포(Joint probability distribution)

이산형 동시 확률 분포(동시 확률 질량 함수)

![](./images/ch6/joint_probability_mass_function1.gif)

필요 조건

![](./images/ch6/joint_probability_mass_function2.gif)

임의의 사상 A가 나타날 확률

![](./images/ch6/joint_probability_mass_function3.gif)

연속형 동시 확률 분포(동시 확률 밀도 함수)

필요 조건

![](./images/ch6/joint_probability_density_function2.gif)

임의의 사상 A가 나타날 확률

![](./images/ch6/joint_probability_density_function3.gif)

![](./images/ch6/joint_probability_density_function1.gif)

- 동시 확률 분포
  - 확률변수 X, Y를 2차원 벡터로 나타냄 `(X, Y)`
  - 그 확률변수의 벡터 `(X, Y)`에 대한 확률의 매칭(함수)을 동시 확률 분포라 함
  - 2차원 확률 변수의 경우, 사상 역시 2차원 공간 안에 있음
    - 사상이란, (x, y)가 모인 어떤 부분집합

### 주변확률분포(Marginal probability distribution)

주변 확률 분포 식

![](./images/ch6/marginal_probability_function1.gif)

![](./images/ch6/marginal_probability_function2.gif)

- 주변 확률 분포
  - 주변 확률 질량함수
  - 주변 확률 밀도함수
- 특성
  - 주변 확률 분포는 동시 확률 분포로부터 유도됨
    - 역은 성립x
    - 아버지의 신장의 분포 / 아이의 신장의 분포 개개를 알고 있다고 해서 둘 사이의 관계를 알 수 없고, (아버지의 신장, 아들의 신장)에 관한 이차원 분포를 알아야만 함

### 공분산과 상관계수

![](./images/ch6/covariance.gif)

![](./images/ch6/covariance2.gif)

- 2변수의 분산
  - 두 변수 X, Y 사이에 관계가 있으면 하나의 변화는 다른 하나에 영향을 미친다고 생각
- 공분산
  - 확률 변수 X, Y가 각각의 평균으로부터 어떻게 관련되면서 분포되는지를 나타냄
  - 특성
    - `Cov > 0`
      - X, Y는 대소가 같은 경향
    - `Cov < 0`
      - X, Y는 대소가 반대 경향
    - X, Y의 관계의 방향을 나타내지만 그 강함의 절대적 정도를 판단할 기준이 없음
  - 예시
    - 주식 투자에서 A석유 회사, B석유 회사 주식에 동시 투자를 하는 것은 일반적으로 좋지 못함
      - 두 주식의 같은 방향으로의 연동 성이 강하면(Cov > 0) 위기에 대한 리스크가 크다

![](./images/ch6/correlation_coefficient1.gif)

![](./images/ch6/correlation_coefficient2.gif)

- 상관계수
  - 범위가 -1 <= p <= 1
    - 증명은 `Q(t) = V(tX + Y) = E{tX + Y - E(tX + Y)}^2`
  - 두 확률변수의 관계의 절대적 정도를 표현 가능
  - 특성
    - p > 0
      - X, Y는 같은 대소의 방향으로 변화하는 경향이 있음
    - p = 1 or -1
      - X, Y는 `Y = aX + b`로 표현가능 (a > 0 when p = 1)
    - p = 0
      - `Cov(X, Y) = 0`이므로 무상관(uncorrelated) != 독립

공분산

![](./images/ch6/covariance3.gif)

![](./images/ch6/covariance4.gif)

평균

![](./images/ch6/covariance5.gif)

![](./images/ch6/covariance6.gif)

## 조건부확률분포와 독립 확률변수

### 조건부 확률(Conditional probability)

- 조건부 확률은 사상 B가 일어나는 경우에 사상 A가 일어날 확률을 말한다. P(A|B)
- 사상 B가 발생했을 때 사상 A가 발생할 확률은 사상 B의 영향을 받아 변하게 된다.
  - 사상 B가 먼저 발생했다는 것이 아니라 사상 B에 대한 정보를 알게 되므로써(정보의 획득), 사상 A의 확률이 변화한다는 것이 핵심이다.
  - e.g
    - 미국 국민의 소득 분포에서 성별이 남성일 경우의 임금의 로그값의 기댓값은 `E(log(wage) | sex = man)` 이는 성별이 남성이라는 것이 먼저 일어나서 기댓값이 결정되는 것이 아니라, 성별이 남성이라는 정보의 획득 으로 인하여 임금의 로그값의 기댓값이 결정되는 것이다.

조건부 확률

![](./images/ch6/conditional_probability1.gif)

![](./images/ch6/conditional_probability2.gif)

조건부 확률 밀도 함수(conditional probability density function)

![](./images/ch6/conditional_probability_density_function1.gif)

조건부 확률 밀도 함수가 확률 분포임을 증명

![](./images/ch6/conditional_probability_density_function2.gif)

기댓값

![](./images/ch6/conditional_probability_distribution_expectation.gif)

분산

![](./images/ch6/conditional_probability_distribution_variance1.gif)

![](./images/ch6/conditional_probability_distribution_variance2.gif)

연속형 확률 변수일 경우에는 시그마 대신 적분기호를 써서 표현

- 상관 계수 p는 확률변수 X, Y사이의 관계의 전체적인 경향을 보기 위한 지표이고, X, Y의 관련의 근원 정보는 동시확률분포에 포함됨 >> 이를 조건부확률의 시점으로 보자
- 조건부 확률 분포
  - 이 역시 확률 분포임
  - 조건부 기댓값
  - 조건부 분산

### 독립 확률 변수



## 다차원 정규분포
