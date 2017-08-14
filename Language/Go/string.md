# 문자열

## 문자열

문자열은 바이트들이 연속적으로 나열되어 있는 것이다. Go에서는 String이라는 자료형을 이용한다. 바이트들의 연속을 나타내는 방식으로는 []byte가 있다.

### 유니코드 처리

전 세계 모든 문자를 일관되게 표현하기 위한 산업 표준.

Go언어의 소스 코드는 UTF-8이다. 따라서 소스 코드안의 문자열도 UTF-8로 인코딩 되어있다.

```go
package main

import "fmt"

func main() {
	for i, r := range "가나다" {
		fmt.Println(i, r)
	}
	fmt.Println(len("가나다")) // 문자열의 길이 => 바이트 단위로 9바이트
}

// 0 44032
// 3 45208
// 6 45796
// 9
```

i는 `int`, r은 `rune(int32)`로 유니코드 포인트 하나를 담을 수 있다.

```go
for _, r := range "가갛힣" {
  fmt.Println(string(r), r)
}
```

`string()`로 해당 코드 포인트의 유니코드 문자열로 변환.

**마지막 문자에 받침이 있는지 없는지 확인하는 소스**

```go
// 마지막 문자에 받침이 있는지 없는지 확인하는 소스
// hangul.go
package hangul

var (
  start = rune(44032)
  end = rune(55204)
)

func HasConsonantSuffix(s string) bool {
  numEnds := 28
  result := false
  for _, r := range s {
    if start <= r && r < end {
      index := int(r-start)
      result = index%numEnds != 0
    }
  }
  return result
}

```

### 번외) 테스트 코드 작성

#### 1. 일반 테스트

```go
// hangul_test.go
package hangul

import "testing"

func TestHasConsonantSuffix(t *testing.T) {
  cases := []struct {
    in string
    want bool
  }{
    {"Go 언어", false},
    {"그럼", true},
    {"우리 밥 먹고 합시다.", false},
  }
  for _, s := range cases {
    got := HasConsonantSuffix(s.in)
    if got != s.want {
      t.Errorf("HasConsonantSuffix(%q) == %q, want %q", s.in, got, s.want)
    }
  }
}
```

#### 2. example 테스트

...

### 바이트 단위 처리

바이트 단위로 출력 UTF-8은 한 문자당 3바이트(2^8)로 표현

```go
func Example_printBytes() {
  s := "가나다"
  for i := 0; i < len(s); i++ {
    fmt.Println("%x:", s[i]) // ea:b0:80:eb:82:98:eb:8b:a4
  }
  fmt.Println()
}
```

더 간단한 표현

```go
func Example_printBytes2() {
  s := "가나다"
  fmt.Printf("%x\n", s) // eab080eb8298eb8ba4
  fmt.Printf("% x\n", s) // ea b0 80 eb 82 98 eb 8b a4
}
```

문자열을 아에 바이트 단위의 슬라이스로 변환

```go
func Example_modifyBytes() {
  b := []byte("가나다")
  b[2]++
  fmt.Println(string(b)) // 각나다
}
```

어떠한 문자들이 들어있는지를 중시한다면 `string`

실제 바이트 표현이 어떤지를 중시한다면 `[]byte`를 이용하는 것이 좋다.

### 문자열 잇기

문자열을 잇는 방법은 다음과 같다

```go
package main

import (
	"fmt"
	"strings"
)

func Example_strCat1() {
	s := "abc"
	ps := &s
	s += "def" // 간단한 문자열을 이어 붙이기 좋다.
	fmt.Println(s)
	fmt.Println(*ps)
}

func Example_strCat2() {
	s := "abc"
	s = fmt.Sprint(s, "def") // 반드시 문자열이 아닌 것들도 마치 다른 Print계열처럼 서로 이어붙일 수 있다.
	fmt.Println(s)
}

func Example_strCat3() {
	s := "abc"
	s = fmt.Sprintf("%sdef", s) // 형 선택 가능.
	fmt.Println(s)
}

func Example_strCat4() {
	s := "abc"
	s = strings.Join([]string{s, "def"}, "") // 구분자를 넣어서 이어 붙이기 좋다.
	fmt.Println(s)
}

func main() {
	Example_strCat1()
	Example_strCat2()
	Example_strCat3()
	Example_strCat4()
}

```

### 문자열을 숫자로

```go
var i int
var k int64
var f float64
var s string
var err error
i, err = strconv.Atoi("350") // i == 350
k, err = strconv.ParseInt("cc7fdd", 16, 32) // k == 13402077
k, err = strconv.PraseInt("0xcc7fdd", 0, 32) // k == 13402077
f, err = strconv.ParseFloat("3.14", 64) // f == 3.14
s = strconv.Itoa(340) // s == "340"
s = strconv.FormatInt(13402077, 16) // s == "cc7fdd"
```

다른 방법(fmt이용)

```go
var num int
fmt.Sscanf("57", "%d", &num) // num == 57

var s string
s = fmt.Sprint(3.14) // s == "3.14"
s = fmt.Sprintf("%x", 13402077) // s == "cc7fdd"
```

### rune vs string 꿀팁

```go
func ExampleDeleteMap() {
	src := map[rune]int{'가': 1, '갈': 3, '갱': 5}
	delete(src, '갈')
	fmt.Println(src['가'])
	fmt.Println(src['갈'])
	dst := map[string]int{"고": 1}
	fmt.Println(dst["고"])
	// Output:
	// 1
	// 0
	// 1
}
```

위의 코드에서 알 수 있듯이, 단따옴표는 unicode의 `rune`을 뜻하며, 쌍따옴표는 `string`을 나타내는 것을 알 수있다.
