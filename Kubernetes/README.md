# 쿠버네티스

- 의문
- 개요

## 의문

## 개요

- 쿠버네티스
  - 개요
    - 컨테이너화된 서비스들을 다루는 오픈소스 플랫폼
      - 선언적 설정과 자동화
      - A라는 상태로 계속해서 유지하도록 설정파일로 관리
  - 필요성
    - 분산 시스템을 탄력있게 실행하는 프레임워크
      - scaling, failover
      - 까나리 배포
  - 특징
    - 점진적이고 자동 rollout and rollback
      - 배포되는 컨테이너들의 원하는 상태를 기술언어로 기술 가능
    - *서비스 디스커버리와* 로드밸런싱
      - 팟들에게 각자 IP 주소를 부여하고, 팟의 집합에 하나의 DNS 이름을 부여하고 그것들의 로드밸런싱 가능
        - 하나의 DNS 이름으로 inbound 트래픽이 들어오고, 그 트래픽을 로드밸런싱
    - 스토리지 오케스트레이션
      - 다양한 스토리지 마운트해서 사용 가능
    - 시크릿 / 설정 관리
      - 이미지를 다시 빌드하지 않고도 애플리케이션의 설정과 시크릿을 업데이트하고 배포할 수 있음
    - 자동 *bin packing*
      - 컨테이너를 리소스 요청과 노드와 같은 다른 제한에 기반해서 효율적이며 자동적으로 배치
    - 배치 실행(CI도 가능)
    - IPv4/IPv6 둘다 사용가능
    - 수평적 확장
      - 커맨드나 UI 혹은, CPU 사용량에 따른 자동적인 스케일 아웃 가능
    - 자가 치유
      - 컨테이너가 죽으면 재시작시키고, 노드가 죽으면 컨테이너들을 재배치 시키고, 유저가 정의한 헬스체크에 반응하지 않는 컨테이너를 죽이고, 서빙이 준비되기 전까지는 노출시키지 않음
    - 확장성
      - 소스코드를 변경시키지 않고도, 쿠버네티스 클러스터에 기능 추가 가능

### 컴포넌트

쿠버네티스의 컴포넌트

![](./images/components-of-kubernetes1.svg)

- cluster
  - node의 집합
- node
  - 컨테이너화된 애플리케이션을 실제로 실행하는 워커 머신
  - pod들을 호스팅함
- pod
  - 애플리케이션 컴포넌트들
    - 컨테이너들을 포함
- control plane
  - 클러스터 내부의 워커 노드와 팟들을 관리함

#### Control Plane Components

- 개요
  - 클러스터에 대한 global decision을 내리는 곳(e.g 스케쥴링, 팟의 개수 싱크)
  - 일반적으로 단일 머신에 컴포넌트들을 배치
- 종류
  - `kube-apiserver`
    - Kubernetes API를 노출하는 컴포넌트
      - control plane의 인터페이스
  - `etcd`
    - 쿠버네티스가 사용하는 모든 클러스터 데이터를 저장하는데에 사용되는 key-value 스토어
  - `kube-scheduler`
    - 새로 만들어진 노드에 할당되지 않은 팟들을 보고, 그것이 실행될 노드를 선택함
      - *팟이 만들어진다 != 팟이 실행된다?*
      - 다양한 요소를 고려함
        - 개인, 집단 자원 requirements, hardware/software/policy 제한
  - `kube-controller-manager`
    - 컨트롤러 프로세스를 실행하는 컴포넌트
    - 컨트롤러는 논리적으로는 분리된 프로세스이나, 복잡도를 줄이기 위해서 실제로는 하나의 바이너리에서 싱글 프로세스로 동작함
    - 종류
      - node controller
        - 노드가 죽었을경우, 알아채고 반응하는 역할
      - job controller
        - 태스크를 수행하는 잡 오브젝트를 보고, 팟을 만들어 태스크가 끝나기까지 실행
      - endpoints controller
        - *엔드포인트 오브젝트들을 살게 함?*
      - service account & token controllers
        - *default 계정과, 새 namespace를 위한 API 접근 토큰을 생성*
  - `cloud-controller-manager`
    - 클라우드에 특화된 제어 로직을 포함
      - 클라우드 제공자의 API로 클러스터를 링크함
      - 오직 클러스터와 상호작용하는 컴포넌트와 클라우드 플랫폼과 상호작용하는 컴포넌트 분리
    - 종류
      - node controller
        - 응답이 멈춘 뒤에 클라우드에서 노드가 삭제되었는지 판단하는것을 체크하기 위함
      - route controller
        - 클라우드 인프라 내부에서 라우트를 설정하기 위함
      - service controller
        - 클라우드의 로드 밸런서를 생성하고, 갱신하고, 삭제하기위함

#### Node Components

- 개요
  - 노드 각각에서 실행되며, 실행중인 팟들을 관리하고 쿠버네티스 런타임 환경을 제공함
