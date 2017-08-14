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
