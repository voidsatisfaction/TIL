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

### 개요

- 하나의 리퀘스트, CLI command, 다른 동작을 수행하는 동안의 application-level 데이터를 트래킹하는 컨텍스트
- 애플리케이션 자체를 각각의 함수에 인자로 던져주기 보다는, `current_app`, `g` 프록시가 대신 accessed됨
- request context와 비슷한 개념이며, request context가 푸시될 때, application context도 푸시됨

### Purpose of the Context

- Flask application object는 `config`와 같은 view와 CLI command에서 접근할 때 유용한 속성을 갖고 있음
- 그러나, `app`인스턴스를 모듈 안으로 `import`하는 것은 circular import issue를 불러 일으킴 / app factory pattern이나 재사용 가능한 blueprint나 extension을 사용할 때에는, import할 `app` 인스턴스조차 존재하지 않을 수 있음
- application context의 도입
  - `app`을 직접적으로 참조하기 보다는, `current_app` 프록시(현재 행동을 handling하는 애플리케이션을 가리킴)를 사용함
- **Flask는 리퀘스트를 핸들링할 때, 자동적으로 application context를 푸시**
  - 하나의 리퀘스트 동안 실행되는 View functions, error handlers, other functions은 `current_app` 프록시에 접근 가능
  - 그런데, 이 얘기는 단순히 flask를 initialize할 때에는 application context가 푸시되지 않는 다는 말과 같음(리퀘스트 실행이 아니므로)
- Flask는 `@app.cli.command()`를 사용하는 Flask.cli와 함께 등록된 CLI commands를 실행할 때, 자동적으로 app context를 푸시

### Lifetime of the Context

- application context 바깥에서 `current_app`을 접근하거나, 그것을 사용하는 무엇인가를 접근할 때에는, `RuntimeError: Working outside of application context`와 같은 에러를 얻음
- 이러한 에러가 발생할 경우에는, `with app.app_context()`로 app context를 수동으로 푸시해줘야 함

### Storing Data

`g object`

- 배경
  - application context는 하나의 리퀘스트나 CLI command 동안에 공통 데이터를 저장하기에 좋은 장소
  - flask에서는 `g object`를 제공하고 있음
- 개요
  - `g object`는 application context와 같은 라이프타임을 갖는 간단한 네임스페이스 오브젝트
  - g는 하나의 context에서 글로벌하다는 것을 뜻함
    - *만약, 새로운 request context 혹은 application context가 thread.local에 push되면 기존의 g는 치환되는가?*
      - *application context와 같은 라이프타임을 갖으므로 아마 그럴듯?*
- 사용 예시
  - 일반적으로 한 리퀘스트 동안 resources를 다룸
    - `get_X()`
      - 자원 `X`가 존재하지 않으면 자원 `X`를 생성하고, `g.X`로 캐싱
    - `teardown_X()`
      - 자원이 존재하면, 자원을 close하거나 자원을 deallocate 함. `teardown_appcontext()`핸들러로 등록됨

g 오브젝트의 사용 예시 코드

```py
from flask import g

def get_db():
  if 'db' not in g:
    g.db = connect_to_database()

  return g.db

@app.teardown_appcontext
def teardown_db():
  db = g.pop('db', None)

  if db is not None:
    db.close()
```

위의 코드 설명

- 하나의 리퀘스트 동안, 모든 `get_db()` 호출은 같은 connection을 반환하고, request 종료시에 자동적으로 db close

`LocalProxy`를 사용한 새로운 `get_db()` 로부터의 context local

```py
from werkzeug.local import LocalProxy
db = LocalProxy(get_db)
```

`db` 오브젝트에 접근하면, `get_db` 함수가 내부적으로 호출됨(`current_app`과 같은 느낌)

### Events and Signal

- 애플리케이션은 애플리케이션 context가 pop될 때, `teardown_appcontext()`에 등록된 함수들을 호출할 것임
- `signals_available` 이 `true`면, 다음 시그널들이 보내짐 `appcontext_pushed`, `appcontext_tearing_down`, `appcontext_popped`
  - *시그널들이 보내지면 무엇을 할 수 있는것인지?, 시그널에 맞는 핸들러 등록이 가능한것인지?*

### Flask extension

- [Flask extension 개발](https://flask.palletsprojects.com/en/1.1.x/extensiondev/)
  - `g`는 유저가 사용하는 코드로 둬야 함
  - 컨텍스트를 만들어도 좋으나, 충분히 unique한 이름으로 만들어야 함
  - current context는 `_app_ctx_stack.top`으로 접근됨

Flask extension code의 예시
(middleware 같은 느낌인데, 일반적인 미들웨어가 request의 컨텍스트를 다루는 것이라면, Flask extension은 app자체의 컨텍스트를 다룸)

```py
import sqlite3
from flask import current_app, _app_ctx_stack


class SQLite3(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('SQLITE3_DATABASE', ':memory:')
        app.teardown_appcontext(self.teardown)

    def connect(self):
        # QUESTION
        # 왜 여기서는 current_app을 사용하고, connection에서는 _app_ctx_stack.top을 사용하는것인지?
        ## 여기서는 데이터를 참조만 하므로, current_app이 맞음
        ## connection 에서서는, application context 속의 cache를 수정하므로 stack에 직접 접근
        # 왜 self.app은 사용하지 않는 것인지?
        return sqlite3.connect(current_app.config['SQLITE3_DATABASE'])

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'sqlite3_db'):
            ctx.sqlite3_db.close()

    @property
    def connection(self):
        # 여기서 ctx는 application context
        # The internal LocalStack that holds AppContext instances. Typically, the current_app and g proxies should be accessed instead of the stack. Extensions can access the contexts on the stack as a namespace to store data.
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'sqlite3_db'):
                ctx.sqlite3_db = self.connect()
            return ctx.sqlite3_db

###### 참고 - flask src/flask/globals.py #######
def _lookup_req_object(name):
    top = _request_ctx_stack.top
    if top is None:
        raise RuntimeError(_request_ctx_err_msg)
    return getattr(top, name)


def _lookup_app_object(name):
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError(_app_ctx_err_msg)
    return getattr(top, name)


def _find_app():
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError(_app_ctx_err_msg)
    return top.app


# context locals
from functools import partial

from werkzeug.local import LocalProxy
from werkzeug.local import LocalStack

def _lookup_req_object(name):
    top = _request_ctx_stack.top
    if top is None:
        raise RuntimeError(_request_ctx_err_msg)
    return getattr(top, name)


def _lookup_app_object(name):
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError(_app_ctx_err_msg)
    return getattr(top, name)


def _find_app():
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError(_app_ctx_err_msg)
    return top.app

_request_ctx_stack = LocalStack()
# 스택에 직접 접속해서 attribute 수정 가능
_app_ctx_stack = LocalStack()
# Local Proxy 이기 때문에 참조만 가능
current_app = LocalProxy(_find_app)
request = LocalProxy(partial(_lookup_req_object, "request"))
session = LocalProxy(partial(_lookup_req_object, "session"))
g = LocalProxy(partial(_lookup_app_object, "g"))
```

extension code의 사용예시

```py
from flask import Flask
from flask_sqlite3 import SQLite3

app = Flask(__name__)
app.config.from_pyfile('the-config.cfg')
db = SQLite3(app)

# inside of a request
@app.route('/')
def show_all():
    cur = db.connection.cursor()
    cur.execute(...)

# If outside of a request
with app.app_context():
    cur = db.connection.cursor()
    cur.execute(...)
```
