# Tensorflow-gpu 모듈 환경 설정

- 의문
- 순서
  - 도커를 사용하지 않는 경우(네이티브 윈도우 환경)

## 의문

## 순서

### 도커를 사용하지 않는 경우(네이티브 윈도우 환경)

https://www.tensorflow.org/install/gpu?hl=ko

- `python3 -c "import tensorflow as tf; tf.test.is_gpu_available()"`로 현재 gpu가 사용가능한지 확인
  - 이 커맨드는 수시로 활용
- CUDA 설치
  - 설치하고자 하는 `tensorflow-gpu` version과 compatible한 CUDA 버전 확인
  - 해당 CUDA 버전 설치
  - PATH 설정
- CUDNN 설치(설치를 해야만 위 커맨드로 tensorflow-gpu의 모듈을 runtime error없이 활용 가능)
  - 설치
  - CUDA가 설치된 `bin` 폴더에 CUDNN 넣어주기
- `python3 -c "import tensorflow as tf; tf.test.is_gpu_available()"`로 현재 gpu가 tensorflow에서 사용가능한지 확인
