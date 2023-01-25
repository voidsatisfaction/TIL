# Spring event

- 의문
- 개요
  - 구현 방법
- `@Async`

## 의문

## 개요

- 개요
  - event pulishing은 `ApplicationContext`가 제공하는 기능이며, 이벤트 드리븐으로 스프링애플리케이션을 개발할 수 있게 함
- 특징
  - `ApplicationContext`자체적으로 발행하는 이벤트도 있음
    - `ContextRefreshedEvent`
    - `ContextStartedEvevnt`
    - `RequestHandledEvent`
  - 따로 `ApplicationListener` 인터페이스를 구현한 빈을 만들지 않아도, 기존의 빈의 public method를 리스너로 만들 수 있음(`@EventListener`)
    - `@Async` 애노테이션을 사용하면, 비동기로 쉽게 만들 수 있음
  - publisher
    - 만약 `@EventListener`로 어노테이션된 메서드가 반환값이 있으면, 그 반환값이 새 이벤트로 발행됨, 컬렉션이 반환값이면 여러개의 새 이벤트가 발행될 수 있음
  - transaction bound event
    - transaction phase에 바인딩할 수 있는 리스너를 생성할 수 있음
      - `AFTER_COMMIT`
        - 트랜잭션이 성공적으로 커밋되면 호출됨
      - `AFTER_ROLLBACK`
        - 트랜잭션이 롤백되면 호출됨
      - `AFTER_COMPLETION`
        - 트랜잭션이 COMMIT or ROLLBACK되면 호출됨
      - `BEFORE_COMMIT`
        - 트랜잭션이 커밋하기 전에 호출됨
    - 트랜잭션이 존재하고, 그 트랜잭션 안에서 event producer가 동작하고, 커밋되려고 할때에만 transaction listener가 호출됨
      - `fallbackExecution` 속성을 `true`로 설정해야지만 트랜잭션이 없어도 동작함

### 구현 방법

```java
// AsyncTaskExecutor
@Configuration
public class AsynchronousSpringEventsConfig {
    @Bean(name = "applicationEventMulticaster")
    public ApplicationEventMulticaster simpleApplicationEventMulticaster() {
        simpleApplicationEventMulticaster eventMulticaster = new SimpleApplicationEventMulticaster();

        eventMulticaster.setTaskExecutor(new SimpleAsyncTaskExecutor());
        return eventMulticaster
    }
}

// Event
public class CustomSpringEvent {
    private String message;

    public CustomSpringEvent(Object source, String message) {
        super(source);
        this.message = message;
    }

    public String getMessage() {
      return message;
    }
}

// Publisher
@Component
public class CustomSpringPublisher {
    @Autowired
    private ApplicationEventPublisher applicationEventPublisher;

    public void publishCustomEvent(final String message) {
        System.out.println("Publishing custom event. ");
        CustomSpringEvent customSpringEvent = new CustomSpringEvent(this, message);
        applicationEventPublisher.publishEvent(customSpringEvent);
    }
}

// Listener
@Component
public class CustomSpringEventListener implements ApplicationListener<CustomSpringEvent> {
    @Override
    public void onApplicationEvent(CustomSpringEvent event) {
        System.out.println("Received spring custom event - " + event.getMessage());
    }
}

@Component
public class AnnotationDrivenEventListener {
    @EventListener
    public void handleContextStart(ContextStartedEvent cse) {
        System.out.println("Handling context started event.");
    }
}

@TransactionalEventListener(phase = TransactionPhase.BEFORE_COMMIT)
public void handleCustom(CustomSpringEvent event) {
    System.out.println("Handling event inside a transaction BEFORE COMMIT.");
}
```

## `@Async`

```java
@Async
public Future<String> asyncMethodWithReturnType() {
    System.out.println("Execute method asynchronously - "
      + Thread.currentThread().getName());
    try {
        Thread.sleep(5000);
        return new AsyncResult<String>("hello world !!!!");
    } catch (InterruptedException e) {
        //
    }

    return null;
}
```

- 개요
  - `@Async` 애노테이션을 빈의 메서드에 붙이면, 호출시 다른 스레드에서 실행되며, caller method는 기다리지 않음
- 특징
  - public method에만 적용 가능
    - proxied되기 위함
  - 같은 클래스에서 `async` 메서드를 호출하면 동작하지 않음
    - 같은 클래스에서 호출할경우, proxy를 바이패스하고, method를 직접 호출함

### configuration

```java
// override executor at method level
@Configuration
@EnableAsync
public class SpringAsyncConfig {
    @Bean(name = "threadPoolTaskExecutor")
    public Executor threadPoolTaskExecutor() {
        return new ThreadPoolTaskExecutor();
    }
}

// override executor at application level
//// default (@Async)
@Configuration
@EnableAsync
public class SpringAsyncConfig implements AsyncConfigurer {
   @Override
    public Executor getAsyncExecutor() {
        ThreadPoolTaskExecutor threadPoolTaskExecutor = new ThreadPoolTaskExecutor();
        threadPoolTaskExecutor.initialize();
        return threadPoolTaskExecutor;
    }

    @Override
    public void handleUncaughtException(
      Throwable throwable, Method method, Object... obj) {

        System.out.println("Exception message - " + throwable.getMessage());
        System.out.println("Method name - " + method.getName());
        for (Object param : obj) {
            System.out.println("Parameter value - " + param);
        }
    }
}
```
