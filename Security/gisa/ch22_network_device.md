# ch22. Network 장비의 이해

- 22.1 네트워크 장비의 이해
  - 랜카드
  - 허브
  - 브리지
  - 스위치
  - 라우터
  - 게이트웨이
- 22.2 VLAN의 구성 및 관리
  - 개요
  - 특징
  - VLAN 종류
  - 장점

## 의문

## 22.1 네트워크 장비의 이해

### 랜카드

- 개요
  - PC혹은 네트워크에서 전달되는 정보를 상호 교환할 수 있도록 만들어 줌
  - PC에서 전송 요구 발생 -> 랜카드로 정보를 일정한 형태로 만들어 보냄 -> 랜카드는 정보를 버퍼에 저장 -> 네트워크에 맞는 형태로 보냄
  - PC --- (네트워크 드라이버) --- 랜카드

### 허브

- 개요
  - 물리 계층에서만 동작하는 장치
  - repeater + ports
- 특징
  - 연결된 포트로 브로드캐스팅 됨

### 브리지

- 개요
  - 데이터링크 계층인 MAC에서 동작
  - 둘 & 그 이상의 네트워크를 상호 연결하는데 사용함
- 특징
  - collision domain을 나누어줌(CSMA/CD)
  - MAC이라는 하드웨어 주소를 기반으로 전송할 포트를 결정함

### 스위치

- 개요
  - 리피터 기능 ∧ 브리지의 기능
  - 모니터링 포트의 존재
    - 스위치를 통과하는 모든 패킷의 내용을 복제해서 전달하는 포트
    - 공격자가 sniffing에 쓰기도 함
- 종류
  - L2 스위치
    - 모든 포트에 연결된 호스트의 MAC 주소를 학습하며, 스위칭 테이블을 생성/갱신함. 이 테이블을 기초로하여 프레임 전달
  - L3 스위치
    - 소프트웨어보다는 하드웨어를 사용한 라우터의 한 형태
    - *ASIC* 스위칭 기술 사용
  - L4 스위치
    - 포트번호를 기준으로 패킷 전송하며, 주로 네트워크의 암호화나 애플리케이션 프로토콜에 대한 패킷 필터링에 사용됨
    - Transport 계층 포트번호를 통해 응용 계층 서비스(HTTP, NFS 등)을 구분하고, L4 스위치가 관리하고 있는 서버의 부하에 따라 세그먼트를 적절히 부하분산
      - SLB(Server Load Balancing)
  - L7 스위치
    - 세션 계층과 응용 계층의 데이터 영역까지 분석하여 응용 세션의 제어 수행이 가능
    - 일반적으로 L4 스위치가 0 ~ 1023 번까지의 포트만을 인식하는데, L7 스위치는 그 이외의 포트번호에 대해서도 인식 가능
  - L4스위치 VS L7스위치
    - 구조적 차이점
      - L4스위치
        - TCP/UDP 포트 정보를 분석해 해당 패킷이 현재 사용하는 서비스 종류(HTTP, FTP, 텔넷) 별로 패킷 처리
      - L7스위치
        - 트래픽의 내용(e-mail의 문자열, HTTP URL, FTP 파일 제목 등) 패턴 등을 분석해 패킷을 처리함
    - 기능적 차이점
      - 높은 수준의 intelligence를 갖춘 스위치일수록 더 정교한 패킷의 부하분산 및 QoS기능 구현이 가능함
- 스위칭 방법에 따른 분류
  - Store-and-Forward
    - 스위치나 브리지가 일단 들어오는 프레임을 전부 받아들인 다음에 처리를 시작하는 방식
    - 에러가 발견되면, 해당 프레임을 버리고 재전송을 요구하므로, 에러 복구능력이 뛰어남
  - Cut-Through
    - 앞에 들어오는 목적지 주소만을 본 다음에 바로 목적지로 전송하기 때문에 처음 48비트만을 보게 됨
    - 빠르게 처리하나, 프레임 에러 찾기 힘듬
  - Fragment-Free
    - Store-and-Forward ∧ Cut-Through 512비트를 봄
      - 에러감지능력이 컷스루에 비해 우수

### 라우터

- 개요
  - 3계층 장치로, 물리, 데이터 링크, 네트워크 계층에 동작
- 기능
  - 이기종 LAN 간의 연결
  - LAN을 WAN에 연결
  - 효율적인 경로를 선택하는 라우팅 기능
  - 에터 패킷에 대한 폐기 등의 기능
- 특징
  - broadcasting domain(and multicasting domain)의 분리
  - ACL(Access Control List)에 기반을 두어 트래픽 필터링하고, 분류 가능
  - 라우팅 프로토콜을 통하여, 경로와 네트워크에서 발생하는 변경에 대한 정보를 발견
    - 라우터에게 링크가 다운되었는지, 특정 경로가 혼잡한지, 다른 경로가 보다 경제적인지 알려줌\

브리지 vs 라우터

