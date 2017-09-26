# Basic Grammer of GO

## 출처

- [Go Programming](https://www.youtube.com/watch?v=CF9S4QZuV30)
[Go Tour]
- [예제로 배우는 GO 프로그래밍](http://golang.site/)

## 내용

### variable, constant

#### 변수

사용되지 않는 변수는 에러를 발생시킨다.

변수를 선언하면서 초기값을 지정하지 않으면, Go는 Zero Value를 기본적으로 할당한다. e.g: 숫자형 0, bool타입 false, string ""

`:=`(Short Assignment Statement)도 사용가능(타입 추론)

```go
var f float32 = 11
var i, j, k int // 0 0 0
var i, j, k int = 1, 2, 3 // 1 2 3
num := 4
```

#### 상수

```go
const c int = 10
const c = 10 // 타입추론
const (
  Visa = "Visa"
  Master = "MasterCard"
  Amex = "American Express"
)
const (
  Apple = iota //0
  Grape // 1
  Orange // 2
)
```

### Data type

#### GO데이터 타입

- 부울린
  - bool
- 문자열
  - string: immutable type
- 정수형
  - int int8 int16 int32 int64
  - uint uint8 uint16 uint32 uint64 uintptr
- Float & 복소수
  - float32 float64 complex64 complex128
- etc(byte, rune)
  - byte: uint8과 동일하며 바이트 코드에 사용
  - rune: int32와 동일하며 유니코드 코드 포인트에 사용

#### 문자열

- \`\`: Raw String Literal 문자열이 별도로 해석되지 않고 있는 그대로의 값을 갖음. 복수 라인의 문자열 표현할때 자주 사용.
- "": Interpreted String Literal 인용부호안의 Escape 문자열은 특별한 의미로 해석. +로 문자열을 여러 라인에 결합하여 사용. 복수 라인에 걸쳐 쓸 수 없음.

```go
package main

import "fmt"

func main() {
  rawLiteral := `아리랑\n
  아리랑\n
  아라리요`

  interLiteral := "아리랑알랑\n아라리요"
}
```

#### 데이터 타입 변환

```go
package main

func main() {
	var i = 100
	var u = uint(i) // 100
	var f = float32(i) // +1.000000e+002
	println(f, u)

	str := "ABC"
	bytes := []byte(str) // [3/32]0xc42003df48
	str2 := string(bytes) // ABC
	println(bytes, str2)
}

```

### 연산자

산술연산자(+ - * / % ++ --)

관계연산자(== != >=)

논리연산자(&& || NOT)

Bitwise연산자(& << |): XOR AND OR

할당연산자(= += &= <<=)

포인터연산자(*, &): 산술포인터는 제공하지 않는다.

### 조건문

#### if문

조건문 사용하기 이전에 간단한 문장을 함께 실행할 수 있다. 대신 이때 정의된 변수 val은 if문 블럭 안에서만 사용가능하다.

```go
if k == 1 { // {가 반드시 if와 같은 라인에 있어야 한다.
  println("One")
}

if val := i * 2; val < max {
  println(val)
}
val ++ // 이는 에러
```

#### switch문

```go
var name string
var category = 1

switch category {
case 1:
  name = "paper book"
case 2:
  name = "ebook"
case 3:
  name = "blog"
default:
  name = "other"
}
println(name)

// Expression을 사용한 경우
switch x := category << 2; x - 1 {
  // ...
}
```

Go만의 특성

1. **switch뒤에 expression이 없을 수 있음**: 이 경우 switch expression을 true로 생각하고 첫번째 case문으로 이동
2. **case문에 expression을 쓸 수 있음**: case문에 복잡한 expression을 쓸 수 있음
3. **No default fall through**: 다음 case로 자동으로 가지 않는다.
4. **type switch**: 변수의 type에 따라서 case분기도 가능하다.

```go
func grade(score int) {
    switch {
    case score >= 90:
        println("A")
    case score >= 80:
        println("B")
    case score >= 70:
        println("C")
        fallthrough
    case score >= 60:
        println("D")
    default:
        println("No Hope")
    }
}
grade(75) // C D
```

### 반복문

1. for문
2. for문 - 조건식만 쓰는 for루프
3. for문 - 무한루프
4. for range 문
5. break, continue, goto문

#### 1. for문

```go
sum := 0
for i := 1; i <= 100; i++ {
    sum += i
}
println(sum) // 5050
```

#### 2. for문 - 조건식만 쓰는 for루프

```go
n := 1
for n < 100 {
  n *= 2
}
println(n) // 128
```

#### 3. for문 - 무한루프

```go
for {
  println("Infinite loop")
}
```

#### 4. for range문

```go
names := []string{"a", "b", "c"}

for i, name := range names {
  println(i, name)
}
```

#### 5. break, continue, goto문

```go
var a = 1
for a < 15 {
  if a == 5 {
    a += a
    continue
  }
  a++
  if a > 10 {
    break
  }
}
if a == 11 {
  goto END
}
println(a)

END:
  println("END") // END
```

### export

Go에서는 첫 문자가 대문자로 시작하면, 그패키지를 사용하는 곳에서 접근할 수 있는 exported name이 된다.

### Arrays

배열과 슬라이스 모두 연속된 메모리 공간을 순차적으로 이용하는 자료구조. 주로 슬라이스를 이용하여 간접적으로 배열을 이용하는 경우가 많다.

```go
var favNums2[5] float64

favNums2[0] = 163
...

favNums3 := [5]float64 {1, 2, 3, 4, 5}
// favNums3 := [...]float64 {1, 2, 3, 4, 5} // 위와 같음 자동으로 길이 정해줌

for i, value := range favNums3 {
  fmt.Println(value, i)
}

for _, value := range favNums3 {
  fmt.Println(value)
}
```

### Slice

array를 from to로 나누어서 자를 수 있게 한다.

루비의 `a[1..2]`와 같다.

```go
var a []int
a = []int{1, 2, 3}

numSlice := []int {5, 4, 3, 2, 1}

numSlice2 := numSlice[3:5]

fmt.Println(numSlice2) // [2 1]

fmt.Println(numSlice[:2]) // [5 4]

fmt.Println(numSlice[2:]) // [3 2 1]

numSlice3 := make([]int, 5, 10) // int array안에 5개의 초기 value(0)을 넣고 array의 최대길이는 10이다.

copy(numSlice3, numSlice) // numSlice의 배열의 요소를 numSlice3에 deep copy한다.

fmt.Println(numSlice3[0])

numSlice3 = append(sumSlice3, 0, -1)

fmt.Println(numSlice3)
```

슬라이스 병합

```go
func main() {
  sliceA := []int{1, 2, 3}
  sliceB := []int{4, 5, 6}

  sliceA = append(sliceA, sliceB...)

  fmt.Println(sliceA) // [1 2 3 4 5 6]
}
```

### Map

루비의 해시와 같은 역할. 파이선의 dictionary.

key에 대응하는 값(value)을 신속히 찾는 해시테이블을 구현한 자료구조이다.

```go
var idMap map[int]string // nil Map이므로 데이터를 쓸 수 없다.
idMap = make(map[int]string) // make함수로 초기화 가능(데이터 쓸 수 있다)
tickers := map[string]string{ // Literal로 초기화
  "GOOG": "Google Inc",
  "MSFT": "Microsoft",
  "FB": "FaceBook",
}

println(tickers["GOOG"]) // Google Inc
```

```go
presAge := make(map[string]int)

presAge["TheodoreRoosevelt"] = 42

fmt.Println(len(presAge)) // 1

presAge["John F. Kennedy"] = 43

fmt.Println(len(presAge)) // 2

delete(presAge, "John F. Kennedy")

fmt.Println(presAge) // map[ThedoreRoosevelt]
```

**Map Key check**

map을 사용하는 경우 종종 map안에 특정 키가 존재하는지를 체크할 필요가 있다. 이를 위해 Go에서는 map변수[키] 읽기를 수행할 때 2개의 리턴값을 리턴한다. 첫번째는 키에 상응하는 값이고, 두번째는 키가 존재하는지 아닌지를 나타내는 bool값이다.

```go
func main() {
  tickers := map[string]string {
    "GOOG": "Google Inc",
    "MSFT": "Microsoft",
    "FB": "FaceBook",
    "AMZN": "Amazon",
  }

  val, exists := tickers["MSFT"]
  if !exists {
    println("No MSFT ticker")
  }
}
```

**for loop를 사용한 map열거**

```go
func main() {
  myMap := map[string]string {
    "A": "Apple",
    "B": "Banana",
    "C": "Charlie",
  }

  for key, val := range myMap {
    fmt.Println(key, val)
  }
}
```

### Functions

파라미터 전달 방식은 `Pass By Value`와 `Pass By Reference`가 있다.

#### 1. Pass By value

msg의 값 "Hello"문자열이 복사되어서 함수 say()에 전달된다.

```go
package main
func main() {
  msg := "Hello"
  say(msg)
}

func say(msg string) { // Pass By Value
  println(msg)
}
```

#### 2. Pass By Reference

```go
package main
func main() {
  msg := "Hello"
  say(&msg)
  println(msg)
}

func say(msg *string) {
  println(*msg)
  *msg = "Changed"
}
```

#### 3. Variadic Function(가변인자함수)

```go
package main
func main() {
  say("This", "is", "a", "book")
  say("Hi")
}

func say(msg ...string) {
  for _, s := range msg {
    println(s)
  }
}
```

#### 4. 함수 리턴값

Named Return Prameter들에 리턴값들을 할당하여 리턴할 수 있음.

```go
func main() {
  count, total := sum(1, 7, 3, 5, 9)
  println(count, total)
}

func sum(nums ...int) (count int, total int) {
  for _, n := range nums {
    total += n
  }
  count = len(nums)
  return // 반드시 return을 붙여줘야함.
}
```

Just one value returns

```go
func main() {
	listNums := []float64{1, 2, 3, 4, 5}

	fmt.Println("Sum :", addThemUp(listNums)) // 15
}

func addThemUp(numbers []float64) float64 {
	sum := 0.0

	for _, val := range numbers {
		sum += val
	}

	return sum
}
```

Multiple value returns

```go
func main() {
	num1, num2, num3 := next2Values(5)
	fmt.Println(num1, num2, num3)
}

func next2Values(number int) (int, int, int) {
	return number + 1, number + 2, number + 3
}
```

임의의 길이의 인자를 받기(js의 args랑 비슷함, go에서도 args는 배열이 아니라 배열같은 무엇인가)

```go
func main() {
	fmt.Println(subtractThem(1, 2, 3, 4, 5)) // -15
}

func subtractThem(args ...int) int {
	finalValue := 0

	for _, value := range args {
		finalValue -= value
	}

	return finalValue
}
```

### Lambda(Anonymous Function)

함수명을 갖지 않는 함수를 익명함수라고 한다.

Go에서는 함수가 first class citizen이므로, 기본 타입과 동일하게 취급되며, 다른 함수의 파라미터로 전달하거나 다른 함수의 리턴값으로도 사용될 수 있다.

```go
package main

type calculator func(int, int) int

func main() {
  add := func(i int, j int) int {
    return i + j
  }

  r1 := calc(add, 10, 20)
  println(r1) // 30

  r2 := calc(func(x int, y int) int { return x - y }, 10, 20)
  println(r2) // -10
}

func calc(f calculator, a int, b int) int {
  result := f(a, b)
  return result
}
```

또한, `type`문을 사용해서 함수의 원형을 정의할 수 있다. 보통 `type`문은 구조체, 인터페이스 등 custom type을 정의하기 위해 사용된다. 또, 함수의 원형을 정의하는데에 사용될 수 있다.

이렇게 함수의 원형을 정의하고 함수를 타 메서드에 전달하고 리턴받는 기능을, Delegate라 부른다.

### Closures

Go언어에서 함수는 First Class Citizen이다.

```go
func main() {
	num3 := 3

	doubleNum := func() int {
		num3 *= 2

		return num3
	}

	doubleNum()

	fmt.Println(num3) // 6
}

```

### Recursion

```go
func main() {
	fmt.Println(factorial(5)) // 120
}

func factorial(num int) int {
	if num == 0 {
		return 1
	}

	return num * factorial(num-1)
}
```

### 지연실행 defer

자기자신을 감싸는 함수가 리턴하기 직전에 실행된다. 마지막에 Clean-up작업을 위해 사용된다.

```go
func main() {
	defer printTwo()
	printOne()
}

func printOne() { fmt.Println(1) }
func printTwo() { fmt.Println(2) }

/*
결과
1
2
*/
```

### panic 함수

panic은 go언어의 runtime error를 일으킨다.
defer속의 lambda 함수가 error message를 넘겨받고 출력해준다.

```go
func main() {
	demPanic()
}

func demPanic() {
	defer func() {
		fmt.Println(recover())
	}()

	panic("PANIC")
}
/*
결과
PANIC
*/
```

### recover 함수

panic 함수에 의한 패닉상태를 다시 정상상태로 되돌리는 함수이다.

recover함수는, 에러가 나도 exit하지 않고 그냥 계속 실행하게 만든다.

defer로 지정하므로써 에러가 나도 계속 진행하게 만듬.

```go

func main() {
	fmt.Println(safeDiv(3, 0))
	fmt.Println(safeDiv(3, 2))
}

func safeDiv(num1, num2 int) int {
	defer func() {
		recover()
	}()

	solution := num1 / num2

	return solution
}

/*
결과
0
1
*/
```

### Pointers

```go
func main() {
	x := 0

	changeXValNow(&x)

	fmt.Println("x =", x) // 2

  fmt.Println(&x) // Memory address hexadecimal
}

func changeXValNow(x *int) {
	*x = 2
}
```

```go
func main() {
	yPtr := new(int) // generate yPtr(pointer) with new function

	changeXValNow(yPtr)

	fmt.Println(*yPtr) // 100
}

func changeXValNow(yPtr *int) {
	*yPtr = 100
}
```

### Structs

Custom Data Type를 표현하는데 사용. Go의 struct는 필드들의 집합체이며 필드들의 컨테이너이다. Go에서 struct는 필드 데이터만을 가지며, 메서드를 갖지 않는다.

메서드는 별도로 분리하여 정의한다.

패키지 외부에서 사용할 수 있게 하려면 struct명의 가장 앞 글자를 대문자로 변경하면 된다.

```go
type Person struct {
  name string
  age int
}

func main() {
  p := person{}

  p.name = "Lee"
  p.age = 10

  fmt.Println(p)
}
```

Struct객체 생성

```go
var p1 Person
p1 = Person{"Bob", 20}
p2 := Person{name: "Bob", age: 50} // 일부 필드가 생략될 경우, Zero value가 된다.
p := new(Person)
p.name = "Lee" // p가 포인터라도 .을 사용한다. 포인터는 자동으로 dereference된다.
```

Go에서 struct는 기본적으로 mutable 개체로서 필드값이 변화할 경우, 해당 개체 메모리에서 직접 변경된다. 하지만, struct 개체를 다른 함수의 파라미터로 넘긴다면, Pass by Value에 따라 객체를 복사해서 전달하게 된다. **그래서 만약 Pass by Reference로 struct를 전달하고자 한다면, struct의 포인터를 전달해야 한다.**

**생성자(constructor) 함수**

때로 구조체의 필드가 사용 전에 초기화 되어야 하는 경우가 있다.

e.g. struct의 필드가 map타입인 경우 map을 사전에 초기화해 놓으면, 외부 struct사용자가 매번 map을 초기화 해야한다는 것을 기억할 필요가 없음.

```go
package main

type dict struct {
  data map[int]string
}

func newDict() *dict {
  d := dict{}
  d.data = map[int]string{}
  return &d
}

func main() {
  dic := newDict()
  dic.data[1] = "A"
}
```

```go
func main() {
	// rect1 := Rectangle{leftX: 0, topY: 50, height: 10, width: 10}
	rect1 := Rectangle{0, 50, 10, 10}

	fmt.Println(rect1.area()) // 100
}

type Rectangle struct {
	leftX  float64
	topY   float64
	height float64
	width  float64
}

func (rect *Rectangle) area() float64 {
	return rect.width * rect.height
}
```

### Go 메서드(Method)

Go에서의 객체지향 프로그래밍의 지원방식. struct가 필드만을 가지며, 메서드는 별도로 분리되어 정의된다.

Go메서드는 함수 정의에서 func 키워드와 함수명 사이에 "그 함수가 어떤 struct를 위한 메서드인지"를 표시하게 한다. 흔히 receiver로 불리우는 이 부분은 메서드가 속한 struct 타입과 struct변수명을 지정하는데, struct변수명은 함수 내에서 마치 입력 파라미터 처럼 사용된다.

```go
package main

type Rect struct {
  width, height int
}

func (r Rect) area() int {
  return r.width * r.height
}

func main() {
  rect := Rect{10, 20}
  area := rect.area() // 메서드 호출
  println(area)
}
```

**Value vs 포인터 receiver**

- Value receiver는 struct의 데이터를 복사 하여 전달
- 포인터 receiver는 struct의 포인터만을 전달한다.
  - 메서드 내의 필드값 변경이 그대로 호출자에서 반영된다.

```go
package main

type Rect struct {
  width, height int
}

func (r *Rect) area2() int {
  r.width++ // 포인터도 그냥 .width로 참조 가능 자동 변환
  return r.width * r.height
}

func main() {
  rect := Rect{10, 20}
  area := rect.area2()
  println(rect.width, area) // 11 220
}
```

### Interfaces

구조체: 필드들의 집합체

interface: 메서드들의 집합체, 사용자 정의 type(struct)이 구연해야 하는 메서드의 prototype들을 정의한다. 인터페이스는 struct와 마찬가지로 type문을 사용하여 정의한다.

```go
type Shape interface {
  area() float64
  perimeter() float64
}
```

**인터페이스 구현**

인터페이스를 구현하기 위해서는 해당 타입이 그 인터페이스의 메서드들을 모두 구현하면 된다. 위의 Shape 인터페이스를 구현하기 위해서는 아래와 같이 각 타입별로 두개의 메서드를 구현해 주면 된다.

```go
type Rect struct {
  width, height float64
}

type Circle struct {
  radius float64
}

func (r Rect) area() float64 { return r.width * r.height }
func (r Rect) perimeter() float64 { return 2 * (r.width + r.height) }

func (c Circle) area() float64 {
  return math.Pi * c.radius * c.radius
}
func (c Circle) perimeter() float64 {
  return 2 * math.Pi * c.radius
}
```

**인터페이스 사용**

인터페이스를 사용하는 일반적인 예로 함수가 파라미터로 인터페이스를 받아들이는 경우를 들 수 있다. 함수 파라미터가 interface인 경우, 이는 어떤 타입이든 해당 인터페이스를 구현하기만 하면 모두 입력 파라미터로 사용될 수 있다는 것을 의미한다.

```go
func main() {
  r := Rect{10., 20.}
  c := Circle{10}

  showArea(r, c)
}

func showArea(shapes ...Shape) {
  for _, s := range shapes {
    a := s.area()
    println(a)
  }
}
```

**인터페이스 타입**

빈 인터페이스는 흔히 인터페이스 타입으로도 불리운다. Go의 모든 타입을 나타내기 위한 인터페이스다. 빈 인터페이스는 어떠한 타입도 담을 수 있는 컨테이너 이다(Dynamic Type)

```go
// func Println(a ...interface{}) (n int, err error);

package main

import "fmt"

func main() {
  var x interface{}
  x = 1
  x = "Tom"

  printIt(x) // Tom
}

func printIt(v interface{}) {
  fmt.Println(v)
}
```

**Type Assertion**

Interface type의 x와 타입 T에 대하여 `x.(T)`로 표현했을 때, 이는 x가 nil이 아니며, x는 T타입에 속한다는 점을 확인(assert)하는 것으로 이러한 표현을 "Type Assertion"이라 부른다.

만약 x가 nil이거나 x의 타입이 T가 아니라면, 런타임 에러가 발생할 것이고, x가 T타입인 경우는 T타입의 x를 리턴한다.

```go
func main() {
  var a interface{} = 1

  i := a // a와 i는 dynamic type 값은1
  j := a.(int) // j는 int 타입, 값은 1

  println(i) // 포인터 주소 출력
  println(j) // 1 출력
}
```

polymorphism

아래의 코드는 Shape라는 interface를 갖고 있기 때문에 작동 가능하다.

동적 속박을 가능하게 해줌.

```go
func main() {
	rect := Rectangle{20, 50}
	circ := Circle{4}

	fmt.Println(getArea(rect)) // 1000
	fmt.Println(getArea(circ)) // 50.26 ...
}

type Shape interface {
	area() float64
}

type Rectangle struct {
	height float64
	width  float64
}

type Circle struct {
	radius float64
}

func (r Rectangle) area() float64 {
	return r.height * r.width
}

func (c Circle) area() float64 {
	return math.Pi * math.Pow(c.radius, 2)
}

func getArea(shape Shape) float64 {
	return shape.area()
}
```

### 에러처리

#### 1. Go 에러

Go는 내장 타입으로 `error`라는 interface 타입을 갖는다. Go 에러는 이 error 인터페이스를 통해서 주고 받게 되는데, 이 interface는 다음과 같은 하나의 메서드를 갖는다. 개발자는 이 인터페이스를 구현하는 커스텀 에러 타입을 만들 수 있다.

```go
type error interface {
  Error() string
}
```

#### 2. Go 에러처리

Go함수가 결과와 에러를 함께 리턴한다면, 이 에러가 nil인지를 체크해서 에러가 없는지를 체크할 수 있다.

`log.Fatal()`은 메시지를 출력하고 `os.Exit(1)`을 호출하여 프로그램을 종료한다.

```go
package main

import (
  "log"
  "os"
)

func main() {
  f, err := os.Open("C:\\temp\\1.txt")
  if err != nil {
    log.Fatal(err.Error())
  }
  println(f.Name())
}
```

또 다른 에러처리로서 error의 Type을 체크해서 여러 타입별로 별도의 에러 처리를 하는 방식이 있다. 아래 예제에서 `otherFunc()`를 호출한 후 error가 `err`로 리턴되었을 때, 이 err의 타입별로 다른 처리를 하는 것을 볼 수 있다.(switch문에서 `변수명.(type)`의 방식으로 타입 체크를 한다) 디폴트는 에러타입이 없는 경우이고, 에러가 있으면 다음 case문에서 그 에러타입이 MyError인지를 체크하고, 아니면 다음 case에서 일반 에러 케이스를 처리한다. 모든 에러는 `error`인터페이스를 구현하므로 마지막 case문은 모든 에러에 적용된다.

```go
_, err := otherFunc()
switch err.(type) {
default:
  println("ok")
case MyError:
  log.Print("Log my error")
case error:
  log.Fatal(err.Error())
}
```

### String manipulation

```go
func main() {
	sampleString := "Hello World"

	fmt.Println(strings.Contains(sampleString, "lo"))       // true
	fmt.Println(strings.Index(sampleString, "lo"))          // 3
	fmt.Println(strings.Count(sampleString, "l"))           // 3
	fmt.Println(strings.Replace(sampleString, "l", "x", 2)) // Hexxo World

	csvString := "1,2,3,4,5,6"

	fmt.Println(strings.Split(csvString, ",")) // [1 2 3 4 5 6]

	listOfLetters := []string{"c", "a", "b"}

	sort.Strings(listOfLetters)

	fmt.Println(listOfLetters) // [a b c]

	listOfNums := strings.Join([]string{"3", "2", "1"}, ", ")

	fmt.Println(listOfNums) // 3, 2, 1
}
```

### File I/O

```go
func main() {
	file, err := os.Create("samp.txt")

	if err != nil {
		log.Fatal(err)
	}

	file.WriteString("This is some random text")

	file.Close()

	stream, err := ioutil.ReadFile("samp.txt")

	if err != nil {
		log.Fatal(err)
	}

	readString := string(stream)

	fmt.Println(readString)
}

```

### Casting

형변환이 참 간단하다.

```go
func main() {
	randInt := 5
	randFloat := 10.5
	randString := "100"
	randString2 := "250.5"

	fmt.Println(float64(randInt)) // 5
	fmt.Println(int(randFloat)) // 10.5

	newInt, _ := strconv.ParseInt(randString, 0, 64) // 100
	fmt.Println(newInt)

	newFloat, _ := strconv.ParseFloat(randString2, 64) // 250.5
	fmt.Println(newFloat)
}
```

### Create Web Server

```go
func main() {
	http.HandleFunc("/", handler)

	http.HandleFunc("/earth", handler2)

	http.ListenAndServe(":8080", nil)
}

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello\n")
}

func handler2(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello earthman\n")
}
```

### Go Routines

Go루틴은 Go 런타임이 관리하는 Lightweight 논리적(가상적) 쓰레드이다.

Go에서 `go`키워드를 사용하여 함수를 호출하면, 런타임시 새로운 goroutine을 실행한다. goroutine은 비동기적으로(asynchronously) 함수루틴을 실행하므로, 여러 코드를 동시에(Concurrently) 실행하는데 사용된다.

- gorountine은 OS쓰레드보다 훨씬 가볍게 비동기(Concurrent) 처리를 구현하기 위해서 만든 것.
- go runtime이 자체관리.
- 여러 go routine들이 하나의 OS쓰레드로 실행되곤 함(OS 쓰레드와 1:1대응 아님)
- OS 쓰레드가 1메가바이트 스택 / Go루틴은 몇 킬로바이트 스택(동적 증가)
- Go runtime은 Go 채널을 통한 Go루틴 간의 통신관리

```go
package main

import (
	"fmt"
	"time"
)

func say(s string) {
	for i := 0; i < 10; i++ {
		fmt.Println(s, "***", i)
	}
}

func main() {
	// 함수를 동기적으로 실행
	say("Sync")

	// 함수를 비동기적으로 실행
	go say("Async1")
	go say("Async2")
	go say("Async3")

	time.Sleep(time.Second * 3) // 이것이 없으면 Sync만 출력하고 바로 끝남.
}
```

#### c.f Concurrency와 Prallelism의 차이

- Concurrency: composition of independently executin processes
  - Dealing with lots of things at once
- Prallelism: simultaneous execution of computations
  - Doing lots of things at once

**익명함수 Go루틴**

```go
package main

import (
  "fmt"
  "sync"
)

func main() {
  // WaitGroup 생성. 2개의 Go루틴을 기다림.
  var wait sync.WaitGroup
  wait.Add(2)

  go func() {
    defer wait.Done() // 끝나면 .Done() 호출
    fmt.Println("Hello")
  }()

  go func(msg string) {
    defer wait.Done()
    fmt.Println(msg) // 끝나면 .Done() 호출
  }("Hi")

  wait.Wait() // Go루틴 모두 끝날 때까지 대기
}
```

`sync.WaitGroup`은 여러 Go루틴들이 끝날 때까지 기다리는 역할을 한다. `WaitGroup`을 사용하기 위해서는 먼저 `Add()` 메소드에 몇 개의 Go루틴을 기다릴 것 인지 지정하고, 각 Go루틴에서 `Done()`메서드를 호출한다(여기서는 `defer`를 사용) 그리고 메인루틴에서는 `Wait()` 메서드를 호출하여, Go루틴들이 모두 끝나기를 기다린다.

**다중 CPU처리**

Go는 디폴트로 1개의 CPU를 사용한다. 여러개의 Go루틴을 만들더라도 1개의 CPU에서 작업을 시분할하여 처리한다(Concurrent).

머신이 복수개의 CPU를 가진 경우, Go 프로그램을 다중 CPU에서 병렬처리(Parallel처리) 하게 할 수 있는데, 이는 `runtime.GOMAXPROCS(CPU수)` 함수를 호출하여야 한다. (여기서 CPU 수는 Logical CPU 수를 가리킨다)

```go
package main

import (
  "runtime"
)

func main() {
  // 4개의 CPU사용
  runtime.GOMAXPROCS(4)

  // ...
}
```

---

`go count(i)`하면 루틴을 하나 새로 만든다.

그러니까, 처음에는

`go count(i)`에서 루틴을 먼저 만들고 그다음에 실행한다.

```go
func count(id int) {
	for i := 0; i < 10; i++ {
		fmt.Println(id, ":", i)

		time.Sleep(time.Millisecond * 1000)
	}
}

func main() {
	for i := 0; i < 10; i++ {
		go count(i)
	}

	time.Sleep(time.Millisecond * 11000)
}

```

**여기서 주의해야 하는데, 꼭 순차적으로 i가 적용되지 않는다는거다.**

실제로 결과값은 다음과 같았다.

```
1 : 0
0 : 0
6 : 0
3 : 0
2 : 0
7 : 0
8 : 0
4 : 0
5 : 0
9 : 0
2 : 1
0 : 1
8 : 1
9 : 1
3 : 1
7 : 1
1 : 1
6 : 1
4 : 1
5 : 1
0 : 2
2 : 2
7 : 2
5 : 2
8 : 2
1 : 2
4 : 2
9 : 2
6 : 2
3 : 2
3 : 3
4 : 3
9 : 3
6 : 3
1 : 3
7 : 3
0 : 3
2 : 3
5 : 3
8 : 3
1 : 4
9 : 4
0 : 4
6 : 4
8 : 4
2 : 4
5 : 4
7 : 4
3 : 4
4 : 4
8 : 5
1 : 5
9 : 5
6 : 5
2 : 5
7 : 5
5 : 5
3 : 5
0 : 5
4 : 5
2 : 6
8 : 6
1 : 6
9 : 6
6 : 6
5 : 6
7 : 6
3 : 6
0 : 6
4 : 6
6 : 7
4 : 7
2 : 7
5 : 7
8 : 7
7 : 7
9 : 7
3 : 7
0 : 7
1 : 7
1 : 8
8 : 8
9 : 8
3 : 8
6 : 8
0 : 8
7 : 8
4 : 8
2 : 8
5 : 8
5 : 9
7 : 9
4 : 9
0 : 9
6 : 9
2 : 9
9 : 9
8 : 9
1 : 9
3 : 9

```

반드시 동기라고 생각할 수는 없다.

### Channels

Go routines간의 데이터를 주고 받기 위한 통로이다.

`make()`함수를 통해 미리 생성되어야 하며, 채널 연산자 `<-`를 통해 데이터를 주고 받는다. 채널은 흔히 goroutine들 사이 데이터를 주고 받는데 사용되는데, 상대편이 준비될 때까지 채널에서 대기함으로써 별도의 lock을 걸지 않고 데이터를 동기화 하는데 사용된다.

```go

var pizzaNum = 0
var pizzaName = ""

func makeDough(stringChan1 chan string) {
	pizzaNum++

	pizzaName = "Pizza #" + strconv.Itoa(pizzaNum)

	fmt.Println("Make Dough and Send for Sauce")

	stringChan1 <- pizzaName

	time.Sleep(time.Millisecond * 10)
}

func addSauce(stringChan1, stringChan2 chan string) {
	pizza := <-stringChan1

	fmt.Println("Add Sauce and Send", pizza, "for toppings")

	stringChan2 <- pizzaName

	time.Sleep(time.Millisecond * 10)
}

func addToppings(stringChan2 chan string) {
	pizza := <-stringChan2

	fmt.Println("Add Toppings to", pizza, "and ship")

	time.Sleep(time.Millisecond * 10)
}

func main() {
	stringChan1 := make(chan string)
	stringChan2 := make(chan string)

	for i := 0; i < 3; i++ {
		go makeDough(stringChan1)
		go addSauce(stringChan1, stringChan2)
		go addToppings(stringChan2)

		time.Sleep(time.Millisecond * 5000)
	}
}

/*

Make Dough and Send for Sauce
Add Sauce and Send Pizza #1 for toppings
Add Toppings to Pizza #1 for ship

....

*/

```
