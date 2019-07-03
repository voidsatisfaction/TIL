# Python

- 목차
  - 맨날 고생하는거
    - PYTHONPATH
  - 기본
    - 화이트 스페이스는 중요함
    - 모듈 불러오기
    - 리스트
    - 튜플
    - 딕셔너리
    - 함수
    - 불린 식
    - Looping
    - 예외 처리
  - 발전
    - os 패키지
      - 환경 변수
      - 커맨드라인 인터페이스
      - 디렉터리
    - time 패키지
      - sleep
    - logger 패키지
      - 로깅을 해보자
      - 스트림과 파일에 동시에 남기기
      - 로그 포매팅

## 맨날 고생하는거

### PYTHONPATH

파이썬은 모듈을 import하기 위해서 PYTHONPATH를 설정해야 한다. 이는 로컬에 자신이 작성한 모듈도 마찬가지이다.

따라서 이떄에 만약 우리가 `from abc/def/ghi import jk`

라는 abc폴더 속의 모듈들을 import한다면 우리가 설정해야 하는 PYTHONPATH 환경변수는 `abc 디렉토리가 위치한 디렉토리위치`이다.

참고로, 파이썬 프로그램을 크론으로 동작시키게 할때에 PYTHONPATH의 설정이 필요한 경우가 있다.

## 기본

### 화이트 스페이스는 중요함

```python
listOfNumbers = [1, 2, 3, 4, 5, 6]

for number in listOfNumbers:
    print(number)
    if (number % 2 == 0):
        print("is even")
    else:
        print("is odd")

print ("all done")
```

### 모듈 불러오기

```python
import numpy as np

A = np.random.normal(30.0, 5.0, 10)
print (A)
```

### 리스트

- 가변

```python
x = [1, 2, 3, 4, 5, 6]
x[:4] # [1, 2, 3, 4]
x[3:] # [4, 5, 6]
x[-2:] # [5, 6]

x.extend([7, 8])
x # [1, 2, 3, 4, 5, 6, 7, 8]

x.append(9)
x # [1, 2, 3, 4, 5, 6, 7, 8, 9]

y = [10, 11, 12]
listOfLists = [x, y]

z = [3, 2, 1]
z.sort()
z # [1, 2, 3]

z.sort(reverse=True)
z # [3, 2, 1]
```

### 튜플

- 불변

```python
x = (1, 2, 3)
len(x) # 3

y = (4, 5, 6)
y[2] # 6

listOfTuples = [x, y]

(age, income) = "32, 120000".split(',')
age # 32
income # 120000
```

### 딕셔너리

```python
captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janeway"

print(captains["Voyager"]) # Janeway

print(captains.get("NX-01")) # None

for ship in captains: # key를 iterate
    print(ship + ": " + captains[ship])
```

### 함수

```python
def SquereIt(x):
    return x * x

print(SquereIt(2)) # 4

def DoSomething(f, x):
    return f(x)

print(DoSomething(SquereIt, 3)) # 9

print(DoSomething(lambda x: x * x * x, 3))
```

### 불린 식

```python
print(1 == 3) # False

print(True or False) # True

print(1 is 3) # False

if 1 is 3:
    print("How did that happen?")
elif 1 > 3:
    print("Yikes")
else:
    print("All is well with the world")
```

### Looping

```python
for x in range(10):
  print(x)

for x in range(10):
  if (x is 1):
      continue
  if (x > 5):
      break
  print(x)

x = 0
while (x < 10):
    print(x)
    x += 1
```

### 예외 처리

```py
(x,y) = (5,0)
z=None
try:
  z = x / y
except ZeroDivisionError as e:
  z = e
  print(z)
print('divide by zero')
print(z) # integer division or modulo by zero
```

## 발전

### os 패키지

#### 환경 변수

```py
import os

os.environ # 환경변수 딕셔너리
os.environ['PATH'] # 이렇게 참조 대신 PATH라는 키가 없으면 에러 발생
os.environ.get('PATH') # 이렇게 참조 대신 PATH라는 키가 없으면 None 반환
```

#### 커맨드라인 인터페이스

- os
- subprocess

```py
# os를 이용한 방법
import os

os.system('ls -al .')

# subprocess를 이용한 방법
from subprocess import call

call(["ls", "-l"])

abc = a.c
call(["vim", abc]) # 커맨드라인 인자 넘겨주기
```

#### 디렉터리

- 현재 디렉터리
- 부모 디렉터리

```py
import os
os.path.dirname(os.path.abspath(__file__)) # 현재 스크립트가 존재하는 곳의 디렉터리

os.getcwd() # 현재 working directory 어느 위치에서 이 script를 실행했는가

os.path.abspath(os.path.join(currentdir, os.pardir)) # 현재 디렉터리의 부모디렉터리 1
os.path.dirname(currentdir) # 현재 디렉터리의 부모디렉터리 2

os.chdir(path) # path로 current working directory를 변경하기
```

### time 패키지

```py
import time
while True:
  print('sleep 5 sec')
  time.sleep(5) # 초단위
```

### logger 패키지

- 참고
  - http://ourcstory.tistory.com/97
- 스트림(커맨드 라인)과 파일에 동시에 로그를 남기는 기능
- 로그 레벨에 따라 출력되는 로그를 제한
- 예외처리
  - 로그 파일의 크기가 일정 크기를 넘어가면 새로운 로그 파일을 자동으로 생성

```py
import logging

logging.basicConfig(filename='./log/test.log', level=logging.DEBUG)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
```

#### 스트림과 파일에 동시에 로그 남기기

- fileHandler
- streamHandler

```py
import logging
import logging.handlers

logger = logging.getLogger('crumbs')
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler('./log/my.log')
streamHandler = logging.StreamHandler()

logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')
```

#### 로그 포매팅

- 핸들러에다가 포매터 지정함

```py
import logging
import logging.handlers

logger = logging.getLogger('crumbs')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

fileHandler = logging.FileHandler('./log/my.log')
streamHandler = logging.StreamHandler()

fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)

logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')
```

#### 파일이 너무 큰 경우 자동으로 새로운 파일 생성

```py
file_max_bytes = 10 * 1024 * 1024
fileHandler = logging.handlers.RotatingFileHandler(filename='./log/test.log', maxBytes=file_max_bytes, backupCount=10)
```
