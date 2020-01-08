# Deep learning from scratch

- 의문
- 큰 그림
- 1 퍼셉트론
- 2 신경망
- 3 신경망 학습

## 의문

## 큰 그림

![](./images/big_picture1.jpeg)

## 1. 퍼셉트론

### 1.1 퍼셉트론이란?

여기에서는 인공 뉴런, 단순 퍼셉트론으로 불리는 것

- 정의
  - 다수의 신호(흐름)를 입력으로 받아 하나의 신호를 출력
- 매개변수
  - 가중치
  - 편향
- 동작
  - 다른 뉴런(노드)으로부터의 입력 신호에 각각 고유한 가중치를 곱하고 그 합이 정해진 한계를 넘을 때만 1을 출력
  - 가중치가 클 수록 그 신호가 더 중요함을 의미
    - 가중치는 전류의 저항의 역작용을 함
  - 예시
    - y
      - 0 `(w1x1 + w2x2 <= θ)`
      - 1 `(w1x1 + w2x2 > θ)`

### 1.2 단순한 논리 회로

- 퍼셉트론을 이용한 논리 회로 구축
  - AND
  - NAND
- 퍼셉트론의 매개변수 값(가중치, 임계값)을 정하는 주체
  - 인간
    - NAND 게이트 등
  - 컴퓨터
    - 매개변수의 값을 컴퓨터가 자동으로 정하게 하는 작업을 **학습** 이라 함
    - 사람은 퍼셉트론의 구조(모델)를 고민하고, 컴퓨터에 학습할 데이터를 주는 일을 함
- **퍼셉트론으로 논리 회로를 구현할 수 있는데, 구조 자체는 똑같으나, 세 가지 게이트에서 다른 것은 매개변수(가중치와 임계값) 뿐**

### 2.3 퍼셉트론 구현하기

- AND
  - `w1x1 + w2x2 + b > 0 => 1`
  - `w1x1 + w2x2 + b <= 0 => 0`
  - `(w1, w2 = 0.5, b = -0.7)`
- NAND
  - `w1x1 + w2x2 + b > 0 => 1`
  - `w1x1 + w2x2 + b <= 0 => 0`
  - `(w1, w2 = -0.5, b = 0.7)`
- OR
  - `w1x1 + w2x2 + b > 0 => 1`
  - `w1x1 + w2x2 + b <= 0 => 0`
  - `(w1, w2 = 0.5, b = -0.3)`
- XOR
  - 단층 퍼셉트론으로 구현 불가
  - 2층 퍼셉트론으로 구현 가능

단층 퍼셉트론은 직선형 영역만 표현할 수 있고, 다층 퍼셉트론은 비선형 영역도 표현할 수 있다.
2층 퍼셉트론이면 컴퓨터를 만들 수 있다.

- 활성화 함수
  - 정의
    - 입력신호의 총합을 출력 신호로 변화시켜주는 함수
      - `y = h(b+w1x1+w2x2)`
      - `h(x) = { 0 (x≦0), 1 (x>0)}`
  - 종류
    - 계단 함수
      - `h(x) = { 1 (x>0), 0 (x<=0)}`
    - 시그모이드 함수
      - `h(x) = 1/(1+e^-x)`
        - 연속함수
        - 단조증가함수
          - 입력이 중요하면 큰 값 출력, 중요하지 않으면 작은 값 출력
    - ReLU 함수
      - `h(x) = { x (x>0), 0 (x<=0) }`
      - 최근에 많이 사용됨
        - *왜 최근에 많이 사용되지?*
- 퍼셉트론과 신경망의 주된 차이
  - 활성화 함수 뿐
  - 신경망의 활성화 함수는 비선형 함수여야 함(시그모이드 함수 or ReLU 함수)
    - *왜죠?*
    - 선형 함수는 가감승제, 합성해도 계속 선형함수
- 신경망 모델 계산

![](./images/neural_net_calculation.jpeg)

- 출력층 설계하기
  - 어떤 딥러닝 문제냐에 따라서 출력층에서 사용하는 활성화 함수가 달라짐
    - 회귀(입력데이터에서 연속적인 수치 예측)
      - I(항등함수)
    - 분류(데이터가 어느 클래스에 속하는가)
      - softmax
        - *이 함수는 무슨 배경으로 등장했고, 어떤 특징을 갖는가? - 수학적으로*
- softmax 함수 특징
  - ① `sigma_{k=1}^{n}(y_k) = 1`
  - ② `y_k`는 단조증가 함수
  - ③ 클래스 인식을 확률적으로 가능하게 함(값 0 ~ 1)
- 용어 설명
  - 정규화
    - 데이터를 특정 범위로 변환하는 것
  - 전처리
    - 신경망의 입력데이터에 pre-processing 특정변환을 가하는것
  - 백색화(whitening)
    - 전체 데이터를 균일하게 분포시킴
  - 배치(batch)
    - 하나로 묶은 입력 데이터
    - 느린 I/O 비율을 줄임
      - 데이터 전체에서 표본을 추출한 것

## 2. 신경망

- 학습
  - 정의
    - 훈련 데이터로부터 가중치・매개변수의 최적값을 자동으로 획득하는 것
- 학습지표
  - 정의
    - 손실 함수의 값
- 우리의 목표
  - **손실 함수의 결과값을 가장 작게 만드는 가중치 매개 변수 찾기**
    - 경사법
- 데이터 주도 학습
  - 데이터가 핵심
  - 데이터에서 패턴 추출(기계 학습)
    - 사람의 개입 배제
