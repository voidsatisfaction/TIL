# 네트워크 유량

- 개요
- 네트워크 유량 문제
- ford-fulkerson(포드 풀커슨) method
  - 정당성의 증명
  - 코드 예시

## 개요

- 예시
  - 네트워크를 이용해서 수백 GB에 달하는 큰 파일을 다운로드 하는 경우에는, 패킷이 내 컴퓨터에 몇초만에 도착하느냐 보다 1초에 몇 MB의 데이터를 전송받을수있는가가 더 중요
    - 네트워크 케이블은 일정한 대역폭을 갖고 있음
- 비유
  - vertex
    - 네트워크 장비
  - edge
    - 케이블
      - 케이블은 대역폭(capacity)을 갖고 있음

## 네트워크 유량 문제

- 정의
  - 각 간선이 용량을 갖는 그래프에서 두 정점 사이에 얼마나 많은 흐름 혹은 유량을 보낼 수 있는지를 계산하는 문제
- 예시
  - 초당 네트워크를 통한 최대 다운로드 속도
  - 두 도시 사이를 이동할 수 있는 시간당 차량의 수
  - 송유관 네트워크에서 두 도시 사이에 보낼 수 있는 석유의 양
  - 그래프와 별 관련없는 다양한 최적화 문제들을 해결하는데에 큰 도움이 됨
- 용어 정의
  - flow network(유량 네트워크)
    - 각 edge에 capacity라는 추가 속성이 존재하는 directed graph
  - `c(u,v)`
    - vertex u, v 사이 간선의 용량
  - `f(u,v)`
    - vertex u, v 사이 실제 흐르는 유량
  - `r(c,v)`
    - `r(c,v) = c(u,v) - f(u,v)`
    - 잔여 용량
  - source
    - 유량이 시작되는 vertex
  - sink
    - 유량이 도착하는 vertex
  - 참고
    - source와 sink에서는 유량의 보존 법칙이 성립하지 않으나, 나머지 정점에서는 성립함
- 유량의 성질
  - **용량 제한 속성**
    - `f(u,v) <= c(u,v)`
  - **유량의 대칭성**
    - `f(u,v) = -f(v,u)`
  - **유량의 보존(source, sink 이외에)**
    - 각 정점에 들어오는 유량과 나가는 유량의 양은 정확히 같아야 함
- 증가 경로
  - 현재의 flow network에서 더 유량을 증가시킬 수 있는 경로
  - 각 간선에 이미 흐르고 있는 유량 외에 추가로 유량을 보낼 수 있는 여유 용량이 필요
  - 증가 경로를 통해 흘려보낼 수 있는 유량의 최대량은, 포함된 간선의 잔여 용량 중 가장 작은 값으로 결정

## ford-fulkerson(포드 풀커슨) method

- 원리
  - 유량 네트워크의 모든 간선의 유량을 0으로 두고 시작해, 소스에서 싱크로 잔여 용량이 남은 간선들만을 사용하는 증가 경로를 찾아 유량 보내기를 더 이상 증가 경로가 없을 때 까지 반복
    - 구체적인 알고리즘은 아님
- 알고리즘 레벨의 구현
  - Edmond-Karp 알고리즘
    - bfs를 이용
    - dfs를 이용해도 되는데, 시간 복잡도가 `O(|E|f)`에서 f가 최대 유량이므로, f가 너무 크면 문제가 생길 수 있음
    - 성능
      - `min(O(|E|f), O(|V||E|^2)), 단 f는 최대 유량`

### 정당성의 증명

- 의문
  - 증가 경로가 여러개인 경우, 그 중 아무것이나 택해도 괜찮은가?
- 해결
  - **최소 컷 문제**
    - 네트워크에서 용량이 가장 작은 컷을 찾는 것
    - 용어 정리
      - 컷(유량 네트워크의 컷)
        - 소스와 싱크가 각각 다른 집합에 속하도록 그래프의 정점을 두 개의 집합으로 나눈 것
          - 소스가 속한 집합을 S
          - 싱크가 속한 집합을 T
      - 컷 S,T의 용량
        - S에서 T로 가는 간선들의 용량 합
      - 컷 S,T의 유량
        - S에서 T로 가는 실제 유량의 합
    - 성질
      - 컷의 유량은 소스에서 싱크로 가는 총 유량과 같음
      - 컷의 유량은 용량과 같거나 작음
      - lemma
        - *임의의 flow network에서 임의의 컷에 대하여, S,T로 가는 유량은 전부 동일하다*
          - *증명?*
  - 최소 용량 최대 유량 정리
    - **`용량과 유량이 같은 컷 <=> 최소 컷 <=> 최대 유량`**
      - `최대유량 => 용량과 유량이 같은 컷` 은 정확히 어떤 의미인가? 어떠한 네트워크 플로우가 최대유량이면, 용량과 유량이 같은 컷이 존재한다?
    - 즉, *잔여 용량이 있는 간선을 통해 갈 수 있는 정점들의 집합 S*(???) 와 그럴 수 없는 정점들의 집합 T로 정점의 집합을 나눔
      - 소스는 S에 속함
      - 싱크는 T에 속함
      - 즉, S,T는 유량 네트워크의 컷
      - *그러면?*

