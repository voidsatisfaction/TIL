# Next Steps in Scala

## Step 7. 타입을 이용해서 배열을 매개변수화(parameterize) 함

- `new` 키워드를 이용해서 오브젝트와 클래스를 initialize할 수 있다.
- 스칼라에서는 initialize할 때에 `parameterize`할 수 있다(값과, 타입을 지정)
- 하지만 이런 식으로 생성하는 것은 바람직하지 않음.

```scala
val big = new java.math.BigInteger("12345")

val greetStrings = new Array[String](3)

greetStrings(0) = "Hello"
greetStrings(1) = ", "
greetStrings(2) = "world!\n"

for (i <- 0 to 2)
  print(greetStrings(i))
```

- `greetingStrings`는 항상 같은 배열(`Array[String]`)을 가르킴
- 하지만 그 배열의 요소는 변경가능함(mutable)
- `0 to 2`
  - (0).to(2)와 같음
  - 이는 명시적으로 메서드의 리시버(receiver)를 나타냈을 때만 사용 가능
- `1 + 2`
  - `(1).+(2)`와 같음
  - 정수 오브젝트인 1이 +메서드를 2로인자로 넘겨주면서 부름
  - 스칼라는 연산자 오버로딩이 없음. 전통적인 연산자가 존재하지 않기 때문
- `greetingStrings(i)`
  - `greetingStrings.apply(i)`와 같음
  - 배열 요소에의 접근은 단순히 메서드 호출과 같다
    - 사실 모든 오브젝트에 같은 논리가 적용
    - 오직 `apply`라는 메서드가 정의 되어야만이 컴파일 가능
- `greetingStrings(i) = "Hello"`
  - `greetingStrings.update(0, "Hello")`와 같음
  - 하나나 그 이상의 `apply`된 인자가 있는 곳에 할당기호가 있으면, 컴파일러는 그것을 `update`메서드의 호출로 봄

- 스칼라의 간결함
  - **모든 것을 오브젝트와 메서드로 표현**
- 보다 더 나은 표현

```scala
val numValues = Array("zero", "one", "two") // factory메서드인 apply메서드 호출

val numValues2 = Array.apply("zero", "one", "two")
```

- 위의 `apply`메서드는 factory메서드
- 이 메서드는 `Array companion object`에 정의되어있음
  - 동료 오브젝트
    - `Array`클래스 안에 `apply`라는 이름을 가진 클래스 메서드(static method)가 있다고 생각하면 됨

## Step 8. 리스트 사용하기

- 함수형 프로그래밍에 있어서 OOP에서는 불변성이 매우 중요함
- 배열
  - 가변 객체(요소의 내용을 변경 가능)
- 리스트
  - 불변 객체(요소의 내용을 변경 불가)
    - `:::`
      - 새로운 리스트 생성
    - `::`
      - cons
      - 메서드가 콜론으로 끝나는 경우는 오른쪽 항이 메서드를 부르는 것으로 함
      - `1 :: twoThree`
        - `twoThree.::(1)`과 같음
        - 대신 결과 값은 `List(1, 2, 3)`
      - 비어있는 리스트는 `Nil`이므로
        - `1 :: 2 :: 3 :: Nil`
        - 이는 `List(1, 2, 3)`과 같음

```scala
val oneTwo = List(1, 2)
val threeFour = List(3, 4)
val oneTwoThreeFour = oneTwo ::: threeFour // new list (concatenation)

val twoThree = List(2, 3)
val oneTwoThree = 1 :: twoThree
println(oneTwoThree) // List(1, 2, 3)

```

## Step 9. 튜플(tuple) 사용하기

- 불변성
- 다양한 타입의 요소들을 가질 수 있음
- 최대길이는 22까지
- 다른 함수형 언어에서도 튜플을 1베이스 인덱싱하므로 따라함

```scala
val pair = (99, "Luftballons") // type: Tuple2[Int, String]
println(pair._1) // 99
println(pair._2) // Luftballons

val other = ("u", "r", "the", 1, 4, "me") // type: Tuple6[Char, Char, String, Int, Int, String]
```

## Step 10. 집합(sets)과 맵(maps) 사용하기

- 집합
  - 불변, 가변의 집합이 존재
  - `+`
    - 가변 집합: 자기자신에 요소를 더함
    - 불변 집합: 새로운 집합을 생성하고 그곳에 다 더한후 반환

```scala
var jetSet = Set("Boeing", "Airbus") // immutable
jetSet += "Lear" // 새로운 jetSet을 만듬, 새로운 오브젝트의 재할당을 위해서 var로 선언
println(jetSet.contains("Cessna"))

import scala.collection.mutable.Set

val movieSet = Set("Hitch", "Poltergeist") // mutable
movieSet += "Shrek" // add element, 기존의 오브젝트를 변형하므로 val로 선언
println(movieSet)

import scala.collection.immutable.HashSet

val hashSet = HashSet("Tomatoes", "Chilies")
println(hashSet + "Coriander")
```

- 맵
  - 불변, 가변 맵이 존재
  - `->`
    - `1 -> "Go to island"`는 아래와 같음
    - `(1).->("Go to island.")`
    - 키와 값을 갖는 두개의 요소를 갖는 튜플을 반환
    - 이 튜플을 += 메서드의 인자로 줌

```scala
import scala.collection.mutable.Map

val treasureMap = Map[Int, String]()
treasureMap += (1 -> "Go to island.")
treasureMap += (2 -> "Find big X on ground.")
treasureMap += (3 -> "Dig.")
println(treasureMap(2))

// 불변 맵이 초기설정
// scala.collection.immutable.Map
```

## Step 11. 함수형 스타일을 알아보자

- 함수형
  - `var`을 사용하지 않음
    - 스칼라에서는 `var`이든 `val`이든 둘다 유용한 도구(상황에 따라서 맞춰 사용)
  - 더 알아보기 쉽고 에러가 나기 어려운 코드를 쓰기위해
  - 테스트 하기도 쉬움

## Step 12. 파일에서 줄읽기

```scala
import scala.io.Source

if (args.length > 0) {
  for (line <- Source.fromFile(args(0)).getLines())
    println(line.length + " " + line)
}
else
  Console.err.println("Please enter filename")
```
