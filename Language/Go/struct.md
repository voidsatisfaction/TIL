# Go언어의 struct기초

## 참조

- [DeepEqual - golang.org](https://golang.org/pkg/reflect/#DeepEqual)

## 두 struct가 같은지 아닌지 확인하는 방법

go언어로 작업을 하다 보니 같은 struct인지 아닌지에 따라서 작업을 달리하는 조건 분기를 사용하는 경우가 생겼다. 이와 같은 경우에는 어떻게 하면 좋을까?

```go
type Animal struct {
  name string
  age int
}

func main() {
  cat := &Animal{name: "meow", age: 1}

  fmt.Printf("%+v", *cat == Animal{name: "meow", age: 1}) // True
}
```

위와 같이 만일 Struct내부의 모든 값이 value라면 == 로 비교가 가능하다.

하지만 Animal struct에 string의 슬라이스가 포함되면 어떨까?

```go
type Animal struct {
  name string
  age int
  friends []string
}

func main() {
  cat := &Animal{name: "meow", age: 1}

  fmt.Printf("%+v", *cat == Animal{name: "meow", age: 1}) // invalid operation: *cat == Animal literal (struct containing []string cannot be compared)
}
```

위와 같이 단순히 == 로만 비교하면 `Animal`구조체 내부에 `friends`라는 문자열의 슬라이스가 존재하므로 비교할 수 없게 된다.

그러므로 `reflect`패키지의 `DeepEqual`이라는 함수를 이용하여 friends의 내부 값까지 비교하는 것이 바람직하다.

```go
type Animal struct {
  name string
  age int
  friends []string
}

func main() {
  cat := &Animal{name: "meow", age: 1}

  fmt.Printf("%+v", reflect.DeepEqual(*cat, Animal{name: "meow", age: 1})) // True
}
```

## reflect.DeepEqual을 좀더 자세히 알아보기.

(golang의 공식문서를 참조)

여기서 그렇다면 `reflect.DeepEqual`이란 어떠한 함수이며 값을 어떻게 비교하는 것일까?

DeepEqual은 numbers, bools, strings, and channels의 값의 경우에는 `==`연산자로 비교하고, 나머지 타입들을 비교할 때에는 각각 다른 방식으로 비교한다.

- Array: 두 배열의 대응하는 원소가 deeply equal인가?
- Struct: 두 구조체의 대응하는 field가 deeply equal인가? + exported / unexported의 성질은 같은가?
- Func: 둘다 nil인 경우
- Interface: 두 인터페이스가 deeply equal한 구체적인 값을 갖고 있는 경우
- Map: 둘다 nil이거나 둘다 nil이 아니거나. 둘다 nil이 아닌경우, 같은 길이를 가지며, 같은 map object이거나 대응하는 키들과 deeply equal한 value를 갖을 경우
- Pointer: 두 포인터가 deeply equal한 값들을 가질 경우에, `==`로 비교
- Slice: 둘다 nil이거나 둘다 nil이 아니거나. 둘다 nil이 아닌경우, 같은 길이를 가지며, 같은 entry(&x[0] == &y[0])를 갖거나 각각에 대응하는 요소들이 deeply equal하는 경우

deeply equal은 위에서 살펴본 봐와 같이, recursive한 구성을 갖고 있다. 여기서 조심해야 하는 경우는 func타입(일반적으로 비교 불가) NaN이나 floating-point와 같이 자기자신을 비교할 때 다르다고 나올 수 있다.

또한 deeply equal에서는 비교의 사이클이 존재할 수 있는데 한 번 비교한 내용은 두번 다시 반복되지 않도록 cache해둔다.
