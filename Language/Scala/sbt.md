## Build definition

`build.sbt`의 빌드 정의에 대해서 확인

### sbt버전 특정하기

- 빌드 정의(build definition)
  - sbt의 버전 지정
    - 서로 다른 버저의 sbt런처가 같은 프로젝트를 동일하게 만들도록 함
    - `project/ build.properties`에서 값 수정
    - 파일이 없으면 sbt런처가 알아서 지정해줌
  - 빌드 정의란?
    - `build.sbt`파일에 정의된 빌드 정의. 프로젝트(서브 프로젝트)들의 집합으로 구성
    - 현재의 디렉터리(베이스 디렉터리)에서의 서브 프로젝트를 나타냄
    - 각각의 서브 프로젝트들은 `키-값`페어로 설정됨
  - 키들
    - 타입
      - 설정 키: 값이 한번만 계산되는 키
      - 태스크 키: 태스크라고 불리는 어떠한 값에 대한 키. 매번 새로 계산되며 부작용이 존재
      - 입력 키: 커맨드라인 인자를 입력값으로 받는 태스크에 대한 키
  - 라이브러리 의존을 추가
    - 방법
      - 1 `jars`를 `lib/`에 둠(관리되지 않음)
      - 2 관리되는 의존을 추가(build.sbt)

```scala
val derby = "org.apache.derby" % "derby" % "10.4.1.3" // 추가되는 라이브러리

lazy val commonSettings = Seq(
  organization := "com.example",
  version := "0.1.0-SNAPSHOT",
  scalaVersion := "2.12.4"
)

lazy val root = (project in file("."))
  .settings(
    commonSettings,
    name := "Hello",
    libraryDependencies += derby
  )
```
