# Reactive Streams

## 의문

## 개요

- 개요
  - 논 블로킹 백프레셔가 가능한 비동기 스트림 프로세싱의 JVM 표준을 제공
- 목표
  - 잠재적으로 unbounded 숫자의 요소를 가공
  - 순차적이며
  - 비동기적으로 컴포넌트 사이에 요소들을 넘겨줌
  - backpressure가 논 블로킹
- 특징
  - API
    - Reactive Streams를 구현하기 위한 타입을 명시
  - TCK(Technology Compatibility Kit)
    - 구현의 적합도를 확인하기위한 표준 테스트

## API 컴포넌트

- 구성
  - Publisher
    - 잠재적으로 unbounded한 숫자의 순차적인 요소들의 제공자
      - Subscriber로부터 수요 요청에 따라서 퍼블리싱함
  - Subscriber
  - Subscription
  - Processor
