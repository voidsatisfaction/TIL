# Advice for applying machine learning & machine learning system design

- 의문
- Advice for applying machine learning
  - Evaluating a Learning Algorithm
  - Bias vs Variance
- Machine learning system design
  - Building a Spam Classifier
  - Handling Skewed Data
  - Using Large Data Sets

## 의문

## Advice for applying machine learning

### Evaluating a Learning Algorithm

- 문제
  - housing price를 예측하기 위하여, regularized linear regression을 구현했는데, hypothesis가 test set에서 예측이 매우 크게 벗어나는 현상이 발생하면, 우리는 무엇을 해야하는가?
- 우리가 취할 수 있는 선택지
  - 트레이닝 데이터셋을 늘린다
  - 피쳐의 수를 줄인다
  - 피쳐의 수를 늘린다
  - polynomial 피쳐를 추가한다
  - λ를 감소 시킨다
  - λ를 증가 시킨다

### Evaluating a Hypothesis

Training/testing procedure for logistic regression

![](./images/week6/training_testing_procedure1.png)

- 데이터의 분리
  - training set(70%)
    - Parameter learning에 사용
  - test set(30%)
    - Test set error를 구해서 학습된 모델이 얼마나 잘 맞는지 확인
      - regression의 경우
        - `Jtest(θ) = 1/2m sigma_{i=1}^{m}(hθ(x(i))-y(i))^2`를 구함
      - classification의 경우
        - Misclassification error를 구함
          - `err(hθ(x),y)`
            - `1 (if (hθ(x)≥0.5 and y=0) or (hθ(x)<0.5 and y=1))`
            - `0 (else)`
          - `Test Error = 1/m sigma_{i=1}^{m}(err(hθ(x(i)), y(i)))`

### Model Selection and Train/Validation/Test Sets

Model selection

![](./images/week6/train_validation_test1.png)

- 위의 내용 부연 설명
  - training set으로 θ를 각각 degree에 따라서 학습시킴
  - test set으로 각 학습시킨 모델의 성능을 degree에 따라서 비교
    - 근데 그냥 여기서 `Jtest(θ(5))`를 가지고 일반적인 성능이 좋다 나쁘다를 따질 수 없음
    - `Jtest(θ(5))`가 optimistic estMimate of generalization error일 수 있기 때문
      - `d = polynomial의 degree`가 test set에 피팅되어있다고 봄(**다른 degree의 모델을 이겼다는 사실이 추가되니까**)

Train/Validation/Test error expressions

![](./images/week6/train_validation_test_error2.png)

- Training set(60%)
  - 파라미터 학습에 사용
- Validation set(20%)
  - 모델 끼리의 cross validation에 사용 등
- Test set(20%)
  - hypothesis의 일반적인 성능 측정에 사용

### Bias vs Variance

bias vs variance

![](./images/week6/diagnosing_bias_vs_variance1.png)

diagnosing high bias vs high variance

![](./images/week6/diagnosing_bias_vs_variance2.png)

- Diagnosing Bias vs Variance

Regularization and Bias/Variance

![](./images/week6/regularization_and_bias_vs_variance1.png)

- Regularization and Bias/Variance
  - 개요
    - Regularization이 Bias와 Variance에 미치는 영향은?
  - d와 λ의 선정 방법(일반적인 여러 파라미터)
    - `λ=0`, `λ=0.01` 에서 `λ=10`까지 `λ:=λ*2`로 늘려나감 list of λ를 생성
    - 서로 다른 degree 또는 다른 변수를 가지고 모델을 생성
    - 각 λ를 iterate하면서, θ학습
    - 얻어진 θ를 바탕으로 cross validation error를 구함
      - **대신 이때의 Jcv(θ)는 regularization term을 고려하지 않아야 함**
    - cross validation error가 가장 낮은 조합을 선택
    - 선택된 조합으로 `Jtest(θ)`에 적용하여, generalization이 충분히 잘 되었는지 확인

### Learning Curve

Learning curve of high biased model

![](./images/week6/learning_curve1.png)

Learning curve of high variance model

- 개요
  - x축이 training set size, y축이 error
  - 현재의 모델이 high variance인지, high biased인지 판단할 수 있도록 도와주는 커브
    - 항상 그려보자!
- 케이스 분석
  - high bias
    - 모델 자체가 bias가 높을경우에, training data set이 많다고 하더라도 별 도움이 되지 않음
  - high variance
    - 모델 자체가 variance가 높을경우는, training data set이 많아지면 도움이 될 가능성이 있음

### Deciding What to Do Next Revisited

![](./images/week6/debugging_a_learning_algorithm1.png)

- 문제
  - 새로 만든모델이 Large error를 내는 경우 어떻게 할 것인가?
- 해결
  - 1 high variance문제인지, high bias문제인지 확인
  - 2 각각의 문제에 맞는 전략 시행

Neural Network and Overfitting

![](./images/week6/neural_network_and_overfitting1.png)

- NN의 경우, 하나의 hidden layer로 시작한 뒤에, 다수의 hidden layers로 넘어가서 cross validation set으로 검증해보면 좋음

## Machine learning system design

### Building a Spam Classifier

### Handling Skewed Data

### Using Large Data Sets
