# Tree

- 의문
- tree
- binary search tree
- self-blanacing binary search tree

## 의문

## tree

- 정의
  - cycle이 없이 모든 정점이 연결되어있는 그래프
- 특징
  - 노드의 개수가 N개인 경우, 간선은 N-1개

## binary search tree

- 정의
  - tree s.t. 각 노드의 키가 노드의 왼쪽 subtree의 모든 키보다 더 크고, 오른쪽 subtree의 모든 키보다 더 작음
- 특징
  - preorder traversal을 할 경우, 맨 처음으로 traverse하는게 root node, 그 바로 다음이 root의 left node, 그 뒤로 처음으로 root 노드의 key값보다 큰 값이 나오는 노드가 right node

## Self-balancing binary search tree

- 정의
  - binary search tree s.t. 임의의 아이템의 삽입과 삭제에 대해서 해당 높이를 자동으로 최소화 함
- 활용
  - ordered lists
  - priority queues
  - sets
- 특징
  - 해당 노드를 포함하여, 모든 subtree의 노드의 개수를 해당 노드에 기록함으로써, k번째 큰 노드를 시간복잡도 `O(logn)`에 구할 수 있음
