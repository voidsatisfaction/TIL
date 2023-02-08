# Atlantis

- 의문
- 개요

## 의문

## 개요

- 개요
  - `terraform plan`과 `apply`를 원격에서 실행하고, PR에 output을 커멘트로 남기는 애플리케이션
    - Terraform PR 이벤트를 webhook을 통해서 listen하고 실행하고 실행결과를 PR코멘트로 작성하는 애플리케이션
- 장점
  - terraform 변화를 팀 전체에 공유
  - 비운영 엔지니어도 terraform을 사용할 수 있도록 함
  - terraform 워크플로우의 표준화
    - credential없이도 terraform PR을 제출할 수 있도록 함

## 실전 예시

### atlantis를 사용해서 여러 어카운트의 terraform인프라 관리하기

오늘은 회사 서비스의 terraform의 iam모듈의 리팩토링을 하면서, atlantis pod이 어떤식으로 k8s 클러스터 및 aws와 상호작용하는지 파악할 수 있었습니다.

일단 atlantis도 helm chart를 이용해서 k8s내에 릴리스 됩니다.

그런데 여기에서 IRSA를 이용해서 IAM role을 부여받습니다. 따라서, atlantis role에는 eks IRSA 세팅을 해주고(OIDC policy적용) service account에 토큰을 주입해서 사용하면 문제가 없습니다.

그런데, 다른 계정의 자원에도 접근해야 하는 경우가 있습니다.

그럴때에는 다른 계정의 IAM role에(모든 자원에 접근 가능한 policy가 적용됨) 기존 계정의 IAM role이 assume가능하게 해두고, terraform을 init하거나 plan시, iam role을 assume하게 해주면 됩니다.

이미 pod은 기존 iam role을 assume하고 있고, 그 role은 다른 계정의 role을 assume할 수 있으므로, 다른 계정의 자원도 atlantis로 관리가 가능합니다.
