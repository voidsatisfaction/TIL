# 웹 어플리케이션 개발 환경을 도커라이즈 하기

보통 개발자들은 자신의 개발 환경에서 개발을 한다. 그렇게 되면 팀 개발을 할 때에 제각각의 개발환경에서 작업을 하기 때문에, `내 컴퓨터에서는 되는데...`의 딜레마에 빠지기 쉽다. 또한, 개발환경과 베포환경이 일치하지 않으면 따로 환경을 설정해줘야하는 불편함도 존재한다.

필자도 개인적인 사이드 프로젝트에서 이러한 딜레마에 빠질 것을 대비하여 웹 앱 개발환경을 프론트엔드부터 백엔드까지 완전히 도커라이징 했다. 지금부터 그 방법에 대해서 알아보도록 하자.

참고로 사용되는 기술은 이하와 같다.

- Create-React-App
- Revel framework(golang)

위의 기술들 외에도 기본적으로 `hot-reloading`이 가능한 기술들을 사용한다면 더 편리하게 도커 개발 환경을 즐길 수 있다.

## 참고

- [Docker-Compose를 이용한 개발환경 구축하기](http://ggoals.tistory.com/61)
- [Webpack and Docker for Development and Deployment](https://medium.com/@andyccs/webpack-and-docker-for-development-and-deployment-ae0e73243db4)
- [Dockerを使ったGolang開発環境](http://unknownplace.org/archives/golang-development-enviroment-with-docker.html)

## 도커화

### Dockerfile 준비

가장 먼저 컨테이너 내부의 환경을 제어할 수 있는 `Dockerfile`을 정의해준다.

웹 서버 Dockerfile

```
FROM golang:1.9.2-stretch

ENV GOPATH $GOPATH:/go

RUN apt-get update && \
    apt-get upgrade -y

# install revel and revel-cli
RUN go get github.com/revel/revel && \
    go get github.com/revel/cmd/revel

# Add our code
ADD . /go/src/near_me_server
WORKDIR /go/src/near_me_server

EXPOSE 9000

CMD sh start_server.sh
```

클라이언트 Dockerfile

```
FROM node:8.9.1

ADD . /go/src/near_me_client
WORKDIR /go/src/near_me_client
RUN npm i

CMD npm start

EXPOSE 13000
```

docker-compose.yml

```
version: "3"
services:
  web-server:
    build: .
    container_name: "near_me_server"
    ports:
      - "19000:9000"
    volumes:
      - "$PWD:/go/src/near_me_server"
    env_file:
      - "$PWD/.env"
  web-client:
    build: $PWD/../near_me_client/.
    container_name: "near_me_client"
    ports:
      - "13000:3000"
    volumes:
      - "$PWD/../near_me_client:/go/src/near_me_client"
    links:
      - web-server:web-server
```

### Client 준비

클라이언트에서는 `package.json`에 있는 proxy설정을 `docker-compose`의 서버 이름으로 호스트명을 바꿔준다.

```sh
# package.json
# 포트번호는 웹 서버 컨테이너쪽의 포트로 설정(호스트에서의 연결된 port가 아니라)
"proxy": "http://web-server:9000",
```

이렇게 설정해두면 클라이언트에서 개발 서버로 proxy를 이용해서 api를 주고 받을 수 있게 된다.

### Server 준비

`.env`가 환경변수가 들어있는 파일이다.

```sh
var1=~
var2=~
```

위와 같이 설정한다.

### 실행

```
docker-compose up
```

## 장점

1. 클라이언트 코드를 수정하면 volume설정에 의해서 컨테이너 내부의 코드도 바뀌게 되는데 여기서 `webpack-dev-server`에 의하여 코드의 수정이 자동으로 반영된다. 즉, 로컬 환경에서 코드를 수정하면 코드 수정이 컨테이너 내부로 반영이 되고, 그 결과가 hot-reload에 의하여 브라우저에도 표시된다.
2. 서버의 코드를 수정해도 위와 같이 hot-reload가 된다.
3. 개발환경과 배포환경이 일치하므로, 배포하는 것이 참 편해진다.
4. 새로운 개발자가 들어와도 docker만 설치하면 쉽게 개발 환경을 구축할 수 있다.

## 함정에 빠지기 쉬운 부분

1. revel프레임워크에서는 외부 어플리케이션과 상호작용하기 위해서 host를 `0.0.0.0`으로 설정해줘야한다.
2. 도커에서 환경변수 파일을 지정하기 위해서는 docker-compose에서는 `env_file`이라는 항목을 이용한다.
3. revel에서의 `app/tmp`, `app/routes`와 같이 자동으로 생성되는 파일은 `.dockerignore`에 지정해서 build에 포함되지 않도록 한다.
