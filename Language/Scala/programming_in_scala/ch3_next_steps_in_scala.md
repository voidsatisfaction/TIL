# Next Steps in Scala

## Step 7. Parameterize arrays with types

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