|브리지|라우터|
|----|-----|
|헤더정보를 읽지만, 변경시킬 수는 없음|각 프레임에 새로운 헤더를 생성|
|MAC 주소에 근거하여 전송 테이블을 작성|IP 주소에 근거하여 라우팅 테이블을 작성|
|모든 포트에 대해 동일한 네트워크 주소를 사용|포트마다 서로 다른 네트워크 주소를 지정|
|MAC 주소에 기반하여 트래픽을 필터링|IP 주소에 기반하여 트래픽을 필터링|
|브로드캐스트 패킷을 전달|브로드캐스트 패킷을 전달하지 않음|
|브리지에게 알려지지 않은 목적지 주소를 가진 트래픽도 전달|라우터에게 알려지지 않은 목적지 주소를 가진 트래픽은 전달하지 않음|

### 게이트웨이

- 개요
  - **두 개의 서로 다른 환경을 연결하는 장비에서 실행되는 소프트웨어를 위한 일반적 용어**
    - 한 환경이 다른 언어를 말하는 경우, 번역자로 동작하고 상호작용을 제한하는 역할도 수행
  - OSI 참조모델의 모든 계층을 포함하여 동작하는 네트워크 장비로서, 두 개의 완전히 다른 네트워크 사이의 데이터 형식을 변환하는 기능을 수행
    - e.g) WSGI
  - 여러 계층의 프로토콜 변환기능을 수행하므로, 네트워크 내에 병목현상을 일으키는 지점이 될 수 있음

## 22.2 VLAN의 구성 및 관리

### 개요

- 물리적인 선이 아닌, 소프트웨어에 의해 구성한 근거리 네트워크
  - 논리적인 세그먼트로 분할
  - 물리적으로는 네트워크가 같이 이어져있으나, 논리적으로는 broadcast doamin이 분리된 네트워크로 분리됨
- VLAN에서 한 사람이 다른 그룹으로 이동하더라도, 물리적인 구성을 바꿀 필요가 없음
- 스위치에서 지원하는 기능
- VLAN간의 통신은 L3SW나 라우터를 통해야만 가능

### 특징

- 데이터링크 계층에서 Broadcast domain을 나누기 위하여 사용하는 기술
- 각 스위치는 하나의 브로드캐스트 프레임에 대하여, 동일 브로드캐스트 그룹이 아닌 곳에는 전달하지 않는다는 조건을 바탕으로 하고 있음
- VLAN 태그가 상이한 네트워크로의 접근을 근본적으로 차단하여, 보안성을 유지
- VLAN은 관리자가 서로 다른 논리적 그룹에 대하여 서로 다른 보안 정책을 적용할 수 있게 함

### VLAN 종류

- Port 기반 VLAN
  - 스위치 포트를 각 VLAN에 할당
  - 같은 VLAN에 속한 포트에 연결된 호스트들 간에만 통신이 가능
  - 가장 일반적이고 많이 사용됨
  - e.g)
    - 관리자는 포트 1,2,3,7에 연결하는 지국들을 VLAN 1에 속하는 것으로 정의하고, 4,10,12에 연결하는 지국들을 VLAN 2에 속하는 것으로 정의함
- MAC 기반 VLAN
  - 맥어드레스를 VLAN에 등록하여 같은 VLAN에 속한 맥어드레스들 간에만 통신이 되도록 하는 방법
  - 이 방법은 각 호스트의 맥어드레스를 전부 등록해야 하기 때문에 자주 사용되지 않음
  - e.g)
    - 관리자는 `E2:13:42:A1:23:34`와 `F2:A1:23:BC:D3:41`를 가진 지국들은 VLAN1 에 속하는 것으로 정의할 수 있음
- 네트워크주소 기반 VLAN
  - 네트워크주소별로 VLAN을 구성하여 같은 네트워크에 속한 호스트들 간에만 통신이 가능하도록 구성한 VLAN. 주로 IP 네트워크 VLAN을 사용
  - e.g)
    - 관리자는 IP 주소 `181.34.23.72`, `181.34.23.112`를 가진 지국들을 VLAN 1에 속하는 것으로 정의
- 프로토콜기반 VLAN
  - 같은 통신 프로토콜(TCP/IP, IPX/SPX, NETVIEW)을 가진 호스트들 간에만 통신이 가능하도록 구성된 VLAN
- 멀티캐스트 IP 기반 VLAN
  - ?
- 조합
  - 최근 일부 제조사에서 제공하는 소프트웨어는 이러한 모든 특성을 조합하여 사용하고 있음
  - 관리자는 소프트웨어를 설치할 때 하나 이상의 특징을 선택할 수 있음

### 장점

- 경비와 시간 절약
  - 한 그룹에서 다른 그룹으로 이동하는 장비를 줄일 수 있음
- 가상 워크그룹의 생성
  - 학교 환경 속의 같은 프로젝트에서 일하는 교수들을 같은 과에 속하지 않더라도 서로 브로드캐스트 메시지를 주고 받을 수 있음
- 보안
  - 같은 그룹에 속한 사람들은 다른 그룹의 사용자들이 메시지를 수신하지 못함
  - 확실한 보장 하에 브로드캐스트 메시지 송신 가능