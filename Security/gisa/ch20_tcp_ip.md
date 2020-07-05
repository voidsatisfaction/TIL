# TCP/IP

- 의문
- 20.1 Physical Layer
- 20.2 Datalink Layer
- 20.3 Network Layer
- 20.4 Transport Layer
- 20.5 Application Layer

## 의문

## 20.1 Physical Layer

### 물리 계층 개요

- 데이터와 신호
  - 개요
    - 데이터와 데이터를 표현하는 신호는 아날로그 또는 디지털 형태일 수 있음
- 아날로그와 디지털 데이터
  - 아날로그 데이터
    - 연속적인 정보
  - 디지털 데이터
    - 이산적 데이터

## 20.2 Datalink Layer

### 데이터링크 계층의 소개

- 노드와 링크
  - 데이터링크 계층에서의 통신은 node-node
    - 인터넷은 LAN과 WAN과 같은 많은 네트워크를 통해 전달
  - 링크는 노드와 노드 사이를 이어주는 네트워크 망
- 서비스
  - Framing
    - 네트워크 계층의 패킷을 프레임으로 캡슐화가 필요
  - Flow Control
    - 프로토콜에 따라 다름
  - Error Control
    - 오류 검출이 필요
    - 오류 검출 이후에 송신자 노드에서 이를 수정하거나 오류를 폐기하고, 재전송을 송신 노드에게 요청해야 함
  - Congestion Control
    - 대부분의 데이터링크 계층의 프로토콜은 혼잡제어를 사용하지 않음
    - 대신 인터넷 계층에서 많이 사용

## 20.3 Network Layer

### 네트워크 계층 개요

#### 네트워크 계층 서비스

- routing
  - 정의
    - 패킷이 source에서 destination으로 갈 수 있도록 경로를 지정해주는 것
- forwarding
  - 정의
    - 라우터상의 하나의 인터페이스에 패킷이 도착했을 때 라우터가 취하는 행동
    - 일반적으로 forwarding(routing) table을 이용해서 의사결정을 함
- IPv4 주소
  - 클래스 기반의 주소 지정
    - 더 이상 사용되지 않음(주소 고갈)
    - 주소 고갈 해결
      - network mask
        - 클래스에 할당된 ip의 마스크
      - subnet mask
        - 클래스의 내부에 할당된 서브넷의 마스크
  - 클래스 없는 주소 지정
    - CIDR
      - 개요
        - 클래스 A, B, C의 개념 무시
      - 특징
        - 주소 클래스가 없기 때문에, `byte.byte.byte.byte/n` 등으로 표현
  - 특수 주소
    - this-host address
      - 정의
        - 호스트가 IP 데이터그램을 보내려고 하지만, 근원지 주소인 자신의 주소를 모를 때 사용
    - limited-broadcast address
      - 정의
        - `255.255.255.255/32`이며, 호스트나 라우터가 네트워크상의 모든 장치로 데이터그램을 보낼 때 사용됨
        - 네트워크 외부로 패킷을 보낼 수는 없음
    - loopback address
      - 정의
        - `127.0.0.1/8`이며, 이 블록 내의 주소를 가진 패킷은 호스트를 벗어나지 않고 호스트에 남음
        - 소프트웨어 테스트의 용도로 많이 사용됨
    - private addresses
      - 정의
        - 사설 주소에만 사용 가능한 라우팅이 불가능한 특수 주소 집합(public internet에 존재하지 않음)
      - 종류
        - class A
          - 24비트 블록
          - 10.0.0.0 - 10.255.255.255
        - class B
          - 20비트 블록
          - 172.16.0.0 - 172.31.255.255
        - class C
          - 16비트 블록
          - 192.168.0.0 - 192.168.255.255

### 네트워크 계층 프로토콜

- IP
- ARP
- ICMPv4

#### IP

- 개요
  - IPv4는 비신뢰적, 비연결형인 데이터그램 프로토콜로, 최선형 전송 서비스(best-effort delivery service)
    - 최선형의 의미는, IPv4 패킷이 훼손되거나 손실, 순서에 맞지 않게 도착, 지연 도착, 네트워크 혼잡 발생 가능성을 의미
  - 신뢰성이 중요한 경우 TCP 처럼 신뢰성 있는 전송 계층 프로토콜과 함께 사용해야 함
  - TCP/UDP, ICMP, IGMP 데이터는 IP 데이터그램을 사용하여 전송됨
- IP 데이터그램
  - 정의
    - 패킷 교환망에서 취급되는 패킷의 일종(IP가 사용하는 패킷)
    - 발신 단말에서 수신 단말에 이르는 경로를 결정하기 위한 정보를 내부에 포함하는 패킷
- IPv4 데이터그램 형식
  - header
    - 20~60 bytes
    - source IP address, Destination IP address 등의 많은 필드 포함
  - payload
    - 데이터

#### 논리주소와 물리주소의 변환

- ARP(Address Resolution Protocol)
  - 개요
    - 호스트는 ARP 요청 메시지를 보낼 때 자신의 IP 주소, 자신의 MAC address, 수신자측 IP 주소는 알고 있지만, 물리 주소는 모르기 때문에 물리 계층 브로드캐스트를 통해 모든 호스트에게 패킷 전송
    - ARP 요청 메시지를 수신한 호스트 또는 라우터는 수신 IP 주소와 자신의 IP 주소를 검사하여, 자신에 대해 물리 주소를 요구하는 경우라면 ARP 응답 메시지를 전송
    - 각 시스템은 ARP Cache가 있고, 이 Cache에 정보를 저장해 둠(일정 시간 후 삭제 (보통 1-2분))
      - dynamic, static cache가 존재
  - ARP 메시지 종류
    - ARP 요청 메시지
      - 특정 IP 주소에 대한 물리 주소를 요구
      - 브로드캐스트
    - ARP 응답 메시지
      - 물리 주소 정보를 알림
      - 유니캐스트로 전송
      - 호스트가 라우터를 넘어서 다른 네트워크에 있으면, 라우터가 해당 호스트를 대신하여 응답 메시지 전송
- RARP(Reverse Address Resolution Protocol)
  - 개요
    - 물리주소에 해당하는 IP 주소를 얻고자 할 때 사용
    - 디스크와 같은 저장장치가 없는 호스트에서 주로 사용됨
      - RARP 응답은 RARP 서버에서 생성됨
- GARP(Gratuitous ARP)
  - 개요
    - Sender IP와 Target IP가 동일한 ARP 요청
    - 장비가 ARP 요청 브로드캐스트를 통해 다른 장비에게 네트워크에 있는 자신의 존재를 알리는 목적으로 사용되는 패킷
      - 이 패킷을 수신한 장비는 자신의 ARP Cache에 해당 정보가 있으면 이를 갱신
    - 자신의 MAC 정보를 동일 네트워크상의 다른 장비들에게 알려, ARP Cache를 갱신 하도록 하는 목적
  - 목적
   - IP 충돌 감지
     - 자신과 동일한 IP가 설정되어 있는 호스트가 있다면, 해당 호스트로부터 ARP 응답이 오기 때문에, 충돌 여부 확인 가능
     - 호스트 IP 변경 or 재부팅 시에 GARP 패킷이 생성됨
   - 상대방의 ARP Cache 정보 갱신
     - 이 패킷을 받은 쪽은 Sender IP를 인정하지 않고 Cache 정보를 갱신하게 되므로, MAC 정보가 위 변조가 될 수 있음

#### ICMPv4(Internet Control Message Protocol version 4)

### IPv6

## 20.4 Transport Layer

## 20.5 Application Layer
