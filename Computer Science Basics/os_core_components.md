# 핵심 OS 요소

## 목차

- 의문
- 개요
- 프로세스 vs 스레드
  - 프로세스
  - 스레드
- 동기화
  - 배경
  - 동기화 방법
  - 어떻게 동기화 할 것인가?
  - 동기화의 문제
- Blocked I/O vs Non-Blocked I/O
- 멀티스레딩과 서버
- 윈도우즈의 최강자 서버 - IOCP

## 의문

![](./images/os_core_components/thread_and_memory.gif)

- 한 프로세스 내의 서로 다른 두 스레드안에서 함수를 호출하면, 프로세스 메모리 영역의 스택은 어떻게 관리 될 수 있는가?
  - 스택은 따로 관리
  - 나머지 코드, 전역 데이터, 힙은 공유
  - 그렇다면 스택의 영역은 1/n 되는 것인가?
    - 아니다. 각각의 스택은 1MB로 고정(OS나 언어에 따라 다를 수 있음. 하지만 1/n이 아님)
    - *그런데 프로그램 실행의 자원 관리의 단위는 프로세스인데, 처음 프로세스를 실행할 때, 전체 스택 사이즈를 멀티스레딩까지 포함해서 어떻게 정하는가?*
- *스레드나 고루틴이 4kb다. 와 같은것은 무엇이 4kb라는 것인가?*
  - 공유되지 않는 오버헤드 영역
    - 스택 영역
    - 레지스터 상태

## 개요

- 프로세스 vs 스레드
  - 프로세스
    - 프로그램이 실행되기 위해 필요한 자원의 소유 단위
  - 스레드
    - 코드를 수행하는 단위
    - 단일 CPU에서는 문맥 전환이 일어나는 단위
    - 프로세스당 복수개의 스레드 허용
      - 프로세스에 속하는 자원의 일종
- Blocked I/O vs Non-Blocked I/O
  - Blocked I/O
    - I/O 작업이 끝나는 동안 CPU가 대기 상태에 머무르는 I/O 작업
  - Non-Blocked I/O
    - I/O 작업이 완료되기 전에 곧바로 리턴하고 CPU가 다른 일을 할 수 있게 되는 경우

## 프로세스 vs 스레드

- OS의 핵심기능 중 하나
  - 멀티 태스킹
    - 컨텍스트 스위칭
    - 프로세스

### 프로세스

- 프로그램이 수행되기 위한 자원 소유의 단위
  - **자원** 을 OS에 요청
    - 메모리
    - 핸들 값(이 값으로 OS에 다양한 장치를 요구함)
- (과거 / 임베디드 환경)실행 단위
  - CPU를 사용할 수 있는 권한이 필요
  - **CPU 수행시간을 분배받는 단위**
  - 하지만 워드 프로세서의 맞춤법 검사기 처럼 매 타이핑 마다 체크하기는 힘듬
  - 현재는 실행 단위가 아님

### 스레드

![](./images/os_core_components/process_thread1.png)

- 스레드란
  - 프로세스 자원에 속하면서 프로세스의 코드를 수행하는 단위
    - 하나의 프로세스로 동일한 자원을 사용하되, 실행 단위만 별도로 분리하는 개념
  - 1프로세스는 적어도 하나의 스레드는 소유해야 함
- 문맥 전환
  - CPU가 한 스레드의 코드 일부 수행하고 잠시 후 다른 스레드의 코드를 수행하려고 하는 것
  - 다른 스레드로 문맥 전환이 일어나면, 기존에 사용하던 레지스터 값을 다른 곳에다 저장해두고 새로 전환되는 문맥에서 축적된 레지스터 값을 복원해야 함
    - 메모리상에 보관
  - 문맥전환은 코스트가 크므로, 너무 자주일어나지 않도록 하는 것이 중요
- 윈도우즈의 `CreateThread` API가 있음

스레딩을 이용한 프로그래밍의 예

```c
#include <stdio.h>
#include <WINDOWS.H>

int g_idx = 0;
unsigned int NewThread(void* pParam)
{
  while(1)
  {
    g_idx++;
  }
}

int main(int argc, char* argv[])
{
  CreateThread(
    NULL,
    0,
    (LPTHREAD_START_ROUTINE) NewThread,
    0,
    0,
    NULL
  );

  while (1)
  {
    printf("g_idx : %d\n", g_idx++);
  }

  return 1;
}
```

