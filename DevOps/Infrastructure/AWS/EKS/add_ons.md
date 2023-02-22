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

- 개요
  - kubernetes의 ingress 오브젝트를 nginx에 프로비저닝 해주는 컨트롤러

## 5. cluster-autoscaler

- 참고
  - https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md#cluster-autoscaler-on-aws
- 개요
  - 클러스터의 워커 노드의 auto scaling해주는 애드온
    - c.f) karpenter라는 친구가 새로 있긴 함
- 주의
  - Auto Scaling Group의 tag에 taint 등의 값을 지정해줘야 함
    - e.g)
      - `k8s.io/cluster-autoscaler/node-template/taint/dedicated:	jenkins:NoSchedule`
      - `k8s.io/cluster-autoscaler/node-template/label/jenkins:	true`
    - terraform에서는 `aws_autoscaling_group_tag`를 사용하면 가능(`tags_all`아님!)

## 6. google-auth-server(custom OAuth2 proxy server)
