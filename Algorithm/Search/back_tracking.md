# Back tracking

모든 경우의 수를 전부 고려하는 알고리즘. 상태공간을 트리로 나타낼 수 있을 때 적합한 방식이다(폐회로가 없는 연결 그래프) 일종의 트리 탐색 알고리즘.

- 모든 경우의 수를 고려해야 할 때: DFS
- 트리의 깊이가 무한대가 될 때: BFS
- 좀 더 나은 알고리즘: 최선 우선 탐색(우선순위 큐로 휴리스틱(적당한 지능)을 구현)

## 참고

- [백트래킹 - 나무위키](https://namu.wiki/w/%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9)

## 코드

주목하고 싶은 것은 한 번 방문했을때 어떻게 대처하느냐이다. DFS의 경우 재귀함수에 visited라는 배열을 직접 넘겨줄 수 있지만 많은 메모리를 차지하게 되므로, 다음과 같은 센스있는 방식으로 DFS를 구현한다.

다음은 스도쿠를 풀어주는 알고리즘이다.

```c++
#include <cstdio>
#include <vector>

using namespace std;

#define N 9

struct noNum {
  int i;
  int j;
};

int sudoku[N][N];
vector<noNum> noNumList;
bool stop;

bool checkHorizon(int num, int i, int j)
{
  for (int k = 0; k < 9; k++)
  {
    if (sudoku[i][k] == num){
      return false;
    }
  }
  return true;
}

bool checkVertical(int num, int i, int j)
{
  for (int k = 0; k < 9; k++)
  {
    if (sudoku[k][j] == num){
      return false;
    }
  }
  return true;
}

bool checkBox(int num, int i, int j)
{
  int boxStartI = (i / 3) * 3;
  int boxStartJ = (j / 3) * 3;
  for (int l = boxStartI; l < boxStartI + 3; l++)
  {
    for (int m = boxStartJ; m < boxStartJ + 3; m++)
    {
      if (sudoku[l][m] == num){
        return false;
      }
    }
  }
  return true;
}

void backTrack(int depth, int fromI, int fromJ)
{
  if (depth == noNumList.size()){
    stop = true;
    return;
  }

  for (int i = 1; i <= 9; i++)
  {
    if (checkHorizon(i, fromI, fromJ) && checkVertical(i, fromI, fromJ) && checkBox(i, fromI, fromJ)){
      sudoku[fromI][fromJ] = i;
      int nextI = noNumList[depth+1].i;
      int nextJ = noNumList[depth+1].j;
      // 이 부분이 바로 센스있는 부분! 재귀함수 뒤에 다시 원상복귀 시켜놓는다.
      backTrack(depth + 1, nextI, nextJ);
      if (stop) return;
      sudoku[fromI][fromJ] = 0;
    }
  }
}

int main()
{
  for (int i = 0; i < N; i++){
    for (int j = 0; j < N; j++){
      scanf("%d", &sudoku[i][j]);
      if (sudoku[i][j] == 0){
        noNum nn; nn.i = i; nn.j = j;
        noNumList.push_back(nn);
      }
    }
  }

  int startI = noNumList[0].i;
  int startJ = noNumList[0].j;
  backTrack(0, startI, startJ);

  for (int i = 0; i < N; i++)
  {
    for (int j = 0; j < N; j++)
    {
      printf("%d ", sudoku[i][j]);
    }
    printf("\n");
  }
}

```
