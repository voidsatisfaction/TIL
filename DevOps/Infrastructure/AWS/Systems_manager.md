# AWS Systems Manager

## 의문

## 개요

AWS Systems manager 프로세스 흐름

![](./images/systems_manager/ssm_process1.png)

- 개요
  - AWS 클라우드에서 실행되는 애플리케이션 및 인프라를 관리하는 데 도움이 되는 기능 모음
- 위의 그림
  - 3
    - Systems manager가 IAM 유저, 그룹 또는 역할에 지정한 작업을 수행할 권한이 있는지 체크
    - 작업 대상이 관리형 노드인 경우, Systems(SSM) Agent가 작업을 수행
  - 4
    - 상태의 보고
  - 5
    - SSM의 운영 관리 기능(Explorer, OpsCenter), Incident Manager는 리소스의 이벤트나 오류에 대응하여 운영 데이터를 집계하거나 아티팩트를 생성
- SSM 기능
  - 애플리케이션 관리
    - 파라미터 스토어
  - 변경 관리
  - 노드 관리
    - session management
  - 운영 관리
    - cloudwatch dashboard
  - Quick Setup
  - 공유 리소스
    - documents
      - SSM가 수행하는 작업의 정의

### SSM 
