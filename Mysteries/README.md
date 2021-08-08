# 일단 큰 문제는 없어 넘어갔는데, 꼭 알고싶은 개념

- Network
  - TCP연결은 어떻게 성립되는가? 어떤 소프트웨어가 관여하는가? OSI 네트워크의 각 레이어마다 담당하는 소프트웨어 혹은 하드웨어?
- Web
  - WSGI에서는 어떻게 web socket연결을 할 수 있었던 것일까?
  - 웹 서버에, 웹 소켓 기능을 붙인다는 얘기는, 웹 소켓 서버를 붙인다는 것과 동치인가?
  - gunicorn의 역할과, eventlet등의 효과?
  - 웹어셈블리가 뭐지?

## Network

### TCP연결은 어떻게 성립되는가? 어떤 소프트웨어가 관여하는가? OSI 네트워크의 각 레이어마다 담당하는 소프트웨어 혹은 하드웨어?

https://d2.naver.com/helloworld/47667

## Web

### WSGI에서는 어떻게 web socket연결을 할 수 있었던 것일까?

- 애초에 web socket은 WSGI에는 붙일 수 없는건가?

### 웹 서버에, 웹 소켓 기능을 붙인다는 얘기는, 웹 소켓 서버를 붙인다는 것과 동치인가?

### gunicorn의 역할과, eventlet등의 효과?

- gunicorn
  - 개요
    - UNIX를 위한 파이썬 WSGI HTTP서버
  - 특징
    - WSGI 서포트
    - 자동 워커 프로세스 관리(pre-fork 모델)
      - 하나의 mother process, 여럿의 worker process
    - configuration이 간단함
  - workers
    - sync workers
      - 한번에 하나의 request를 처리
    - async workers
      - eventlet or gevent에 기반하여 사용가능
        - coroutine기반

### 웹 어셈블리가 뭐지?