### 코드 예시

```py
# 농사꾼 존은 소들이 충분한 물을 마시길 원했다. 그래서 농장에서 우물에서 외양간을 잇는 N개의 배수관의 지도를 만들기로 했다. 존은 아주 다양한 크기의 배수관들이 완전히 우연한 방법으로 연결돼있음을 알았다. 존은 파이프를 통과하는 유량을 계산하고 싶다.
#
# 두개의 배수관이 한줄로 연결 돼 있을 때 두 관의 유량 중 최솟값으로 흐르게 된다. 예를 들어 용량이 5인 파이프가 용량이 3인 파이프와 연결되면 한개의 용량 3짜리 파이프가 된다.
#
#   +---5---+---3---+    ->    +---3---+
#
# 게다가, 병렬로 연결돼 있는 배수관들은 각 용량의 합만큼의 물을 보낼 수 있다.
#
#     +---5---+
#  ---+       +---    ->    +---8---+
#     +---3---+
#
# 마지막으로, 어떤 것에도 연결돼 있지 않은 파이프는 물을 흐르게 하지 못하므로 제거된다.
#
#     +---5---+
#  ---+               ->    +---3---+
#     +---3---+--
#
# 이로 인해 복잡하게 연결된 모든 배수관들은 한개의 최대 유량을 갖는 배수관으로 만들어진다.
#
# 주어진 파이프들의 맵으로부터 우물(A)와 외양간(Z) 사이의 유량을 결정하라.
#
# 각 노드의 이름은 알파벳으로 지어져 있다.
#
#                  +-----------6-----------+
#         A+---3---+B                      +Z
#                  +---3---+---5---+---4---+
#                          C       D
#
# 파이프 BC와 CD는 합쳐질 수 있다.
#
#                  +-----------6-----------+
#         A+---3---+B                      +Z
#                  +-----3-----+-----4-----+
#                              D
#
# 그러면 BD와 DZ 역시 합쳐질 수 있다.
#
#                  +-----------6-----------+
#         A+---3---+B                      +Z
#                  +-----------3-----------+
#
# 병렬 연결된 BZ 역시 합쳐진다.
#
#                  B
#         A+---3---+---9---+Z
#
# 그러면 AB와 BZ 역시 합쳐질 수 있고 용량 3인 배수관 하나가 만들어진다.
#
#         A+---3---+Z
#
# 한 파이프들의 집합을 읽고. 두개의 끝점을 가진 파이프로 만들어놓은 뒤 A부터 Z까지 흐르는 최대 유량을 계산하라. 모든 파이프들은 위의 규칙을 적용시켜 줄일 수 있다.
#
# i번째 파이프는 두개의 다른 노드 ai와 bi와 연결돼 있고 Fi (1 ≤ Fi ≤ 1,000)만큼의 유량을 갖는다. 알파벳은 같지만, 대소문자가 다르면 다른 문자이다. 파이프는 양방향으로 흐를 수 있다.

# 첫째 줄에 정수 N (1 ≤ N ≤ 700)이 주어진다. 둘째 줄부터 N+1번째 줄까지 파이프의 정보가 주어진다. 첫 번째, 두 번째 위치에 파이프의 이름(알파벳 대문자 또는 소문자)이 주어지고, 세 번째 위치에 파이프의 용량이 주어진다.

# 첫째 줄에 A에서 Z까지의 최대 유량을 출력한다.

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

def change(i):
    if i <= 'Z':
        return ord(i)-ord('A')
    return ord(i)-ord('a')+26

MAX_VERTEX = 52


capacity = [ [ 0 for _ in range(MAX_VERTEX) ] for _ in range(MAX_VERTEX) ]
flow = [ [ 0 for _ in range(MAX_VERTEX) ] for _ in range(MAX_VERTEX) ]
adj_list = [ [] for _ in range(MAX_VERTEX) ]

for _ in range(N):
    a, b, F = input().split()
    a, b = change(a), change(b)
    F = int(F)
    capacity[a][b] += F
    capacity[b][a] += F
    adj_list[a].append(b)
    adj_list[b].append(a)

total_flow = 0
source, sink = change('A'), change('Z')
while True:
    # find an augment path
    parent = [ -1 for _ in range(MAX_VERTEX) ]
    q = deque()
    q.append(source)

    while q and parent[sink] == -1:
        v = q.popleft()

        for next_v in adj_list[v]:
            if parent[next_v] == -1 and (capacity[v][next_v] - flow[v][next_v]) > 0:
                q.append(next_v)
                parent[next_v] = v

    # if there is no augment path, exit
    if parent[sink] == -1:
        break

    # find maximum amount which can flow for the augment path
    augment_path_max_amount = sys.maxsize
    v = sink
    while v != source:
        augment_path_max_amount = min(
            augment_path_max_amount,
            capacity[parent[v]][v] - flow[parent[v]][v]
        )
        v = parent[v]

    v = sink
    while v != source:
        flow[parent[v]][v] += augment_path_max_amount
        flow[v][parent[v]] -= augment_path_max_amount
        v = parent[v]

    total_flow += augment_path_max_amount

print(total_flow)


```
