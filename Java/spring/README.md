# Spring

- 의문
- 개요
- Bean

## 의문

## 개요

## Bean

- 개요
  - Spring IoC 컨테이너가 관리하는 자바 객체
  - `ApplicationContext.getBean()`으로 얻어질 수 있는 객체
- 등록 방법
  - 1 Component Scanning
    - `@SpringBootApplication`
      - `@ComponentScan`
        - 어디서부터 컴포넌트를 찾아볼 것인지 알려줌
        - `@Component`애노테이션 or `@Component`애노테이션을 사용하는 다른 애노테이션이 붙은 클래스를 찾음
  - 빈 설정파일에 직접 빈을 등록
    - 2 자바 설정 파일
      - 클래스에 `@Configuration`애노테이션을 붙이고, 그 안에 `@Bean` 애노테이션을 사용해서 직접 빈을 정의
        - 환경변수에 따라서, 다른 빈을 주입할 때에 사용
          - `@Configuration`애노테이션 자체도 `@Component`를 사용하므로, `@ComponentScan`의 스캔 대상이 되고, 그에 따라 빈 설정파일이 읽힐 때, 그 안에 정의된 빈들이 IoC 컨테이너에 등록됨
    - 3 XML
      - 요즘은 잘 사용하지 않음
