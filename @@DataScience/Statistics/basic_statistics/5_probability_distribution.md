# 확률 분포

- 이산형 확률분포
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

## 연속형 확률분포
