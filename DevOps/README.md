# DevOps

- 의문
- 추천 자료
- 0 업무 범위
- 1 DevOps의 기본적 이해
  - 5가지 철학(CAMSP)
  - Immutable infrastructure
- 2 DevOps 엔지니어의 역할
  - DevOps 엔지니어가 갖추어야할 스킬
  - IaaC(Infrastructure as Code)
  - 데브옵스 로드맵

## 의문

공부방법은, 지금 당장 설치하고 작성해서 무엇을 만드는게 최고다

## 참고 자료

- 모니터링
  - 성능 모니터링
    - https://www.brendangregg.com/methodology.html
      - use, tsa 등 추천
    - [위의 저자가 쓴 책 - System Performance](https://www.amazon.com/Systems-Performance-Brendan-Gregg/dp/0136820158/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=deirdrestraug-20&linkId=815ef3388ba65b674f4f8fd582713f24&language=en_US)

## 0. 업무 범위

애플리케이션 개발도 병행하여 기본적으로 해당 도메인을 잘 알아야 수월히 업무를 진행할 수 있음

- 인프라 구축
  - 클라우드(온프레미스)
  - IaaC
- 애플리케이션 제작
  - 아키텍처 설계
  - 최적화
- CI/CD 파이프라인
  - CI
  - CD
- 운영
  - 모니터링
    - 인프라 모니터링
    - 로그, 메트릭, 트레이스, apm 관제 시스템 구축
      - prometheus
      - Elastic stack
        - Elastic APM
    - 얼럿 시스템 세팅
      - infrastructure
        - cloud watch(USE method) + SNS + Slack(or PagerDuty or Email)
          - DB CPU utilization
          - DB load
          - DB rollback history segment
          - Queue too long waiting task alert
          - Queue saturation alert
          - Queue dead letter queue
        - alertmanager(prometheus)
          - USE method
          - cluster
          - node
          - deployment
          - service
          - persistence volume
      - application
        - sentry
        - prometheus
  - 배포 전략
    - rolling update
    - canary deploy
  - 장애 예방
    - 이중화
  - 컨테이너 오케스트레이션
    - k8s
    - helm
  - DB 관리
    - 장애가 나기 쉬운 지점 관리하기
      - e.g) foreign key추가로 인한 metadata lock 이슈등
    - 파라미터 튜닝
- 장애대응
  - 모니터링 지표를 보고 대응
  - AINDA
    - Alert
    - Infra
    - Network
    - DB
    - Application
  - 장애 문서 작성
- 보안
  - IAM role을 사용한 개발 프로세스 정립
  - https://alas.aws.amazon.com/
    - rss feed를 구독해서 계속 관리하자
- 각종 자동화
  - 프로그래머 대신 컴퓨터가 대신 하도록

## 1. DevOps

- 개요
  - **어떤 요구사항을 효율적(빠르게)으로 만족시키기 위하여, 일을 자동화하며 변경사항 지표들을 측정하고, 공유하고, 이 모든 결과물들을 지속적으로 축적해 나가아가는 문화를 만들어가는 철학, 방법론, 기술**
  - 소프트웨어를 유저에게 전달하는데에 생산성을 증대하는 모든 활동
    - 속도와 효율화
      - 복잡한 현대 서비스(S/W)를 DevOps철학과 방법론으로 풀어나가기
- 고성과 조직이 저성과 조직보다 나은 점
  - 계획에서 배포까지의 리드 타임 속도 440배 빠름
  - 코드 배포 횟수 46배
  - 다운타임에서 회복하는 평균 시간 170배 빠름
  - 변화 실패할 확률 1/5
  - 위와 같은 결과는, 올바른 케이퍼빌리티를 향상시켰는가의 차이

### 소프트웨어 전달 성과의 측정

- 기존
  - 코드 라인 수
  - 진척도(스토리포인트)
    - 상대적
  - 가동률
    - 너무 높은 가동률은, 오히려 일을 완료하는데에 드는 리드 타임이 기하급수적으로 늘어날 수 있음
