# Heap

힙이란, 완전 이진트리의 특별한 형태를 말한다.

최소 힙과 최대 힙이 있다.

최소힙은 부모의 노드가 자식의 노드보다 항상 작은 특성을 만족하며, (최대 힙은 그의 반대) 왼쪽 서브트리부터 채워나가는것이 특징이다.

이를 응용하면 우선순위 큐를 만들 수 있다.

(평가 함수만 다르게 해 주면 되니까)

## 구현

보통 배열을 이용해서 구현한다. 왜냐하면 힙의 마지막 노드의 위치를 빠르게 알 수 있고, 완전 이진 트리이므로 따로 링크를 보관하지 않아도 되기 떄문이다.

그리고 어떠한 노드 n(n > 0)의 부모는 `(n-1) / 2`로 바로 알 수 있다.

자식노드의 경우 왼쪽 노드는 `2*n + 1` 오른쪽 노드는 `2*n -1`이다.

## 최소 힙의 삽입

1. 일단 트리의 가장마지막 요소, 즉 배열의 마지막 원소 위치에서 그 뒤에 값을 삽입한다.
2. 그 값을 기준으로 부모 노드와 값의 크기를 비교하여 값이 자신의 값이 더 작은 경우에 위치를 바꿔준다.
3. 이를 계속 수행한다(자신이 루트노드이거나, 부모노드가 더 작은 경우까지)

## 최소 힙의 삭제(가장 작은 원소의 삭제)

1. 배열의 마지막 원소 위치에 있는 값을 가장 위에 있는 값이랑 바꿔치기 하고 마지막 값을 `null`로 변경
2. 현재 노드를 루트노드로 설정
3. 다음을 반복한다. 루트 노드(현재의 노드)와 각각의 자식 노드와의 값을 비교한다. 이때, 1) 자식 노드가 둘다 존재하지 않는경우 2) 왼쪽 자식만 존재하는 경우 3) 둘 다 존재하는 경우 를 생각해서 자식 노드 중 비교할 노드를 정한다.
3. 비교할 노드의 값이 현재의 노드보다 작은 경우 두 값을 바꿔치기한다.
4. 더 이상 비교할 수 있는 노드가 없어질때나, 현재의 노드의 값이 비교할 노드의 값보다 작으면 그만둔다.

## 효율

- Insert: O(logn)
- Delete: O(logn)
- 최소(혹은 최대)값 찾기: O(1)

## 참고

몰랐는데, go언어에서는 `conatiner/heap`패키지에서 이미 지원해주고 있다. 인터페이스로 되어있어서 알맞는 매서드만 추가해주면 된다.

## 예시코드(최소힙)

모듈

```go
package heap

import "sort"

type Interface interface {
	sort.Interface
	Push(x interface{})
	Pop() interface{}
}

func Init(h Interface) {
	n := h.Len()
	for i := n/2 - 1; i >= 0; i-- {
		down(h, i, n)
	}
}

func Push(h Interface, x interface{}) {
	h.Push(x)
	up(h, h.Len()-1)
}

func Pop(h Interface) interface{} {
	lastIndex := h.Len() - 1
	h.Swap(0, lastIndex)
	down(h, 0, lastIndex)
	return h.Pop()
}

func up(h Interface, i int) {
	for {
		p := (i - 1) / 2
		if i == 0 || h.Less(p, i) {
			break
		}
		h.Swap(i, p)
		i = p
	}
}

func down(h Interface, i, n int) {
	for {
		l := 2*i + 1
		if l >= n {
			break
		}
		if l+1 < n && h.Less(l+1, l) {
			l++
		}
		if !h.Less(l, i) {
			break
		}
		h.Swap(i, l)
		i = l
	}
}

```

모듈을 부른 코드

```go
package heapTest

import (
	"testing"

	"../pkg/heap"
)

type DummyIntHeap []int

func (h DummyIntHeap) Len() int {
	return len(h)
}

func (h DummyIntHeap) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h DummyIntHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *DummyIntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *DummyIntHeap) Pop() interface{} {
	old := *h
	n := old.Len()
	top := old[n-1]
	*h = old[0 : n-1]
	return top
}

func TestHeap(t *testing.T) {
	h := &DummyIntHeap{}
	heap.Push(h, 1)
	heap.Push(h, -1)
	heap.Push(h, 3)
	v := heap.Pop(h)

	if v != -1 {
		t.Errorf("heap.Pop() method is not right")
		t.Errorf("Expect: %d, got: %d", -1, v)
	}

	h = &DummyIntHeap{1, 7, 9, 3, 2, 2, 5, 4, 6, 8}
	heap.Init(h)
	expected := []int{1, 2, 2, 3, 4, 5, 6, 7, 8, 9}
	for i := 0; h.Len() > 0; i++ {
		v := heap.Pop(h)
		if expected[i] != v {
			t.Errorf("Expected: %+v, got: %+v\n", expected, *h)
			break
		}
	}
}

```
