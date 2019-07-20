# "What happens when you type google.com into your browser's address box and press enter?"

- 클라이언트 웹 브라우저
- 클라이언트 커널
  - DNS resolution
  - destination 컴퓨터와 통신하기
- 서버
  - HTTP 서버 요청 핸들링
- 클라이언트 웹 브라우저

## 의문

## 정리

### 1. 클라이언트 웹 브라우저

- "g"키가 눌렸을 경우
- "enter"키가 눌려지고 손을 뗄 경우
- Interrupt 이벤트 발생
- 키가 눌렸다는 메시지를 앱으로 전달
- URL 파싱
- URL 검증(URL인지, 쿼리인지)
- 호스트이름에 있는 유니코드 글자를 변환
- HSTS(HTTP Strict Transport Security) 리스트 확인
  - 서버가 HTTPS로만 클라이언트(웹 브라우저)가 접근할 수 있도록 클라이언트 쪽에서 강제하도록 하는 것(최초 접속시)
  - 강제된 사이트는 리스트에 등록됨
  - Man in the Middle 공격 방어

### 2. 클라이언트 커널

- DNS resolution
  - DNS 확인
    - 해당 도메인이 브라우저 캐시에 있는지 확인
    - 없으면 `gethostbyname()` 함수 호출
      - 먼저 로컬 `hosts`파일에서 호스트 이름 찾음
    - 없으면 network stack에 정의된 DNS 서버에 리퀘스트를 보냄
      - 로컬 라우터나, ISP의 캐싱된 DNS 서버임
    - DNS 서버가 같은 서브넷 속에 있으면 ARP process를 DNS 서버 IP를 대상으로 직접 수행
    - DNS 서버가 같은 서브넷 속에 없다면 ARP process를 default gateway IP를 대상으로 직접 수행
  - ARP 프로세스
    - 대상 IP가 ARP 캐시가 되어있는지 확인. 있으면 대상 IP에 해당하는 MAC 주소를 사용
    - 캐시가 없다면
      - 타겟 IP 주소가 서브넷의 로컬 라우트 테이블에 있는지 확인
      - 없으면 default gateway의 서브넷을 갖는 인터페이스를 사용함
    - 선택된 네트워크 인터페이스의 맥 주소가 확인됨
    - 네트워크 라이브러리가 Layer 2 ARP 리퀘스트를 보냄

`ARP Request :`

```
Sender MAC: interface:mac:address:here
Sender IP: interface.ip.goes.here
Target MAC: FF:FF:FF:FF:FF:FF (Broadcast)
Target IP: target.ip.goes.here
```

컴퓨터와 라우터 사이가 Switch 일 경우

- 만일 컴퓨터가 (L2)스위치에 연결되어있으면, 스위치는 local CAM/MAC 테이블을 찾아서 어떤 포트가 타겟 맥 주소를 갖고 있는지 확인. 그러한 맥 주소가 없으면 모든 다른 포트에 ARP rebroadcast를 함
- 만일 스위치의 MAC/CAM 테이블에 해당 타겟이 존재하면, 그 포트에 ARP request를 보냄
- 라우터가 같은 와이어에 있다면, `ARP Reply`와 함꼐 값을 반환함

`ARP Reply :`

```
Sender MAC: target:mac:address:here
Sender IP: target.ip.goes.here
Target MAC: interface:mac:address:here
Target IP: interface.ip.goes.here
```

이제 우리가 사용하는 네트워크 라이브러리가 DNS 서버나 default gateway의 IP 주소를 갖고 있으므로, DNS 프로세스를 계속 진행 가능(데이터 프레임 구성 가능)

- 포트 53이 DNS 서버에 UDP 리퀘스트를 하기 위해서 열림
  - 응답 사이즈가 너무 크면 TCP가 대신 사용됨
- 로컬 ISP DNS 서버에 해당 도메인이 없으면 recursive하게 도메인을 찾아나감

- destination 컴퓨터와 통신하기
  - TCP 소켓 열기
    - 브라우저가 destination의 IP 주소를 받으면, 포트번호와 `socket`이라는 시스템 라이브러리와 함께 해당 시스템에 call 하고, TCP 소켓 스트림을 요청함 - (`AF_INET/AF_INET6` 그리고 `SOCK_STREAM`)
    - 패킷 생성
      - 이 요청은 먼저, TCP segment가 만들어지는, Transport Layer에 넘겨짐. destination port가 헤더에 추가되고, source port가 커널의 다이나믹 포트 레인지에 의해서 선택됨
      - 이 세그먼트는 Network Layer로 보내지며, 그곳에서 세그먼트에 추가적인 IP 헤더를 덮어줌 destination server의 IP 주소와 현재의 컴퓨터의 IP 주소가 패킷형태로 추가됨
      - 이 패킷은 Data Link레이어로 넘겨짐. source 그래픽 카드의 MAC 주소와 로컬 라우터(게이트웨이)의 맥 주소가 추가됨 포함된 프레임 헤더가 추가됨
        - 게이트웨이의 맥 주소를 모르면, ARP request를 broadcast해서 알아내야 함
      - 여기 까지 끝나면 다음과 같은 네트워크에서 데이터를 전송할 수 있음
        - Ethernet
        - WiFi
        - Cellular data network
    - 패킷 전송
      - 결국, 이 패킷은 로컬 서브넷을 관리하는 라우터로 도착
      - 이 패킷은 destination을 포함하는 라우터까지 여행해서 결국엔 destination으로 전송됨
        - 그 동안 각각의 라우터는 IP 헤더로부터 destination 주소를 얻고, 적절한 next hop 으로 보내준다.
        - IP 헤더의 TTL(Time To Live) 필드는 각각의 라우터를 지나갈 때 마다 1씩 줄어둔다.
          - TTL field가 0이되면 패킷이 드랍됨
  - TLS handshake 하기
    - TLS 문서 참고
  - HTTP 프로토콜
    - HTTP 문서 참고

### 3. 서버

- HTTP 서버 요청 핸들링
  - HTTPD(HTTP Daemon) 서버는 서버 사이드 requests/responses를 핸들링하는 소프트웨어임
    - 대표적으로는 Apache / NginX / IIS 가 있음
  - 순서
    - HTTPD가 request를 받음
    - 아래와 같은 파라미터로 request를 분해
      - HTTP Request Method
      - Domain
      - Requested path/page

### 4. 클라이언트 웹 브라우저

- 웹 브라우저의 뒷편에서..
- 브라우저
- HTML 파싱
- CSS 해석
- Page 렌더링
- GPU 렌더링
