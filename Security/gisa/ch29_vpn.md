# 29. VPN

- 의문
- 29.1 VPN
- 29.2 IPSec

## 의문

## 29.1 VPN(Virtual Private Network)

### 29.1.1 개요

- 등장배경
  - 인터넷을 기반으로 한 기업 업무 환경의 변화에 기인(본사와 다수의 지사)
  - 사설망은 비용을 포함한 한계를 가짐
  - public network는 보안에 취약
- VPN의 정의
  - public network를 이용하여, private network가 요구하는 서비스를 제공할 수 있도록 네트워크를 구성한 것
    - 가상 사설 네트워크(Virtual Private Network)
      - Virtual
        - 공중망을 이용하여 필요시에만 전용선과 같이 사용할 수 있다는 것을 의미
      - Private
        - 사용자의 데이터 혹은 호스트에 대해 타인이 접근하지 못함을 의미
      - Network
        - 지역적, 기능적 분산 네트워크의 통합
    - 주소 및 라우터 체계의 비공개
    - 데이터 암호화
    - 사용자 인증
    - 사용자 엑세스 권한 제한
- VPN 구현 기술
  - **터널링**
    - 인터넷 같은 안전하지 못한 네트워크 환경에서, 전용선과 같은 강력한 보안을 제공하는 것으로, IP 패킷이 공중망을 통과할 때, 사용자 간에 마치 터널이 뚫린 것처럼 통로를 마련하여 이 통로를 통해 데이터를 안전하게 전송
  - **암호화 및 인증**
    - 정보의 Credentiality
      - 대칭키 암호를 사용
      - 대칭키는 공개키 암호방식을 통하여 키 교환을 통해 공유됨
    - 정보의 Integrity
      - MAC또는 HMAC를 이용하여 확인
    - Authentication
      - 공유키, 공개키, 인증서, 전자서명 등을 활용
  - **Access Control**
    - 인증된 사용자에게만 접근을 허용

### 29.1.2 VPN의 분류

- 구성 형태에 따른 분류
  - Intranet VPN
    - 기업 내부를 LAN을 통해 연결하는데 사용하여, 넓게는 자사까지 연결. 가장 단순한 형태
  - Extranet VPN
    - 자사와 밀접한 관계가 있는 고객사나 협력업체에게 Intranet을 이용할 수 있도록 Intranet을 확장한 개념
    - 업무처리의 원활한 데이터 교환을 목적
  - Remote Access VPN
    - 재택근무자나 원격접속자는 ISP의 NAS(Network Access Server)에 접속
    - NAS는 사용자 접속 인증과 터널링에 관련된 기능을 수행
      - ISP가 제공하는 NAS에는 VPN 제공을 위한 기능이 추가되어야 함
    - Remote Access VPN에서 가장 중요한 요소는 보안

### 29.1.3 VPN의 구성

- 터널링
  - 송신자와 수신자 사이의 전송로에 외부로부터의 침입을 막기 위해 일종의 파이프를 구성하는 것
    - 파이프는 터널링을 지원하는 프로토콜을 사용하여 구현
  - payload
    - 터널링 되는 데이터
  - 터널링을 지원하는 프로토콜
    - 2계층 프로토콜
      - PPTP(Point-to-Point Tunneling Protocol)
      - L2TP(Layer 2 Tunneling Protocol)
      - L2FP(Layer 2 Forwarding Protocol)
    - 3계층 프로토콜
      - IPSec
    - 2,3계층 모두 지원 프로토콜
      - MPLS
- 2계층 터널링 프로토콜
  - **PPTP(Point-to-Point Tunneling Protocol)**
    - 개요
      - IP 페이로드를 암호화하고, IP헤더로 캡슐화하여 전송
      - 터널의 유지 보수 관리를 위해 TCP 연결을 사용하고, 모바일 유저가 서버에 접속하기 용이하게 되어있음
      - PPP(Point-to-Point Protocol)에 기초하여 두 대의 컴퓨터가 직렬 인터페이스를 이용하여 통신할 때 사용
        - 전화선을 통해 서버에 연결하는 PC에서 자주 사용되었음
  - **L2F(Layer 2 Forwarding Protocol)**
    - 개요
      - 시스코에서 제안된 프로토콜
      - NAS 개시 VPN형이기 때문에, 사용자는 별도의 S/W가 필요 없음
