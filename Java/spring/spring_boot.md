# Spring Boot

- 의문
- 개요

## 의문

- `@Repository`, `@Service`, `@Controller`는 Web에서 주로 사용되는데, `@Component`는 어떤 경우에 사용되는가?
  - `@Component`는 위의 경우 이외의 경우에 사용되나, Meta Annotation으로 구현해서 사용하는게 바람직
- `@Controller`, `@RestController`
  - `@RestController` = `@Controller` + `@ResponseBody`

## 개요

- 개요
  - 스프링을 손쉽게 쓰기 위해 제공해주는 툴
  - c.f) 스프링
    - 자바 엔터프라이즈 애플리케이션 개발을 편리하게 하기위해 개발된 툴
- 스프링 부트가 다루는 영역
  - 애플리케이션 개발 관련 거의 모든 영역
    - 빌드
      - 프로젝트 생성
      - 의존성 관리
      - 애플리케이션 패키징 및 실행
    - 코딩
      - 개발 툴 제공
      - 자동 설정(Auto-Configuration)
      - 외부 설정
    - 배포 및 관리
      - 내장 컨테이너(톰켓, 제티, 언더토우)
      - 도커 이미지 생성
      - Actuator
      - 스프링 부트 어드민

### 스프링 부트 빌드

- 스프링 부트 버전
  - GA
    - stable버전
  - M4
    - 배포는 됐는데, 아직 stable은 아님
  - SNAPSHOT
    - 개발중
- 프로젝트 메타데이터
  - group, artifact, version의 조합으로 구분 가능
- 스프링 부트에서 알아서 특정 라이브러리의 적절한 버전을 지정 가능(`dependency-management`)

### 애플리케이션 실행

빌드: 애플리케이션 실행

![](./images/spring_boot/build_application_execution1.png)

- `gradlew`
- main 클래스 실행
- JAR 패키징 & java -jar
  - JAR 패키징
    - `gradle bootjar`
      - build 폴더가 생김
  - 실행(예시)
    - `java -jar demo-0.0.1-SNAPSHOT.jar`

### 자동 설정

코딩 자동 설정

![](./images/spring_boot/auto_configuration1.png)

- 만약 애플리케이션 빈과 자동 설정으로 제공하는 빈의 id가 중복되면, 빌드가 안되도록 막혀있음
  - 풀어줄 순 있다

### 외부 설정 파일

![](./images/spring_boot/properties1.png)

- 개요
  - 코드에서 값을 밖으로 꺼내는 방법 제공
- 구체적이고 가까운 위치에 있는 설정의 우선 순위가 높음
  - 구체적
    - config라는 디렉터리에 들어있는 설정인지 아닌지
  - 가까운
    - JAR파일 안보다는 커맨드라인 or 파일 시스템에 있는 application properties가 가까움
      - 대신 여기에서는 current working directory랑도 싱크가 맞아야 함(실행하는 working directory에 있는 application.properties)

### 배포
