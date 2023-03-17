# Kotlin spring

- 의문
- 개요
- Gradle 설정

## 의문

## 개요

## Gradle 설정

build.gradle.kts

```kotlin
import org.jetbrains.kotlin.gradle.tasks.KotlinCompile

plugins {
  id("org.springframework.boot") version "3.0.1"
  id("io.spring.dependency-management") version "1.1.0"
  // org.jetbrains.kotlin에서 제공하는 jvm 플러그인을 resolve하고 apply도 함
  kotlin("jvm") version "1.8.0"
  // Spring 애노테이션으로 meta-annotated 혹은 annotated된 메서드나 클래스를 자동으로 open해주는 플러그인
  kotlin("plugin.spring") version "1.8.0"
  // JPA에서 non-nullable properties를 사용할 수 있게 하기 위함
  // @Entity, @MappedSuperclass, @Embeddable로 애노테이션 된 클래스의 no-arg constructors를 생성함
  // 이는 궁극적으로 java reflection으로 오브젝트를 생성하기 위함
  kotlin("plugin.jpa") version "1.8.0"
}

// Lazy fetch등이 원하는 대로 동작할 수 있도록
allOpen {
	annotation("jakarta.persistence.Entity")
	annotation("jakarta.persistence.Embeddable")
	annotation("jakarta.persistence.MappedSuperclass")
}
```
