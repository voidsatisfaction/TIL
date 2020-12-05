# Docker Deep Dive

- 의문
- 1 개요
  - 개요
  - Docker technology
  - OCI(Open Container Initiative)
- 2 The technical stuff
  - 2.1 The Docker Engine

## 의문

## 1. 개요

### 배경

- 역사
  - 1서버 1애플리케이션
    - 컴퓨터의 스펙을 얼마나 좋은걸 사야하는가?
    - 남는 자원은?
  - VM
    - 한 머신에서 여러 애플리케이션 동작하도록 함
    - OS overhead가 심함
  - Container
    - VM보다 효율적
    - 대중화 하기는 힘듬
  - Docker
    - Container의 대중화
      - 사용성
      - ecosystem

### 개요

- 도커 컨테이너 기술의 근간
  - Linux
    - Linux container
  - Windows
    - Windows container
    - WSL을 이용한 Linux container
  - MacOS
    - lightweight Linux VM을 이용한 Linux container
      - MACOS에서 Linux container를 개발하고 테스팅 가능
- 도커의 컨테이너들은 host OS의 kernel을 공유
  - 컨테이너화된 windows앱은 linux-based docker host에서는 동작하지 않음(서로 마찬가지)
    - Windows docker desktop에 "Linux containers"모드를 사용해서 Linux container를 실행할 수 있음

### Docker technology

Docker architecture

![](./images/docker_architecture1.png)

- daemon(engine)
  - runtime
    - `runc`
      - 개요
        - low-level
        - OS와의 인터페이스 담당, 컨테이너 start, stop 담당
          - namespaces, cgroup의 생성 등
      - 특징
        - OCI(Open Containers Initiative)의 runtime-spec을 맞춤
        - Docker node에서 동작하는 모든 컨테이너는 자신을 관리하는 `runc` 인스턴스를 갖음
    - `containerd`
      - 개요
        - high-level
        - 모든 컨테이너 라이프 사이클 관리
          - pulling images
          - creating network interfaces
          - managing lower level runc instances
      - 특징
        - 일반적인 도커의 설치는, 하나의 containerd process(docker-containerd)를 설치하는 것
          - `containered`는 각각의 컨테이너와 연관되는, 여러개의 `runc(docker-runc)`인스턴스를 관리
  - daemon
    - `dockerd`
      - 개요
        - lower level을 추상화하여, 일관적이고 쉬운 인터페이스 제공
        - `containerd`위에 존재하여, 보다 높은 추상도의 일을 행함
          - Docker remote API를 노출
          - image관리
          - volumes의 관리
          - networks의 관리
          - ...
- client
  - 개요
    - Linux에서는 IPC/Unix socket(`/var/run/docker.sock`), Windows에서는 named Pipe(`npipe:////./pipe/docker_engine`)를 이용해서, docker daemon과 상호작용 함
- orchestrator
  - `swarm`
    - 개요
      - 도커가 실행하는 노드의 클러스터를 관리하도록 하는 native support

### OCI(Open Container Initiative)

- 개요
  - low-level 기반 컨테이너 인프라의 components를 표준화하는 관리 기구
    - image format
    - container runtime
  - 과거 docker에 불만을 품어서, 컨테이너 표준에 대한 분쟁이 있었음
    - 표준은 무조건 합의하는게 좋다

## 2. The technical stuff

### 2.1 The Docker Engine

Docker architecture

![](./images/docker_architecture2.png)
