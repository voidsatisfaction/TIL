# Basic usage of GO

## Package and Library

go tool을 이용할 경우에는 directory하나가 한 패키지가 된다. 한 패키지는 메인 패키지 혹은 라이브러리 패키지가 될 수 있다.

- 메인 패키지로 설치: 실행파일이 bin 아래에 생성
- 라이브러리 패키지로 작성: hanoi package가 됨(hanoi 디렉토리인 경우)
  - 패키지 안에 대문자로 시작하는 함수들: `hanoi.Move`와 같이 접근 가능
  - 소문자로 시작하는 함수들은 패키지의 라이브러리로 접근 불가능
  - 패키지 이름은 간결하게. 패키지 내부의 함수 이름도 간결하게.

package의 예
```go
// src/github.com/voidsatisfaction/gogo/seq
package seq

func Fib(n int) int {
	p, q := 0, 1
	for i := 0; i < n; i++ {
		p, q = q, p+q
	}
	return p
}

```

seq를 부르는 경우
```go
// src/github.com/voidsatisfaction/gogo/seq_call
package main

import (
  "fmt"
  "github.com/voidsatisfaction/gogo/seq"
)

func main() {
  fmt.Println(seq.Fib(6))
}
```

## 도구 사용하기

### 1. Godoc

godoc은 Go프로그램의 문서를 볼 수 있는 도구이다.

**커맨드라인에서 보기**

`godoc fmt`

`godoc -src fmt Printf`

**로컬 웹 서버에서 보기**

`godoc -http=:6060`

그 뒤에 웹 브라우저에

`http://localhost:6060/pkg/github.com/`

를 입력하면 자신이 입력한 라이브러리도 볼 수 있다.

주석을 입력하면 매우 fancy하게 볼 수 있다.

![go doc](./assets/fancy_godoc.png)

### 2. Oracle

소스 코드에 대해서 여러 가지를 물어볼 수 있는 매우 강력한 도구.

편집기와 연동해서 사용하는 것을 추천

`oracle -pos=src/github.com/username/gogo/seq/seq.go:#134 callers`

### 3. Vet

소스 코드를 검사하기 위한 도구.

`go tool vet github.com/myusername/gogo/seq`

`go tool vet *.go`

### 4. Fix

이미 변경된 옛 API호출 등을 자동으로 고쳐주는 도구.

Go버전이 업그레이드 되면 한 번 실행하여 변경된 점을 확인하면 도움이 된다.

`go tool fix github.com/myusername/gogo/seq`

### 5. Test

테스트를 수행하는 도구.

`go test github.com/myusername/gogo/seq`
