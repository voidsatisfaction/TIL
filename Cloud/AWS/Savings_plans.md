# AWS Savings Plans

- 의문
- 참고
  - 온디맨드란?
- 개요
  - Savings Plans vs RI(Reserved Instance)

## 의문

## 참고

- 온디맨드란?
  - 하나의 인스턴스를 장기약정없이 필요할때 사용하고 과금하는 과금 모델
    - 즉, 어느정도의 시간동안 사용했냐가 포인트
- 비용 참고
  - 공식: https://aws.amazon.com/savingsplans/compute-pricing/
  - 비공식 비교: https://instances.vantage.sh/?region=ap-northeast-2

## 개요

- 1년 또는 3년 약정 단위로, 온디맨드 요금보다 저렴한 요금을 제공하는 유연한 요금 모델
- 종류
  - Compute Savings Plans
    - 대상: EC2, Lambda, Fargate
    - 인스턴스 유형, 인스턴스 사이즈, 리전, OS, *tenancy* 에 관계 없음
  - EC2 Instance Savings Plans
    - 대상: EC2
    - 리전, 인스턴스 유형은 고정, AZ, 인스턴스 사이즈, OS, tenacy에는 관계 없음
  - Amazon SageMaker Savings Plans
    - 대상: Amazon SageMaker(기계학습)
- 이점
  - 비용 절감
    - 60 ~ 70%
  - 편의성
    - 쉽게 도입 가능

### Savings Plans vs RI(Reserved Instance)

- Savings Plans
  - 커밋
    - 일정 기간동안 사용하는 돈의 양
  - RI + 유연성
  - 인스턴스 설정이 아닌, 사용량에 대한 과금 가능
- RI
  - 커밋
    - 일정 기간동안 특정 가용존에 용량과 자원을 예약하여 사용
  - 대상: EC2, RDS
- 공통점
  - 둘이 가격 정책은 같음
