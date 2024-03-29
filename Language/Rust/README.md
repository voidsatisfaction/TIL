# 그 책

https://rinthel.github.io/rust-lang-book-ko/ch00-00-introduction.html

- 1 시작하기
  - 소개
  - Cargo
- 3 보편적인 프로그래밍 개념
- 4 소유권 이해하기
- 5 연관된 데이터들을 구조체로 다루기
- 8 일반적인 컬렉션

## 의문

- *링커가 뭐지?*

## 1. 시작하기

### 소개

- 컴파일러가 매우 강력하다
  - 동시성 버그를 비롯하여 찾기 어려운 버그를 가진 코드는 컴파일 거부
    - *어떻게 이게 가능한것일까?*
- 현대적 개발자 도구
  - Cargo
  - Rustfmt
    - 일관적인 코딩 스타일
  - Rust Language Server
    - IDE와 결합해서 자동완성, 인라인 에러 기능 제공
- 속도와 안정성을 둘다 소중히 여긴다
  - 속도
    - 프로그램의 속도
    - 생산성
  - 안정성
- 감상
  - 인간의 모든 실수를 미리 예상해서 막아주려는 노력의 흔적이 보임
    - 그런데 진짜 모든 것을 막아줄 수 있을까?
    - e.g) data race

### Cargo

- 개요
  - 러스트 빌드 시스템 및 패키지 매니저
  - c.f) crate
    - 코드의 패키지(라이브러리)
- 장점
  - OS를 위한 특정 명령이 없음
- 프로젝트 생성
  - `cargo new hello_cargo --bin`
- `cargo build`
  - `target/debug/hello_cargo`
    - 실행파일 생성
- `cargo run`
  - 실행
- `cargo check`
  - 코드가 컴파일되는지 빠르게 확인

## 3. 보편적인 프로그래밍 개념

### Shadowing

```rust
fn main() {
  let x = 5;

  // immutability is maintained
  let x = x + 1;

  let x = x * 2;

  println!("The value of x is: {}", x);
}
```

### 타입

- 스칼라 타입
  - integer
    - `i8, u8, i16, u16, i32(default), u32, i64, u64, isize, usize`
  - float
    - `f32, f64(default)`
    - *f32, f64의 차이? 정밀도?*
  - boolean
    - `true, false`
  - char
    - unicode scalar
- 복합 타입
  - tuple
    - `let tup: (i32, f64, u8) = (500, 6.4, 1)`
  - array
    - 같은 타입의 고정된 길이의 값들의 집합체

### 함수

- expression
  - literal, operation, block, function call, macro, if expression
    - 종결을 나타내는 세미콜론을 사용하지 않음
    - 함수는 암묵적으로 마지막 표현식 반환
- statement

### 제어문

- loop
- while
- for
  - collection반복

## 4. 소유권 이해하기

### 4.1 소유권이 뭔가요?

- 메모리 관리
  - gc
  - 프로그래머가 명시적으로 메모리 할당 / 해제
  - 컴파일 타임에 컴파일러가 체크할 규칙들로 구성된 소유권 시스템을 통해 관리
- 소유권
  - 정의
    - 힙 데이터를 관리하기 위한 러스트만의 고유한 메모리 관리 시스템
  - 규칙
    - 1 러스트의 각각의 값은 해당값의 owner라고 불리는 변수를 갖고 있음
    - 2 한번에 딱 하나의 owner만 존재할 수 있음
    - 3 owner가 스코프 밖을 벗어나는 때, 값은 버려짐

#### String 예제와 함께하는 소유권 이해

- 힙 메모리와 할당
  - 1 런타임에 운영체제로부터 메모리가 요청되어야 한다
  - 2 `String`의 사용이 끝났을 때 운영체제에게 메모리를 반납할 방법이 필요하다
    - 어려움
- RAII(Resource Acquisition Is Initialization)
  - 아이템의 수명주기의 끝나는 시점에 자원을 해제

Rust RAII의 예시

```rust
{
    let s = String::from("hello"); // s는 여기서부터 유효합니다

    // s를 가지고 뭔가 합니다
}                                  // 이 스코프는 끝났고, s는 더 이상
                                   // 유효하지 않습니다(drop 자동 호출)
```

- 변수와 (힙)데이터가 상호작용하는 방법: 이동(move)
  - 정의
    - 소유권의 이전
  - 특징
    - `(let s2 = s1)`
    - s1은 더이상 유효하지 않은 name
  - 이유
    - double free error를 피하기 위함
- 변수와 (힙)데이터가 상호작용하는 방법: 클론(clone)
  - 정의
    - 힙 데이터의 복사
  - 특징
    - 다른 언어에서의 deep copy
    - c.f) 기본적으로 스택에만 있는 데이터는, 컴파일 타임에 크기가 모두 확정되기 때문에 쉽게 복사가 됨
      - scalar 데이터 타입은 기본적으로 copy
      - scalar 데이터 타입으로만 구성된 tuple도 copy
  - 이유
    - 때로는 정말로 복사가 필요한 경우가 존재
