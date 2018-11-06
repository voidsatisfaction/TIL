# 자료구조 / 알고리즘

- 알고리즘 문제 해결 팁
  - 파인만 알고리즘
  - 문제 풀이과정은 노트에 정자로
- 자료구조
  - 자료구조의 정의
  - 추상적 자료형의 정의
  - 종류
    - 데이터 타입
    - 선형 데이터 구조
    - 비선형 데이터 구조
- 알고리즘(기초)
  - 정의
  - 분류
    - 패러다임에 따른 분류
    - 구현에 따른 분류
    - 최적화 문제 해법에 따른 분류
    - 프로그래밍 대회를 위한 분류
      - 정렬
      - 탐색
      - 그래프
        - 최단거리
        - 최소 신장 트리
        - 최대 유량
        - Union find
      - 문자열
        - kmp

## 알고리즘 문제 해결 팁

- 파인만 알고리즘
  - 문제를 쓴다
  - 답을 생각한다
  - 답을 작성한다
- 문제 풀이과정은 노트에 정자로
  - **문제 풀이과정은 무조건 또박또박 정자로 쓰자**
    - 빠르게 풀려고 막 쓰지 말자
    - 아이디어에 휘말리지 말자
    - 코딩은 그냥 생각을 옮기는 작업에 불과
  - 사실 모든 문제 해결과정을 이렇게 또박또박 글로 쓰고, 제대로 설계해서 해결하는 것이 중요하다.

## 자료구조

### 자료구조(Data Structure)의 정의

추상적 자료형이 정의한 연산들을 구현한 구현체

### 추상적 자료형(Abstract Data Type)의 정의

알고리즘이 문제를 해결하는데 필요한 자료의 형태와 자료를 사용한 연산들을 수학적으로 정의한 모델

예) 스택의 예를 들면, 함수 호출을 관리하기 위해 후입선출의 성질을 가진 추상적 자료형이 필요하니 pop과 push를 가지도록 스택이라는 추상적 자료형을 정의하고, 그것을 구현해서 함수 호출을 관리하는데 사용하는 구현체, 즉 자료구조를 콜 스택이라고 부르는 것이다.

- 스택 ADT
  - top()
  - length()
  - pop()
  - push(e)
- 이 스택을 어떻게 구체적으로 구현할지는 리스트나 배열 둘 다 사용가능. 각각의 구현에 장단점이 존재함.

### 종류

분류하는 기준이 매우 다양하다. 여기서는 [위키피디아 - 영문](https://en.wikipedia.org/wiki/List_of_data_structures) 를 참조하도록 한다

#### 데이터 타입

- **구현 레벨에서의 타입은 프로그래밍 언어마다 차이가 있음**
  - 어떤 언어는 리스트가 원시 타입일 수 있음
  - js는 enum이 없음
- 원시 타입
  - Boolean
  - Character
  - Floating-point numbers
  - Fixed-point numbers
  - Integer
  - Reference(pointer or handle)
    - 일부는 pointer를 지원하지 않는다.
  - Enumerated type
    - consisting of a set of named values called elements, members, enumeral, or enumerators of the type.
- 복합 타입(Composite types) 혹은 원시 타입이 아닌 타입(Non-primitive type)
  - Array
  - Record(tuple, structure)
  - String(스트링)
  - Union
    - 같은 메모리 위치에 다양한 데이터 저장 가능
    - c.f) struct는 다양한 필드를 선형적으로 배치
    - *union의 활용?*
  - *Tagged union(variant)?*
- 추상 데이터 타입(ADT)
  - Container(collection)
    - 컴퓨터 공학에서 문제를 해결하기 위해서 어떠한 제어된 방식으로 다뤄야 하거나 함꼐 그룹화 해야하는 데이터 개체의 그룹
  - List
  - Tuple
  - Associative array
    - map, symbol table, dictionary
    - (key, value) pair
  - Multimap
  - Heap
  - Set
  - Multiset
  - Stack
  - Queue
  - Double-ended queue(Dequeue)
  - Priority queue
  - Tree
  - Graph

#### 선형 데이터 구조(Linear data structure)

- Array
  - *Bit array*
  - *Bit field*
  - *Bitboard*
  - *Bitmap*
  - *Circular buffer*
  - *Control table*
  - *Image*
  - *Dope vector*
  - *Dynamic array*
  - *Gap buffer*
  - *Hashed array tree*
  - *Heightmap*
  - *Lookup table**
  - *Matrix*
  - *Parallel array*
  - *Sorted array*
  - *Sparse matrix*
