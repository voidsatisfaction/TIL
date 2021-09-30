# 함수가 호출되기 까지

## 의문

## 13.0 개요

## 13.1 벽돌과도 같은 함수 - 구조화된 프로그래밍

- 함수의 기능
  - 1 호출 지점으로 복귀 가능
  - 2 caller, callee간에 데이터 교환을 할 수 있어야 함
    - 인자를 넘기고, 리턴값을 받을 수 있어야 함
  - 3 함수 중첩 호출이 가능해야 함
    - 함수 안에서 자기자신을 포함해 어떤 함수든지 부를 수 있어야 함

## 13.2 함수호출의 기본 원리 - 스택 프레임

- 스택 세그먼트 vs 스택 프레임
  - 스택 세그먼트
    - 프로그램에서 사용하기 편하도록 메모리를 몇 가지 용도로 나눈 것 중 하나
    - 지역 변수를 저장하는 메모리 세그먼트
  - 스택 프레임
    - 함수가 호출될 때마다 그 함수 호출을 위해 할당받는 메모리 블록
    - 스택 세그먼트에 생기는 블록
    - 함수 호출을 위한 메모리란?
      - 리턴후 PC 복귀 주소
      - 함수 호출의 인자
        - `push`로 스택 프레임에 넣어줌
      - 함수의 리턴 값
        - 이는 `eax`레지스터에 저장

### 지역 변수

```c
#include <stdio.h>

int triple_sum(int a, int b)
{
  // push   ebp
  // mov    ebp, esp
  // sub    esp, 8 (지역 변수로 선언된 두 개의 int변수 크기만큼 스택을 늘려둠)
  int nTripleA = a * 3;
  // mov    eax, dword ptr [ebp+8]
  // imul   eax, eax, 3
  // mov    dword ptr [ebp-4], eax
  int nTripleB = b * 3;
  // mov    ecx, dword ptr [ebp+0Ch]
  // imul   ecx, ecx, 3
  // mov    dword ptr [ebp-8], ecx

  return nTripleA + nTripleB;
  // mov    eax, dword ptr [ebp-4]
  // add    eax, dword ptr [ebp-8]
}
// mov    esp, ebp
// pop    ebp
// ret

void printresult(int c)
{
  printf("(10*3) + (20*3) = %d", c);
}

int main(int argc, char* argv[])
{
  printresult(triple_sum(10,20));

  return 1;
}
```

- 인스트럭션 해셜
  - `push`
    - SP(ESP 레지스터의 값)에 값을 추가하고, SP를 주어진 값의 크기만큼 낮은 주소로 이동
  - `pop`
    - Stack의 가장 마지막 원소를 pop하고, 해당 원소를 지정한 레지스터에 저장
    - Stack에 저장되는 데이터는 alignment(정해진 크기만큼을 할당하고 해제)되어 있음
      - 32비트 CPU면, 전부 2**32의 크기로 데이터 저장
  - `call`
    - 함수가 있는 메모리 주소로 점프하고, 현재 PC 레지스터의 값의 주소를 스택에 push
      - push이므로, SP에 주어진 값을 추가하고, SP를 주어진 값의 크기만큼 낮은 주소로 이동
- 해설
  - `triple_sum`함수가 호출되는 caller에서 `push 14h`, `push 0Ah`, `call _sum (00401000)`과 같이 스택 프레임에 인자를 push하고, 호출함
  - `call triple_sum (해당 함수의 메모리 주소)`
  - `triple_sum`
    - 컴파일러는 `triple_sum`함수 내에서 선언된 두개의 지역 변수를 이미 알고 있고, 그것이 각각 int 타입이므로, 스택 포인터를 미리 -8만큼 확장시켜놓음
      - esp레지스터가 가리키는 곳이 스택의 끝
    - 코드 실행
    - esp를 호출 전으로 되돌리고, ebp를 호출전 원래값으로 되돌림과 동시에 스택 pop
    - ret로 caller의 실행하는 주소로 PC값 복원
- 함수 호출 규약
  - __cdecl
  - __stdcall
  - __fastcall
