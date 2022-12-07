# Spring Cloud

- 의문
- 개요
- AWS Credential 설정
  - 방식

## 의문

## 개요

## AWS Credential 설정

- 개요
  - AWS를 사용할 권한을 애플리케이션에 부여하는 것

### 방식

DefaultAWSCredentialsProviderChain의 예시

```java
// gryphon 키네시스 설정
@Bean
fun amazonKinesis(awsCredentialsProvider: AWSCredentialsProvider, regionProvider: RegionProvider): AmazonKinesisAsync {
    return AmazonKinesisAsyncClientBuilder.standard()
        .withCredentials(awsCredentialsProvider)
        .withRegion(regionProvider.region.name)
        .build()
}

// 기본 체인 설정
public DefaultAWSCredentialsProviderChain() {
    super(new EnvironmentVariableCredentialsProvider(),
          new SystemPropertiesCredentialsProvider(),
          WebIdentityTokenCredentialsProvider.create(),
          new ProfileCredentialsProvider(),
          new EC2ContainerCredentialsProviderWrapper());
}

// WebIdentityTokenCredentialsProvider에서 사용되는 환경변수
public static final String AWS_WEB_IDENTITY_ENV_VAR = "AWS_WEB_IDENTITY_TOKEN_FILE";

/** Environment variable name for the AWS role arn */
public static final String AWS_ROLE_ARN_ENV_VAR = "AWS_ROLE_ARN";
```

- `DefaultAWSCredentialsProviderChain`
  - AWS credential을 순서대로 참조하기위한 설정된 체인
- AWS Credential 종류
  - `BasicAWSCredentials`
    - 액세스키와 비밀키를 코드에 직접 적어 주입하는 방법
  - `EnvironmentVariableCredentialsProvider`
    - 환경 변수로 액세스키와 비밀키를 입력해주는 방법
      - `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`
  - `SystemPropertiesCredentialsProvider`
    - 자바의 시스템 속성을 이용해 주입하는 방법
      - `aws.accessKeyId`, `aws.secretKey`
  - `InstanceProfileCredentialsProvider`(recommended)
    - IAM role을 애플리케이션이 구동하는 EC2에 바로 부여하는 방법
  - `WebIdentityTokenCredentialsProvider`(recommended)
    - IAM의 WebIdentityToken으로 설정하는 방법
- 아무 credentials 설정을 하지 않았을 경우
  - `DefaultAWSCredentialsProviderChain`를 사용
  - *`AWSCredentialsProvider`만 설정한 경우는 뭐지?*
