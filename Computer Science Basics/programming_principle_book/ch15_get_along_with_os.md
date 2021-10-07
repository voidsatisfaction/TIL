# OS와 친해지기 - 핵심 OS 요소

- 의문
- 15.1 프로세스 vs 스레드
- 15.2 동기화
- 15.3 Blocked I/O vs Non-blocked I/O
- 15.4 멀티스레딩과 서버
- 15.5 윈도우즈 최강자 서버 - IOCP

## 의문

- 리틀 엔디안, 빅 엔디안
  - 개요
    - **메모리는 일반적으로 1바이트 단위로 엑세스** 할 수 있는 반면, 32비트 CPU같이 동시에 여러 바이트를 취급할 수 있는 경우, int 형의 4바이트 값을 저장할 때 어떤 순서로 저장하는가의 문제
- 스택의 증가 방향
  - 개요
    - CPU에서 처음부터 스택이라는 개념 도입
    - push, pop 인스트럭션 제공
      - SP가 push할때 증가하느냐, pop할때 증가하느냐는 CPU 설계에 달림
      - c.f) 힙에서는 OS가 관리하므로 OS에 달림
- 스택과 힙의 증가 방향은 서로 마주보게 되어있음
  - 최대한 메모리 충돌이 일어나지 않게 하기 위해서

## 15.1 프로세스 vs 스레드

- 프로세스
  - 개요
    - 하나의 프로그래밍 실행하는 단위
    - 프로그램이 수행되기 위한 자원 소유의 단위
  - 프로그램이 돌아가기 위한 자원
    - 프로그램 이미지(코드, 데이터)
    - 메모리
    - file descriptor
    - page table
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
- 스레드의 CPU 점유율
  - 개요
    - 작업 관리자를 보면, 대다수 프로그램의 CPU 사용률이 0이고, 일부의 프로그램이 거의 대부분의 CPU 사용률을 기록함
  - 이유
    - 대부분의 프로그램의 스레드는 대기모드에 있기 때문
      - 대부분의 프로그램은 I/O를 대기하고 있음
      - I/O에 관련된 API를 호출하면, 스레드를 대기모드로 전환하고, I/O작업이 끝나게 되면 다시 실행모드로 되돌아옴(Blocked I/O인 경우)

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
    - 같은 프로세스 안에서
    - lock, unlock
  - Mutex
    - 서로 다른 프로세스에 속한 스레드끼리
    - lock, unlock
  - Semaphore
    - 락을 한 번이 아니라, 지정된 횟수만큼 여러 번에 걸쳐 할 수 있음
- 동기화 원칙
  - 1 - 2개 이상의 복수의 스레드에서 공용 자원마다 동기화 객체를 생성해 둠
  - 2 - 각 공용 자원이 사용되는 논리적 단위마다 해당 동기화 객체로 묶음
  - 3 - 가능한 한 동기화 객체로 보호되는 논리적 단위를 작게 잡음
- 동기화 프로그램의 어려움
  - 동기화 객체로 보호되는 논리적 단위를 어디까지 잡을 것인가
    - 너무 넓게 잡으면 성능에서 병목이 생김
  - 동기화 객체로 보호되는 논리적 단위가 너무 많은 경우, 디버깅이 힘듬
  - 데드락 문제 해결
- 데드락
  - 개요
    - 각각의 스레드가 하나씩의 자원을 소유한 채 서로 다른 스레드가 소유한 자원을 요청하고 각자가 소유한 자원을 기다리는 것
      - 이 관계가 순환 관계가 되면 발생
    - 프로세스간에서도 I/O 장치등을 놓고 데드락이 발생할 수 있음

## 15.3 Blocked I/O vs Non-blocked I/O

- 개요
  - I/O처리는 CPU처리보다 일반적으로 무지막지하게 느림
    - 메모리 접근도 마찬가지
    - 하드웨어 접근도 마찬가지
    - 그래서 캐시 메모리를 사용
- 개선(Non-blocked I/O)
  - 하드웨어
    - CPU가 I/O장치랑 직접 통신하지 않고, 중간에 컨트롤러를 두고, 컨트롤러와 통신을 함
    - CPU가 컨트롤러에게 데이터를 읽기 위해 요청하거나, 쓰기 위해 요청을 보내주기만 함
    - 컨트롤러는 실제 장치랑 통신하면서 데이터의 읽고 쓰기가 완료될 때까지 기다리는 책임을 짐
    - 컨트롤러는 요청한 작업이 끝나면 CPU에게 인터럽트를 dispatch
      - CPU는 필요한 작업의 요청만 할 뿐, 그 작업을 끝날 때까지 기다릴 필요가 없음
      - I/O요청 동안 다른 인스트럭션 수행
- 코드
  - 하드웨어에서는 Non-blocked I/O로 동작하도록 하지만, 코드상으로는 `ReadFile`, `WriteFile`과 같은 I/O용 API함수들은 내부적으로 컨트롤러로부터 작업이 완료되었다는 인터럽트가 들어올 때까지 리턴하지 않고 블로킹하게 만들기도 함
    - 더 간단하게 코딩할 수 있음
    - 이는 하드웨어적으로는 Non-blocking이므로, CPU가 I/O작업을 기다리는 동안 다른 스레드의 작업을 수행할 수 있게 함
      - 하나의 응용프로그램 스레드에서는 블로킹하는 것 처럼 보일 뿐
    - I/O 동작중 다른 동작을 동시에 수행하고 싶으면, 멀티 스레딩을 이용하면 됨

## 15.4 멀티스레딩과 서버

멀티 스레딩을 이용한 서버 구현

```c
unsigned int ClientThread(void* pClientSock)
{
  SOCKET client_sock = (SOCKET) pClientSock;

  do
  {
    recv(client_sock, data, ...);

    if (data == "Hello")
    {
      send(client_sock, "World", ...);
    } else if (data == 숫자)
    {
      send(client_sock, data * 2, ...);
    }
  } while (data != bye);

  close(client_sock)
}

int main(int argc, char* argv[])
{
  char data[100];

  SOCKET server_sock = socket(...);

  SOCKET client_sock;

  listen(server_sock, ...);

  while (1)
  {
    client_sock = accept(server_sock);

    CreateThread(..., ClientThread, ..., client_sock, ...);
  }

  return 1;
}
```

- 스레드의 분리의 이유
  - 자연스러운 논리적 흐름이 멀티스레딩에 부합하는 경우가 존재
  - 성능 향상
- 서버
  - 클라이언트가 언제 접속할지 모르므로, 항상 대기하고 있어야 함
  - 클라이언트 접속 대기 함수 `accept`
    - 서버 소켓의 `accept`는 논블로킹 모드로 해두고, 스레드로 클라이언트 소켓 통신 로직을 처리함
  - 구현 방법
    - select를 이용한 I/O multiplexing(싱글 스레드)
    - multithreading
      - 단점
        - 클라이언트가 너무 많아지면, 스레드가 너무 많아져서 문맥전환으로 인한 오버헤드가 발생

## 15.5 윈도우즈 최강자 서버 - IOCP

- 개요
  - CPU개수만큼의 스레드 풀을 두어서, idle인 스레드 워커로 request를 처리(client socket)
