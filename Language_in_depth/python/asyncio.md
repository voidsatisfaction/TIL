# AsyncIO in Python

## 참고

- https://docs.python.org/ko/3/library/asyncio-task.html

## 의문

## The asyncio Package and async/await

### The async/await Syntax and Native Coroutines

- async IO의 기저에는 coroutine이 핵심

코드 예시1

```py
import asyncio

async def count(i):
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

# output
# One
# One
# One
# Two
# Two
# Two
# countasync.py executed in 1.01 seconds.
```

- 코드 해설
  - single event loop(coordinator)가 존재하여, Talking to each of the calls to `count()` 를 함
  - task가 `await`와 만나게 되면, 함수는 실행 흐름을 event loop에게 yield 하고, event loop는 다른 일을 행함

코드 예시2(??? 는 맞는지 아닌지 모르는 부분)

```py
import asyncio

async def count(i):
    print(i)
    await asyncio.sleep(i)
    print(i)

async def main():
    # 3. asyncio.gather() 실행으로 일단 main의 실행 흐름을 yield
    # asyncio.gather 시점에서 애초에 task가 다 등록이 되는것인가? task가 메인루프에서 등록된다의 의미?
    # 7. event loop는 태스크로 등록된 count(1) 코루틴을 실행.
    # 8. event loop는 count(1) 로부터 yield 된 실행 흐름을 받아, count(2)코루틴을 실행
    # 9. event loop는 count(2) 로부터 yield 된 실행 흐름을 받아, count(3)코루틴을 실행
    # 10. count(3) coroutine은 event loop로 실행 흐름 yield
    # 11. event loop는 count(1)에서 asyncio.sleep(1)이 끝난 뒤에(?? 애초에 끝났다는 것을 어떻게 알지?), 실행 흐름을 다시 count(1) 코루틴으로 넘겨줌
    # 13. event loop는 count(2)에서 asyncio.sleep(2)이 끝난 뒤에, 실행 흐름을 다시 count(2) 코루틴으로 넘겨줌
    # 14. event loop는 count(2)에서 asyncio.sleep(3)이 끝난 뒤에, 실행 흐름을 다시 count(3) 코루틴으로 넘겨줌
    await asyncio.gather(count(1), count(2), count(3))

async def main2():
    # 5. print 실행
    print('main2 start')
    # 6. asyncio.sleep로 sleep 태스크 등록(??) 후 event loop로 실행 흐름 yield
    await asyncio.sleep(2)
    print('main2 end')

async def main_of_main():
    # 2. event loop는 main() 코루틴을 먼저 실행
    # 4. event loop는 main2() 코루틴을 실행
    # 12. event loop는 main2의 asyncio.sleep(2)가 끝난 뒤에 main2() coroutine으로 실행 흐름 넘겨줌. 실행이 끝나면 event loop으로 실행 흐름 다시 넘겨줌
    # 15. event loop는 asyncio.gather의 task가 다 끝난것을 인지
    await asyncio.gather(main(), main2())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    # 1. event loop 생성 및 main_of_main() coroutine 실행
    # 16. event loop 제거 및 순차적 실행
    asyncio.run(main_of_main())
    # main2 start
    # 1
    # 2
    # 3
    # 1
    # main2 end
    # 2
    # 3
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
```

- 의문
  - `asyncio.sleep`가 끝나고 나서 event loop는 어떻게 끝났다는 것을 알고 실행 흐름을 넘겨줄 수 있는가?

### The Rules of Async IO

- syntax
  - `async`
    - `async def`
      - 의미
        - native coroutine 혹은 asynchronous generator를 의미
      - 사용법
        - `await`, `return`, `yield` 전부 사용 가능(optional)
          - `async def noop(): pass` 역시 valid
          - `yield from`은 syntax error
        - return, await를 내부에서 사용하면, coroutine 함수를 생성하게 되고, `await`를 사용하여 결과를 받아와야 함
        - yield를 사용하면 asynchronous generator를 생성하게 되고, `async for`를 사용하여 iterate할 수 있게 됨
    - `async with`, `async for`
      - 식 역시 valid
  - `await`
    - 의미
      - 실행 흐름의 컨트롤을 event loop로 넘겨줌
      - 만약 `await f()` 식을 `g()` 스코프에서 봄 == `g()`의 실행을 `f()`의 결과가 반환될 때 까지 await함
        - 그러면서 실행 흐름의 컨트롤을 event loop로 넘겨줌
    - `await f()`
      - f는 awaitable이어야 함
        - 종류
          - coroutine, task, future
        - `__await__()`을 정의한 오브젝트

## Async IO Design Patterns

- Chaining Coroutines
  - coroutine속에서 coroutine을 `await` 하는 경우
- Using Queue
  - 시나리오
    - 많은 서로 관련 없는 Producer들이 item을 queue에 넣음
    - Comsumer의 그룹은 queue로부터 아이템을 가져와서 processing함

Using Queue 예시

