## 입출력

Go의 입출력에 대한 표준 라이브러리는 `io`에 들어있다. 그리고, fmt패키지에 형식을 이용한 입출력도 구현되어 있다.

### io.Reader과 io.Writer

바이트들을 읽고 쓸 수 있는 인터페이스. fmt패키지에서는 F로 시작하는 함수들이 `io.Reader`와 `io.Writer`를 인자로 받는다.

```go
fmt.Fprintln(os.Stdout, s) == fmt.Println(s)
fmt.Fprintf(os.Stdout, format, ...) == fmt.Println(format, ...)
fmt.Scanf(foramt, ...) == fmt.Fscanf(os.Stdin, format, ...)
```

따라서 기본 입출력 역시 파일을 읽고 쓰는 것과 거의 동일한 방법으로 읽고 쓸 수 있다. 함수를 작성할 때, `io.Reader`혹은, `io.Writer`등을 받아서 처리하게 작성하면 표준 입출력, 파일, 네트워크 등 모두 적용할 수 있으며, 테스트 등을 할 떄 좋다.

### 파일 읽기

```go
f, err := os.Open("my_text.txt")
if err != nil {
	fmt.Println(err)
}
defer f.Close() // 해당 함수를 벗어날 때 호출할 함수를 등록
var num int
if _, err := fmt.Fscanf(f, "%d\n", &num); err == nil { // 하나만 읽으므로 몇개를 읽었는지는 _로 무시한다.
	fmt.Println(num)
}
```

위의 코드에서 보이듯이 `os.Open()`는 파일 **오브젝트**와 에러를 반환한다. 실제로 파일을 읽는 함수는 `fmt.Fscanf()`이다.

### 파일 쓰기

```go
f, err := os.Create("my_write.txt")
if err != nil {
	fmt.Println(err)
}
defer f.Close()
if _, err := fmt.Fprintf(f, "%d\n", 12345); err != nil {
	fmt.Println(err)
}
```

### 텍스트 리스트 읽고 쓰기

```go
func WriteTo(w io.Writer, lines []string) error {
	for _, line := range lines {
		if _, err := fmt.Fprintln(w, line); err != nil {
			return err
		}
	}
	return nil
}

func ReadFrom(r io.Reader, lines *[]string) error {
	scanner := bufio.NewScanner(r)
	for scanner.Scan() {
		*lines = append(*lines, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		return err
	}
	return nil
}


func ExampleWriteTo() {
	lines := []string{
		"bill@mail.com",
		"tom@mail.com",
		"jane@mail.com",
	}
	if err := io_part.WriteTo(os.Stdout, lines); err != nil {
		fmt.Println(err)
	}
	// Output:
	// bill@mail.com
	// tom@mail.com
	// jane@mail.com
}

func ExampleReadFrom() {
	r := strings.NewReader("bill\ntom\njane\n")
	var lines []string
	if err := io_part.ReadFrom(r, &lines); err != nil {
		fmt.Println(err)
	}
	fmt.Println(lines)
	// Output:
	// [bill tom jane]
}
```

### stdio로부터 한줄씩 읽기

[Go でファイルや標準入力からテキストを一行ずつ読む](http://www.yunabe.jp/tips/golang_readlines.html)

#### bufio.Scanner

`bufio.Scanner`를 사용하여 파일/표준입력으로 부터 텍스트를 한줄씩 읽을 수 있다. `s.Scan()`이 파일의 말미에 도착하면 false를 반환하므로, for루프를 돌린다. 행의 내용은 `Text()`로 string으로서 취득하고, 이때, 개행문자(`'\n'`)는 포함하지 않으므로, strings.Trim은 필요 없다. 만약, 제대로 파일의 말미까지 도달했는지 알고 싶으면, `s.Err()`를 확인해서 문제가 없다면 `nil`을 반환한다.

- 파일의 경우: `os.Open(path)`
- 표준 입출력의 경우: `os.Stdin`

```go
// file ver
func readLines(path string) {
    f, err := os.Open(path)
    if err != nil {
        log.Fatal(err)
        return
    }
    s := bufio.NewScanner(f)
    for s.Scan() {
        log.Print(strconv.Quote(s.Text()))
    }
    if s.Err() != nil {
        // non-EOF error.
        log.Fatal(s.Err())
    }
}

// stdio ver
func readLines(path string) {
    s := bufio.NewScanner(os.Stdin)
    for s.Scan() {
        log.Print(strconv.Quote(s.Text()))
    }
    if s.Err() != nil {
        // non-EOF error.
        log.Fatal(s.Err())
    }
}
```

#### bufio.Reader

`bufio.Scanner`뿐 아니라 `bufio.Reader`를 이용해서 한 행 씩 파일을 읽는 것도 가능하다. 대신에 `r.ReadString('\n')`을 써야하는것이 차이. 반환값으로 문말의 개행문자를 포함하므로 `strings.TrimLeft`등을 이용해 개행문자를 제거해야할 필요가 있다.

```go
func readLines(f *file.File) {
    r := bufio.NewReader(f)
    for {
        // line includes '\n'.
        line, err := r.ReadString('\n')
        if err == io.EOF {
            break
        } else if err != nil {
            log.Fatal(err)
        }
        log.Print(strconv.Quote(line))
    }
}
```

### fmt.Scanf()

어떠한 형식으로 입력될지 이미 알고 있다면 C언어에서처럼 Scanf()함수를 사용하는 것도 좋을것이다.

### stdio를 이용해서 출력하기

`fmt.Println`은 매우 편리하지만 성능상 `bufio.NewWriter(os.Stdou)`를 이용한 방법에 비하면 엄청나게 느리다. 20배 정도(?!) 차이난다(백준 온라인 저지에서 확인).

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var M, N int
	fmt.Scanf("%d %d", &M, &N)
	nums := make([]bool, N+1)
	out := bufio.NewWriter(os.Stdout)
	for i := 2; i < N+1; i++ {
		if nums[i] {
			continue
		}
		if i >= M {
			fmt.Fprintln(out, i)
		}
		for j := i * 2; j <= N; j += i {
			nums[j] = true
		}
	}
	out.Flush()
}
```
