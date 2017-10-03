# 최단거리 알고리즘

1. 다익스트라 알고리즘(O(E+VlogV))
2. 벨만포드 알고리즘(O(VE))
3. 플로이드 워셜 알고리즘(O(V^3))

## 다익스트라 알고리즘

### 개요
- 전제
  - 모든 간선의 가중치는 0보다 크거나 같다.
- 원리
  - 1. 출발점(노드)의 거리를 0이라고 두고, 나머지 노드까지의 거리는 다 무한대로 놓는다.
  - 2. 출발점에 인접한 노드들에 대하여, 만약 `가장 처음 출발점에서 출발점의 거리 + 출발점에서 인접노드의 거리`가 `가장 처음 출발점에서 인접노드까지의 거리`보다 작으면, 그러한 인접노드의 출발점으로부터의 거리를 갱신한다.
  - 3. 갱신한 거리들 중에서, 가장 가까운 거리에 있는 인접노드를 새로운 출발점으로 둔다.
  - 4. 더 이상 거리를 갱신할 수 없을 때 까지 2,3을 반복한다.
- 효율
  - O(ElogV) (우선순위 큐를 사용할 경우)

### 코드

#### C++

문제

[파티 - 백준1238](https://www.acmicpc.net/problem/1238)

```c++
#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>

#define MAX 1001
#define MAX_TIME 1000000

using namespace std;

struct adjNode {
  adjNode(int a, int b) {
    num = a;
    times = b;
  }
  int num, times;
};

struct comp {
  bool operator()(const adjNode &a, const adjNode &b) {
    return a.times > b.times;
  }
};

int N, M, X;
vector<vector<adjNode> > adjList(MAX);
vector<int> totalTimes;

int dijkstra(int from, int to) {
  int timeToNode[MAX];
  for (int i = 1; i < MAX; i++)
    timeToNode[i] = MAX_TIME;
  timeToNode[from] = 0;

  priority_queue<adjNode, vector<adjNode>, comp> pq;
  pq.push(adjNode(from, 0));

  while(!pq.empty()) {
    int nodeNum = pq.top().num;
    int times = pq.top().times; pq.pop();
    if (times > timeToNode[nodeNum]) continue;
    for (int i = 0; i < adjList[nodeNum].size(); i++)
    {
      int adjNodeNum = adjList[nodeNum][i].num;
      int adjTimes = adjList[nodeNum][i].times;
      if (timeToNode[nodeNum] + adjTimes < timeToNode[adjNodeNum]){
        timeToNode[adjNodeNum] = timeToNode[nodeNum] + adjTimes;
        pq.push(adjNode(adjNodeNum, adjTimes));
      }
    }
  }

  return timeToNode[to];
}

int main() {
  scanf("%d %d %d", &N, &M, &X);
  for (int i = 0; i < M; i++)
  {
    int from, to, times;
    scanf("%d %d %d", &from, &to, &times);
    adjList[from].push_back(adjNode(to, times));
  }

  for (int i = 1; i < N+1; i++)
  {
    int totalTime = dijkstra(i, X) + dijkstra(X, i);
    totalTimes.push_back(totalTime);
  }
  printf("%d\n", *max_element(totalTimes.begin(), totalTimes.end()));

  return 0;
}
```

## 벨만-포드 알고리즘

### 개요

- 전제
  - 최단거리는 도중에 사이클이 존재하지 않으므로 최대 간선의 개수가 V-1이다.
- 원리
  1. 출발점의 거리를 0이라 두고, 나머지 노드까지의 거리를 무한대로 놓는다.
  2. V-1회 다음을 반복한다.
  3. 모든 점에 대하여 다음과 같은 조건이 있을때 인접한 점까지의 거리를 갱신한다. 각각의 거리 > 현재 점의 거리 + 인접한 간선의 가중치.
  4. 한번 더 3을 반복했을 때, 거리가 갱신되는 곳이 있으면 음의 루프가 존재하는 것이다.
- 효율
  - O(VE)

### 코드

문제

[웜홀 - 백준1865](https://www.acmicpc.net/problem/1865)

```c++
#include <cstdio>
#include <vector>

#define INF 100000000
#define MINUS_INF -INF
#define MAX_N 501

using namespace std;

struct adjNode {
  int num, times;
  adjNode(int n, int t) {
    num = n;
    times = t;
  }
};
int T, N, M, W;

int bellmanFord(int from, int to, vector<vector<adjNode> > adjList) {
  bool isInfinite = false;

  int takingTimes[N+1];
  for(int i=0; i < N+1; i++)
    takingTimes[i] = INF;
  takingTimes[from] = 0;

  for(int i=1; i < N+1; i++) {
    for(int j=1; j < N+1; j++) {
      for(int k=0; k < adjList[j].size(); k++) {
        int adjNodeNum = adjList[j][k].num;
        int adjNodeTimes = adjList[j][k].times;
        if (takingTimes[j] != INF && takingTimes[adjNodeNum] > takingTimes[j] + adjNodeTimes) {
          takingTimes[adjNodeNum] = takingTimes[j] + adjNodeTimes;
          if (i == N)
            isInfinite = true;
        }
      }
    }
  }

  if(isInfinite) {
    return MINUS_INF;
  }
  return takingTimes[to];
}

int main() {
  scanf("%d", &T);
  while (T--) {
    scanf("%d %d %d", &N, &M, &W);

    vector<vector<adjNode> > adjList(N+1);
    for(int i=0; i < M; i++) {
      int from, to, times;
      scanf("%d %d %d", &from, &to, &times);
      adjList[from].push_back(adjNode(to, times));
      adjList[to].push_back(adjNode(from, times));
    }
    for(int i=0; i < W; i++) {
      int from, to, times;
      scanf("%d %d %d", &from, &to, &times);
      adjList[from].push_back(adjNode(to, -times));
    }

    int minDist = bellmanFord(1, 2, adjList);

    if (minDist == MINUS_INF) {
      printf("%s\n", "YES");
    } else {
      printf("%s\n", "NO");
    }
  }
  return 0;
}
```

## 플로이드-워셜 알고리즘

### 개요

- 전제
  - 두 정점을 잇는 최소 비용 경로는 경우지를 거치거나 거치지 않는 경로 중 하나에 속한다.
  - 만약 경유지를 거친다면 그것을 이루는 부분 경로 역시 최소 비용 경로여야 한다.
- 원리
  - 경유점이 없는 경로는 그 경로의 가중치를 그대로 적는다. 나머지는 무한대로 둔다.
  - 경유점이 0 ~ N인 경우에 대하여 시작점이 0 ~ N인 경우에 대해서 도착점이 0 ~ N인 경우에 대해서, 각각의 케이스에 따라서 dist[i][j] > dist[i][k] + dist[k][j] 인경우에 dist[i][j]를 갱신해준다.
- 효율
  - O(V^3)

### 코드

아직 원리 자체를 이해하지 못함.
