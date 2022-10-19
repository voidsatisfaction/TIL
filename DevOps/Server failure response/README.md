# 장애대응 매뉴얼

- 의문
- 개요
- 장애 대응 순서
  - 장애 파악의 틀
- 장애 문서 작성
- 공유

## 의문

## 개요

- 데브옵스 사상(CAMSP)
  - Culture
  - Automation
  - Measurement
  - Share
  - Pile up

## 장애 대응 매뉴얼

### 장애 파악의 틀(AINDA)

- 얼럿 확인(Alert)
  - 센트리 얼럿
    - 어떤 에러가 나고 있는지?
    - 장애의 원인이 되는것으로 보이는 에러의 모든 이벤트 파악하기
- 인프라 이슈인가?(Infra)
  - 모니터링
    - k8s cluster use method
    - istio service
    - deployments
    - pods
    - jvm micrometer
- 네트워크 이슈인가?(Network)
  - 모니터링
    - 네트워크 메트릭 관찰
    - 얼럿
  - 대응사례
- DB 이슈인가?(DB)
  - 모니터링
    - AWS AuroraDB cloud watch
      - CPU / Memory / DB connection 수(max 확인)
    - AWS AuroraDB performance insights
    - 실제 DB 들어가서
      - `select * from information_schema.processlist (where info is not null)`
        - 스레드들의 상태를 관찰(데드락 등)
  - 대응 사례
    - 데드락
    - 커넥션 이슈
    - long running tx로 인한 rollback history가 너무 많이 자라는 문제
- 서버 이슈인가?(Application server)
  - 얼럿 확인
  - 로그 확인

### 장애 파악 팁

- 장애 파악시에 로깅을 잘 남기자
  - 추후에 원인 특정에 유리

### 장애 문서 작성

- 현상
- 대응
- 원인
- 조취

### 공유

- 서버 팀 내부 공유
- 다른 팀 외부 공유
  - 기술적인 용어는 알기 쉽게 풀어서 써주자