- 3계층 터널링 프로토콜
  - **IPSec**
    - 개요
      - IP망에서 안전하게 정보를 전송하는 표준화된 3계층 터널링 프로토콜. IP계층의 보안을 위해 IETF에 의해 제안되었으며, VPN 구현에 널리 쓰이고 있음
      - AH(Authentication Header)와 ESP(Encapsulation Security Payload)를 통해 IP 데이터그램의 인증과 무결성, 기밀성을 제공
    - 모드
      - 전송모드
        - IP 페이로드를 암호화하여 IP헤더로 캡슐화
      - 터널모드
        - IP패킷을 모두 암호화하여 전송
          - 새로운 IP헤더를 붙여줌
        - 라우터와 라우터 사이만 암호화 됨
    - IPSec의 헤더
      - AH
        - 데이터와 순서번호 보유, 송신자를 확인하고 메시지가 송신되는 동안 수정되지 않았음을 보장하는 헤더로, 암호화 기능 없음
      - ESP
        - IP 페이로드를 암호화하여 데이터 Confidentiality를 제공하므로, 제3자에 의해 데이터 노출 차단
- **SSL VPN**
  - 특징
    - 일반 사용자가 쉽게 사용할 수 있는 보안 프로토콜
    - IPSec VPN에 비해 설치 및 관리가 편리하고 비용 절감 가능
    - 클라이언트와 서버 사이의 안전한 통신 채널 관리 담당
    - 데이터 암호화와 인증을 통해 송수신 경로의 안전성 보장
    - PKI의 공개키/개인키를 이용한 웹사이트 통신 보안 가능
- **인증**
  - 데이터 인증
    - MAC, HMAC등을 이용하여 무결성 만족 가능
  - 사용자 인증
    - 방식
      - Peer-Peer
        - PAP(Password Authentication Protocol)
          - PPP연결시 사용되는 인증 포로토콜
          - 연결을 원하는 호스트는 사용자 계정과 패스워드를 목적지 호스트로 보내고, 목적지 시스템은 요청 컴퓨터를 인증한 후 연결을 허용하는 두 단계 핸드셰이킹으로 구성
        - CHAP(Challenge Handshake Authentication Protocol)
          - PPP 연결 인증 과정의 보안을 위해 보안요소를 강화시킴
          - 3단계 핸드셰이킹과 해시
      - Client/Server
        - TACACS(Terminal Access Controller Access-Control System)
          - 인증에 필요한 사용자 ID, 암호, PINs 및 암호키 정보를 인증서버에서 데이터베이스 형태로 관리하며 클라이언트로부터의 인증 요청을 처리함

### 29.1.4 MPLS VPN

*정확히 이게 뭔지 잘 모르겠다*

- MPLS 기본 개념
  - 시스코사의 태그 스위칭과 IBM의 ARIS(Aggregate Route based IP Switching)를 결합해 IETF에서 정한 표준
  - 유입되는 패킷을 진입부분에서 3계층 주소를 이용해서 해당 라우터가 갖고 있는 레이블 정보와 비교하여 부가적인 MPLS 레이블 정보를 덧붙임
  - 현재 부여 받은 레이블이 다음 라우터에서 새로운 레이블로 변경되는 작업을 레이블 스와핑이라 함
- MPLS VPN
  - 개요
    - MPLS 통신 네트워크를 이용하여 VPN을 제공하는 서비스로 여타 VPN 구조에 비하여 서비스 도입과 운영관리가 간단하고 편리하며, 저가의 VPN 서비스 제공이 가능
    - MPLS VPN의 특징은 다음과 같음
      - 기존 인터넷에 그대로 적용가능
      - 2계층의 스위칭 속도와 3계층의 라우팅 기능을 접목
      - 짧고 고정된 길이(4byte)의 레이블을 이용하여 스위칭
      - packet forwarding은 레이블 스와핑으로 수행
      - 패킷 지연 시간 감소
      - 레이블 부여는 LER(Label Edge Router)에서만 수행
      - 네트워크 내의 라우터와 스위치의 부담을 덜어줌
      - 여러 가지 다양한 서비스 제공 가능
        - QoS, VoIP, TE 등

## 29.2 IPSec(IP Security Protocol)
