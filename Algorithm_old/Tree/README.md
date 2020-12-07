# 트리

트리 기초

## 종류

- [이진 탐색 트리 - Binary Search Tree](./Binary_search_tree/README.md)

## 정의

폐로가 없는 연결 그래프.

내부를 루트노드, 부모노드, 자식노드, 잎노드, 내부노드 등의 노드로 분리한다.

## 생성

1. 배열을 이용한 순차적 표현
2. 연결리스트를 이용한 연결적 표현

### 1. 배열을 이용한 표현

```c++
// 노드의 구조(여기서는 이진트리를 생각)
struct node {
  int left;
  int right;
};

// 트리 생성
node tree[MAX];

// 각각의 노드들을 키에 대응하는 트리배열의 index에 넣어줌
tree[nodeNum] = node

// 트리 탐색
tree[root] ~
```

- 장점: 복잡한 포인터나 insert함수 없이 간단하게 트리 생성 가능. 특정 노드에 바로 접근 가능.
- 단점: MAX의 수가 너무 커지면 비효율적임. 또한, 포화 트리가 아닐경우에는 공간적인 비효율이 생김. 삽입 삭제가 비효율적임.

### 1.5 배열과 해시를 이용한 표현

포화트리의 공간적 비효율을 개선.

트리 배열에 노드를 순차적으로 배치한다. 그리고 노드의 키를 map의 키로대응하고 그 map의 키에대한 값에 현재 존재하는 배열의 인덱스를 저장.

위와 같이 하면 array의 불필요한 공간을 줄일 수 있으나 대신 해시를 복합적으로 사용하므로 노드의 수가 매우 많을 경우에는 시간적 비효율이 생길 수 있다.

```c++
// 노드의 구조(여기서는 이진트리를 생각)
struct node {
  int left;
  int right;
};

// 트리 생성
node tree[MAX];

// 각각의 노드들을 순서대로 트리배열에 넣어줌
tree <- node

// 노드가 존재하는 인덱스를 기억
map m;
m[nodeNum] = index

// 트리 탐색
tree[root] ~
```

### 2. 연결리스트를 이용한 표현

```c++
// 노드의 구조(여기서는 이진트리를 생각)
struct node {
  int num;
  node* left;
  node* right;
};

// 트리의 상층부
struct tree {
  node* root;
};

// 트리 생성
node root;
root.num = n;
root.left = nil;
root.right = nil;

tree t;
t.root = &root;
```

- 장점: 직관적으로 트리 표현 가능. 삽입 삭제에 용이. 공간적 비효율이 생기지 않음.
- 단점: 특정 노드에 접근하는 속도가 느림(탐색을 해야하므로)

## 종류
