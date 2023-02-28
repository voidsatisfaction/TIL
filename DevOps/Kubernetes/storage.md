# Kubernetes storage

- 의문
- 개요
- persistent volume vs persistent volume claims vs storage class
  - PVC로 인하여 팟에 pv가 바인딩 되는 순서

## 의문

## 개요

## persistent volume vs persistent volume claims vs storage class

- persistent volume
  - 개요
    - 클러스터에서의 물리적 스토리지의 부분을 나타내는 자원
  - 특징
    - 클러스터 레벨의 자원
- persistent volume claims
  - 개요
    - 팟에 의해서 만들어진 스토리지의 리퀘스트
      - 팟이 요청하면, kubernetes는 요청한 storage class와 access mode를 충족하는 PV를 찾고, 없으면 dynamically provision할 수 있음
  - 특징
    - 네임스페이스 레벨 자원
    - 요청 사이즈, access mode, storage class name 지정
- storage class
  - 개요
    - PVC에서 요청하는 파라미터로, provision되고 싶어하는 PV의 특성을 기술한 것(PVC와 분리되어서 재사용 가능)
      - kubernetes는 필요한 프로퍼티와 함께 새로운 PV를 일치하는 storage class를 매칭해서 제공
        - e.g) 성능 특성, 물리적 스토리지 위치 등
  - 특징
    - PVC가 생성될 때, storage class를 attribute로 지정하고, kubernetes는 요청한 storage class attribute를 만족할 수 있는 PV를 동적으로 생성할 수 있는 provisioner를 탐색하고,

### PVC로 인하여 팟에 pv가 바인딩 되는 순서

- 팟이 PVC를 생성하여 PV를 요청함
  - PVC에는 사이즈, access mode, storage class등의 요청 정보 포함
- kubernetes는 PVC의 내용을 보고 해당 PVC를 만족하는 PV를 찾음
- kubernetes는 PVC의 내용을 만족하는 PV가 없으면 해당 사이즈, access mode, storage class를 만족하는 PV를 동적으로 provision
- 해당 PV를 PVC에 bound 시킴
- 팟이 클러스터에 스케쥴링 됨
- 팟이 동작하기 시작하면, 마운트된 볼륨을 사용할 수 있음
- 팟이 삭제되면 PVC와 PV는 삭제되지 않고 재사용될 수 있음
