# 통계적 추정(estimation)

- 의문
- 추정
- 점추정과 구간추정
- 점추정
  - 추정량과 추정값
  - 점추정 방식
    - 모먼트 법
    - 최우법
  - 점추정의 기준(4가지)
  - 점추정의 예시
- 구간추정

## 의문

*통계량은 함수인가?*

- 통계량은 아직 관측에 의해서 값이 정해지지 않은 상태의 것임
  - 따라서, 통계의 관측 input(벡터)에 따라서 output이 달라지므로 일종의 함수라고 할 수 있음

*어떤 함수의 대수화를 한 후에 미분을 해서 0인 좌표는 기존 함수의 미분을 해서 0인 좌표와 같다고 할 수 있는가?*

- 직관적으로는 그렇다
  - log함수는 단조증가

*모집단이 균등분포인 경우의 추정에서 최우법으로 파라미터를 구하는 방법*

- 직관적으로 이해는가는데 엄밀하게 증명하려면?
  - 참고
    - [1](http://m.blog.daum.net/gongdjn/125?np_nil_b=-1)

## 추정

- 표본을 바탕으로, 해당 표본이 추출된 원래 모집단의 모수(모평균, 모분산 등)의 값을 정하는 것
  - 데이터 = 시그널 + 오차
    - 시그널을 빼 내는것이 통계적 추정
- 통계학과 확률론의 차이
  - 모수를 추정하는가?
- parametric vs non-parametric
  - parametric
    - 모수를 알면, 모집단의 분포도 안다고 전제
  - non-parametric
    - 모집단의 분포 보다는 일부의 모수(모평균 등)만 알고싶은 경우
- 용어
  - 추정(estimation)
    - 표본으로부터 모수를 정하는 것
  - 추정량(estimator)
    - 모수를 추정하기 위해서 표본으로부터 구한 통계량
    - 예시
      - mu의 추정량은 X bar
      - sigma^2의 추정량은 s^2
- 표기
  - 추정하고자 하는 모수
    - theta
  - 추정량
    - theta^

## 점추정과 구간추정

- 점추정(point estimation)
  - 모집단의 미지의 모수 theta를 추정하는 경우, 그것을 하나의 값 theta^로 지정하는 방법
  - 특징
    - 오차 존재(오차 평가가 필요 => 추정량의 표본분포를 생각한 확률적 취급이 필요 => 불편추정량, 일치추정량 등의 기준 필요)
- 구간추정(interval estimation)
  - 파라미터의 값이 포함되는 확률이 임의의 값 1-a 이상이라고 보장되는 구간 [L, U]를 구하는 것으로, 처음부터 추정에 어느정도 오차가 있음을 인정한 추정법
    - `P(L <= mu <= U) >= 1-a`
    - L, U는 X1, X2, ..., Xn의 함수, 즉, 통계량이며, 좌변의 확률이 1-a이상이 되도록 표본분포로부터 구함

## 점추정

### 추정량과 추정값

- 추정량
  - 모수를 추정하기 위해서 표본으로 부터 구한 통계량
- 추정값(estimate)
  - 실제로 n개의 관측값이 주어진 경우, 추정량을 실제의 숫자로 계산할 수 있는데, 이를 추정값이라고 함
  - 우리가 현실의 데이터로부터 계산하는 것은 추정값이며, 이것은 추정량의 가능한 값의 하나가 실현되는 것
  - 예시
    - 표본 평균은 어떻게 표본을 추출했느냐에 따라서 변화하는 추정량이나, X1=x1, X2=x2, ..., Xn=xn이 표본으로 주어진 경우에 이것을 대입하여 계산되는 값이 추정값
- **모수를 추정하기 위해서는 어떠한 통계량을 추정량으로 할지 결정하는 것이 중요**

### 점추정의 방식

#### 모먼트 법(적률방법 - method of moments)

- 모먼트를 통해서 모집단에 대해서의 정보를 흡수하는(?), 매우 전형적인 방법
  - 모먼트 도함수와 관계가 있음
- 예시
  - 모집단 분포 = N(mu, sigma^2)

모집단의 1차, 2차 모먼트(mu1, mu2)

![](./images/ch10/method_of_moment1.gif)

표본으로부터 구한 표본 1차 2차 모먼트(mu1^, mu2^)

![](./images/ch10/method_of_moment2.gif)

추정을 위해서, 모집단의 모먼트 = 표본 집단의 모먼트 라고 두면,

![](./images/ch10/method_of_moment3.gif)

모평균 모분산의 추정량

![](./images/ch10/method_of_moment4.gif)

- 일반적으로는 모집단이 k개의 미지의 모수를 갖는 모집단 분포를 따른다고 할 때, 이 분포를 따르는 확률변수를 X라고 하여, 그것을 1차부터 k차까지 모먼트(모모먼트) mu1 = E(X), mu2 = E(X^2), ..., muk = E(X^k)를 생각함
- 그리고 모모먼트 = 표본모먼트 라고 두어서
- mu1, mu2, ..., muk의 모먼트 방정식을 해결

#### 최우법(최대우도추정법 - maximum likelihood method)

- 예시
  - 1을 갖는 확률이 p, 0을 갖을 확률이 1-p인 베르누이 분포 Bi(1, p)가 모집단분포일 경우를 생각
  - 추정해야할 미지의 모수는 p
  - X1 = 1, X2 = 1, X3 = 1, X4 = 1, X5 = 0의 n=5의 표본이 얻어졌다고 함
  - p는 0부터 1까지의 사이의 값을 갖을 가능성이 있으나, 모수가 될 수 있는 값의 집합을 모수공간(parameter space)라고 부르며, Theta로 나타냄
  - 위의 표본이 나올 확률
    - `L(p) = p^4(1-p)`
    - p = 0.2, p = 0.8 중에서 p = 0.8인 경우가 L(p)가 더 크므로, 0.8이 최우값으로 적당
- 최우원리(principle of maximum likelihood)
  - 현실의 표본은 확률이 최대의 것을 실현한 것이라는 가정
- L(p): 우도함수
  - 모수공간 Theta에서의 p의 다양한 값에 있어서 가장 적합한 것을 나타내는 함수로 간주할 수 있으며, 이러한 적합도를 우도(likelihood), 그 함수를 우도함수(likelihood function)이라고 부름
- 최우법(maximum likelihood method)
  - 우도함수를 모수공간 Theta에서 최대가 되도록하는 것을 추정값이나 추정량으로 하는 것
- 최우추정값(maximum likelihood estimate)
  - 우도함수를 최대로 하는 값
  - 우도함수를 미분해서 구할 수 있음
    - 확률 p는 구간 [0 1]에서 존재
- 최우추정량(maximum likelihood estimator)
  - 함수

모수가 하나인 일반적인 우도함수(theta는 모수)

![](./images/ch10/maximum_likelihood_method1.gif)

모수가 여러개인 일반적인 우도함수

![](./images/ch10/maximum_likelihood_method2.gif)

일반적인 우도함수는 곱의 형태이므로 수학적으로 다루기 힘드므로, 로그를 취해서 합의 형태로 변환(**대수우도**)

![](./images/ch10/maximum_likelihood_method3.gif)

최우추정량 theta^는 logL(theta)를 모수공간 Theta에 있어서 최대로 하는 추정량

![](./images/ch10/maximum_likelihood_method4.gif)

베르누이 분포에서는

![](./images/ch10/maximum_likelihood_method5.gif)

![](./images/ch10/maximum_likelihood_method6.gif)

*to be continued*

### 점추정의 기준

- 점추정은 여러가지로 생각할 수 있음
  - 표본평균
  - 중앙값
  - 미드레인지
  - 표본 최대, 최소를 잘라낸 표본평균
- 점추정에서 추정량의 결정 기준
  - 본질
    - **추정량의 표본분포가 모수인 theta의 주변에 집중해있는 것을 타나내는 기준을 만족해야 함**
  - 기준
    - 1 불편성
    - 2 일치성
    - 3 점근정규성
    - 4 유효성

#### 1. 불편성(unbiased)

- 추정량의 기댓값이 모수의 값이 되는 것
  - 평균적 과대 / 과소 추정이 없는 것
- 불편추정량(unbiased estimator)
  - 위의 기준을 만족하는 추정량
- 특히 표본평균, 표본분산(불편분산)의 불편성이 중요함
  - E(X bar) = mu
  - E(s^2) = sigma^2

#### 2. 일치성(consistent)

일치추정량(consistent estimator)의 조건

![](./images/ch10/rule_of_point_estimation1.gif)

- 표본의 크기 n이 커짐에 따라, thetan^(추정량의 표본분포가 n에 의해서 변화하므로, 여기서는 첨자 n을 붙임)이, 그림 11.4와 같이, 모수의 값 theta에 가까워지는 성질
- 확률수속
- 큰수의 법칙과 유사

**불편성과 일치성이 점추정을 하기위한 최소한의 조건**

#### 3. 점근정규성(asymptotic normality)

- 중심극한정리에 의하여 점근 분포(n -> 무한대 인경우의 분포)는 정규분포인 경우가 많음
  - 점근 분포가 정규분포인 경우의 성질을 **점근정규성** 이라고 함
- 점근정규추정량(asymptotically normal estimator)
  - 점근 정규성을 만족하는 추정량
- 예시
  - X bar의 점근분포는 정규분포이므로 X bar는 점근정규추정량임

#### 4. 유효성(efficient)

- 배경
  - 두 추정량 theta^, theta~가 있을 때, 먼저, 두쪽다 불편추정량이며, 일치추정량이라고 함
  - 두 분산을 생각해서 그 우열을 비교해야만 함
  - 불편추정량인 경우 추정량의 기댓값이 모수와 같기 때문에, 분산이 작을 수록, 모수의 값의 주변에 표본분포가 집중해 있다고 생각할 수 있기 때문
    - 그래서 분산이 작을 수록 보다 바람직한 추정량으로 생각할 수 있음
- 유효추정량(efficient estimator) / 최소분산불편추정량(minimum variance unbiased estimator)
  - 어떠한 불편추정량보다도 분산이 작은 추정량
  - 모집단이 N(mu, sigma^2)인 경우 표본평균이 mu의 유효추정량으로 알려져 있음
  - 발견 자체가 매우 어려움
- 점근유효성(asymptotic efficiency)
  - 유효추정량의 발견이 어려운 경우 기준을 좀더 느슨하게
  - 점근분포가 정규분포가 되는 추정량 중에서, 그 점근 분산이 최소가 되는 성질
  - 점근적유효추정량
    - 점근유효성을 만족하는 추정량
    - 최우법의 추정량은 보통 이 기준을 만족

### 점추정의 예시

#### 모집단이 정규분포인 경우의 추정

최우법

![](./images/ch10/point_estimation_normal1.gif)

![](./images/ch10/point_estimation_normal2.gif)

![](./images/ch10/point_estimation_normal3.gif)

![](./images/ch10/point_estimation_normal4.gif)

최우 추정량

![](./images/ch10/point_estimation_normal5.gif)

보통은 불편성은 만족하기 위해서 S^2대신 s^2을 이용(n-1)

모먼트법도 최우법과 같은 결과가 나옴

#### 모집단이 이항분포인 경우의 추정

모집단 분포가 표본 Xi = 0, 1을 내는 모수 p의 베르누이 분포 Bi(1, p)의 이항분포일 때, 우도함수의 대수는 이하와 같음

![](./images/ch10/point_estimation_binomial.gif)

여기서 최우추정량은 p^ = X bar(1이 나오는 상대도수)가 됨

모먼트법도 최우법과 같은 결과가 나옴

#### 모집단이 포아슨분포인 경우의 추정

모집단분포가 모수 lambda의 Po(lambda)일 때, 우도함수의 로그는

![](./images/ch10/point_estimation_poisson1.gif)

![](./images/ch10/point_estimation_poisson2.gif)

lambda^ = X bar

모먼트법도 최우법과 같은 결과가 나옴

#### 모집단이 균등분포인 경우의 추정

모먼트법

모집단 분포가 구간(a, b)의 균등분포(a < b)일 때, a,b가 모수이나,

mu = (a+b)/2, sigma^2 = (a-b)^2/12

이렇게 a,b를 풀면

a = mu - sqrt(3)sigma, b = mu + sqrt(3)sigma

이므로 모먼트법에의한 추정량은

a = X bar - sqrt(3)S, b = X bar - sqrt(3)S

최우법

a = Min{X1, X2, ..., Xn}, b = Max{X1, X2, ..., Xn}

이 경우에는 모먼트법과 최우법이 전혀 다른 추정량을 야기함

- 최우법의 경우
  - a, b가 위와 같지 않을 경우에는, 표본이 X1, X2, ..., Xn이 나올확률이 점점 줄어듬

#### Non-parametric인 경우의 추정

![](./images/ch10/point_estimation_non_parametric1.gif)

![](./images/ch10/point_estimation_non_parametric2.gif)

- 최우법으로는 확률 밀도 / 질량함수를 알 수 없기 때문에 구할 수 없음
- 모먼트법으로 모평균과 모분산을 추정
