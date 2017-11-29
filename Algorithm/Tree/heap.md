# Heap

힙이란, 완전 이진트리의 특별한 형태를 말한다.

최소 힙과 최대 힙이 있다.

최소힙은 부모의 노드가 자식의 노드보다 항상 작은 특성을 만족하며, (최대 힙은 그의 반대) 왼쪽 서브트리부터 채워나가는것이 특징이다.

이를 응용하면 우선순위 큐를 만들 수 있다.

(평가 함수만 다르게 해 주면 되니까)

## 구현

보통 배열을 이용해서 구현합니다. 왜냐하면 힙의 마지막 노드의 위치를 빠르게 알 수 있고, 완전 이진 트리이므로 따로 링크를 보관하지 않아도 되기 떄문이다.

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

```go
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type minHeap []int

func (mh *minHeap) swap(i, j int) {
	(*mh)[i], (*mh)[j] = (*mh)[j], (*mh)[i]
}

func (mh *minHeap) insert(n int) {
	l := len(*mh)
	(*mh) = append((*mh), n)

	currentIndex := l
	parentIndex := (l - 1) / 2
	for currentIndex > 0 && (*mh)[parentIndex] > (*mh)[currentIndex] {
		mh.swap(currentIndex, parentIndex)
		currentIndex = parentIndex
		parentIndex = (currentIndex - 1) / 2
	}
}

func (mh *minHeap) pop() int {
	l := len(*mh)
	if l == 0 {
		return 0
	}
	temp := (*mh)[0]

	mh.swap(l-1, 0)
	(*mh) = (*mh)[:l-1]

	currentIndex := 0
	leftChildIndex := 1
	rightChildIndex := 2
	l--

	for {
		nextChildIndex := 0
		if leftChildIndex >= l {
			break
		}

		if rightChildIndex >= l {
			nextChildIndex = leftChildIndex
		} else {
			if (*mh)[leftChildIndex] < (*mh)[rightChildIndex] {
				nextChildIndex = leftChildIndex
			} else {
				nextChildIndex = rightChildIndex
			}
		}

		if (*mh)[nextChildIndex] < (*mh)[currentIndex] {
			mh.swap(nextChildIndex, currentIndex)
			currentIndex = nextChildIndex
		} else {
			break
		}
		leftChildIndex = 2*currentIndex + 1
		rightChildIndex = 2*currentIndex + 2
	}

	return temp
}

func (mh *minHeap) top() int {
	if len(*mh) > 0 {
		return (*mh)[0]
	}
	return 0
}

func main() {
	var N int
	s := bufio.NewScanner(os.Stdin)
	fmt.Scanf("%d", &N)
	mh := make(minHeap, 0, N)
	for i := 0; i < N; i++ {
		s.Scan()
		x, err := strconv.Atoi(s.Text())
		if err != nil {
			fmt.Printf("%+v", err)
			return
		}
		if x > 0 {
			mh.insert(x)
		} else {
			fmt.Printf("%d\n", mh.pop())
		}
	}
}

```
