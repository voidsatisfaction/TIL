# 도커

- 도커 기초
  - 도커의 역사
  - 도커란
  - 컨테이너
  - 이미지
  - 핫한 이유
- 도커 실습
  - (참고)도커 커맨드
  - 도커 구성
  - 도커 실습
  - 도커 기본 명령어
  - 컨테이너 업데이트
  - Docker Compose
- 도커 이미지 만들고 배포하기
- 팁

## 도커 기초

### 도커의 역사

- [The future of Linux Containers - 2013년 3월](https://www.youtube.com/watch?v=wW9CAH9nSLs&feature=youtu.be)

### 도커란

- 정의
  - 컨테이너 기반의 오픈소스 가상화 플랫폼
    - 도커는 리눅스컨테이너 기반
- 서버 개발
  - 다양한 프로그램, 실행환경을 컨테이너로 추상화하고 동일한 인터페이스를 제공하여 프로그램의 배포 및 관리를 단순하게 해줌

### 컨테이너

![](./assets/vm-vs-docker.png)

- 정의
  - 격리된 공간에서 프로세스가 동작하는 기술
    - *여기에서 격리된 공간의 정의?*
- 기존의 가상화 기술과의 차이
  - 기존
    - OS의 가상화(전가상화)
      - HOST OS위에 GUEST OS를 둠
      - 사용법은 간단하나 무겁고 느림
      - 반가상화 방법도 생겼으나, 여전히 무겁고 느림
  - 리눅스 컨테이너
    - 프로세스의 격리
      - *프로세스의 격리의 정확한 의미는? - 프로세스를 격리했는데 어떻게 새로운 OS(?)처럼 행동할 수 있는가?*
      - CPU나 메모리는 딱 프로세스가 필요한 만큼만 추가로 사용
      - 성능적 손실이 거의 없음

### 이미지

- 정의
  - 컨테이너 실행에 필요한 파일과 설정값등을 포함하고 있는 것
- 특징
  - 상태 값을 가지지 않고 변하지 않음(immutable)
  - 컨테이너는 이미지를 실행한 상태
    - 추가되거나 변하는 값은 컨테이너에 저장
  - 컨테이너 실행을 위한 모든 정보를 갖고 있으므로, 의존성 파일을 컴파일하고 이것저것 설치할 필요가 없음
  - Docker hub / registry 저장소를 직접 만들어 관리할 수 있음
- 예시
  - ubuntu이미지
    - ubuntu를 실행하기 위한 모든 파일을 가지고 있음
  - MySQL이미지
    - debian을 기반으로 MySQL을 실행하는데 필요한 파일과 실행 명령어, 포트 정보등을 가지고 있음
- 이미지 경로
  - url방식으로 관리

### 핫한 이유

![](./assets/docker_image_url.png)

- 레이어 저장방식
  - 컨테이너 실행하기 위한 모든 정보는 수백메가에 이르나, "레이어" 개념을 도입하여, 여러개의 레이어를 하나의 파일 시스템으로 이용할 수 있게 해줌
    - 하나의 파일 시스템으로 이용할 수 있게 해줌이라는게 정확히 무슨 말인가?
      - 레이어들을 다 결합해서 하나의 컨테이너를 하나의 파일 시스템으로 구성되었다고 생각할 수 있는 것
  - 기존에 다운로드 받아놓은 레이어를 다른 이미지를 만들 때 재활용 할 수 있게 해줌
    - 이미지 = 레이어로 구성
  - 컨테이너 생성시에도 레이어 활용
    - 기존의 이미지 레이어 위에 R/W(읽기/쓰기) 레이어를 추가
    - 이미지 레이어를 그대로 사용하면서, 컨테이너가 실행중에 생성하는 파일이나 변경된 내용은 R/W레이어에 저장
- Dockerfile
  - 의존성 관리를 쉽게
- Docker Hub
- Command API
  - 알기 쉬움
- 새로운 기능들이 빠르게 추가
- 훌륭한 생태계
- 커뮤니티 지원

## 도커 실습

### (참고)도커 커맨드

[도커 커맨드](https://docs.docker.com/engine/reference/commandline/docker/)

### 도커의 구성

![](./assets/docker_structure.png)

- 클라이언트 서버 구성
  - 클라이언트
    - `docker command`를 docker-daemon으로 보냄
  - 서버
    - 받은 도커 커맨드를 실행하고 다시 client쪽으로 보냄

### 도커 실습

- `dockefr run ubuntu:16.04`
  - 도커 이미지를 다운받고 컨테이너 실행
  - 컨테이너는 실행했으나, 명령어가 없으므로 컨테이너가 생성되자마자 종료
  - 컨테이너 = 프로세스
    - 더 이상 실행할 프로그램이 없다면 컨테이너는 종료

### 도커 기본 명령어

- `docker run`
  - 컨테이너 실행
- `docker ps`
  - 컨테이너 목록 확인
- `docker stop`
  - 실행중인 컨테이너 중지
  - 컨테이너는 종료되어도 삭제되지 않고 그대로 남아있음
  - (팁)중지된 컨테이너 모두 삭제하기
    - `docker rm -v $(docker ps -a -q -f status=exited)`
- `docker images`
  - 도커 이미지 목록 확인
- `docker pull`
  - 도커 이미지 다운로드
- `docker rmi`
  - 도커 이미지 삭제
- `docker logs`
  - 컨테이너 로그 보기
  - 도커는 표준 스트림중 stdout, stderr를 수집
    - 따라서 컨테이너에서 실행되는 프로그램의 로그 설정을 파일이 아닌 표준출력으로 바꾸어야 함
  - 컨테이너의 로그 파일은 json 방식으로 어딘가에 저장이 됨
    - 로그가 많으면 파일이 차지하는 용량이 커지므로 주의
    - 플러그인으로 json이 아닌, 특정 로그 서비스에 스트림을 전달하도록 하는것이 바람직
- `docker exec`
  - 실행중인 컨테이너에서 명령어 실행하기
    - ssh 쓰지 말자

### 컨테이너 업데이트

- 이미지 다운 -> 기존 컨테이너 삭제 -> 새 컨테이너 실행
  - 이때에, 데이터 유지가 중요(컨테이너 외부로 격리)
    - 1: 클라우드 서비스(S3)
    - 2: 데이터 볼륨(마운트)

### Docker Compose

- 컨테이너 조합이 많아지고 여러가지 설정이 추가되면 명령어가 금방 복잡해지는데 그것을 쉽게 제어할 수 있는 도구

```docker
virsion: '2'

services:
  db:
    image: mysql:5.7
    volumns:
      - db_data:/var/lib/mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: wordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress

  wordpress:
    depends_on:
      - db
    image: wordpress:latest
    volumns:
      - wp_data:/var/www/html
    ports:
      - "8000:80"
    restart: always
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_PASSWORD: wordpress
volumns:
  db_data:
  wp_data:
```

## 도커 이미지 만들고 배포하기

### 도커 이미지 만들기

![](./assets/dockerfile1.png)

- 도커 이미지 만들기
  - 도커는 이미지를 만들기 위해, **컨테이너 상태를 그대로 이미지로 저장** 하는 방법을 사용
    - 콘솔에서 명령어를 직접 입력하는 것과 별 차이가 없음
  - Dockerfile이라는 DSL을 사용

```dockerfile
FROM ubuntu:16.04
MAINTAINER yeongyumin@vuno.co
RUN apt-get -y update

RUN apt-get -y install ruby
RUN gem install bundler

COPY . /usr/src/app

WORKDIR /usr/src/app
RUN bundle install

EXPOSE 4567
CMD bundle exec ruby app.rb -o 0.0.0.0
```

- Dockerfile의 기본 명령어
  - FROM
    - 베이스 이미지 지정
  - MAINTAINER
    - Dockerfile을 관리하는 사람의 이름 또는 이메일 정보
  - COPY
    - 파일이나 디렉토리를 이미지로 복사
    - target 디렉토리가 없으면 자동으로 생성
  - ADD
    - COPY + src에 URL 입력 가능 + src에 압축 파일을 입력하면 자동으로 압축을 해제하면서 복사됨
  - RUN
    - 명령어를 그대로 실행 `/bin/sh -c` 뒤에 명령어를 실행하는 방식
  - CMD
    - 도커 컨테이너가 실행되었을 때 실행되는 명령어를 정의
    - 여러개의 CMD가 있으면 마지막 CMD만 실행됨
  - WORKDIR
    - RUN / CMD / ADD / COPY 등이 이루어질 기본 디렉토리를 설정
  - EXPOSE
    - 도커 컨테이너가 실행되었을 떄 Listen하고 있는 포트를 지정
  - VOLUMN
    - 컨테이너 외부에 파일시스템을 마운트 할 때 사용
  - ENV
    - 컨테이너에서 사용할 환경 변수를 지정
    - 컨테이너 실행할 때, `-e`옵션을 사용하면 기존 값을 오버라이딩 함

### 빌드 만들기

```
Sending build context to Docker daemon  5.12 kB   <-- (1)
Step 1/10 : FROM ubuntu:16.04                     <-- (2)
 ---> f49eec89601e                                <-- (3)
Step 2/10 : MAINTAINER subicura@subicura.com      <-- (4)
 ---> Running in f4de0c750abb                     <-- (5)
 ---> 4a400609ff73                                <-- (6)
Removing intermediate container f4de0c750abb      <-- (7)
Step 3/10 : RUN apt-get -y update                 <-- (8)
...
...
Successfully built 20369cef9829                   <-- (9)
```

- 빌드 별 설명
  - (1)
    - 빌드 명령어를 실행한 디렉토리의 파일들(build context)을 도커 서버(daemon)로 전송
  - (2)
    - 명령어 한줄한줄 수행
    - 이미지 다운
  - (3)
    - 명령어 수행 결과를 이미지로 저장
  - (5)
    - 명령어를 수행하기 위해 바로 이전에 생성된 f49eec89601e이미지를 기반으로 f4de0c750abb 컨테이너를 임시로 생성하여 실행
  - (6)
    - 명령어 수행 결과를 이미지로 저장
      - *근데 그냥 생성된 f4de0c750abb로 이미지 저장하면 되지 왜 또 따로 4a400609ff73을 만들어서 저장하는가?*
  - (7)
    - 임시로 만들었던 컨테이너 제거
- 빌드 분석
  - **기존의 새 이미지에서 임시 이미지 생성 -> 임시 이미지에서 커맨드 실  -> 성공 -> 임시 이미지 삭제 -> 새 이미지 생성**
    - 이렇게 하면, 각각 step에서 이미지가 생성되어있으므로, Dockerfile의 변경된 부분만 새로 이미지를 생성해주면 됨

### 도커 이미지 리팩토링

- Base Image
  - `FROM ubuntu:16.04 -> FROM ruby:2.6`
- Build Cache
  - 이미지를 빌드하는 과정에서 각 단계를 이미지 레이어로 저장하고 다음 빌드에서 캐시로 이용
  - 그러므로 최대한 캐시가 안깨지게 Dockerfile을 설계하는 것이 중요
  - 예시

```
# before
COPY . /usr/src/app    # <- 소스파일이 변경되면 캐시가 깨짐
WORKDIR /usr/src/app
RUN bundle install     # 패키지를 추가하지 않았는데 또 인스톨하게 됨 ㅠㅠ

# after
COPY Gemfile* /usr/src/app/ # Gemfile을 먼저 복사함
WORKDIR /usr/src/app
RUN bundle install          # 패키지 인스톨
COPY . /usr/src/app         # <- 소스가 바꼈을 때 캐시가 깨지는 시점 ^0^
```

- 명령어 최적화
  - 불필요한 로그는 무시
  - 문서 파일 생성할 필요가 없음

```
# before
RUN apt-get -y update

# after
RUN apt-get -y -qq update

#######

# before
RUN bundle install

# after
RUN bundle install --no-rdoc --no-ri # 필요없는 문서 생성(x) 이미지 용량 줄임
```

- 이쁘게
  - 명령어는 비슷한 것끼리 묶어주는게 레이어 수를 줄이는 데에 도움이 됨
  - 도커 엔진에 따라서 레이어 개수가 127개로 제한되는 경우도 있음

```
#before
RUN apt-get -y -qq update
RUN apt-get -y -qq install ruby

# after
RUN apt-get -y -qq update && \
    apt-get -y -qq install ruby
```

Dockerfile 개선 결과

```
FROM ruby:2.6
MAINTAINER lourie@naver.com

COPY Gemfile* /usr/src/app/
WORKDIR /usr/src/app

RUN bundle install --no-rdoc --no-ri

COPY . /usr/src/app

EXPOSE 4567

CMD bundle exec ruby app.rb -o 0.0.0.0
```

### 이미지 저장소

![](./assets/docker_registry1.png)

- 이미지 저장소
  - 도커 레지스트리
    - push & pull
    - 오픈소스
  - 도커 허브
      - 이미지 무료 저장
  - docker cloud
    - 유료 클라우드
  - private docker registry
    - `docker run -d -v $PWD/registry:/var/lib/registry -p 5000:5000 distribution/registry:2.6.0`
- 보안
  - 도커 레지스트리는 일반적으로 HTTP 프로토콜을 사용해서 이미지를 전송하는데, HTTPS를 사용하지 않으면 이미지 내용이 유출될 수 있음

## 배포하기

- 이미지 다운 후 컨테이너 실행
  - 끝

![](./assets/docker_update1.png)

- 업데이트
  - 최신 이미지로 새 컨테이너 만들고 이전 컨테이너 삭제
- 복잡한 서버 관리
  - 가상네트워크, 공유 파일, 로그관리, CPU나 메모리 자원 분배 고민
  - service discovery
  - orchestration

## 팁

### EXPOSE와 PUBLISH의 차이

- EXPOSE / PUBLISH(-p) 둘다 하지 않는 경우
  - 컨테이너 안 서비스는 오직 그 컨테이너 안에서만 접근 가능
- EXPOSE 만 설정
  - 컨테이너 사이에서 접근 가능
- EXPOSE PUBLISH 둘다 설정
  - 다른 컨테이너 뿐 아니라, 도커 환경 밖에서도 접근 가능
