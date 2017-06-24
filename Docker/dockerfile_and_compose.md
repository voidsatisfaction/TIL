# Dockerfile and docker-compose.yml

## 차이점

The Compose file describes the container in its running state, leaving the details on how to build the container to Dockerfiles. http://deninet.com/blog/1587/docker-scratch-part-4-compose-and-volumes

- Dockerfile: 만들고자 하는 어플리케이션의 각각의 구성요소설치에 필요한 정보들을 자세히 기술.
- docker-compose.yml: 각각의 구성요소들을 서로 링킹하게 하여 어플리케이션을 구현.
