# EKS addons

- 의문
- 개요

## 의문

## 개요

- EKS자체에서 자주 사용하는 애드온들
- 종류
  - VPC CNI
  - external-secrets
  - alb controller
  - nginx ingress controller
  - cluster-autoscaler
  - google-auth-server(custom OAuth2 proxy server)

## 1. VPC CNI

## 2. external-secrets

## 3. alb controller

ALB controller의 디자인

![](./images/add_ons/alb-design1.png)

- 개요
  - kubernetes의 ingress(service) 오브젝트를 ALB(NLB)에 프로비저닝 해주는 컨트롤러
    - 당연히 IRSA가 필요함

## 4. nginx ingress controller

## 5. cluster-autoscaler

## 6. google-auth-server(custom OAuth2 proxy server)
