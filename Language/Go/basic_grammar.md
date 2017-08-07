# Basic Grammer of GO

## 출처

[Go Programming](https://www.youtube.com/watch?v=CF9S4QZuV30)
[Go Tour]

## 내용

### export

Go에서는 첫 문자가 대문자로 시작하면, 그패키지를 사용하는 곳에서 접근할 수 있는 exported name이 된다.

### Arrays

```go
var favNums2[5] float64

favNums2[0] = 163
...

favNums3 := [5]float64 {1, 2, 3, 4, 5}

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

### Map

루비의 해시와 같은 역할. 파이선의 dictionary.

```go
presAge := make(map[string]int)

presAge["TheodoreRoosevelt"] = 42

fmt.Println(len(presAge)) // 1

presAge["John F. Kennedy"] = 43

fmt.Println(len(presAge)) // 2

delete(presAge, "John F. Kennedy")

fmt.Println(presAge) // map[ThedoreRoosevelt]
```

### Functions

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

### Defer

자기자신을 감싸는 함수의 실행이 끝나고 나중에 실행된다.

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

recover의 이용

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

panic의 이용

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

### Interfaces

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

Go routines간의 데이터를 주고 받는다.

루틴간의 데이터 통로라고 생각하면 될 듯.

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
