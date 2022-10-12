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
