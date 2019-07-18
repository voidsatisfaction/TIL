# TLS(Transport Layer Security)

- 의문
- TLS의 정의
- TLS동작 원리

## 의문

- *TLS에서 맨 처음 클라이언트가 ClientHello 메시지를 보내고 Server가 ServerHello메시지를 보내면서 인증서와 공개키를 준다고 했는데, 이것들은 암호화가 된 정보들인가? 아니면 되지 않아도 되는가? 만일, 암호화기 되어있다면 클라이언트는 어떻게 복호화하는가?*

## TLS의 정의

## TLS동작 원리

![](./images/TLS/tls_negotiation.png)

- Transport layer의 연결을 끝냄(TCP / UDP)
- 클라이언트가 서버로 `ClientHello`메시지를 보냄
  - 클라이언트가 가능한 TLS 버전
  - 서버 도메인
  - 세션 식별자
  - 암호 설정
- 서버가 클라이언트로 `ServerHello` 메시지를 보냄
  - 사용하기로한 TLS 버전
  - 세션 식별자
  - 암호 설정
  - certificate
    - CA가 서명해준것
    - 공개키 포함
- 클라이언트가 서버로 부터 받은 인증서 검증
  - 유효 기간
  - CA유효성
- 클라이언트가 pre-master secret을 생성하고, 공개 키를 사용해 암호화 한 뒤, pre-master-secret을 `ClientKeyExchange`메시지에 포함시켜 서버에 전송
  - 이떄에 pre-master secret을 이용해서 master secret을 만들고, session key(대칭키)도 만들어 놓음
- 서버가 받은 정보를 private키로 복호화 하여 pre-master secret을 파악
  - 해당 pre-master secret으로 master secret을 생성
  - master secret으로 session key 생성
    - 이 session key(대칭키)로 서버와 클라이언트간의 통신을 암호화
- 서로 `ChangeCipherSpec`메시지를 보냄
  - 앞으로의 모든 통신 내용은 세션 키를 사용해 암호화 할것임을 명시
- 서로 `Finished`메시지를 송신
  - handshaking 종료
