# Prometheus Operator

- 의문
- 개요
  - 아키텍처
- 설치
  - alertmanager
  - PrometheusRule

## 의문

## 개요

- 개요
  - 프로메테우스의 개발과 운영 및 관련 모니터링 컴포넌트를 쿠버네티스 환경에 제공
    - 쿠버네티스 클러스터를 위한 프로메테우스 기반 설정의 자동화 및 간단화(오퍼레이터 패턴 사용)
    - Service Monitor와 같은 모니터링 설정을 재배포 없이 CRD와 오퍼레이터를 이용해서 쉽게 추가및 수정 제거 가능
- 기능
  - k8s custom resource
    - 프로메테우스와 얼럿매니저와 관련 컴포넌트를 쿠버네티스 커스텀 리소스로 관리
      - e.g) serviceMonitor
  - simplified deployment configuration
    - 네이티브 쿠버네티스 리소스로 프로메테우스의 버전, 영속화, retention policy, replica등을 관리
  - prometheus target configuration
    - 쿠버네티스 레이블 쿼리 등으로 자동으로 모니터링 타겟 설정을 만들어줌
      - 프로메테우스 설정 언어를 학습할 필요가 없음
- c.f) 오퍼레이터 패턴
  - 개요
    - CRD(커스텀 리소스와 커스텀 컨트롤러)를 사용하여 애플리케이션 및 해당 컴포넌를 관리하는 쿠버네티스의 소프트웨어 익스텐션
    - 컨트롤 루프 원칙을 따름
  - 특징
    - 쿠버네티스 코드 자체를 수정하지 않고, 컨트롤러를 하나 이상의 사용자 정의 리소스(CRD)에 연결하여 클러스터의 동작을 확장
  - 예시
    - Prometheus operator

### 아키텍처

프로메테우스 오퍼레이터 아키텍처

![](./images/prometheus_operator_architecture1.png)

- 구성
  - Prometheus
    - Prometheus deployment에 대해서 desired state를 기술함
    - Prometheus configuration을 기술하는 secret을 관리
  - Alertmanager
    - 얼럿 매니저의 replica
    - 얼럿 매니저의 팟들은 `alertmanager-<alertmanager-name>` 시크릿을 마운트 하도록 함
  - AlertmanagerConfig
    - 선언적으로 Alertmanager 설정의 subsection을 기술함
      - routing
      - receiver
      - inhibition rules
  - PrometheusRule
    - Prometheus가 소화해야 하는 desired 프로메테우스 룰을 기술
      - e.g) 얼럿 매니저로 보낼 이벤트 등
    - Operator에 의해서 자동으로 reconcile됨
      - restart안해도 됨
  - ServiceMonitor
    - 프로메테우스에 의해서 모니터링 될 대상 서비스를 CRD로 operator pattern으로 구성함
      - 원래라면 configMap으로 설정할것을 serviceMonitor인 k8s CRD로 대신함
      - 실시간으로 갱신 가능
  - PodMonitor
    - 프로메테우스에 의해서 모니터링 될 대상 팟을 CRD로 operator pattern으로 구성함
  - *ThanosRuler*
    - k8s 클러스터 내부에서 Thanos Ruler 의 desired state를 기술
    - *애초에 이게 뭐임?*
  - Probe

## 설치

- 애플리케이션 & 서비스 디플로이
- 프로메테우스 권한 디플로이
  - service account
  - cluster role
  - clusterRoleBinding
- 프로메테우스 디플로이
  - service account 매핑
  - service monitor selector 설정
- 서비스 모니터 디플로이

### alertmanager

- 설정
  - Prometheus Operator
    - AlertmanagerConfig(클러스터 설정)
      - k8s 시크릿으로 native alertmanager config파일을 사용
      - `spec.alertmanagerConfiguration`을 사용하여 설정
      - `AlertmanagerConfig`오브젝트를 참조
  - Alerting rules

#### PrometheusRule

```yaml
apiVersion: monitoring.coreos.com/v1
kind: Prometheus
metadata:
  name: example
spec:
  serviceAccountName: prometheus
  replicas: 2
  alerting:
    alertmanagers:
    - namespace: default
      name: alertmanager-example
      port: web
  serviceMonitorSelector:
    matchLabels:
      team: frontend
  ruleSelector: # PrometheusRule을 선택하는 셀렉터
    matchLabels:
      role: alert-rules
      prometheus: example
  ruleNamespaceSelector: # empty dict로 설정하면 모든 네임스페이스에서 룰을 발견함
    matchLabels:
      team: frontend

---

apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  creationTimestamp: null
  labels:
    prometheus: example
    role: alert-rules
  name: prometheus-example-rules
spec:
  groups:
  - name: ./example.rules
    rules:
    - alert: ExampleAlert
      expr: vector(1)
```

- 개요
  - alerting등을 포함한 프로메테우스의 룰을 정의하도록 함
