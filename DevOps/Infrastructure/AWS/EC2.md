# AWS EC2

- 의문
- 개요
  - EC2 설정
  - EC2 타입
  - Security Groups
  - EC2 비용 설정
  - Elastic IP

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

### EC2 비용 설정

- On-demand
  - 필요할때 잠깐 인스턴스를 쓰고 shutdown하는 방식
- Savings Plan
  - 오래 지속해서 인스턴스를 사용할떄, 시간당 과금양을 미리 정해두고 인스턴스를 사용하는 방식
    - 같은 region의 같은 EC2 타입에 적용
- Reserved Instance
  - 미리 인스턴스의 개수를 예약해두고 사용하는 방식
    - 같은 region의 같은 EC2 타입에 적용
- Spot Instance
  - 실시간 경매에 참여하여 인스턴스를 사용하는 방식
    - 자신이 설정한 비용보다 비싸지면 2분의 termination time을 주고 shutdown됨
    - 가장 큰 비용 절감 가능
- c.f) Dedicated host
  - 물리 서버 독점 전용 가능
    - MS및 Oracle과 같은 공급업체의 소프트웨어 라이선스가 있을떄 활용 가능
    - 소켓 및 물리적 코어의 가시성 확보
    - 여러개의 instance(VM 인스턴스)를 사용가능
- c.f) Dedicated instance
  - Dedicated host위에서 물리 서버의 VM instance를 전용 사용 가능

### Elastic IP

- public IP
  - instance가 stop이후 다시 start될 때마다 계속해서 변화함
- elastic IP
  - 일정한 IP
  - 계정당 5개만 부여
    - AWS에 요청하면 늘릴 수 있음
  - 사용하지 않는 것이 좋음
    - **대신, DNS이름을 random public IP와 연동하는게 좋다**
