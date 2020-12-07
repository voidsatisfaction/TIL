# Docker Deep Dive

- 의문
- 1 개요
  - 개요
  - Docker technology
  - OCI(Open Container Initiative)
- 2 The technical stuff
  - 2.1 The Docker Engine

## 의문

- *OS agnostic을 지원하는 도커의 툴 이름이 뭔가?*
  - `runc?`, `containerd?`, `libcontainer?`

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
          - managing lower level runc instances
        - 그 외 추가 기능
          - pulling images
          - creating network interfaces
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
    - **image format**
    - **container runtime**
  - 과거 docker에 불만을 품어서, 컨테이너 표준에 대한 분쟁이 있었음
    - 표준은 무조건 합의하는게 좋다

## 2. The technical stuff

### 2.1 The Docker Engine

최신 Docker architecture

![](./images/docker_architecture2.png)

초기 Docker architecture

![](./images/original_docker_architecture1.png)

#### 1. 초기 docker

- Docker daemon
  - 개요
    - 하나의 바이너리
  - 구성
    - Docker cliient, API, container runtime, image builds, ...
- LXC
  - 개요
    - 리눅스 커널에 존재하는 fundamental container building blocks에 daemon이 접근할 수 있도록 함
      - e.g)
        - namespaces
        - control groups(cgroups)

#### 2. LXC의 제거

- 문제
  - LXC는 Linux-specific
    - multi-platform 불가능
  - 프로젝트의 코어 로직을 외부의 툴에 의존하는 것은 개발함에 있어서 매우 큰 리스크
- 해결
  - `libcontainer`의 개발
    - host OS 환경에 구애받지 않고, host kernel에 존재하는 fundamental container building blocks에 도커가 접근 할 수 있도록 함
      - *`jvm`같은 거라고 생각하면 될까?*
    - Docker 0.9에서 LXC를 대신해서 기본 execution driver로 지정됨

#### 3. monolithic Docker daemon의 제거

Docker의 모듈화와 아키텍처

![](./images/docker_architecture3.png)

- 문제
  - 모든 기능이 하나의 monolithic binary에 있어서 다음과 같은 문제가 생김
    - 새로 기능 개발하기 힘듬
    - 점점 느려짐
    - ecosystem이 원하는 방식이 아님
- 해결
  - monolithic daemon을 분리하고, 작게 모듈화 함
    - daemon에서 분리해서 교체, 재사용할 수 있는 외부 모듈로 만듬

#### 4. OCI의 spec도입

- Docker 1.11 이후, Docker engine은 OCI 스펙을 따름
  - 예시
    - daemon은 container runtime code를 포함하지 않음
      - 다른 OCI-compliant layer에 구현됨
      - default로 `runc`사용
  - `runc`
    - OCI container-runtime-spec의 참조 구현
  - `containerd`
    - 도커 이미지가 유의미한 OCI bundle로 `runc`로 제공될 수 있도록 함

#### runc

runc의 커맨드 예시

```sh
# run as root
cd /mycontainer
runc create mycontainerid

# view the container is created and in the "created" state
runc list

# start the process inside the container
runc start mycontainerid

# after 5 seconds view that the container has exited and is now in the stopped state
runc list

# now delete the container
runc delete mycontainerid
```

- `runc`
  - 개요
    - **OCI 스펙에 compatible한 create container가 메인 목적**
      - 잘하고, 빠름
      - *OCI 스펙에 따른 다는 것이 무엇을 의미하는것인가?*
        - *라이프 사이클 같은 걸까?*
    - `libcontainer`의 작고, 가벼운 CLI wrapper
      - host OS에 구애받지 않고, 커널에 존재하는 fundamental container building blocks에 도커가 접근할 수 있도록 하는 소프트웨어
    - OCI container-runtime-spec의 참조 구현체
      - OCI layer에서 동작한다고 표현 함

#### containerd

containerd 코드 예시

