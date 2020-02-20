# 파이썬 스레딩

## 의문

## 개요

- 스레딩
  - 개요
    - concurrently 프로그램을 실행 할 수 있도록 함
    - 코드 디자인을 심플하게 함

### thread

- 개요
  - 하나의 실행의 흐름
  - 외부 이벤트를 기다리는데에 많은 시간을 소비하는 tasks은 스레딩을 도입 하기에 좋은 대상이다
    - 반대로, CPU 사용이 많고 외부 이벤트를 기달리는 시간이 매우 작은 경우에는 더 빨라지지 않는 경우도 존재
  - 프로그램의 디자인이 간결해짐

기본적인 스레딩 예시 코드

```py
import logging
import threading
import time

def thread_function(name):
    logging.info('Thread %s: starting', name)
    time.sleep(2)
    logging.info('Thread %s: finishing', name)

if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')

    logging.info('Main : before creating thread')
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info('Main : before running thread')
    x.start()
    logging.info('Main : wait for the thread to finish')
    # block until thread x finish
    x.join()
    logging.info('Main : all done')

```

### Daemon thread

- 개요
  - 메인 프로그램이 종료되면 데몬 스레드도 즉시 종료됨
  - 즉, daemon thread는 종료를 걱정할 필요 없이 background에서 실행되는 스레드
    - daemon thread가 아닌 스레드를 프로그램이 실행하면, 프로그램을 종료하기 전 해당 스레드들이 종료될 때 까지 기다림
- 코드
  - `x = threading.Thread(target=thread_function, args=(1,), daemon=True)`
    - 위의 예시에서 이렇게 지정하고, `x.join()`을 주석으로 두면, 해당 프로그램은 x 스레드를 기다리지 않고 바로 종료
- `join()`
  - daemon thread던 일반 thread던 callee 스레드가 실행이 끝날 때 까지 caller thread를 blocking함

## Working with many threads

- 문제
  - 단순히 for loop으로 스레드를 실행시키고 `join()`으로 블록 시키면 순서대로 스레드가 끝나지 않아서 예상하지 못한 결과를 반환
  - **스레드를 실행하는 순서는 os가 정해주므로 예측하기 힘듬**
    - 심지어 실행시 마다 다름

### ThreadPoolExecutor

- 개요
  - `concurrent.futures` 스탠다드 라이브러리에 포함됨
    - `with` context manager로 쉽게 위의 for loop으로 실행하는 스레드를 만들 수 있음
- 특징
  - 여전히 os가 스레드 실행 순서를 관장하므로 순서 보장을 할 수 없음

```py
import time
import concurrent.futures

def thread_function(name):
    logging.info('Thread %s: starting', name)
    time.sleep(2)
    logging.info('Thread %s: finishing', name)

if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))
        logging.info('done')

# Thread 0: starting
# Thread 1: starting
# Thread 2: starting
# done
# Thread 1: finishing
# Thread 0: finishing
# Thread 2: finishing
```

### Race Conditions

- 개요
  - 두개나 그 이상의 스레드가 공유 데이터나 자원을 접근할 때 발생함
  - race condition은 명백하지 않음
    - 디버깅하기 힘듬
  - os는 심지어 `x = x + 1`과 같은 코드에서 x의 값만 읽고 컨텍스트 스위칭을 할 수 있음(다시 돌아와서 갱신)
    - 어셈블리어를 생각해보면 매우 자명함

문제의 코드

```py
import logging
import time
import concurrent.futures

class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.info('Thread %s: starting update', name)

        # local_copy는 thread-safe
        # local-variable
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)

        self.value = local_copy
        logging.info('Thread %s: finishing update', name)

if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')

    database = FakeDatabase()
    logging.info('Testing update. Starting value is %d.', database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            # submit: 스레드에서 실행하는 함수에 positional / named arguments를 전달 가능한 함수
            executor.submit(database.update, index)
    logging.info('Testing update. Ending value is %d.', database.value)

# output
# Testing unlocked update. Starting value is 0.
# Thread 0: starting update
# Thread 1: starting update
# Thread 0: finishing update
# Thread 1: finishing update
# Testing unlocked update. Ending value is 1.
```

위 코드 그림 해설

![](./images/threading/threading_example1.png)

### Basic Synchronization Using Lock

- Lock(Mutex(Mutual Exclusion))
  - race condition의 해결책중 하나
  - 한번에 하나의 스레드만 lock을 갖을 수 있음
    - 다른 lock을 원하는 스레드는 owner가 풀어주기 까지 기다려야 함(`.acquire()`, `.release()`)
    - 다른 lock을 갖은 스레드가 release하지 않으면 프로그램의 실행 흐름이 막혀버림
  - `with`와 같은 context manager과 같이 쓰임
    - release를 하지 않아도 알아서 해줌
- Lock을 이용한 문제 해결

코드

```py
import logging
import time
import concurrent.futures
import threading

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        logging.info('Thread %s: starting update', name)
        logging.debug('Thread %s about to lock', name)
        with self._lock:
            logging.debug('Thread %s has lock', name)

            local_copy = self.value
            local_copy += 1
            time.sleep(1)

            self.value = local_copy
            logging.debug('Thread %s about to release lock', name)
        logging.debug('Thread %s after release', name)
        logging.info('Thread %s: finishing update', name)

if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO,
     datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)

    database = FakeDatabase()
    logging.info('Testing update. Starting value is %d.', database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info('Testing update. Ending value is %d.', database.value)

# 22:38:40: Testing update. Starting value is 0.
# 22:38:40: Thread 0: starting update
# 22:38:40: Thread 1: starting update
# 22:38:40: Thread 0 about to lock
# 22:38:40: Thread 1 about to lock
# 22:38:40: Thread 0 has lock
# 22:38:41: Thread 0 about to release lock
# 22:38:41: Thread 0 after release
# 22:38:41: Thread 1 has lock
# 22:38:41: Thread 0: finishing update
# 22:38:42: Thread 1 about to release lock
# 22:38:42: Thread 1 after release
# 22:38:42: Thread 1: finishing update
# 22:38:42: Testing update. Ending value is 2.
```

### Deadlock
