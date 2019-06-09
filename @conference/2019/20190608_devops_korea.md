# 20190608 - Devops korea meetup

- [데브옵스란 무엇인가](https://aws.amazon.com/ko/devops/what-is-devops/)
- 종합
  - DevOps의 본질
  - DevOps의 작동 방식
  - 장점
- 세션1: 운영팀 없는 스타트업에서 개발자가 알아야 하는 서비스 운영지식
- 세션2: DevOps의 인문학적 접근
- 세션3: DevOps art 1년부채부터 10년부채까지
  - Migration
  - Devops란
- 세션4: DevSecOps를 접해보시렵니까?
  - Devops
  - Doing DevOps
  - Doing DevSecOps

## 종합

**~샤오미 밴드를 획득한 아주 바람직하고 좋은 컨퍼런스~**

**~무려 1/3의 사람들이 경품 받고 돌아간 즐거운 컨퍼런스~**

![](./images/what_is_devops.png)

- DevOps의 본질
  - 애플리케이션과 서비스를 빠른 속도로 제공할 수 있도록 조직의 역량을 향상시키는 문화 철학, 방식, 도구의 조합
    - IT가 비즈니스의 핵심적인 구성요소가 되면서, 소프트웨어를 구축하고 제공하는 방법의 혁신이 필요하게 됨
  - DevOps는 다음과 같은 시각으로 접근이 가능하다
    - Culture
    - 그것을 구현하기 위한 Technology
    - Shared Ownership
      - freedom & responsibility
  - 애자일이 애플리케이션 자체를 빠르게 개발하기 위한 방법론이라면, DevOps는 소프트웨어 라이프 사이클을 빠르고 안전하고 자동적으로 제어하기 위한 문화 / 기술 / shared ownership
- DevOps 작동 방식
  - 개발팀과 운영팀이 더이상 각각의 부서에만 묶여있지 않음
  - 두 팀이 병합되어, 엔지니어가 개발, 테스트, 배포, 운영까지 전체 애플리케이션 수명주기에 걸쳐 작업하고 단일 기능에 한정되지 않은 광범위한 기술 개발
  - QA와 보안 팀도 애플리케이션 수명주기 전체에 걸쳐서 긴밀하게 통합
    - DevSecOps
  - 수동적 프로세스를 자동화해서 애플리케이션 수명 주기 가속화
  - 그리고 그것을 가능하게 하는 기술 스택과 도구 사용
- 장점
  - 속도
    - 시장의 니즈에 보다 빠르게 적응
    - 효율적인 비스니스 성과 창출
    - 빠른 업데이트 릴리즈
  - 빠른 CD
    - 릴리즈 빈도와 속도 개선으로 제품을 더 빠르게 혁신하고 향상 가능
    - CI / CD
      - 빌드에서 배포까지 소프트웨어 릴리스 프로세스를 자동화
  - 안정성
    - 애플리케이션 업데이트와 인프라 변경의 품질 보장
      - 최종 사용자에게 빠르고 안정적으로 긍정적인 경험 제공
    - CI / CD
    - Monitoring / Logging
      - 실시간 성능 정보 측정
  - 확장 가능
    - 규모에 따른 인프라와 개발 프로세스를 운영 및 관리
    - Infrastructure as Code를 사용하면, 개발, 테스트, 프로덕션 환경을 반복 가능하고 좀 더 효율적인 방식으로 관리 가능
  - 협업 강화
    - 주인 의식 / 책임
    - 개발자와 운영 팀이 긴밀하게 협력하고 책임을 공유하며, 워크 플로를 결합
      - 개발자와 운영 팀 간에 인도 기간 단축
      - 실행되는 환경을 고려한 코드 작성
  - 보안
    - 제어를 유지하고 보안 규정을 준수하면서 신속하게 진행 가능
    - Infrastructure as Code를 사용하면, 규모에 따라 보안 규정을 정의하고 추적 가능

## 세션1: 운영팀 없는 스타트업에서 개발자가 알아야 하는 서비스 운영지식

- 초기 / 중기 스타트업에서는 운영은 CTO / CEO에게 맡기고 서버개발자는 어플리케이션 로직에만 집중
  - 클라우드 활용하는 것이 좋음
- 데브옵스로 수익을 창출하는 것이 아님
  - 데브옵스는 규모가 커지면서 자연스럽게 발생하는 니즈임

## 세션2: DevOps의 인문학적 접근

- 오픈소스
  - eric raymond
    - 중앙 집중적 vs 비중앙 집중적 개발
- 깃
  - fully distributed 코드 관리 / 개발
- devops
  - 개발 뿐 아니라, 운영도 fully distributed하게 할 수 있는 문화 & 방법론 &
  - freedom & responsibility
- 가장 효과적으로 구사하고 있는 사례
  - netflix
- 노자의 도덕경과 비슷함

## 세션3: DevOps Art 1년부채부터 10년 부채까지

### Migration

- DevOps환경을 migration을 하는 이유
  - 기술 부채 탕감
  - 과거 추적이 불가능 하기 때문
    - 왜 어떻게 만들었는가?에 대답할 수 없는 경우
- migration의 준비를 위해서 고려할 것들
  - 사람
    - 리더, 인원
  - 프로세스
    - 비용
  - 팀 구성 / 서비스 성격
    - 조직 / 서비스의 성격
  - 도구
    - 트레이드 오프
    - 속도
    - 편의성
  - 일정
    - 변경가능성
    - 보고

### Devops란

- Culture
- Automation
  - 핵심
    - 모든 것은 코드로 기록을 남긴다
    - Infrastructure As Code
  - 종류
    - Account / Identity / Security
    - App / Language / Architecture
      - 인프라 정의는 모드 코드로
      - vpc정의도 전부 코드로
    - CI / CD
      - Jenkins도 코드로
    - Monitoring / Tools
      - SaaS전성시대
      - New relic, datadog, sumologic
- Measurement
  - 무엇인가를 했으면 무조건 기록을 남긴다
  - 기록을 잘해야 기술부채를 없앨 수 있음
- Sharing
  - 공부한 것을 언제나 쉐어
  - 끊임 없이 개선하는 것을 문화로
- File up / Pile up
  - 루이뷔똥의 사례
    - 예술가들의 모든 고민과 콜라보를 수동으로 기록
    - pile up
  - 데브옵스는 예술이다.
    - 예술은 단순히 영감의 산물이 아닌, 끊임없는 고민 노력 생각의 산물
    - 단순히 테크니션을 넘어서 예술의 영역으로 가자
      - 끊임 없는 기록
      - 공유

## 세션4: DevSecOps 를 접해보시렵니까?

### DevOps

- 가치 제공
- 마켓 니즈의 충족이 빠르고 스케일링 가능

### Doing DevOps

- technology
- methodology(culture)
- shared ownership
- 위의 3박자가 맞아떨어져야 함

### Doing DevSecOps

- 위의 3박자 각각에 대하여 어떻게 보안상 안전한 devOps를 구현할 것인가?
- technology
  - 새 기술에 맞는 보안 도구를 적용하자
- methodology(culture)
  - Devops 파이프라인에 자동화 되어서 보안 체크를 해야 함 / 흐름 제약하면 안됨
    - static analysis
      - 코드
    - dynamic analysis
      - 만들어진 앱
  - 대표적 도구
    - sonarlint
    - pre-commit hook
    - CI결합
      - FindSecutiyBugs
      - Bandit
      - NodeJsScan
      - Gosec
      - Phan
    - 의존성 체크
      - npm audit
      - owasp > sonar cube integration가능
      - jenkins plugin은 항상 조심!
    - 미국의 국방성도 파이프라인 보안 사용하고 있다!
- shared ownership
  - 팀 기반 decision making
  - 정보 공유
  - 빠르게 실패하고, 점진적으로 고쳐나가자
  - 변화를 제한하고 빨리빨리 개선하자
    - 작은 규모로 자주자주 디플로이
  - Dev + Ops는 개발자와 운영자의 융합
    - 망분리는 목표가 아니다!!
    - 수단이 목적이 되어서는 안된다
