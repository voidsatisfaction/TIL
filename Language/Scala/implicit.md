# implicit 이해하기

- 참조
  - [스칼라 강좌 - implicit](http://hamait.tistory.com/605)

## 암시적 변환과 암시적 파라미터

### 암시규칙

- `x + y`라는 표현식에서 타입오류가 있으면 컴파일러는 `convert(x) + y`를 시도해봄
- `convert`는 암시적으로 적용되는 변환에 사용

- **표시규칙** : implicit으로 표시한 정의만 검토 대상이 됨, 변수, 함수, 객체정의에 사용 가능
- **스코프 규칙** : 삽입할 implicit 변환은 스코프 내에 단일 식별자로만 존재하거나, 변환의 결과나 원래 타입과 연관이 있어야 함
  - `someVariable.convert` 불가능, 외부에서 가져올 경우 `import Preamble._`를 이용해서 단일 식별자로 가리킬 수 있게 해야함
  - 스코프 종류
    - local scope
    - import된 implicit값
    - class의 패키지 오브젝트
    - class의 컴페니언 오브젝트
    - 부모 클래스 / 트레 혹은 그것들의 컴페니언 오브젝트
- **한번에 하나만** : 오직 하나의 암시적 선언만 사용, `convert1(convert2(x)) + y`는 불가능
- **명시성 우선 규칙** : 코드가 그 상태 그대로 타입 검사를 통과하면 암시를 통한 변환 시도하지 않음

### 암시적 변환(implicit conversion)

버튼에 행동 추가하기

```scala
// too verbose
button.addButtonDownAction(
  new ActionListener {
    def actionPerformed(event: ActionEvent) {
      println("hi")
    }
  }
)
```

`implicit`을 이용한 간단한 코드

```scala
implicit def functionToActionClass(f: ActionEvent => Unit) = {
  new ActionListener {
    def actionPerformed(event: ActionEvent) = f(event)
  }
}

button.addButtonDownAction((_: ActionEvent) => println("hi")) // work nicely
```

### 암시적 파라미터(implicit parameter)

- 매개변수를 암시적으로 넣어줌(자동으로 들어감)
- 미리 변수 정의: `implicit val b = new B;`
- 함수를 인자 없이 호출: `test(a)`
- 호출 당하는 함수쪽에 인자를 `implicit`로 설정: `def test(a: A, implicit b: B) {}`

```scala
object HamaPrefs {
  implicit val prompt = new MyPrompt("ubuntu>")
}

object Greeter {
  def greet(name: String) (implicit prompt: MyPrompt) {
    println(name)
    println(prompt.preference)
  }
}

Greeter.greet("hi") // hi, ubuntu>
```

### 실전 예제

- 쇼핑몰 사이트에서 방문자의 장바구니에 상품이 몇개가 담겨있는지 보여주고자 할 때를 생각해보자

```scala
// shop.scala
obejct Shop extends Controller with WithCart {
  def catalog() = Action { implicit request =>
    val products = ProductDAO.list
    OK(views.html.products.catalog(products))
  }
}
```

```scala
// catalog.scala.html
@(products: Seq[Product])(implicit cart: Cart)

// main 뷰 템플릿으로 cart를 명시적으로 넘겨주지 않음
@main() {
  <h2>Catalog</h2>
  <ul>
  @for(product <- products) {
    <li>
      <h3>@product.name</h3>
      <p class="description">@product.description</p>
    </li>
  }
  </ul>
}
```

```scala
@(content: Html)(implicit cart: Cart)
<!DOCTYPE html>
<html>
    ... 생략 ...

    <span id="cartSummary" class="label label-info">
      @cart.productCount match {
        case 0 => {
          Your shopping cart is empty.
        }

        case n => {
          You have @n items in your shopping cart.
        }
      }
    </span>

    <div class="container">
      @content
    </div>
```

- cart를 매번 세션에서 직접 가져오는 번복이 사라짐

```scala
trait WithCart {
  implicit def cart(implicit request: RequestHeader) = {
    Cart.demoCart()
  }
}
```

- `WithCart`는 위와같은 구현
