# 자바 애플리케이션 배포

- 의문
- 개요
  - JAR(Java ARchive)
  - WAR(Web application ARchive)
  - APK(Android Application Package)

## 의문

## 개요

### JAR(Java ARchive)

- 개요
  - 자바 플랫폼에 애플리케이션이나 라이브러리를 배포하기 위한 패키지 파일 포맷
- 구성
    - 자바 클래스 파일
    - 클래스들이 이용하는 관련 리소스(텍스트 그림 등)
    - 매니페스트 파일(`MANIFEST.MF`)
      - 메타정보 포함
        - 확장 정보
        - 패키지 관련 데이터
        - 애플리케이션의 메인 클래스 이름
- 원리
  - ZIP 파일 포맷
    - JDK의 jar명령어로 파일을 만들고 압출 풀기 가능
      - `jar -xf foo.jar`
- 특징
  - 실행 가능(매니페스트 파일에 `Main-Class: myPrograms.MyClass` 형식으로 기술되어야 함)
  - 난독화 가능
  - 디지털 서명 가능(보안)

### WAR(Web application ARchive)

- 개요
  - 자바서버 페이지, 자바 서블릿, 자바 클래스, 그 외의 파일, 라이브러리, HTML 템플릿 자원과 같은 웹 애플리케이션 배포를 위한 파일들을 한데 모아 배포하는데 사용되는 JAR파일의 컬렉션

### APK(Android Application Package)

- 개요
  - 안드로이드 애플리케이션에서 사용되는 자바 압축 포맷
