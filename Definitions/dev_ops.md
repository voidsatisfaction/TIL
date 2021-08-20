# DevOps

- General
  - Blue-Green 배포
  - CNCF(Cloud Native Computing Foundation)
  - Cloud Native

## 강의 자료

- [Introduction to Kubernetes](https://www.edx.org/course/introduction-to-kubernetes)

## General

### Blue-Green 배포

- 정의
  - 이전 버전을 blue, 새 버전을 green환경으로 두면, blue에서 green으로 점진적으로 이전하는 애플리케이션 릴리스 모델
- 절차
  - blue와 똑같은 마이크로서비스를 똑같은 별도의 컨테이너에 복사
    - 이미 Q/A및 스테이징을 거침
  - 로드 밸런서를 이용하여 blue에서 green으로 리다이렉트
  - blue는 재해 복구 옵션이 되어 대기하거나, 다음 업데이트를 위한 컨테이너가 됨

### CNCF(Cloud Native Computing Foundation)

- 미션
  - make cloud native computing ubiquitous
  - 벤더에 중립적인 오픈소스의 생태계를 유지하고, 촉진시키는 것
    - SOTA 패턴을 누구든 사용가능하게 민주화 한다
- 역할(오픈소스 커뮤니티)
  - 프로젝트 관리
  - 생태계의 진화와 성장 촉진
  - 기존 기술의 프로모션, 애플리케이션 정의 및 관리, 이벤트 컨퍼런스, 트레이닝 코스, 개발자 인증
- 가치
  - Fast is better than slow
  - Open
  - Fair
  - Strong technical identity
  - Clear boundaries
  - Scalable
  - Platform agnostic

### Cloud Native

- 정의
  - 클라우드의 이점을 최대로 활용할 수 있도록 애플리케이션을 구축하고 실행하는 방식
  - CNCF정의
    - 퍼블릭, 프라이빗, 그리고 하이브리드 클라우드와 같은 현대적이고 동적인 환경에서 확장 가능한 애플리케이션을 개발하고 실행할 수 있게 해줌
      - e.g) 컨테이너, 서비스 메쉬, 마이크로서비스, 불변 인프라, 선언형 API
    - resilient, manageable, observable한 loosely coupled system을 가능하게 함
    - 자동화 기능을 함께 사용하면, 영향이 큰 변경을 최소한의 노력으로 자주, 예측 가능하게 수행할 수 있음
