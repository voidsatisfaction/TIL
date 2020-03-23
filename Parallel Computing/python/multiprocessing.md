# multiprocessing - process-based parallelism

## 의문

## Introduction

- multiprocessing module
  - 개요
    - `threading`모듈과 비슷한 API를 사용하여 process를 spawning하는 것을 도와주는 패키지
    - GIL을 subprocess를 이용하여 효과적으로 피해감
      - multiple processor를 최대한 활용할 수 있도록 도와줌
    - `pool`을 이용하여 효과적으로 data parallelism을 실현 가능

## Contexts and start methods

### platform(OS)에 따라서, 세가지 process start 방법을 제공

- spawn
  - 부모 프로세스는 완전히 새로운 python interpreter process를 시작함
  - 자식 프로세스는 프로세스 오브젝트의 `run()` 메서드를 실행하는 데에 필요한 자원들을 상속받기만 함
    - 특히 필요없는 file descriptor, handles은 상속받지 않음
  - fork, forkserver보다는 다소 느림
  - 지원OS
    - Unix, Windows(default), macOS(default)
- fork
  - 부모 프로세스는 `os.fork()`를 사용하여 python interpreter를 포크함
  - 자식 프로세스는 시작할 때, parant process와 동일함
  - 모든 부모 프로세스의 자원을 상속받음
  - 안전하게 multithreaded process를 forking하는 것은 문제가 많음
  - 지원OS
    - Unix(default)
- forkserver
  - 프로그램이 시작하고, forserver를 start method로 선택할 때, 서버 프로세스가 시작됨
  - 그때부터 새 프로세스가 필요할 때 마다, 부모 프로세스는 서버에 연결하고 새 프로세스를 fork하도록 요청
  - fork server process는 싱글 스레드이므로, `os.fork()`를 사용하는 것이 안전함
  - 필요하지 않은 자원은 상속되지 않음
  - 지원OS
    - Unix(passing file descriptor over Unix pipe를 지원하는 플랫폼에서만)

start method의 선택 방법

```py
import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()
```

## Sharing state between processes

- 어지간 하면 사용하지 않는게 나음
- 그래도 필요하다면...

### Shared memory

- Data
  - `Value`
  - `Array`
