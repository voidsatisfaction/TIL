# Spring WebFlux

- 의문
- 개요

## 의문

## 개요

- webflux
  - 개요
    - Netty, Undertow, Servlet3.1+ 컨테이너와 같은 논블로킹 서버에서 실행되는 Reactive Streams API기반의 Reactive 스택 웹 애플리케이션 프레임워크
  - 특징
    - Spring Web MVC의 소스 모듈 `spring-webmvc`와, Web flux 소스 모듈 `spring-webflux`가 Spring framework 내부에서 공존함
      - 각 모듈은 optional
      - 따라서, application은 둘다 사용할 수 있고, 하나만 사용할 수 있음
      - e.g)
        - Spring MVC controller와 reactive `WebClient`의 공존
  - 등장 배경
    - 1 적은 스레드의 개수로도 동시성을 다룰 수 있는 논 블로킹 웹 스택의 필요성
    - 2 함수형 프로그래밍
- c.f) Spring Web MVC
  - 개요
    - Servlet API와 Servlet 컨테이너를 위해서 만들어진 웹 프레임워크