- 종류
  - `kubelet`
    - 클러스터에 있는 각각의 노드위에서 동작
      - 하나의 팟에서 컨테이너들이 실행되도록 함
      - PodSpec의 집합을 받아서 컨테이너들이 PodSpec에 기술된대로 건강하게 실행되는것을 보장
  - `kube-proxy`
    - 클러스터에 있는 각각의 노드위에서 동작하는 네트워크 프록시
    - 노드들사이의 네트워크룰을 유지함
      - 팟들사이의 커뮤니케이션을 가능하게 함
  - `container runtime`
    - 컨테이너를 실행하는 역할을 담당
    - Kubernetes가 서포트하는 종류
      - `containerd`
      - `CRI-O`
      - 그 외의 Kubernetes CRI (Container Runtime Interface)를 만족하는 구현체들

#### Addons

- 개요
  - 클러스터 기능들을 구현하기 위해서 쿠버네티스 자원을 사용
  - 네임스페이스된 애드온의 리소스들은 `kube-system` 네임스페이스속에 포함됨
- 종류
  - DNS(필수)
    - 모든 쿠버네티스 클러스터는 클러스터 DNS를 갖음
    - 쿠버네티스에 의해서 시작된 컨테이너들은 DNS 서칭시(외부와의 통신할때)에, 쿠버네티스 DNS역시 포함함
  - Web UI (대시보드)
    - 쿠버네티스 클러스터를 위한 웹 기반 UI
    - 유저가 애플리케이션을 트러블 슈팅하거나, 클러스터 그 자체를 트러블 슈팅할 수 있게 도와줌
  - Container Resource Monitoring
    - 중앙 DB에 시계얼 컨테이너 메트릭을 저장하고, 데이터 브라우징을 가능하게 함
  - Cluster-level Logging
    - 컨테이너 로그들을 중앙 로그 저장소에 저장하고, search/browsing interface를 확충

### 쿠버네티스 API

- 개요
  - kubernetes의 control plane의 핵심은 HTTP API 서버
    - 엔드유저가, 클러스터의 서로 다른 파트가, 외부 컴포넌트가 서로 커뮤니케이션하도록 함
    - API 오브젝트(Pods, Namespaces, ConfigMaps, Events)들의 상태를 조작하고, 쿼리할 수 있도록 함
  - 대개 `kubectl`이라는 커맨드라인 인터페이스나 `kubeadm`이라는 다른 커맨드라인 툴(둘다 API를 사용)을 사용해서 조작하나, 직접 REST call을 해서 API에 직접 접근도 가능

### 쿠버네티스 오브젝트

yaml파일로 만들어진 object spec의 예시

```yaml
apiVersion: apps/v1 # required: K8s의 API버전
kind: Deployment    # required: 생성하고자 하는 오브젝트의 종류
metadata:           # required: 오브젝트의 유니크 식별자
  name: nginx-deployment
spec:               # required: 원하는 state(e.g 각 팟에 대해서 desired 상태를 기술)
  selector:
    matchLabels:
      app: nginx
  replicas: 2 # tells deployment to run 2 pods matching the template
  template:     # StatefulSet 컨트롤러가 생성하는 팟들을 나타냄
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

- 개요
  - 쿠버네티스 오브젝트는 쿠버네티스 시스템의 영속적인 엔티티들을 의미함
  - 쿠버네티스는 클러스터의 상태를 엔티티로 나타냄
- 내용
  - 어떤 컨테이너화된 애플리케이션 / 노드가 실행되고 있는지
  - 그러한 애플리케이션이 사용가능한 자원
  - 애플리케이션이 동작하는 방법에 대한 정책
    - 재시작 정책, 업그레이드, fault-tolerance
- 특징
  - 오브젝트를 만들면, 쿠버네티스 시스템은 지속적으로 해당 오브젝트가 존재하도록 동작함
    - 클러스터의 desired state를 만듬
  - 쿠버네티스 오브젝트를 만들고, 수정하고, 삭제하기 위해서는, 쿠버네티스 API를 사용해야 함
    - `kubectl`등과 같은 툴로도 제어 가능
- Object spec & status
  - 개요
    - 거의 모든 쿠버네티스 오브젝트는 오브젝트의 설정을 제어하는 두개의 네스팅된 오브젝트 필드를 포함함
      - `(object)spec`
      - `(object)status`
      - 선언적으로 desired state를 기술해서 오브젝트를 생성함
    - 쿠버네티스 시스템은 spec을 이용해서 오브젝트를 생성하고, 지속적으로 현재 state를 spec으로 맞춤
    - spec은 일반적으로 yaml파일로 기술
    - 해당 파일을 JSON으로 바꾸고, API 리퀘스트를 보낼 수 있음
      - `kubectl apply -f ~.yaml` 이런식으로도 가능
  - status
    - 오브젝트의 현재 상태
      - control plane이 지속적으로 모든 오브젝트의 실제 상태를 desired 상태로 싱크를 맞춰줌
        - *control plane*이 맞는가?
    - 예시
      - 쿠버네티스에서는 하나의 deployment도 클러스터에서 동작하는 애플리케이션을 타나내는 오브젝트임
      - deployment를 만들때, deployment `spec`을 만들어서, 실행할 애플리케이션의 replica를 만듬
      - 쿠버네티스 시스템은 deployment 스펙을 읽고 인스턴스의 개수를 원하는 상태로 맞춤
  - spec
    - 오브젝트의 desired 상태
    - 쿠버네티스 시스템이 계속해서 이 스펙으로 상태를 맞춰줌
