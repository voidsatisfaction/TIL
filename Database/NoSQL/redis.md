# Redis

- 의문
- Pub/Sub
  - Redis Pub/Sub
- Redis Protocol specification
  - RESP(REdis Serialization Protocol) 개요
  - 타입
  - 서버로 커멘드 보내는 법
  - 특성
  - 특징
  - 네트워킹 방법

## 의문

- *binary safe의 의미는?*

## Pub/Sub

- 개요
  - publisher는 특정 subscriber로 메시지를 보내는 것이 아닌, 채널들로 분배가 되고, 퍼블리셔는 어떤 서브스크라이버들이 있는지 모름
  - 서브스크라이버는 하나 이상의 채널을 구독하고, 해당 채널에서의 메시지를 수신받고, 퍼블리셔들에 대해서는 지식이 없음
- 특징
  - 파블리셔와 서브스크라이버의 디커플링이 scalability와 dynamic network topology를 허락해줌

### Redis pub/sub

- 개요
  - 다른 클라이언트에 의해서 특정 채널로 보내진 메시지가 다른 모든 서브스크라이빙 하는 클라이언트로 푸시될것임
  - RESP를 사용하지만, client-server 모델은 아님

## Redis Protocol specification

- RESP(REdis Serialization Protocol) 개요
  - redis 클라이언트가 서버와 상호작용하기 위한 프로토콜
    - 정수(`:`), 문자열(`+`), 배열(`*`), 에러(`-`), bulk 문자열(`$`), Null 직렬화 가능
    - `\r\n`으로 메시지 전송을 끝낼 수 있음
- 타입
  - 문자열
  - RESP 에러
    - 문자열과 같으나, prefix가 `-`임
    - 클라이언트가 exception으로 처리하고, 에러 타입 그자체가 에러 메시지임
  - 정수
    - 예시
      - `:0\r\n`, `:1000\r\n`
    - 많은 레디스 커맨드는 RESP 정수를 반환함
      - `INCR`, `LLEN`, `LASTSAVE`
        - 해당 정수는 딱히 큰 의미는 없음
      - `EXISTS`, `SISMEMBER`
        - 1은 true, 0은 false
      - `SADD`, `SREM`, `SETNX`
        - 1은 수행된 경우, 0은 그 외
  - Bulk 문자열
    - binary safe인 512MB 길이까지의 문자열
    - 예시
      - `$6\r\nfoobar\r\n`
        - 6바이트, 내용은 foobar
      - `$0\r\n\r\n`
        - 0바이트, 내용은 비었음
    - Null 표현
      - `$-1\r\n`
        - null bulk string
        - 클라이언트는 빈 스트링이 아니고 nil 오브젝트를 반환해야 함
  - RESP 배열
    - redis 서버로 커멘드를 보내는 데에 사용
    - 굳이 모든 원소가 같은 타입은 아니어도 됨
    - 예시
      - `*0\r\n`
        - 빈 배열
      - `*2\r\n$3\r\nfoo\r\n$3\r\nbar\r\n`
        - 2개의 원소, 내용은 bulk 스트링 foo, bar
      - `*3\r\n:1\r\n:2\r\n:3\r\n`
        - 3개의 원소, 원소 1, 2, 3
    - Null 표현
      - `*-1\r\n`
    - 배열의 배열
      - `*2\r\n*3\r\n:1\r\n:2\r\n:3\r\n*2\r\n+Foo\r\n-Bar\r\n`
- 서버로 커멘드 보내는 법
  - 클라이언트는 Bulk String을 포함하는 RESP Array를 보냄
    - e.g) `*2\r\n$4\r\nLLEN\r\n$6\r\nmylist\r\n`
  - 서버는 클라이언트에게 유효한 RESP 데이터 타입을 응답으로 보냄
- 특성
  - 구현 간단함
  - 파싱이 빠름
  - 사람이 읽을 수 있음
- 특징
  - request
    - 실행할 명령어의 인수를 나타내는 bulk 문자열의 배열로 클라이언트에서 Redis 서버로 보내짐
  - response
    - 명령별 데이터 유형으로 응답
  - 접두사 길이 사용
- 네트워킹 방법
  - 네트워킹 레이어
    - TCP or Unix socket
      - RESP가 TCP를 사용해야만 하는것을 강제하는 것은 아닌데, TCP 연결로만 주고받곤 함
  - 리퀘스트 - 리스폰스 모델
    - 레디스 서버는 서로 다른 아규먼트로 구성된 커맨드를 받고, 해당 동작을 수행한 뒤에, 클라이언트로 다시 보냄
    - 예외
      - **파이프라이닝**
        - 여러개의 커맨드를 한번에 보내는 것이 가능
      - **pub/sub 채널을 클라이언트가 서브스크라이빙 하는 경우**
        - push protocol로 변화
          - 클라이언트는 sending커맨드를 보내지 않아도, 서버로부터 자동적으로 새 메시지를 받음
