# ch11 변수의 정체

- 의문
- 11.0 퀴즈
- 11.1 개요
- 11.2 포인터
  - 일반 포인터
- 11.3 포인터의 사촌 - 배열
- 11.4 다차원 배열

## 의문

## 11.0 퀴즈

- char형으로 선언된 변수에 255를 대입하고 `printf`등으로 출력해보면 x이라는 값이 출력됨
  - `x = -1`
- 64비트 컴퓨터에서 아래 코드의 실행 결과는?
  - `int *a = 5; printf("%d %d %d\n", a, a+10, (short)a+10);`
    - `int*` 타입
      - 5 45 15
    - `short*` 타입
      - 5 25 15
    - `short**` 타입
      - 5 85 15
        - 64비트이므로, 포인터변수의 데이터 크기는 2**64즉, 8바이트

## 11.1 개요

- 컴퓨터는 기본적으로 0과 1밖에 기억할 수 없는 장치
- 0과 1의 2진수는 우리가 익숙한 10진수 대신 숫자를 다르게 표현한 것뿐. 즉, 컴퓨터는 2진수 숫자를 기억해 여러 작업을 하는 장치
  - 여러작업 = 프로그램
- 변수
  - 숫자를 기억하는 메모리 공간일 뿐
  - **char, int, short 등도 결국에 메모리에 이진수를 저장하는 메모리 공간일 뿐**
- 포인터 변수
  - 변수일 뿐
    - 일반 변수로 할 수 있는 연산을 포인터로도 할 수 있음
  - 메모리 주소를 담는 변수일 뿐(그렇기 때문에 unsigned int와 크기가 같음)
    - 32비트 CPU
      - 2**32 = 4GB 메모리 공간 표현 가능
    - 64비트 CPU
      - 2**64 = 18.4467441EB(Exabytes) 메모리 공간 표현 가능
  - *연산자를 통해, 포인터 변수의 값을 읽고, 그 값을 메모리 주소로 보고 해당 메모리 주소의 값을 다시 엑세스 할 수 있는 간접 엑세스를 지원

## 11.2 포인터

어셈블리어로 함수를 호출하는 예제

```c
#include <stdio.h>
#include <conio.h>

void MyFunc()
{
  printf("Hey! I'm in the MyFunc function\n")
  getch();
}

int main(int argc, char* argv[])
{
  int nAddr;

  nAddr = (int)MyFunc;

  __asm
  {
    // call 대신 jmp명령어를 사용하면,
    // 점프한 지점으로 되돌아오는 매커니즘이 없으므로, 메모리 access violation 에러가 생김
    call  dword ptr [ebp-4]
  }

  printf("End of main\n");
  getch();
  return 0;
}
```

함수 포인터로 함수를 호출하는 예제

```c
// 이쪽 코드는 위의 예시와 같음

int main(int argc, char* argv[])
{
  void (*nAddr) ();

  nAddr = MyFunc;

  // 직접 호출할때는, MyFunc의 주소로 직접 call
  // 함수 포인터를 사용해서 호출할 때는, nAddr의 값을 읽고, 이 값을 주소로 삼아서 call
  nAddr();

  printf("End of main\n");
  getch();
  return 0;
}
```

- 개요
  - 메모리 주소를 저장하는 변수
- 특징
  - `char* a`인 경우, a라는 포인터 변수는, 자체 값을 64비트 정수로(64비트 컴퓨터에서)갖음, 다만, 해당 값을 주소로 갖는 데이터가 char임을 나타낸 것
  - 특정 함수의 코드 주소까지 저장 가능
- 용도
  - 동적 메모리 할당
  - 동적으로 프로그램을 실행하다가 생성되는 함수 다루기
    - e.g) DLL
  - 콜백 함수
- c.f) 라이브러리
  - 정적 라이브러리
    - 소스 코드를 컴파일 할때(링킹), 라이브러리의 코드가 실행 파일에 첨부됨
    - 프로그램이 실행되면, 라이브러리의 함수들이 메모리에 이미 존재하고, main 프로그램 안에서는 이 코드가 있는 주소로 점프하여 함수 호출을 함
  - 동적 라이브러리
    - 프로그램이 실행되는 동안, 프로그램 안에서 `LoadLibrary`라는 윈도우즈에서 제공하는 API 함수를 이용해, 이 DLL을 메모리에 로드하도록 코드를 작성한 후, 함수 포인터 변수를 만들어 이 변수가 새로 로드된 호출하고 싶은 라이브러리 함수를 가르키도록 만듬
- 주의
  - 댕글링 포인터
    - 유효하지 않은 주소를 가리키고 있는 포인터
    - NULL 포인터를 사용하여 댕글링 포인터가 생성되는 것을 회피

