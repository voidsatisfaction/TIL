# 웹 소켓

- 의문
- 개요
- 프로토콜 핸드셰이크
- Nginx에서 웹 소켓 설정하기

## 의문

## 개요

- **TCP 접속에 전이중 통신(duplex) 채널을 제공하는 컴퓨터 통신 프로토콜**
  - 참고
    - Full duplex(전이중 통신)
      - 두 대의 단말기가 데이터를 송수신하기 위해 동시에 각각 독립된 회선을 사용하는 통신 방식
    - Half duplex(반이중 통신)
      - 한 쪽이 송신하는 동안 다른 쪽에서 수신하는 통신 방식으로, 전송 방향을 교체함
    - Simplex(단방향 통신)
- 특징
  - **HTTP포트 80과 443 위에 동작하도록 설계**
  - HTTP프록시 및 중간 층을 지원하도록 설계되었으므로, HTTP 프로토콜과 호환 가능
    - HTTP 업그레이드 헤더 사용(HTTP 프로토콜에서 웹소켓 프로토콜로 변경)
  - 양방향 대화 가능
  - HTTP 헤더 부하 문제 해결
  - `ws://`, `wss://` 스킴을 사용하여, 웹 소켓 프로토콜임을 명시
    - `wss://`는 TLS를 사용했음을 보여줌

## 프로토콜 핸드셰이크

클라이언트 웹소켓 핸드셰이크 요청

```
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==
Sec-WebSocket-Protocol: chat, superchat
Sec-WebSocket-Version: 13
Origin: http://example.com
```

서버 웹소켓 핸드셰이크 응답

```
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: HSmrc0sMlYUkAGmm5OPpG2HaGWk=
Sec-WebSocket-Protocol: chat
```

## Nginx에서 웹 소켓 설정하기

nginx socket.io config파일 설정 예시

```Nginx
# in the http{} configuration block
upstream socket_nodes {
    ip_hash;
    server srv1.app.com:5000 weight=5;
    server srv2.app.com:5000;
    server srv3.app.com:5000;
    server srv4.app.com:5000;
}

server {
    server_name app.domain.com;
    location / {
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_http_version 1.1;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_pass http://socket_nodes;
    }

    location /assets {
        alias /path/to/assets;
        access_log off;
        expires max;
    }
}
```
