# OS와 친해지기 - 핵심 OS 요소

- 의문
- 15.1 프로세스 vs 스레드
- 15.2 동기화
- 15.3 Blocked I/O vs Non-blocked I/O
- 15.4 멀티스레딩과 서버
- 15.5 윈도우즈 최강자 서버 - IOCP

## 의문

## 15.1 프로세스 vs 스레드

- 프로세스
  - 개요
    - 하나의 프로그래밍 실행하는 단위
    - 프로그램이 수행되기 위한 자원 소유의 단위
  - 프로그램이 돌아가기 위한 자원
    - 프로그램 이미지(코드, 데이터)
    - 메모리
    - file descriptor
    - 스레드
- 스레드
  - 개요
    - 실행 흐름 단위
    - 멀티 태스킹 OS상에서 프로그램간의 context switching이 일어날 때 전환의 대상이 되는 주체
- context switching
  - 개요
    - CPU가 한 스레드의 코드를 일부 수행하고 잠시 후 다른 스레드의 코드를 수행하려고 하는 것
    - CPU의 모든 레지스터 정보는 해당 스레드와 연계된 메모리상에 보관되어야 하고, 다시 그 스레드가 실행될 때는 보관했던 레지스터 값으로 레지스터를 세팅해야 함
      - `LOAD`, `STORE`와 같은 인스트럭션으로 수행해야 함

C에서의 멀티스레딩 프로그래밍 예제

```c
#include <stdio.h>
#include <WINDOWS.H>

int g_idx = 0;

unsigned int NewThread(void* pParam)
{
  while ( 1 )
  {
    g_idx ++;
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

  while ( 1 )
  {
    printf("g_idx : %d\n", g_idx++);
  }

  return 1;
}
```

- 위 코드는 동기화 문제를 갖고 있음

## 15.2 동기화

- 개요
  - 서로 다른 스레드가 공용자원을 접근하는 경우, race condition을 방지하기 위한 방법
- 동기화 객체
  - Critical Section
    - lock, unlock
  - Mutex

## 15.3 Blocked I/O vs Non-blocked I/O

## 15.4 멀티스레딩과 서버

## 15.5 윈도우즈 최강자 서버 - IOCP
