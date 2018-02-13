// Problem link: yahoo-procon2018
// https://yahoo-procon2018-qual.contest.atcoder.jp/tasks/yahoo_procon2018_qual_c
#include <iostream>
#include <cstdio>

#define MAX_N 19

typedef long long ll;

int N;
ll x[MAX_N], c[MAX_N], v[MAX_N];
ll xSum[MAX_N], cSum[1<<MAX_N], vSum[1<<MAX_N];
ll dp[MAX_N][1<<MAX_N], dp2[MAX_N][2][1<<MAX_N];
const ll LLINF=1001001001001001001LL;

ll llmax(ll a, ll b)
{
  if (a > b){
    return a;
  }
  return b;
}

ll llmin(ll a, ll b)
{
  if (a < b) {
    return a;
  }
  return b;
}

bool contains(int s, int i)
{
  return (s & (1 << i));
}

ll game(int i, int p, int s)
{
  ll& DP = dp2[i][p][s];
  if (DP >= 0)
    return DP;
  if (i >= N)
    return 0;

  // T turn
  if (p){
    ll maxScore = 0;
    maxScore = llmax(maxScore, game(i+1, 1^p, s));
    maxScore = llmax(maxScore, dp[i][s]);
    return DP = maxScore;
  }
  // A turn
  ll minScore = LLINF;
  for (int j=0; j < N; j++) {
    if (contains(s, j)){
      minScore = llmin(minScore, game(i, 1^p, (s^(1<<j))));
    }
  }
  return DP = minScore;
}

int main()
{
  scanf("%d", &N);
  for (int i = 0; i < N; i++)
    scanf("%lld", &x[i]);
  for (int i = 0; i < N; i++)
    scanf("%lld", &c[i]);
  for (int i = 0; i < N; i++)
    scanf("%lld", &v[i]);

  xSum[0] = x[0];
  for (int i=1; i < N; i++)
    xSum[i] = xSum[i-1] + x[i];
  for (int s=0; s < (1<<N); s++) {
    for (int i=0; i < N; i++) {
      if (contains(s, i)){
        cSum[s] += c[i];
        vSum[s] += v[i];
      }
    }
  }

  for (int i = 0; i < N; i++) {
    for (int s = 0; s < (1<<N); s++) {
      if (xSum[i] >= cSum[s]){
        // same with dp[i][s] = vSum[s]; ??
        dp[i][s] = llmax(dp[i][s], vSum[s]);
      }
    }
  }

  for (int s = 0; s < (1<<N); s++) {
    for (int i = 0; i < N; i++) {
      if (!contains(s, i)) {
        for (int j = 0; j < N; j++) {
          dp[j][s|(1<<i)] = llmax(dp[j][s|(1<<i)], dp[j][s]);
        }
      }
    }
  }

  for (int i = 0; i < N; i++) {
    for (int s = 0; s < (1<<N); s++) {
      dp2[i][0][s] = -1;
      dp2[i][1][s] = -1;
    }
  }
  ll ans = game(0, 0, (1<<N)-1);

  printf("%lld\n", ans);
    
  return 0;
}