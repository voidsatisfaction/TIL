# Sample distribution

우리가 알고싶은 것은 표본의 평균, 분산, 분포가 아니라, 모집단의 평균, 분산, 분포이다.

*유한 모집단 수정 계수의 증명을 어떻게하지?!*

- 배경
- 모집단과 표본
  - 모집단과 모집단분포
  - 모집단분포의 모수
  - 표본의 추출
- 모수와 통계량
  - 통계량
  - 표본평균과 표본분산
- 통계량의 표본분포
  - 표본분포의 역할
  - 표본합의 표본분포
- 유한모집단과 유한모집단수정

## 배경

- 전체의 특징을 파악
  - 애초에 전체에 대한 정보를 아는 경우
    - 기술 통계학
    - 분석하는 집단의 속성에 대해서 완전히 아는 것이 가능한 경우, 그 분포를 알기 쉽게 요약, 정리하기 위한 수법
  - 부분에서 전체를 추측할 수 있는 경우
    - 표본 추출
    - 무작위로 일부의 대상을 추출하여 전체의 특성을 잘 반영하도록 함
  - 부분에서 전체를 추측하기 힘든 경우(애초에 전체의 수를 확정하기도 힘든 경우)
    - 전수 조사
    - e.g
      - 국세조사

## 모집단과 표본

- 모집단(population)
  - 파악하고 싶은 집단 전체 or 속성값
  - 예시
    - 일본인 의식조사인 경우: 일본인 전체가 모집단
- 모집단을 파악하기 힘든 경우
  - 모집단의 요소가 매우 많은 경우
  - 모집단의 요소가 제품의 파괴강도의 조사 등과 같이 전체 조사가 의미가 없는 경우나, 각각의 조사가 고가이므로 예산상의 제약으로 부터 전체의 조사가 불가능할 경우
  - 내년의 경제성장률과 같이 장래에 일어나기 때문에, 현재는 측정이 불가능한 요소를 포함하는 경우
  - **해결책(통계적 추측)**
    - 모집단으로 부터 그 일부를 선택
    - 그것을 분석
    - 모집단에 대해서 추측
- 표본(sample)
  - 모집단으로부터 분석을 위하여 선택된 요소 혹은 그 속성값
  - 모집단의 일부인 표본에서 모집단의 속성에 대해서 추측을 행함
- 표본추출(sampling)
  - 표본을 선택하는 행위
  - 모집단의 추측이 표본 추출 방식에 의존
- 표본분포
  - 표본에의한 ばらつき를 대응하기 위한 확률적인 취급이 불가결

### 모집단과 모집단 분포

- 모집단을 파악 하고 싶다 => 모집단의 분포(population distribution)를 파악하는 것이 목적
  - 통계학에서는 무한 모집단을 생각하는 경우가 많으므로 확률 분포를 생각하는 경우가 많음
    - 예시
      - 일본인은 유한 모집단이나, 무한모집단으로 생각해도 상관 없음
- 표본 X1, X2, ..., Xn(Xi)
  - **동일 모집단 분포 f(x)를 따르는 n개의 독립 확률변수임**
    - *항상 독립이라는 것을 어떻게 알 수 있는가?*
  - 모집단의 확률분포를 따르는 확률변수이나, 현실에서 다루는것은 그 실제의 값인 관측값이다.
  - f(x)는 문제에 따라서 연속형 또는 이산형이어도 됨
- 표본 크기(n)

### 모집단분포의 모수

- 모집단을 실제로 분석할 경우
  - 모집단 분포가 어떤 알려진 확률분포라는 것이, 이론적 / 경험적으로 알고 있는경우
    - Parametric의 경우라고 불림
    - 모집단을 결정하는 **파라미터** 가 존재
      - 포아슨 분포에서는 lambda
      - 정규분포에서는 mu, sigma^2
    - 통계적 추측에서는 파라미터를 모수(parameter)라고 부름
    - 포아슨 분포의 예시
      - 교통사고에 의한 1일당 사망자의 수
        - 교통사고 발생률은 매우 낮음
        - 그러므로 포아슨 분포
        - lambda값만 알면 모집단 분포에 대해서 모두 알 수 있음
  - 모집단 분포가 알려지지 않은 경우
    - Nonparametric
    - 모집단 분포에 관계없이 널리 정의 가능한 파라미터로 모집단 분포를 분석함
      - 분포의 위치
        - 모평균
        - 중앙값
        - 최빈값
      - 분포의 흩어짐
        - 모분산
        - 렌지(range)
      - 왜도
      - 첨도
    - 예시
      - 세계 각국의 면적이나 인구의 분포

### 표본의 추출

- 표본의 추출
  - 모집단에 속하는 요소 전부의 관측값을 얻는 것이 불가능한 경우
