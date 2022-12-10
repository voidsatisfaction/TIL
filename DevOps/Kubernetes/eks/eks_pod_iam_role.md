# EKS Pod IAM Role

- 의문
- 개요
- EKS의 팟에 적용하는 순서

## 의문

## 개요

EKS에서 pod level IAM role을 service account로 사용하기 큰 그림

![](./images/eks_pod_iam_role/eks_iam_role1.png)

- AWS의 기존의 인증 체계 대체
  - IAM role
    - EC2 node에만 부여 가능하므로 least privilege principle에 위배
  - `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` 환경변수를 k8s secret으로 마운팅
    - 키의 수명주기가 매우 김
    - 유출시 피해 발생
  - 새로운 방식의 인증이 필요함
- 개요
  - EKS클러스터를 OpenID인증 가능하게 해두고, IAM role을 OpenID를 이용해서 assume가능하게 설정하고, ServiceAccount과 팟을 연결시켜, 팟 레벨의 세분화되고 안전한 권한 부여를 하는 것
- 특징
    - 팟마다 별도 role 부여 가능
    - STS Token을 활용하여 키 관리 필요없음
    - 1~12시간 길이의 STS Token을 사용하여 키 노출 시에도 노출 범위 / 기간 최소화

## EKS의 팟에 적용하는 순서

- 1 EKS Cluster API에 OpenID Connect Provider(인증서버)를 연동한다
- 2 IAM role 생성
- 3 k8s service account 생성 & IAM 정보 주입(IAM Role의 ARN)
- 4 JWT 토큰 생성 및 팟에 service account 연결(projected volume)
- 5 해당 JWT를 가지고 AWS cli나 sdk가 자원에 접근

### 1. EKS Cluster API에 OpenID Connect Provider(인증서버)를 연동한다

- EKS생성시 자동으로 EKS IdP가 생성됨
- EKS IdP가 사용자의 신원을 확인
  - 해당 확인의 증거가 JWT token임

### 2. IAM role 생성

![](./images/eks_pod_iam_role/iam_role1.png)

- policy 설정
- trust relationship 설정
  - OpenID 설정
  - EKS IdP를 신뢰하도록
- 해석
  - 1 principal의 federated에서 지정된 provider에서 인증이 된 유저만 assume이 가능하다
  - 2 그 중에서도 "oidc.eks.ap-northeast-2.amazonaws.com/id/---:sub" 가 다음과 같은 문자열 매칭 조건을 만족하는 경우에만 assume이 가능하다

### 3. k8s service account 생성 & IAM 정보 주입(IAM Role의 ARN)

- `kind: ServiceAccount`
- k8s의 service account는 자체적으로 secret을 생성해서 해당 secret의 내용(JWT)으로 EKS의 openID에 인증을 하고, 그 인증 결과로 인증의 증거인 JWT를 받아옴
- 해당 JWT는 팟에 volume mount되어서 AWS cli나 AWS sdk가 자원을 접근하는데에 사용할 수 있게 함

### 4. JWT 토큰 생성 및 팟에 service account 연결(projected volume)

- `serviceAccountName: ...`

### 5. 해당 JWT를 가지고 AWS cli나 sdk가 자원에 접근

- 정확히는 해당 토큰으로 AWS STS(Security Token Service)에서 AssumeRole(임시 access key, secret key를 발급)을 하고 그것을 바탕으로 AWS의 자원에 접근
