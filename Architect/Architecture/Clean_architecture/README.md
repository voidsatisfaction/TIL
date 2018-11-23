# Clean architecture

![](./images/clean-architecture.png)

## Clean architecture의 본질

- 레이어를 나눔으로 인해, 외부 환경이 변해도 비지니스 로직(도메인 로직)이 변경되지 않도록 하자

## DDD와의 관계

- 둘이 충분히 공존할 수 있음

## OOP로만 구현이 가능한가?

- 사실 Clean Architecture자체가 구현의 문제를 다루는 것이 아니라, 어떻게 레이어를 짜서 책임을 분담할 것인가를 다루는 문제
- 함수형 프로그래밍 패러다임으로도 구현 가능
  - 물론, OOP도 함수형 프로그래밍 패러다임에서 잘 쓰는 개념을 구현 가능
  - 언어는 사용자에게 affordance(행동 유도)를 제공할 뿐