- 해설
  - `CreateThread()`함수에 스레드 우선 순위, 속성, 스택 사이즈 등 다른 필요한 정보 넣어줌
    - `NewThread()`라는 함수 주소를 넘겨줌
    - 메인 스레드와는 별개로 NewThread 함수를 수행
  - 프로그램 실행 > OS가 새로운 스레드 생성 > 다른 곳에서 프로그램 시작 > main 함수 호출 > 새로 스레드 생성 > 리턴 후 스레드 종료
- 멀티스레딩
  - 복수의 스레드가 존재하게끔 프로그램을 작성하는 것
  - 단점
    - 문맥 전환시 CPU가 레지스터를 저장하고 복구하는데 시간을 허비
    - 동기화 문제
      - 프로그램의 규모가 커지면 정말 다루기 힘들어진다.
      - 서로 다른 스레드가 같은 프로세스 자원을 공유 하지만, 서로 독립적으로 실행하므로 같은 자원이나 변수를 사용할 때 동기화 문제가 발생
      - 위의 코드는 `g_idx` 변수를 원하는 횟수만큼 증가 시키는 것이 불가능
      - 동기화 객체를 사용해야 함

## 동기화

### 배경

- 멀티스레딩은 효과는 효율적이지만 그 관리는 악몽이다.
  - 하나의 메인 스레드 외의 다른 스레드를 만들어 복수의 스레드가 동시에 돌아가는 프로그램 기법
  - 단일 CPU의 경우, 복수의 스레드가 논리적인 단위로만 동시에 코드가 수행되는 것 처럼 보임
    - 인스트럭션 레벨에서는 결국 한 번에 한 인스트럭션이 수행되는 것

예제 코드

```c
#include <stdio.h>
#include <WINDOWS.H>

int g_idx = 0;

unsigned int NewThread(void* pParam)
{
  while(1)
  {
    g_idx++;
    Sleep(50);
  }
}

int main(int argc, char* argv[])
{
  CreateThread(
    NULL,
    0,
    (LPTHREAD_START_ROUTINE) NewThread,
    0,
    0,
    NULL
  );

  while(1)
  {
    printf("g_idx : %d", g_idx);
    printf("g_idx * 2 = %d\n", g_idx * 2);
    Sleep(500);
  }
}
```

- 위의 코드를 실행하면
  - `g_idx`와 `g_idx * 2`의 출력값이 알맞게 싱크되지 않음
    - 어떤 값은 `g_idx`가 0 인데 `g_idx * 2`가 2인 경우도 존재
  - 이는 메인 스레드와 NewThread의 두 코드가 독립적으로 실행되기 때문
    - 우리가 원하는 '동시'는 논리적인 단위
    - 실제로 CPU가 코드를 실행하는 단위는 '인스트럭션'
  - 두 번의 `printf`코드는 서로 다르지만, 사실은 동일한 `g_idx`를 참조해야 하므로 논리적으로는 한 단위로 이루어져 있어야 함
    - 마치 DB의 Transaction과 비슷한 느낌이 든다
    - 이때에 동기화가 필요
  - 두 번의 `printf`가 수행되는 동안에는 `NewThread`가 `g_idx`값을 변경하지 못하도록 해야 함

![](./images/os_core_components/multi_threading_without_sync.png)

### 동기화 방법

크리티컬 섹션을 이용한 동기화(Window specific)

![](multi_threading_critical_section1.png)

- **멀티태스킹 OS에서 제공한 동기화 객체를 사용**
  - **크리티컬 섹션(Critical Section)**
    - 두 개의 스레드가 공용으로 사용하는 변수 등의 자원이 있을 경우, 프로그램상에서 공용의 크리티컬 섹션을 만듬
    - 한 스레드가 지정한 섹션을 사용(lock)
    - 다른 스레드는 사용하고 있는 스레드가 다 마칠 때까지(unlock) 대기 모드
      - 블로킹 상태
    - 미리 사용하던 스레드가 unlock함
    - 대기 하던 스레드가 섹션을 lock하고 해당 코드 수행

```c
#include <stdio.h>
#include <WINDOWS.H>

intg_idx = 0;
CRITICAL_SECTION g_csFor_g_idx;

unsigned int NewThread(void* pParam)
{
  while(1)
  {
    EnterCriticalSection(&g_csFor_g_idx); // lock

    g_idx++;

    LeaveCriticalSection(&g_csFor_g_idx); // unlock

    Sleep(50);
  }
}

int main(int argc, char* argv[])
{
  InitializeCriticalSection(&g_csFor_g_idx); // 초기화

  CreateThread(
    NULL,
    0,
    (LPTHREAD_START_ROUTINE) NewThread,
    0,
    0,
    NULL
  );

  while(1)
  {
    EnterCriticalSection(&g_csFor_g_idx); // lock

    printf("g_idx : %d", g_idx);
    printf("g_idx * 2 = %d\n", g_idx * 2);

    LeaveCriticalSection(&g_csFor_g_idx); // unlock

    Sleep(500);
  }

  DeleteCriticalSection(&g_csFor_g_idx); // 삭제
}
```

