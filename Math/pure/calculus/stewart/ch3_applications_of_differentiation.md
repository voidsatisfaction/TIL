# 3. Applications of Differentiation

- 의문
- 3.1 Maximum and Minimum Values
- 3.2 The Mean Value Theorem
- 3.3 How Derivatives Affect the Shape of a Graph
- 3.4 Limits at Infinity; Horizontal Asymptotes
- 3.5 Summary of Curve Sketching
- 3.6 Graphing with Calculus and Calculators
- 3.7 Optimization Problems
- 3.8 Newton's Method
- 3.9 Antiderivatives

## 의문

## 3.1 Maximum and Minimum Values

- 개요
  - 최적화 문제의 해결
    - 예시
      - 제조 비용의 최대 / 최솟값
      - 우주선의 최대 가속도
      - ...
- absolute(global) maximum(minimum) value
  - 정의
    - `c∈D, D is domain of f`
      - `∀x∈D, f(c)≥f(x)` <=> f(c)는 f의 D에서의 **absolute maximum value**
      - `∀x∈D, f(c)≤f(x)` <=> f(c)는 f의 D에서의 **absolute minimum value**
    - extreme values
      - absolute maximum value
      - absolute minimum value
- local maximum(minimum) value
  - 정의
    - `f(c)≥f(x) (x≈c)` <=> f의 local maximum
    - `f(c)≤f(x) (x≈c)` <=> f의 local minimum
- **Extreme Value Theorem**
  - `f`가 닫힌 구간`[a,b]`에서 연속 => f는 구간 `[a,b]`에서 absolute maximum value를 `f(c)`로 갖음 ∧ 구간 `[a,b]`에서 absolute minimum value를 `f(d)`로 갖음 (단, `c,d ∈ [a,b]`)
- **Fermat's Theorem**
  - `c∈D (D는 함수f의 domain), f(c) is local minimum or maximum ∧ ∃f'(c) => f'(c) = 0 (c is critical number of f)`
    - 역이 성립하지 않음에 주의!!
- critical number
  - critical number of function f
    - `c∈D, s.t f'(c)=0 or f'(c) does not exist`
- The Closed Interval Method
  - **by Extreme Value Theorem and Fermat's Theorem**
  - absolute maximum, minimum값을 닫힌구간 `[a, b]`위의 연속함수f에서 찾는 방법
    - `f(a)`, `f(b)`의 값을 구함
    - `(a, b)`구간에서 f의 극값을 구함
    - 위의 모든 값들중에서 가장 큰 값과 작은 값이 구간 `[a,b]`에서의 최대, 최솟값

## 3.2 The Mean Value Theorem

- Rolle's Theorem
  - f가 다음을 만족 => `∃c∈(a,b), f'(c)=0`
    - f가 닫힌 구간 `[a,b]`에서 연속
    - f가 열린 구간 `(a,b)`에서 미분가능
    - `f(a)=f(b)`
- Mean Value Theorm
  - `f가 닫힌구간 [a,b]에서 연속 ∧ f가 열린구간 (a,b)에서 미분가능` => `∃c∈(a,b), f'(c) = (f(b)-f(a))/(b-a)`
  - 해석
    - 한 기간동안의 평균 변화율이 그 사이의 순간 변화율과 같게되는 경우는 반드시 존재한다.
  - 따름정리1
    - `∀x∈(a,b), f'(x)=0 => f is constant on (a,b)`
  - 따름정리2
    - `∀x∈(a,b), f'(x)=g'(x) => f-g is constant on (a,b) <=> f(x)=g(x)+c`

## 3.3 How Derivatives Affect the Shape of a Graph

## 3.4 Limits at Infinity; Horizontal Asymptotes

## 3.5 Summary of Curve Sketching

## 3.6 Graphing with Calculus and Calculators

## 3.7 Optimization Problems

## 3.8 Newton's Method

## 3.9 Antiderivatives
