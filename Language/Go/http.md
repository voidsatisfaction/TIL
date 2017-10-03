# HTTP모듈

## HTTP Get

### 1. 간단한 GET요청

```go
package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	res, err := http.Get("http://csharp.news")
	if err != nil {
		panic(err)
	}

	defer res.Body.Close()

	data, err := ioutil.ReadAll(res.Body)
	if err != nil {
		panic(err)
	}
	fmt.Printf("%s\n", string(data))
}

```

이는 쉽게 HTTP GET을 호출하는 장점이 있으나, Request시에 헤더를 추가한다거나 Request 스트림을 추가하는 것과 같은 세밀한 컨트롤을 할 수 없는 단점이 있다. 보다 많은 컨트롤이 필요하다면, Request객체를 직접 생성해서 `http.Client`객체를 통해 호출하면 된다.

### 2. 커스터마이징된 GET요청

```go
package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	// create request object
	req, err := http.NewRequest("GET", "https://ko.wikibooks.org/wiki/C_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D_%EC%9E%85%EB%AC%B8", nil)
	if err != nil {
		panic(err)
	}

	// add header
	req.Header.Add("User-Agent", "Crawler")

	// execute request by using client object
	client := &http.Client{}
	res, err := client.Do(req)
	if err != nil {
		panic(err)
	}
	defer res.Body.Close()

	// print result
	bytes, _ := ioutil.ReadAll(res.Body)
	str := string(bytes)
	fmt.Println(str)
}

```

## HTTP POST 호출

### 1. HTTP POST 호출

http패키지는 웹 관련 클라이언트 및 서버 기능을 제공한다. 그 중 `http.Post()`메서드는 웹 서버로 간단히 데이터를 POST 하는데 사용된다.

```go
package main

import (
	"bytes"
	"io/ioutil"
	"net/http"
)

func main() {
	reqBody := bytes.NewBufferString("Post plain text")
	res, err := http.Post("http://httpbin.org/post", "text/plain", reqBody) // URL MIME Reqbody
	if err != nil {
		panic(err)
	}
	defer res.Body.Close()

	resBody, err := ioutil.ReadAll(res.Body)
	if err != nil {
		return
	}
	str := string(resBody)
	println(str)
  println(string(reqBody))
}

```

### 2. HTTP PostForm 호출

`http.PostForm()`은 From데이터를 보내는데 유용한 메서드이다. 일반 웹페이지의 Submit버튼을 눌렀을때와 동일한 효과를 낸다.

```go
package main

import (
	"io/ioutil"
	"net/http"
	"net/url"
)

func main() {
	res, err := http.PostForm("http://httpbin.org/post", url.Values{"Name": {"Lee"}, "Age": {"10", "20"}})
	if err != nil {
		panic(err)
	}
	defer res.Body.Close()

	resBody, err := ioutil.ReadAll(res.Body)
	if err == nil {
		str := string(resBody)
		println(str)
	}
}

```

### 3. JSON 데이터 POST

JSON 데이터의 POST도 위의 Plain Text를 POST하는 것과 비슷하나, 다만 데이터가 JSON포맷 이므로, `http.Post()`의 두번째 파라미터에 `application/json`을 적고, 세번째 파라미터에 JSON으로 인코딩된 데이터를 전달하면 된다.

아래 예제에서는 `encoding/json`표준 패키지의 `Marshal()`함수를 써서 임의의 구조체 데이터를 JSON으로 변경하는 방법을 썼다.

```go
package main

import (
	"bytes"
	"encoding/json"
	"io/ioutil"
	"net/http"
)

type Person struct {
	Name string
	Age  int
}

func main() {
	person := Person{"Alex", 10}
	pbytes, _ := json.Marshal(person)
	buff := bytes.NewBuffer(pbytes)
	res, err := http.Post("http://httpbin.org/post", "application/json", buff)
	if err != nil {
		panic(err)
	}

	resBody, err := ioutil.ReadAll(res.Body)
	if err != nil {
		panic(err)
	}
	st := string(resBody)
	println(st)
}

```

### 4. XML 데이터 POST

JSON 데이터를 POST하는 것과 비슷하다. 다만, `encoding/xml`패키지를 사용하여 마샬링하고, MIME 타입을 `application/xml`으로 지정한다.

```go
package main

import (
	"bytes"
	"encoding/xml"
	"io/ioutil"
	"net/http"
)

type Person struct {
	Name string
	Age  int
}

func main() {
	person := Person{"Alex", 10}
	pbytes, _ := xml.Marshal(person)
	buff := bytes.NewBuffer(pbytes)
	res, err := http.Post("http://httpbin.org/post", "application/xml", buff)
	if err != nil {
		panic(err)
	}

	resBody, err := ioutil.ReadAll(res.Body)
	if err != nil {
		panic(err)
	}
	str := string(resBody)
	println(str)
}

```

보다 커스터마이징된 POST 요청을 보내기 위해서는 다음과 같이 request객체를 생성하고, client오브젝트를 통해서 서버에 request를 보낸다.

```go
package main

import (
    "bytes"
    "encoding/xml"
    "io/ioutil"
    "net/http"
)

//Person -
type Person struct {
    Name string
    Age  int
}

func main() {
    person := Person{"Alex", 10}
    pbytes, _ := xml.Marshal(person)
    buff := bytes.NewBuffer(pbytes)

    // Request 객체 생성
    req, err := http.NewRequest("POST", "http://httpbin.org/post", buff)
    if err != nil {
        panic(err)
    }

    //Content-Type 헤더 추가
    req.Header.Add("Content-Type", "application/xml")

    // Client객체에서 Request 실행
    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    // Response 체크.
    respBody, err := ioutil.ReadAll(resp.Body)
    if err == nil {
        str := string(respBody)
        println(str)
    }
}
```
