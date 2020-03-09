# Flask

- 의문
- Request Context
- Application Context

## 의문

## Request Context

### 개요

- requet context는 request-level 데이터를 한 request 동안에 계속 추적(사용)
  - request object를 request를 하는 동안에 각각의 함수에 인자로 넘겨주는 대신, **request와 session 프록시에 대신 접근할 수 있음**
- request context가 push될 때, application context가 push됨

### Context의 목적

- Flask application이 한 리퀘스트를 다룰 때, WSGI 서버로부터 전달받은 환경(environment)에 기반해서 Request 오브젝트를 생성
  - 하나의 worker(thread, process, coroutine 등... 서버에 따라서 다름)는 오직 한번에 하나의 request만 핸들링할 수 있으므로, request data는 각 worker에 있어서 request 도중에는 global 이라고 간주할 수 있음(flask에서는 context local 이라는 단어를 사용)
- **Flask는 한 request를 다룰 때, 하나의 request context를 푸시함**
- 따라서, `View functions`, `error handlers`, 한 request동안 실행되는 `other functions`에서는 request proxy에 접근할 수 있게 되고, 해당 request proxy는 current request의 request object를 가리킨다

## Application Context
