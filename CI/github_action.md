# Github action

- 의문
- Core concept

## 의문

## Core concept

Workflow > Job > Action(portable) > Step

### Workflow

- 개요
  - 리포지토리에서 build, test, package, release, deploy할 수 있도록, 설정가능한 자동 프로세스
  - 하나 이상의 job들로 구성되어, event에 의해서 스케쥴링 되거나 활성화됨

### Job

- 개요
  - **같은 runner에서 실행되는 step들의 집합**
    - 하나 이상의 step으로 정의되어짐
  - 한 workflow file에서 어떻게 job이 실행되어져야 하는지 dependency rule을 정의할 수 있음
- 특징
  - parallel하게 혹은 순차적으로 실행할 수 있음(이전 job의 상태에 따라서)
    - 예를들어, 한 workflow가 build, test job을 가지고, test job은 build job의 status에 의존한다고 하면, 만일, build job이 실패했을 경우, test job은 실행되지 않음
    - 각 job은 가상환경의 fresh instance에서 실행됨

### Action

- 개요
  - 하나의 job을 만들기 위해서 step이라고 불리는 개별적인 태스크를 결합한것
- 특징
  - workflow의 가장 작은 portable한 블록
  - Gihhub community에서 공유된 것이나, custom action을 사용할 수 있음
  - workflow안에서 한 action을 사용하기 위해서는, 이것을 step으로 넣어줘야 함

### Step

- 개요
  - command를 실행하거나 action을 실행할 수 있는 개개의 task
- 특징
  - job에 들어있는 각 step은 같은 runner에서 실행됨
  - job의 action들이 file system을 통하여 information을 공유할 수 있도록 함

### Artifact

- 개요
  - 빌드 하거나 코드를 테스할 때 생성된 파일들
    - 바이너리 / 패키지 파일들, 테스트 결과, 스크린샷, 로그 파일들 등
- 특징
  - 다른 job에 사용되거나, deploy 될 수 있음

### Event

- 개요
  - workflow를 동작하게 하는 특별한 활동
  - 예시
    - 누군가가 리포지토리에 푸시했을 경우 혹은 push / pull request가 만들어졌을 경우 등
- 특징
  - repository dispatch webhook을 이용하여, 외부 이벤트가 일어났을 떄, 특정 workflow가 동작하도록 설정할 수 있음

### Runner

- 개요
  - GitHub Actions runner application이 설치된 임의의 machine
- 특징
  - gitHub or 자기자신의 runner를 사용할 수 있음
  - runner는 실행할 수 있는 job을 기다림
- 종류
  - Github-hosted runner
  - Self-hosted runner

#### Github-hosted runner

- 개요
  - Linux / Windows / macOS runner를 갖고 있음(job runner)
  - virtual machine을 사용. 하드웨어 구성을 바꿀 수는 없다
    - 해당 machine의 환경을 virtual environment라고 함

#### Self-hosted runner

- 개요
  - runner application이 설치된 사용자가 관리하고 유지하는 machine
- 특징
  - 하드웨어 설정 / os설정 등이 가능

### CI

- 개요
  - 작은 코드 변화를 repository에 자주 커밋하는 소프트웨어 개발 practice
- 특징
  - github action에서는 custom CI workflow를 만들 수 있음

### CD

- 개요
  - 새 commit이 CI 테스트를 통과하면, 코드가 자동적으로 production 환경으로 deploy되는 것
