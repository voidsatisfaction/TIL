# Nginx기초

- Nginx란
- Nginx 설정 파일의 구조
  - Configuration file
  - Feature-Specific Conguration Files
  - Contexts
  - Virtual Servers
  - Inheritance
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

### Configuration file

- 형식
  - 텍스트
- 이름
  - default `nginx.conf`
- 위치
  - `/etc/nginx` or `/usr/local/nginx/conf` or `/usr/local/etc/nginx`에 위치
- 구조
  - directive + parameter
    - 각 라인은 ;로 끝남
    - 어떤 directive는 container(block)로 역할하여 관련된 directive들을 `{}`로 감쌈
- 주의 사항
  - configuration file을 변경한 뒤에는 `reload`가 필요함
    - nginx process restart
    - reload

```nginx
user nobody;
error_log logs/error.log notice;
worker_processes 1;
```

### Feature-Specific Conguration Files

- 유지보수를 쉽게 하기
  - feature-specific 파일들을 `/etc/nginx/conf.d` 디렉터리에 두고 `include` directive로 main `nginx.conf`파일에 넣어두자

```nginx
include conf.d/http;
include conf.d/stream;
include conf.d/exchange-enhanced;
```

### Contexts

- 개요
  - 서로 다른 traffic type에 적용되는 여러 directive의 top level block
- 종류
  - `events`
    - General connection processing
  - `http`
    - HTTP traffic
  - `mail`
    - Mail traffic
  - `stream`
    - TCP / UDP traffic
  - 위의 contexts 밖에 위치한 directive들은 `main` 컨텍스트 안에 있다고 간주

### Virtual Servers

- 개요
  - 각각의 traffoc-handling context에서, 리퀘스트들을 프로세싱하기 위한 virtual server들을 정의하기 위하여 `server`블록을 포함시켜야 함
    - traffic 타입에 따라서, `server` 블록에 넣을 수 있는 directive가 다름
- 예시
  - `http` context에서는, 각 `server` directive는 request의 processing을 제어할 수 있음(도메인과 IP주소에 따라서)
  - `mail` 과 `stream` context에서는, `server`가 특정 TCP나 UNIX 소켓에 도착한 traffic에 대한 processing을 제어할 수 있음

Sample Configuration File with Multiple Contexts

```nginx
user nobody; # a directive in the 'main' context

events {
    # configuration of connection processing
}

http {
    # Configuration specific to HTTP and affecting all virtual servers

    server {
        # configuration of HTTP virtual server 1
        location /one {
            # configuration for processing URIs starting with '/one'
        }
        location /two {
            # configuration for processing URIs starting with '/two'
        }
    }

    server {
        # configuration of HTTP virtual server 2
    }
}

stream {
    # Configuration specific to TCP/UDP and affecting all virtual servers
    server {
        # configuration of TCP virtual server 1
    }
}
```

### Inheritance

- 개요
  - child context
    - 다른 context(parent) 속에 포함된 context
    - parent level의 모든 directive의 설정을 상속받음
    - overidding가능

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
