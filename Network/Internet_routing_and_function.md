# Internet Routing & Function

## 게이트웨이 vs 라우터

- 게이트웨이
  - 컴퓨터 네트워크에서 서로 다른 통신망, 프로토콜을 사용하는 네트워크 간의 통신을 가능하게 하는 컴퓨터나 소프트웨어를 두루 일컫는 용어
  - 다른 네트워크로 들어가는 입구 역할(네트워크 포인트)
  - 개념
- 라우터(공유기)
  - 패킷의 위치를 추출하여 그 위치에 대한 최상의 경로를 지정하며 이 경로를 따라 데이터패킷을 다음 장치로 전향시키는 장치
  - 장비

## IGP vs EGP

### IGP(Interior Gateway Protocol)

- 라우터가 AS(Autonomous System, 자치적 시스템) 안에 있는 라우팅 정보를 교환하기 위한 프로토콜
  - 회사 네트워크
  - 캠퍼스 네트워크
  - ISP(Internet Service Provider) 네트워크
- IGP 카테고리
  - LS(Link-State) 라우팅 프로토콜
  - DV(Distance-Vector) 라우팅 프로토콜
- IGP의 예
  - OSPF(Open Shortest Path First): 가장 많이 사용
  - RIP(Routing Information Protocol)
  - IS-IS(Intermediate System to Intermediate System)
  - EIGRP(Enhanced Interior Gateway Routing Protocol)

#### OSPF(Open Shortest Path First)

- 인터넷 상에서 가장 많이 사용되는 IGP 라우팅 프로토콜
- IPv4, IPv6 그리고 CIDR주소를 위한 라우팅 프로토콜
- 인터넷 게이트웨이나 라우터에 의해서 사용됨
- LSR(Link State Routing)알고리즘 사용

##### 동작

- 라우터가 LS(Link State)정보를 같은 AS 네트워크 안에 있는 다른 라우터로부터 얻음
- 네트워크 연결 맵(트리 구조)가 링크들의 비용 값을 포함해서 만들어짐
  - 트리의 루트노드는 내 노드(출발지 노드)가 됨
  - 거기서 부터 모든 다른 노드에게 가지를 뻗어나감
- LS 라우팅 알고리즘은 출발지 노드(루트 노드)에서 모든 다른 노드까지의 최단 거리 트리를 구하는데에 사용됨(루프를 제거)
  - SPT(Shortest Path Tree)는 가장 적은 코스트의 라우팅 경로를 **다익스트라 알고리즘**을 사용해서 구할 수 있음
- 게이트웨이/라우터는 SPT 라우팅 경로에 기반한 그들의 라우팅 테이블을 설정하고 갱신함
- 만일 네트워크에 변화가 감지되면 앞의 동작을 다시 반복

**다익스트라 최소비용 트리 알고리즘의 예시**

![](./images/dijkstra_routing_path.png)

##### OSPF 링크 비용 요소

- 라우터의 거리
- RTT(Round-Trip Time)
- 목적지에 도착하기 위한 hop의 개수(routers/switches)
- 스루픗(throughput): 비트/s, 패킷/s
- availability
- reliability

##### OSPF 라우팅 타입

- IR(Internal Router)
  - 모든 라우팅 인터페이스가 같은 네트워크 구역에 포함됨
- ABR(Area Border Router)
  - 서브 구역 네트워크를 핵심 네트워크에 연결함
- BR(Backbone Router)
  - 핵심 네트워크를 연결함
- ASBR(Autonomous System Boundary Router)
  - 여러가지 라우팅 프로토콜을 사용하여 AS사이를 연결해줌

라우터는 다양한 역할을 갖을 수 있음

#### MOSPF(Multicast Open Shortest Path First)

- 멀티캐스트 라우팅(multicast routing)을 지원하기 위한 OSPF 확장
- 그룹 멤버십 정보를 멀티캐스트 라우딩 경로 설정에 라우터들이 사용할 수 있도록 공유함
- 대체 멀티캐스팅 체계는 다음을 포함:
  - OSPF + PIM(Protocol Independent Multicast)

