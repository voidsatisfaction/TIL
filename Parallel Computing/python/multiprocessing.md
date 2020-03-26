# multiprocessing - process-based parallelism

- 의문
- 현실 문제
- Introduction
- Contexts and start methods
- Sharing state between processes
- Using a pool of workers
- Programming guidelines
  - All start methods
  - The spawn and forkserver start methods

## 의문

- *start_method에서 fork-server는 왜 존재하는가?*

## 현실 예시

### multiprocessing 자원 inherit에 관하여

```py
import multiprocessing, as mp

# these global objects will be imported(inherited) by spawned process
# not serialized(pickled)
x = 0
class A:
  y = 0

def f():
    print(x) # 0
    print(A.y) # 0

def g(x, A):
    print(x) # 1
    print(A.y) # 0; really, not even args are inherited?

def main():
    global x
    x = 1
    A.y = 1
    p = mp.Process(target = f)
    p.start()
    # args will be serialized(pickled)
    q = mp.Process(target = g, args = (x, A))
    q.start()


if __name__=="__main__":
    mp.set_start_method('spawn')
    main()
```

- 위와 같은 결과가 나오는 이유
  - `mp.Process(target = f)`
    - main 프로세스가 내용을 실행하다가, `main()`함수 실행
    - `p = mp.Process(target = f)`에서 f를 spawn해서 새 프로세스 실행
    - f가 있는 파일 다시 새로 initialize한 뒤에, `f`실행
    - x는 0, A.y는 0이 옳음
  - `mp.Process(target = g, args(x, A))`
    - `q = mp.Process(target = g, args(x, A))`에서 g를 spawn해서 새 프로세스 실행
    - g가 있는 파일 다시 새로 initialize한 뒤에, `g`실행
    - x는 pickled된 `args`가 넘겨져와서 1
    - `A`는 unpickled 되는데, 클래스의 경우 클래스 자체의 state(클래스변수)는 pickled되지 않으므로, 사실상 shared resource인 `class A`가 대신 참조되어서 `A.y`는 0
- 참고
  - serialize
    - 한 오브젝트를 다른 형태로 변환시키는 것
    - e.g
      - pickle은 serialization protocol의 한 가지 가능한 형태임

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
  - Shared memory
  - Server process

### Shared memory

`Value`, `Array`를 이용한 shared memory예시

```py
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0) # double
    arr = Array('i', range(10)) # signed integer

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
```

- Data
  - 종류
    - `Value`
    - `Array`
  - 특징
    - process, thread safe

### Server process

## Using a pool of workers

- `Pool`클래스는 pool of worker process를 나타냄
  - **task를 워커 프로세스에게 배분하는 여러 방법을 가지고있음**

```py
from multiprocessing import Pool, TimeoutError
import time
import os

def f(x):
  return x*x

if __name__ == '__main__':
  with Pool(processes=4) as pool:
    # print "[0, 1, 4,..., 81]"
    print(pool.map(f, range(10)))

    # print same numbers in arbitrary order
    for i in pool.imap_unordered(f, range(10)):
        print(i)

    # evaluate "f(20)" asynchronously
    res = pool.apply_async(f, (20,))      # runs in *only* one process
    print(res.get(timeout=1))             # prints "400"

    # evaluate "os.getpid()" asynchronously
    res = pool.apply_async(os.getpid, ()) # runs in *only* one process
    print(res.get(timeout=1))             # prints the PID of that process

    # launching multiple evaluations asynchronously *may* use more processes
    multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
    print([res.get(timeout=1) for res in multiple_results])

    # make a single worker sleep for 10 secs
    res = pool.apply_async(time.sleep, (10,))
    try:
        print(res.get(timeout=1))
    except TimeoutError:
        print("We lacked patience and got a multiprocessing.TimeoutError")

    print("For the moment, the pool remains available for more work")

# exiting the 'with'-block has stopped the pool
print("Now the pool is closed and no longer available")
```

## Programming guidelines

- All start methods
- The spawn and forkserver start methods

### All start methods

- Avoid shared state
  - 프로세스 사이에 많은 양의 데이터를 옮기는 것은 피해야 함
  - 데이터를 옮기는 방식은 `queue`나 `pipe`를 사용하는 것이 low level synchronization primitive를 사용하는 것 보다 나음
- Picklability
  - proxy들의 인자들이 pickable한 것을 확실히 하는 것이 바람직함
- Joining zombie processes
  - **Unix** 에서는 process가 끝났으나, join되지 않으면 zombie가 되는데, 이 zombie의 숫자는 많으면 안됨
    - 왜냐하면, new process가 시작할 때나, `Process.is_alive`가 호출될 때 모든 프로세스를 `join`하기 때문
      - *암묵적으로 join되기 때문에 위험하다는 것인가?*
  - 명시적으로 시작한 프로세스는 join하자
- **Better to inherit than pickle/unpickle**
  - `spawn`, `forkserver` start method를 사용할 때, `multiprocessing`으로부터의 많은 타입들은, pickable이 전제되어야, 자식 프로세스가 그것들을 사용할 수 있음
  - 하지만 일반적으로, shared object들을 pipe나 queue를 사용해서 주고 받는것을 피하는 것이 좋다
  - **대신, 어떤 공유 자원에 대한 접근이 필요한 한 프로세스가 조상 스레드로부터 그 공유 자원을 inherit하는 것이 바람직**
    - *inherit이 정확히 어떤 것을 의미하는 것인지?*
