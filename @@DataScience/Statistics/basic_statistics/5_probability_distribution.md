# 확률 분포

**항상 어떤 사상이 확률 번수가 되는지 의식하자.**

- 이산형 확률분포
  - 초기하 분포
  - 이항 분포
  - 포아슨 분포
- 연속형 확률분포

## 이산형 확률분포

### 초기하분포(hypergeometric distribution)

기댓값

![](./images/ch5/hypergeometric_expectation1.gif)

![](./images/ch5/hypergeometric_expectation2.gif)

분산

![](./images/ch5/hypergeometric_variance1.gif)

![](./images/ch5/hypergeometric_variance2.gif)

- 두 종류의 A, B를 갖는 N개의 어떤 물체가 있음, 개수의 구성은 각각 M, N-M개로 둠. 이 집단으로 부터 무작위로 n개를 추출할 경우, A가 x개, B가 n-x개 라고 한다면, x의 최소값은 0(n < N-M의 경우)혹은 n - (N - M) (n >= N - M의 경우) 이며, 최댓값은 n(n < M의 경우) 혹은 M (n >= M 의 경우) 이다.
  - 이때, 위와같이 n개 추출에서 n개가 될 확률은, `f(x) = MCx * (N-M)C(n-x) / NCn`, `x=Max(0, n-(N-M)), ...., Min(n, M)`
  - 이러한 확률분포를 초기하분포라고 함
    - 이것이 왜 확률분포가 되는지는 `(1+t)^M * (1+t)^(N-M) = (1+t)^N`의 n번째 계수를 x를 이용해서 구하면 됨
- 특징
  - 비복원 추출
    - 복원추출인 경우, 단순 이항분포가됨
- 확률변수의 기댓값, 분산
  - `E(X) = n(M/N) = np`
  - `V(X) = n{M(N-M)/N^2}{(N-n)/(N-1)} = np(1-p){(N-n)/N-1}`
    - N이 무한히 크면, 이항분포의 경우와 일치함
    - **증명이 재미있음**

### 이항분포(binomial distribution)

이항분포의 확률 질량 함수

![](./images/ch5/binomial_distribution.gif)

이항분포가 확률분포인 것의 증명

![](./images/ch5/binomial_distribution_sum.gif)

이항분포의 표현

![](./images/ch5/binomial_distribution2.gif)

이항분포의 기댓값

![](./images/ch5/binomial_expectation.gif)

이항분포의 분산

![](./images/ch5/binomial_variance.gif)

증명이 재미있음

- 베르누이 시행
  - 두 종류의 가능한 결과(성공 S, 실패 F)를 발생시키는 실험이나, 관찰이 있으며, 그것의 확률을 각각 p, 1-p 라고한다. 이것을 같은 조건에서 그리고 독립적으로 n번 반복하는것
- 이항분포
  - 베르누이 시행에서 나온 확률 분포
  - 확률론에서 역사적으로 매우 오래되었고, 정규분포와 포아슨분포의 모양을 확인할 수 있음
- 이항분포 특징
  - 기댓값: p확률로 성공하니까 n번했을 때, 평균적으로 n*p회 성공하게 되는것
  - 분산: p=1/2 일 때, 최대가 되는데, 이는, 어떤 것이 일어날 확률이 1/2 일때, 예측하기 힘든것과 같다.
    - 만일 p=3/4 라면 p확률이 더 높기때문에 예측하기가 나름 쉬울것이다.

### 포아슨 분포(Poisson distribution)

포아슨분포의 확률 질량 함수

![](./images/ch5/poisson_distribution.gif)

포아슨분포가 확률분포인 것의 증명

![](./images/ch5/poisson_distribution2.gif)

포아슨분포의 기댓값

![](./images/ch5/poisson_expectation.gif)

포아슨분포의 분산

![](./images/ch5/poisson_variance.gif)

