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

### Cheat sheet

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

**몇초간의 딜레이 발생**

하지만 one-node swarm은 여전히 작동하고 있다.(`docekr node ls`)

swarm까지 종료

`docker swarm leave --force`

### Cheat sheet

```docker
docker stack ls              # List all running applications on this Docker host
docker stack deploy -c <composefile> <appname>  # Run the specified Compose file
docker stack services <appname>       # List the services associated with an app
docker stack ps <appname>   # List the running containers associated with an app
docker stack rm <appname>                             # Tear down an application
```

## Swarms

이 어플리케이션을 다수의 machines에서 작동하도록 클러스터에 배포한다.

다수의 machines을 `swarm`이라 불리는 **Dockerized** 클러스터에 합류시키므로써, 멀티 컨테이너 혹은 멀티 머신 어플리케이션을 만들 수 있다.

### Swarm clusters의 이해

swarm이란, 클러스터에 합류된 도커를 실행하는 기계의 그룹을 말한다.

클러스터에서 `swarm manager`로 실행.

`swarm`에 속한 기계들은 물리적일 수 있고 가장적일 수 있다.

`swarm`에 포함된 이후로는 `nodes`로서 참조.

Swarm manager는 여러가지 방법으로 컨테이너들을 실행할 수 있는데, "empiest node", "global" ... 등이 있다. Swarm manager는 이러한 방식들을 Compose file을 이용해서 작동할 수 있게 한다.

Swarm manager는 swarm에서 명령들을 실행할 수 있는 유일한 기계이며 혹은 다른 기계들이 swarm에 `workers`로서 참여할 수 있게한다.

지금까지는 Docker를 `single-host mode로` 사용했는데, Docker는 `swarm mode`로 변경 가능하다.

### 1. Swarm의 설정

swarm 모드 사용 + 현재의 machine을 swarm manager로 한다.

`docker swarm init`

다른 worker가 될 machine에서는 그 swarm에 join한다.

`docker swarm join`

**가상 머신을 이용한 예제**

VirtualBox driver를 이용하여 도커 가상머신을 생성한다.

`docker-machine create --driver virtualbox myvm1` manager
`docker-machine create --driver virtualbox myvm2` worker

docker-machine확인

`docker-machine ls`

docker-machine에 명령 보내기

`docker-machine ssh myvm1 "docker swarm init"`

**여기서 결과로 나온 내용 저장**

docker-machine2를 docker-machine1의 swarm에 worker로 등록하기

`docker-machine ssh myvm2`

`docker swarm join ...(위에서 저장한 내용 붙여넣기) `

### 2. 배포하기

`docekr-machine ssh myvm1 "docker stack deploy -c docker-compose.yml getstartedlab"`

`docker-machine ssh myvm1 "docker stack ps getstartedlab"`

...결과 표시

### Cheat Sheet

```
docker-machine create --driver virtualbox myvm1 # Create a VM (Mac, Win7, Linux)
docker-machine create -d hyperv --hyperv-virtual-switch "myswitch" myvm1 # Win10
docker-machine env myvm1                # View basic information about your node
docker-machine ssh myvm1 "docker node ls"         # List the nodes in your swarm
docker-machine ssh myvm1 "docker node inspect <node ID>"        # Inspect a node
docker-machine ssh myvm1 "docker swarm join-token -q worker"   # View join token
docker-machine ssh myvm1   # Open an SSH session with the VM; type "exit" to end
docker-machine ssh myvm2 "docker swarm leave"  # Make the worker leave the swarm
docker-machine ssh myvm1 "docker swarm leave -f" # Make master leave, kill swarm
docker-machine start myvm1            # Start a VM that is currently not running
docker-machine stop $(docker-machine ls -q)               # Stop all running VMs
docker-machine rm $(docker-machine ls -q) # Delete all VMs and their disk images
docker-machine scp docker-compose.yml myvm1:~     # Copy file to node's home dir
docker-machine ssh myvm1 "docker stack deploy -c <file> <app>"   # Deploy an app
```

## Stack

stack이란, interrelated인 services의 의존성을 공유하는 그룹이다. 그리고 같이 orchestrated하고 scaled된다.

하나의 `stack`은 전체 어플리케이션의 기능을 정의하고 조화시킬 수 있다(매우 복잡한 어플리케이션은 다양한 stack을 사용할 수 있다)

### 새로운 service와 재베포

`docker-compose.yml`을 다음과 같이 추가하고, deploy한다.

```yml
version: "3"
services:
  web:
    # replace username/repo:tag with your name and image details
    image: username/repo:tag
    deploy:
      replicas: 5
      restart_policy:
        condition: on-failure
      resources:
        limits:
          cpus: "0.1"
          memory: 50M
    ports:
      - "80:80"
    networks:
      - webnet
  visualizer:
    image: dockersamples/visualizer:stable
    ports:
      - "8080:8080"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
    deploy:
      placement:
        constraints: [node.role == manager]
    networks:
      - webnet
networks:
  webnet:
```

### 데이터 베이스 추가

```yaml

version: "3"
services:
  web:
    # replace username/repo:tag with your name and image details
    image: username/repo:tag
    deploy:
      replicas: 5
      restart_policy:
        condition: on-failure
      resources:
        limits:
          cpus: "0.1"
          memory: 50M
    ports:
      - "80:80"
    networks:
      - webnet
  visualizer:
    image: dockersamples/visualizer:stable
    ports:
      - "8080:8080"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
    deploy:
      placement:
        constraints: [node.role == manager]
    networks:
      - webnet
  redis:
    image: redis
    ports:
      - "6379:6379"
    volumes:
      - ./data:/data
    deploy:
      placement:
        constraints: [node.role == manager]
    networks:
      - webnet
networks:
  webnet:

```

## 어플리케이션 베포

도커 클라우드와 연결

swarm생성

앱 베포
