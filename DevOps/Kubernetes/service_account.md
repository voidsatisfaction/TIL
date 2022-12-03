# 서비스 어카운트

## 의문

## 개요

- 정의
  - 팟에서 실행되는 프로세스에게 컨트롤플레인의 API 서버를 사용할 수 있도록 id를 제공하는 오브젝트
    - 사람에게 부여하는 id는 유저 어카운트
- 특징
  - 각 namespace에는 반드시 `default` 서비스 어카운트가 존재
    - 명시하지 않으면 `default`서비스 어카운트 사용
  - `.spec.serviceAccountName`으로 서비스 어카운트 지정 가능
  - 생성시에만 지정 가능해서 이미 존재하는 팟에 업데이트 불가
  - `imagePullSecret`도 추가 가능
    - imagePullSecret을 생성(secret 오브젝트)
    - service account에 imagePullSecret을 추가
    - 새 팟에 imagePullSecret이 잘 붙었는지 체크
      - 팟에 설정된 `imagePullSecret`이 더 우선됨

### IAM roles for service accounts

- AWS의 기존의 인증 체계 대체
  - IAM role
    - least privilege principle에 위배
  - `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` 환경변수를 k8s secret으로 마운팅
    - 키의 수명주기가 매우 김
    - 유출시 피해 발생
- 개요
  - IAM role을 ServiceAccount와 연관시키고, ServiceAccount를 파과 연결시켜, 세분화되고 안전한 권한 부여를 하는 것
- 특징
    - 팟마다 별도 role 부여 가능
    - STS Token을 활용하여 키 관리 필요없음
    - 1~12시간 길이의 STS Token을 사용하여 키 노출 시에도 노출 범위 / 기간 최소화
- EKS의 팟에 적용하는 순서
  - 1 IAM <-> EKS Cluster 연결
    - *Create Provider*
      - *이게 뭐야?*
  - 2 IAM role 생성
    - web identity
    - trust relationship 수정
  - 3 k8s service account 생성
    - `kind: ServiceAccount`
  - 4 service account에 IAM 정보 주입(IAM Role의 ARN)
  - 5 팟에 service account 연결
    - `serviceAccountName: ...`
  - 6 팟에 연결된 것을 확인(볼륨 마운트)

### 수동으로 생성

```
k create token admin-user --duration ...
```
