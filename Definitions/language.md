# Language

- 의문
- Java

## 의문

## Java

WORA(Write Once and Run Anywhere)

- 개요
  - 1 언어
  - 2 애플리케이션 소프트웨어를 개발하고, 크로스 플랫폼 컴퓨팅 환경에 배포하기 위한 컴퓨터 소프트웨어와 스펙의 집합인 플랫폼
    - 다양한 하드웨어와 OS위에서 자바 프로그램을 전부 동일하게 실행시킬 수 있도록 함
- 플랫폼 구성
  - Byte code compilers
    - Java, Ada, Javascript, Python, Ruby 코드를 bytecode로 변환
  - JRE(Java Runtime Environment)
    - JVM(Java Virtual Machine)
      - 역할
        - bytecode실행
        - GC
      - 특징
        - OS-dependent
    - JIT compiler
      - 런타임에 bytecode를 native processor instruction으로 컴파일하고 인메모리에 캐싱함
  - Libraries
    - 현대 OS에서 찾아볼 수 있는 공통적으로 재사용가능한 함수들을 포함하는 자체 표준 클래스 라이브러리를 제공
    - 역할
      - 프로그래머가 일반적으로 사용하는 standard library기능
      - 하드웨어나 OS에 강하게 의존할만한 인터페이스를 추상화 함
      - 주어진 플랫폼이 자바 애플리케이션이 기대하는 모든 기능을 서포트하지 않을 경우, class libraries가 존재하지 않는 컴포넌트를 잘 다룸
- 플랫폼에서 동작하는 언어들
  - Clojure
  - Jython
  - Kotlin
  - Scala
- 유사 플랫폼
  - .NET platform
    - 자바의 성공에 자극을 받아서 만들어짐
    - 컴파일된 byte code를 CLR(Common Language Runtime)가 실행함
- JDK
  - 자바 SDK
    - Java compiler, JRE 등 다양한 툴이 포함됨
