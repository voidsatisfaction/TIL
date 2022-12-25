# AWS vault

- 의문
- 개요
- 설치 및 사용
  - 테라폼에서 사용하기

## 의문

## 개요

- 개요
  - 99designs에서 개발한 AWS 인증 정보를 안전하게 보관하도록 도와주는 도구
    - AWS의 AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY를 직접 노출하는 것을 방지
- 특징
  - mac OS의 키체인, 윈도우 자격 증명 관리자, Gnome 키링, KWallet등을 백엔드로 사용해 인증 정보를 안전하게 저장
  - 키를 사용할 때에는 Assume Role을 해서 사용함
- 동작 순서
  - `aws-vault exec <PROFILE_NAME> -- <COMMAND>`실행
  - `~/.aws/config`에서 aws-vault profile을 읽어옴
  - keychain에서 필요한 AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY를 읽어옴
  - STS에 AssumeRole을 하여, 임시 credential을 받아옴
  - 해당 임시 credential을 캐싱
  - 캐싱한 임시 credential값을 가지고, COMMAND를 실행
  - c.f) `aws-vault exec --debug test aws s3 ls`와 같은 커맨드로 확인 가능

## 설치 및 사용

```sh
brew install awscli
brew cask install aws-vault

aws-vault add <PROFILE_NAME>
# aws-vault add test
# aws-vault add staging
# aws-vault add prod
# 엑세스 키 정보 입력
Enter Access Key ID: ...
Enter Secret Access Key: ...

#사용하는 법
aws-vault exec test --
```

1. AWS CLI설치(`brew install awscli`)
2. aws-vault 설치(`brew install --cask aws-vault`)
3. AWS 콘솔에 로그인하여, 액세스 키 생성 & 기억해두기
4. `aws-vault add test(staging)`를 실행하고, 생성된 액세스 키 정보 입력
5. `$HOME/.aws/config`파일을 열어서 다음과 같이 수정(mfa_serial을 자신의 aws security credential에 등록된 값으로 변경)
6. 키체인 암호를 계속 물어보지 않도록 설정하기 위해서 다음과 같이 실행 `security set-key-chain-settings ~/Library/Keychains/aws-vault.keychain-db`
7. `aws-vault exec test -- aws sts get-caller-identity`를 실행

### 테라폼에서 사용하기

```sh
aws-vault exec <PROFILE_NAME> -- terraform plan
```
