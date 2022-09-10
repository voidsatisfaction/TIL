# IAM(Identity and Access Management)

- 의문
- 기반 지식
- 개요
  - Policy Structure
  - Policy 평가 로직

## 의문

## 기반 지식

IAM aws ninja > 좋은 강의 자료

- IAM ARN(Amazon Resource Name)
  - 개요
    - 리소스의 표시 이름
  - 형식
    - `arn:partition:service:region:account:resource`
      - partition
        - 리소스가 위치하는 파티션 e.g) `aws-cn`
      - service
        - AWS 제품 e.g) `iam`
      - region
        - 리소스 리전 e.g) iam의 경우 글로벌이라서 공백
      - account
        - 하이픈이 없는 AWS 계정 ID
      - resource
        - 특정 리소스를 이름으로 식별
    - e.g)
      - `arn:aws:iam::123456789012:user/JohnDoe`
      - `arn:aws:iam::123456789012:role/aws-service-role/access-analyzer.amazonaws.com/AWSServiceRoleForAccessAnalyzer`

## 개요

- 개요
  - AWS 리소스에 대한 액세스를 안전하게 제어할 수 있는 웹 서비스
  - 인증 / 권한 부여 된 대상 제어
- 구성 요소
  - IAM user
    - AWS 내에서 생성하는 사용자 / 애플리케이션
  - IAM group
    - IAM User의 집합
      - 다수의 사용자에 대한 권한을 쉽게 관리
  - IAM role
    - *특정 권한을 가진 IAM 자격 증명*
    - *특정 사용자 / 애플리케이션에 / AWS 서비스에 접근 권한 위임 가능*
    - e.g) EC2 서비스에 IAM role을 할당 해서 EC2는 할당한 IAM role의 권한을 가지게 함
  - IAM policy
    - AWS의 리소스에 접근하는 해당 권한을 정의하는 개체

### Policy structure

```js
{
  "Statement": [
    {
      "Effect": "Allow", // "Allow" or "Deny"일 수 있음
      "Action": [
        "ec2:AuthorizeSecurityGroupIngress",
        "ec2:AuthorizeSecurityGroupEgress"
      ], // action은 권한을 부여하거나 거부할 특정 API 작업
      "Resource": "arn", // 작업의 영향을 받는 리소스. ARN(Amazon Resource Name)을 사용하거나 명령문이 모든 리소스에 적용됨을 표시하는 와일드카드(*)를 사용
      "Condition": { // 선택 사항으로서 정책이 적용되는 시점을 제어하는 데 사할 수 있음. 다양한 조건을 넣어 권한을 부여할 수 있음
        "condition": {
          "key": "value"
        }
      }
    }
  ]
}
```

### Policy 평가 로직

- 개요
  - IAM 설정시에, 다양한 policy가 적용될 경우 AWS가 해당 요청을 받으면 요청을 허용할지 거부할지 여부를 결정하는 로직
- 특징
  - Deny가 Allow보다 우선
  - Deny, Allow 둘다 없으면 암묵적 거부

## Best practice

- 직접 Access key, Secret key를 가지고 사용하지 말고, 각 서비스(e.g EC2)에 IAM role을 부여해서 사용할 수 있게 하는게 베스트