- 표본추출의 방법
  - 복원 추출(sampling with replacement)
    - 추출한 요소를 다시 모집단에 돌려 그 뒤의 추출 대상으로 하는 경우
  - 비복원 추출(sampling without replacement)
    - 추출한 요소를 다시 모집단에 돌려 그 뒤의 추출 대상으로 하지 않는 경우
    - 일반적인 실험이나 조사에서는 비복원 추출을 이용
      - N(집단 크기)이 n(표본의 크기)에 비교해서 매우 크면 거의 차이가 없음
- 비복원 추출
  - NCn의 경우의 수가 있음
  - **단지 우리는 위의 경우의 수 중 하나만 선택된 것임**
  - 모집단의 요소를 구체적으로 표본으로 선택하는 방법들
    - 단순 무작위 샘플링(단순무작위추출)
      - 모집단의 각 요소가 표본에 포함될 확률(추출률)을 일률적으로 `n/N`으로 둠
      - 가장 기본적이고 중요한 추출 방식
      - 난수가 사용되는 경우도 존재
    - 다른 방식은 생략

## 모수와 통계량

### 통계량

- 모집단분포 f(x) 특정하기 위한 대표적 모수
  - 모평균(population mean)
  - 모분산(population variance)
  - 위의 모수들을 이용해서 많은 사실을 알 수 있고, 다른 집단과 비교도 가능
    - 그러므로 위와같은 다양한 모수들을 파악하는 것이 중요
- 표본 조사
  - 전수조사가 힘드므로, 크기 n의 표본 X1, X2, ..., Xn을 가져와서, 표본평균 `X bar = (X1 + X2 + .. + Xn) / n`을 이용함. 이것은 직관적으로는 명확하나 그 이유는 무엇인가.
    - E(X bar) = mu
    - 대수의 법칙으로 부터 n이 커짐에 따라 X bar -> mu (확률수속)
  - 위의 두 사실이 성립하므로, 모집단의 mu에의 중요한 단서가 되기 떄문
- 통계량(statistic)
  - 표본을 요약하여, 모집단의 모수의 여러가지 추정에 사용되는 것
  - **표본의 요약이므로, 미지의 파라미터는 포함되지 않음**
  - 종류
    - 표본의 평균
    - 분산
    - 표준편차
    - median
    - 최소값
    - 최대값
    - 상관계수 등 많은 것들이 존재
  - 모집단의 분포의 특징을 요약하는 것에 적합한 통계량을 선택하는 것이 중요
    - 예를들어 모집단의 분산, range를 생각하면, 통계량으로 각각 표본의 분산, 최대값 최소값이 중요함
- 표본 분포(sampling distribution)
  - 통계량 `t(X1, ..., Xn)` 의 확률분포를 그 통계량의 표본 분포라 함
  - 통계량의 표본분포는, 모집단 분포에 의존하며, 다중적분을 필요로하므로 정확히 구하는 것이 힘든 케이스도 존재
    - 하지만 모집단이 정규분포일 경우, 표본의 평균, 분산의 정확한 표본분포를 구하는 것이 가능
    - *중심극한 정리에 의해서 n >= 30일 경우에는 표본의 평균, 분산, 메디안의 분포를 정규분포로 근사적으로 구할 수 있음*
      - 분산, 메디안까지?

### 표본평균과 표본분산

- 모집단의 특성을 나타내는 대표적 모수
  - 모평균
  - 모분산
  - 이유
    - mu와 sigma^2는 분포의 위치와 분포를 규정하기 때문
    - 모집단분포가 정규분포의 경우, 이 두 모수 mu, sigma^2로 모집단분포의 특성을 완전히 나타내기 때문
- 위의 이유로, 표본 평균, 표본 분산이 단서가 됨

#### 표본 평균

표본 평균

![](./images/ch9/sample_mean.gif)

표본 평균의 평균

![](./images/ch9/sample_mean_expectation.gif)

표본 평균의 분산

![](./images/ch9/sample_mean_variance.gif)

- X bar(표본 평균)는 mu를 과대, 과소도 아닌 평균적으로 추정 함
- 또한, n이 커질수록 mu에 집중하는 경향이 보임

#### 표본 분산

표본 분산(불편 분산)(unbiased variance)

![](./images/ch9/sample_variance.gif)

- n-1로 나누고 있는 점에 주의
  - 표본 분산의 기댓값 `E(s^2) = sigma^2`로 만들기 위해서
  - 이는 모분산을 과대 혹은 과소가 아닌 편중되지 않게 추정하기 위함
- *자유도(degree of freedom)*
  - 자유롭게 움직일 수 있는 변수의 개수
  - `(X1 - X bar) + (X2 - X bar) + ... + (Xn - X bar) = 0`
    - 마지막 변수 Xn - X 는 자유롭게 움직일 수 없음
  - 위의 예시의 `n-1`
    - 1만큼 자유도가 줄어듬

#### 통계량의 의의

