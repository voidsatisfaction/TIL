# Sort기초

모든 Sort알고리즘을 Golang으로 구현. 기본적으로 다음과 같은 인터페이스를 갖고 있다:

```go
type Comparable interface{
  Less(i, j int) bool // i번째 요소가 j번쨰 요소 보다 작은가?
  Len() int // Comparable의 요소의 개수
  Swap(im j int) //
}
```

## Selection Sort

```go
func (a Comparable) SelectionSort {
  for i := 0; i < a.Len(); i++ {
    for j := i+1; j < a.Len(); j++ {
      if a.Less(j, i) {
        a.Swap(i, j)
      }
    }
  }
}
```

## Insertion Sort

## Merge Sort

## Quick Sort

## Heap Sort
