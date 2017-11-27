# memset에 대하여

## 배열의 초기화

```c++
#include <cstdio>
#include <cstring>

int cache[10][10];

int main()
{

  for (int i = 0; i < 10; i++)
  {
    for (int j = 0; j < 10; j++)
      printf("%d ", cache[i][j]); // 전부 0

    printf("\n");
  }

  std::memset(cache, -1, sizeof(cache));

  for (int i = 0; i < 10; i++)
  {
    for (int j = 0; j < 10; j++)
      printf("%d ", cache[i][j]); // 전부 -1
    printf("\n");
  }
  return 0;
}
```
