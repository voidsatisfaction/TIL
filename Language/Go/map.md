# Map

## 맵

맵은 해시테이블로 구현된다. 해시맵은 키와 값으로 되어있다. 키를 이용해서 값을 상수 시간에 가져올 수 있다. 대신에 순서는 존재하지 않는다.

**만일 해당 키가 없으면, 값의 자료형의 기본값을 반환한다.**

```go
// 이는 맵을 읽을 수는 있지만 변경할 수 없다.
var m map[keyType]valueType

// 맵의 생성
m := make(map[keyType]valueType)
m := map(keyType)valueType{}
```

### 맵 사용하기

```go
package count

func Count(s string, codeCount map[rune]int) {
	for _, r := range s {
		codeCount[r]++
	}
}

```

맵은 슬라이스와 다르게, 맵 변수 자체에 다시 할당하는 일이 없으므로, 포인터를 취하지 않아도 맵을 변경할 수 있다. 그래서 `codeCount *map[rune]int`로 쓸 필요가 없다. 물론 맵 자체를 다른 맵으로 바꿔치기하기 위해서는 포인터를 넘겨줘야하는데 이는 흔한 케이스가 아니다.

위와 같은 Count서브루틴은 어떻게 테스트 하면 좋을까? 맵은 순서가 없다.

```go
// 방법 1
func TestCount(t *testing.T) {
	codeCount := map[rune]int{}
	count.Count("가나다나", codeCount)
	if !reflect.DeepEqual(
		map[rune]int{'가': 1, '나': 2, '다': 1},
		codeCount,
	) {
		t.Error("codeCount mismatch:", codeCount)
	}
}

// 방법 2 - 하지만 지정한 키 이외의 다른 키가 있을경우는 잘못된 테스트가 될 가능성이 있다.
func ExampleCount() {
	codeCount := map[rune]int{}
	count.Count("가나다나", codeCount)
	for _, key := range []rune{'가', '나', '다'} {
		fmt.Println(string(key), codeCount[key])
	}
	// Output:
	// 가 1
	// 나 2
	// 다 1
}

// 방법 3
func ExampleCount() {
	codeCount := map[rune]int{}
	count("가나다나", codeCount)
	var keys sort.IntSlice
	for _, key := range keys {
		keys = append(keys, int(key))
	}
	sort.Sort(keys)
	for _, key := range keys {
		fmt.Println(string(key), codeCount[rune(key)])
	}
	// Output:
	// 가 1
	// 나 2
	// 다 1
}

```

### 집합

map을 이용하여 집합을 만들 수 있다.

```go
// 오버헤드가 있는 set(bool때문에 그럼)
func HasDupeRune(s string) bool {
	runeSet := map[rune]bool{}
	for _, r := range s {
		if runeSet[r] {
			return true
		}
		runeSet[r] = true
	}
	return false
}

// 오버헤드가 없는 set: 빈 구조체를 넘겨준다.
func HasDupeRune(s string) bool {
	runeSet := map[rune]struct{}{}
	for _, r := range s {
		if _, exists := runeSet[r]; exists {
			return true
		}
		runeSet[r] = struct{}{}
	}
	return false
}

```

`srcut{}`는 아무런 필드가 없는 구조체이므로, 값이 아니라 자료형이다.

삭제는 `delete(m, key)`이렇게 한다.

맵의 키에는 변경될 수 있는 것들이 들어가면 안된다. 왜냐하면 해시 테이블이 깨지기 때문이다.