![](./images/os_core_components/multi_threading_critical_section1.png)

- **뮤텍스(Mutex)**
  - 크리티컬 섹션의 기능
  - 서로 다른 프로세스에 속한 스레드끼리 동기화 가능
- **세마포어(Semaphore)**
  - 크리티컬 섹션의 기능
  - 락을 한 번이 아니라 지정된 횟수만큼 여러 번에 걸쳐 가능

### 어떻게 동기화를 할 것인가?

- 원칙
  - 2개 이상의 복수의 스레드에서 함께 사용하는 자원(주로 변수)마다 동기화 객체(크리티컬 섹션이나 뮤텍스)를 생성해 둔다.
  - 각 공용 자원이 사용되는 논리적 단위마다 해당 동기화 객체로 묶는다.
  - 가능한 한 동기화 객체로 보호되는 논리적 단위를 작게 잡는다.

### 동기화의 문제

- 논리적 단위를 어디까지 끊을 것인가? 에 대한 판단이 매우 어려움
  - 무식하게 공용 자원을 사용하는 코드 함수 전체를 하나의 단위로 묶어서 락 / 언락
    - 성능면에서 엄청난 손해
- 논리적 단위의 누락 가능성 존재
  - 어디서 잘못됐는지 확인하기 매우 힘듬

![](./images/os_core_components/thread_deadlock1.png)

- 멀티스레딩 프로그래밍에서의 데드락
  - **서로 다른 스레드가 각각 서로 다른 자원을 소유한 채 서로 소유한 자원을 요청하고 기다리는 경우 에 발생**
    - 개발자의 미스로 발생하며, 프로그램 수정 해결이 가능
    - c.f) 프로세스의 데드락
      - 그냥 재부팅하는 수 밖에 없음

데드락 코드 예시

```c
#include <stdio.h>
#include <WINDOWS.H>

int g_A = 0;
int g_B = 0;
CRITICAL_SECTION g_csA;
CRITICAL_SECTION g_csB;

unsigned int NewThread(void* pParam)
{
  while(1)
  {
    EnterCriticalSection(&g_csA);
    EnterCriticalSection(&g_csB);

    g_A++;
    g_B++;

    LeaveCriticalSection(&g_csB);
    LeaveCriticalSection(&g_csA);

    Sleep(50);
  }
}

int main(int argc, char* argv[])
{
  InitializeCriticalSection(&g_csA);
  InitializeCriticalSection(&g_csB);

  CreateThread(
    NULL,
    0,
    (LPTHREAD_START_ROUTINE) NewThread,
    0,
    0,
    NULL
  );

  while(1)
  {
    EnterCriticalSection(&g_csB);
    EnterCriticalSection(&g_csA);

    printf("A : %d", g_A);
    printf("B : %d", g_B);

    LeaveCriticalSection(&g_csA);
    LeaveCriticalSection(&g_csB);

    Sleep(50);
  }

  DeleteCriticalSection(&g_csA);
  DeleteCriticalSection(&g_csB);

  return 1;
}
```

데드락이 걸리는 이유

![](./images/os_core_components/thread_deadlock2.png)

데드락이 걸리지 않게 스레드마다 같은 순서로 락을 걸어주는 경우

![](./images/os_core_components/thread_deadlock3.png)

- 위의 프로그램은 십중팔구 결과가 나오다가 프로그램이 멈춤
  - 데드락 발생
  - 원인
    - `main`스레드에서 크리티컬 섹션 락 순서가 `g_csB`, `g_csA`순인데, NewThread 스레드에선 `g_csA`, `g_csB`로 메인스레드와 반대로 락을 시도하고 있음
  - 해결
    - 두 스레드가 동일한 순서로 크리티컬 섹션 락 순서를 따르도록 함
- 프로세스의 데드락
  - IO 장치
  - 해결 방안이 없음

그럼에도 불구하고 멀티스레딩을 하는 이유는 I/O 처리에 매우 유용하기 때문

## Blocked I/O vs Non-Blocked I/O

## 멀티스레딩과 서버

## 윈도우즈의 최강자 서버 - IOCP
