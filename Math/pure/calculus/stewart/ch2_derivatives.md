# 2. Derivatives

## 의문

## 2.1 Derivatives and Rates of Change

- `y = f(x)`의 점 `P(a, f(a))`에서의 접선의 기울기는 만일 존재한다면 아래와 같음
  - `m = lim_{x->a}{(f(x)-f(a))/(x-a)}`
  - `m = lim_{h->0}{(f(a+h)-f(a))/h}`
  - 과학이나 공학에서의 변화율(rate of change)를 계산할 때 사용됨
- 도함수(derivative)
  - 함수 f의 a에서의 도함수가 존재하는 경우 아래와 같음
    - `f'(a) = lim_{h->0}{(f(a+h)-f(a)) / h} = lim_{x->a}{(f(x)-f(a)) / (x-a)}`
  - `f'(a)`는 `y=f(x)`가 `x=a`에서의 순간변화율과 같음

## 2.2 The Derivative as a Function

- 도함수
  - `f'(x) = dy/dx(not ratio) = df/dx = lim_{h->0}{(f(x+h)-f(x)) / h}`
    - `(x, f(x))`에서의 접선의 기울기
    - 정의역
      - `{x | f'(x)가 존재}`
- `f'(a)`가 존재한다 => 함수 f가 a에서 미분가능하다
  - f가 열린구간 `(a, b)`에서 미분가능하다 => f가 해당 구간의 모든 값에서 미분가능하다
- 연속과 미분가능성의 관계
  - `f`가 a에서 미분가능 => f는 a에서 연속
    - 역의 반례
      - `f(x) = |x|`

미분 불가능한 케이스

![](./images/ch2/fail_to_be_differentiable1.png)

higher derivatives

![](./images/ch2/higher_derivative1.png)

- Higher Derivatives
  - 배경
    - f가 미분가능한 함수 => f'역시 함수
    - f'가 미분가능한 함수 => f''역시 함수
  - 개요
    - f''
      - second derivative of f
      - `y=f'(x)`의 점`(x,f'(x))`에서의 기울기
      - 변화율의 변화율
        - 예시
          - 가속도(속도의 변화율)
    - f'''
    - f'''' 역시 정의 가능

## 2.3 미분 공식

- `d(c)/dx = 0`
- `d(x^n)/dx = nx^(n-1) (n∈R)`
- New Derivatives from Old
  - `d(cf(x))/dx = c・df/dx (단, c는 상수이고, f는 미분가능)`
  - `d(f(x)+g(x))/dx = df/dx + dg/dx (단, f,g는 미분가능)`
  - `d(f(x)・g(x))/dx = f(x)g'(x) + f'(x)g(x) (단, f,g는 미분가능)`
  - `d(f(x)/g(x))/dx = (g(x)・df/dx - f(x)・dg/dx) / g(x)^2 (단, f,g는 미분가능)`
  - **어떠한 polynomial도 R에서 미분가능 ∧ 어떠한 유비함수도 해당 정의역에서 미분가능**
