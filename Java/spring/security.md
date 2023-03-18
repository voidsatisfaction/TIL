# Spring Security

- 의문
- Servlet 개요
  - DelegatingFilterProxy
  - FilterChainProxy
  - SecurityFilterChain
  - Security Exception Handling
- Authentication
  - SecurityContextHolder
  - Authentication
  - GrantedAuthority
  - AuthenticationManager
  - ProviderManager
  - AuthenticationProvider
  - Request Credentials with AuthenticationEntryPoint

## 의문

## Servlet 개요

Servlet filter chain

![](./images/security/filter_chain1.png)

필터 코드 예시

```kotlin
fun doFilter(request: ServletRequest, response: ServletResponse, chain: FilterChain) {
    // do something before the rest of the application
    chain.doFilter(request, response) // invoke the rest of the application
    // do something after the rest of the application
}
```

- 개요
  - Servlet Filter Chain 기반

### DelegatingFilterProxy

DelegatingFilterProxy의 구조

![](./images/security/DelegatingFilterProxy1.png)

DelegatingFilterProxy 코드 예시

```kotlin
fun doFilter(request: ServletRequest, response: ServletResponse, chain: FilterChain) {
	// Lazily get Filter that was registered as a Spring Bean
	// For the example in DelegatingFilterProxy delegate is an instance of Bean Filter0
	val delegate: Filter = getFilterBean(someBeanName)
	// delegate work to the Spring Bean
	delegate.doFilter(request, response)
}
```

- 개요
  - Servlet컨테이너의 라이프 사이클과 Spring의 `ApplicationContext`를 이어주는 브릿지 필터
    - 기존 Servlet 컨테이너는 Spring-defined Bean은 알지 못하나, `DelegatingFilterProxy`를 등록하면, 모든 일을 `Filter`를 구현하는 Spring Bean으로 delegate할 수 있음
    - Filter bean 인스턴스의 look up을 딜레이해서, Spring Bean이 전부 initialize되기 전에 미리 servlet 필터로 등록 가능

### FilterChainProxy

FilterChainProxy의 구조

![](./images/security/FilterChainProxy1.png)

- 개요
  - 특수한 `Filter`로 `SecurityFilterChain`을 통해서 많은 `Filter`인스턴스를 delegating가능
    - `FilterChainProxy`자체는 Bean이므로, `DelegatingFilterProxy`로 래핑되어있음

### SecurityFilterChain

SecurityFilterChain의 구조

![](./images/security/SecurityFilterChain1.png)

Multiple SecurityFilterChain의 구조

![](./images/security/MultipleSecurityFilterChain1.png)

- 개요
  - `SecurityFilterChain`은 `FilterChainProxy`가 어떤 Spring Security `Filter`인스턴스들을 현재 리퀘스트에서 호출해야하는지 정하는데에 사용됨
    - `SecurityFilterChain`에 있는 `Securiy Filters`는 일반적으로 Bean이나, `FilterChainProxy`에 등록됨
  - **url기반으로 어떤 SecurityFilterChain을 적용할 것인지도 설정 가능**
- 특징
  - 디버깅 포인트를 `FilterChainProxy`로 지정하면, 쉽게 디버그 할 수 있음
  - `Filter`는 특정 URL에만 기반해서 호출되나, `FilterChainProxy`는 `HttpServletRequest`의 어떤것이든 기반해서 호출 가능
  - Multiple SecurityFilterChain도 가능함
    - `FilterChainProxy`가 어떤 `SecurityFilterChain`을 호출해야하는지 결정함
  - 자체적으로 제공하는 Security Filter가 존재함
    - e.g)
      - `CorsFilter`
      - `CsrfFilter`
      - `BearerTokenAuthenticationFilter`

### Security Exception Handling

Security Exception Handling 구조

![](./images/security/SecurityExceptionHandling1.png)

위 구조의 대략적인 코드 구성

```java
try {
	filterChain.doFilter(request, response);
} catch (AccessDeniedException | AuthenticationException ex) {
	if (!authenticated || ex instanceof AuthenticationException) {
		startAuthentication();
	} else {
		accessDenied();
	}
}
```

- 개요
  - `ExceptionTranslationFilter`는 `AccessDeniedException`과 `AuthenticationException`을 HTTP response로 변환함
    - `ExceptionTranslationFilter`는 `FilterChainProxy`에 `Security Filters`중 하나로 등록됨

## Authentication

- URL차이에 따라 서로 다른 SecurityFilterChain을 적용하고
- 각 SecurityFilterChain은 AbstractAuthenticationProcessingFilter를 각각 갖으며, 해당 Filter는 Authentication을 생성해서 AuthenticationManager로 해당 Authentication인스턴스를 넘겨준다.
- AuthenticationManager는 받은 Authentication을 기반으로 인증
  - ProviderManager를 사용할 경우, 미리 주입된 AuthenticationProvider들을 기반으로 인증 진행
  - *그럼, AbstractAuthenticationProcessingFilter에서 AbstractAuthenticationProcessingFilter의 서브클래스에 따라서 Authentication을 생성한다는 것은 AuthenticationProvider와는 별개인건가?*

Authentication architecture

![](./images/security/authentication_architecture1.png)

1. 유저가 credentials를 제출하면, `AbstractAuthenticationProcessingFilter`는 `Authentication`을 `HttpServletRequest`로부터 생성함(`Authentication`의 타입은 `AbstractAuthenticationProcessingFilter`의 서브클래스에 따라 다름 - `UsernamePasswo rdAuthenticationFilter`는 `UsernamePasswordAuthenticationToken`을 생성)
2. `Authentication`이 `AuthenticationManager`로 넘겨짐
3. authentication이 실패하면, failure
  - SecurityContextHolder가 clear out됨
  - `RememberMeService.loginFail()`가 호출되며, 설정하지 않았으면 아무것도 안함
  - `AuthenticationFailureHandle`가 호출됨
