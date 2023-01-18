# Terraform State

- 의문
- Purpose of Terraform State
  - 왜 테라폼은 state를 갖는가

## 의문

- *`terraform plan`에서 `-refresh=false`와 `refresh-only`의 차이는 무엇인가?*

## 개요

- 개요
  - 실제 인프라 리소스를 테라폼 설정과 매핑해주는 역할
    - 메타데이터를 트래킹(디펜던시 의존 관계)
    - 성능 향상
- 특징
  - remote 스토어에서 관리하는게 좋음
    - 팀 프로젝트의 경우
- 커맨드
  - `refresh`
    - state를 실제 아키텍처와 싱크하는 커맨드
  - `state`
    - state를 CLI를 통해서 수정하는 커맨드
    - `terraform state rm`
      - terraform state에서 실제 인프라 리소스에 관련된 정보를 지워버리는 것
  - `import`
    - 외부로부터 생성된 오브젝트를 테라폼형상으로 가져오는 것(state file)

## Purpose of Terraform State

- 개요
  - 테라폼은 state의 하나의 대상이 실제 하나의 인프라 오브젝트와 대응하도록 함

### 왜 테라폼은 state를 갖는가

- 실제 인프라 오브젝트와 매핑하기 위함
  - state와 같은 DB가 없으면, id같은 것으로 인프라와 코드사이의 매핑이 어려움
    - id는 실제 인프라가 생성되고나서 생성되므로
  - tag를 활용할 수도 있으나, 일부 provider는 태그를 제공하지 않는 경우도 있음
- 메타데이터
  - 리소스와 리모트 오브젝트의 매핑 뿐 아니라 리소스 디펜던시와 같은 메타데이터도 트래킹해야 함
    - 만약 state가 없으면, terraform 리소스가 삭제되었을 경우, 디펜던시 순서를 모르기때문에, 어떻게 지워야할지 모름
- 성능
  - 테라폼은 state에 모든 리소스의 attribute값의 캐시를 저장하며, 성능 향상에만 의도가 맞춰짐
    - `terraform plan`시에 actual state를 알기 위해서 provider에 모든 상태를 조회하면, 크기가 큰 인프라같은경우 너무 느려짐 & rate limit도 존재
    - 그래서 `-refresh=false`, `-target` 플래그를 사용해서 cached state를 record of truth로 삼음
- 싱크하기
  - 여러 팀원이 terraform을 동시에 동작시켜서 inconsistent한 state가 되지 않게 할 수 있음

## The terraform_remote_state Data Source

- 개요
  - `terraform_remote_state` 데이터 소스는 지정된 state backend로부터 다른 테라폼 설정의 root 모듈의 output value를 가져오기 위해서 최신 state snapshot을 사용함
- 특징
  - output value만 노출하더라도, 유저는 모든 state snapshot을 접근해야 하고, 민감한 정보를 포함할 수도 있음