표본평균 표본 분산과 모평균 모분산의 관계 표현

![](./images/ch9/sample_and_population.gif)

- 통계량은 모집단과 표본을 잇는 중요한 양

## 통계량의 표본분포

### 표본분포의 역할

- 표본의 집계값으로서, 모집단의 다양한 양, 성질(모평균, 모분산)을 반영하여, 그것의 단서를 제공
  - 집계값 == 통계량
- 모집단과 표본을 연결해주는 것
  - 특히 표본합, 표본평균은 매우 중요

### 표본합의 표본분포

- 표본합, 표본평균의 구체적인 표본분포는 모집단분포에 의존함
- parametric의 경우
  - 분포가 재생성을 갖고 있으면 간단히 구할 수 있음
    - 재생성이란, 독립의 둘 이상의 확률변수가 동일 분포 종류에 속하는 경우, 그 합도 그것에 속하는 것
    - 이항분포, 포아슨분포, 정규분포 등
  - 이항모집단
    - `Xi ~ Bi(1, p)`
    - `X1 + X2 + ... + Xn ~ Bi(n, p)`
    - 예시
      - QC(Quality Control) 품질관리: 공장에 있어서, 제품이 불량할 확률이 p이며, n개의 제품에 포함되는 불량품의 수의 분포는 이항분포 `Bi(n, p)`이다. 그러나, 품질관리가 엄중하게 이뤄지는 공업제품의 모집단에서는 p가 매우 작으므로(1/1000 이하) 이 경우는 포아슨 모집이라고 생각해야만 함
      - 과일 농작물이 저품질일 경우와 그 확률
      - 사회조사법에서 어떤 내용에 대해 찬반
  - 포아슨모집단
    - 모집단분포가 모수 lambda의 포아슨분포 Po(lambda)이면, X1 + X2 + .. + Xn은 포아슨 분포 Po(nlambda)를 따름
    - 예시
      - 교통사고 사망자수: 일본 전국에서 하루에 교통사고로 죽는 사람을 평균 30명이라고 하는경우, 1년의 사망자 분포는 Po(10950)임. 하지만 `f(x) = e^(-30)*lambda^x/x!`에서 e^(-30)의 계산은 반드시 현실적이지 않고, e^(-10950)은 더더욱 그렇기 때문에, lambda가 1자리 수가 아니면, *중심극한정리* (잘 모르겠음). 그렇기 때문에, 일본전국을 현, 시 또는 경찰서관내 정도로 작게 범위를 한정해야 함. 또한 인구 10만명당... 등을 생각하는 이유도 같은 목적 때문임
  - 정규모집단
    - 모집단 분포가 mu, sigma^2의 정규분포 N(mu, sigma^2)라면 `X1 + X2 + ... + Xn ~ N(nmu, nsigma^2)`이며, `X bar ~ N(mu, sigma^2/n)`에 따름
    - 예시
      - 측정오차: 100cm의 봉의 길이를 측정하면, 1회당 측정은 측정오차 때문에 평균 100cm, 표준편차 0.1cm의 정규분포 N(100, 0.1^2)를 따른다고 하자. 이 측정을 100번 반복해서 그 평균을 생각하면, 그 분포는 평균 100cm 표준편차 0.01cm의 정규분포 N(100, 0.01^2)를 따름
      - 동일 규격의 것을 n개 제조 혹은 측정하는 경우에 정규분포가 잘 맞음
  - 점근적 정규성
    - 일반 표본분포를 구하기 위해서는 중적분(합성곱을 機重에도 행함)이 필요하며, 정확히 구하는 것이 힘들거나 불가능한경우도 많음
    - 그러나 중심 극한정리를 이용해서 근사적으로 그 분포를 구하는 것이 가능
      - n이 충분히 크다면(30이상), 모집단 분포에 관계없이, X bar의 분포는 기댓값 mu, 분산 sigma^2/n 의 정규분포 N(mu, sigma^2/n)이므로 표본 정규분포를 이용해서 모수에 근사 가능
    - 점근적
      - `n -> 무한대` 의 경우에 성립하는 것을 의미
      - 표본 평균 X bar의 점근 분포는 평균 mu 분산 sigma^2/n 의 정규분포 N(mu, sigma^2/n)임
    - 표본분포론은 거의가 정규모집단을 가정함
      - 피어슨, 고셋, 피셔 이후의 이론

## 유한모집단과 유한모집단수정

- 무한모집단 가정이 적합하지 않는 경우
  - N이 그다지 크지 않은 경우
  - n/N이 클 경우
- 위의 경우에는 N이 유한하다는 것을 고려하여 수정을 해줘야 함
- 유한모집단
  - `E(X bar) = mu`
  - `V(X bar) = (N-n / N-1) * (sigma^2 / n)`
    - `C(N) = (N - n) / (N - 1)`
    - N -> 무한대 면 소실됨