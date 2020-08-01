# Web 관련 용어 정리

- 의문
- HTML
  - Document Object Model(DOM)
  - Document(interface)
  - Origin
  - Same-origin policy
  - Iframe(HTML Inline Frame Element)
  - Referer
- Server
  - WSGI

## 의문

- Cross origin error는 어디에서 generate되는 것일까?
  - 서버?
  - 브라우저?
    - 아마 브라우저 같은것이, Server에서 response header만 설정해주면 동작이 제대로 되기 떄문

## HTML

### Document Object Model(DOM)

- 정의
  - 메모리속에서 웹 페이지를(e.g HTML), document의 구조를 표현함으로써, scripts or 프로그래밍 언어와 연결하는 것
- 구조
  - logical tree
    - branch는 하나의 node에서 끝남
    - 각 node는 object들을 포함
    - DOM method는 tree에 programmatic access를 가능하게 함
      - 그것들을 가지고, document의 구조, 스타일, 내용을 변화시킬 수 있음
    - node는 event handler를 갖을 수 있음
- HTML DOM
  - HTML을 포함하는 document는 `Document` 인터페이스를 사용해서 나타나짐
    - HTML-specific 기능을 포함하기 위해서 확장된 Document
    - 특히 `Element` interface가 강화됨
  - tab, windows, css style, browser history를 비롯한 다양한 브라우저 기능에 접근 가능

### Document(interface)

- 정의
  - 브라우저에 로드된 웹 페이지를 나타내는 인터페이스 ∧ **DOM tree인 웹 페이지 컨텐츠에 대한 entry point역할을 함(root node)**
    - e.g) 엔트리 포인트 역할: `document.getElementById('....')`
- 특징
  - DOM tree는 `<body>`, `<table>` 등의 태그를 포함하며, 페이지의 URL을 가져오는 것, 새로운 element를 생성하는 등의 기능을 제공
  - Document 인터페이스는 common properties와 methods를 기술
  - document의 type에 따라서, 서로 다른 범위의 API가 사용 가능
    - `text/html`
      - `HTMLDocument` interface
    - `XML`, `SVG`
      - `XMLDocument` interface

### Origin

- 정의
  - URL의 scheme(protocol), host(domain), port까지를 결합한 것
- 특징
  - 같은 origin
    - scheme, host, port가 모두 일치하는 경우
- origin 예시
  - 다른 경우
    - different schemes
      - `http://example.com/app1`
      - `https://example.com/app2`
    - different hosts
      - `http://example.com`
      - `http://www.example.com`
      - `http://myapp.example.com`

### Same-origin policy

자원에 대한 AC(Access Control) policy

- 정의
  - 하나의 origin으로 부터 로드 된 document나 script가 어떻게 또 다른 origin으로 부터의 자원과 상호작용하는가에 대한 내용을 제한하는 보안 매커니즘
- 특징
  - Origin 변환
    - 정의
      - 페이지는 자신의 origin을 제한조건 속에서 변환 가능
        - `document.domain`을 현재의 도메인 혹은 superdomain으로 변경 가능(js)
  - Cross-origin network access
    - 정의
      - same-origin policy는 서로다른 두 origin 자원 사이에서 상호작용하는 것을 제어할 수 있음
      - e.g)
        - `XMLHttpRequest`, `<img>` element
    - cross origin 상호작용의 종류
      - *각 상호작용은 writes, embedding, reads*로 나뉘어지는데, 구체적으로 무슨 기준인것인가?
      - Cross-origin writes
        - 일반적으로 허용됨
        - e.g)
          - 링크, 리다이렉트, form submission
      - Cross-origin embedding
        - 일반적으로 허용됨
        - e.g)
          - `<script src="..."></script>`
            - syntax error에 대한 detail은 same-origin script에서만 볼 수 있음
          - `<link rel="stylesheet" href="...">`
            - `Content-Type` header가 올바르게 설정되어있어야 함
          - `<img>`로 나타나진 image들
          - `<object>` or `<embed>`로 embedded된 외부 자원
          - `@font-face`가 적용된 font들
          - `<iframe>`에 의해서 embedded된 모든 것
            - `X-Frame-Options` 헤더를 사용해서 cross-origin framing을 막을 수 있음
      - Cross-origin reads
        - 일반적으로 허용되지 않음
          - 가끔씩 embedding에 의해서 leaked됨
        - e.g)
          - embedded된 이미지의 차원을 읽을 수 있음
          - embedded된 스크립트의 액션
          - embedded된 자원의 가용성
    - [cross-origin script API access](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)
      - `Window`
        - method
          - `window.blur`
          - `window.close`
          - `window.focus`
          - `window.postMessage`
            - 서로 다른 origin 자원(document, scripts)사이에서 communication할 때 사용하는 메서드
        - attributes
          - `window.closed`
          - `window.frames`
          - ...
      - `Location`
        - methods
          - `location.replace`
        - attributes
          - `URLUtils.href`
      - Cross-origin data storage access
        - 개요
          - web storage, indexedDB에 저장된 데이터는 origin마다 격리되어 있음
            - 다른 origin의 js에서 접근 불가능
        - c.f) 쿠키
          - 다른 개념의 origin을 사용
            - 하나의 페이지는 자신의 domain 뿐 아니라, 임의의 parent domain으로 설정 가능(대신, public suffix가 아니어야 함)
