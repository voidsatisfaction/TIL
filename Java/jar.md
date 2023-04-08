# JAR 파일

- 의문
- 개요
- 특징
- Spring boot executable jar 구조
  - 개요

## 의문

## 개요

- java class file과 관련 메타데이터와 리소스(text, images 등)파일들을 하나의 파일로 배포하기위해서 모아두는데에 사용되는 패키지 파일 포맷
  - zip으로 압축됨

## 특징

- executable JAR 파일의 경우, 매니페스트에 `Main-Class: myPrograms.MyClass`와 같은 엔트리포인트 클래스와 클래스 패스를 명시함
  - *클래스 패스와 java 코드의 패키지 선언과의 차이는 무엇일까?*

## Spring boot executable jar 구조

### 개요

- 기본적으로 nested jar이지만, nested jar에 대한 java의 표준이 없기 때문에 spring boot만의 구조를 따름

Spring boot application의 MANIFEST.MF 예시

```
Manifest-Version: 1.0
Main-Class: org.springframework.boot.loader.JarLauncher
Start-Class: org.maysnow.gratitude.diary.ApplicationKt
Spring-Boot-Version: 3.0.4
Spring-Boot-Classes: BOOT-INF/classes/
Spring-Boot-Lib: BOOT-INF/lib/
Spring-Boot-Classpath-Index: BOOT-INF/classpath.idx
Spring-Boot-Layers-Index: BOOT-INF/layers.idx
Build-Jdk-Spec: 17
Implementation-Title: gratitude-diary
Implementation-Version: 0.0.1
```

- `META-INF`
  - `MANIFEST.MF`
    - 패키지 관련 데이터를 정의하는 파일이며, name-value 페어
    - `Main-Class`는 `public static void main(String[] args)`메서드를 갖는 클래스
- `BOOT-INF`
  - `classpath.idx`
    - classpath에 추가되어야 하는 jar이름의 리스트를 제공
  - `layers.idx`
    - Docker/OCI 이미지를 만들때 사용되는 레이어를 순서대로 나열
  - `classes`
    - `mycompany`
      - `project`
        - `YourClasses.class`
  - `lib`
    - `dependency1.jar`
    - `dependency2.jar`
- `org`
  - `springframework`
    - `boot`
      - `loader`
        - `<spring boot loader classes>`
