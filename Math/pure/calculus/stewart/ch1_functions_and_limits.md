# 1. Functions and Limits

- 의문
- 용어
- 1.1 Four Ways to Represent a Function

## 의문

- *자유도랑 기저의 관계?*

## 용어

- parabola
  - 포물선
- piecewise defined functions
  - 다수의 sub functions으로 구성되어 있으며, 각 sub function들은 main function의 특정 정의역(sub domain)구간에 정의가 되어있다

## 1.1 Four Ways to Represent a Function

- four ways
  - 종류
    - an equation(algebrically)
    - a graph(visually)
    - a table(numerically)
    - in words(verbally)
  - 특징
    - 각각의 form에 대해서 장단점이 존재하고, 현상을 분석할 때 네가지의 방식 모두를 사용할 수 있음
- function
  - definition
    - each element x in a set D(domain) exactly one element, called f(x) in a set E
  - **4ways to picture a function**
    - an equation(algebrically)
      - 꼭 식이 주어져야만 calculus를 할 수 있는 것은 아님
    - a graph(visually)
      - 단순히 값들만 주어져있을 때에는, approximation을 이용한 그래프를 그려줄 수 있음
    - a table(numerically)
    - in words(verbally)
- function의 특징에 따른 분류
  - piecewise defined functions
    - 정의
      - 다수의 sub functions으로 구성되어 있으며, 각 sub function들은 main function의 특정 정의역(sub domain)구간에 정의가 되어있다
    - 예시
      - `f(x) = `
        - `1 - x if x ≦ -1`
        - `x^2 if x > -1`
      - absolute value function
        - `f(x) = |x|`
      - step functions
  - Symmetry
    - **even function(우함수/짝함수)**
      - 정의
        - `f(-x) = f(x)`
        - 덧셈 역원의 상이 서로 같은 함수
    - **odd function(기함수/홀함수)**
      - 정의
        - `f(-x) = -f(x)`
  - Increasing and Decreasing Functions
    - 구간 I에서 increasing function(`I = [a,b]`)
      - `f가 [a,b]에서 증가 <=> ∀x1,x2∈[a,b] s.t. x1 < x2, f(x1) < f(x2)`
    - 구간 I에서 decreasing function(`I = [a,b]`)
      - `f가 [a,b]에서 감소 <=> ∀x1,x2∈[a,b] s.t. x1 < x2, f(x2) < f(x1)`

## 1.2 Mathematical Models: A Catalog of Essential Functions

![](./images/ch1/mathematical_model1.png)

- Mathematical model
  - 정의
    - 현실 세계의 현상에 대한 수학적 기술(함수나 식을 통한)
      - 인구, 제품의 수요, 낙하하는 물체의 속도, 사람의 기대수명
  - 목적
    - 현상 이해
    - 미래 예측 등
  - 과정
    - ① 실제 세상의 문제 파악
      - 다양한 경로를 통해서 정보 획득
      - 데이터를 바탕으로 그래프를 그려서 알맞은 대수 공식을 파악하기도 함
    - ② 수학적 모델 생성
      - independent, dependent variables를 파악
      - apply the mathematics that we know (such as the calculus that will be developed throughout this book) to the mathematical model that we have formulated in order to derive mathematical conclusions
    - ③ 수학적 결론
      - 얻은 수학적 결론을 해석하여, 실제 세상의 문제에 대한 데이터를 정보화 시킴
    - ④ 실제 세상의 예측(문제해결)
      - 실제 대이터를 체크 하면서 수학적 결론(예측)을 테스트 함
      - 데이터와 기존의 결론이 잘 맞지 않으면, 모델을 더 개량하거나 새로운 모델을 만들기 위해서 위의 사이클을 반복함
  - 특징
    - 수학적 모델은 실제 세상 완벽히 같지 않음
      - **idealization**의 성질을 갖음
      - 애초에 수학적 모델은 한계를 가짐
    - 좋은 수학적 모델
      - **현실 세상의 문제를 수학적 계산이 가능하도록 단순화 하면서도, 충분히 가치있는 결론을 가져야 함**
    - 현실 세계에서 관찰된 수학적 모델을 기술하기 위한 다양한 타입의 함수들이 존재함
    - 주어진 현상에 수학적 모델을 구성하기 위한 물리적인 법칙이나, 원리가 존재하지 않으면, **empirical model** 즉, 수집된 데이터를 바탕으로 수학적 모델을 구성하는 수 밖에 없다
      - 수집한 데이터에 잘 적합된 curve를 찾으려고 노력해야 함(captures basic trend of the data points)

