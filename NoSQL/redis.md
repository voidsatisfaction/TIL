# Redis

- 의문
- Pub/Sub
  - Redis Pub/Sub
- Redis Protocol specification

## 의문

## Pub/Sub

- 개요
  - publisher는 특정 subscriber로 메시지를 보내는 것이 아닌, 채널들로 분배가 되고, 퍼블리셔는 어떤 서브스크라이버들이 있는지 모름
  - 서브스크라이버는 하나 이상의 채널을 구독하고, 해당 채널에서의 메시지를 수신받고, 퍼블리셔들에 대해서는 지식이 없음
- 특징
  - 파블리셔와 서브스크라이버의 디커플링이 scalability와 dynamic network topology를 허락해줌

### Redis pub/sub

- 개요
  - 다른 클라이언트에 의해서 특정 채널로 보내진 메시지가 다른 모든 서브스크라이빙 하는 클라이언트로 푸시될것임

## Redis Protocol specification

- 개요
  - redis 클라이언트가 서버와 상호작용하기 위한 프로토콜
    - 정수, 문자열, 배열 직렬화 가능
- 특성
  - 구현 간단함
  - 파싱이 빠름
  - 사람이 읽을 수 있음
- 특징
  - request
    - 실행할 명령어의 인수를 나타내는 문자열 배열로 클라이언트에서 Redis 서버로 보내짐
  - response
    - 명령별 데이터 유형으로 응답
  - 접두사 길이 사용
- 네트워킹 레이어
  - TCP or Unix socket
- 리퀘스트 - 리스폰스 모델
