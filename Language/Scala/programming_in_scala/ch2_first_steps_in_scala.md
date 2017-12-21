# Ch2 First Steps in Scala

## Step 1. 스칼라 인터프리터 사용법 배우기

```scala
scala> 1 + 2
res0: Int = 3
```

- 위에서 타입 `Int`는 패키지 `scala`의 `Int`클래스를 나타낸다.
- 패키지는 글로벌 네임스페이스로서 정보 은닉(information hiding)을 위한 매커니즘을 제공한다.
- 모든 자바의 `primitive types`는 `scala`패키지의 클래스에 대응하는 클래스들을 보유한다.

## Step 2. 변수 정의하기

- 스칼라는 `vals`(재할당 불가)와 `vars`(재할당 가능)라는 두 종류의 변수를 갖는다.

```scala
val msg = "Hello, world!" // 이미 타입 추론을 하고 있음
// msg: java.lang.String = Hello, World!

val msg2: java.lang.String = "Hello again, world!" // 명시적으로 타입을 나타냄
val msg3: String = "Hello yet again, world!" // 위와 같음
```

```scala
var greeting = "Hello, world!"
greeting = "Leave me alone, world!"
```

## Step 3. 함수 정의하기

```scala
def max(x: Int, y: Int): Int = {
  if (x > y) x
  else y
}
```

- 위의 `max`함수는 타입추론을 할 수 있지만 명시적으로 써 놓는것이 읽기 좋은 코드를 위한 선택이 될 수 있다.

```scala
def greet() = println("Hello, world!") // Unit타입. 이는 자바의 void 타입과 비슷하다.
```

- `Unit`타입의 함수는 `side effects`를 위해서만 실행된다.

## Step 4. 스칼라 스크립트 작성하기

```scala
object Hello {
  def main(args: Array[String]) = { // args로 커맨드라인 인자를 받을 수 있다.
    println("Hello, "+ args(0) + "!") // 배열의 요소 참조는 ()로 한다.
    println("Hello, world, from a script!")
  }
}
```

## Step 5. while과 함께하는 반복문, if와 함께하는 선택

```scala
object Hello {
  def main(args: Array[String]) = {
    var i = 0
    while (i < args.length) {
      if (i != 0)
        print(" ") // if 뒤에 한 줄만 올 경우 블록을 생략할 수 있다.
      print(args(i))
      i += 1
    }
    println()
  }
}
```

## Step 6. `foreach`와 `for`을 사용한 `Iteration`

- 스칼라에서 함수는 `first-class-constructs`이다.

```scala
// foreach라는 메소드에 arg를 매개변수로 받는 함수 리터럴을 넘겨준다.
// 매개변수가 하나고, 타입추론을 이용하고 있으므로 괄호는 생략 가능.
args.foreach(arg => println(arg))

// 타입을 명시하고 있으므로, 괄호가 필요.
args.foreach((arg: String) => println(arg))

// 더 간결한 코드
args.foreach(println)
```

`for`를 사용한 iteration

```scala
for (arg <- args)
  println(arg)
```

- for에서 화살표(`<-`) 왼쪽의 값은 `val`이다. 그러므로 불변(immutable).