- 참고) 문제 해결 방법
  - ① 사람의 알고리즘
  - ② 사람이 문제에서의 feature를 추출 후 기계학습 구동
  - ③ 사람은 데이터만 제공하고 기계가 알아서 최적화
    - end-to-end machine learning
    - 그렇기 떄문에, 모든 문제를 같은 맥락에서 풀 수 있고, 주어진 데이터를 온전히 학습하고, 주어진 문제 패턴을 발견하려 시도

### 손실 함수

- 손실 함수
  - 정의
    - 신경망 성능의 "나쁨"을 나타내는 지표(현재의 신경망이 훈련 데이터를 얼마나 잘 처리하지 못하는가)
      - 만일, 정확도를 지표로 삼으면 (e.g) 100개중 33개가 맞아서 33%의 정확도), 미분값이 대부분의 장소에서 0이 되어 매개변수 갱신이 안됨
  - 종류
    - 평균제곱오차(MSE - Mean Squared Error)
      - `E = 1/2・sigma_{k}(y_k - t_k)^2`
        - `y_k`는 k번쨰 뉴런의 신경망의 출력값
        - `t_k`는 k번쨰 뉴런의 정답 레이블
          - e.g) `y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]`
          - `t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0] (원 핫 인코딩)`
    - 교차 엔트로피 오차(CEE - Cross Entropy Error)
      - `E = -sigma_{k}(t_k・log(y_k))`
        - *왜 하필 이 함수를 쓰는가? - 애초에 어떤 배경으로 나타난 함수인가? 정보엔트로피와의 관계는 무엇인가?*
- 신경망의 학습
  - 정의
    - 손실함수 값을 최대한 줄여주는 매개변수를 탐색
  - 방법
    - 매개변수의 손실함수에 대한 미분값을 계산(그래서 활성화함수를 연속함수인 시그모이드 사용)
      - 가중치 매개변수의 값을 조금 변화시키면, 손실함수는 어떻게 변하는가
  - 수식으로 손실함수 표현
    - `E = -1/N・sigma_{n}sigma_{k}(t_nk・log(y_nk))`
    - 데이터가 너무 많으면 손실함수의 값을 구하기 힘들어짐
    - 데이터 일부를 추려 근사치로 이용가능(mini-batch)
      - 통계학

## 3. 신경망 학습

### 손실 함수의 값을 최대한 줄이는 가중치 찾기

- 수치 미분(numerical_diff)
  - 정의
    - 무한소가 아닌, 아주 작은 차분으로 미분하는 것(근사)
      - c.f) 해석적 미분: 무한소를 이용한, 수학적인 미분(이론)
    - `df(x)/dx = lim_{n->0}((f(x+h)-f(x))/h)`
- 기울기(gradient)
  - 정의
    - 모든 변수의 편미분을 gradient라 함
      - e.g) `x0, x1의 편미분 동시에 계산 = (df/dx0, df/dx1)`
  - 특징
    - 기울기가 가리키는 방향은 각 장소에서 함수의 출력값을 가장 크게 줄이는 방향
      - *수학적으로 왜?*

```py
def numerical_diff(f, x):
  h = 1e-4
  grad = np.zeros_like(x)

  for idx in range(x.size):
    tmp_val = x[idx]

    x[idx] = temp_val + h
    fxh1 = f(x)

    x[idx] = temp_val - h
    fxh2 = f(x)

    grad[idx] = (fxh1-fxh2)/(2*h)
    x[idx] = tmp_val

  return grad
```

- 경사법(경사하강법)
  - 정의
    - 손실함수가 최솟값이 되는 매개변수(가중치, 편향)을 찾아야 함
    - 그 방법중에서 "기울기"를 잘 활용해 함수의 최솟값을 찾는 것이 경사법
  - 주의
    - 기울기가 가리키는 곳으로 가야 최솟값이 있는지, 그곳이 정말 나아가야 할 방향인지는 보장되지 않음
    - 오히려 복잡한 함수에서는 기울기가 가리키는 방향에 최솟값이 없는 경우가 대부분
      - e.g) 안장점(saddie point), 극솟값, 고원(plateau)
    - 그럼에도 불구하고 기울기 정보를 단서로 나아갈 방향을 정해야 함
  - 방법
    - `x0 = x0 - η・df/dx0`
      - `η`는 학습률(한번 학습에서 얼마나 학습해야 할지 - 매개변수값을 얼마나 갱신해야 할지)
      - `η`를 너무 크거나 작게 하면 안됨. 적당히 좋은 값 설정이 필요

```py
def gradient_decent(f, init_x, lr=0.01, step_num=100):
  x = init_x

  for i in range(step_num):
    grad = numerical_gradient(f,x)
    x -= lr * grad

  return x
```

- 하이퍼 파라미터
  - 정의
    - 사람이 직접 설정해야 하는 매개변수
    - 여러 후보값 중에서 시험을 통해 가장 잘 학습하는 값을 찾는 과정을 거쳐야 함
  - 예시
    - `η`
- 신경망에서 기울기
  - `dL/dW`
    - `L`는 손실함수
    - `W`는 가중치 행렬

TwoLayerNet의 예시

```py
import sys, os
sys.path.append(os.pardir)
from common.functions import *
from common.gradient import numerical_gradient

class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)

        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

    def predict(self, x):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']

        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)

        return y

    # x: input, t: answer label
    def loss(self, x, t):
        y = self.predict(x)

        return cross_entropy_error(y, t)

    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t) / float(x.shape[0])

        return accuracy

    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)

        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])

        return grads
```
