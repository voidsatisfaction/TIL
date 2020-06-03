# Network 관련 정의

- 네트워크
  - computer network
  - internet
  - intranet
  - ethernet
  - host
  - router
  - gateway
  - bridge
  - intranet
  - network bandwidth
- Application Layer
  - LDAP

## 네트워크

### Computer Network

- 정의
  - **네트워크 노드(머신)에 의해서 제공되는 혹은 네트워크 노드에 위치한 자원을 공유하는 목적을 달성하기 위해서, 디지털 상호 연결 위에서 공통의 커뮤니케이션 프로토콜의 집합을 사용하는 컴퓨터들의 그룹**
- 특징
  - 노드들 사이의 상호 연결은 다양한 telecommunication network 기술을 사용하여 형성됨
    - 물리적, 광학 와이어, 와이어리스, 라디오 주파수 방식 등
  - 각 노드는들은 hostname과 network address로 구별됨
    - IP 프로토콜을 이용한 노드의 locating / identification 가능
- 역사적 배경
  - 과거 IBM 호스트 장비가 엄청 비쌌는데, 그래서 '터미널'이라 불리는 지금 쓰는 단말기와 비슷하게 생긴 장비들 여러 대를 호스트 컴퓨터에 붙여서 사용하고
  - 프린터를 공유하고 사용하고
  - 여러 호스트를 공유해서 사용

### Internet

- 정의
- 특징
  - 하나의 프로토콜만 사용(IP)

### intranet

- 정의
  - 외부의 접근을 배제한 한 조직내의 컴퓨터 네트워크
- 구성
  - LAN, WAN 등의 기술을 이용

### Ethernet

- 정의
  - 컴퓨터 네트워킹 기술중 하나(LAN, MAN, WAN)
- 특징
  - CSMA/CD(Carrier Sense Multiple Access / Collision Detection) 프로토콜 사용해서 통신
    - CS(Carrier Sense)
      - 현재 네트워크 자원이 사용되고 있는지(누군가가 통신을 하고 있는지) 감지
    - MA(Multiple Access)
      - 다수의 노드가 동시에 네트워크상에 데이터를 실어 보내는 경우
    - CD(Collision Detection)
      - 데이터를 실어 보낸 노드가 네트워크 상의 동시 전송에 의한 충돌을 감지하는 것
      - 충돌이 감지되면 임의의 짧은 시간 이후에 전송될때까지 계속해서 재전송
  - 상대적으로 높은 bit rates
    - 일정 시간에 많은 비트를 통신 가능
  - 더 많은 노드 수용 가능
  - 보다 긴 link 거리
- 통신 방법
  - 데이터 링크 레이어에서 동작
  - 데이터 스트림을 frame이라는 더 작은 조각으로 나눔
  - 각 frame은 source, destination 주소를 갖고, error-checking-data를 갖음
    - 만일, 손상된 frame이 탐지되면, 버려지고 상위의 레이어 프로토콜이 lost frame의 retransmission을 행함
  - 48-bit MAC 주소를 표준으로 채택
  - Internet Protocol도 Ethernet에서 흔하게 *carried over* 되므로, internet 구성의 핵심기술이기도 함
- c.f)
  - token ring
  - FDDI
  - ATM
  - 어떤 네트워크 방식을 사용하느냐에 따라 랜카드를 비롯한

### host

- 정의
  - 네트워크에 연결된 머신

### router

- 정의
  - 다수의 네트워크와 연결되어 있으며, 서로 다른 독립된 네트워크간에 데이터를 중계할 수 있는 호스트

### gateway

- 정의
  - 하나의 네트워크에서 다른 네트워크로 데이터를 흐를 수 있도록 하는 네트워크 하드웨어
- 특징
  - 일반적으로, 라우터나 default gateway같은 하나의 gateway의 일을 행하도록 설정된 컴퓨터 프로그램을이나 컴퓨터를 지칭하는 경우도 존재
  - 라우터나 스위치와의 차이
    - **하나 이상의 프로토콜을 사용해서 많은 네트워크와 연결 가능**
    - **OSI 7 layer 어느 레이어에서도 동작 가능**
- c.f) Network gateway(protocol translation gateway, mapping gateway)
  - 서로 다른 네트워크 프로토콜을 갖는 네트워크들 사이에 protocol conversion을 가능하게 함
  - enterprise network에서는 network gateway가 일반적으로 proxy server와 firewall의 역할도 하는 경우가 존재
  - e.g)
    - office와 home intranet <-> internet

### bridge

network bridging의 high level overview

![](./images/network/network_bridging.png)

- 정의
  - 다수의 network segments, communication networks 로부터 하나의 aggregate network를 만드는 컴퓨터 네트워크 장치
    - 그러한 기능을 network bridging이라고 함
- 특징
  - vs routing
    - routing
      - 다수의 네트워크가 독립적으로, 분리된 채로 커뮤니케이션 가능하게 함
    - bridging
      - 서로 다른 네트워크들을 하나의 네트워크인 것 처럼 연결하는 것
  - data link layer에 작용
- 종류
  - *Transparent bridging*
  - *Simple bridging*
  - *Multiport bridging*

### Network Bandwidth(대역폭)

- 정의
  - 주어진 경로를 통해서 단위 시간당 데이터를 전송 속도
    - 즉, 단위시간 당 주어진 경로에 얼마나 많은 데이터를 전송할 수 있는가

## Application Layer

### LDAP(Lightweight Directory Access Protocol)

- 정의
  - TCP/IP 위에서 분산 디렉터리 정보 서비스를 조회하고 수정하는 application protocol
- 응용
  - username과 password의 저장소를 제공
    - 여러 서로 다른 애플리케이션이 user를 validate하기 위해서 연결함
- 연산
  - Add
  - Bind
  - Delete
  - Search and Compare
  - Modify
  - StartTLS
  - ...
- URI scheme
  - `ldap://host:port/DN?attributes?scope?filter?extensions`
