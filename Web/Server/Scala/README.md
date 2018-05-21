# 스칼라 웹 애플리케이션 서버

- http://mangkyu.tistory.com/14

## Servlet(애플리케이션)이란?

- 클라이언트 요청을 처리하고 그 결과를 다시 클라이언트에게 전송
- `Servlet`클래스의 구현 규칙을 지킨 자바 프로그램
- 결국 Servlet이라는 것도 하나의 프로토콜
- 자바 소스 코드 안에 HTML소스 코드를 삽입
  - `out`객체의 `println()`메서드를 사용해서 구현
  - 직접 작업하기엔 버거움

## Servlet 컨테이너란

- HTTP요청을 받아서 Servlet을 실행하고 그 결과를 사용자 브라우저에 전달해주는 기능을 제공하는 컴포넌트
- 기능
  - Servlet실행
    - 프로세스 기반이 아닌, 스레드 기반(효율 높음)
  - 라이프사이클 관리
  - Servlet과 웹 서버가 서버 통신할 수 있는 방법을 제공함
  - 웹 서버 자체는 Servlet자체를 실행할 수 없으므로, JVM을 내장한 컨테이너인 서블릿 컨테이너가 실행환경이 되어줌(Servlet과 웹 서버를 소켓 기술로 이어줌)
- 예시
  - Tomcat
    - 자체 웹 서버도 내장함

## JSP(Java Server Pages)

- HTML안에 Java코드를 넣게 하여, 웹 서버에서 동적으로 웹 페이지를 생성하여 클라이언트에게 돌려주는 기술
- 뷰를 담당

```java
// jsp파일
<%@ page contentType="text/html;charset=UTF-8" language="java" %> <% String name = "Yongho"; %> <html> <head> <title>${name}</title> </head> <body> <h1>Hello world!</h1> <p>My name is ${name}</p> </body> </html>

출처: http://yongho1037.tistory.com/691 [게임 서버 개발 노트]
```

```java
// .class파일
public final class index_jsp extends org.apache.jasper.runtime.HttpJspBase implements org.apache.jasper.runtime.JspSourceDependent { ... 생략 ...

public void _jspService(final javax.servlet.http.HttpServletRequest request, final javax.servlet.http.HttpServletResponse response)
  throws java.io.IOException, javax.servlet.ServletException {
    final javax.servlet.jsp.PageContext pageContext; javax.servlet.http.HttpSession session = null; final javax.servlet.ServletContext application; final javax.servlet.ServletConfig config; javax.servlet.jsp.JspWriter out = null; final java.lang.Object page = this; javax.servlet.jsp.JspWriter _jspx_out = null; javax.servlet.jsp.PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html;charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response, null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;

      out.write('\r');
      out.write('\n');

      String name = "Yongho";

      out.write("\r\n");
      out.write("<html>\r\n");
      out.write("<head>\r\n");
      out.write(" <title>");
      out.write((java.lang.String)

      org.apache.jasper.runtime.PageContextImpl.proprietaryEvaluate("${name}", java.lang.String.class, (javax.servlet.jsp.PageContext)_jspx_page_context, null, false));
      out.write("</title>\r\n");
      out.write("</head>\r\n");
      out.write("<body>\r\n");
      out.write("<h1>Hello world!</h1>\r\n");
      out.write("<p>My name is ");
      out.write((java.lang.String) org.apache.jasper.runtime.PageContextImpl.proprietaryEvaluate("${name}", java.lang.String.class, (javax.servlet.jsp.PageContext)_jspx_page_context, null, false));
      out.write("</p>\r\n");
      out.write("</body>\r\n");
      out.write("</html>\r\n");
    } catch (java.lang.Throwable t) {
      if (!(t instanceof javax.servlet.jsp.SkipPageException)){ out = _jspx_out; if (out != null && out.getBufferSize() != 0) try {
        if (response.isCommitted()) {
          out.flush();
        } else {
          out.clearBuffer();
        }
      } catch (java.io.IOException e) {} if (_jspx_page_context != null) _jspx_page_context.handlePageException(t); else throw new ServletException(t); } } finally { _jspxFactory.releasePageContext(_jspx_page_context); } } }

```