- Avoid terminating processes
  - `Process.terminate`메서드를 사용하는 것은 lock, semaphore, pipe, queue와 같은 공유 자원들을 고장낼 위험성이 있음
  - 따라서, shared resources를 사용하지 않는 프로세스들만 `Process.terminate`를 사용하는 것이 바람직
- Joining processes that use queues
  - 어떤 `queue`에 item을 `put` 했던 프로세스는, 주어진 `pipe`의 모든 buffered item들이 소진될 때 까지 `terminate`되기 전에 `wait`한다
    - child process는 `Queue.cancel_join_thread` 메서드를 호출하여 이러한 행위를 피할 수 있음
  - **process가 join되기 전에, queue의 모든 아이템들이 제거되어야 함**
    - 그렇지 않으면 아이템을 넣은 process가 제거되었다고 확신할 수 없음
    - non-daemonic process들은 자동적으로 join됨

데드락 예시

```py
from multiprocessing import Process, Queue

def f(q):
    q.put('X' * 1000000)

if __name__ == '__main__':
    queue = Queue()
    p = Process(target=f, args=(queue,))
    p.start()
    p.join()                    # this deadlocks
    obj = queue.get()
    # swap last 2 lines or
    # remove p.join() line
```

- Explicitly pass resources to child processes
  - Unix에서 `fork` start method를 사용하는 경우, 자식 프로세스는 global resource를 사용하는 부모 프로세스에서 만들어진 shared resource(같은 메모리의 object)를 사용할 수 있음
    - *구체적으로 예시는?*
    - windows에서도 사용 가능했는데..? 왜지?
      - windows에서는 default로 `spawn` start method를 적용하는데, 정확히 이야기하면 shared resource를 사용하는 것이 아니고, 새로 initialize된 부모 resource랑은 격리된 또 다른 자식 resource를 사용하는 것
      - 그러므로 오브젝트의 메모리 주소가 서로 다름
  - 참고
    - **코드에 따라서 `multiprocessing`은 `start_method`를 암묵적으로 정해줌**
      - **모듈의 global에 변수가 존재하고 그것을 child process에서 사용하는 경우 `fork`로 변경**
      - **모듈의 global에 함수만 존재하고 그것을 child process에서 사용하는 경우 암묵적 `start_method` 변경이 일어나지 않음**
  - 하지만, 그러한 object를 argument로 넘겨주는 것이 더 좋음
  - child process가 살아있는 동안, 해당 오브젝트는 부모 프로세스에서 garbage collected 되지 않음

위의 안좋은 예시

```py
from multiprocessing import Process, Lock

def f():
    ... do something using "lock" ...

if __name__ == '__main__':
    # fork의 경우에는 lock resource가 공유됨(메모리 주소가 같음)
    # 만일 start_method가 spawn이라면, 애초에 f 속에서 lock을 접근할 수 없을것
    lock = Lock()
    for i in range(10):
        Process(target=f).start()
```

위의 좋은 예시

```py
from multiprocessing import Process, Lock

def f(l):
    ... do something using "l" ...

if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        # 명시적으로 lock을 args를 통해서 넣어주는게 바람직
        # work with both spawn and fork start_method
        Process(target=f, args=(lock,)).start()
```

global resource와 process start method

```py
from multiprocessing import Process, Queue
q = Queue()

def f():
    q.put([42, None, 'hello'])

def main():
    p = Process(target=f)
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()

if __name__ == '__main__':
    # on MacOS
    # start_method is automatically set to 'fork'
    # since, global shared resource is defined (q = Queue())
    main()
```

- `fork`의 경우
  - `q = Queue()` 부분이 parent process에 의해서 fork가 실행되기 전에 한 번 호출이 됨
  - 자식 프로세스는 부모 프로세스가 `fork`를 실행한 그 시점부터 실행을 계속함
  - 결국 같은 `multiprocessing.Queue`를 scope에 두게 됨
- `spawn`의 경우
  - 새 process가 spawn되고, 위의 example script가 자식 프로세스에서 처음부터 다시 실행됨
    - *아마도, target으로 들어간 `f`가 위의 example script에 직접들어가 있으므로?*
      - f를 실행시키기 위한 환경을 고려(global scope라던지...)
    - *만일, `f`가 다른 파일에 들어가있었으면, 그 파일의 환경(global variable 등)을 새로 생성했겠지?*
  - 결국 자식 프로세스는 새 Queue object를 생성하고, 부모 프로세스의 Queue와는 전혀 접점이 없게 됨
  - *애초에 윈도우 환경에서 위의 코드를 실행하면 어떤 일이 벌어지나? error? or 부모 프로세스와 독립된 queue의 생성?*

### The spawn and forkserver start methods

- **More picklability**
  - `Process.__init__()`메서드에 들어가는 모든 인자가 picklable해야 함
    - *picklable을 어떻게 판단하는가?*
- **Global variables**
  - 코드가 자식 프로세스에서 global variable에 접근하려고 하면, 자식 프로세스에서 보는 그 값은, 부모 프로세스에서 보는 값과 같지 않을 수 있음
  - However, global variables which are just module level constants cause no problems.
- **Safe importing of main module**
  - `if __name__ == '__main__'` 필수
