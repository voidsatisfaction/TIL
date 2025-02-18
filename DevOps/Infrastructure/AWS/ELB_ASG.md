# ELB

- 의문
- 개요
- ELB
  - ELB 컴포넌트 아키텍처
- ELB 타입: ALB(Application) vs NLB(Network) vs GLB(Gateway)
  - ALB
  - NLB
  - GLB
- ELB의 기능
  - Sticky Sessions(Session Affinity)
- ASG

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

## ELB

- 개요
  - incoming 트래픽을 다양한 타겟(EC2 인스턴스, 컨테이너, IP주소, 람다 함수)으로 분배
  - 등록된 타겟들의 헬스체크도 진행해서 오직 건강한 타겟으로만 트래픽 보냄
- 특징
  - internet facing 로드밸런서의 경우, IPv4 주소가 부여되고, 내부 로드 밸런서의 경우 서브넷 IPv4주소 부여

### ELB 컴포넌트 아키텍처

ELB 컴포넌트 아키텍처

![](./images/LB/elb_components_architecture1.png)

- 리스너
  - 개요
    - 클라이언트의 커넥션 리퀘스트를 프로토콜 / 포트를 기반으로 체크(설정값과 대조)
    - 인바운드 커넥션이 어떻게(어디로) 라우팅되어야 하는지 정의
    - 각 로드 밸런서는 적어도 하나의 리스너를 가져야 함
  - 룰
    - 로드 밸런서가 등록된 타겟으로 리퀘스트를 어떻게 라우팅해야하는지 정의
    - 우선순위 존재
    - default룰이 존재하고, 선택적으로 추가 룰을 정의함
- 타겟 그룹
  - 개요
    - ELB가 리퀘스트를 라우팅하는 리소스 그룹
    - 서로 다른 타겟 그룹에 각각 다른 리스너 설정과 룰로 연결시킬 수 있음
    - 하나의 타겟을 다수의 타겟 그룹으로 등록할 수 있음
  - 헬스 체크
    - 로드 밸런서가 주기적으로 타겟 그룹으로 다음을 행하게 할 수 있음
      - 핑 보내기
      - 커넥션 시도하기
      - 테스트 리퀘스트 보내기

## ELB 타입: ALB(Application) vs NLB(Network) vs GLB(Gateway)

### ALB

- 개요
  - 애플리케이션 레이어에서의 다양한 변수에 대해서 트래픽 분배
- 특징
  - Application레이어의 HTTP, HTTPS 리스너에만 적용됨
    - HTTP/2와 웹 소켓도 적용 가능
  - 변동 IP
  - contextful
    - 트래픽 내용(HTTP의 헤더, 바디 등)까지도 라우팅하는데 사용할 수 있음
  - availability판단시, HTTP요청이 성공적으로 반환되는것 뿐 아니라, 특정 파라미터에 대해서 내용이 예상한대로 잘 반환되는지도 판단근거로 삼음
  - 타겟 그룹에 대해서 로드 밸런싱을 행함
  - 같은 머신에 대해서 다양한 앱으로 로드밸런싱도 가능
    - 마이크로 서비스나 컨테이너 기반 애플리케이션에 잘 어울림(Docker, Amazon ECS)
  - 호스트네임이 고정됨
    - e.g) `XXX.region.elb.amazon.com`
  - 애플리케이션 서버는 클라이언트의 IP를 직접 보지 못함
    - `X-Forwarded-For`
      - 클라이언트의 IP주소
    - `X-Forwarded-Port`
      - 클라이언트의 포트
    - `X-Forwarded-Proto`
      - 클라이언트의 프로토콜
- 라우팅 방식
  - Listener내부의 Rule을 사용하여 설정
    - URL path
      - `example.com/users`, `example.com/posts`
    - URL hostname
      - `one.example.com`, `other.example.com`
    - Query String, Headers
      - `example.com/users?id=123&order=false`
- 타겟 그룹
  - EC2 인스턴스들(오토스케일링 그룹) - HTTP
  - ECS 태스크 - HTTP
  - 람다 함수 - HTTP 리퀘스트가 JSON 이벤트로 번역됨
  - IP 주소들 - private ips

