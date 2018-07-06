# 보다 알기 쉬운 코드를 쓰기 위한 방법

## 오브젝트 내의 클래스, 클래스 내의 오브젝트

- 오브젝트 안에 클래스 선언
- 클래스 안에 오브젝트 선언
  - 위의 행위가 스칼라에서는 쉽게 가능하다는 것을 이용해서 읽기 쉬운 코드를 작성가능

```scala
object Join {
  class Inner[A, B, It[X] <: IterableLike[X, It[X]]](
    left: It[A],
    right: Iterable[B]
  ) {
    def on[K](
      leftKey: A => K,
      rightKey: B => K
    :disappointed: Join[A, B, K, It] = Join(left, right, leftKey, rightKey, _ => None)
  }
}

Join.Inner(a, b).on(_.key, _.key)
```