4. authentication이 성공하면, success
  - `SessionAuthenticationStrategy`가 새 로그인 이벤트를 받음
  - `SecurityContextHolder`에 `Authentication`이 세팅됨
    - `SecurityContextPersistenceFilter`가 `SecurityContext`를 `HttpSession`에 저장
  - `RememberMeService.loginSuccess`가 호출됨
  - `ApplicationEventPublisher`에서 `InteractiveAuthenticationSuccessEvent`를 publish함
  - `AuthenticationSuccessHandler`를 호출

---

- `SecurityContextHolder`
  - authenticated된 사람에 대한 정보를 저장하는 곳
- `SecurityContext`
  - 현재 authenticated된 유저의 `Authentication`을 갖고 있으며, `SecurityContextHolder`로부터 얻을 수 있음
- `Authentication`
  - `AuthenticationManager`에 인증하기 위한 자격을 입력값으로 보내주거나, `SecurityContext`에서 현재 사용자를 제공하기 위함 `AuthenticationManager`에 대한 입력이 될 수 있음
- `GrantedAuthority`
  - `Authentication`주체에 대해서 부여된 권한
- `AuthenticationManager`
  - Spring Security의 필터들이 authentication을 어떻게 할것인가를 정의한 API
- `ProviderManager`
  - `AuthenticationManager`의 가장 일반적인 구현
- `AuthenticationProvider`
  - `ProviderManager`에 의해서 특정 타입의 인증을 실행하기 위해서 사용됨
- `RequestCrednetials with AuthenticationEntryPoint`
  - 클라이언트로부터 credential을 요청하기 위해서 사용됨
    - e.g) 로그인 페이지로 리다이렉트, `WWW-Authenticate` response를 반환하는 등
- `AbstractAuthenticationProcessingFilter`
  - 인증을 위해서 사용되는 기본 `Filter`

### SecurityContextHolder

SecurityContextHolder의 구조

![](./images/security/SecurityContextHolder1.png)

- 특징
  - default는 `ThreadLocal`을 사용
    - 매 리퀘스트가 끝날때마다 `FilterChainProxy`가 `SecurityContext`가 언제나 clear되도록 해줌
    - `MODE_GLOBAL`, `MODE_INHERITABLETHREADLOCAL`, `MODE_THREADLOCAL(default)`등이 있음

### Authentication

- 개요
  - 두가지 목적
    - `AuthenticationManager`의 input으로, 주어진 credentials로 authenticate를 진행
      - 이 시나리오로 진행될경우, `isAuthenticated()`는 false를 반환
    - 현재 authenticated된 user를 반환
  - 포함되는 오브젝트
    - `principal`
      - 유저가 누군지를 식별
      - username/password를 사용하여 인증할 경우, 일반적으로 `UserDetails`의 인스턴스가 됨
    - `credentials`
      - 주로 password인 경우가 많음
    - `authorities`
      - 유저가 받은 하이레벨 권한이며, `GrantedAuthority`의 인스턴스
      - e.g)
        - roles, scopes

### GrantedAuthority

- 개요
  - principal이 부여받은 어플리케이션 레벨의 허가인스턴스
    - roles, scopes
  - `Authentication.getAuthorities()`로 참조 가능
- 특징
  - username/password 기반 인증을 사용할 경우, `GrantedAuthority`인스턴스는 `UserDetailsService`가 가져옴

### AuthenticationManager

- 개요
  - Spring Security의 필터들이 어떻게 authentication을 진행할지를 정의하는 API 인터페이스
    - Authentication을 생성함

### ProviderManager

ProviderManager의 구조

![](./images/security/ProviderManager1.png)

여러개의 SecurityFilterChain이 있고 공통 authentication이 존재하는 경우

![](./images/security/ProviderManager2.png)

- 개요
  - `AuthenticationManager`의 가장 일반적인 구현체
    - `List<AuthenticationProvider>`에 위임함
- 특징
  - 각 `AuthenticationProvider`는 authentication이 successful, fail, cannot decide인지 나타낼 수 있음
    - 만약, 어떤 `AuthenticationProvider`도 authenticate할 수 없으면, `ProviderNotFoundException`이 발생함
  - 각 `AuthenticationProvider`는 특정 타입의 authentification을 어떻게 수행하는지를 알고 있음
    - e.g) username/password전용 `AuthenticationProvider` 혹은 SAML전용 등
  - `Authentication`오브젝트의 sensitive credential 정보를 제거함
    - 캐시를 사용할때에는 `eraseCredentialsAfterAuthentication`을 disable해야 함

### AuthenticationProvider

- 개요
  - `ProviderManager`에 여러개의 `AuthenticationProvider`인스턴스를 주입하여, 각 `AuthenticationProvider`가 특정 타입의 인증을 진행
    - e.g)
      - `JwtAuthenticationProvider`는 JWT token인증을 지원

### Request Credentials with AuthenticationEntryPoint

- 개요
  - client에서 credential을 먼저 포함해서 요청하는 경우, Spring Security가 request credential을 하는 response를 돌려줄 필요가 없음
  - 그러나, client가 unauthenticated request를 보내는 경우, `AuthenticationEntryPoint`를 써서, login page로 redirect를 하곤 함
