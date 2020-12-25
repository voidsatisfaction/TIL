# 4. Integrals

- 4.1 Areas and Distances
- 4.2 The Definite Integral
- 4.3 The Fundamental Theorem of Calculus
- 4.4 Indefinite Integrals and the Net Change Theorem
- 4.5 The Substitution Rule

## 의문

## 4.1 Areas and Distances

Area of curve

![](./images/ch4/area1.png)

Area of curve generalized

![](./images/ch4/area2.png)

- area
  - `S = {(x,y) | a≤x≤b, 0≤y≤f(x)}`
- 연속함수 f의 region S의 area A는 다음과 같음
  - `A = lim(n->∞)R(n) = lim(n->∞)(f(x1)Δx + f(x2)Δx + ... + f(xn)Δx) = lim(n->∞)(f(x0)Δx + f(x1)Δx + ... + f(xn-1)Δx)`
    - A는 항상 존재 (∵f는 연속함수)
  - 특징
    - 사실, left endpoiint, right endpoint뿐 아니라, `∀xi* ∈ [xi-1, xi]`이어도 성립하고 이러한 `xi*`을 sample point라고 함
    - **A는 임의의 upper sum보다는 작고 임의의 lower sum보다는 큰 unique number**
- 거리 문제
  - 특정 시간동안 한 물체가 움직인 거리 구하기
- 다양한 예시
  - 일정시간 동안 변화하는 힘에 의한 작용된 일 구하기
  - cardiac output of the heart
  - area under a curve

## 4.2 The Definite Integral

리만 합과 Definite integral

![](./images/ch4/definite_integral1.png)

- 배경
  - `lim(n->∞)(sigma_(i=1)^(n)(f(xi*)Δx)) = lim(n->∞)(f(x1*)Δx + f(x2*)Δx + ... + f(xn*)Δx)`
    - 이 식은 다양한 곳에서 확인 가능(generalized)
    - 따라서 특별한 이름을 부여
- Definite Integral
  - `int_a^b(f(x))dx = lim(n->∞)sigma_(i=1)^(n)(f(xi*)Δx) <=> a에서 b까지의 definite integral`
    - `f는 [a,b]에서 정의되어 있고, Δx = (b-a)/n, xi*는 [xi-1, xi]사이에 존재하는 sample point`
  - 용어 정리
    - `int`
      - integral sign
    - `f(x)`
      - integrand
    - limits of integration
      - `a`
        - lower limit
      - `b`
        - upper limit
    - `dx`
      - 독립 변수가 x임을 나타냄
    - integration
      - integral을 계산하는 절차
    - `int_a^b(f(x))dx`
      - 전체가 하나의 심볼
      - 숫자
        - 이 심볼자체가 dx에 의존하지 않음
  - 특징
    - `int_a^b(f(x))dx = int_a^b(f(t))dt = int_a^b(f(r))dr = ...`
    - `int_a^b(f(x))dx`에서 일반적으로 같은 너비의 subinterval들로 나눴으나, unequal width로 하는것이 더 유리할 떄가 있음
      - 속도 데이터가 equally spaced되지 않은 경우
  - 리만 합
    - `sigma_(i=1)^n(f(xi*)Δx)`
    - f가 주어진 범위에서 양의 값을 갖을 경우, 리만 합은 직사각형으로 근사시킨 영역의 합을 의미
  - integrable
    - 모든 함수가 integrable인 것은 아니나 다음 theorem에 의하여 대부분의 함수가 integrable
- integrable theorem
  - `f가 [a,b]에서 연속 ∨ f가 오직 유한개의 discontinuities를 갖음 => (f는 [a,b]에서 integrable <=> int_a^b(f(x)dt)가 존재)`
    - 증명은 해석학에서

## 4.3 The Fundamental Theorem of Calculus

## 4.4 Indefinite Integrals and the Net Change Theorem

## 4.5 The Substitution Rule
