# Servlet

- 의문
- Web Server vs Web Application Server vs Web Application vs Web Framework
- 개요

## 의문

## Web Server vs Web Application Server vs Web Application vs Web Framework

- WS(Web Server)
  - 개요
    - 정적인 웹 리소스(이미지, html, css, js 등)를 서빙하기 위한 서버
      - 동적인 웹 리소스는 다룰 수 없어서 WAS로 요청을 포워딩한다
  - 예시
    - Nginx, Apache
- WAS(Web Application Server)
  - 개요
    - 동적인 웹 리소스를 서빙하기 위한 서버
      - WS로부터 포워딩된 요청을 받아서 동적으로 response를 구성하여 돌려준다
  - 예시
    - WSGI 구현체(gunicorn), Servlet container 구현체(Tomcat)
- WA(Web Application)
  - 개요
    - WAS 내부에서 커넥션과 request-response로 이어지는 라이프사이클을 제외한 비즈니스로직을 담당하는 애플리케이션
  - 예시
    - Spring Web Application, Node Web Application
- WF(Web Framework)
  - 개요
    - WA를 쉽게 만들기 위해서, 만들어진 웹 프레임 워크
  - 예시
    - Spring, Express, Flask, Sanic, Ktor, Gin
  - C.f) Spring boot는 tomcat, jetty등을 내장하여 stand-alone으로 동작

## 개요

Servlet 명세를 구현한 WA의 예시

```java
import java.io.IOException;

import jakarta.servlet.ServletConfig;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

public class ServletLifeCycleExample extends HttpServlet {
    private Integer sharedCounter;

    @Override
    public void init(final ServletConfig config) throws ServletException {
        super.init(config);
        getServletContext().log("init() called");
        sharedCounter = 0;
    }

    @Override
    protected void service(final HttpServletRequest request, final HttpServletResponse response) throws ServletException, IOException {
        getServletContext().log("service() called");
        int localCounter;
        synchronized (sharedCounter) {
            sharedCounter++;
            localCounter = sharedCounter;
        }
        response.getWriter().write("Incrementing the count to " + localCounter);  // accessing a local variable
    }

    @Override
    public void destroy() {
        getServletContext().log("destroy() called");
    }
}
```

- 개요
  - 자바를 사용하여 서버의 다양한 리퀘스트를 응답할 수 있게 하는 서버측 프로그램 혹은 그 사양(주로 웹)
    - WSGI, PSGI
- 특징
  - Jakarta Servlet API를 준수하는 자바 클래스를 저장하고 가공함
- web container
  - 개요
    - servlet과 상호작용하는 웹 서버의 컴포넌트
      - wsgi호환이 가능한 WAS 같은 느낌
  - 역할
    - servlet의 lifecycle를 관리
    - URL을 특정 servlet과 매핑
    - URL requester가 액세스 권한이 있는지 확인
- `Servlet`
  - 개요
    - request를 받고, 해당 request기반으로 response를 생성하는 하나의 오브젝트
      - `javax.servlet.Servlet`인터페이스의 구현체
        - 라이프 사이클 메서드
          - `init(ServletConfig config)`
          - `service(ServletRequest req, ServletResponse res)`
          - `destroy()`
        - `getServletConfig()`
        - `getServletInfo()`
  - 라이프 사이클
    - 웹 컨테이너가 `init()`메서드를 호출하여 서블릿 인스턴스를 이니셜라이제이션함
      - 라이프사이클 안에서 오직 한 번만 호출됨
    - 웹 컨테이너가 각 리퀘스트마다 각각의 스레드에서 `service()`메서드를 호출함
      - `service()`메서드는 리퀘스트의 종류를 정하고, 그 리퀘스트를 다루기에 적절한 메서드로 dispatch함
      - 개발자는 이러한 메서드들을 구현해둬야 함
    - 웹 컨테이너는 `destroy()`메서드를 호출하여 그 servlet을 더이상 사용하지 못하게 함
      - 라이프사이클 안에서 오직 한 번만 호출됨
