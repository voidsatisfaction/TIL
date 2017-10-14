# Parametric Search

## 참고

[이분탐색 파라메트릭 서치(개념)](http://sarah950716.tistory.com/16)

## 정의

최적화 문제를 결정 문제로 바꾸어 푸는 기법. 이분탐색의 응용.

1. 해당값이 정답이 될 수 있는 값인지 아닌지를 쉽게 판단할 수 있어야 한다.
2. 정답이 될 수 있는 값들이 연속적이어야 한다.

이분탐색은 단순히 값인지 아닌지가 명확한 기준으로 나타나있다. 하지만, Parametric Search는 문제에 따라서 기준도 다르므로, 그것을 알아내는 것도 관건.

## 예시

e.g 나이순으로 정렬된 사람들이 있다. 25살 이상이면 소주를 좋아한다는 것이 증명되어 있는데, 그렇다면 정렬된 사람들 중에서 소주를 좋아하는 가장 나이가 어린 사람은?(주어진 조건을 만족하는 것들중 최소값)

1. 위의 정렬된 사람들을 `[A B C D E F G]`라고 두자.
2. 가장 가운데 사람인 D에게 소주를 좋아하는지 묻는다.
3. 아니오가 나왔으므로 나이가 25미만 이라는것을 알게 되어서 이번엔 가운데 D+1(E)와 G사이인 다시 F에게 소주를 좋아하는지 묻는다.
4. 예가 나왔으므로 또 가운데 E와 E사이인 E에게도 물어본다.
5. 예가 나왔으므로 답은 E (아니면 F)

## 코드

- [백준 2110 공유기 설치](https://www.acmicpc.net/problem/2110)

```c++
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int N, C;
vector<int> pos;

int main()
{
  scanf("%d %d", &N, &C);
  for (int i = 0; i < N; i++)
  {
    int x;
    scanf("%d", &x);
    pos.push_back(x);
  }

  sort(pos.begin(), pos.end());
  // 여기까지가 입력

  int left = 1;
  int right = pos[N-1] - pos[0];
  int ans;
  while(left <= right)
  {
    // 이분탐색적으로 찾아나간다.
    int mid = (left + right) / 2;
    int start = pos[0];
    int counts = 1;

    // 여기가 기준을 만족하는지 안하는지 체크
    for (int i = 1; i < N; i++)
    {
      if(pos[i] - start >= mid) {
        counts++;
        start = pos[i];
      }
    }

    if(counts >= C) {
      ans = mid;
      left = mid + 1;
    } else {
      right = mid -1;
    }
  }

  printf("%d\n", ans);
  return 0;
}
```

- [백준 1300 K번째 수](https://www.acmicpc.net/problem/1300)

```c++
#include <cstdio>

typedef long long ll;

ll N, k;

ll llMin(ll a, ll b)
{
  return a < b ? a : b;
}

int main()
{
  scanf("%lld", &N);
  scanf("%lld", &k);
  ll left = 1, right = N * N;
  ll ans;
  while(left <= right)
  {
    // 이분탐색
    ll mid = (left + right) / 2;
    ll mk = 0;

    for (int i = 1; i <= N; i++)
      mk += llMin(mid / i, N);

    // 결정문제
    if(mk < k) {
      left = mid + 1;
    } else {
      right = mid - 1;
      ans = mid;
    }
  }

  printf("%lld\n", ans);

  return 0;
}
```
