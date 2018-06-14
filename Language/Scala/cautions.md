# 스칼라에서 오해하기 쉬운 것들

## 1. a b와 a(b)의 차이

```scala
a b == a.b

a b != a(b)

obj meth arg == obj.meth(arg)
```

즉, `println "hi"`는 동작하지 않는다.

## 2. 클래스 인스턴스화 할떄의 블록

```scala
class B {
  var x1: String = "B"

  def setText(text: String) {
    x1 = text
  }

  override def toString = x1
}

new B { setText("next Text") } // o
new B { setText "next Text" } // x
new B { this setText "next Text" } // o
new B { o => // self-type alias
  o setText "new Text"
} // o
```

클래스를 인스턴스화 할때, 블록을 사용할 수 있는데 이는, 컨스트럭터 로직으로 추가된다(물론 인스턴스 메서드를 그 블록 안에서 사용 가능)
