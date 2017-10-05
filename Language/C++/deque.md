# Deque

## 선언

```c++
#include<deque>

using namespace std;

deque<int> dq;
```

## 사용

```c++
dq.push_back(1);
dq.push_back(2);
dq.pop_back();
dq.pop_back();

printf("%d %d\n", dq.front(), dq.size()); // 1 0 이것을 조심!! front에 아직 남아있음
```
