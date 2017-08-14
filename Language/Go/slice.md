# 배열과 슬라이스

## 배열과 슬라이스

배열과 슬라이스 모두 연속된 메모리 공간을 순차적으로 이용하는 자료구조. 주로 슬라이스를 이용하여 간접적으로 배열을 이용하는 경우가 많다.

### 배열

```go
func Example_array() {
	fruits := [3]string{"사과", "바나나", "토마토"}
	for _, fruit := range fruits {
		fmt.Printf("%s는 맛있다.\n", fruit)
	}
	// Output:
	// 사과는 맛있다.
	// 바나나는 맛있다.
	// 토마토는 맛있다.
}
```

컴파일러가 배열의 개수를 알아내어서 넣게 만들고 싶으면 `[3]string{ ... }`대신에 `fruits := [...]string {...}`와 같이 써도 된다.

### 슬라이스

배열이 크기가 자료형에 고정이 되어있다면, 슬라이스는 길이와 용량을 갖고 있고 길이가 변할 수 있는 구조이다.

```go
var fruits []string // 빈 슬라이스

fruits := make([]string, n) // 슬라이스에 몇개가 미리 들어갈지 아는 경우
```

#### 슬라이스 잘라내기

```go
func Example_slice_slicing() {
	nums := []int{1, 2, 3, 4, 5}
	fmt.Println(nums)
	fmt.Println(nums[1:3])
	fmt.Println(nums[2:])
	fmt.Println(nums[:3])
	// Output:
	// [1 2 3 4 5]
	// [2 3]
	// [3 4 5]
	// [1 2 3]
}
```

- 기본적으로 `[a:b]`가 있을 경우에는 a에서 b-1까지 라고 생각하면 된다.
- b나 a에는 음수가 들어갈 수 없다.
- 범위가 넘어가지 않도록 해야한다. 범위가 넘어가는 경우에는 패닉이 발생(다른 언어의 exception과 비슷)

#### 슬라이스 덧붙이기

```go
func Example_slice_append() {
	f1 := []string{"apple", "banana", "tomato"}
	f2 := []string{"grape", "strawberry"}
	f3 := append(f1, f2...) // js에서의 ...obj와 같은 역할을 한다.
	f4 := append(f1[:2], f2...)
	fmt.Println(f1)
	fmt.Println(f2)
	fmt.Println(f3)
	fmt.Println(f4)
	// Output:
	// [apple banana tomato]
	// [grape strawberry]
	// [apple banana tomato grape strawberry]
	// [apple banana grape strawberry]
}
```

- append함수는 가변인자를 받는 함수이다.
- `append(f1, f2...)`등과 같은 표현도 가능.

#### 슬라이스의 용량

슬라이스는 연속된 메모리 공간을 활용하는 것이라서 용량에 제한이 있을 수 밖에 없다. 남은 자리가 없는데 내용을 덧붙이고자 하면, 더 넓은 메모리 공간으로 이사를 가야하며, 전의 내용은 복사된다. 그리고 새로 이사한 공간 맨 뒤에 남는 공간에 덧붙이게 된다.

`make([]int, 5)`와 같이 다섯 개의 빈 공간을 미리 할당하거나, `[]int{0, 0, 0, 0, 0}`과 같이 다섯 개의 정수로 초기화한 경우에는 길이 뿐 아니라 용량도 5로 맞춰지게 된다. 공간 낭비가 없음. 하지만 여기서 요소를 더 추가하게 되면 내용 전체를 복사한 후 새로운 공간으로 이사간다.

용량을 알아보려면 `cap(x)`를 사용하면 된다.

```go
func Example_spliceCap() {
	nums := []int{1, 2, 3, 4, 5}

	fmt.Println(nums)
	fmt.Println("len:", len(nums))
	fmt.Println("cap:", cap(nums))
	fmt.Println()

	sliced1 := nums[:3]
	fmt.Println(sliced1)
	fmt.Println("len:", len(sliced1))
	fmt.Println("cap:", cap(sliced1))
	fmt.Println()

	sliced2 := nums[2:]
	fmt.Println(sliced2)
	fmt.Println("len:", len(sliced2))
	fmt.Println("cap:", cap(sliced2))
	fmt.Println()

	sliced3 := sliced1[:4]
	fmt.Println(sliced3)
	fmt.Println("len:", len(sliced3))
	fmt.Println("cap:", cap(sliced3))
	fmt.Println()

	nums[2] = 100
	fmt.Println(nums, sliced1, sliced2, sliced3)
	// Output:
	// [1 2 3 4 5]
	// len: 5
	// cap: 5
	//
	// [1 2 3]
	// len: 3
	// cap: 5
	//
	// [3 4 5]
	// len: 3
	// cap: 3
	//
	// [1 2 3 4]
	// len: 4
	// cap: 5
	//
	// [1 2 100 4 5] [1 2 100] [100 4 5] [1 2 100 4]
}
```