- 소유권과 함수
  - 함수에게 변수를 argument로 넘겨주는 것은 move or copy임
    - scalar가 아닌경우 move
    - references, borrowing으로 해결

```rust
fn main() {
    let s = String::from("hello");  // s가 스코프 안으로 들어왔습니다.

    takes_ownership(s);             // s의 값이 함수 안으로 이동했습니다...
                                    // ... 그리고 이제 더이상 유효하지 않습니다.
    let x = 5;                      // x가 스코프 안으로 들어왔습니다.

    makes_copy(x);                  // x가 함수 안으로 이동했습니다만,
                                    // i32는 Copy가 되므로, x를 이후에 계속
                                    // 사용해도 됩니다.

} // 여기서 x는 스코프 밖으로 나가고, s도 그 후 나갑니다. 하지만 s는 이미 이동되었으므로,
  // 별다른 일이 발생하지 않습니다.

fn takes_ownership(some_string: String) { // some_string이 스코프 안으로 들어왔습니다.
    println!("{}", some_string);
} // 여기서 some_string이 스코프 밖으로 벗어났고 `drop`이 호출됩니다. 메모리는
  // 해제되었습니다.

fn makes_copy(some_integer: i32) { // some_integer이 스코프 안으로 들어왔습니다.
    println!("{}", some_integer);
} // 여기서 some_integer가 스코프 밖으로 벗어났습니다. 별다른 일은 발생하지 않습니다.
```

### 4.2 참조자(References)와 빌림(Borrowing)

```rust
fn main() {
    let s1 = String::from("hello");

    let len = calculate_length(&s1);

    println!("The length of '{}' is {}.", s1, len);
}

fn calculate_length(s: &String) -> usize { // s는 String의 참조자입니다
    s.len()
} // 여기서 s는 스코프 밖으로 벗어났습니다. 하지만 가리키고 있는 값에 대한 소유권이 없기
  // 때문에, 아무런 일도 발생하지 않습니다.

```

위 코드에 대한 References and borrowing 다이어그램 예시

![](./images/references_and_borrowing1.png)

- 참조자
  - 정의
    - 값은 참조하지만 소유하지는 않음
  - 특징
    - 참조하는 것은 데이터 변경 불가
- 가변 참조자
  - 특징
    - 참조하는 것을 변경하려면 가변 참조자(mutable references)로 만들어야 함
    - 특정한 스코프 내에 특정한 데이터에 대한 가변 참조자를 딱 하나만 만들 수 있음
      - compile time data race 방지
      - 그래서 여러개만들고 싶으면, 블록으로 가변참조자 여러개 만들면 됨
    - 불변 참조자가 있을때는 가변 참조자를 만들 수 없음
      - 단순히 read할때는 data race가 일어나지 않음
  - c.f) data race 조건
    - 두 개 이상의 포인터가 동시에 같은 데이터에 접근
    - 그 중 적어도 하나의 포인터가 데이터를 작성
    - 데이터에 접근하는데 동기화를 하는 어떠한 메커니즘도 없음
  - c.f) dangling references
    - 어떤 메모리를 가리키는 포인터를 보존하는 동안, 그 메모리를 해제함으로써 다른 개체에게 사용하도록 줘버렸을 지도 모를 메모리를 참조하고 있는 포인터
- 빌림
  - 정의
    - 함수의 파라미터로 참조자를 만드는 것

### 4.3 슬라이스

스트링 슬라이스 코드 예시

```rust
let s = String::from("hello world")

let hello = &s[0..5];
let world = &s[6..11];
```

위 코드에 대한 slice 다이어그램 예시

![](./images/slice1.png)

- 슬라이스
  - 정의
    - 컬렉션 전체가 아닌, 컬렉션의 연속된 일련의 요소들을 참조할 수 있게 함
- 주의
  - `String` type과 `&str` 타입은 엄연히 다름

## 5. 연관된 데이터들을 구조체로 다루기

### 5.1 구조체를 정의하고 생성하기

```rust
struct User {
  username: String,
  email: String,
  sign_in_count: u64,
  active: bool,
}

let mut user1 = User {
    email: String::from("someone@example.com"),
    username: String::from("someusername123"),
    active: true,
    sign_in_count: 1,
};

user1.email = String::from("anotheremail@example.com");

fn build_user(email: String, username: String) -> User {
    User {
        email,
        username,
        active: true,
        sign_in_count: 1,
    }
};

// 기존 구조체 데이터로 새로운 구조체 생성
let user2 = User {
    email: String::from("another@example.com"),
    username: String::from("anotherusername567"),
    ..user1
};

// tuple structs
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

let black = Color(0, 0, 0);
let origin = Point(0, 0, 0);

// unit-like structs
어떤 필드도 없는 구조체
특정 타입의 trait을 구현해야하지만, 타입 자체에 데이터를 저장하지 않는 경우에 유용
```

