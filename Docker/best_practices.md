# Docker developement best practices

- 의문
- How to keep your images small
- Where and how to persist application data
- Best practices for writing Dockerfiles
  - Dockerfile instructions
- Prune unused Docker objects

## 의문

## How to keep your images small

- 적절한 베이스 이미지 사용
- **multistage build를 사용**
  - multistage build
    - 개요
      - 하나의 도커 파일에서 이미지를 넘나들며 artifact들을 전달하고 받아서 사용하는 방식
- 이미지의 레이어 수 줄이기
  - before
    - `RUN apt-get -y update`
    - `RUN apt-get install -y python`
  - after
    - `RUN apt-get -y update && apt-get install -y python`
  - 참고
    - 사실, 단순히 위의 예시는 레이어만 줄이는 것이 아니고, 항상 `apt-get` repository가 설치하는 패키지가 바뀔 때마다 최신으로 유지할 수 있게 함
- **공통 레이어를 공유하는 다수의 이미지는 base image를 만들어서 공유함**
  - 도커는 common layer를 만들어두면, 그것을 캐싱해서 사용함
- production image를 base image로 두고, testing, debugging tool 을 그 이미지 위에다가 올려서 진행하라
- 이미지를 생성할 때는, `prod`, `test`등과 같이 제대로 태깅하라

## Where and how to persist application data

결론: writable layer에 데이터를 저장하지 말고, volume을 사용하라

- **application data를 storage driver를 사용해서 writable layer에 저장하는 것을 피해야 함**
  - 컨테이너 사이즈 증가 & volumes, bind mounts를 사용하는 것 보다 I/O 관점에서 비효율
  - *컨테이너 안에 volume mount되지 않은 디렉터리에 application data를 두지 말라는 것인가?*
- bind mounts는 developement 모드일때만 사용
  - *bind mounts* 가 뭐지?
- `secrets`를 sensitive application data를 저장하는데에 사용
- `configs`를 sensitive 하지 않은 데이터를 저장하는데에 사용

## Best practices for writing Dockerfiles

*정리가 끝나고, 중요한 순서대로 재배치*

- Create ephemeral container
  - 셋업과 configuration없이 컨테이너가 언제든 멈추고, 파괴되고, 다시 만들어지고 대체될 수 있도록 Dockerfile을 작성하라
  - stateless 해야함
- Understand build context
  - `Dockerfile`의 위치에 상관없이 `-f` 옵선을 지정하여, build context를 지정 가능
    - 선택된 디렉터리로부터 재귀적으로 모든 파일과 디렉터리를 Docker daemon에게 build context로 제공
  - 필요없는 파일들이 build context에 포함되지 않도록 해야함
    - 이미지 build하는 시간이 증가
    - pull, push하는 시간이 증가
    - runtime size의 증가
    - `.dockerignore` 작성
- Exclude with `.dockerignore`
  - build context를 docker daemon에 보내기 전에 context에서 제거할 파일들을 제거함
- **Use multi-stage builds**
  - 최종 이미지의 크기를 매우 많이 줄일 수 있는 방법
- Decouple applications
  - **각 컨테이너는 하나의 관심사만 처리할 수 있어야 함**
    - horizontal scalability
    - reusability
- Layer의 수를 최소화 하라
  - 현재는 매커니즘상 많이 개선이 됨
    - `RUN`, `COPY`, `ADD` instruction만 레이어를 생성. 다른 instruction들은 임시 중간 이미지들을 생성하고, 빌드의 사이즈를 키우지 않음
    - 웬만하면 `multi-sage builds`를 사용해서 artifacts만 final image로 복사해오자
- Leverage build cache
  - 주의) 캐시가 invalidated되는 경우
    - `ADD`, `COPY` instruction의 경우, 이미지에 있는 파일들의 내용이 검사되고, 체크섬이 각 파일마다 계산됨. 최종 수정, 최종 엑세스 시간은 체크섬의 고려대상이 아님. 체크섬이 존재하는 이미지의 체크섬과 비교가 되고, 파일의 수정이 있는 경우에는 캐시가 invalidate됨
    - `ADD`, `COPY` 이외의 instruction의 경우에는, 그것으로 인해 생성되는 파일이 아니고, 명령어가 같은지만 체크해서 캐시를 사용할지 안할지를 정함
  - 한 번 cache가 invalidated되면, 그 다음 `Dockerfile`의 커맨드들은 새 이미지를 생성하고 캐시가 사용되지 않음
