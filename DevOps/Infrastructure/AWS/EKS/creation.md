# EKS 클러스터 생성

- 의문
- 1 인프라 깔기
- 2 EKS 클러스터 생성
- 3 그 외 EKS 설정
- 4 kubernetes 시스템 오브젝트 설정(여기부터는 커스터마이징)
  - 4-1 kubernetes 서비스 메시 설정
- 5 워크로드 설치
  - 5-1 모니터링 시스템
  - 5-2 CI/CD 시스템
  - 5-3 애플리케이션
- 용어

## 의문

## 1. 인프라 깔기

- DNS
  - Route 53
  - ACM
- VPC
  - IP 주소들
    - Private ips
    - Public ips
  - subnet
    - private subnets
    - public subnets
  - nat gateway
  - route table
  - DNS 부여

## 2. EKS 클러스터 생성

기본적으로 terraform의 aws eks모듈을 사용하면 아래의 편하게 eks를 운용하는데에 필요한 자원을 생성 가능하다

- EKS 클러스터용 IAM role 생성
  - role policy
    - `--policy-arn arn:aws:iam::aws:policy/AmazonEKSClusterPolicy`
  - trust policy
    - `"Principal": { "Service": "eks.amazonaws.com" }`
  - IAM role
    - 위의 두 policy를 붙인 role 생성
- 클러스터 생성
  - 구성
    - 이름
    - k8s 버전
    - cluster service role
      - k8s 컨트롤 플레인이 사용자를 대신해서 AWS 리소스 관리할 수 있도록 함
    - k8s secret의 암호화(kms활용)
    - 태그 추가
  - 네트워크 설정(요구사항 및 고려사항 준수)
    - VPC 지정
      - 서브넷 지정
        - 2개 이상의 서브넷 설정 필요
        - 클러스터 생성후에는 서브넷 변경 불가
    - 보안 그룹 설정
- OIDC provider 생성
- *CNI 플러그인 구성*
  - 정말 필요한 것인지?
- AWS EBS CSI 드라이버 설치
  - 애드온
  - 자체 관리형 설치(helm chart 등)
  - gp3용 storage class 생성

## 3. 그 외 EKS 설정

- 접근 권한
  - EKS primary security group에 ingress rule의 추가
  - `aws-auth`에 eks 접근 권한 추가(API server)
    - 바스티온 role
    - 사용자 등
- `kubectl` 설정
  - config파일에 새 컨텍스트를 추가하여 `kubectl`이 클러스터와 통신하도록 설정
- EKS API server 엔드포인트의 제어
  - 프라이빗 활성화
    - VPC내에서 클러스터에 액세스하도록 하기
  - 퍼블릭 비활성화

## 4. kubernetes 시스템 오브젝트 설정(여기부터는 커스터마이징)

EKS 버전을 업데이트하는 경우

만약 기존에 이미 사용하던 helm chart가 있다면, 이참에 전부 새로 version up을 하도록 하자

- Helm 설치
- Helm을 이용하여 필요 오브젝트 설치
  - 아래의 오브젝트들의 설정 값을 새 클러스터용으로 변경
    - 아래 친구들의 자세한 내용은 `./add_ons.md`파일에 설명
  - 주로 사용하는 오브젝트들(helmfile로 관리하면 편함)
    - CNI(eks addon으로 설정하지 않은 경우)
    - cluster-autoscaler
    - aws-node-termination-handler
      - 이건 eks버전업으로 필요없어짐
    - external-secrets
    - alb controller
    - ingress controller
    - google-auth-server(custom OAuth2 proxy server)

### 4-1 kubernetes 서비스 메시 설정

- istio
  - istio-base, istiod를 헬름 차트를 통해서 쉽게 설치 가능

## 5. 워크로드 설치

### 5-1 모니터링 시스템

스타트업은 데이터독 쓰는게 나을것 같다는 생각도 든다

- Metrics Server
  - 쿠버네티스의 오직 autoscaling pipeline을 위한 리소스 메트릭을 제공(kubelet 으로부터)
    - HPA, VPA만을 위한 메트릭 서버
- Prometheus stack
  - kube-prometheus-stack
    - custom grafana dashboard
  - loki
    - promtail agent가 알아서 kubelet으로부터 log를 수집
- ELK stack
  - Elastic Search
  - Kibana
  - Elastic APM

### 5-2 CI/CD 시스템

- jenkins
  - 주의
    - eks 1.23 버전부터는 docker-shim지원이 중지 되었으므로, docker daemon을 native로 사용할 수 없음
      - 따라서, docker in docker, user data를 이용한 docker 설치 등의 방법을 동원해봐야한다
    - helm chart를 이용하여 jenkins 내부의 플러그인을 설치하고, jcasc를 정의하면 쉽게 provisioning가능하다

### 5-3 애플리케이션

## 용어

- AWS VPC CNI(Container Network Interface)
  - EKS클러스터가 pod networking으로 VPC networking을 사용하도록 하는 것
    - pod IP = EC2 instance IP
  - 네트워크 성능이 더 좋음
  - but 설정을 더 해야하고, 비용이 높아서, 크고 network performance가 중요한 곳에서 사용하는것을 권장
