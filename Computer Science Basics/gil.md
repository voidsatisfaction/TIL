# GIL(Global Interpreter Lock)

- 의문
- 개요
- GIL은 파이썬의 어떤 문제를 해결하기 위해서 존재하는가?
- 왜 GIL을 도입했는가?
- GIL과의 고군분투
- GIL로 인한 대한 문제의 해결 방법

## 의문

## 개요

- 개요
  - 오직 하나의 스레드가 python interpreter의 컨트롤을 갖도록 허락하는 mutex(or lock)
  - 오직 하나의 스레드만 특정 시점에 실행 상태에 있을 수 있음
  - CPU-bound / multi-threaded code의 bottleneck이 될 수 있음

## GIL은 파이썬의 어떤 문제를 해결하기 위해서 존재하는가?

- 파이썬 GC는 오브젝트의 reference수를 카운팅해서, 이것이 0이되면 오브젝트가 차지하는 memory를 release함
- 이러한 reference count variable은 race condition(서로다른 두 스레드가 값을 동시에 높이거나 낮추는 것)으로부터 지켜져야 함
  - GC가 제대로 reference count variable을 계산하지 못하면, memory leak 발생, 잘못된 memory release 가 발생
  - `lock`을 사용하기에는, 데드락의 위험성도 있고, 퍼포먼스가 떨어질 수 있다는 것
- GIL 도입
  - interpreter 자체에 도입한 single lock
  - python bytecode를 실행하기 위해서 필요한 인터프리터 lock
  - 장점
    - deadlock 방지
    - 퍼포먼스 overhead가 적음
  - 단점
    - cpu bound문제를 single threaded화
      - 여러개의 thread를 만들어서 실행시켜도 cpu bound문제에서는 전혀 도움이 되지 않음(오히려 context switching 비용만 발생)
  - 참고
    - 다른 언어에서는 thread-safe memory management로 reference counting이 아닌, 다른 방법을 사용하여, GIL을 도입하지 않음

## 왜 GIL을 도입했는가?

- 파이썬은 OS에 thread라는 개념이 없을 때 부터 존재했었음
- python은 쉽게 사용할 수 있도록 디자인 됨
- 많은 C 라이브러리 extension이 작성됨
- 이러한 C extension은 thread-safe 메모리 관리가 필요했음
- GIL은 구현하기가 쉬웠고, 쉽게 파이썬에 추가됐음
  - 싱글 스레드 프로그램에서는 하나의 lock만 관리하면 되므로, 성능이 향상됨
- thread-safe하지 않은 C라이브러리들도 쉽게 통합할 수 있음(GIL 덕분에)

## GIL과의 고군분투

- Python3 에서의 GIL 퍼포먼스 개선
  - 일부가 CPU-bound, 나머지 일부기 I/O-bound 인경우의 멀티 스레드 프로그램의 case
    - GIL을 acquire후 고정된 시간 뒤에 강제로 release해야 하는데, 그 때에 GIL을 acquire하려는 스레드가 없으면, 같은 스레드가 계속 GIL을 acquire하여 사용함
      - 다른 스레드가 acquire하기 전에 CPU-bound thread가 계속 GIL을 점유하는 문제
    - GIL acquisition 숫자를 관찰하는 메커니즘을 도입하여 해결

## GIL로 인한 대한 문제의 해결 방법

- `multiprocessing`모듈 도입
  - python process는 각각 자기자신만의 python interpreter와 memory space를 갖으므로, GIL이 문제가 되지 않음
- 다른 python interpreter 사용
  - CPython에만 GIL이 존재
