# 오브젝트 지향 디자인이란?(Object-Oriented Design?)

- 참고
  - [What Is Object-Oriented Design?](http://web.archive.org/web/20131031015906/http://www.objectmentor.com:80/omSolutions/oops_what.html)
  - [객체 지향의 사실과 오해 - 메모](https://taehwanno.github.io/post/oop/2016/09/%EA%B0%9D%EC%B2%B4%EC%A7%80%ED%96%A5%EC%9D%98-%EC%82%AC%EC%8B%A4%EA%B3%BC-%EC%98%A4%ED%95%B4)
- 목차
  - Introduction
  - The principles of Object Oriented Design and Dependency Management
    - 썩은 디자인의 증상
    - 의존성 관리
    - 오브젝트 지향 클래스 디자인의 원칙
  - SRP — The Single Responsibility Principle
  - OCP — The Open Closed Principle
  - LSP — The Liskov Substitution Principle
  - DIP — The Dependency Inversion Principle
  - ISP — The Interface Segregation Principle
  - REP — The Reuse Release Equivalency Principle
  - CCP — The Common Closure Principle Principle
  - CRP — The Common Reuse Principle
  - ADP — The Acyclic Dependencies Principle
  - SDP — The Stable Dependencies Principle
  - SAP — The Stable Abstractions Principle

## Introduction

- 오브젝트 지향 디자인은 60년대 말에 프로그램이 점점 복잡해지면서 생겨난 프로그래밍 패러다임
- 실제 세상의 물체들에 기반한 소프트웨어 시스템 모델링
  - e.g 뱅킹 시스템은 고객, 계좌 오브젝트를 포함하는 등
- 올바르게 사용하는 것이 매우 중요

## The principles of Object Oriented Design and Dependency Management

- 소프트웨어 아키텍처의 정의
  - 높은 수준의 레벨
    - 애플리케이션의 전체적인 모양과 구조를 정의하는 패턴
  - 하나 낮은 레벨
    - 소프트웨어 애플리케이션의 목적과 연관 되어있음
  - 그보다 하나 낮은 레벨
    - 모듈과 그 사이의 연결에 대한 아키텍처
    - 디자인 패턴의 도메인
      - 패키지
      - 컴포넌트
      - 클래스

### 아키텍처와 의존성(Architecture and Dependencies)

- 처음에는 아름답던 소프트웨어 아키텍처가 시간이 지날 수록 못생겨지고 관리하기 어렵게 됨

#### 썩은 디자인의 증상

대표적으로 경직성, 취약성, 이동불가능성, 점성 이라는 네가지 특징을 갖음

- 경직성(Rigidity)
  - 소프트웨어가 변경하기 힘들어지는 특성
  - 하나의 변화가 또 다른 의존하는 모듈의 변화를 가져옴
- 취약성(Fragility)
  - 소프트웨어가 변화할 때마다 많은 다른 부분이 망가지는 특성
  - 시간적 손실이 커짐
  - 버그를 고치는 것이 새로운 버그를 낳음
- 이동불가능성(Immobility)
  - 다른 프로젝트나, 같은 프로젝트의 어떠한 다른 부분으로 부터 재사용 할 수 없는 특성
- 점성(Viscosity)
  - 디자인의 점성
    - 개발자가 디자인을 지기면서 변경을 하는 것 보다 디자인을 어기면서 변경을 하는 것이 더 쉬운 경우
  - 환경의 점성
    - 컴파일 시간이 너무 오래걸리면 엔지니어는, 디자인의 관점에서는 비효율적인 컴파일 시간이 덜 걸리는 방법으로 구현하려 함

#### 변화 요구

- 디자인 퀄리티의 저하는, 초기 디자인이 미래의 변화까지 예측할 수 없기 때문에 발생

#### 의존성 관리

- 디자인을 썩게 만드는 변화
  - **새롭고 계획되지 않은 의존성의 추가**
- 오브젝트 지향 프로그래밍의 핵심

### 오브젝트 지향 클래스의 디자인

#### The Open Closed Principle

> 모듈은 확장에는 열려있고, 변경에는 닫혀있어야 한다.

- 코드의 변경 없이 모듈이 변화하도록 해야함
  - 무조건 확장으로
- 추상화가 키 포인트

##### 동적 다형성(Dynamic Polymorphism)

```cpp
struct Modem
{
  enum Type {hayes, courrier, ernie} type;
};

struct Hayes
{
  Modem::Type type;
  // Hayes related stuff
}
```