- 포아슨 분포
  - 이항 분포에서 n이 충분히 크고(즉, 대량의 관찰), p가 작을 경우(즉, 매우 희소한 현상), 두 경향에 의하여, 많지는 않지만 어느정도의 사상 x가 일어나는 것이 관찰된다.
    - 부동산 계약성립에 도달하는 확률(p=0.002)과 신청횟수(n=1000) 가 있을 때, 계약 성립이 3건이 될 확률은 1000C3 * p^3 * (1-p)^997
    - E(X) = np = 2
  - 단위 시간 / 단위 거리 / 단위 면적 / 단위 체적 안에 어떤 사건이 몇 번 발생할 것인가
  - 소수의 법칙에 적합한 사상의 확률 분포
  - 조건
    - 어떤 구간은 더 짧은 작은 단위의 구간으로 나눌 수 있고, 이 구간에서 어떤 사건이 발생할 확률은 전체 척도 중에서 항상 일정해야 함
    - 단위 구간 당 사상은 독립적으로 발생함
    - 단위 구간 당 사상이 일어날 확률은 시간의 흐름에 따라서 변하지 않음
    - 특정 구간에서의 사건 발생확률은 그 구간의 크기에 비례한다.
  - 예시
    - 하루동안의 교통사고건수
    - 대량생산의 불량품수
    - 파산건수
    - 화재건수
    - 포탄명중수
    - 유전자 돌연변이수
    - 안전관련 현상
    - 15초간 고속도로 톨게이트에 차가 몇대나 지나갈 것인가
    - 세계 2차대전 독일군에 의한 런던 폭격의 명중 수(0.25km^2 단위로)
- 포아슨 분포의 응용
  - 현실 사상이 발생될 확률의 근사를 위해서 사용됨
  - 확률 변수가 포아슨 분포를 따르는지 확인하는 것은 어려울 수 있음
- 포아슨 소수의 법칙(Poisson's law of small numbers)
  - np -> lambda가 되도록 n->무한대, p->0이 되는 극한에서는, 각 x에 대하여 `nCx*p^x*(1-p)^(n-x) -> e^(-lambda)*(lambda^x)/x!`이 성립함

### 기하 분포(Geometric distribution)

기하 분포 확률 질량 함수

![](./images/ch5/geometric_distribution.gif)

기댓값

![](./images/ch5/geometric_expectation.gif)

분산

![](./images/ch5/geometric_variance.gif)

- 기하분포
  - 베르누이 시행을 다른 관점에서 생각
  - 시행 횟수를 미리 결정하지 않고, 처음 성공 S가 출현할 때 까지 계속 시행.
  - **처음 S가 나올 때 까지 총 시행 횟수를 확률 변수 x로 둠**
  - 예시
    - 시간을 1, 2, 3 ... 등으로 이산적으로 생각할 때, 처음으로 S를 얻을 때 까지 기다리는 시간의 길이의 확률분포
      - 이산적 기다리는 시간 분포(waiting time distribution)
    - 어떤 풍수재해는 1년동안 일어날 확률이 0.04이면, 이것이 일어나는 것은 평균적으로 몇년후인가? 또한, 10년 이내에 일어나는 확률은 어느정도인가?
      - 재해의 확률이 매우 작다고 해도, 언제든지 충분히 일어날 수 있는 확률이 존재함
      - 표준편차가 매우 크다.
- 기하분포의 특성
  - 기댓값이 `1/p`가 되는것은, 예를들어, 확률이 `1/50`일때, 그 역수는 50, 즉, 50번은 시행해야지 S가 한 번 나온다는 것을 직관적으로 의미
- c.f
  - 어떤 것이 일어난 횟수를 세는 것에 의해 생기는 데이터를 계수형(計数型)이라고 부름
    - 예를들어, 불량품의 개수, 교통사고의 건수 등
  - 애초에 "불량품이란 무엇인가", "교통사고란 무엇인가"를 미리 정의해두는 것은 모집단을 정하는 것과 함께 매우 중요함

### 음이항 분포(Negative binomial distribution)

음이항분포 확률 질량 함수

![](./images/ch5/negative_binomial.gif)

기댓값

![](./images/ch5/negative_binomial_expectation.gif)

분산

![](./images/ch5/negative_binomial_variance.gif)

- 음이항 분포
  - k번째의 성공을 얻을 때 까지 실패 횟수를 확률변수 x로 두었을 때의 분포
- 특성
  - 처음 성공을 얻을 때 까지의 실패 횟수를 확률변수 x로 두었을 때의 분포의 기댓값과 분산을 각각 k배 하면 음이항 분포의 기댓값과 분산을 구할 수 있음

### 이산형 균일분포(Uniform distribution of discrete type)

확률 질량 함수

`1/N, x = 1, 2, ..., N`

기댓값

![](./images/ch5/uniform_discrete_expectation.gif)

분산

![](./images/ch5/uniform_discrete_variance.gif)

- 이산형 균일분포
  - 시행에 대한 표본 사상의 모든 표본점이 같은 확률을 갖는 확률 분포
  - 예시
    - 주사위를 던졌을 때 나온 눈을 확률변수 X로 둔 확률분포

## 연속형 확률분포