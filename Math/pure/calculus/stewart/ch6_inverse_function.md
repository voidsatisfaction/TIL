# 6. Inverse Function

- 의문
- 6.1 Inverse Functions
- 6.2 Exponential Functions and Their Derivatives
- 6.3 Logarithmic Functions
- 6.4 Derivatives of Logarithmic Functions
- 6.5 Exponential Growth and Decay
- 6.6 Inverse Trigonometric Functions
- 6.7 Hyperbolic Functions
- 6.8 Indeterminate Forms and l'Hospital's Rule

## 의문

## 6.1 Inverse Functions

- inverse continuous theorem
  - `f가 단사함수 ∧ 특정 구간 I에서 연속 => f^-1도 I에서 연속`
    - *f가 invertible이 아니어도, 특정 구간에서 연속이기 때문에 그 구간안에서는 자동적으로 invertible이 되는가?*
- inverse differntial theorem
  - `f가 전단사함수 ∧ 미분가능 ∧ f'(f^-1(x)) ≠ 0 => (f^-1)'(x) = 1/f'(f^-1(x))`

## 6.2 Exponential Functions and Their Derivatives

Exponential functions

![](./images/ch6/exponential_function1.png)

- exponential function
  - `f: R -> R, f(x) = b^x (b>0)`
    - x=양의 정수
      - `b^n = b x b x ... x b`
    - x=0
      - `b^0 = 1`
    - x=음의 정수
      - `b^-n = 1/b^n`
    - x=유비수(`p/q`)
      - `b = b^(p/q) = qroot(b^p) = (qroot(b))^p`
    - x=무리수
      - 2^1.7 < 2^root(3) < 2^1.8
  - 특징
    - `b^x = lim_{r->x}(b^r) (r은 유비수)`
      - *`b^x`를 unique하게 specify하고, `f(x) = b^x`는 연속임을 보여줌*
        - *증명?*
  - 종류
    - `b>1`
    - `b=1`
    - `0<b<1`
- exponential function theorem
  - `b>1 => f:R -> (0,∞), f(x)=b^x는 연속 ∧ ∀x∈R, b^x>0 ∧ 증가함수`
  - `0<b<1 => f:R -> (0,∞), f(x)=b^x는 연속 ∧ ∀x∈R, b^x>0 ∧ 감소함수`
  - `a,b>0 ∧ x,y∈R`
    - `b^(x+y)=b^x・b^y`
    - `b^(x-y)=b^x/b^y`
    - `(b^x)^y=b^xy`
    - `(ab)^x=a^x・b^x`
  - `b>1 => lim_{x->∞}(b^x)=∞ ∧ lim_{x->-∞}(b^x)=0`
  - `0<b<1 => lim_{x->∞}(b^x)=0 ∧ lim_{x->-∞}(b^x)=∞`
- e
  - 정의
    - `e is s.t lim_{h->0}((e^h-1)/h) = 1`
  - 특성
    - `d/dx(e^x) = e^x`
    - `d/dx(e^u) = e^u・du/dx`
    - domain R
    - increasing
    - continuous
    - range (0, ∞)
    - `∀x∈R, e^x>0`
    - `lim_{x->-∞}(e^x)=0, lim_{x->∞}(e^x)=∞`
    - `int(e^x)dx = e^x + C`

## 6.3 Logarithmic Functions

- log의 의미
  - `log_{b}(x) = 밑이 b일때 이 로그를 지수로 하면, 그 값은 x이다`
- logarithmic function
  - `f: (0,∞) -> R, f(x) = log_{b}(x)`
- logarithmic function theorem
  - `b>1 => f: (0,∞) -> R, f(x) = log_{b}(x), f는 일대일 대응 ∧ 연속 ∧ 증가 함수`
  - `x,y>0 ∧ r∈R`
    - `log_{b}(xy) = log_{b}(x) + log_{b}(y)`
    - `log_{b}(x/y) = log_{b}(x) - log_{b}(y)`
    - `log_{b}(x^r) = rlog_{b}(x)`
  - `b>1 => lim_{x->∞}(log_{b}(x))=∞ ∧ lim_{x->0+}(log_{b}(x))=-∞`

## 6.4 Derivatives of Logarithmic Functions
## 6.5 Exponential Growth and Decay
## 6.6 Inverse Trigonometric Functions
## 6.7 Hyperbolic Functions
## 6.8 Indeterminate Forms and l'Hospital's Rule
