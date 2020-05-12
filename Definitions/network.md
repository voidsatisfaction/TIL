# Network 관련 정의

- 네트워크
  - host
  - router
  - gateway
  - bridge
  - intranet

## 네트워크

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

### intranet

- 정의
  - 외부의 접근을 배제한 한 조직내의 컴퓨터 네트워크
- 구성
  - LAN, WAN 등의 기술을 이용
