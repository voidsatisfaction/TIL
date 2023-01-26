# ELB

- 의문
- 개요

## 의문

## 개요

- 왜 로드밸런서를 사용해야 하는가?
  - 애플리케이션의 접근의 하나의 포인트를 노출하기 위함
  - 부하를 여러개의 downstream 인스턴스로 분산시키기 위함
  - 인스턴스의 healthcheck를 하기 위함
  - downstream 인스턴스들의 실패를 심리스하게 다루기 위함
  - 높은 availability를 제공하기 위함
  - 웹 애플리케이션 통신에 TLS를 제공하기 위함
  - 쿠키의 stickiness를 위함
- ELB 쓰는 이유
  - managed LB이다
    - AWS가 동작하는 것을 보증
    - AWS가 업그레이드, 유지보수, 높은 availability를 관리
    - AWS가 아주 약간의 설정 knob만 제공
  - 다양한 AWS 서비스들과 연동 가능
    - EC2, EC2 오토 스케일링 그룹, ECS
    - AWS Certificate Manager
    - CloudWatch
    - Route53, AWS WAF, AWS Global Accelerator
- ELB 타입
  - Classic LB(CLB)
    - HTTP, HTTPS, TCP, SSL
  - Application LB(ALB)
    - HTTP, HTTPS, WebSocket
  - Network LB(NLB)
    - TCP, TLS, UDP
  - GateWay LB(GWLB)
    - IP
- LB Security Groups
  - HTTP TCP 80 0.0.0.0/0 Allow HTTP
  - HTTPS TCP 443 0.0.0.0/0 Allow HTTPS