```py
import asyncio
import itertools as it
import os
import random
import time

async def makeitem(size: int = 5) -> str:
    return os.urandom(size).hex()

async def randsleep(a: int = 1, b: int = 5, caller=None) -> None:
    i = random.randint(0, 10)
    if caller:
        print(f'{caller} sleeping for {i} seconds')
    await asyncio.sleep(i)

async def produce(name: int, q: asyncio.Queue) -> None:
    n = random.randint(0, 10)
    for _ in it.repeat(None, n):
        print(f'bef {name}')
        i = await makeitem()
        print(f'after {name}')
        t = time.perf_counter()
        await q.put((i, t))
        print(f'Producer {name} added <{i}> to queue.')

async def consume(name: int, q: asyncio.Queue) -> None:
    while True:
        await randsleep(caller=f'Consumer {name}')
        i, t = await q.get()
        now = time.perf_counter()
        print(
            f'Consumer {name} got element <{i}>'
            f' in {now-t:0.5f} seconds'
        )
        q.task_done()

async def main(nprod: int, ncon: int):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
    # consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
    for n in range(1):
        asyncio.create_task(consume(n, q))
    await asyncio.gather(*producers)
    await q.join() # implicitly awaits consumers, too
    # for c in consumers:
    #     c.cancel()

if __name__ == '__main__':
    import argparse
    random.seed(444)
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--nprod', type=int, default=5)
    parser.add_argument('-c', '--ncon', type=int, default=10)
    ns = parser.parse_args()
    start = time.perf_counter()
    asyncio.run(main(**ns.__dict__))
    elapsed = time.perf_counter() - start
    print(f'Program completed in {elapsed:0.5f} seconds.')

# python3 async_queue.py -p 2 -c 5
#
# bef 0
# after 0
# Producer 0 added <71c8fc6c28> to queue.
# bef 0
# after 0
# Producer 0 added <e8815a575e> to queue.
# bef 0
# after 0
# Producer 0 added <8f8612aae1> to queue.
# bef 0
# after 0
# Producer 0 added <7c244edd31> to queue.
# bef 1
# after 1
# Producer 1 added <74c1dbbda8> to queue.
# bef 1
# after 1
# Producer 1 added <971b874ac1> to queue.
# bef 1
# after 1
# Producer 1 added <8d2d0ad0e2> to queue.
# bef 1
# after 1
# Producer 1 added <c2165b038b> to queue.
# Consumer 0 sleeping for 0 seconds
# Consumer 0 got element <71c8fc6c28> in 0.00071 seconds
# Consumer 0 sleeping for 4 seconds
# Consumer 0 got element <e8815a575e> in 4.00863 seconds
# Consumer 0 sleeping for 7 seconds
# Consumer 0 got element <8f8612aae1> in 11.01602 seconds
# Consumer 0 sleeping for 4 seconds
# Consumer 0 got element <7c244edd31> in 15.02276 seconds
# Consumer 0 sleeping for 4 seconds
# Consumer 0 got element <74c1dbbda8> in 19.02715 seconds
# Consumer 0 sleeping for 8 seconds
# Consumer 0 got element <971b874ac1> in 27.03263 seconds
# Consumer 0 sleeping for 10 seconds
# Consumer 0 got element <8d2d0ad0e2> in 37.03482 seconds
# Consumer 0 sleeping for 7 seconds
# Consumer 0 got element <c2165b038b> in 44.04057 seconds
# Consumer 0 sleeping for 8 seconds
# Program completed in 44.09003 seconds.
```

## AsyncIO's Roots in Generators

- coroutine을 단순히 실행하면, awaitable coroutine object를 반환
- **`await`은 `yield from`와 더 유사함**
  - `yield from x()` == `for i in x(): yield i`
  - 이전의 generator-based coroutine은 `yield from`을 사용해서 coroutine result를 기다림
- generator의 특징
  - stop 후에 언제든 다시 시작할 수 있음
- `await`은 break point로서, 일시적으로 정지시키고, 프로그램이 나중에 실행될 수 있도록 함

### Other Features: async for and async generators + comprehensions

- `async for`
  - asynchronous iterator를 iterate 하기 위한 키워드
  - asynchronous iterator의 목적은 asynchronous code를 각 스테이지에서 이터레이션을 하면서 호출할 수 있도록 하기 위함
  - 아직 잘 모르겠음

```py
import asyncio

# asynchronous generator
async def mygen(u: int = 10):
    i = 0
    while i < u:
        print(u)
        yield 2 ** i
        i += 1
        await asyncio.sleep(0.1)

async def main():
    g = [i async for i in mygen(10)] # 동기적으로 실행됨
    f = [j async for j in mygen(20) if not (j // 3 % 5)]
    return g, f

g, f = asyncio.run(main())
print(g)
print(f)
```

## What is an event loop?

- event loop
  - 하나의 프로그램에서의 event나 message를 기다리거나, dispatch하는 프로그래밍 구조
