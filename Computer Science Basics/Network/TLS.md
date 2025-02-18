# TLS(Transport Layer Security)

- 의문
- TLS의 정의
- TLS동작 원리
- TLS설정

## 의문

- *TLS에서 맨 처음 클라이언트가 ClientHello 메시지를 보내고 Server가 ServerHello메시지를 보내면서 인증서와 공개키를 준다고 했는데, 이것들은 암호화가 된 정보들인가? 아니면 되지 않아도 되는가? 만일, 암호화기 되어있다면 클라이언트는 어떻게 복호화하는가?*
- 브라우저는 자신이 CA list를 갖고 있어서 server로 부터 받은 certificate이 신용 가능한 CA로부터 사인된 것인지 확인할 수 있는데, 그렇다면 단순 http 애플리케이션은(`requests`, `axios`) 어떻게 해당 certificate이 신용 가능한지 판단할 수 있는가?
  - 애초에 chrome browser는 OS에 내장된 certificate program을 활용(혹은 유저에 의해서 추가됨)
  - library에서는 TLS 처리하는 모듈에서 인증서 체인을 검증해주는 기능이 존재함. 인증서가 있는 곳은 설정을 따로 해주어야 함
- *근데, 사실, certificate을 중간에 해커가 탈취하면, 변장 공격이 가능한 것 아닌가?*

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

## TLS설정

- Nginx에서 직접 설정할 수 있음

NginX 설정 예시

```
server {
    listen       80;
    server_name  example.com;
    root         html;

    location / {
        return 301 https://example.com$request_uri;
    }
}


server {
    listen       443;
    server_name  example.com
    root         html;


    ssl                  on;
    ssl_certificate      /etc/pki/tls/certs/example.com.chained.crt;
    ssl_certificate_key  /etc/pki/tls/private/example.com.key;
    ssl_session_timeout  5m;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
    ssl_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH';
    ssl_prefer_server_ciphers   on;
    location ~ /\.ht {
         deny  all;
    }
}
```
