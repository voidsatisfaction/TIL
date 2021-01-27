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
    - **에러를 구할 때에는, `dg(WX)/dX` 이전 layer의 output vector로 미분**
      - backpropagation을 하기 위해서
    - **특정 weight에 대한 미분값을 구할 때에는, `dg(WX)/dW`를 구하면 됨**

## Backpropagation in Practice

## Application of Neural Networks
