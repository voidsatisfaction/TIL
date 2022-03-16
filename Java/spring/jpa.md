# Spring data-jpa

- 의문
- TransactionManager
- Annotations
  - Transactional

## 의문

## TransactionManager

*어디까지가 스프링에서 해주고, 어디까지가 jpa가 해주는건지 명확화 하면 좋을듯*

JPA transaction manager

![](./images/jpa/transaction_manager1.png)

- `TransactionManager`
  - 개요
    - spring transaction manager 의 최상위 인터페이스(아무 동작 없음)
    - 하나의 트랜잭션의 생성, 커밋, 롤백과 같은 라이프사이클을 관리하기위한 매니저
- `PlatformTransactionManager`
  - 개요
    - spring의 imperative transaction 인프라에서의 중심이 되는 인터페이스
    - 직접 사용하는 용도가 아니라, `TransactionTemplate`나 `AOP`를 이용해서 사용
    - 이걸 직접 구현하기 보다는 `AbstractPlatformTransactionManager`클래스가 미리 propagation behaviour와 synchronization handling을 구현했으니 그걸 상속받아서 구현하는걸 추천
  - API
    - `TransactionStatus getTransaction(@Nullable TransactionDefinition definition)`
    - `void commit(TransactionStatus status) throws TransactionException;`
    - `void rollback(TransactionStatus status) throws TransactionException;`

### 회사에서는 TransactionManager를 어떻게 사용하고 있는가?

## Annotations

### Transactional

- 개요
  - 하나의 메서드나 클래스 트랜잭션 속성을 부여
- 특징
  - 클래스 레벨로 어노테이션이 된 경우
    - 클래스와 서브클래스의 모든 메서드에 적용
    - 조상 메서드에 적용하려면, 재선언해줘야 함
  - `RuntimeException`이나 `Error`가 발생했을 경우 롤백이 됨
    - checked exception의 경우에는 롤백하지 않음
  - `PlatformTransactionManager`에 의해서 thread-bound로 관리됨
    - 해당 트랜젝션을 현재 **실행중인 스레드 내에서** 모든 데이터 접근 연산들에게 노출함
      - 그렇기 때문에 컨트롤러에서 `suspend function`과 `Transactional`을 같이 사용하지 못함
        - 중간에 디스패쳐에 의해서 스레드가 변경될 수 있으므로
- 속성
  - `TransactionDefinition`
    - 개요
      - spring-compliant transaction 속성
    - propagation 속성
      - `PROPAGATION_REQUIRED`
        - 디폴트 속성
        - 현재 트랜잭션 그대로 사용 / 현재 트랜잭션 없으면 새로 만듬
      - `PROPAGATION_REQUIRES_NEW`
        - 새 트랜잭션 생성 / 현재 태랜잭션 있으면 중지시킴
- c.f) Transaction
- c.f) `PlatformTransactionManager`
- c.f) `ReactiveTransactionManager`
  - 개요
    - 같은 리액티브 파이프라인속에서 같은 리액터 컨텍스트 내부에서 데이터 접근이 실행되어야 만 함
