# OSI(Open Systems Interconnection)model

## 참조

- [나무위키 - OSI7 Model](https://namu.wiki/w/OSI%20%EB%AA%A8%ED%98%95)
- [열혈강의 TCP_IP 설명](http://jjoreg.tistory.com/entry/%EC%97%B4%ED%98%88%EA%B0%95%EC%9D%98-TCPIP-%EC%86%8C%EC%BC%93%EC%97%90-%EB%8C%80%ED%95%9C-%EC%84%A4%EB%AA%85)

## 정의

국제표준화기구(ISO)에서 개발한 모델로, 컴퓨터 네트워크 프로토콜 디자인과 통신을 계층으로 나누어 설명한 것이다.

## OSI계층

### 1. Physical layer

단위: Bit

대표적 프로토콜: 전선, 전파, 광섬유, 모뎀 ..

### 2. Datalink layer

단위: Frame

대표적 프로토콜: Ethernet, WLAN, PPP, FDDI

### 3. Network layer

단위: Packet, Datagram

대표적 프로토콜: IP, ICMP, IGMP, ARP

### 4. Transport layer

단위: Segment

대표적 프로토콜: TCP, UDP, ...

### 5. Session layer

단위: Message, Data

대표적 프로토콜: TLS, SSH, ...

### 6. Presentation layer

단위: Message, Data

대표적 프로토콜: JPEG, MPEG, ...

### 7. Application layer

단위: Message, Data

대표적 프로토콜: HTTP, SMTP, Telnet, SSH, ...
