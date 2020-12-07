# Segment Tree

구간에 대한 정보를 효율적으로 탐색하고 갱신하기 위한 자료 구조. 구간의 최대값, 최소값, 현재의 수 보다 큰 수들의 개수 등을 시간적 복잡도 O(log(n))에 구할 수 있음

공간적 복잡도는 대략 O(4*n)이 소모

## API

- New
- Get
- Update

## 코드(Golang)

```go
package segmentTree

// This segment tree saves maximum value of certain segments
func max(nums ...int) int {
	maxNum := nums[0]
	for _, n := range nums {
		if n > maxNum {
			maxNum = n
		}
	}
	return maxNum
}

type segmentTree []int

func New(arr []int) segmentTree {
	segTree := make(segmentTree, 4*len(arr))

	st, ed := 0, len(arr)-1
	getMax(segTree, arr, st, ed, 1)
	return segTree
}

func getMax(segTree segmentTree, arr []int, st, ed, node int) int {
	if st == ed {
		segTree[node] = arr[st]
		return arr[st]
	}

	mid := (st + ed) / 2
	// You can customize this part according to function of your segment tree
	segTree[node] = max(
		getMax(segTree, arr, st, mid, 2*node),
		getMax(segTree, arr, mid+1, ed, 2*node+1),
	)
	return segTree[node]
}

func (segTree segmentTree) Get(st, ed, tst, ted, node int) int {
	if tst <= st && ted >= ed {
		return segTree[node]
	}

	if tst > ed || ted < st {
		return -987654321
	}

	mid := (st + ed) / 2
	if ted <= mid {
		return segTree.Get(st, mid, tst, ted, 2*node)
	} else if tst >= mid+1 {
		return segTree.Get(mid+1, ed, tst, ted, 2*node+1)
	} else {
		return max(
      segTree.Get(st, mid, tst, ted, 2*node),
      segTree.Get(mid+1, ed, tst, ted, 2*node+1),
    )
	}
}

func (segTree segmentTree) Update(st, ed, i, newVal, node int) int {
	if st == i && ed == i {
		segTree[node] = newVal
		return newVal
	}

	if i < st || i > ed {
		return -987654321
	}

	mid := (st + ed) / 2
	if i <= mid {
		segTree[node] = max(segTree.Update(st, mid, i, newVal, 2*node), segTree[2*node+1])
	} else if i >= mid+1 {
		segTree[node] = max(segTree[2*node], segTree.Update(mid+1, ed, i, newVal, 2*node+1))
	}
	return segTree[node]
}

```
