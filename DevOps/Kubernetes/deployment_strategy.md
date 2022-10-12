# Kubernetes Deployment strategies

- 의문
- 개요
  - 종류
    - Canary
    - Ramped slow rollout
    - Rolling deployment
    - Best-effort controlled rollout
    - Recreate

## 의문

## 개요

- 배포 전략
  - 서로 다른 버전의 쿠버네티스 애플리케이션을 어떻게 만들고, 업그레이드하고, 다운그레이드할 것인지를 정의

### 종류(안전 - 위험 순)

- **Canary deployment**
  - 대부분의 유저에게는 기존 버전을 서빙하고, 일부 유저에게 새 버전을 서빙하도록 한 뒤에, 새 버전이 성공적이면 더 많은 유저에게 점진적으로 배포
- **Ramped slow rollout**
  - 레플리카가 롤아웃되는 페이스 조절 가능
  - e.g)
    - maxSurge: 1
    - maxUnavailable: 0
  - e.g) 타다의 모든 팟들
- **Rolling deployment**
  - 클러스터의 다운타임 없이 이전 버전의 애플리케이션을 새 버전으로 교체해 나감
    - 기존 팟을 내리기 전에 readiness probe를 사용해서 새 팟을 체크
  - 파라미터
    - MaxSurge
      - 롤 아웃 중간에 한번에 최대 몇개의 팟이 생성될 수 있는지(퍼센트의 경우 반올림 적용)
      - 기본값은 25%
    - MaxUnavailable
      - 롤 아웃 중간에 최대 몇개의 팟이 사용 불가능한지 나타내는 수치
- **Best-effort controlled rollout**
  - max unavailable의 비율을 정해두고, max Surge를 0으로 두고 기존 일부 팟들만 다운타임을 허용해서 빠르게 교체해나가는 것
  - e.g)
    - maxSurge: 0
    - maxUnavailable: 20%
- **Recreate**
  - 모든 팟을 지우고, 새 버전의 팟으로 대체
    - 다운타임 존재
