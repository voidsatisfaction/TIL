# Longlong에 관한 주의사항

## 다음과 같은 코드가 있는경우

```c++
#include <cstdio>

#define MAX 1000000000

using namespace std;

typedef long long ll;

int main(){

  int a[3]={MAX, MAX, MAX};

  ll b = a[0]+ a[1]+ a[2];
  printf("%lld", b); // -1294967296
}
```

a의 배열이 int형인경우 int + int + int 가 int의 범위를 넘으면 그것은 자동적으로 long long이 되지 않는다. 즉, 처음부터 a의 배열을 long long(ll)로 지정해 둘 필요가 있다.
