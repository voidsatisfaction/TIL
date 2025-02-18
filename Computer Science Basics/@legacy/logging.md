# Logging (in python)

- 의문
- 개요
- The Logging Module
- Root Logger Configurations
- Formatting the Output
- Custom logger
- Other Configuration Methods

## 의문

## 개요

- 로깅의 중요성
  - 정보 저장의 기능
    - 어떤 유저, IP access
  - 에러 대응
    - stack trace + 에러가 나기 직전의 프로그램의 state
  - 애플리케이션 퍼포먼스 분석
  - 사용 패턴 분석

## The Logging Module

- 개요
  - 파이썬 내장 라이브러리가 제공하는 로깅 모듈
- 5 level(severity)
  - `DEBUG`
  - `INFO`
  - `WARNING`
  - `ERROR`
  - `CRITICAL`

## Root Logger Configurations

- 개요
  - `basicConfig(**kwargs)` 메서드를 이용해서 root logger의 설정 가능
  - [주요 사용 파라미터](https://docs.python.org/3/library/logging.html#logging.basicConfig)
    - `level`
      - root logger를 특정 severity level로 설정
      - 설정된 level 이상의 로그는 전부 출력됨
    - `filename`
      - 파일을 특정함
    - `filemode`
      - `filename`을 지정한 경우, `filemode`에서 지정한 모드로 염
      - `a`(append)로 설정되는게 기본
    - `format`
      - log message의 포맷
- 주의
  - **`basicConfig()`를 이용한 root logger의 configuration은 과거에 root logger가 configured되지 않았을 때에만 가능**
    - 즉, 이 함수는 오직 한 번만 호출 가능
    - `debug()`, `info()`, `warning()`, `error()`, `critical()` 역시 `basicConfig()`를 자동적으로 호출함(과거에 실행하지 않았다면)
      - 결국, 이 함수를 실행하기 전에 `basicConfig`를 해줘야지 root logger에 설정이 반영됨

간단한 로깅 예시

```py
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

# 실행하면, app.log 라는 파일에 로그가 저장됨
# filemode가 w이므로, 항상 내용이 덮어씌워짐. a로해야지 계속해서 로그가 추가됨
```

## Formatting the Output

- 기본적인 `LogRecord`의 attribute가 있어서, log message formatting에 사용할 수 있음
  - 사용 가능한 요소
    - `%(process)d`
    - `%(levelname)s`
    - `%(asctime)s`
      - basicConfig의 `datefmt` 옵션으로 어떤식으로 datetime을 나타낼 것인지 적용 가능

### Logging Variable Data

- 방법
  - `logging.error('%s raised an error', name)`
  - `logging.error(f'{name} raised an error')`

### Capturing Stack Traces

stack trace logging 예시

```py
import logging

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logging.error('Exception occured', exc_info=True)

"""
ERROR:root:Exception occurred
Traceback (most recent call last):
  File "exceptions.py", line 6, in <module>
    c = a / b
ZeroDivisionError: division by zero
[Finished in 0.2s]
"""
```

- `logging.exception()`
  - level을 `ERROR`로 설정한 뒤, stack trace를 기록
- c.f)
  - `sys.exc_info()`
    - 현재 다뤄지고 있는(현재 스레드 / 현재의 stack frame) exception의 세가지 값들을 반환
      - `(type, value, traceback)`
      - `type`
        - `BaseException`의 서브클래스인 예외의 type
      - `value`
        - exception instance(`type`의 인스턴스 그 자체)
      - `traceback`
        - exception이 어디에서 일어났는지를 알려주는 call stack을 캡슐화한 `traceback object`

## Custom logger

custom logger작성의 예시

```py
import logging

logger = logging.getLogger(__name__)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')
```

- logging 모듈에서 자주 쓰이는 클래스들
  - `Logger`
    - 이 클래스의 instance가 우리가 실제로 다루는 application code에서 직접 logging관련 메서드를 호출함
  - `LogRecord`
    - Logger가 자동적으로 생성하는 오브젝트
      - log되는 이벤트에 관련있는 정보를 갖고 있음(logger 이름, 함수, line number, message 등)
  - `Handler`
    - LogRecord를 output destination(console, file)으로 전달
    - `StreamHandler`, `FileHandler`, `SMTPHandler`, `HTTPHandler` ...과 같은 subclass의 base가 됨
      - 각 subclass는 `sys.stdout`이나 `disk file`등으로 output을 logging함
  - `Formatter`
    - output을 string format으로 지정해서 format을 결정하는 곳
- custom logger
  - 보통 위의 클래스들 중에서 `Logger`클래스의 object를 대부분 다루게 됨
    - Logger 클래스의 object는 `logger.getLogger(name)`으로 생성할 수 있음
      - root logger와는 다르게 이름을 지정해줘야 함
      - 일반적으로, `logger.getLogger(__name__)`으로 설정해 주는 것이 관례(현재의 모듈의 이름을 명시)
  - `basicConfig()`메서드로 설정할 수 없고, `Handlers`와 `Formatters`로 설정해야 함
- Handler 사용하기
  - 개요
    - 로그가 생성될때 마다 다양한 장소로 보내주고 싶을 때 사용
      - `stdout`, `file`, `HTTP`, `SMTP(email)`
    - 로거 하나에 한개 이상의 핸들러를 만들 수 있음
    - severity level을 설정해서, 각 handler마다 다른 severity level로 logging할 수 있도록 함

## Other Configuration Methods

file configuration을 이용한 logger 작성의 예시: Config 파일1

```
[loggers]
keys=root,sampleLogger

[handlers]
keys=consoleHandler

[formatters]
keys=sampleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_sampleLogger]
level=DEBUG
handlers=consoleHandler
qualname=sampleLogger
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=sampleFormatter
args=(sys.stdout,)

[formatter_sampleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
```

file configuration을 이용한 logger 작성의 예시: Config 파일1

```yaml
version: 1
formatters:
  simple:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: simple
    stream: ext://sys.stdout
loggers:
  sampleLogger:
    level: DEBUG
    handlers: [console]
    propagate: no
root:
  level: DEBUG
  handlers: [console]
```

file configuration을 이용한 logger 작성의 예시: python 코드

```py
import logging
import logging.config

# conf 파일의 경우
logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

import logging
import logging.config
import yaml

# yaml 파일의 경우
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
```
