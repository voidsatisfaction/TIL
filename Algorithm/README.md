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
    - 트리
    - 해시 기반 구조
    - 그래프
    - 그 외
- 알고리즘(기초)
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
  - 문제 풀이과정은 무조건 또박또박 정자로 쓰자
    - 빠르게 풀려고 막 쓰지 말자
    - 아이디어에 휘말리지 말자
    - 코딩은 그냥 생각을 옮기는 작업에 불과

## 자료구조

### 자료구조(Data Structure)의 정의

추상적 자료이 정의한 연산들을 구현한 구현체

### 추상적 자료형(Abstract Data Type)의 정의

알고리즘이 문제를 해결하는데 필요한 자료의 형태와 자료를 사용한 연산들을 수학적으로 정의 모델

예) 스택의 예를 들면, 함수 호출을 관리하기 위해 후입선출의 성질을 가진 추상적 자료형이 필요하니 pop과 push를 가지도록 스택이라는 추상적 자료형을 정의하고, 그것을 구현해서 함수 호출을 관리하는데 사용하는 구현체, 즉 자료구조를 콜 스택이라고 부르는 것이다.

- 스택 ADT
  - top()
  - length()
  - pop()
  - push(e)
- 이 스택을 어떻게 구체적으로 구현할지는 리스트나 배열 둘 다 사용가능. 각각의 구현에 장단점이 존재함.

### 종류

분류하는 기준이 매우 다양하다. 여기서는 [위키피디아 - 영문](https://en.wikipedia.org/wiki/List_of_data_structures) 를 참조하도록 한다

- 데이터 타입
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
- 선형 데이터 구조(Linear data structure)
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
