# Neural Networks: Learning

- 의문
- Cost Function and Backpropagation
- Backpropagation in Practice
- Application of Neural Networks

## 의문

## Cost Function and Backpropagation

- L
  - NN의 레이어 수
- s(l)
  - layer l에서의 unit의 개수(bias unit은 제외)

### Cost function

Neural Networks Cost Function(Generalization of logistic regression)

![](./images/week5/neural_networks_cost_function1.png)

### Backpropagation Algorithm

Gradient computation

![](./images/week5/gradient_computation1.png)

**Back propagation algorithm**

![](./images/week5/back_propagation1.png)

- 위 알고리즘 부가 설명
  - `Δ^l = dJ/dW^l = dz^(l+1)/dW^l・dJ/dz^(l+1) = δ^(l+1)・ta^l`
  - `J(θ)`는 전체 데이터 X에 대해서 minimum값을 찾는것을 목표로 해야함. 따라서, back propagation에서도 모든 데이터에 관해서 gradient descent를 진행해야하는데, J의 `sigma_{i=1}^{m}`의 부분의 내부의 함수들이 전부 미분가능이므로 각 트레이닝 데이터하나마다 미분한 값을 각각 더할 수 있음
    - 그것이 위 루프의 이유(`For i=1 to m ...`)
    - 결국 back propagation은 각 트레이닝 데이터셋 하나하나마다 시행해서 더해줌
      - **vectorization이 가능**
- error of node j in layer l
  - `δ_j^l`
  - `δ^3 = t(θ^3)δ^4 .* g'(z^3)`
    - 이전 layer의 output을 input으로 대응하는 레이어3의 미분값
  - `δ^L = a^L - y`
    - *이건 왜 그런가?*
  - 참고
    - **에러를 구할 때에는, `dg(W^(l)Z^(l))/dZ^(l)`, 즉 이전 layer의 output vector・weights로 미분. 그리고 그 값에다가 현재 레이어의 다음 레이어의 error를 곱하면 됨**
      - backpropagation을 하기 위해서
    - **특정 weight에 대한 미분값을 구할 때에는, `dg(WA)/dW`를 구하고 현재 레이어의 다음 레이어들의 error를 곱하면 됨**

### Backpropagation Intuition

Forward propagation

![](./images/week5/forward_propagation1.png)

Back propagation intuition1

![](./images/week5/back_propagation2.png)

- *위 그림에서, 왜, `δ_2^2 = θ_{12}^2 δ_1^3 + θ_{22}^2 δ_2^3`와 같이 activation함수는 고려되지 않은 것인가? 시그모이드 함수를 적용하면, chain rule을 적용할 때, 이처럼 되지 않을것같은데..*
  - activation함수로 ReLU를 적용한것인가? ...
    - 아니고, 식이 잘못된 것임

## Backpropagation in Practice

### Unrolliing Parameters(octave implementation)

Octave에서의 Unrolling parameters의 예시

![](./images/week5/unrolling_parameters2.png)

Octave에서의 Learning algorithm의 구성

![](./images/week5/unrolling_parameters1.png)

- unroll
  - 개요
    - Octave의 `fminunc`를 사용하기 위해서, matrix를 vector로 변환
  - 대상
    - `θ`(weights), `D`(gradients)

### Gradient Checking

Numerical estimation of gradients(intuition)

![](./images/week5/numerical_estimation_of_gradients1.png)

Numerical estimation of gradients(on weights)

![](./images/week5/numerical_estimation_of_gradients2.png)

Octave implementation

```octave
for i = 1:n,
  thetaPlus = theta;
  thetaPlus(i) = thetaPlus(i) + EPSILON;
  thetaMinus = theta;
  thetaMinus(i) = thetaMinus(i) - EPSILON;
  gradApprox(i) = (J(thetaPlus)-J(ThetaMinus))/(2*EPSILON);
end;

/* and check gradApprox ~~ Dvec(from backpropagation) */
```

- 참고
  - Backpropagation이 numerical estimation보다 훨씬 빠르므로, 무조건 Backpropagation으로 학습시켜야 함

### Random Initialization

- 개요
  - 모든 웨이트를 0으로 두면 학습이 잘 되지 않는 문제가 생김
    - *같은 레이어에 있는 웨이트들이 다 같은 값을 갖게 됨*
- 해결 방법
  - `theta`를 `[-ε, ε]`사이의 임의의 값으로 설정
  - octave
    - `Theta1 = rand(10, 11) * (2*INIT_EPSILON) - INIT_EPSILON`

### Putting It Together

- Training a neural network
  - ① Pick a network architecture
    - Input units의 개수
    - Output units의 개수
    - Hidden layer의 각 레이어 별 unit개수(유닛 개수는 같게)
  - ② Training a Neural Network
    - Randomly initialize the weights
    - *Implement forward propagation to get `h_θ(x(i)) for any x(i)`*
      - forward propagation이 정확히 무엇을 하는 것인지?
    - Implement the cost function
    - Implement backpropagation
    - Use gradient checking
      - then disable that
    - Use gradient descent or built-in optimization function
- 참고
  - 언제나 cost function을 global minimum으로 최적화 할 수는 없으나, 성능이 꽤 좋다

## Application of Neural Networks