- Lists
  - Linked list
  - *Doubly linked list*
  - *Array list*
  - *Self-organizing list*
  - *Skip list*
  - *Unrolled linked list*
  - *VList*
  - *Conc-tree list*
  - *Xor linked list*
  - *Zipper*
  - *Doubly connected edge(half-edge)*
  - *Difference list*
  - *Free list*

#### 비선형 데이터 구조

- 트리
  - Binary trees
    - Binary search tree
    - Binary tree
    - *AVL tree*
  - B-trees
    - B-tree
    - 2-3 tree
  - Heaps
    - Heap
  - *Tries*
  - *Multiway trees*
  - Space-partitioning trees
    - Segment tree
  - Application-specific trees
- 해시 기반 구조
  - Hash table
  - *Hash tree*
  - *Hash array mapped trie*
  - *Hash trie*
  - *Koorde*
  - *Prefix hash tree*
  - *Rolling hash*
  - *MinHash*
  - *Quotient filter*
  - *Ctrie*
  - *Bloom filter*
  - *Count-Min sketch*
  - *Distributed hash table*
- 그래프
  - Adjacency list
  - Adjacency matrix
  - Directed graph
  - *Directed acyclic graph*
  - *Propositionally directed acyclic graph*
  - *Graph-structured stack*
  - *Scene graph*
  - *Decision tree*
    - *Binary dicision diagram*
  - *Zero-suppressed decision diagram*
  - *And-inverter graph*
  - *Multigraph*
  - *Hypergraph*
- 그 외
  - *Lightmap*
  - *Winged edge*
  - *Quad-edge*
  - *Routing table*
  - Symbol table
    - (key value)페어로 구성된 자료구조

|Structure|Order|Unique|
|---------|-----|------|
|List|yes|no|
|Associative array|no|yes|
|Set|no|yes|
|Multiset(bag)|no|no|

## 알고리즘

### 정의

### 분류

#### 디자인 패러다임에 따른 분류

- Brute-force / exhaustive search
- Divide and conquer
  - 하나의 문제를 쉽게 풀 수 있도록 작게 분할하고 그것을 다시 위로 해결해나감
  - e.g
    - Merge sort
- Search and enumeration
  - 주로 그래프 탐색
- Randomized algorithm
  - 선택을 임의로 함. 완벽한 해를 찾는것이 비현실적인 경우에 근사 해를 찾는데에 유용.
  - e.g
    - 몬테 카를로 알고리즘
- Reduction of complexity
  - 어려운 문제를 이미 알고 해법이 나름 최적화 되어있는 기존문제로 변형 후 해결하는 법
  - e.g
    - 정렬되지 않은 배열 안에서 median값을 구하기
      - 정렬 후 가운데 값을 구함
- Back tracking
  - 다양한 해법이 만들어지나, 유효한 해법으로 이어지지 않을 때 그 해법을 도중에 버리는 방식

#### 구현에 따른 분류

- 재귀
  - 어떠한 조건이 만족될 때 까지 반복적으로 그 자신을 호출
- *논리적*
  - 공리 + 컨트롤 컴포넌트
- 연속적, 병렬적 혹은 분산적
  - 다양한 프로세서를 이용한 알고리즘
- 결정적, 비결정적(단계가)
  - 알고리즘의 매 단계가 매우 정확한 결정으로 되어있는가
  - 휴리스틱한 결정을 내리는가
- 정확 혹은 근사(해답이)
  - 올바른 해답에 근접한 근사 알고리즘
  - e.g
    - 냅색 문제
- 퀀텀 알고리즘
  - 양자 컴퓨팅을 이용한 알고리즘

#### 최적화 문제 해법에 따른 분류

- *Linear programming*
- Dynamic programming
  - 문제의 해가 서브 문제의 최적 해로 구성되고(optimal substructures) & 같은 서브 문제들이 다른 많은 문제 인스턴스들을 해결되는 데에 사용 되면(overlapping subproblems)
  - 이미 푼 하위 문제를 다시 풀지 않고 테이블에 저장해서 다른 상위 문제를 푸는 데에 이용함
- The greedy method
  - 각 단계마다 부분 최적을 고르다가 보면 전체의 최적이 되는 것들
  - e.g
    - 허프만 코딩
    - Kruskal
    - Prim
- The heuristic method
  - 최적 해를 찾는 것이 비현실적일 경우에 사용
  - 무한정 시간으로 작동시키면 언젠가 최적 해를 찾음
  - 최적 해에 근접한 해를 비교적 적은 시간에 찾을 수 있는 장점
  - e.g
    - 유전 알고리즘
- By complexity
  - Constant time
  - Linear time
  - Logarithmic time
  - Polynomial time
  - Exponential time

#### 프로그래밍 대회를 위한 분류