- Build an image using a dockerfile from stdin, without sending build context
  - `docker build [OPTIONS] -`
  - 파일 copy를 하지 않을 때 유용함
- Build from a local build context, using a dockerfile from stdin
  - `docker build [OPTIONS] -f- PATH`
- Build from a remote build context, using a dockerfile from stdin
  - `docker build [OPTIONS] -f- PATH`
  - e.g)
    - `docker build -t myimage:latest -f- https://github.com/docker-library/hello-world.git <<EOF`
      - `FROM busybox`
      - `COPY hello.c .`
      - `EOF`
      - 외부의 git repository를 build context로 두면, docker는 `git clone`을 행한뒤에, daemon에 build context를 넘겨줌
- Sort multi-line arguments
  - 알파벳 순서대로
  - `\` 활용

### Dockerfile instructions

- `FROM`
  - official image를 사용하자
  - Alpine image가 매우 작아서 추천
- `LABEL`
  - docker object에 메타데이터 부여
- `RUN`
  - `\`를 이용해서 멀티라인으로 분리하자
- `APT-GET`
  - `apt-get upgrade`, `dist-upgrade` 회피하는 것이 좋음
    - `unprivileged container` 에서는 parent image의 essential packages를 업그레이드 할 수 없기 때문
  - `apt-get update`와 `apt-get install`은 반드시 결합해서 사용하라
    - `apt-get update`가 캐싱되어서 업데이트가 되지 않음
    - cache busting을 사용함
- `EXPOSE`
  - 컨테이너가 연결을 위해서 listen하는 포트를 나타냄
- `ADD`, `COPY`
  - `COPY`가 더 바람직함
    - COPY는 오직 복사만 하기 때문
  - `ADD`
    - 복사
    - tar파일의 auto-extraction을 이미지에 함
      - remote URL support도 존재
- `ENTRYPOINT`
  - image의 메인 command를 지정
    - 이 경우 `CMD`는 default flag를 지정
    - e.g)
      - 설정
        - `ENTRYPOINT ["s3cmd"]`
        - `CMD ["--help"]`
      - 실행
        - `docker run s3cmd`
- `USER`
  - 서비스가 루트 권한 없이 동작 가능하다면, `USER`를 사용해서 non-root user로 변경해서 사용하라
  - `sudo`를 사용하는 대신, `gosu`를 사용하라
- `WORKDIR`
  - `WORKDIR`은 절대 경로로 지정하라(explicit)
  - `RUN cd ... && do-something` 대신 `WORKDIR`을 사용하라
    - 메인테이닝 하기 쉬움

## Prune unused Docker objects

- 개요
  - docker는 docker object를 명령을 받기 전까지는 prune하지 않음
  - e.g command)
    - `docker image prune`
    - `docker system prune`
- Prune images
  - 개요
    - docker image는 별도로 명령을 받기 전까지 지워지지 않음
  - 명령
    - `docker image prune`
      - dangling image만 제거
        - not tagged, not referenced by any container
    - `docker image prune -a`
      - 사용되지 않는 이미지 전부 제거
    - `docker image prune -a --filter "until=24h"`
      - 24시간 이상된 이미지 중에서만 prune함
- Prune container
  - 개요
    - container를 stop하면 자동적으로 지워지지 않음
    - stopped container의 writable layer는 여전히 디스크 공간을 차지함
    - `docker container prune ..` 으로 해당 공간 청소 가능
  - 명령
    - `docker container prune`
      - stop된 컨테이너 제거
    - `docker container prune --filter "until=24h"`
      - 24이상된 stop 컨테이너만 prune함
- Prune volumes
  - 개요
    - volume은 host의 공간을 차지하며, 자동적으로 지워지지 않음(데이터 파괴 방지)
  - 명령
    - `docker volume prune`
    - `docker volume prune --filter "label!=keep"`
      - `keep`이라는 레이블이 달려지지 않은 볼륨만 제거
- Prune networks
  - 개요
    - docker network는 많은 디스크 공간을 차지하지 않으나, `iptables` 룰을 생성하고, 브릿지 네트워크 디바이스와 라우팅 테이블 entries를 생성함
  - 명령
    - `docker network prune`
      - 어떠한 컨테이너도 사용하고 있지 않은 네트워크를 prune함
    - `docker network prune --filter "until=24h"`
- Prune all
  - 명령
    - `docker system prune`
      - images, containers, networks를 전부 prune
    - `docker system prune --volumes`
      - + volumes까지 prune
