# Designing Data Intensive Application

- 의문
- 개요
  - Data-intensive
  - Data-intensive application helper tools

## 의문

## 개요

### Data-intensive

- Data-intensive
  - 데이터가 주된 challenge
    - 데이터의 양
    - 데이터의 복잡도
    - 데이터의 속도
- c.f) compute-intensive
  - CPU cycle이 bottleneck

### Data-intensive application helper tools

- NoSQL
- message queues
- caches
- search indexes
- frameworks for batch
- stream processing
- ...

위의 기술의 조합으로 data-intensive application을 작성

## Reliable, Scalable, Maintainable Applications

시스템을 설계 및 제작 및 운영하는데에 가장 중요한 3가지 요소

- Reliability
  - 정의
    - 시스템에 갑작스런 fault들이 등장해도 계속해서 올바르게 동작하는 것
      - fault는 용인하되, failure는 용인하지 않음
      - 당연히 일반적인 상황에서는 계속해서 올바르게 동작해야 함
    - *Availability와 비슷한 개념? 같은 개념?*
- Scalability
  - 정의
    - 시스템이 커질 수록, 그러한 성장을 다루는 합리적인 방법 존재하는 것
- Maintainability
  - 정의
    - 서로 다른 시스템의 개발자들이 생산성 있게 일을 할 수 있는 것
- (Security)
  - 정의
    - 보안

### Reliability

- 용어 정리
  - faults
    - 정의
      - 잘못될 수 있는 것들
    - c.f) fault-tolerant / resilient
      - 정의
        - faults를 예측하고, 그것들을 잘 다룰 수 있는 것
          - predict가 아닌 tolerant
          - 단, security는 predict가 바람직
        - faults를 다 막을수는 없으나, failure는 막자
  - failure
    - 정의
      - 전체적인 시스템이 유저에게 필요한 모든 서비스들을 제공할 수 없을 때
- fault-tolerant system 만들기 위한 전략
  - 일부러 fault를 많이 만들어보자
- faults의 종류
  - **Hardware faults**
    - 예시
      - Hard disks crash
        - 평균적으로 10 to 50 years에 망가짐
        - 따라서 1만개의 디스크가 있으면, 평균적으로 한개의 디스크가 고장난다고 생각해야 함
      - RAM faulty
      - power grid blackout
      - unplug the wrong network cable
    - 해결 방법
      - redundancy
        - disk의 경우 RAID 설정을 함
        - server의 경우, dual power supplies, hot-swappable CPU를 사용
        - data center에서는 백업 전원을 위한 배터리와 디젤 생성기를 갖고 있을 수 있음
      - software
        - 머신을 리부팅해야할 때, *rolling upgrade*를 사용하여 하나의 노드를 한 타이밍에 리부팅 할 수 있음
  - **Software Errors**
    - 개요
      - 하드웨어 에러의 경우 일반적으로, 독립적이고 서로 약한 상관관계를 갖음
      - 소프트웨어 에러는 예측하기 더 어렵고, 노드에 걸쳐서 서로 상관관계가 있으므로, 상관관계가 옅은 하드웨어 faults보다 더 많은 시스템 faults를 일으킬 가능성이 큼
    - 예시
      - 특정 bad input을 넣으면 application server가 크래시 되는 경우
      - CPU, memory, disk space, network bandwith와 같은 공유 자원을 다 사용해버리는 *runaway process*
      - cascading failures
        - 하나 컴포넌트에 있어서의 fault가 다른 컴포넌트에 fault를 일으키고, 그것이 더 많은 faults를 일으키는 경우
    - 해결 방법(작은 방법들의 결합)
      - 시스템 안의 전제와 상호작용을 주의깊게 생각하는 것
      - 철저한 테스팅
      - 프로세스 격리
      - 프로세스가 크래시되고 재시작하는 것을 가능하게 하는 것
      - measuring
      - monitoring
      - production 모드에서 시스템 행동을 분석하는 것
  - **Human Errors**
    - 개요
      - 사람은 reliable하지 않음
        - 대부분의 큰 인터넷 서비스의 faults중에서 hardware faults는 오직 10-25%만 차지하고 나머지는 human configuration error임
    - 해결 방법
      - 에러가 날 기회를 최소화하는 방향으로 시스템을 디자인 함
        - 잘 설계된 추상화, APIs, admin 인터페이스는 올바른 일을 하기 쉽게 독려하고, 옳지 않은 일을 하기 어렵게 함
        - 하지만, 인터페이스가 너무 제한적이면 사람들은 work around를 찾으려 하므로, balance를 맞추는 것이 좋음
      - 사람들이 가장 많이 실수를 저지르는 장소와 그것들이 system failures를 야기할 수 있는 곳을 decouple해야 함
        - 사람들이 실제 대이터를 기반으로 쉽게 실험할 수 있는 *sandbox* non-production 환경을 제공하자
      - 모든 레벨에서 테스트를 철저히 함
        - unit test -> 전체 시스템 integration tests -> 수동 테스트
        - 코너 케이스도 잘 파악하자
      - human error로부터 빠르고 쉬운 recovery가 가능하도록 함
        - 빠르게 configuration 변화를 roll back하거나, 새 코드를 점진적으로 roll out하거나, 데이터를 recompute하는 툴을 제공
      - 자세하고 명확한 모니터링을 구축
        - performance metrics
        - error rates
      - 좋은 관리 관습과 training을 구현
