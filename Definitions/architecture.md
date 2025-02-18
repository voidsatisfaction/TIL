# Architecture

- 의문
- General
  - Architecture
  - Architect
- Pattern
  - publish-subscribe(Pub-Sub)

## 의문

## General

### Architecture

Design stamina hypothesis

![](./images/architecture/architecture_design_stamina_hypothesis1.png)

- 정의
  - ANSI/IEEE
    - 정의
      - 그것의 컴포넌트와 서로간의 관계와 환경과 그것의 디자인과 발전을 관리하는 원칙으로 이루어진 시스템의 근본적인 구조
  - 마틴 파울러
    - 정의
      - **겁나 중요한 것**
    - 특징
      - **프로젝트 관련 전문 개발자 끼리 공유하고 있는 지식** &
        - 해당 지식에는 모든 개발자들에 의해서 이해되는 컴포넌트와 인터페이스를 포함함
        - group consensus가 중요함
        - 따라서, 위의 정의에 의하면, 프로그래밍 언어도 architecture에 속한다고 볼 수 있음
        - 무엇이 핵심인가?
          - **개발자들이 생각하는 핵심이 아키텍처에 속함**
            - 따라서, '무엇을 개발하려는지, 그 개발하려는 것에서 무엇이 핵심인지'에 따라서 아키텍처는 달라짐
          - 핵심을 코드로 녹임
          - 아키텍처에서는 핵심 가치를 위한 결정들이 매우 중요함
      - **결정된 선택은 바꾸기 어려운 것**
        - 그래서 미리 잘 결정하는 것이 중요함
        - e.g)
          - DB 스키마를 가장 먼저 작성하는 이유(바꾸기 힘들어서)
          - DB 스키마를 쉽게 바꿀 수 있도록 조치하면, DB schema는 더이상 아키텍처적인 요소라고 부르지 않음
        - irreversibility(비가역성)이 그 원인
      - **경제(economics)적 관점으로 생각해야 하는 것**
        - quality라는 것은 cost의 tradeoff이다
        - 하지만, 소프트웨어의 quality는 end user에게는 전혀 보이지 않음
          - 참고: 아키텍처와 quality
            - external
              - 엔드 유저와 직접적으로 관련이 있는 quality
                - **기능 추가**
            - internal
              - 엔드 유저에게 직접적으로 보이지 않음
                - **소프트웨어 아키텍처**
              - 장기적인 관점에서 중요
    - 특징2
      - **전문 개발자들은 시스템 디자인에 대한 이해를 공유함**
        - 아키텍처는 사회적 요소가 꽤나 많이 영향을 끼침
        - 그림을 그리는 것은 '표현'일 뿐
      - 아키텍처 디자인에 관한 결정은 일찍 정해져야 함
      - 결정은 바꾸기 매우 어려움
    - 왜 아키텍처는 중요한가?
      - 아키텍처를 고려한 설계와 고려하지 않은 설계의 차이
        - 고려하지 않는다면, 새로운 기능을 추가하는데에 점점 힘들어 질 것
          - Design stamina hypothesis
          - **이것이 소프트웨어 아키텍처가 중요한 이유!**
        - 낮은 퀄리티의 소프트웨어는 시간을 계속해서 잡아먹기만 함
          - CI, CD를 도입하려는 이유
          - 결국 **경제적 관점** 에서 소프트웨어 아키텍처가 매우 중요함
            - craftmanship이 아니다!!!

### Architect

- 참고
  - [마틴 파울러 - Who Needs an Architect?](http://files.catwell.info/misc/mirror/2003-martin-fowler-who-needs-an-architect.pdf)
- 정의
  - 겁나 중요한 것을 다루는 사람
    - architecture = 겁나 중요한 것
- 역할
  - **1 프로젝트가 어떻게 흘러가는 지 큰그림 파악**
    - 심각한 문제가 터지기 전에 미리 대응 착수
  - **2 협력**
    - e.g)
      - 아침에, 개발자와 보틀넥이 되는 코드를 같이 프로그램함
      - 오후에, requirements 세션에 참가하여 개발 비용등에 관한 협의 비 기술적인 언어로 설명
  - **3 개발팀 멘토링**
    - 개발팀 전체의 수준을 끌어올려, 복잡한 문제도 해결 가능하게 함
    - 아키텍트가 프로젝트에 대해서 내리는 의사 결정의 개수를 줄임
      - 아키텍트의 가치는 자신이 내리는 프로젝트에 대한 의사 결정에 반비례함
  - **4 소프트웨어 디자인에 있어서 irreversibility를 제거할 수 있는 방법을 찾아서 architecture를 제거 하는 것**
- 명언
  - Software is not limited by physics, like buildings are. It is limited by imagination, by design, by organization, In short, **it is limited by properties of people** , not by properties of the world. **"We have met the enemy, and he is us."**

## Pattern

### Publish-subscribe(Pub-Sub)

- 정의
  - 메시지의 송신자(publisher)는 특정 receiver로 메시지를 직접 보내지게 되도록 프로그램하지 않고, published message를 클래스로 나누어서 카테고리화 함
    - 수신자에 대해서 무지
  - 메시지의 수신자(subscriber)는 특정 메시지 타입만 구독
    - 송신자에 대해서 무지
- 특징
  - message queue 패러다임의 자손
- Message filtering
  - 정의
    - reception을 위한 메시지를 선택하고, 가공하는 프로세스를 filtering이라 함
  - 종류
    - topic-based
      - publisher가 정의한 topic(logical channel)을 subscriber가 구독하고 있으면 그 메시지를 전달
    - content-based
      - subscriber가 정의한 제한과 메시지의 attributes나 content가 매치되면 해당 메시지를 전달
    - hybrid
- 구성
  - 큰 그림
    - pub -----> message broker(event bus) <-----> sub
  - 주체
    - pub
    - message broker
      - filtering을 행함
      - store and forward
      - message prioritize
    - sub
- DDS(Data Distribution Service)에서의 PubSub
  - 특징
    - broker가 존재하지 않음
    - Pub와 Sub는 meta-data를 IP multicast를 통해서 공유함
    - 공유된 metadata를 캐시하고, message를 route함
- 장점
  - Loose coupling
    - Pub와 Sub는 시스템 구조에 대해서 무지해도 됨
    - 유연함
      - c.f) client server 시스템
  - Scalability
- 단점
  - Message delivery issues
    - 메시지가 반드시 도달하는 것을 보장하도록 잘 설계해야 함
    - subscriber가 구독하고 있지 않아도, publisher는 구독하고 있다고 착각하는 경우가 있음
  - PubSub의 노드 수가 많아질 때 문제가 생길 가능성이 매우 커짐
  - DOS 공격에 취약
  - broker가 잘못된 sub에게 메시지를 보낼 위험성
