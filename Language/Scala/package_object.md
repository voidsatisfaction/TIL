# 패키지 오브젝트

스칼라에서는 많은 독자적인 로직이 존재함. 하나하나가 충분히 납득이 가고 멋진 기능을 가진 도구임에 틀림없으나, 프로그래머가 좋은 코드를 쓰려면 이러한 도구들을 정확하고 전부 알고 있어야 하는 코스트가 생김

## 예시

- 패키지 오브젝트
- 아래의 코드는 repository에서 공통으로 사용되는 로직을 재활용하기 위해서 만들어 놓음
- run메서드는 오직 repository패키지 안에서만 사용 가능

```scala
// scala/interndiary/repository/package.scala

package interndiary
import slick.dbio.{NoStream, DBIOAction}

package object repository {
  // package private
  private[repository] def run[R](a: DBIOAction[R, NoStream, Nothing])(implicit ctx: Context): R = Context.runDBIO(a)
}
```
