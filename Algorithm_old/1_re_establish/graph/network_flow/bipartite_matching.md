# 이분 매칭

- 의문
- 개요

## 의문

## 개요

- 매칭 문제
  - 예시
    - N명의 사람이 사이좋은 사람끼리 짝을 찌어주기
    - 최대 몇 쌍이나 만들 수 있는가?
  - matching(매칭)
    - vertex를 공유 하지 않는 edge

## 이분 매칭

- 이분 그래프
  - 정의
    - 정점을 두 그룹으로 나눠서 모든 간선이 서로 다른 그룹의 정점들을 연결하도록 할 수 있는 그래프
  - 예시
    - 작업 배분
      - N명의 사람에게 N개의 작업을 배분하는 방법. 단 모든사람이 모든 작업을 할 수 있는것은 아님
      - 최대 매칭
        - 가능한 한 많은 작업과 사람을 짝지을 수 있는 방법

## 이분 매칭 문제 해결

- 네트워크 유량 문제로 변환
  - 증가 경로를 찾아서 계속 갱신해주고, 더 이상 증가경로가 나타나지 않을 때 까지 반복
- 일반적으로 dfs로 포드 풀커슨 알고리즘을 구현하면 됨
  - 1 어차피 최대 유량 `f = |V|` 이므로 시간 복잡도적 측면에서 괜찮음
  - 2 증가 경로를 탐색하는 도중 B에 포함되는 정점에 도착했는데, 이미 해당 정점에 도달했던 적이 있으면 증가경로의 다음 경로는 유일하게 결정됨(기존에 매칭된 정점)

## 문제 예시

백준 9577 토렌트

```py
'''

희원이가 사용하는 ACM토렌트는 하나의 파일을 공유받을 때 여러 조각으로 나누어, 조각을 지닌 시드가 접속하는 시간에 시드로 부터 일부 조각을 전송 받아 파일을 완성시키는 방법으로 파일이 공유된다.  시드는 자신이 가지고 있는 조각을 자신이 접속했을 때 다른 사용자에게 배포하는 역할을 한다.

희원이는 N개의 조각으로 나눠진 하나의 파일을 공유 받으려고 한다.  각 시드 별로 접속시간과 가지고 있는 조각의 정보가 주어졌고 희원이 이외의 다른 사용자가 가지고 있는 조각은 고정되어 있다고 가정할 때 희원이가 받으려는 파일의 모든 조각을 전송 받을 수 있는 최소의 시간을 알아보자.

시드별로 가지고 있는 조각이 다르고 접속하는 시간도 다르다. 하나의 조각을 받는 데 1초가 걸린다. 즉 여러 시드로부터 같은 시간에 조각을 동시에 받을 수 없다. 예를 들어 시드가 0초에 접속해서 3초에 나간다고 하면 희원이는 시드로 부터 최대 3개의 조각을 전송 받을 수 있다. 희원이는 0초부터 접속해 있다.



첫째 줄에 테스트케이스 T가 주어진다.

두 번째 줄부터 각 테스트케이스마다 파일이 나뉘어져 있는 조각수 n(1 ≤ n ≤ 100), 시드를 나누어 가지고 있는 사람수 m(1 ≤ m ≤ 100)이 주어진다. 다음 줄부터 m개의 줄에 걸쳐 사용자별로 접속하기 시작한 시간 t1 (0 ≤ t1 ≤ 100), 나가는 시간 t2 (t1 ≤ t2 ≤ 100), 가지고 있는 조각의 수 a (0 ≤ a ≤ n), a개 조각의 각각의 번호 qi (1 ≤ qi ≤ n, 1 ≤ i ≤ a)가 주어진다.


파일을 다운받을 수 있는 최소 시간을 출력한다. 만약 더 이상 접속하는 사용자가 없는데 파일을 모두 다운받지 못한 경우에는 -1을 출력한다.

'''


T = int(input())

for _ in range(T):
    n, m = [ int(x) for x in input().split(' ') ]

    a_adj_list = [ set() for _ in range(101) ]
    a_visited = [ False for _ in range(101) ]

    a_match = [ -1 for _ in range(101) ]
    b_match = [ -1 for _ in range(101) ]

    for _ in range(m):
        input_list = input().split(' ')
        t1, t2, a = int(input_list[0]), int(input_list[1]), int(input_list[2])
        if a == 0:
            continue

        b_num_list = [ int(n) for n in input_list[3:] ]

        for t in range(t1, t2):
            for b in b_num_list:
                a_adj_list[t].add(b)

    def dfs(a):
        if a_visited[a] is True:
            return False
        a_visited[a] = True

        for b in a_adj_list[a]:
            if b_match[b] == -1 or dfs(b_match[b]):
                a_match[a] = b
                b_match[b] = a
                return True

        return False

    total_match_count = 0

    for a in range(0, 101):
        a_visited = [ False for _ in range(101) ]

        if dfs(a) is True:
            total_match_count += 1

    if total_match_count != n:
        print(-1)
        continue

    max_a_with_match = 0
    for i, a in enumerate(a_match):
        if a != -1:
            max_a_with_match = i

    print(max_a_with_match+1)
```
