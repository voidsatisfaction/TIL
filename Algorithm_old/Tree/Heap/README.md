# Binary Heap

- 키는 각 노드의 값을 나타낸다.
- 부모노드의 키는 무조건 자식노드의 키보다 크거나 같다.
- 배열 인덱스의 시작은 1부터(top)
- 각 레벨은 `2^l`의 인덱스부터 `2^(l+1) - 1`까지의 인덱스 범위를 갖는다.

## 필요한 API

- insert()
- popTop()

## 특징

현 노드의 인덱스를 `k`라고 하자.

- 부모 노드의 인덱스는 `k/2`
- 자식 노드의 인덱스는 `2*k` 그리고 `2*k+1`

```go
package heap

import (
	"sort"
)

type Interface interface {
	sort.Interface
	Push(x interface{})
	Pop() interface{}
}
```

### Swim: 자식 노드의 키가 부모 노드의 키보다 커졌을 경우 힙 유지

k번째 노드의 키가 그 부모 노드의 키 보다 클 경우(최대힙에서)

```go
func up(h Interface, k int) {
	for {
		p := (k - 1) / 2
		if p == k || !h.Less(k, p) {
			break
		}
		h.Swap(p, k)
		k = p
	}
}
```

### Push

```go
func Push(h Interface, x interface{}) {
	h.Push(x)
	up(h, h.Len()-1)
}
```

### Sink: 부모 노드의 키가 자식 노드의 키보다 더 작아졌을 경우 힙 유지

```go
func down(h Interface, k, n int) {
	for (2*k + 1) < n {
		j := 2*k + 1
		if j+1 < n && h.Less(j+1, j) {
			j++
		}
		if !h.Less(j, k) {
			break
		}
		h.Swap(k, j)
		k = j
	}
}
```

### Pop(top)

```go
func Pop(h Interface) interface{} {
	n := h.Len() - 1
	h.Swap(0, n)
	down(h, 0, n)
	return h.Pop()
}
```
