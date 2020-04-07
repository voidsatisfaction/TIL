# Nonce

## 의문

## 개요

the application of nonce

![](./images/nonce.png)

- 정의
  - 오직 한 번만 사용되는 숫자나 값
    - pseudo-random number
- 특징
  - 값을 재활용하지 못하게 하므로써, replay attack을 막아줌
  - 일반적으로는 timestamp를 포함해서 timeliness를 보장
  - 중복 값이 생기면 안됨
    - time-variant or
    - generated with enough random bits
  - nonce는 암호화 되는 정보에 대한 originality를 부여하는 역할
    - 같은 주문들을 같은 nonce로 받게되면, 그 주문들을 invalid라고 평가
