# 서비스 어카운트

- 의문
- 개요
  - IAM roles using service accounts(EKS)
  - 수동으로 생성

## 의문

- *IAM roles using service accounts(EKS)에서 projected volume mount된 토큰의 시간이 만료가되면 팟에 어떤 현상이 일어나는지?*
  - 재인증해주나?

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

### 수동으로 생성

```
k create token admin-user --duration ...
```