- 신규
  - 리드 타임
    - 어떤 일을 완료하는데에 드는 시간
    - 고객이 요청하는 시점부터 그 요청을 만족시킬 때까지 걸린 총시간
      - `피처를 설계하고 구현하는 데에 걸리는 시간 + 피처를 고객에게 전달하는 데 걸리는 시간`
    - 고성과 조직
      - **1시간 이하**
  - 배포 빈도
    - 소프트웨어 전달 주기에 관한 성과 측정 방법(릴리스)
    - 고성과 조직
      - **원할때 언제나**
  - 서비스 복구에 걸리는 시간
    - 빠르게 변화하는 복잡한 시스템인 현대의 소프트웨어 제품이나 서비스에서의 실패는 불가피하므로, 얼마나 빠르게 복구하는가가 중요해짐
    - 고성과 조직
      - **1시간 이하**
  - 변경 실패율
    - 전체 배포의 수에 대해서 배포된 이후, 고쳐져야 하거나, 패치되어야 하거나, 롤백되어야 하는 것들의 비율
    - 고성과 조직
      - **0~15%**

### 5가지 철학(CAMSP)

- 문화
  - 하나의 문화를 만들어 나갑니다
  - 구성요소
    - 사람(팀, 인원), 일(프로세스, 방법론), 서비스(서비스의 가치, 성격), 자원(H/W, S/W, 기술, 도구), 시간(일정, 변경 가능성, 회복탄력성, 예측)
- 자동화
  - 자동화를 통해 효율성과 빠른 속도를 지향합니다
  - 구성요소
    - 인프라 및 보안(클라우드, 네트워크, 접근제어, 암호화), 언어 및 도구, CI/CD, 모니터링
- 측정
  - 지표를 측정하여 지속적으로 개선해 나갑니다
    - 변경사항 발생시, 항상 측정(예측 불가능 -> 예측 가능)
    - 애플리케이션 성능, 개발속도 모니터링
    - 나아지고 있는지, 아닌지 측정
    - 의사결정 시 추측 배제
- 공유
  - 언제든 접근 가능한 투명한 데이터
  - 지식의 공유 OpenMind
    - 인턴이 CTO가 해결하지 못하는 문제도 해결 가능
  - 문제 발생시 함께 해결
  - 일의 가속도
- 축적
  - 기록을 축적하여 자산을 만들어 나갑니다
    - 효율적으로 1만 시간의 법칙을 이루어 내는 것
    - 루이비똥은 100년전의 디자이너의 생각도 기록해뒀음

### Immutable Infrastructure

- 개요
  - 배포이후에 수정이 불가능
    - 업데이트(x)
    - 패치(x)
    - 설정 변경(x)
  - 새로 이미지를 만들어서 다시 배포해야 함
- 장점
  - 버전 트래킹이 쉬움
  - 롤백이 쉬움
  - 일관적인 테스팅 프로세스

## 2. DevOps 엔지니어의 역할

- 개요
  - 올바른 DevOps 문화를 위해 서비스 혹은 S/W 라이프 사이클에서 반복적인 일들을 자동화하고, 기술적 문제 혹은 팀의 차이를 기술적으로 예방하고, 해소시키는 사람
- 특징
  - 기획팀 / 마케팅팀의 업무를 자동화 하는것도 DevOps의 역할이라고 할 수도 있음
  - 공통된 기술들을 다양한 곳에 접목시키는 것

### DevOps 엔지니어가 갖추어야할 스킬

소프트 스킬

![](./images/soft_skill1.png)

기술적 스킬

![](./images/technical_skill1.png)

### IaaC(Infrastructure as Code)

- 개요
  - 인프라를 이루는 서버, 미들웨어 그리고 서비스 등, 인프라 구성요소들을 코드를 통해 구축하는 것
- (코드로서의) 장점
  - 작성용이성
  - 재사용성
  - 유지보수
  - 생산성
- 대표적으로 Terraform이 있음

### 데브옵스 로드맵

![](./images/devops_loadmap1.png)

위의 선형구조가 순서는 아니고, 전체가 다 중요함
