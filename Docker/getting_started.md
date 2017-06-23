# Docker Getting Started

## 계층

1. Container
2. Services
3. Stack

## Container

### 1. 컨테이너를 Dockerfile에 정의하라

Dockerfile은 portable이미지로서, 어떠한 프로그램의 런타임을 이미지로 가지고 있다.

컨테이너 안의 환경을 `Dockerfile`로 정의한다.

도커파일로 생성된 컨테이너는 다른 기존의 시스템과 격리됨과 동시에 `networking interfaces`나 `disk drive`등을 사용할 수 있으며, 외부 세계와 연결하기 위해서 `port`설정을 따로 해주어야 한다.

```docker
# Use an official Python runtime as a base image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

### 2. app그 자체를 정의하라

앞서 정의한 Dockerfile에서 `app.py`랑 `requirements.txt`를 정의하라.

그러면 `Dockerfile`의 `ADD`명령으로 인하여 파일이 컨테이너에 추가가 될 것이고,

`app.py`는 `EXPOSE`명령으로 인하여 HTTP통신이 가능해진다.

`requirements.txt`

```txt
Flask
Redis
```

`app.py`

```python
from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

### 3. app을 build하라

`docker build -t friendlyhello(이름)`

`docker images`

### 4. app을 실행하라

호스트의 4000포트를 컨테이너의 EXPOSE된 포트 80으로 매핑한다(-p)

`docker run -p 4000:80 friendlyhello`

백그라운드로 docker app을 실행하기

`docker run -d -p 4000:80 friendlyhello`

현재 background로 돌아가고 있는 컨테이너 확인

`docker ps`

컨테이너 정지

`docker stop 컨테이너아이디`

### 5. image를 공유하라

registries > repository > images

1. docker CLI로 올릴 수 있음.

`docker login`

2. 태그와 다른 파일들을 다 합쳐서 하나의 이미지로 만든다.

`docker tag image username/repository:tag`

3. docker hub에 repository업로드

`docker push username/repository:tag`

docker hub에 접속하면 새로운 이미지를 확인할 수 있다.

4. docker hub에서 이미지를 가져온 후 실행하기

`docker run -p 4000:80 username/repository:tag`

(이미 이미지가 존재한 경우 그것을 실행)

> :tag를 명시하지 않는 경우, 가장 마지막 버전의 이미지를 사용한다(latest)

## Cheat sheet

```docker
docker build -t friendlyname .  # Create image using this directory's Dockerfile
docker run -p 4000:80 friendlyname  # Run "friendlyname" mapping port 4000 to 80
docker run -d -p 4000:80 friendlyname         # Same thing, but in detached mode
docker ps                                 # See a list of all running containers
docker stop <hash>                     # Gracefully stop the specified container
docker ps -a           # See a list of all containers, even the ones not running
docker kill <hash>                   # Force shutdown of the specified container
docker rm <hash>              # Remove the specified container from this machine
docker rm $(docker ps -a -q)           # Remove all containers from this machine
docker images -a                               # Show all images on this machine
docker rmi <imagename>            # Remove the specified image from this machine
docker rmi $(docker images -q)             # Remove all images from this machine
docker login             # Log in this CLI session using your Docker credentials
docker tag <image> username/repository:tag  # Tag <image> for upload to registry
docker push username/repository:tag            # Upload tagged image to registry
docker run username/repository:tag                   # Run image from a registry
```

## Services

어플리케이션의 scale과 load-balancing

### 정의

containers in production

one service === one image 작동

이미지가 작동하는 방식 + 어떠한 포트가 사용되는가 + 얼마나 많은 복제 컨테이너가 작동돼야 하는가

=> 전부 `docker-compose.yml`파일에서 정의

### `docker-compose.yml`파일

`docker-compose.yml`파일은 어떻게 Docker 컨테이너들이 production에서 행동해야 하는지 정의한 것이다.

**docker-compose.yml**

```yaml
version: "3"
services:
  web:
    # replace username/repo:tag with your name and image details
    image: nersery/get-started:part1
    deploy:
      replicas: 5
      resources:
        limits:
          cpus: "0.1"
          memory: 50M
      restart_policy:
        condition: on-failure
    ports:
      - "80:80"
    networks:
      - webnet
networks:
  webnet:
```

### load-balanced app실행하기

반드시 설정

`docker swarm init`

app에다가 이름을 지정.

`docker stack deploy -c docker-compose.yml getstartedlab`

**10여초 정도의 시간이 걸리므로 주의!!**

내가 방금 실행한 다섯 컨테이너의 리스트를 보여줌.

`docker stack ps getstartedlab`

== `docker ps`

localhost를 방문

`curl http://localhost`

### app scale하기

먼저, `docker-compose.yml`안의 replicas의 값을 바꾼다.

그리고 `docker stack deploy -c docker-compose.yml getstartedlab` 실행

### app 종료하기

`docker stack rm getstartedlab`

하지만 one-node swarm은 여전히 작동하고 있다.(`docekr node ls`)

swarm까지 종료

`docker swarm leave --force`
