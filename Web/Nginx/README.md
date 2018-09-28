# Nginx기초

- Nginx란
- Nginx 설정 파일의 구조
- 기능 예시

참고: https://nginx.org/en/docs/beginners_guide.html

## Nginx란

- 서버
  - HTTP
  - Reverse Proxy
  - Mail Proxy
  - UDP / TCP Proxy
- 구성
  - master process
    - 설정 파일 관리
    - 워커 프로세스 관리
  - worker process

## Nginx 설정 파일의 구조

- 지시(directives)
  - 단순 지시(simple directives)
    - 이름 파라미터;
  - 블록 지시(block directives)
    - 컨텍스트
      - 블록 지시 속에 다양한 다른 지시들을 갖는 경우
      - 다른 모든 컨텍스트의 밖에 놓인 지시들은 `main context`속에 있다고 생각할 수 있음
      - `events`, `http` 지시들은 `main` 컨텍스트에 있고, `server`는 `http`안에, `location`은 `server`안에 존재
    - `#`는 커멘트

## 기능 예시

### 정적 컨텐츠 제공

- 웹 서버의 중요한 기능 중 하나
- 설정 파일은 여러개의 포트 번호와 이름으로 구별되는 서버 블록을 갖고 있을 수 있음

```
http {
  server {
    location / {
      root /data/www;
    }

    location /images/ {
      root /data;
    }
  }
}
```

- `http://localhost/images/example.png`에 대한 응답은 `/data/images/example.png`이다.
  - 파일이 존재하지 않으면 404에러 돌려줌
- `/images/`로 uri가 시작하는 경우
  -  `http://localhost/some/example.html`에 대한 응답은 `/data/www/some/example.html`파일이다.
- 설정을 바꾼다음에는 재시작 해야함
  - `nginx -s reload`

### 프록시 서버

- 요청(request)을 받고, 그것을 프록시된 서버에 넘겨주고, 프록시된 서버로부터 응답을 받고, 다시 그것을 클라이언트로 보냄

```
# 서버
server {
  listen 8080;
  root /data/upl;

  location / {

  }
}

# 리버스 프록시 서버
server {
  location / {
      proxy_pass http://localhost:8080/;
  }

  location ~ \.(gif|jpg|png)$ {
    root /data/images;
  }
}
```

- 서버
  - 포트 8080에서 요청 대기(초기 설정은 80)
  - 모든 요청을 `/data/upl`로 매핑
- 프록시 서버
  - 요청에 대한 응답은 prefix가 긴 location부터 참조
  - 정규 표현식은 ~ 뒤에 나온다.
  - `.gif` `.jpg` `.png`파일들을 `/data/images` 디렉터리로 매핑함
  - 그 외의 다른 요청들은 리버스 프록시된 서버로 보냄

### Fast CGI 프록시

```
server {
    location / {
        fastcgi_pass  localhost:9000;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param QUERY_STRING    $query_string;
    }

    location ~ \.(gif|jpg|png)$ {
        root /data/images;
    }
}
```
