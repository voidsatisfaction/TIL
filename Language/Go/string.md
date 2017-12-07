# 문자열(string)

문자열을 제대로 이해하기 위해서는 difference between a byte, a character, and a rune, the difference between Unicode and UTF-8, the difference between a string and a string literal, and other even more subtle distinctions.

## 참고

- [strings - go blog](https://blog.golang.org/strings)
- [디스커버리go - book]

## 문자열

문자열은 **임의의(arbitrary) 바이트들이 연속적으로 나열되어 있는 것이다(slice of bytes)**. 이것은 문자열이 항상 unicode text, utf-8 text나 다른 미리 정의되어진 형식이 아니어도 된다는 것을 의미한다. Go에서는 String이라는 자료형을 이용한다. 바이트들의 연속을 나타내는 방식으로는 `[]byte`가 있다.

### 문자열 출력하기

다음과 같은 경우를 생각하자.

```go
const sample = "\xbd\xb2\x3d\xbc\x20\xe2\x8c\x98"
fmt.Println(sample) // ��=� ⌘
```

sample string의 몇몇 bytes들은 유효한 ASCII도, UTF-8도 아니기 때문에, 이 문자열을 그대로 출력하면 이상한 결과를 보여줄 것이다.

그러므로, 문자열이 진정 무엇을 갖고 있는지 확인하려면, 각각으로 쪼개서 확인해야 한다.

```go
for i := 0; i < len(sample); i++ {
	fmt.Printf("%x ", sample[i])
	// bd b2 3d bc 20 e2 8c 98
}
```

위의 예에서는, **각각의 bytes에 접근**한 것이지, 글자에 접근한 것이 아니다.

```go
fmt.Printf("% x\n", sample)
// %와 x사이에 스페이스를 두는 트릭
// bd b2 3d bc 20 e2 8c 98

fmt.Printf("%q\n", sample)
// 보다 이해하기 쉽게 바이트를 출력한다(escape non-printable byte sequences)
// \xbd\xb2=\xbc ⌘

fmt.Printf("%+q\n", sample)
// +q는 UTF-8만 해석하며, non-printable sequences와 non-ASCII bytes를 escape한다.
// \xbd\xb2=\xbc \u2318
```

### UTF-8과 string literals

```go
func main() {
    const placeOfInterest = `⌘`

		// Plain string
    fmt.Printf("plain string: ")
    fmt.Printf("%s", placeOfInterest) // ⌘
    fmt.Printf("\n")

		// ASCII-only quoted string
    fmt.Printf("quoted string: ")
    fmt.Printf("%+q", placeOfInterest) // \u2318
    fmt.Printf("\n")

		// bytes in hexadecimal
    fmt.Printf("hex bytes: ")
    for i := 0; i < len(placeOfInterest); i++ {
        fmt.Printf("%x ", placeOfInterest[i])
    }
		// e2 8c 98
    fmt.Printf("\n")
}
```

| 분류 | 내용|
| :-- | --- |
| plain string | ⌘ |
| bytes | e2 8c 98  |
| UTF-8 | \u2318 |

Go의 소스코드는 UTF-8 이기 때문에, string literal의 소스 코드 역시 UTF-8 text이다. raw string(back quote로 된 문자열)은 언제나 UTF-8을 내용을 갖고 있는다. 유사하게, UTF-8을 망가뜨리는 escape가 없는 일반적인 string literal은 항상 유효한 UTF-8을 내용으로 갖는다.

Go의 string이 항상 UTF-8인게 아니고, string literals가 UTF-8이다.

요약하자면, strings는 임의의 바이트들을 포함할 수 있는데, string literals로 부터 만들어졌을때, 그러한 bytes들은 거의 항상 UTF-8이다.

**참고: 영어는 1바이트 아시아문자는 3바이트**

### Code points, characters, and runes

Unicode 표준에서는 **code point** 라는 말을 쓰며, 이는 단일 값에 대한 item을 나타낸다. 앞서 예제에서는 코드포인트 `U+2318`는 symbol`⌘`를 나타낸 것이다. 마찬가지로 a의 유니코드 코드포인트는 `U+0061`이다.

하지만, à는 `U+00E0`이라는 코드 포인트를 갖고 있으면서도, grave accent의 코드 포인트 `U+0300`과 소문자 a `U+0061`의 합성으로 생성될 수 있다. 결국 different sequences of UTF-8 bytes로 생성될 수 있다는 얘기이다.

이렇게 컴퓨팅에서 `character`라는 개념은 매우 혼란스럽기 때문에, 언어 사용의 주의를 요한다. 물론 `normalization`이라는 기술을 사용해서 주어진 character가 항상 하나의 코드 포인트를 나타내도록 할 수 있으나, 이는 나중에 언급하겠다.

사실 코드포인트는 말하기 기므로, Go에서는 `rune`이라는 새로운 개념을 도입했다. 이 rune은 바로 코드포인트와 같은 말이다.

`rune === code point === int32 (golang)`

주의할점은 유니코드의 코드 포인트는 16진수이나, golang에서의 rune은 10진수이므로 변환해서 생각해야한다.

`a == U+0061 == 97(rune)`

고언어에서는 character constant(⌘와 같은것들)을 `rune constant`라고 부른다.

- Go source code is always UTF-8.
- A string holds arbitrary bytes.
- A string literal, absent byte-level escapes, always holds valid UTF-8 sequences.
- Those sequences represent Unicode code points, called runes.
- No guarantee is made in Go that characters in strings are normalized.

### Range loops

string은 바이트의 슬라이스이기 때문에, 단순히 `for루프`로 출력하면 byte가 출력되나, `for range`로 출력하게 되면, `코드포인트`(UTF-8-encoded rune)가 나온다. 여기서 `index`는 현재 rune의 **바이트상의 시작 위치**를 나타낸다.

```go
const nihongo = "日本語"
for index, runeValue := range nihongo {
		fmt.Printf("%#U starts at byte position %d\n", runeValue, index)
}
// U+65E5 '日' starts at byte position 0
// U+672C '本' starts at byte position 3
// U+8A9E '語' starts at byte position 6
```

### Libraries

`for range`로도 UTF-8 텍스트를 해석하기 힘들면, library를 이용할 수 있다.

아래는 그에 대한 예시

```go
const nihongo = "日本語"
for i, w := 0, 0; i < len(nihongo); i += w {
	 runeValue, width := utf8.DecodeRuneInString(nihongo[i:])
	 fmt.Printf("%#U starts at byte position %d\n", runeValue, i)
	 w = width
}
// U+65E5 '日' starts at byte position 0
// U+672C '本' starts at byte position 3
// U+8A9E '語' starts at byte position 6
```

### 결론

- String은 바이트들의 슬라이스이다. 그러므로 그들의 indexing의 결과값은 바이트다. 문자가아님.
- 하나의 String은 문자를 전혀 갖고있지 않을 수 있고, 애초에 문자라는 개념 자체가 애매하므로 용어 사용을 지양한다.
- Go는 코드자체가 UTF-8이기 때문에, Unicode, UTF-8 에서의 코드 포인트 개념을 사용한다.

---

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

**위의 코드에서 알 수 있듯이, 단따옴표는 unicode의 `rune`을 뜻하며, 쌍따옴표는 `string`을 나타내는 것을 알 수있다.**
