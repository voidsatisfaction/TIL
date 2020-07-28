# AsyncIO in Python

## The asyncio Package and async/await

### The async/await Syntax and Native Coroutines

- async IO의 기저에는 coroutine이 핵심

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
        - 또 다른 coroutine
        - `__await__()`을 정의한 오브젝트

### Async IO Design Patterns

- Chaining Coroutines
- Using Queue
  - Producer / Comsumer pattern
