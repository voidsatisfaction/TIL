# EKS

- 의문
- 개요
- service account와 IAM role 연동

## 의문

- OIDC(Open ID Connect)
  - OAuth2.0 기반으로 유저를 인증하는 프로토콜로, OAuth2.0과의 차이점은 OAuth2.0은 authorization을 포함한다면, OIDC는 Authentication에 집중함

## 개요

## service account와 IAM role 연동

- 개요
  - service account object를 이용하여 pod level에서 IAM role을 부여할 수 있게 해주는 방법
- 방법
  - IRSA(IAM Roles for Service Account)
    - OIDC(OpenID Connect) identity provider와 k8s 서비스 어카운트 애노테이션을 이용해서, IAM role을 팟 레벨로 사용할 수 있게 함
  - 1 OIDC가 IAM role을 STS(Secure Token Service)를 사용해서 취득할 수 있게 함
    - JWT(STS)로 IAM role을 취득할 수 있게 함
      - *즉, STS로 IAM role을 취득할 수 있게 한다는것인가?*
  - 2 k8s에서는 *projected service account token*을 발급하여 팟에 유효한 OIDC JWT를 발급받을 수 있음
- 해석
  - 
