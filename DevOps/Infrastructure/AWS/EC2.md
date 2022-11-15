# AWS EC2

- 의문
- 개요
  - EC2 설정
  - EC2 타입
  - Security Groups

## 의문

## 개요

- 개요
  - EC2 = Elastic Compute Cloud = Infrastructure As A Service
- 기능
  - EC2(가상 머신 대여)
  - EBS(가상 드라이브에 데이터 저장)
  - ELB(호스트 사이에 부하 분배)
  - ASG(오토 스케일링 그룹)

### EC2 설정

- OS
  - Linux, Windows, MacOS
- CPU
- RAM
- Storage space
  - EBS / EFS
  - *하드웨어*
- NIC
  - 네트워크 카드 속도
  - 파블릭 IP주소 등
- Firewall
  - security group
- EC2 User Data
  - 부트스트랩 스크립트(첫 런칭에 실행될 스크립트)

### EC2 타입

- m-family
  - 범용
    - compute
    - memory
    - networking
    - 밸런스 중시
- c-family
  - CPU 집중
    - 배치 프로세싱
    - 미디어 트랜스코딩
    - 높은 성능의 웹서버
    - 높은 성능의 컴퓨팅
    - ML
    - 게임 서버
- r-family
  - 메모리 집중
    - 높은 성능의 DB
    - 분산 웹 캐시 스토어(elastic cache)
    - 큰 규모의 실시간 데이터 프로세싱
- i,d,h1-family family
  - 스토리지 집중
    - 매우 잦은 빈도로 동작하는 OLTP(Onlint Transaction Processing)시스템
    - 관계형 & NoSQL 데이터베이스
    - 인메모리 데이터베이스
    - 데이터 웨어하우스 애플리케이션
    - 분산 파일 시스템
- t-family
  - 버스트 가능
- e.g)
  - m5.2xlarge
    - m
      - 인스턴스 클래스
    - 5
      - generation
    - 2xlarge
      - 인스턴스 클래스에서의 사이즈

### Security Groups(Firewall)

![](./images/ec2/security_group_good_to_know1.png)

- 개요
  - EC2 인스턴스들로부터 바깥으로, 혹은 안으로 들어오는 트래픽을 제어
- 특징
  - 오직 allow룰만 포함
  - security group 룰은 IP나 security group로 참조가능
- 규제 방식(**Transport layer**)
  - ports, ip ranges, inbound network, outbound network
