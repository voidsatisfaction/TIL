# Neural Networks: Learning

- 의문
- Cost Function and Backpropagation
- Backpropagation in Practice
- Application of Neural Networks

## 의문

## Cost Function and Backpropagation

### Cost function

Neural Networks Cost Function(Generalization of logistic regression)

![](./images/week5/neural_networks_cost_function1.png)

### Backpropagation Algorithm

Back propagation algorithm

![](./images/week5/back_propagation1.png)

- error of node j in layer l
  - `δ_j^l`
  - `δ^3 = t(θ^3)δ^4 .* g'(z^3)`
    - 이전 layer의 output을 input으로 대응하는 레이어3의 미분값
  - 참고
    - **에러를 구할 때에는, `dg(WX)/dX`, 즉 이전 layer의 output vector로 미분. 그리고 그 값에다가 현재 레이어의 다음 레이어들의 error를 곱하면 됨**
      - backpropagation을 하기 위해서
      - 이게 맞는 것인지?
    - **특정 weight에 대한 미분값을 구할 때에는, `dg(WX)/dW`를 구하고 현재 레이어의 다음 레이어들의 error를 곱하면 됨**
      - 이게 맞는것인지?

### Backpropagation Intuition

Forward propagation

![](./images/week5/forward_propagation1.png)

Back propagation intuition1

![](./images/week5/back_propagation2.png)

- *위 그림에서, 왜, `δ_2^2 = θ_{12}^2 δ_1^3 + θ_{22}^2 δ_2^3`와 같이 activation함수는 고려되지 않은 것인가? 시그모이드 함수를 적용하면, chain rule을 적용할 때, 이처럼 되지 않을것같은데..*
  - activation함수로 ReLU를 적용한것인가? ...
    - 아니고, 식이 잘못된 것임

## Backpropagation in Practice

## Application of Neural Networks
