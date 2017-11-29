# 비트마스크

변수 혹은 수식에서 원하는 열의 비트만 변경하기 위한 상수를 비트 마스크라고 한다.

프로그램의 각종 flag구현에 사용된다. 특정 함수 호출 시 약속된 규칙을 넘기기 위해서 사용되는 용도라고 볼 수 있다.

e.g. 외판원 문제에서의 Dynamic Programming해답

**사실 플래그 라는 것도 하나의 상태이므로 상태를 구현하는데에 사용된다고 볼 수 있다**

**공간 복잡도의 이득이 있는 경우에 유효**

## Go에서의 비트 연산자 정리

참고

- [가장 빨리 만나는 Go언어](http://pyrasis.com/book/GoForTheReallyImpatient/Unit13)

## 외판원 문제 비트마스크 예시

visited의 구현과 cache의 구현에서 비트 마스크 사용. 비트마스크는 어떠한 상태의 경우 + 순서에 상관없는 flag에 대해서 유효한 듯 하다.

## 사칙연산의 비트마스크 예시

```c++
#include <cstdio>

char PLUS = 1;
char MIN = 2;
char MULTI = 4;
char DIV = 8;

void arithmetic(char flag)
{
  int n1, n2;

  scanf("%d %d", &n1, &n2);

  if (flag & PLUS)
    printf("%d + %d = %d\n", n1, n2, n1 + n2);

  if (flag & MIN)
    printf("%d - %d = %d\n", n1, n2, n1 - n2);

  if (flag & MULTI)
    printf("%d * %d = %d\n", n1, n2, n1 * n2);

  if (flag & DIV)
    printf("%d / %d = %d\n", n1, n2, n1 / n2);
}

int main()
{
  char flag = PLUS;
  arithmetic(flag);

  flag |= MIN;
  arithmetic(flag);

  flag |= MULTI;
  arithmetic(flag);

  flag |= DIV;
  arithmetic(flag);

  retrun 0;
}
```
