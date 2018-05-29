# Sort기초

모든 Sort알고리즘을 Golang으로 구현. 기본적으로 다음과 같은 인터페이스를 갖고 있다:

```go
import (
    "fmt"
    "time"
    "math/rand"
)

const (
    MaxN = 10000
)

// interface for sorting
type Sortable interface {
    Len() int
    Less(i int, j int) bool
    Swap(i int, j int)
}

type ListOfInt []int

func (loi *ListOfInt) Len() int {
    return len(*loi)
}

func (loi *ListOfInt) Less(i int, j int) bool {
    return (*loi)[i] < (*loi)[j]
}

func (loi *ListOfInt) Swap(i int, j int) {
    (*loi)[i], (*loi)[j] = (*loi)[j], (*loi)[i]
}

func (loi *ListOfInt) Push(x interface{}) {
    (*loi) = append((*loi), x.(int))
}

func (loi *ListOfInt) Pop() interface{} {
    old := (*loi)
    n := old.Len()
    top := old[n-1]
    (*loi) = old[0:n-1]

    return top
}

// for making initial random number list
func makeRandomList(size int) *ListOfInt {
    rand.Seed(time.Now().UnixNano())

    loi := make(ListOfInt, 0, size)
    for i := 0; i < size; i++ {
        n := rand.Intn(size)
        loi = append(loi, n)
    }
    return &loi
}
```

## Selection Sort

```go
func (loi Sortable) SelectionSort {
  for i := 0; i < loi.Len(); i++ {
    for j := i+1; j < loi.Len(); j++ {
      if loi.Less(j, i) {
        loi.Swap(i, j)
      }
    }
  }
}
```

## Insertion Sort

```go
func InsertSort(loi Sortable) time.Duration {
    start := time.Now()
    for i := loi.Len()-1; i >= 1; i-- {
        for j := 1; j <= i; j++ {
            if loi.Less(j, j-1) {
                loi.Swap(j-1, j)
            }
        }
    }
    return time.Since(start)
}
```

## Merge Sort

```go
func MergeSort(loi ListOfInt) (time.Duration, ListOfInt) {
    var mergeSort func(loi ListOfInt) ListOfInt

    merge := func(loi1, loi2 ListOfInt) ListOfInt {
        size, i, j := loi1.Len()+loi2.Len(), 0, 0
        mergedLoi := make(ListOfInt, 0, size)
        for i+j < size {
            if i == size/2 {
                mergedLoi = append(mergedLoi, loi2[j])
                j++
            } else if j == size/2 {
                mergedLoi = append(mergedLoi, loi1[i])
                i++
            } else if loi1[i] <= loi2[j] {
                mergedLoi = append(mergedLoi, loi1[i])
                i++
            } else if loi2[j] < loi1[i] {
                mergedLoi = append(mergedLoi, loi2[j])
                j++
            }
        }
        return mergedLoi
    }

    mergeSort = func(loi ListOfInt) ListOfInt {
        if loi.Len() == 1 {
            return loi
        }
        mid := loi.Len() / 2
        loi1 := mergeSort(loi[:mid])
        loi2 := mergeSort(loi[mid:])
        return merge(loi1, loi2)
    }

    start := time.Now()
    ans := mergeSort(loi)
    return time.Since(start), ans
}
```

## Heap Sort

```go
type Heap interface {
    Sortable
    Push(x interface{})
    Pop() interface{}
}

// min heap
func up(h Heap, i int) {
    for {
        p := (i - 1) / 2
        if i == 0 || h.Less(p, i) {
            break
        }
        h.Swap(i, p)
        i = p
    }
}

func down(h Heap, i, n int) {
    for {
        cLeft, cRight := (2*i) + 1, (2*i) + 2
        minIndex := cLeft
        if cLeft > n { // there is no child node
            break
        }
        if cRight <= n && h.Less(cRight, cLeft) { // there are left and right children Nodes
            minIndex = cRight
        }
        if !h.Less(minIndex, i) {
            break
        }

        h.Swap(minIndex, i)
        i = minIndex
    }
}

func Push(h Heap, x interface{}) {
    h.Push(x)
    up(h, h.Len()-1)
}

func Pop(h Heap) interface{} {
    lastIndex := h.Len()-1
    h.Swap(0, lastIndex)
    down(h, 0, lastIndex-1)
    return h.Pop()
}

func HeapSort(loi ListOfInt) time.Duration {
    start := time.Now()

    h := make(ListOfInt, 0, loi.Len())
    for num := range loi {
        Push(&h, num)
    }

    for i := 0; i < loi.Len(); i++ {
        num := (Pop(&h)).(int)
        loi[i] = num
    }

    return time.Since(start)
}
```

## Quick Sort

```go
func quickSort(loi Sortable) time.Duration {
    var quickSortRec func(low, high int)

    quickSortRec = func(low, high int) {
        if low >= high {
            return
        }
        i, lt, gt := low+1, low, high
        for i <= gt {
            if loi.Less(i, lt) {
                loi.Swap(lt, i)
                lt++
                i++
            } else if loi.Less(lt, i) {
                loi.Swap(i, gt)
                gt--
            } else {
                i++
            }
        }
        quickSortRec(low, lt-1)
        quickSortRec(gt+1, high)
    }

    start := time.Now()
    quickSortRec(0, loi.Len()-1)
    return time.Since(start)
}
```
