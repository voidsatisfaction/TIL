# 도커

## 도커란

## 팁

### EXPOSE와 PUBLISH의 차이

- EXPOSE / PUBLISH(-p) 둘다 하지 않는 경우
  - 컨테이너 안 서비스는 오직 그 컨테이너 안에서만 접근 가능
- EXPOSE 만 설정
  - 컨테이너 사이에서 접근 가능
- EXPOSE PUBLISH 둘다 설정
  - 다른 컨테이너 뿐 아니라, 도커 환경 밖에서도 접근 가능
