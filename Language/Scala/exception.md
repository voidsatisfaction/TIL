# 예외 처리

## 목차

- allCatch

## allCatch

```scala
import scala.util.control.Exception._

allCatch.opt("42".toInt) // Some(42)
allCatch.opt("42a".toInt) // None

allCatch.toTry("42".toInt) // 42
allCatch.toTry("42a".toInt) // Failure(java.lang.NumberFormatException: For input string: "42a")

allCatch.either("42".toInt) // Right(42)
allCatch.either("42a".toInt) // Left(java.lang.NumberFormatException: For input string: "42a")
```