댕글링 포인터 회피

```c
int *pInt = NULL;

...

// pInt에 유효한 메모리 주소 할당 ㅆ
pInt = malloc(100);

...

if (pInt != NULL)
{
  ...
}

...

free(pInt);
pInt = NULL;
```

### 일반 포인터

- 개요
  - 데이터 타입과 관계없는 or generic한 작업을 하는 경우에 사용하는 포인터
- 예시
  - e.g) `memcpy`
    - source 주소, target 주소, 사이즈만 가지고 target주소에 source주소로 부터 시작하는 메모리를 복사
    - `void* memcpy(void* destination, const void* source, size_t num);`
      - `size_t`는 unsigned int (cpu 비트에 따른 조절이 가능하도록)
  - e.g) `qsort`
    - `void qsort(void *base, size_t num, size_t size, int (*comp_func)(const void *, const void *))`
      - base주소에서 총 size를 갖는 데이터가 num개가 배열형태로 존재할때, 그것을 comp_func를 사용하여 퀵 소팅함

## 11.3 포인터의 사촌 - 배열

```c
#include <stdlib.h>
#include <conio.h>
#include <stdio.h>

int main(int argc, char* argv[])
{
  int arrInt[5] = { 0, 1, 2, 3, 4 };
  int *parrInt = arrInt;

  printf("arrInt : 0x%x, parrInt : 0x%x\n", arrInt, parrInt); // arrInt : 0x12ff6c, parrInt : 0x12ff6c
  printf("arrInt+1 : 0x%x, parrInt+1 : 0x%x\n", arrInt+1, parrInt+1); // arrInt : 0x12ff70, parrInt : 0x12ff70
  printf("arrInt+2 : 0x%x, parrInt+2 : 0x%x\n", arrInt+2, parrInt+2); // arrInt : 0x12ff74, parrInt : 0x12ff74
  printf("Array[0] : 0x%x, \*Pointer : 0x%x\n", arrInt[0], \*parrInt); // Array[0] : 0, \*Pointer : 0
  printf("Array[1] : 0x%x, \*(Pointer+1) : 0x%x\n", arrInt[0], \*(parrInt+1)); // Array[1] : 1, \*(Pointer+1) : 1
  printf("Array[2] : 0x%x, \*(Pointer+2) : 0x%x\n", arrInt[0], \*(parrInt+2)); // Array[2] : 2, \*(Pointer+2) : 2
}
```

- 개요
  - 배열 변수가 나타내는 것은 배열의 시작 주소
- 특징
  - 포인터에서 1을 더하면, 현재 포인터 타입의 사이즈만큼의 바이트를 더함
  - 배열 변수의 접근법을 포인터 변수도 사용 가능
    - `parrInt[0] = *parrInt`
- 배열 변수와 포인터 변수의 차이점
  - 포인터 변수
    - 포인터 변수는 이미 기존에 존재하는 변수를 가리킬 수 있지만, 새로운 변수를 확보할 수는 없음
    - 배열 변수 값 바꾸기 가능 + 연산도 가능
  - 배열 변수
    - 포인터 역할 + 컴파일러가 메모리에서 필요한 메모리를 확보하도록 함
    - 배열 변수 값을 바꿀 수 없음
    - 배열 변수는 일종의 const
- 주의
  - 포인터로 배열을 할당된 공간보다 더 사용하는 잘못된 경우를 조심해야 함

## 11.4 다차원 배열

동적 다차원 배열 할당 코드

```c
void Make_2DArray(int ***array, int row, int col)
{
  int i,j;
  // *array[i]는 pointer를 갖고 있기 때문에 sizeof(int\*) * row만큼 할당
  \*array = malloc(sizeof(int\*) * row)

  for (i = 0; i < row; i++)
  {
    (*array)[i] = malloc(sizeof(int) * col)
  }

  for (i = 0; i < row; i++)
  {
    for (j = 0; j < col; j++)
    {
      (*array)[i][j] = 0;
    }
  }
}
```

- 어셈블러이어에서의 변수
  - 변수 선언은, 변수 이름과 타입을 기억해 적절한 메모리 위치에 필요한 사이즈만큼 확보하는 것
  - 어셈블리어의 경우에는, 임의의 메모리 주소에 원하는 값을 저장하고, 그 주소값을 직접 필요한 곳에서 다시 사용해서 메모리에서 읽어오면 됨
  - 일일이 번호로 기억하기에는 쉽지 않으므로, 레이블을 붙여서 사용하면 됨
    - 변수와의 차이점은, 개발자가 직쩝 메모리의 주소를 지정해주긴 해야한다는 점