- 구조체 데이터의 소유권
  - 기본적으로 구조체가 데이터를 소유함
  - 구조체가 소유권이 없는 데이터의 참조를 저장할 수 있지만, 라이프 타임의 사용을 전제로 함

### 5.2 구조체를 이용한 예제 프로그램

### 5.3 메소드 문법

## 8. 일반적인 컬렉션

### 8.1 벡터

### 8.2 스트링

- 스트링
  - 스트링
    - 러스트 표준 라이브러리
  - 스트링 슬라이스
    - 스트링 타입
- 특징
  - UTF-8로 인코딩
  - 인덱싱 문법으로 접근 불가
  - `Vec<u8>`을 래핑한 것
    - `String::from("Hola").len() == 4, String::from("Здравствуйте") == 24`
    - `hello[0..4] == "Зд"`
  - 복잡함

## 9. 에러 처리

- 복구 가능한 에러
  - `Result<T, E>`
- 복구 불가능한 에러
  - `panic!`
    - 실패 메시지 출력
    - 스택 되감기(데이터 제거)
      - *굳이 제거를 해야함?*
    - 종료

## 10. 제네릭 타입, 트레잇, 그리고 라이프타임

- 제네릭
  - 개요
    - 구체화된 타입이나 다른 속성들에 대하여 추상회된 대리인
  - 사용 대상
    - 함수, 구조체, 열거형
  - 추출법
    - 중복된 코드(타입)가 있음을 파악
      - e.g) 이름과 시그니처만 다른 두 함수
    - 중복된 코드를 generic한 타입으로 추출
      - generic대신에 ISortable과 같은 인터페이스로도 구현 가능
        - 서로의 장단점?
- 트레잇
  - 개요
    - 타입들이 공통적으로 갖는 동작에 대하여 추상화
    - 제네릭 타입과 결합되어, 제네릭 타입에 대해 아무 타입이나 허용하지 않고, 특정 동작을 하는 타입으로 제한
      - 우리가 사용하길 원하는 동작을 갖도록 하기 위해 trait bounds를 사용할 수 있음
- 라이프타임
  - 개요
    - 제네릭의 일종으로서, 컴파일러에게 참조자들이 서로에게 어떤 연관이 있는지에 대한 정보를 줄 수 있도록 해줌

### 10.1 제네릭 데이터 타입

```rust
struct Point<T, U> {
    x: T,
    y: U,
}

impl<T, U> Point<T, U> {
    fn mixup<V, W>(self, other: Point<V, W>) -> Point<T, W> {
        Point {
            x: self.x,
            y: other.y,
        }
    }
}

fn main() {
    let p1 = Point { x: 5, y: 10.4 };
    let p2 = Point { x: "Hello", y: 'c'};

    let p3 = p1.mixup(p2);

    println!("p3.x = {}, p3.y = {}", p3.x, p3.y);
}
```

- 런타임 코드 실행 속도는 컴파일타임 monomorphization(구체적 타입으로 된 코드로 변형) 덕분에, 그대로

### 10.2 트레잇: 공유 동작을 정의하기

```rust
// 시그니처만

pub trait Summarizable {
    fn summary(&self) -> String;
}

// 기본 구현

pub trait Summarizable {
    fn summary(&self) -> String {
        String::from("(Read more...)")
    }
}

pub struct NewsArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}

impl Summarizable for NewsArticle {
    fn summary(&self) -> String {
        format!("{}, by {} ({})", self.headline, self.author, self.location)
    }
}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

impl Summarizable for Tweet {
    fn summary(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}
```

- 트레잇 바운드
  - 제네릭 타입에 제약을 가할 수 있음
  - 제네릭 타입이 특정한 트레잇을 구현하여 이 타입들이 가지고 있을 필요가 있는 동작을 갖고 있도록 제한
    - *그런데, 그냥 trait으로 type annotation하지 왜 뭐하러 generic까지 씀?*
- 런타임 에러를 컴파일 에러로

```rust
pub fn notify<T: Summarizable>(item: T) {
    println!("Breaking news! {}", item.summary());
}

fn some_function<T: Display + Clone, U: Clone + Debug>(t: T, u: U) -> i32 {
  ...
}

fn some_function<T, U>(t: T, u: U) -> i32
    where T: Display + Clone,
          U: Clone + Debug
{
  ...
}
```

### 10.3 라이프타임을 이용한 참조자 유효화
