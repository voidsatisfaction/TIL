# Tips for competitive programming using Golang

이제까지 많은 알고리즘 문제를 go를 사용해서 풀어오면서, go언어는 솔직히 그렇게까지 알고리즘 문제를 푸는데에 특화된 언어는 아니라는 생각이 들었다. go로 풀기보다는 다양한 라이브러리를 제공해주는 c++이 더 좋아보이고, 간단한문제들은 ruby나 python을 이용해서 푸는것이 더 수월하다고 개인적으로 생각한다.

그래도 go언어 자체의 성능도 괜찮을 뿐더러 go를 공부하는 입장에서 좀더 자유자재로 go를 다루고 싶다면, 알고리즘 문제를 go로 풀어보는 것도 **매우 좋다고 생각한다.**

하지만 막상 go언어로 알고리즘 문제를 풀어보면 분명 시간 복잡도는 만족했는데 시간초과가 나온다던지 하는 아리송한 경우가 있다. 이번 글에서 그와같은 부분에 대해서 어떻게 대처해야 하는지 집중 탐구하고자 한다.

## STDIN

기본적으로 세 가지의 방법을 사용한다.

1. `fmt.Scanf`
2. `bufio.NewScanner`
2. `bufio.NewReader`

각각의 방법은 각자의 장 단점이 있는데 알고리즘 문제를 푸는 관점에서 어떠할때 어떤 것을 사용해야하는지 알아보자.

### 1. fmt.Scanf: 빈도가 적은 값을 손쉽게 받을 때

```
10 5
```

예를들어 원소의 총 개수라던지, 쿼리의 수 와 같은 숫자는 보통 한 번만 나온다. 그러므로 간단히 값을 읽어들이기만 하면 되므로 `fmt.Scanf`를 사용해서 값을 읽어들인다.

### 2. bufio.NewScanner: 빈도가 어느정도 큰 값을 한 줄 씩 받을 때

```
1
2
3
4
5
6
...
100000
```

위와 같이 매우 많은 값들이 한 줄씩 있을경우에는 높은 확률로 `fmt.Scanf`를 사용하면 시간초과가 난다. 그러므로, 다음과 같은 코드를 사용해서 값을 받자.

```go
s := bufio.NewScanner(os.Stdin)
for i := 0; i < 100001; i++ {
  var num int
  s.Scan()
  fmt.Sscanf(s.Text(), "%d", &num) // 1 2 3 4 5 ... 100000
}
```

이렇게 값을 받아서 사용하는것이 `fmt.Scanf`보다 속도가 빠르다.

### 3. bufio.NewReader: 빈도가 매우매우 큰 값을 한줄에 받을 때

다음과 같은 입력을 생각하자.

```
1 2 3 4 5 6 ... 10000000
```

위의 입력은 `bufio.NewScanner`로 받으려 하면 에러가 난다. 왜냐하면, bufio의 Scanner는 다음과 같은 제약이 있기 때문이다.

```go
const (
    // Maximum size used to buffer a token. The actual maximum token size
    // may be smaller as the buffer may need to include, for instance, a newline.
    MaxScanTokenSize = 64 * 1024
)
```

그러므로 우리는 다른 방법인 `bufio.NewReader`를 사용해야한다.

```go
r := bufio.NewReader(os.Stdin)
input, _ := r.ReadString('\n')
strSlice := strings.Split(strings.TrimSpace(input), " ") // [1 2 3 4 ... 10000000]
```

위의 코드는 한 줄에 많은 숫자가 있는 경우에 그 숫자들을 slice에 넣어주는 방법이다.

## STDOUT

### 1. fmt.Printf: 간단한 출력

C언어와 동일하게 간단한 출력은 `fmt.Printf`를 이용하면 편리하다.

### 2. bufio.NewWriter: 많은 출력

성능상 더 빠른지는 확실하지 않으나, `bufio.NewWriter`를 이용해서 출력하는 경우가 있다. 필자도 실제로 이 방법을 많이 사용한다. 아무래도 한번에 터미널에 출력하므로 터미널과 프로그램 사이의 api를 훨씬 덜 사용하게 되어서 빠를 것 같다.

```go
p := bufio.NewWriter(os.Stdout)
fmt.Fprintf(p, "%d", n)
p.Flush() // 여기서 결과값이 한번에 출력
```

이렇게 STDIN과 STDOUT을 각각의 케이스에 맞게 알맞게 대처해주면 알 수 없는 시간초과, 런타임에러와 씨름할 필요도 없을 것이다. 
