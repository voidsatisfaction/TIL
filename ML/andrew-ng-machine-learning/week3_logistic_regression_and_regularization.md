# Logistic Regression & Regularization

- 의문
- Logistic Regression
  - Classification and Representation
  - Logistic Regression Model
  - Multiclass Classification
- Regularization
  - Solving the Problem of Overfitting

## 의문

- *logistics regression에서 어차피 우리가 하고 싶은 것은 discrete하게 classify하는 것인데, cost function을 최소화 시키는게 의미가 있는가?*
  - 분류만 잘하면 되는거 아닌가?

## Logistic Regression

Hypothesis function of classification problems

`h_θ: X -> {0, 1, 2, ...}`

- logistic regression
  - 개요
    - **classification 알고리즘**

### Classification and Representation

#### Hypothesis function on logistics regression

![](./images/week3/hypothesis_function_on_logistics_regression1.png)

- logistics regression hypothesis function
  - 개요
    - `h_θ = g(tθ・x) (단, g(z) = 1/(1+e^(-z)))`
    - 값의 결과는 probability
- logistic(sigmoid) function
  - 개요
    - `g: R -> (0,1), g(x) = 1/(1+e^(-x))`

#### Dicision boundary

Decision boundary 유도하기 위한 과정

![](./images/week3/decision_boundary1.png)

Linear Decision boundary

![](./images/week3/decision_boundary2.png)

Non-linear decision boundaries

![](./images/week3/decision_boundary3.png)

- 개요
  - sigmoid function에서 x가 0보다 크거나 같을 경우에, 0.5 이상이 되므로, 결국, `tθ・x ≥ 0`인 경우에 1이 되는데, `tθ・x = 0`을 만족하는 `x1, ..., xn`에 대한 함수를 dicision boundary라고 함
    - The decision boundary is the line that separates the area where y = 0 and where y = 1. It is created by our hypothesis function.
  - classification을 결정하는 값의 경계를 나타내는 함수

### Logistic Regression Model

#### Cost Function

Convex function

![](./images/week3/cost_function1.png)

Cost function1

![](./images/week3/cost_function2.png)

Cost function2

![](./images/week3/cost_function3.png)

- convex
  - cost function이 convex function이어야지, global optima를 찾을 수 있음
    - *그런데, multivariate linear regression같은 경우도 convex아니지 않은가?*
  - 따라서, logistic regression에서의 hypothesis function을 convex하게 만들 필요가 존재
- 개요
  - `cost(h_θ(x), y)`
    - `= -log(h_θ(x)) if y=1`
    - `= -log(1-h_θ(x)) if y=0`
    - cost함수의 값은 오차의 정도를 나타냄

#### Simplified Cost Function and Gradient Descent

Logistic regression cost function

![](./images/week3/gradient_descent1.png)

Gradient descent of logistics regression

![](./images/week3/gradient_descent2.png)

- simplified cost function
  - `J(θ) = 1/m sigma_{i=1}^{m}(Cost(h_θ(x), y))`
    - `Cost(h_θ(x), y) = -ylog(h_θ(x)) - (1-y)log(1-h_θ(x))`
      - *maximum likelyhood estimation(statistics)*

### Multiclass Classification

## Regularization

### Solving the Problem of Overfitting
