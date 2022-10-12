# Docker

## 참조

- [도커 공식 사이트](https://docs.docker.com/)

## 도커의 구성요소

### 도커의 성격

이미지나 콘테이너의 작성이나 관리를 가능하게 하는 툴

콘테이너를 베이스로한 어플리케이션 실행환경으로서의 측면(도커엔진)

### 도커의 특징

1. 리눅스 커널 위에서 Docker엔진이라는 가상화 기반이 존재. 그 엔진 위에서 어플리케이션 실행환경을 구축/가동 할 수 있다.

2. 설정 파일에 기반하여, 도커엔진에서 실행 가능한 어플리케이션 실행환경을 빠르고 자동적으로 구축 가능하다.

3. Docker hub(도커 이미지공유 사이트)

도커는 Provisioning을 지원하는 툴에서도, 부트스트래핑에속함.

> Provisioning 준비/제공/설정을 의미(오케스트레이션, 설정, 부트스트래핑)

### 활용

Build => Ship => Run

마이크로 서비스 아키텍쳐 지원

### 용어

#### 1. 이미지

- 가볍고 독립적이고 실행가능한 패키지 소프트웨어.
- 이미지는 필요한 프로그램과 라이브러리, 소스를 설치한 뒤 파일로 만든 것입니다. 이 이미지를 저장소에 올리고, 받을 수 있습니다.

#### 2. 컨테이너

- 이미지의 런타임 인스턴스(이미지를 실행한 process같은 느낌)
- 호스트 환경과는 완전히 격리된다(호스트 파일들과 포트는 접근 가능)
- 호스트의 커널에서 동작.
- 컨테이너는 이미지를 실행한 상태입니다. 이미지로 여러개의 컨테이너를 만들 수 있습니다. 운영체제로 보면 이미지는 실행파일이고 컨테이너는 프로세스입니다.

**Container vs Virtual Machine**

VM의 경우

![VM 다이어그램](./assets/vm_diagram_ex.png)

컨테이너의 경우

![컨테이너 다이어그램](./assets/container_diagram_ex.png)

### 단축키

```sh
docker pull ubuntu:14.04 # 이미지 받기
docker images # 이미지 출력하기
docker run -i -t --name hello ubuntu:14.04 /bin/bash # 컨테이너를 hello라는 이름으로 생성한뒤 bash shell실행
exit or Ctrl+D # 실행한 컨테이너에서 빠져나오기

docker ps -a # 정지된 컨테이너까지 모두 출력한다
docker start hello # 정지한 컨테이너 다시 시작하기
docker attach hello # 시작한 컨테이너 접속하기
Ctrl+P Ctrl+Q # 컨테이너를 정지하지 않고 빠져나오기

docker exec hello echo "Hello World" # 호스트에서 컨테이너 안의 명령을 실행::패키지 설치 가능
docker stop hello # 컨테이너 정지
docker ps # 컨테이너를 정지했으므로 아무것도 나오지 않음.

docker rm hello # 컨테이너 삭제
docker ps -a # 컨테이너를 삭제했으므로 아무것도 나오지 않음.

docker rmi ubuntu:<태그이름> # 이미지 삭제. 태그이름을 지정하지 않았으므로 ubuntu이름을 가진 모든 이미지가 삭제됨
docker images # 이미지를 삭제했으므로 아무것도 출력되지 않음

```

### 이미지 생성하기

Dockerfile은 Docker 이미지 설정 파일이다. Dockerfile에 설정된 내용대로 이미지를 생성한다.

```dockerfile
FROM ubuntu:14.04
MAINTAINER Foo Bar <foo@bar.com>

RUN apt-get update
RUN apt-get install -y nginx
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
RUN chown -R www-data:www-data /var/lib/nginx

VOLUME ["/data", "/etc/nginx/site-enabled", "/var/log/nginx"]

WORKDIR /etc/nginx

CMD ["nginx"]

EXPOSE 80
EXPOSE 443
```

- FROM: 어떤 이미지를 기반으로 할지 설정
- MAINTAINER: 메인테이너 정보
- RUN: Shell Script혹은 명령을 실행
  - 이미지 생성 중에는 사용자 입력을 받을 수 없으므로 apt-get install 명령에서 `-y`옵션을 사용
  - 나머지는 nginx설정
- VOLUME: 호스트와 공유할 디렉터리 목록. `docker run`명령에서 `-v`옵션으로 설정할 수 있다. e.g. `-v /root/data:/data`(호스트:컨테이너)
- CMD: 컨테이너가 시작되었을 때 실행할 실행 파일 or 스크립트
- WORKDIR: CMD에서 설정한 실행 파일이 실행될 디렉터리
- EXPOSE: 호스트와 연결할 포트 번호

### 이미지 실행하기

```sh
docker build --tag hello:0.1 . # --tag옵션으로 이미지 이름과 태그 설정 가능

## 주의!! 반드시 Dockerfile의 내용을 정확히 기술해야 한다. 틀린 곳이 있으면 제대로 실행이 되지 않는다.
docker images # Dockerfile로부터 생성된 image파일을 출력한다.
docker run --name hello-nginx -d -p 80:80 -v /root/data:/data hello:0.1 # docker compose는 이를 파일에 미리 기술해서 자동화를 도와줌 즉, 실행시의 환경설정을 미리 기술되어있는 대로 자동으로 해줌
```

- `-d`: 컨테이너를 백그라운드로 실행
- `-p 80:80`: 호스트의 80번 포트와 컨테이너의 80번 포트를 연결하고 외부에 노출한다.
- `- /root/data:/data`: 호스트의 `/root/data` 디렉터리를 컨테이너의 `/data`디렉터리에 연결

```sh
docker history hello:0.1 # hello:0.1의 히스토리를 조회 docker history <image>:<tag>
docker cp hello-nginx:/etc/nginx/nginx.conf ./ # hello-nginx 컨테이너의 /etc/nginx/nginx.conf 파일을 호스트의 현재 디렉터리에 복사
docker commit -a "Foo Bar <foo@bar.com>" -m "add hello.txt" hello-nginx hello:0.2 # -a로 커밋한 사용자 특정 -m으로 로그 메시지 설정 그리고 hello-nginx 컨테이너를 hello:0.2 이미지로 생성한다.
docker diff # 컨테이너가 실행되면서 변경된 파일 목록을 출력 A: Added C: Changed D: Deleted
docker inspect hello-nginx # 이미지와 컨테이너의 세부 정보를 출력
```

참고로 bash shell을 실행하려면 `-it`옵션을 반드시 붙여야한다.

e.g. `docker run --name containerName -it -d -p ~:~ image`

### 컨테이너 연결하기

웹 서버 컨테이너와 DB 컨테이너가 있을 때 웹 서버 컨테이너에서 DB 컨테이너에 접근할 수 있어야 한다. 이 때에는 network를 생성해서 컨테이너를 연결시킨다. 해당 네트워크 안에 속한 컨테이너 끼리는 서로 접속할 수 있다.

```sh
docker network create hello-network
docker run --name db -d --network hello-network mongo
docker run --name web -d -p 80:80 --network hello-network nginx

docker exec -it web /bin/bash # web컨테이너에 접속
ping db # db에 핑을 날려봄
```
