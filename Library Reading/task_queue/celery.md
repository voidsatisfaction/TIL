# celery

## 의문

- 왜 클래스를 아래와 같은 형식으로 import하는 것인지...?
  - `log_cls = 'celery.app.log:Logging'`
    - `symbol_by_name()`함수를 가지고 import를 하는데, 정적으로 import를 하는 것이 아니라, 사용자의 인터페이스 및 모듈 구조에 따라서 동적으로 모듈을 import해서 사용해야하는 경우가 있기 때문임
- *왜 `worker_init`의 리시버는 `multiprocessing.Pool`을 쓸 수 없는것인가?*
  - 진짜 안되는지 실험
  - `worker_init`실험
    - concurrency = 2인 경우 print 횟수
  - `worker_process_init`실험
    - concurrency = 2인 경우 print 횟수

## 기본 개념

- **`celery.app`**
  - Celery의 core, 모든 기능의 entry-point
- **`celery.loaders`**
  - configuration을 어떻게 읽을지 정하거나, worker가 시작하면 무엇이 일어나는지 정하거나, task가 언제 시작하고 끝나는지 등을 정함
    - app loader
      - custom celery app instance가 사용
    - default loader
      - single-mode에서는 이 로더를 default로 사용
- **`celery.worker`**
  - worker 구현체
  - 구조
    - consumer
      - kombu를 사용해서 broker로 부터 메시지 받아옴
    - timer
      - ETA-task를 스케쥴링하는 용도
    - taskpool
      - `multiprocessing.pool`를 살짝 변형
        - worker가 missing이면 새것으로 교체
  - 동작 순서
    - consumer가 kombu를 사용해서 broker로부터 메시지 받아옴
    - `celery.worker.request.Request` 오브젝트로 메시지 변환
    - 일반 task(ETA task가 아닌)는 execution pool 보내짐
    - worker로 task수행
- **`celery.backends`**
  - task 결과 backend
- **`celery.apps`**
  - 주된 user applications
    - worker
      - `celery.apps.worker`에 실제로 실행되는 워커가 존재
    - beat
      - 크론같이 일정 주기로 실행하는 워커
  - 이것의 command-line wrapper는 `celery.bin`에 존재
- `celery.bin`
  - command-line application
  - `setup.py`가 이것의 setuptools 엔트리 포인트를 생성
- `celery.db`
  - SQLAlchemy db result backend를 위한 데이터베이스 모델(`celery.backends.database`로 옮겨질 예정)
- `celery.events`
  - monitoring 이벤트들을 보내고 소비함
- `celery.security`
  - cryptographic digest들을 사용하는 serializer가 들어있음
- `celery.task`
  - task를 생성, worker들을 컨트롤하기 위한 single-mode interface
- **`celery.utils`**
  - Celery code base에서 사용되는 유틸리티 함수들
  - 파이썬 버전에 상관없이 compatible하게 만듬
- `celery.contrib`
  - 위의 namespace에 적합하지 않은 public코드들의 집합

## 실행 흐름

```py
def on_worker_init(self):
    """Called when the worker (:program:`celery worker`) starts."""

def on_worker_shutdown(self):
    """Called when the worker (:program:`celery worker`) shuts down."""

def on_worker_process_init(self):
    """Called when a child process starts."""
```

- `app = Celery('tasks', broker='pyamqp://guest@localhost//')`
- `@app.task`
- `def add(x, y): return x + y`
- `result = add.delay(4, 4)`
- `result.get(timeout=1)`
- `app.worker_main()`
  - `celery.bin.worker:worker.execute_from_commandline(argv)`
    - celery worker 프로그램을 argv를 갖고 실행
    - `self.setup_app_from_commandline(self, argv)`
      - 각종 preload_option들을 갖고 와서 오브젝트에 설정
      - `self.app`에 celery app 오브젝트 설정
  - `celery.bin.worker:worker.run()`
    - pool class를 import
    - `worker = self.app.Worker() = celery.app.base.Worker = celery.apps.worker:Worker` 이니셜라이징
      - `celery.worker.worker:WorkController`의 init 실행
      - `self.setup_instance(**self.prepare_args(**kwargs))`
        - 큐, 큐 제외 옵션, pidfile 등을 셋업
        - `self.setup_queues(queues, exclude_queues)`
        - `signals.worker_init.send(sender=self)`
          - **worker_init 시그널의 receiver가 호출되는 순간**
          - **worker_process_init** 시그널의 receiver가 호출되는 순간은 process_initializer가 실행되는 순간이다. 즉, worker process가 실행되는 순간
        - `self.concurrency = cpu_count()`
          - concurrency 설정
        - 로그 레벨 설정
        - eventloop 사용여부 설정 반영
        - initialize bootsteps
          - `self.pool_cls = _concurrency.get_implementation(self.pool_cls)`
            - prefork, solo, ...
          - `self.blueprint.apply`
    - `worker.start() = celery.worker.worker:WorkController.start()`
      - `self.blueprint.start(self)`
    - `worker.exitcode`