- 슬라이스의 slice는 완전히 새로운 슬라이스를 생성하는게 아니라, 기존의 슬라이스에서 일부를 떼낸 결과. 그렇기 때문에 용량은 뒤에 얼마나 덧붙일 공간이 있느냐에 따라서 결정되므로, 뒤에 두개를 잘라낸 경우 길이는 두개가 줄어들지만 용량은 여전히 5이다. 하지만, 앞에 2개를 잘라낸 경우에는 길이도 2줄어들고 뒤에 공간이 없으니까 용량도 3으로 줄게 된다.
- 잘라냈더라도 뒤의 공간이 있다면 그 공간을 살릴 수도 있다.(slice3의 예제)
- 슬라이는 사실 모두 동일한 메모리를 보고 있는것. 그러므로 `nums[2]`만 수정해도 다른 슬라이스 모두에서 변경이 일어난다.

슬라이스의 용량을 지정해서 생성

```go
// 길이 3인 용량 5 슬라이드 생성
nums := make([]int, 3, 5)

// 위와 같은 코드
nums := make([]int, 5)
nums = nums[:3]
```

빈 슬라이드를 예약 공간에 생성하고 싶은 경우

```go
nums := make([]int, 0, 15)
```

위의 코드는 용량 15 까지 예약해두었으므로, 그 전에 append해도 메모리 이사와 복사가 일어나지 않는다.

#### 슬라이스 내부 구현

- 슬라이스는 배열을 가지고 있는 구조체이다.
- 슬라이스는 **시작 주소**, **길이**, **용량**이라는 필드들로 이루어져 있다.
- 복사가 일어나서 이동이 일어났다고 했을 때에는 그 슬라이스는 다른 배열을 보고 있게 된다. 그래서 배열을 `append`함수에서 두 번 써주어야 한다.

```go
nums = append(nums, 10)
```

위의 코드에서 10을 뒤에 하나 추가하는 경우에는 일단 nums의 늘어난 길이가 용량을 초과할 것인지를 조사한다.

1. `len(nums) + 1 <= cap(nums)`즉, 용량을 초과하지 않는경우, 시작 위치에서 길이만큼 오른쪽으로 이동한 위치에 새로운 값을 집어넣고, 길이가 증가한 슬라이스를 반환한다. 길이가 증가한 슬라이스를 `nums`에 다시 할당해야 하므로 두 번 반복해서 써주어야 한다.
2. `len(nums) + 1 > caps(nums)`즉, 용량을 초과하는 경우, 더 큰 크기의 배열을 새로 하나 더 만들고 슬라이스도 거기에 맞게 고쳐서 반환한다. 마찬가지로 다시 `nums`에 할당해주어야 한다.

따라서 어떠한 경우라도 이 값을 받아야 한다. 원래의 실라이스는 길이가 늘어나지 않는다. 받지 않으면 컴파일 오류 발생.

#### 슬라이스의 copy

```go
func Example_sliceCopy() {
	src := []int{10, 20, 30, 40, 50}
	dest := make([]int, len(src))
	for i := range src {
		dest[i] = src[i]
	}
	fmt.Println(dest)
	// Output:
	// [10 20 30 40 50]
}
```

하지만 go에는 더 편한 함수가 이미 내장되어있다.

```go
// 슬라이스 전체 복사 1
src := []int{30, 20, 50, 10, 40}
dest := make([]int, len(src))
copy(dest, src)

// 슬라이스 전체 복사 2
src := []int{30, 20, 50, 10, 40}
dest := append([]int(nil), src...)

// 잘못된 복사(참조)
dest := src
```

#### 슬라이스의 삽입과 삭제

**삽입**

```go
// 방법 1
if i < len(a) {
   a = append(a[:i+1], a[i:]...)
   a[i] = x
} else {
  a = append(a, x)
}

// 방법 2
a = append(a, x)
copy(a[i+1:], a[i:]) // 메모리 상의 a에 b를 넣어준다.
a[i] = x
```

**삭제**