```go
import (
  "github.com/containerd/containerd"
  "github.com/containerd/containerd/cio"
)

// checkpoint the task then push it to a registry
checkpoint, err := task.Checkpoint(context)

err := client.Push(context, "myregistry/checkpoints/redis:master", checkpoint)

// on a new machine pull the checkpoint and restore the redis container
checkpoint, err := client.Pull(context, "myregistry/checkpoints/redis:master")

redis, err = client.NewContainer(context, "redis-master", containerd.WithNewSnapshot("redis-rootfs", checkpoint))
defer container.Delete(context)

task, err = redis.NewTask(context, cio.NewCreator(cio.WithStdio), containerd.WithTaskCheckpoint(checkpoint))
defer task.Delete(context)

err := task.Start(context)
```

- `containerd`
  - 개요
    - **container lifecycle관리**
      - main
      - start | stop | pause | rm ...
    - **image pull, volumes, networks 부착**
  - 특징
    - 도커 데몬으로부터 컨테이너 실행 로직이 분리된 것
    - Linux, Windows 두 환경에서 daemon으로서 사용가능
      - 1.11 release부터 Linux에 도입
    - **`daemon`과 `runc`사이의 OCI 레이어에 존재함**
    - 기존에는 container lifecycle관리 기능만 존재했으나, image pull, volumes, networks등의 기능도 맡게 됨
      - Kubernetes같은 다른 프로젝트에서 사용하기 쉽도록 하기 위해서 기능이 추가됨
        - Kubernetes에서 가장 잘 사용되는 container runtime
      - 대신 optional이며, 모듈화가 잘 되어있음
    - Docker회사에서 개발되었으나, CNCF에 기증됨
    - **OCI compatible container runtime에 의존해서 container를 생성가능**
      - 일반적으로 Docker에서는 `runc` 사용

#### docker daemon에 남은 기능

- 점점 더 기능이 모듈화 되는 추세
- 남은 기능
  - image management
  - image builds
  - REST API
  - authentication
  - security
  - core networking
  - orchestration
  - ...

#### `docker run ...`을 실행하면 일어나는 일들

Docker run 커맨드를 실행하면 일어나는 일들

![](./images/when_docker_run1.png)

- shim
  - 개요
    - daemonless container를 가능하게 하는 구현체
  - 컨테이너 생성 과정과 shim 존재 이유
    - `containerd`가 `runc`를 이용해서 새 컨테이너를 만듬
    - 만들 때 마다 `runc`의 새 인스턴스를 포크
    - 컨테이너가 완전히 생성되면, parent process인 `runc` 프로세스는 종료
    - 해당 컨테이너와 관련된 `containerd-shim` 프로세스가 container의 parent process가 됨
  - 역할
    - STDIN, STDOUT 스트림을 열어둬서, daemon이 재시작되어도 pipe가 닫히는 것 등으로 인한 termination을 막아줌
    - container의 exit status를 daemon으로 알려줌

#### 위와 같은 구조의 장점

- **전체 container runtime이 Docker daemon과 decouple된 상태 유지 가능**
  - `daemonless container`
  - 실행중인 container에 영향없이 Docker daemon을 upgrade하거나 maintenance가능
    - 기존에는 daemon을 시작하고 멈출 때 마다 어쩔 수 없이 모든 container들을 kill할 수 밖에 없었음
    - production 환경에서는 큰 문제

#### 리눅스에서의 구현

- `dockerd`
- `docker-containerd`
- `docker-containerd-shim`
- `docker-runc`

#### 도커 클라이언트와 데몬 사이의 커뮤니케이션

Docker client server communication

![](./images/docker_client_server_communication1.png)

- standalone(IPC)
  - Linux
    - `/var/run/docker.sock`
  - Windows
    - `//./pipe/docker_engine`
  - 그럼 standalone일 경우에는, HTTP를 사용하지 않는것인가?
    - [코드를 보아하니, 사용하는 것 같음](https://github.com/docker/cli/blob/beab92999ad3aeba9da197b8e29b1dcb3a1345f2/vendor/github.com/docker/docker/client/image_build.go#L20)
- network
  - default: HTTP
    - 2375/tcp
  - **HTTPS를 기본으로 설정해서 통신하게 할 수 있음**
