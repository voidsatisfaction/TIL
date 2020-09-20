# Web 관련 용어 정리

- 의문
- HTML
  - Document Object Model(DOM)
  - Document(interface)
  - Origin
  - Same-origin policy
  - CORS
  - Iframe(HTML Inline Frame Element)
  - Referer
- Server
  - WSGI
- JS
  - ArrayBuffer

## 의문

- Cross origin error는 어디에서 generate되는 것일까?
  - 서버?
  - 브라우저?
    - 브라우저이다.
- CORS동작에서 preflight request를 보내는 주체는 누구인가?
  - 브라우저일듯

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

### CORS(Cross-Origin Resource Sharing)

Preflight request sequence diagram

![](./images/web/cors_preflight_sequence1.png)

Preflight Cross-Origin HTTP request, response header의 예시

```
OPTIONS /doc HTTP/1.1
Host: bar.other
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Connection: keep-alive
Origin: http://foo.example

# actual request가 보내질 때에는 POST 리퀘스트 메소드를 사용
Access-Control-Request-Method: POST

# actual request가 보내질 때, X-PINGOTHER, Content-Type 커스텀 헤더를 포함시킬 것
Access-Control-Request-Headers: X-PINGOTHER, Content-Type

#######
# 서버가 위 CORS request를 보고 받아들이지 말지 판단 가능
#######

HTTP/1.1 204 No Content
Date: Mon, 01 Dec 2008 01:15:39 GMT
Server: Apache/2

# 서버의 CORS Access control에 관한 정보
Access-Control-Allow-Origin: https://foo.example

# POST, GET method로 주어진 자원 query가능함
Access-Control-Allow-Methods: POST, GET, OPTIONS

# 해당 자원을 query할 때, 사용 가능한 헤더
Access-Control-Allow-Headers: X-PINGOTHER, Content-Type

# preflight request에 대한 response를 얼마나 캐시 가능한지(86400초 = 24시간)
Access-Control-Max-Age: 86400

Vary: Accept-Encoding, Origin
Keep-Alive: timeout=2, max=100
Connection: Keep-Alive
```

Real Cross-Origin HTTP request, response header의 예시

```
POST /doc HTTP/1.1
Host: bar.other
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Connection: keep-alive
X-PINGOTHER: pingpong
Content-Type: text/xml; charset=UTF-8
Referer: https://foo.example/examples/preflightInvocation.html
Content-Length: 55
Origin: https://foo.example
Pragma: no-cache
Cache-Control: no-cache

<person><name>Arun</name></person>


HTTP/1.1 200 OK
Date: Mon, 01 Dec 2008 01:15:40 GMT
Server: Apache/2
Access-Control-Allow-Origin: https://foo.example
Vary: Accept-Encoding, Origin
Content-Encoding: gzip
Content-Length: 235
Keep-Alive: timeout=2, max=99
Connection: Keep-Alive
Content-Type: text/plain

[Some XML payload]
```

- 정의
  - 브라우저가 어떤 origin에서 동작하는 웹 애플리케이션에게 다른 origin에 존재하는 자원의 접근권을 주기 위한 추가적인 HTTP 헤더를 사용하는 매커니즘
  - e.g
    - `https://domain-a.com`로부터 서빙된 js코드가 `XMLHttpRequest`를 사용해서 `https://domain-b.com/data.json` 자원을 요청하는 경우
- 특징
  - 브라우저가 기본적으로 cross-origin HTTP request를 막음
    - 다른 origin으로부터의 response가 올바른 CORS 헤더를 갖고 있어야지만 자원을 사용할 수 있게 함
    - 같은 origin자원으로의 요청은 항상 허락됨
  - credentials(XMLHttpRequest)
    - actual request를 credential을 이용해서 보낼 수 있는지 여부 확인
      - **쿠키를 사용하는 경우에 필요!**
      - `HTTP cookies` or `HTTP Authentication information`을 이용
    - cross-site XMLHttpRequest는 default로는 브라우저가 credentials(쿠키 등)을 보내지 않음
      - `const invocation = new XMLHttpRequest();`
      - `invocation.withCredentials = true`로 설정해야 Cookie도 같이 전송함
    - 서버에서는 `Access-Control-Allow-Credentials`를 true로 설정해주어야 함
    - 서버에서는 반드시 `Access-Control-Allow-Origin` 헤더 필드를 설정해주어야 함(`*` 제외)
- CORS 대상
  - `XMLHttpRequest` or `Fetch API`
  - web fonts
  - webGL textures
  - Images/video frames
  - CSS Shapes from images
- 동작
  - 서버가 웹 브라우저로부터 어떤 origin이 해당 정보를 접근할 수 있도록 허용할 것인지 작성된 추가적인 HTTP header를 더해야 CORS 표준이 동작함
  - \[preflight\]
    - server data에 side-effect를 일으킬 수 있는 HTTP request method에 대해서, CORS 스펙은 browser에게 preflight request를 보내도록 함(Simple request는 해당하지 않음)
      - 미리 한 번 request가능한지 체크
    - simple request의 조건
      - Http Method
        - `GET`, `HEAD`, `POST`
      - User agent로 인해서 자동적으로 선택된 헤더 & CORS-safelisted request-header들 만 헤더필드에 존재해야 함
        - `Accept`
        - `Accept-Language`
        - `Content-Language`
        - `Content-Type`
          - `application/x-www-form-urlencoded`
          - `multipart/form-data`
          - `text/plain`
        - ...
      - `XMLHttpRequestUpload` 오브젝트에 이벤트 리스너가 존재하지 않아야 함
      - `ReadableStream`이 리퀘스트에서 사용되지 않아야 함
  - 서버로부터 approval을 받은 이후에는 실제 request를 보냄
    - 서버는 `credential`을 requests와 같이 보내도록 강제할 수 있음
      - Cookie나 HTTP Authorization
  - CORS 실패는 에러를 나타내나, 보안적인 이유로, js에서 error를 사용할 수 없음
    - 코드상으로는 그저 에러가 났다는 것만 알 수 있음
    - 브라우저 콘솔상에서만 확인 가능

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

## JS

### ArrayBuffer

- 정의
  - *generic*, fixed-length raw 바이너리 데이터 버퍼를 나타낼 때 사용됨
  - array of bytes
    - 다른 언어에서는 byte array와 유사
- 특징
  - 직접 수정할 수 없음
    - `typed array object`를 생성하거나 `DataView` 라는 특정 포맷의 버퍼 오브젝트를 생성해서 buffer를 read, write할 수 있음
  - 이미 존재하는 데이터로부터 array buffer를 얻을 수 있음
    - Base64 string
    - local file

### Source map

- 정의
  - minified나 coffeeScript, TypeScript와 같은 언어로부터 컴파일된 js의 경우, debug할 때, 기존 소스에 기반하여 할 수 있도록 도와주는 파일
    - original source <-(map)-> transformed source
- 사용법
  - source map을 생성
  - transformed file에 source map의 경로를 지정
    - `//# sourceMappingURL=http://example.com/path/to/your/sourcemap.map`
