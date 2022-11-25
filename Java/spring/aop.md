# AOP(Aspect Oriented Programming)

- 의문
- 개요
- 주의

## 의문

## 개요

## 주의

- 애노테이션은 클래스의 최상위 public 메서드에만 적용 가능
  - 예를들어, 스프링 컨트롤러 내부에서, `@Transactional`, `@EnableReadReplica`와 같은 어노테이션을 붙인 퍼블릭 메서드를 동작시켜도, AOP가 적용되지 않음(즉 트랜잭션과 read replica 설정이 무시됨)
