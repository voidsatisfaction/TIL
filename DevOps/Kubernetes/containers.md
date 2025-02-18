# Containers

- 의문
- 개요
- Images
  - 이미지 업데이트
- 런타임 클래스
- 컨테이너 환경변수
- 컨테이너 라이프사이클 훅

## 의문

## 개요

## Images

- 개요
  - 컨테이너 이미지는 애플리케이션과 모든 소프트웨어 의존성을 캡슐화한 바이너리 데이터
- 특징
  - 독자적으로 실행 가능함
  - 애플리케이션 팟을 만들기 전에 레지스트리에 푸시하고 참조하게 하는 것이 기본

### 이미지 업데이트

- 이미지 pull 정책
  - 개요
    - kubelet이 특정 이미지를 풀하려고 할 때 영향을 주는 정책
  - 종류
    - `IfNotPresent`(default)
      - 이미지가 로컬에 없는 경우에만 내려받음
    - `Always`
      - 컨테이너 기동시 마다, kubelet이 컨테이너 이미지 레지스트리에 이름과 이미지의 다이제스트가 있는지 질의하고, 일치하는 다이제스트를 가진 컨테이너 이미지가 로컬에 있으면 kubelet은 캐시된 이미지를 사용하고, 그 외의 경우는 검색된 다이제스트를 가진 이미지를 내려받아서 사용
        - **다이제스트를 사용한다는 것이 중요(단순히 image-name:tag비교가 아니라 image-name:digest)**
          - 코드를 변경해도 다이제스트는 변해서 정말 같은 버전인것을 보장
    - `Never`
      - 이미지를 가져오지 않고, 오직 로컬에 존재하는 경우에만 실행
- ImagePullBackoff
  - 개요
    - kubelet이 컨테이너 런타임을 이용하여 팟의 컨테이너 생성을 시작할 때, `ImagePullBackOff`로 인해 컨테이너가 waiting상태에 있을 수 있음
  - 원인
    - 이미지 이름이 잘못됨, imagePullSecret 없이 비공개 레지스트리에서 풀링 시도로 인하여 k8s가 컨테이너 이미지를 가져올 수 없어서 컨테이너를 실행할 수 없음을 의미
  - Backoff
    - 시간 간격을 늘려가며 계속해서 시도하며, 시간 간격의 상항은 300초(5분)

## 런타임 클래스

- 개요
  - 팟의 컨테이너를 실행할 때, 런타임 클래스를 지정할 수 있음
    - e.g) 더 강한 보안을 필요로할때는 하드웨어 가상화를 이용하는 런타임 클래스를 사용하던지
- 도입 순서
  - CRI 구현을 노드에 설정
  - 상응하는 런타임클래스 리소스 생성
  - 팟의 spec에 적용하여 사용 & 스케쥴
    - selector
    - toleration

## 컨테이너 환경변수

- 개요
  - 기본적으로 주입되는 컨테이너 환경 변수
    - 컨테이너 자신에 대한 정보
    - 클러스터 내의 다른 오브젝트에 대한 정보
- 종류
  - 생성될 때 실행중이던 동일 네임스페이스의 모든 서비스의 목록을 환경변수로 주입
    - `FOO_SERVICE_HOST=<서비스가 동작중인 호스트>`
    - `FOO_SERVICE_PORT=<서비스가 동작중인 포트>`

## 컨테이너 라이프사이클 훅

- 개요
  - 컨테이너 라이프사이클에 훅을 제공하여, 핸들러에 구현된 코드를 실행할 수 있도록 함
- 종류
  - `PostStart`
    - 컨테이너가 생성된 직후에 실행되며, 컨테이너 엔트리포인트에 앞서서 실행된다는 보장은 없음
      - 파라미터는 핸들러에 전달되지 않음
  - `PreStop`
    - API요청이나 liveness probe실패, 선점, 자원 경합 등의 관리 이벤트로인해 컨테이너가 종료되지 직전에 호출
    - 컨테이너가 이미 terminated 또는 completed 상태인 경우에는 `PreStop`훅 요청이 실패
      - TERM 신호가 보내지기 전에 완료되어야 함
- 구현
  - `Exec`
    - 컨테이너 내부에서 `pre-stop.sh`와 같은 커맨드 실행
  - `HTTP`
    - 컨테이너의 특정 엔드포인트에 대해서 HTTP요청 실행
- 특징
  - 훅은 같은 이벤트에 여러번 호출될 수 있음
  - 훅은 최대한 가벼워야 함
  - 디버깅은 핸들러의 이벤트를 관찰
    - `FailedPostStartHook`
    - `FailedPreStopHook`
