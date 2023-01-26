# Reliability vs Scalability vs Maintainability vs Availability

- 의문
- 개요
  - Reliability vs Availability
  - Scalability
  - Maintainability

## 의문

## 개요

- Reliability vs Availability
- Scalability
- Maintainability

### Reliability vs Availability

- Reliability
  - 개요
    - 특정 시간동안 실패(failure) 없이 의도된 동작을 수행하는 시스템의 능력
      - fault tolerant(fault가 있어도 failure로는 이어지지 않게하는 능력)
  - 메트릭
    - failure_count / time_window
- Availability
  - 개요
    - 시스템이 동작하는 상태인 시간의 비율(uptime)
  - 메트릭
    - uptime / time_window
- 주의
  - Reliability가 높지만, Availability는 비교적 낮을 수 있음
    - e.g) 애플리케이션에 문제가 생기는 경우는 매우 드물지만, 한 번 문제가 생기면 서비스의 downtime이 길다
  - Reliability는 낮지만, Availability는 비교적 높을 수 있음
    - e.g) 애플리케이션에 문제는 다소 자주 생기지만, 서비스의 downtime은 아예 없거나 거의 없을 수 있음

### Scalability

- 개요
  - 시스템의 아키텍처를 변경시키지 않고 시스템이 부하나 요청의 증가량을 다룰 수 있는 능력
- 특징
  - vertical scalability(scale-up)
    - 하나의 노드의 자원을 늘려서 증가된 부하를 처리함
  - horizontal scalability(scale-out)
    - 더 많은 노드를 늘려서 증가된 부하를 처리함
- 메트릭
  - requests/s, loads/s, tx/s

### Maintainability

- 개요
  - 시스템이 얼마나 유지보수하고 새 기능을 추가하기 쉬운지에 대한 능력
- 요소
  - operability
    - 운영하기 쉬움
  - simplicity
    - 시스템 복잡도를 줄이고, 이해하기 쉽게 만들기
  - evolvability
    - 엔지니어가 이후 시스템을 쉽게 변경할 수 있게 하기
- 메트릭
  - 리드 타임, 배포 횟수
