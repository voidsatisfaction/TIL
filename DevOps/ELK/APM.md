# Elastic APM

- 의문
- Elastic APM
- 데이터 모델
  - Transaction
  - Span
  - Error
  - Metric
  - Metadata
- APM java agent

## 의문

## Elastic APM(Application Performance Monitoring)

Elastic APM 아키텍처

![](./images/APM/architecture1.png)

- 개요
  - 애플리케이션에 대한 성능정보 및 발생한 에러정보 그리고 애플리케이션이 동작중인 서버의 기본적인 메트릭 정보를 수집할 수 있는 기능 지원
- 아키텍처 구성
  - APM Agent
    - 개요
      - 실시간으로 퍼포먼스 및 에러 데이터를 수집하여 APM 서버로 전달
      - APM 서버 연동 실패시 데이터 저장을 위한 메모리 버퍼 존재
    - 종류
      - Go, JAVA, .NET, Nodejs, Python, Ruby, JavaScript RUM(Real User Monitoring)
  - APM Server
    - 개요
      - 에이전트에서 수집된 데이터에 대한 유효성 체크
      - 수집된 데이터를 Elasticsearch의 도큐먼트 포맷으로 전환
  - Elasticsearch
    - 개요
      - APM 데이터에 대한 저장, 검색, 분석을 지원
      - 성능 데이터에 대한 집계 기능 제공
  - Kibana
    - 개요
      - APM UI에서 데이터 필터링 및 Service, Trace, Transaction, Error, Metric에 대한 개요 및 상세 기능 제공
      - 데이터 가시화
- 동작 방식
  - APM agent가 transaction으로 묶인 span들을 기록함
  - transaction과 span을 APM 서버로 보냄
  - elasticsearch가 사용 가능한 형태로 데이터가 변환된 후 elastic search에 저장
  - kibana에서 대시보드로 보기

## 데이터 모델

![](./images/APM/distributed_tracing1.png)

- Transaction
- Span
- Error
- Metric
- Metadata

### Transaction

- 개요
  - 애플리케이션내에서 측정되는 최상위 작업이자 span
    - 서버의 리퀘스트, 배치잡, 백그라운드 잡, 커스텀 트랜잭션 등
- 특징
  - 에이전트가 트랜잭션을 샘플링할지 말지 결정 가능
    - 트랜잭션의 span들이 보내질 수도 있고 아닐 수 있음
  - UI에서 `type`과 `name`으로 그룹화 됨
    - `type`
      - `request`, `backgroundjob`
    - `name`
      - `GET /users/:id`, `UsersController#show`
- 구성
  - `Event Timestamp`
  - `유니크 ID, type, name`
  - `Event`가 생성된 환경에 대한 데이터
    - service
      - environment, framework, language
    - host
      - architecture, hostname, IP, etc
    - Process
      - args, PID, PPID
    - URL
      - full, domain, port, query
    - User
      - email, ID, username

### Span

- 개요
  - 실행을 추적하기 위한 논리적 작업 단위
  - 실행되는 코드(어떤 한 행위)의 시작 및 소요시간 정보가 존재
  - span 사이의 부모/자식 관계를 가질 수 있음
- 구성
  - transaction.id
  - parent.id
  - start time, duration
  - name, type, stacktrace
- dropped spans
  - 성능상의 이유로 특정 span을 드롭 가능
- missing spans
  - 트랜잭션과는 별개로 APM 서버로 span을 스트리밍하기 때문에, 몇몇 span은 사라질 수 있음
    - 사라진 것들은 디스플레이에 나타내 줌

### Error

- 개요
  - 애플리케이션에서 발생한 에러나 익셉션의 정보 및 로그
- 구성
  - 에러 발생 위치
  - 스택트레이스 정보
    - 에러 익셉션
    - 에러 로그
  - transactiono.id
  - error 이벤트가 생성된 환경에 대한 데이터
    - server
      - environment, framework, language
    - host
      - architecture, hostname, IP, etc
    - Process
      - args, PID, PPID
    - URL
      - full, domain, port, query
    - User
      - email, ID, username

### Metric

- 개요
  - 에이전트 호스트에 대한 CPU, memory등의 기본 메트릭 정보를 자동으로 수집
  - 자바의 JVM Metric이나 Go의 런타임 메트릭 수집 가능
- 종류
  - System metrics
    - 기본 인프라, 애플리케이션 메트릭
  - Calculated metrics
    - 결합된 trace이벤트 메트릭

### Metadata

- 개요
  - 이벤트에 대한 부가적인정보
- 종류
  - Label
    - transaction, span, error에 인덱스화된 정보를 더함
      - 검색 가능해짐 / 취합 가능해짐
      - 대시보드 만들 수 있음
  - Custom context
    - transaction, span, error에 인덱스화되지 않은 정보를 더함
  - User context
    - transaction, span, error에 인덱스화된 유저 정보를 더함

## APM JAVA Agent

### 개요

- 개요
  - 애플리케이션의 퍼포먼스를 자동으로 측정하고, 에러를 트래킹함
- 특징
  - 클래스의 바이트코드를 조절
    - 따라서, 기존 코드의 수정이 필요 없음

### 설치

- 방식
  - manual
    - `-javaagent` JVM옵션으로 설정
    - 코드 변경이 필요 없음
  - automatic
    - `apm-agent-attach-cli.jar`을 사용함
    - JVM 옵션 설정도 필요 없음
  - programmatic
    - 코드 추가 + `apm-agent-attach` 의존성 추가
    - JVM 옵션 설정 필요 없음
    - agent가 패키징된 애플리케이션 바이너리에 추가됨

### manual

1. APM Agent jar 파일 다운로드
2. 애플리케이션 실행시, -javaagent 옵션을 설정하여 APM Agent 설치

```sh
# 설치 및 jar 실행 예시
java -javaagent:<download>/<path>/elastic-apm-agent.jar
		-Delastic.apm.server_urls="http://<< kubernetes node ip >>:30082"
		-Delastic.apm.service_name=demoappjava-es
		-Delastic.apm.environment=dev
		-Delastic.apm.application_packages=com.example
	 -jar demoappjava.jar
```

- `application_packages`
  - stack trace frame이 in-app frame인지, library frame인지 구분하기 위함
  - 루트 패키지를 설정하면 됨
    - e.g) `kr.co.vcnc.gryphon`
