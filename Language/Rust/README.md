# 그 책

https://rinthel.github.io/rust-lang-book-ko/ch00-00-introduction.html

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
