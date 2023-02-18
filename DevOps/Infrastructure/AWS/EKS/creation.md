# EKS 클러스터 생성

- 의문
- 1 인프라 깔기
- 2 EKS 클러스터 생성
- 3 그 외 EKS 설정
- 4 kubernetes 시스템 오브젝트 설정(여기부터는 커스터마이징)
- 용어

## 의문

## 1. 인프라 깔기

- VPC
  - IP 주소들
    - Private
    - Public
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
- CNI 플러그인 구성
  - 정말 필요한 것인지?
- AWS EBS CSI 드라이버 설치
  - 애드온
  - 자체 관리형 설치(helm chart 등)

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
  - 주로 사용하는 오브젝트들(helmfile로 관리하면 편함)
    - CNI(terraform으로 설정하지 않은 경우)
    - cluster-autoscaler
    - aws-node-termination-handler
    - external-secrets
    - google-auth-server(custom OAuth2 proxy server)
    - alb controller
    - ingress controller

### 4-1 kubernetes 서비스 메시 설정

- istio

## 5. 워크로드 설치

### 5-1 모니터링 시스템

### 5-2 CI 시스템

### 5-3 애플리케이션

## 용어

- AWS VPC CNI(Container Network Interface)
  - EKS클러스터가 pod networking으로 VPC networking을 사용하도록 하는 것
    - pod IP = EC2 instance IP
  - 네트워크 성능이 더 좋음
  - but 설정을 더 해야하고, 비용이 높아서, 크고 network performance가 중요한 곳에서 사용하는것을 권장
