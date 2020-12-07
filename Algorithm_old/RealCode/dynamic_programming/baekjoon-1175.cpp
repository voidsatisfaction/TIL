// baekjoon 1175: https://www.acmicpc.net/problem/1175
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

#define MAX_N 50
#define INF 987654321

using namespace std;

struct node {
  int x;
  int y;
  int dir;

  node(){ x=-1, y=-1; }
  node(int _x, int _y){ x = _x, y = _y; }
  node(int _x, int _y, int _d){ x = _x, y = _y, dir = _d; }
};

int N, M, dx[4]={0, 1, 0, -1}, dy[4]={-1, 0, 1, 0}; // up, right, down, left
int dp[2][MAX_N][MAX_N][4];
string graph[MAX_N];
node s, c1, c2;

bool canGo(int x, int y)
{ return x >= 0 && x < M && y >= 0 && y < N && graph[y][x] != '#'; }

void bfsMapping(int s, int dir, node start)
{
  for (int i = 0; i < M; i++)
    for (int j = 0; j < N; j++)
      for (int b = 0; b < 4; b++)
        dp[s][i][j][b] = INF;

  queue<node> que;
  if (dir == -1){
    for (int i = 0; i < 4; i++) {
      dp[s][start.x][start.y][i] = 0;
      que.push(node(start.x, start.y, i));
    }
  } else {
    dp[s][start.x][start.y][dir] = 0;
    que.push(node(start.x, start.y, dir));
  }

  while (!que.empty()) {
    node currNode = que.front(); que.pop();
    for (int k = 0; k < 4; k++) {
      int nextX = currNode.x + dx[k];
      int nextY = currNode.y + dy[k];
      if (canGo(nextX, nextY) && currNode.dir != k){
        if (dp[s][currNode.x][currNode.y][currNode.dir] + 1 < dp[s][nextX][nextY][k]) {
          dp[s][nextX][nextY][k] = dp[s][currNode.x][currNode.y][currNode.dir] + 1;
          que.push(node(nextX, nextY, k));
        }
      }
    }
  }
}

int main()
{
  cin >> N >> M;
  for (int i = 0; i < N; i++) {
    cin >> graph[i];
    for (int j = 0; j < M; j++) {
      if (graph[i][j] == 'S'){
        s = node(j, i);
      } else if (graph[i][j] == 'C'){
        if (c1.x == -1){
          c1 = node(j, i);
        } else {
          c2 = node(j, i);
        }
      }
    }
  }

  int ans = INF;
  bfsMapping(0, -1, s);
  for (int k = 0; k < 4; k++) {
    bfsMapping(1, k, c1);
    for (int i = 0; i < 4; i++) {
      ans = min(ans, dp[0][c1.x][c1.y][k] + dp[1][c2.x][c2.y][i]);
    }
  }
  for (int k = 0; k < 4; k++) {
    bfsMapping(1, k, c2);
    for (int i = 0; i < 4; i++) {
      ans = min(ans, dp[0][c2.x][c2.y][k] + dp[1][c1.x][c1.y][i]);
    }
  }

  if (ans == INF){
    cout << -1 << endl;
  } else {
    cout << ans << endl;
  }
  return 0;
}
