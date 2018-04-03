# 배열 선언에서 빠지기 쉬운 함정

## 함수 안에서 배열을 선언만 하고 그 함수를 여러번 부르는 경우

### 문제

예를들어 다음과 같이 여러번의 bfs쿼리가 있다고 하자

```cpp
int bfs(int s, int d)
{
  int lv = 0;
  if (s == d)
    return lv;
  bool marked[MAX_N];
  queue<int> q;

  q.push(s);
  marked[s] = true;

  while (!q.empty())
  {
    int size = q.size();
    while (size--)
    {
      int prime = q.front(); q.pop();
      for (int nextPrime : adjList[prime])
      {
        if (!marked[nextPrime])
        {
          if (nextPrime == d)
            return ++lv;
          marked[nextPrime] = true;
          q.push(nextPrime);
        }
      }
    }
    lv++;
  }
  return -1;
}
```

위의 bfs쿼리를 프로그램 내부에서 여러번 호출하는 경우 문제가 되는 곳은 이부분이다.

```cpp
bool marked[MAX_N];
```

단순히 저렇게 선언만 해두면 배열이 새로 초기화가 되지 않는다.

심지어 프로그램을 실행할 때 마다, 답이 바뀌어 나오는 신박함이 나오게 된다.

### 해결책

#### 1. 초기화스러운 문법을 이용한 해법

```c++
bool marked[MAX_N] = {0, };
```

#### 2. memset을 이용하는 해법

```c++
// 반드시 모듈을 불러와야 함
#include <cstring>

bool marked[MAX_N];
memset(marked, 0, sizeof(marked));
```