### NLB

- 개요
  - TCP & UDP 트래픽을 IP주소와 포트 기준으로 트래픽을 분배(network layer)하는 로드 밸런서
- 특징
  - 매초당 수백만의 리퀘스트 핸들링 가능
  - 레이턴시가 ~100ms (ALB는 ~400ms)
  - 각 AZ마다 하나의 고정 IP를 갖고 있음
  - context-less
    - 트래픽 내용이 아닌, 오직 ip와 포트만으로 라우팅
  - availability판단시, 서버와의 ICMP핑 혹은 TCP핸드셰이크가 되는것까지만 판단
    - 따라서, 완전한 availability는 모름
- 타겟 그룹
  - EC2 인스턴스
  - IP 주소들
    - private IPs
  - ALB
  - 헬스체크는 TCP, HTTP, HTTPS

### GLB(Gateway Load Balancer)

- 개요
  - AWS에서의 서드파티의 플릿을 매니지하고 배포하고 스케일할 수 있는 LB
- 특징
  - 네트워크 레이어에서 동작(IP 패킷)
  - 투명한 네트워크 게이트웨이(single entry/exit for all traffic)
    - 다른 애플리케이션은 해당 게이트웨이를 몰라도 됨(투명함 = 알아서 처리함)
  - 타겟 그룹으로 부하를 분배
  - 6081포트의 `GENEVE` 프로토콜을 사용
- 타겟 그룹
  - EC2 인스턴스
  - IP 주소들
    - private IPs
- 예시
  - 네트워크 레이어의 방화벽, 침입감지 / 방지 시스템, 패킷 조사 시스템, payload 변조, ...

## ELB의 기능

- Sticky Sessions(Session Affinity)

### Sticky Sessions(Session Affinity)

- 개요
  - ALB에서 같은 클라이언트를 항상 동일한 인스턴스로 트래픽을 가게 할 수 있음
    - 쿠키 사용
    - 로드 밸런싱이 잘 안될 수 있음
- 사용되는 쿠키
  - Application-based Cookies
    - Custom cookie
      - target에 의해서 생성됨
      - 어떤 데이터도 포함 가능
    - Application cookie
      - ALB에 의해서 생성됨
      - `AWSALBAPP`이라는 쿠키명
  - Duration-based Cookies
    - ALB에 의해서 생성된 쿠키
    - `AWSALB`라는 쿠키명을 갖고 있음

## ASG

![](./images/elb_asg/auto_scaling_group1.png)

- 속성
  - launch template
    - AMI + instance type
    - EC2 User Data
    - EBS Volumes
    - Security Groups
    - SSH Key Pair
    - IAM Roles for EC2 Instances
    - Network + Subnets Information
    - Load Balancer Information
  - size
    - min / max / initial
  - scaling policies
- 오토스케일링
  - Cloud watch alarm
    - CPU, Memory 등의 메트릭으로 오토 스케일링 가능

### Scaling policy

- 개요
  - Target Tracking Scaling
    - e.g) 평균 ASG CPU를 40% 정도로 유지하고 싶다
  - Simple / Step Scaling
    - 클라우드 워치 알람을 설정하고, 각 단계마다 얼마나 추가할지 설정
      - e.g) CPU > 70% 알람이 울리면 2인스턴스 추가하기
  - Scheduled Actions
    - e.g) min capacity를 금요일 5시 오후에 10으로 두기
  - Predictive Scaling
    - ML을 사용해서 AWS에서 제공되는 예측 오토 스케일링
- 메트릭
  - CPU Utilization
    - AVG CPU 사용량
  - Memory Utilization
  - RPS(Request Per Second)
  - Average Network In / Out
- Scaling 쿨다운
  - 오토스케일링이 일어나면 기본 300초 동안은 cooldown period로, ASG는 새로 인스턴스를 만들거나 없애지 않음
    - 당분간은 오토 스케일링 효과를 관찰하는 기간을 갖음
