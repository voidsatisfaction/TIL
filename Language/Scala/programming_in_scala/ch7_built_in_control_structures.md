# Built-in Control Structures

- 종류
  - if
  - while
  - for
  - try
  - match
  - 함수 호출
- **컨트롤 구조는 반환값이 존재**
  - 함수평 프로그래밍적 생각
  - `? : `를 기본으로 채용

## If 식

```scala
// imperative
var filename = "default.txt"
if (!args.isEmpty)
  filename = args(0)

// functional
val filename =
  if (!args.isEmpty) args(0)
  else "default.txt"
```

- val을 사용하므로서, 그 변수가 결코 변하지 않는다는것을 나타낼 수 있음
  - 그러므로 알기 쉬운 코드작성이 가능
- 변수의 이름을 사용하는 대신, 식을 그대로 쓸 수 있음

## while 루프

```scala
def gcdLoop(x: Long, y: Long): Long = {
  var a = x
  var b = y
  while (a != 0) {
    val temp = a
    a = b % a
    b = temp
  }
  b
}

var line = ""
do {
  line = readLine()
  println("Read: " + line)
} while (line != "")
```

- **Unit타입의 값을 반환하기 때문에 식이 아님**
- 결과 타입은 `Unit`임 즉 `()`랑 동등함
  - 스칼라에서는 엄밀한 의미의 `void`가 존재하지 않는 듯
- 함수형 프로그래밍 스타일로 작성했을때 보다 더 알기 쉬운 코드가 되는 경우에만 사용하는것을 권장

```scala
var line = ""
while ((line = readLine()) != "") // 이는 잘못된 결과를 불러일으킴
  println("Read: " + line)
```

- 위의 코드는 무한루프
  - 할당 연산자(메서드)의 리턴값은 `Unit`인데 `Unit`이 비교연산자를 사용할경우 언제나 `true`를 반환해서 무한루프가 되기 때문

## for 식

- 정말 활용도가 높음

### 컬렉션 순회 하기

```scala
val filesHere = (new java.io.File(".")).listFiles

for (file <- filesHere)
  println(file)
```

- `file <- filesHere`: 제너레이터
- `file`에는 toString메서드가 존재해서 파일의 이름과 디렉터리를 제공함
- for식은 어떠한 컬렉션의 종류에서도 사용 가능함
  - `Range`타입의 경우 매우 편리함
    - `a to b`: b포함
    - `a until b`: b미포함
- **컬렉션 자체를 순회하는 것으로 코드 수 절감, 더 알기 쉬운 코드가 작성가능**

```scala
for (i <- 1 to 4)
  println("Iteration " + i)
```

### 필터링

- for식과 filter를 이용해서 컬렉션 전체가 아닌, 일부만 순회할 수 있음
  - `for`의 괄호 안의 if문

```scala
// functional
val filesHere = (new java.io.File(".")).listFiles

for (file <- filesHere if file.getName.endsWith(".scala"))
  println(file)

// imperative
for (file <- filesHere)
  if (file.getName.endsWith(".scala"))
    println(file)
```

- 위의 코드는 눈에 보이는 결과는 같음
- 하지만 명령형으로 코드를 작성하면 `()`유닛값을 반환하게 되어서 부작용이 발생
  - 이는 `for 식`이기 때문

```scala
for (
  file <- filesHere
  if file.isFile
  if file.getName.endsWith(".scala")
) println(file) // 스칼라 파일중 디렉터리가 아닌 파일만 출력
```

### 네스팅된 순회

```scala
def fileLines(file: java.io.File) =
  scala.io.Souce.fromFile(file).getLines().toList

def grep(pattern: String) =
  for ( // 괄호대신 {}를 사용하면 ;로 다른 식을 넣을 수 있음
    file <- filesHere
    if file.getName.endsWith(".scala");
    line <- fileLines(file)
    if line.trim.matches(pattern)
  ) println(file + ": " + line.trim)

grep(".*gcd.*")
```

### 중간 스트림 변수 바인딩

- 위에서 `line.trim`이 계속해서 반복되므로, 한번만 하고 싶음
- `=`를 이용

```scala
def grep(pattern: String) =
  for {
    file <- filesHere
    if file.getName.endsWith(".scala")
    line <- filesLines(file)
    trimmed = line.trim
    if trimmed.matches(pattern)
  } println(file + ": " + trimmed)
```

### 새 컬렉션 생성

- 각각의 순회에 관한 값을 생성할 수 있음
- 키워드 `yield`를 사용

```scala
def scalaFiles =
  for {
    file <- filesHere
    if file.getName.endsWith(".scala")
  } yield file
```

- for식의 내용을 실행하는 각각의 시간마다 하나의 값을 생성
  - 위의 경우는 file
- 결과 값은 하나의 컬렉션에 많은 값들을 포함
  - `Array[File]`

