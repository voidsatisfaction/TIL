# 7. Techniques of Integration

- 의문
- 7.1 Integration by Parts
- 7.2 Trigonometric Integrals
- 7.3 Trigonometric Substitution
- 7.4 Integraion of Rational Functions by Partial Fractions
- 7.5 Strategy for Integration
- 7.6 Integration Using Tables and Computer Algebra Systems
- 7.7 Approximate Integration
- 7.8 Improper Integrals

## 의문

## 7.1 Integration by Parts

- 개요
  - differentiation rule <-> integration rule
    - chain rule <-> substitution rule
    - product rule <-> integration by parts
- integration by parts
  - `f,g는 미분가능일때`
    - `sigma(f(x)g'(x))dx = f(x)g(x) - sigma(g(x)f'(x))dx`
    - `= sigma(u)dv = uv - sigma(v)du (u=f(x), v=g(x))`
  - `f,g가 미분가능 ∧ f', g'가 연속`
    - `sigma_{a}^{b}(f(x)g'(x))dx = [f(x)g(x)]_a^b - sigma_{a}^{b}(g(x)f'(x))dx`
- reduction formula
  - `sigma(sin^n(x))dx = -1/n・cos(x)・sin^(n-1)(x) + (n-1)/n・sigma(sin^(n-2)(x))dx`

## 7.2 Trigonometric Integrals

### `sigma(sin^m(x)cos^n(x))dx`

- `sin, cos`함수가 한쪽은 홀수, 한쪽은 짝수번 거듭제곱된 상태로 곱해진 경우
  - 해결
    - 한쪽을 거듭제곱을 한번만 행한것으로 남김
  - e.g
    - `sigma(cos^3(x))dx`
- `sin, cos`함수가 둘다 짝수번 거듭제곱된 상태로 곱해진 경우
  - 해결
    - 반각공식등을 사용
      - `sin^2(x) = (1/2)(1-cos(2x))`
      - `cos^2(x) = (1/2)(1+cos(2x))`
      - `sin(x)cos(x) = (1/2)(sin(2x))`
  - e.g
    - `sigma_{0}^{π}(sin^2(x))dx`

### `sigma(tan^m(x)sec^n(x))dx`



## 7.3 Trigonometric Substitution

## 7.4 Integraion of Rational Functions by Partial Fractions

## 7.5 Strategy for Integration

## 7.6 Integration Using Tables and Computer Algebra Systems

## 7.7 Approximate Integration

## 7.8 Improper Integrals
