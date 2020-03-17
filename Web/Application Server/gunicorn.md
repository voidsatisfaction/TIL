# Gunicorn

## 의문

- *pre-fork worker 모델이 뭐야, 다른 모델은 뭐가 있지?*

## 개요

- Python WSGI HTTP Server **for Unix**
- *pre-fork worker 모델*

## Design

- Server Model

### Server Model

- 기반
  - pre-fork worker model
    - master process가 중심에 있고, worker process의 집합을 관리함
    - master는 개별 clients에 대해서 전혀 정보를 갖지 않음
      - 모든 request / response는 worker process들이 관리함