```go
// O(n)의 시간 복잡도
// 방법 1
a = append(a[:i], a[i+1:]...) // 1개만 삭제

// 방법 2
a = append(a[:i], a[i+k]...) // i로부터 k개 삭제

// O(1)의 시간 복잡도 but 순서가 뒤바뀜
// 1개만 삭제
a[i] = a[len(a)-1]
a = a[:len(a)-1]

// i로부터 k개 삭제
start := len(a)-k
if i+k > start {
  start = i+k
}
copy(a[i:i+k], a[start:])
a = a[:len(a)-k]
```

또한 삭제 시에 중요한 점은, 슬라이스 내부에 포인터가 있는 경우에는 이것이 뒤의 공간에 남아 있으면 가비지 컬렉션이 일어나지 않기때문에 메모리 누수가 일어난다(일반 값은 괜찮음)

따라서, 구조체 안에 잇는 포인터들을 nil로 초기화해주거나 아니면 아예 해당 구조체를 빈 구조체(포인터가 모두 nil이고 다른 필드들도 기본값이 되는 구조체)로 덮어쓰거나 해주어야 한다.

```go
// 하나만 지우는 경우
copy(a[i:], a[i+1:])
a[len(a)-1] = nil // 생략 시 메모리 누수 위험
a = a[:len(a)-1]

// 여러개를 지우는 경우
copy(a[i:], a[i+k:])
for i := 0; i < k; i++ {
  a[len(a)-1-i] = nil
}
a = a[:len(a)-k]
```

포인터를 포함한 구조체의 경우에는 위의 코드에서 `nil`대신에 구조체 이름을 T라고 하면 T{}을 넣어준다.

#### 슬라이스의 소팅

int를 요소로서 갖는 슬라이스를 소팅할 경우, 그냥`sort.Sort(slice)`하면 안된다. 왜냐하면, 슬라이스 자체는 sort하는 함수에 대응(인터페이스 개념인데 뭔지 잘 모르겠다 아직..)하지 않기 때문이다.

그러므로, 다음과 같이 해야한다.

```go
slice := []int{3, 2, 8, 1}
sort.Sort(sort.IntSlice(slice)) // [1 2 3 8]
```

그리고 [공식 문서](https://golang.org/pkg/sort/#Interface)를 보면, 아래와 같은 type Interface를 갖고 있으면 소팅할 수 있다고 한다.

```go
type Interface interface {
        // Len is the number of elements in the collection.
        Len() int
        // Less reports whether the element with
        // index i should sort before the element with index j.
        Less(i, j int) bool
        // Swap swaps the elements with indexes i and j.
        Swap(i, j int)
}
```

소팅하면 새로운 slice가 생성되는게 아니고, 기존의 슬라이스를 수정하는 것이므로 주의!

### 스택

Last In First Out. 슬라이스로도 충분히 구현이 가능하다.

삽입: `append`
삭제: 마지막 제거

```go
func Eval(expr string) int {
	var ops []string
	var nums []int
	pop := func() int {
		last := nums[len(nums)-1]
		nums = nums[:len(nums)-1]
		return last
	}
	reduce := func(higher string) {
		for len(ops) > 0 {
			op := ops[len(ops)-1]
			if strings.Index(higher, op) < 0 {
				return
			}
			ops = ops[:len(ops)-1]
			if op == "(" {
				return
			}
			b, a := pop(), pop()
			switch op {
			case "+":
				nums = append(nums, a+b)
			case "-":
				nums = append(nums, a-b)
			case "*":
				nums = append(nums, a*b)
			case "/":
				nums = append(nums, a/b)
			}
		}
	}
	for _, token := range strings.Split(expr, " ") {
		switch token {
		case "(":
			ops = append(ops, token)
		case "+", "-":
			reduce("+-*/")
			ops = append(ops, token)
		case "*", "/":
			reduce("*/")
			ops = append(ops, token)
		case ")":
			reduce("+-*/(")
		default:
			num, _ := strconv.Atoi(token)
			nums = append(nums, num)
		}
	}
	reduce("+-*/")
	return nums[0]
}

func ExampleEval() {
	fmt.Println(eval.Eval("5"))
	fmt.Println(eval.Eval("1 + 2"))
	fmt.Println(eval.Eval("1 - 2 + 3"))
	fmt.Println(eval.Eval("3 * ( 3 + 1 * 3 ) / 2"))
	fmt.Println(eval.Eval("3 * ( ( 3 + 1 ) * 3 ) / 2"))
	// Output:
	// 5
	// 3
	// 2
	// 9
	// 18
}
```
