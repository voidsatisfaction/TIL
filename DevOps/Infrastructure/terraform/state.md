# Terraform State

- 의문
- Purpose of Terraform State
  - 왜 테라폼은 state를 갖는가

## 의문

- *`terraform plan`에서 `-refresh=false`와 `refresh-only`의 차이는 무엇인가?*

## Purpose of Terraform State

- 개요
  - 테라폼은 state의 하나의 대상이 실제 하나의 인프라 오브젝트와 대응하도록 함

### 왜 테라폼은 state를 갖는가

- 실제 인프라 오브젝트와 매핑하기 위함
- 메타데이터
  - 리소스와 리모트 오브젝트의 매핑 뿐 아니라 리소스 디펜던시와 같은 메타데이터도 트래킹해야 함
    - 만약 state가 없으면, terraform 리소스가 삭제되었을 경우, 디펜던시 순서를 모르기때문에, 어떻게 지워야할지 모름
- 성능
  - 테라폼은 state에 모든 리소스의 attribute값의 캐시를 저장하며, 성능 향상에만 의도가 맞춰짐
    - `terraform plan`시에 actual state를 알기 위해서 provider에 모든 상태를 조회하면, 크기가 큰 인프라같은경우 너무 느려짐 & rate limit도 존재
    - 그래서 `-refresh=false`, `-target` 플래그를 사용해서 cached state를 record of truth로 삼음
- 싱크하기
  - 여러 팀원이 terraform을 동시에 동작시켜서 inconsistent한 state가 되지 않게 할 수 있음
