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
    # 8. event loop(??)는 count(1) 로부터 yield 된 실행 흐름을 받아, count(2)코루틴을 실행
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
        - *caller coroutine이 아니라? (그 경우에는 root가 event loop???)*
      - 만약 `await f()` 식을 `g()` 스코프에서 봄 == `g()`의 실행을 `f()`의 결과가 반환될 때 까지 await함
        - 그러면서 실행 흐름의 컨트롤을 event loop로 넘겨줌
    - `await f()`
      - f는 awaitable이어야 함
        - 종류
          - coroutine, task, future
        - `__await__()`을 정의한 오브젝트

### Async IO Design Patterns

- Chaining Coroutines
- Using Queue
  - Producer / Comsumer pattern
