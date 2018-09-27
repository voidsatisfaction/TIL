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

### 프록시 서버

```
server {
  location / {
      proxy_pass http://localhost:8080/;
  }

  location ~ \.(gif|jpg|png)$ {
    root /data/images;
  }
}
```

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