- 서버 입장에서
  - Cross-origin access를 허락하는 방법
    - `CORS`(Cross-Origin Resource Sharing)를 사용하면 됨
    - **`CORS`는 서버로부터 어떠한 호스트가 content를 가져올 수 있도록 허가되었는지 명시한 HTTP의 일부분**
  - Cross-oirign access를 막는 방법
    - *request에서 CSRF라고 불리는 예측이 불가능한 토큰을 확인*
      - 이 토큰을 요구하는 페이지의 읽기를 막아야만 함
      - *정확히 무슨 뜻인지?*
    - 자원이 embeddable하지 않은 것을 확실하게 해야함

### Iframe(HTML Inline Frame Element)

- 정의
  - 현재의 HTML에 또 다른 HTML page를 embedding하는 nested된 browsing context
  - c.f) browsing context
    - 정의
      - 브라우저가 Document를 나타내는 environment
    - 특징
      - 현대 브라우저에서는 tab, window의 부분(`frame`, `iframe`)등이 될 수 있음
      - 각각의 browsing context는 specific origin을 갖고 있음
        - active document의 origin과 표시된 document들의 히스토리 등
      - browsing context 사이의 커뮤니케이션은 엄격하게 제한됨
        - same origin의 경우, `BroadcastChannel`을 사용해서 커뮤니케이션 가능
- 특징
  - 각각의 browsing context는 자신만의 session history, document를 갖음
  - parent browsing context
    - 다른 browsing contexts를 embed하는 browsing context
    - topmost browsing context는 `Window` 오브젝트라고 함
- Scripting
  - `<frame>` 요소들은 `window.frames` pseudo-array에 포함됨
  - script는 framed 자원의 `window`오브젝트를, `contentWindow` 속성을 이용해서 접근 가능
  - script는 framed 자원의 `document`오브젝트를, `contentDocument` 속성을 이용해서 접근 가능
  - frame 속에서, 스크립트는 `window.parent`를 이용해서 parent window 접근가능
  - frame의 자원 접근은 same-origin 정책에 종속됨
    - 서로 다른 origin의 경우, 대부분의 `window`의 속성에 접근 불가
    - cross origin communication은 `Window.postMessage()`를 이용해서 가능

### Referer

- 정의
  - request header로서, 이전 웹 페이지의 주소를 포함하고, 그 뒤에 현재 요청된 페이지가 따라옴
    - 서버가 사람들이 어떤 페이지를 방문하는지 알 수 있게 함(analytics, logging, optimized caching 등)
- Referer를 사용하지 못하는 경우
  - referring resource가 file or data URI인 경우
  - An unsecured HTTP request is used and the referring page was received with a secure protocol (HTTPS).
    - *??*
- e.g)
  - `Referer: https://developer.mozilla.org/en-US/docs/Web/JavaScript`

## Server

### WSGI(Web Server Gateway Interface(WSGI))

- 정의
  - web server가 request를 파이썬으로 작성된 web application 혹은 framework로 포워딩 하기 위한 호출 컨벤션
    - 현재 버전은 1.0.1
- 배경
  - 2010년 이전에는, 다양한 파이썬 웹 프레임워크가 있었으나, 각 종류마다 지원하는 웹 서버가 달라서 사용가능한 웹 서버의 선택이 제한되었음
  - Java의 경우에는 servlet API가 다양한 웹 애플리케이션 프레임워크가 servlet를 지원하는 다양한 웹 서버에서 동작할 수 있었음
  - 그래서 WSGI라는 implementation-agnostic interface가 생겨남
- 구성
  - server <-> \[WSGI middleware\] <-> application

Example1: WSGI-compatible "Hello, World" application

```py
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    yield b'Hello, World\n'

# environ
## CGI environment variable들을 포함하는 딕셔너리. 그외에도 request parameters, metadata 도 포함

# start_response(status, response_headers)
## 호출할 수 있으며, status와 response_headers를 인자로 받을 수 있음

# yield b'Hello, World\n'
## iterable of byte strings
```

Example2: calling an application

```py
from io import BytesIO

def call_application(app, environ):
    status = None
    headers = None
    body = BytesIO()

    def start_response(rstatus, rheaders):
        nonlocal status, headers
        status, headers = rstatus, rheaders

    app_iter = app(environ, start_response)
    try:
        for data in app_iter:
            assert status is not None and headers is not None, \
                "start_response() was not called"
            body.write(data)
    finally:
        if hasattr(app_iter, 'close'):
            app_iter.close()
    return status, headers, body.getvalue()

environ = {...} # environ dict
status, headers, body = call_application(app, environ)
```
