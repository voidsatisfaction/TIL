# Treaky Point

## 슬라이스와 append함수

```go
package main

import "fmt"

func main() {
	nums := []int{1, 2, 3}
	fmt.Println(len(nums)) // 3
	fmt.Println(cap(nums)) // 3

	nums0 := nums[:1]
	fmt.Println(len(nums0)) // 1
	fmt.Println(cap(nums0)) // 3
	fmt.Println(nums[2])    // 3

	nums1 := nums[1:]
	fmt.Println(len(nums1)) // 2
	fmt.Println(cap(nums1)) // 2

	nums2 := append(nums1, 5)
	fmt.Println(len(nums2)) // 3
	fmt.Println(cap(nums2)) // 4(왜 여기가 4인것인가?) 원래 capacity의 2배를 증가시켜줌.
}

```

다음의 코드를 보면 이해하기 쉽다.

```go
// len=0, cap=3 인 슬라이스
sliceA := make([]int, 0, 3)

// 계속 한 요소씩 추가
for i := 1; i <= 15; i++ {
  sliceA = append(sliceA, i)
  // 슬라이스 길이와 용량 확인
  fmt.Println(len(sliceA), cap(sliceA))
}

fmt.Println(sliceA) // 1 부터 15 까지 숫자 출력
```

위의 코드의 결과는 1~3까지는 기존의 용량3을 사용하고, 4~6 => 6, 7~12 => 12, 13~15 => 24의 슬라이스가 사용된다. 왜 이렇게 되는 지는 [공식문서](https://golang.org/src/runtime/slice.go#L105)를 참조하면 알 수 있다. 즉, 길이가 1024전에는 cap이 두배씩 늘어난다.

또하나 참고 하자면,

```go
package main

import "fmt"

func main() {
	nums := []int{1, 2, 3}
	fmt.Println(&nums[0], &nums[1], &nums[2]) // 0x1040a124 0x1040a128 0x1040a12c
	fmt.Println(len(nums)) // 3
	fmt.Println(cap(nums)) // 3
	nums0 := nums[:1]
	fmt.Println(&nums0[0]) // 0x1040a124
	fmt.Println(len(nums0)) // 1
	fmt.Println(cap(nums0)) // 3
	fmt.Println(nums[2])    // 3
	nums1 := nums[1:]
	fmt.Println(&nums1[0]) // 0x1040a128
	fmt.Println(len(nums1)) // 2
	fmt.Println(cap(nums1)) // 2
	nums2 := append(nums1, 5)
	fmt.Println(&nums2[0], &nums2[1], &nums2[2]) // 0x1040a160 0x1040a164 0x1040a168
	fmt.Println(len(nums2)) // 3
	fmt.Println(cap(nums2)) // 4

  nums3 := append(nums2, 1, 2, 3, 4, 5, 6, 7, 8)
	fmt.Println(&nums3[0], &nums3[1], &nums3[2])
	fmt.Println(len(nums3)) // 11
	fmt.Println(cap(nums3)) // 12

	nums4 := append(nums2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
	fmt.Println(&nums3[0], &nums3[1], &nums3[2])
	fmt.Println(len(nums4)) // 13
	fmt.Println(cap(nums4)) // 16
}

```

위에서 배열에 관한 포인터값을 보면 슬라이스가 capacity == len일때, append될 경우 새로운 슬라이스로 이사가는 것이 보인다.

그리고, 배열이 늘어날 경우 늘어난 만큼의 양을 **기존 배열의 capacity의 배수**로 커버한다. 위에서는, 원래 `nums2`의 사이즈가 4였으므로, 한번에 여러 요소가 늘어났을때에 4의 배수로 `capacity`가 증가하는것을 알 수 있다.
