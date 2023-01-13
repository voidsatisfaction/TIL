# Jenkins

- 의문
- 용어
  - 동작의 주체
  - job관련
  - 파이프라인
  - 빌드의 상태
  - 그 외

## 의문

## 용어

### 동작의 주체

- Controller(master)
  - 중앙에서 조정하고, configuration을 저장하고, 플러그인을 로드하고, jenkins를 위한 다양한 유저 인터페이스를 제공하는 역할을 하는 프로세스
  - Core(`jenkins.war`)
    - 메인젠킨스 애플리케이션으로, 기본 웹 UI와 설정, 그리고 플러그인을 설치하는 기반을 제공함
- Agent
  - 젠킨스 컨트롤러에 연결되고, 컨트롤러에 의해서 지시받은 태스크를 실행하는 머신이자 컨테이너
  - Label로 agent를 그루핑 할 수 있음
    - e.g) linux는 linux-based agent, docker는 docker-capable agent
  - Executor
    - 하나의 노드에서 파이프라인 또는 잡에 의해서 정의된 일의 실행을 위한 슬롯
      - *정확한 의미는?*
    - 하나의 노드는 0이상의 executor를 갖고, 동시에 job이나 파이프라인을 실행하도록 설정됨
- Node
  - 파이프라인 또는 잡을 실행할 수 있는 젠킨스 환경을 구성하는 머신
    - Controller, Agent 둘다 노드로 간주됨

### job관련

- job(project)
  - 젠킨스가 실행해야하는 유저가 설정한 일의 상세이며, 예를들자면, 소프트웨어 빌드등이 있다
- pipeline
  - 유저가 정의한 CD의 파이프라인 모델
- build
  - 하나의 잡 실행의 결과
- artifact
  - 빌드나 파이프라인 실행 도중에 생성되는 불변파일이며, 컨트롤러에 저장되어서 나중에 유저가 참조 가능하게 함
- folder
  - 파이프라인 또는 잡의 조직적인 컨테이너(파일 시스템의 폴더와 유사)
- item
  - 웹 UI에서의 엔티티
    - 폴더, 파이프라인, 잡중 하나
- Publisher
  - 빌드의 일부로, 구성된 모든 단계가 완료된 후 보고서를 게시하고 알림을 보내는 것
  - 역할
    - Stable or Unstable result를 프로세싱과 설정에 따라서 리포트함
    - e.g) JUnit publisher는 JUnit 테스트가 실패하면 빌드 결과를 Unstable하다고 할 수 있음
- Trigger
  - Pipeline 혹은 job의 실행을 트리거링하는 기준
- Upstream
  - 설정된 Pipeline 혹은 job으로, 실행의 중간에 다른 Pipeline이나 job을 트리거링함

### 파이프라인

- Stage
  - 파이프라인의 부분으로, 전체 파이프라인의 개념적인 부분을 정의할때 사용함
    - e.g) `Build`, `Test`, `Deploy`
- Step
  - 하나의 작은 태스크이며, 젠킨스에게 무엇을 해야하는지 Pipeline 혹은 job 안에서 정의됨

### 빌드의 상태

- aborted
  - 빌드가 예상되는 결과(실패)가 되기전에 중지됨
    - e.g) 유저가 수동으로 멈추거나, 타임아웃이 존재했을 경우
- failed
  - 빌드가 치명적인 에러가 존재함
- stable
  - 빌드가 successful & 퍼블리셔가 unstable하다고 하지 않음
- successful
  - 빌드가 컴파일 에러 없이 성공적이었음
- unstable
  - 빌드가 에러가 있었으나, 치명적이지 않은 경우

### 그 외

- Plugin
  - 젠킨스 코어와 별개로 제공되는 젠킨스 확장 기능
- View
  - 대시보드 스타일로 젠킨스에서 데이터를 나타내는 방식
- Workspace
  - 파이프라인이나 잡을 시행할 수 있는 노드에서의 처분 가능한 파일시스템의 디렉터리
  - 일반적으로는 특정한 cleanup 정책이 없다면 Build, Pipeline 이후에 그대로 두어짐
    - 젠킨스 컨트롤러에서 cleanup 정책을 설정 가능