### 1.2.1 Linear Models

선형 모델의 예시1

![](./images/ch1/linear_model_example1.png)

선형 모델의 예시2 & 최소제곱법

![](./images/ch1/linear_model_example2.png)

- 정의
  - `y = f(x) = mx + b` 형태
- 특징
  - 일정한 비율로 grow함

### 1.2.2 Polynomials

다항 모델의 예시1

![](./images/ch1/polynomial_model_example1.png)

- 정의
  - `P(x) = anx^n + an-1x^n-1 + ... + a2x^2 + a1x + a0 (n > 0인 정수)`
    - `a0, ..., an`은 계수(coefficient)
    - 정의역
      - `R = (-∞, ∞)`
    - degree of polynomial(위의 경우)
      - n
- 특징
  - polynomial of degree
    - 1인 경우: linear function
    - 2인 경우: quadratic function
      - `P(x) = ax^2 + bx + c`는 포물선 `y = ax^2`를 이동시키면서 얻을 수 있음
    - 3인 경우: cubic function
      - `P(x) = ax^3 + bx^2 + cx + d (a≠0)`
  - 자연과 사회 과학에서 일어나는 다양한 양들을 모델링할 때 널리 사용됨
    - 예시
      - 상품의 개수x에 대한 비용을 나타내기 위해서 `P(x)`를 사용
  - 최소제곱법으로 다항식의 곡선의 방정식을 구할 수 있음

### 1.2.3 Power Functions

case1 `a = n (n > 0인 정수)`

![](./images/ch1/power_function1.png)

case2 `a = 1/n (n은 양인 정수)`

![](./images/ch1/power_function2.png)

case3 `a = -1`

![](./images/ch1/power_function3.png)

- 정의
  - `f(x) = x^a (a는 정수)`
    - case1 `a = n (n > 0인 정수)`
    - case2 `a = 1/n (n은 양인 정수)`
    - case3 `a = -1`

### 1.2.4 Rational Functions

![](./images/ch1/rational_function1.png)

- 정의
  - ratio of polynomials:
    - `f(x) = P(x) / Q(x) (P, Q는 다항함수)`
    - domain
      - `{x∈R | Q(x)≠0}`
- 예시
  - `f(x) = 1/x`
  - `f(x) = (2x^4-x^2+1)/(x^2-4) (x ≠ +-2)`

### 1.2.5 Algebraic Functions

![](./images/ch1/algebraic_function1.png)

- 정의
  - 다항함수와 algebraic operations(덧셈, 뺄셈, 곱셈, 나눗셈, 제곱근 구하기)으로 구성되는 함수
  - 임의의 유리함수(rational function)은 자동적으로 algebraic function이다
- 예시
  - `f(x) = root(x^2+1), g(x) = (x^4-16x^2)/(x+root(x)) + (x-2)(x+1)^(1/3)`

### 1.2.6 Trigonometric Functions(삼각함수)

![](./images/ch1/trigonometric_function1.png)

- 참고
  - 각의 단위로서 라디안을 사용
- 정의
  - `f(x) = sin(x), f(x) = cos(x), f(x) = tan(x) = sin(x)/cos(x)`
    - 정의역
      - `(-∞,∞)`
    - 치역
      - `[-1,1]`
  - `tan(x+π) = tan(x) (x≠±π/2 + nπ (n∈Z))`
  - `cosecant, secant, cotangent`도 존재
- 특징
  - `sin(x+2π) = sin(x), cos(x+2π) = cos(x)`
    - 함수의 주기성으로 인하여, 반복적인 현상(물결, 음파) 등을 모델링하기에 적합
- *`f(x) = tan(x)`는 trigonometric function으로 취급하지 않는 것인가?*
  - 하긴 그냥 비율일 뿐이므로..

### 1.2.7 Exponential Functions

![](./images/ch1/exponential_function1.png)

- 정의
  - `f(x) = b^x (b>0)`
- 예시
  - `f(x) = 2^x, f(x) = 0.5^x`
    - 정의역
      - `(-∞, ∞)`
    - 치역
      - `(0, ∞)`
- 특징
  - 자연현상을 기술하는데에 유용
    - e.g) 인구 증가, 방사선동위원소 반감

### 1.2.8 Logarithmic Functions

![](./images/ch1/logarithmic_function1.png)

- 정의
  - `f(x) = log_b^x (b>0)`
    - exponential function의 역함수
