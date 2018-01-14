# OSI(Open Systems Interconnection)모델과 TCP모델

## 프로토콜에 관한 용어

- 1옥텟 = 1바이트 = 8비트
- word(단어): 복수의 비트의 그룹
  - 16비트 단어, 32비트 단어 등등..
- flag(플래그): 1비트의 제어 함수
  - 1: set, 0: clear

## 참조

- [나무위키 - OSI7 Model](https://namu.wiki/w/OSI%20%EB%AA%A8%ED%98%95)
- [열혈강의 TCP_IP 설명](http://jjoreg.tistory.com/entry/%EC%97%B4%ED%98%88%EA%B0%95%EC%9D%98-TCPIP-%EC%86%8C%EC%BC%93%EC%97%90-%EB%8C%80%ED%95%9C-%EC%84%A4%EB%AA%85)

## 개관

![OSI7_TCP5](./images/OSI7_TCP5.png)

## OSI계층

국제표준화기구(ISO)에서 개발한 모델로, 컴퓨터 네트워크 프로토콜 디자인과 통신을, 계층으로 나누어 설명한 것이다.

### 1. Application layer

단위: Message, Data

대표적 프로토콜: HTTP, SMTP, Telnet, SSH, ...

### 2. Presentation layer

단위: Message, Data

대표적 프로토콜: JPEG, MPEG, ...

### 3. Session layer

단위: Message, Data

대표적 프로토콜: TLS, SSH, ...

### 4. Transport layer

단위: Segment

대표적 프로토콜: TCP, UDP, ...

### 5. Network layer

단위: Packet, Datagram

대표적 프로토콜: IP, ICMP, IGMP, ARP

### 6. Datalink layer

단위: Frame

대표적 프로토콜: Ethernet, WLAN, PPP, FDDI

### 7. Physical layer

단위: Bit

대표적 프로토콜: 전선, 전파, 광섬유, 모뎀 ..

## TCP/IP 5 Layer Model

- OSI 7 레이어 모델 보다 더 간단함
- ARPANET 네트워크에 의해 개발되었다.
- DoD 모델로도 불림

### 1. Application Layer

- 애플리케이션 데이터 파일 생성, 받은 데이터 활용
- 다른 두 컴퓨터의 애플리케이션과 서비스들의 의사 소통

### 2. Transport Layer

- 파일을 분해하고 순서를 기록
  - 분해된 파일: TCP Payload Segments
  - 순서: TCP Sequence Numbers
- 데이터를 받는 경우
  - 없어진 조각을 찾는데에 활용
  - 순서를 바로잡는데에 활용
  - 애플리케이션과 연결된 포트를 제공
    - TCP(Transmission Control Protocol)
    - UDP(User Datagram Protocol)

### 3. Internet Layer

- 각각의 조각에다가 출발지와 목적지의 IP주소를 작성
  - 보내는이: Source IP 주소
  - 받는 이: Destination IP 주소
- 이 주소는 라우터가 받는이의 주소를 확인해서 해당하는 아이피가 자신의 서브넷에 속하는지 판단하기 위해서 사용된다.
  - IPv4: 32비트
  - IPv6: 128비트
- 패킷이 다양한 다른 서로 연결된(interconnected) 네트워크로 다닐 수 있게 도와준다.
  - addressing & routing 함수를 도와준다.
  - e.g 이더넷 - 와이파이 - 이더넷 연결이 가능

### 4. Network Access Layer

- 데이터 파일의 타입을 선택
  - 메일의 경우, air mail, surface mail, priority mail 등
  - 위성 커뮤니케이션
  - 모바일 커뮤니케이션: 3G, 4G(LTE), 5G
  - 광 섬유 케이블
- 단일 타입 네트워크의 커뮤니케이션을 제공
  - 이더넷, 와이파이, 블루투스, 모바일 커뮤니케이션(2G, 3G, 4G, 5G) etc
  - 한 네트워크 속에서 기기의 어드레싱, 우선도 관리, 에러 관리, 흐름 관리등을 행한다.
  - LAN(Local Area Networks)에서는 NAL 기기의 주소를 MAC(Medium Access Control)주소라고 부른다.

### 5. Physical Layer

- 네트워크 접근 레이어에서 선택한 타입에 따라서, 어떻게 운반할지를 결정
  - Wired, Wireless, Optical
- 기기나 네트워크의 물리적 인터페이스
  - 신호의 송신 수신을 도와준다.
  - Medium & Channel 특징을 갖음
    - 와이어, 와이어리스, 옵틱
  - Modem(Modulator + Demodulator)
    - 마이크로 웨이브, 밀리미터 웨이브, 빛
  - Antenna
    - 단일 안테나, 다중 안테나

## 애플리케이션 파일 전송의 예시

![TCP_IP](./images/TCP_IP.png)

한 컴퓨터(H1)의 애플리케이션의 파일을 TCP/IP 네트워킹을 통해서 다른 컴퓨터(H5)의 애플리케이션으로 전송하는 예를 생각해보자.

1. 컴퓨터 H1의 애플리케이션은 H5로 전송될 파일을 생성
2. 파일은 IP패킷과 이더넷 프레임 사이즈 기준인 MTU(Maximum Transfer Unit)사이즈에 기반하여 `payload segments`로 분할 된다.
3. TCP 헤더가 데이터의 조각에 추가되고, H1과 H5가 3방향 핸드쉐이크로 TCP 세션을 생성한다. (SYN -> SYN, ACK -> ACK) TCP 흐름과 에러 처리는 H1과 H5에 의해서만 처리된다. 라우터가 끼어들지 못한다.
4. IP헤더가 IP 패킷을 생성하기 위해서 추가된다. IPv4(32비트) IPv6(128비트)은 각각 다른 IP 헤더를 갖으며, 헤더는 `Source`와 `Destination` IP 주소를 포함한다.
5. 이더넷 헤더와 트레일러가 IP 패킷에 추가된다. 이는 이더넷 스위치에 의해 사용되며, 이더넷 스위치는 흐름과 에러 처리를 행한다. 만일 WiFi와 같은 다른 프로토콜을 사용하는 경우에는 그 자신만의 프로토콜 헤더를 넣는다.
6. 송신된 데이터는 송신 중간의 라우터에게 IP 주소를 보여준다. 라우터는 라우팅 테이블을 이용해서 패킷을 어디로 보낼지 결정한다. 최적의 라우팅 경로는 라우팅 알고리즘을 사용해서 설정된다.
7. 제대로된 주소에 도착한 이더넷 프레임은 H5의 네트워크 인터페이스 카드에 의해서 받게 된다. 이더넷 헤더와 트레일러가 프레임 내의 에러를 탐지한다. 만일 에러가 탐지되면 프레임은 버려지고 프레임 재송신 요청이 발급된다.
8. 이더넷 헤더와 트레일러는 IP 패킷을 보여주기 위해서 제거된다. IP 패킷 헤더는 많은 네트워크 제어 함수를 포함한다. e.g ECN(Explicit Congestion Notification)
9. IP 헤더는 TCP 헤더를 보여주기 위해서 제거된다. TCP는 데이터 전송 속도를 증감하기 위해서 윈도우 사이즈를 조절한다. TCP는 데이터를 H5의 앱 X와 연결하기 위해서 포트 주소를 포함한다.
10. TCP 헤더가 제거되고, Payload 조각이 나타난다.
11. Payload 조각은 애플리케이션 데이터 파일을 만들기 위해서 조합된다.
12. 애플리케이션 데이터 파일은 앱 X로 전송된다.

## IPv4

- IP 패킷 == 데이터그램(Datagram)
  - 독립적인 존재(entity)
  - 이전 패킷에 의존하지 않고 라우팅가능한 충분한 데이터 보유
- IPv4 패킷 = `헤더 + 페이로드`
  - 헤더 = IPv4 헤더
  - 페이로드(payload) = TCP/UDP 헤더 + 데이터 (페이로드 조각)
- 중요기능
  - 인터네트워킹(Internetworking)
  - 라우팅

### IPv4 헤더

![ipv4 header](./images/ip_packet_header.png)

- IPv4 패킷을 목적지로 전송하기 위한 모든 정보 제공
  - 그래서 데이터그램으로 불린다.
- 버전(Version)
  - 다른 IP 패킷 버전과 구분하기 위함
  - IPv4 패킷은 버전 값을 4 포함한다(IPv6은 6)
- 인터넷 헤더 길이(Internet Header Length)
  - IPv4헤더를 단어(words)단위로의 길이
  - 1단어 = 4옥텟 = 4바이트 = 32비트
  - 최솟값은 5, 그러므로 최소 헤더 길이는 5 * 4옥텟 = 20옥텟
- DS & ECN (8 비트)
  - DS(Differentiated Services) 부분
    - 첫 6비트
    - 서비스 과제의 우선순위를 나타냄
  - ECN(Explicit Congestion Notification)
    - DS뒤의 2비트
    - 네트워크 속도 지연이 발생한 경우 패킷이 전송되는 속도를 낮추라는 명시적인 시그널링
- Total Length
  - 옥텟을 단위로 하는 IP 패킷의 총 길이
  - 최대 IP패킷의 길이는 (2^16-1) = 65535옥텟 = 524280비트
  - 하지만 IPv4 패킷 사이즈는 `Layer 2`의 프레임 사이즈로 제한된다.
  - MTU
    - IP 패킷이 파편화 없이 전송될 수 있는 최대 사이즈
    - 이더넷의 경우: 1500옥텟(여기에 18~22 옥텟이 추가 오버헤드로 들어간다)
    - Wi-Fi의 경우: 2304옥텟(MPDU Mac Protocol Data Unit역시 포함되는 사이즈)
- 아이덴티티피케이션(Identification)
  - IPv4를 유일하게 식별하기위한 연속된 숫자
  - `출발지 주소`, `도착지 주소`, `프로토콜` 필드와 함꼐 사용된다.
- 플레그 & 프레그먼트 오프셋
  - 패킷 파편화에 사용
  - 패킷이 너무 커서 나눌떄 사용
  - 플레그는 3비트
    - 비트0: 예비용
    - 비트1: DF(Don't Fragment) 1은 파편화 하지 말라, 0은 파편화 하라
    - 비트2: MF(More Fragments) 1은 더 파편화 하라, 0은 마지막 파편이다
  - 기존 데이터그램에서 이 파편이 어디에 속하는지를 나타냄
    - 마지막이 아닌 나머지 파편은 64비트 길이의 데이터 필드를 갖는다.
- TTL(Time to Live) (8비트)
  - 인터넷에 한 데이터 그램이 얼마나 남아있을 수 있는지 나타냄
  - IP패킷이 지나가는 모든 라우터는 TTL을 하나씩 줄여나가야 한다(hop count와 비슷함)
  - 패킷이 지나가다가 TTL이 0이 되면 그 패킷은 버려진다.
- Protocol
  - IPv4 헤더 다음으로 오는 다음 헤더의 타입을 구별
  - ICMP / IGMP / TCP / UDP / ENCAP / OSPF / SCTP
- 헤더 체크섬
  - IPv4 패킷 헤더를 에러로부터 보호하기 위해서 에러 감지 코드를 붙인다.
  - 그러나 payload쪽 부분은 지키지 못한다.
  - 각각의 라우터마다 헤더 체크섬을 읽고 에러를 체크한다. 왜냐면 IP 헤더는 패킷이 라우터에서 나갈때 바뀔 수 있으므로.. (e.g. TTL, Flags, Fragmentation, etc)
- 출발지 주소 & 도착지 주소
  - 각각의 주소는 32비트
  - 클래스 가능한 주소: Class A, B, C, D, E가 존재(요즘은 안쓰임)
  - CIDR(Classless Inter-Domain Routing) => 요즘은 이게 더 유행, IP를 더 쉽게 할당하고 IP라우팅을 쉽게 해줌.
    - 서브넷의 보다 효율적인 라우팅
    - 네트워크 사이즈 + 단기 예측 수요로 기관의 IPv4 & IPv6 주소 할당을 함
    - `123.234.100.56/24`
      - IPv4 주소 (32비트) 123.234.100.56
      - 서브넷 마스크는 24개의 1
      - 서브넷 마스크: `255.255.255.0`
      - 서브넷 사이즈: 2^(32-24) = 2^8 = 256
      - 라우팅 접두사 `123.234.100.0`도 IPv4주소 `123.234.100.56`와 서브넷 마스크 `255.255.255.0`을 이용해서 얻을 수 있다.
- 옵션(변수, 패딩)
  - IPv4의 패킷 헤더가 32비트의 배수라는 것을 확인하려고 사용된다.
  - 32 비트의 배수에 맞춰서 추가 비트를 생성해줌

MTU Ethernet

![mtu-ethernet](./images/mtu-ethernet.png)

MTU Wi-Fi

![mtu-wifi](./images/mtu-wifi.png)
