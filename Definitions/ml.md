# ML

- General
  - Feature(ML)
- Neural Network
  - Autoencoder
- Technique
  - Batch Normalization(BN)

## General

### Feature(ML)

- 개요
  - 관찰되는 현상의 특징이나 측정가능한 개개의 특성
  - informative, discriminating, independent feature를 선택하는 것이, 패턴인식, classification, regression 문제 해결에 매우 중요
  - 일반적으로 수치로 나타나지만, string이나 graph와 같은 structure로 나타나는 경우도 존재
    - syntactic pattern recognition

## Neural Network

### Autoencoder

Simple Autoencoder Architecture Diagram

![](./images/ml/autoencoder1.png)

Autoencoder Architecture and mathematical expressions

![](./images/ml/autoencoder2.png)

- 정의
  - NN의 한 종류
    - input을 output으로 복사
    - 단순히 복사하는 것이 아니고, 근사적으로 복사해서, 데이터의 가장 관련있는(핵심) 점만 복사해서 보존
      - noise제거
  - unsupervised한 방식으로 *efficient data coding*을 학습하는 인공 신경망의 한 종류
  - signal noise를 무시하기 위해서 network를 학습시키므로써 데이터 집합의 representation(encoding)를 학습시키는 것이 목적
    - dimensionality reduction
- 구조
  - encoder(reductor)
    - input -> code
  - decoder(reconstructor)
    - code -> output(reconstruction of the input)
    - reduced encoding으로 부터, original input과 아주 유사한 representation을 생성
- 학습
  - `L(x, x') = ||x-x'||^2`
    - MSE등의 error를 이용해서 loss function을 구성 가능
- 응용
  - dimensionality reduction
  - feature learning
  - *Information retrieval*
  - Anomaly detection
    - normal data로만 training시키고, anomaly data가 들어오면 reconstruction performance가 나빠지는 것을 이용해서 anomaly detection을 행함
      - reconstruction error
      - 그런데, 최신 논문에서는 anomaly마저 reconstructing을 매우 잘하는 모델이 생겼다고 함
  - Image processing
    - lossy image compression
    - image denoising
    - super-resolution
    - machine translation

## Technique

### Batch Normalization(BN)

Batch Normalization Transform

![](./images/ml/batch_normalization_transform1.png)

- 정의
  - re-centering, re-scaling을 통한 input layer의 normalization을 통하여, 더 빠르고, 안정적인 인공 신경망을 만드는 방법
    - in-layer normalization
- 동기
  - NN의 각 레이어는 분포를 갖는 input을 갖고 있고, 이러한 input은 parameter initialization과 input data에서의 randomness에 의해서 training process에 영향을 받음
    - 이러한 internal layer들에 대한 input 데이터 분포의 randomness의 영향을 **internal covariate shift** 라고 함
    - 실제로 실험에서 training시에 internal layer input의 mean, variance를 변화하면 관찰이 되는 현상
  - BN은 internal covariate shift를 완화 하기 위함
    - training stage중에, 앞선 layer들의 파라미터가 변하면, 현재 layer에 있어서의 input의 분포도 따라서 변화하고, 결국 현재 layer도 새로운 distribution마다 계속 다시 조정되어야 함
    - deep network의 경우, shallower hidden layer의 작은 변화가 network의 더 깊은 layer에 그 효과가 증폭됨
- 특징
  - Optimization을 도와줌(속도 향상)
    - 정확한 이유는 모름
      - 내부적 covariate shift를 완화?
      - *objective function* 을 smooth함?
      - length-direction decoupling?
  - Regularization효과
    - 굳이 dropout을 사용할 필요가 없음
  - Learning rate에 크게 영향을 받지 않음
    - gradient exploding / vanishing이 없어짐
