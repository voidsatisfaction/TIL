# Elastic Platform

- 의문
- ELK 스택
  - Ingest
  - Store
  - Consume

## 의문

## ELK 스택

ELK 스택 아키텍처

![](./images/elastic_stack_architecture1.png)

- Ingest
- Store
- Consume

### Ingest

- 개요
  - Elastic Agent, Beats를 사용한 로그, 메트릭, 다른데이터의 수집후 전달하는 역할을 담당하는 컴포넌트
- 종류
  - Fleet and Elastic Agent
    - Elastic Agent
      - 로그, 메트릭, 다른 종류의 데이터를 호스트에 추가하는 통일된 방법
        - 호스트를 보안 위협으로부터 지키고, OS에서 데이터를 가져오기도 함
      - 각 에이전트는 정책을 갖음
        - 정책으로 새로운 데이터 소스와 연동할 수 있고, 보안성을 관리 가능
    - Fleet
      - Elastic Agent와 그것들의 정책을 중앙에서 관리하는 컴포넌트
        - 모든 Elastic Agent를 모니터링 하고, 정책을 관리하고, Elastic Agent 바이너리를 업그레이드 할 수 있음
  - APM
    - Elastic Stack에서 만들어진, 퍼포먼스 모니터링 시스템
      - 실시간으로 소프트웨어서비스와 애플리케이션을 모니터링 가능하게 함
        - 성능 이슈를 쉽게 고칠 수 있게 도와줌
      - 대상
        - response time, db 쿼리, 캐시 호출, 외부 HTTP 요청 등의 데이터 수집
  - Beats
    - Elastic search에 운영적인 데이터를 보내주기 위하여 서버에 에이전트로 설치되는 데이터 shipper
    - 대상
      - audit data, log files, journals, cloud data, availability, metrics, network traffic, Windows event logs
  - Elasticsearch ingest pipelines
    - 데이터를 ElasticSearch에 인덱싱하기 전에 변환해주는 역할
    - 하나 이상의 processor 태스크를 순차적으로 실행하도록 설정하여, Elasticsearch에 저장하기 전 documents에 변화를 가함
  - Logstash
    - 실시간 파이프라이닝을 할 수 있는 데이터 수집 엔진
    - 다양한 소스로부터 데이터를 동적으로 통합하고, 정규화할 수 있음

### Store

- Elasticsearch
  - 분산 검색 / 분석 엔진
- 특징
  - 준 실시간 검색 및 모든 타입의 데이터 분석 가능
    - structured, unstructured text, 수치 데이터, 지역 데이터 등의 데이터를 효율적으로 저장하고, 인덱스를 부여해서 빠른 검색 가능
  - REST API를 제공해서 데이터를 저장하고 뽑아올 수 있게 함

### Consume

- Kibana
  - es(elasticsearch)데이터를 이용해서 Elastic Stack을 매니징하기 위한 툴
    - analyze
    - visualize
- Elasticsearch client
  - API 리퀘스트와 리스폰스를 es로, 혹은 es로부터 쉽게 다룰 수 있도록 도와주는 클라이언트
    - Java, Ruby, Go, Python, ...
