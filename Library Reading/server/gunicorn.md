# gunicorn

- 의문
- 개요
  - 디자인
- 실행 흐름

## 의문

- *gunicorn이 pre-fork 모델을 사용하고, worker를 multiprocessing방식으로 관리한다고 할 때, 웹 소켓이 worker와 직접 연결되어 있는 경우, client에서 server로 message push하는 경우에는 일반적인 대응이 가능하나, server에서 client message로 broadcast하는 경우에는, 실제로 모든 클라이언트로 어떻게 broadcast할 수 있는가?*
  - 가설1: socket서버가 initialize하는 타이밍이 worker의 포크 전타이밍이라서, 모든 worker가 같은 socket서버 오브젝트를 공유함
- *gunicorn의 worker_class를 무엇으로 설정하든, pre-fork 모델은 유지되는가? worker_class가 적용되는 시점은 언제인가?*

## 개요

- UNIX를 위한 파이썬 WSGI HTTP 서버
- pre-fork worker model
- 다양한 파이썬 웹 어플리케이션과 호환 가능

### 디자인

- Server Model
  - 개요
    - **gunicorn은 pre-fork worker model 도입**
      - 중앙 master process와 worker process들의 집합
        - *Worker를 AsyncIO Worker등으로 설정해도 worker process를 따로 fork하는가?*
      - master process는 개별적인 클라이언트에 대해서 전혀 모름
      - 모든 requests, responses는 완전히 worker process들에 의해서 다뤄짐
  - 종류
    - Master
      - 간단한 루프
        - process signal을 listen하고 그에 따라서 반응함
          - TTIN, TTOU 시그널 => 동작하는 워커의 수를 늘리거나 줄임
          - CHLD => child process가 제거된 것을 의미하며, master process는 실패한 워커를 자동적으로 restart시킴
    - Worker
      - Sync Workers
        - 한번에 하나의 request를 처리함
      - Async Workers
        - Greenlets를 이용한 비동기 워커
      - Tornado Workers
        - Tornado framework를 사용할 때 사용되는 워커
          - *왜 이것만 따로 있는거지?*
          - WSGI를 따르지 않는다는듯 함
      - AsyncIO Workers
        - `gthread`
          - accepted connection은 thread pool에 connection job으로 추가됨
          - keepalive connections은 event를 기다리면서 루프로 돌아감
            - timeout 시간동안 아무일이 없으면 connection은 닫힘
        - `aiohttp`
- Choosing a Worker Type
- How Many Workers?
  - `(2 * num_cores) + 1`
- How Many Threads?

## 모듈 구조

TBD

## 실행 흐름

### 전체적

1. Option parsing / configuration
2. Load user made app
3. Master process start
4. Worker process fork

### 구체적

- `gunicorn -w 4 myapp:app`
  - `gunicorn.app.wsgiapp`
    - `WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]")`
    - `gunicorn.app.base:BaseApplication`
      - `BaseApplication.__init__(self, usage=None, prog=None)`
        - `self.do_load_config()`
          - `self.load_default_config()`
            - 말 그대로 default config를 설정
          - `self.load_config()`
            - commandline이나 configuration file로부터 받아온 config 설정
            - `self.init(parser, args, args.args)`
              - app에 대한 optional settings
    - `WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]").run()`
      - `gunicorn.app.base:Application`
        - `run()`
          - `super().run()`
      - `gunicorn.app.base:BaseApplication`
        - `run()`
          - `Arbiter(self)`
            - 앱 모듈을 load함
          - `Arbiter(self).run()`
      - `gunicorn.arbiter:Arbiter`
        - 워커 프로세스를 죽이거나 새로 만들어줘서 언제나 alive하게 유지함
        - `run()`
          - Main master loop
          - `self.start()`
            - arbiter를 initialize함. 필요하면 pidfile을 listening하고 pidfile을 세팅함.
            - 시스템 시그널을 queue로 받는 설정을 함
            - 서버에서 LISTEN할 서버 소켓을 생성
              - Unix socket or TCP socket
          - `self.manage_workers()`
            - spawning, killing하면서 필요한 만큼, worker의 숫자를 유지함
            - 현재 가지고 있는 워커의 수가 실제 워커의 수 보다 작은 경우
              - `self.spawn_workers()`
                - 개수의 차 만큼 워커를 더 생산
              - `self.spawn_worker()`
                - `pid = os.fork()`
                - `if pid != 0` (parent process의 경우)
                  - `self.Workers[pid] = worker, return pid`
                  - *parent process는 어떤식으로 프로세스를 유지하는가? 무한루프?*
                - `else:` (child process의 경우)
                  - `worker.pid = os.getpid()`
                  - `self.log.info('Booting worker with pid: %s', worker.pid)`
                  - `gunicorn.workers.base:Worker`
                    - 어떤 Worker type인지에 따라서, 동작이 다름
                      - geventlet, ggevent, gthread, gtornado, sync
                    - `worker.init_process()`
                      - reloader를 시작함
                      - `self.load_wsgi()`
                        - `self.wsgi = self.app.wsgi()`
                          - *흠 그런데, https://github.com/pallets/flask/blob/632f85b65354ad573bb33c54a0a9dd3ffcef371f/src/flask/app.py#L1984-L2034 에서 보면, 위에서 처럼 `self.app.wsgi()`가 아니고,`app` 자체를 wsgi callable로 호출하게 되어있는데 이것은 무슨일인지?*
                      - `self.run()`
                        - main run loop로 들어감
                      - `self.run_for_one()`
                        - `self.alive`가 참일 동안 계속 무한 루프 수행
                        - `self.notify()`
                          - 매 self.timeout 초 마다 반드시 호출해줘야 함. 호출하지 못하면 master process가 kill함
                            - request timeout handling인가 봄
                        - `self.accept(listener)`
                          - 커넥션을 accept함
                          - `client, addr = listener.accept()`
                          - `client.setblocking(1)`
                          - `util.close_on_exec(client)`
                          - `self.handle(listener, client, addr)`
                            - `parser = http.RequestParser(self.cfg, client)`
                            - `req = next(parser)`
                            - **`self.handle_request(listener, req, client, addr)`**
                              - 이 함수에서 web server가, parsed된 http request를 web application로 넘겨줘서 response를 생성하도록 processing함
                              - **`resp, environ = wsgi.create(req, client, addr, listener.getsockname(), self.cfg)`**
                                - response, environ 생성
                                - headers를 environ에 추가
                                  - HOST, SCRIPT_NAME, CONTENT_NAME, CONTENT_LENGTH, `wsgi.url_scheme`
                                - `gunicorn.http.wsgi:Response`
                              - **`respiter = self.wsgi(environ, resp.start_response)`**
                                - response iterator
                              - `resp.write_file(respiter)`
                              - `resp.close()`
                              - `respiter.close()`
                  - `sys.exit(0)`
                    - worker의 무한 루프가 끝나면 동작하도록 되어있음
            - 현재 가지고 있는 워커의 수가 더 많을 경우
              - `self.kill_worker(pid, signal.SIGTERM)`