```scala
val forLineLengths =
  for {
    file <- filesHere
    if file.getName.endsWith(".scala")
    line <- fileLines(file)
    trimmed = line.trim
    if trimmed.matches(".*for.*")
  } yield trimmed.length
```

## try 식으로 예외 처리 하기

### 예외 던지기(throwing exceptions)

```scala
throw new IllegalArgumentException

val half =
  if (n % 2 == 0)
    n / 2
  else
    throw new RuntimeException("n must be even")
```

- 값을 반환하지 못하게 함
- 예외 `throw`는 `Nothing`타입을 갖음

### 예외 포착하기

```scala
import java.io.FileReader
import java.io.FIleNotFoundException
import java.io.IOExcception

try {
  val f = new FileReader("input.txt")
} catch {
  case ex: FileNotFoundException => // Handle missing file
  case ex: IOException => // Handle other I/O error
}
```

### finally절

- 어떻게 식이 사라져도 코드를 실행할 수 있도록
- 데이터베이스, 소켓, 파일제어에서 유용
  - 스칼라에서는 `loan pattern`을 사용하는 경우가 많음

```scala
import java.io.FileReader

val file = new FileReader('input.txt')
try {
  // use the file
} finally {
  file.close()
}
```

### 값 생성하기

- `try-catch-finally`도 식임. 즉, 값을 반환
  - `finally`에서는 값을 반환하지 말자
  - 파일을 닫거나, 연결을 닫는 부작용을 하는 절이라고 생각하자

## Match 식

- `break`는 암묵적, `falling through`가 존재하지 않음
- 값을 반환

```scala
val firstArg = if (args.length > 0) args(0) else ""

firstArg match {
  case "salt" => println("pepper")
  case "chips" => println("salsa")
  case "eggs" => println("bacon")
  case _ => println("huh?")
}

```

```scala
val friendArg = if (!args.isEmpty) args(0) else ""

val friend =
  firstArg match {
    case "salt" => "pepper"
    case "chips" => "salsa"
    case "eggs" => "bacon"
    case _ => "huh?"
  }

println(friend)
```

## break와 continue없이 살기

- 함수 리터럴 안에서 잘 활용되지 않음
- 스칼라에서는 `break`와 `continue`를 그렇게까지 권장하지 않음
- 예제
  - `.scala`로 끝나는, 첫 글자가 `-`이 아닌 파일 이름을 찾기

```java
// java스타일

int i = 0;
boolean foundIt = false;
while (i < args.length) {
  if (args[i].startWith("-")) {
    i = i + 1;
    continue;
  }

  if (args[i].endsWith(".scala")) {
    foundIt = true
    break;
  }
  i = i + 1;
}
```

```scala
// scala imperative 스타일
var i = 0
var foundIt = false

while (i < args.length && !foundIt) {
  if (!args(i).startsWith("-")) {
    if (args(i).endsWith(".scala"))
      foundIt = true
  }
  i = i + 1
}

// 재귀함수 사용
def searchFrom(i: Int): Int =
  if (i >= args.length) -1
  else if (args(i).startsWith("-")) searchFrom(i+1)
  else if (args(i).endsWith(".scala")) i
  else searchFrom(i + 1)

val i = searchFrom(0)
```

- 스칼라 컴파일러는 위의 코드에 대해서 재귀함수를 컴파일 결과로 나타내지 않을것임
  - 꼬리재귀 최적화가 되기 때문
  - `while`루프와 비슷하게 됨
    - 각각의 재귀는 함수의 첫 부분으로 되돌아가게 구현됨

```scala
import scala.util.control.Breaks._
import java.io._

val in = new BuffreredReader(new InputStreamReader(System.in))

breakable { // catch the exception
  while (true) {
    println("? ")
    if (in.readLine() == "") break // throwing an exception
  }
}
```

## 변수 스코프

- 스코프: 이름을 사용할 수 있는 공간
  - 대괄호는 새로운 스코프를 만듬
- 지역 변수(local variable)

## 명령형 스타일 코드 리팩터링하기

- 부작용이 없으면 유닛테스트 하기 쉬움

```scala
// imperative
def printMultiTable() {
  var i = 1
  while (i <= 10) {
    var j = 1
    while (j <= 10) {
      val prod = (i * j).toString
      var k = prod.length
      while (k < 4) {
        println(" ")
        k += 1
      }
      print(prod)
      j += 1
    }
    println()
    i += 1
  }
}
```

```scala
// functional
def makeRowSeq(row: Int) =
  for (col <- 1 to 10) yield {
    val prod = (row * col).toString
    val padding = " " * (4 - prod.length)
    padding + prod
  }

def makeRow(row: Int) = makeRowSeq(row).mkString

def multiTable() = {
  val tableSeq =
    for (row <- 1 to 10)
    yield makeRow(row)
  tableSeq.mkString("\n")
}
```
