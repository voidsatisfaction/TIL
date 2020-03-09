# Flask

- 의문
- Request Context
- Application Context

## 의문

## Request Context

### 개요

- request context는 request-level 데이터를 한 request life cycle 동안에 계속 추적(사용)
  - request관련 작업을 할 때, request object를 동작을 하기 위한 각각의 함수에 인자로 넘겨주는 대신, **request와 session 프록시에 대신 접근할 수 있음**
- request context가 push될 때, application context도 push됨

### Context의 목적

- Flask application이 한 리퀘스트를 다룰 때, WSGI 서버로부터 전달받은 환경(environment)에 기반해서 Request 오브젝트를 생성
  - 하나의 worker(thread, process, coroutine 등... 서버에 따라서 다름)는 오직 한번에 하나의 request만 핸들링할 수 있으므로, request data는 각 worker에 있어서 request 도중에는 global 이라고 간주할 수 있음(flask에서는 context local 이라는 단어를 사용)
- **Flask는 한 request를 다룰 때, 하나의 request context를 푸시함**
- 따라서, `View functions`, `error handlers`, 한 request동안 실행되는 `other functions`에서는 request proxy에 접근할 수 있게 되고, 해당 request proxy는 current request의 request object를 가리킨다

### Lifetime of the Context

- Flask 애플리케이션이 request를 다룸 -> request context를 푸시 -> application context도 푸시 -> request가 끝나면 두 context를 pop
- context는 각 thread(혹은 worker type)마다 unique
  - request는 다른 스레드에 패스될 수 없음
- context local은 `Werkzeug`에서 구현됨

### 컨텍스트의 수동 푸시

- request context 바깥에서, `request`에 접근하거나, request를 사용하는 무엇인가에 접근하면, `RuntimeError: Working outside of request context` 에러 메시지를 받음
  - 일반적으로 code를 테스트할 때 발생
    - `test_client`를 full request를 사용해서 해결
    - `with test_request_context()`를 사용해서 해결
  - 이러한 에러를 보게 되면, code를 view function으로 두어야 한다는 것을 의미

### Context가 동작하는 원리

- `Flask.wsgi_app()` 메서드는 각 리퀘스트를 다루기 위해서 호출됨
  - request도중의 context를 다룸
  - request / application context는 스택으로 동작
    - `_request_ctx_stack`
    - `_app_ctx_stack`
  - 컨텍스트들이 stack에 푸시되면, stack에 의존하는 proxies들이 사용가능해지고, 스택의 top context에 있는 정보를 가리키게 된다
- 리퀘스트가 시작
- `RequestContext`가 생성되고, 푸시됨, 그리고 이전에 application context가 top context가 아니면 같이 푸시해줌
  - 컨텍스트가 푸시되어 있는 동안, `current_app`, `g`, `request`, `session`과 같은 프록시가 해당 리퀘스트를 처리하는 스레드에서 사용 가능함
  - 컨텍스트가 stack이기 때문에, 하나의 리퀘스트 도중에 다른 컨텍스트가 푸시되어, proxies를 변화시킬 수 있음
    - 내부 redirects
    - 다른 애플리케이션을 체인하는 경우
- request, response 처리
- request context가 pop
- `teardown_request()` 실행
  - `teardown` 함수들은 unhandled exception이 일어나도 실행됨
- application context가 pop
- `teardown_appcontext()` 실행

### Callback과 Error

- Blueprint
  - 개요
    - blueprint에서 지정한 특정 이벤트들에 핸들러들을 추가할 수 있음
    - 핸들러들은 blueprint가 요청에 일치하는 라우트를 갖고 있을 때, 동작함
  - 종류 및 처리 순서
    - `before_request()`
      - 이곳에 부착된 핸들러는, 값을 반환하면 다른 함수들이 스킵되고, 그것이 그대로 서버의 response로 취급됨
    - `view function`이 동작
    - `after_request()`
      - view의 반환 값이 실제의 response object로 변환되고, `after_request()`함수들로 넘겨짐
    - `teardown_request()` / `teardown_appcontext()`
      - response가 반환된 다음, context가 pop되기 전에 실행됨
    - 참고
      - `errorhandler()`는 exception을 다루고 response를 반환
        - 아무것도 지정이 안되어있으면 `500 Internal Server Error`를 반환

Flask API 테스트 방법(defer exit context)

```py
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    print('during view')
    return 'Hello, World!'

@app.teardown_request
def show_teardown(exception):
    print('after with block')

with app.test_request_context():
    print('during with block')

# teardown functions are called after the context with block exits

with app.test_client() as client:
    client.get('/')
    # the contexts are not popped even though the request ended
    print(request.path)

# the contexts are popped and teardown functions are called after
# the client with block exits
```

### Signals

- `signals_available`이 true이면 다음 시그널들이 보내짐
  - `request_started`가 `before_request()`함수 실행 전에
  - `request_finished`가 `after_request()`함수 실행 전에
  - `got_request_exception`이 `errorhandler()`가 호출되기 전에
  - `request_tearing_down`이 `teardown_request()`가 호출되기 전에

### Context Preservation on Error

- `FLASK_ENV='development'`인 경우에, pop되어야 할 request context가 보존됨

### Proxies에 대한 Note

- 몇몇 Flask가 제공하는 object들은 다른 오브젝트들의 프록시이다.
- 프록시들은 각각의 워커 스레드마다 같은 방식으로 접근할 수 있으나, 서로 unique한 오브젝트를 가르킨다.
- 대부분의 경우 이와 같은 사실을 신경 쓸 필요가 없으나, 다음과 같은 경우에는 이러한 오브젝트가 프록시임을 인지하는 것이 좋다
  - proxy 오브젝트는 그들의 type을 실제의 object type처럼 fake할 수 없음
  - The reference to the proxied object is needed in some situations, such as sending Signals or passing data to a background thread.
  - 프록시로 가려진 오브젝트에 접근할 때에는 `_get_current_object()`메서드를 사용

## Application Context