#### OSPF Subdivided Networks

- 운영과 제어 요건에 기반한 분리
  - 운영의 단순화
  - 트래픽과 자원 사용의 최적화
  - 보안 강화
  - 빠른 라우팅 갱신
- 서브 구역 네트워크와 핵심 네트워크를 생성하는 네트워크 서브 분리(Subdividing)

#### OSPF-TE(Traffic Engineering)

- 들어오는 노드에서 나가는 노드로 부터까지의 IP 패킷의 라우팅 제어의 TE QoS(Quality of Service)
- TE는 에러와 실패로 인한 서비스 장애를 최소화 함
  - 신뢰성 증가
- TE는 인터넷 트래픽의 성능 최적화를 위한 모델링, 묘사, 측정을 가능하게 함
- TE는 IP와 IP가 아닌(광학 네트워크) 네트워크에서 사용 가능

### EGP(Exterior Gateway Protocol)

- AS들 사이 혹은 외부의 라우팅 정보를 교환하기 위해 사용되는 프로토콜
- 라우팅 경로 선택은 다음에 기반한다:
  - 네트워크 정책들
  - 네트워크 관리자가 설정한 규칙
- 현재 인터넷은 BGP4(Border Gateway Protocol version 4)를 사용함(2006년부터)

### BGP(Border Gateway Protocol)

#### eBGP(external BGP)

- AS들 사이에서 사용되는 BGP 라우팅

#### iBGP(internal BGP)

- AS내부에서 사용되는 BGP 라우팅

#### BGP 보안

- BGP 라우팅은 보통 다른 ISP들에 속함
  - 각각의 라우터는 다른 암호화와 보안 정책을 사용할 수 있음
  - 라우터와 게이트웨이는 다른 ISP들에 의해서 제어되므로, 보안 셜합이 힘들 수 있음
  - 그래서 BGP 라우터는 서로의 설정과 갱신된 정보를 교환 해야함
    - 통합이 좋지 못하면, 보안적 취약점이 됨
  - 만일 서로 다른 암호화와 보안 설정이 사용되면, 인증과 사칭 BGP 메세지, 말웨어의 방어를 하기 어려워 질 수 있음

### ARP(Address Resolution Protocol)

![arp packet](./images/arp_packet.png)

- 논리적인 IP주소(인터넷 네트워크에서 유일한 호스트 주소)에서 물리적인 MAC주소(네트워크 속의 하드웨어 주소, 네트워크 카드/랜선)를 얻음
- IPv4/IPv6 주소를 장치의 DLL(Data Link Layer) 주소에 매핑함
  - IPv4주소 <=> 매핑 <=> 이더넷(IEEE 802.3) MAC(Medium Access Control)주소
- IPv6 네트워크는 NDP(Neighbor Discovery Protocol)를 ARP의 기능을 구현하기 위해서 사용
  - IPv6주소 <=> 매핑 <=> Wi-Fi(IEEE 802.11) MAC(Medium Access Control)주소
- RFC 826(1982)와 인터넷 표준 STD 37에 규정됨
- IANA(Internet Assigned Numbers Authority)가 ARP 인자 값을 관리

- 4계층에서 필요한 서비스 구분 번호는 애플리케이션 에서 입력
- 3계층에서 필요한 IP주소는 사용자가 통신하기 위해서 디바이스에 입력
- 2계층에서는 따로 입력이 되지 않음 주소를 디바이스 스스로 결정해주어야 함
  - 논리적인 IP주소를 기반으로 물리적인 MAC주소로 바꾸어주는 주소해석 프로토콜
  - 목적지 IP주소가 같은 네트워크일 경우에는 해당 장비를 직접 찾는 Request 메시지를 브로드 캐스트로 보냄
    - 호스트 MAC주소를 직접 얻음
  - 다른 네트워크일 경우에는 직접 브로드캐스트를 보낼 수 없으니, 게이트웨이로 데이터를 전달하기 위해 게이트웨이 에게 요청을 보냄.
    - 그러므로 게이트웨이의 MAC주소를 얻게 됨
