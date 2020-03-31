# OpenSSL

- 의문
- 개요
  - Key and Certificate Management

참고 사이트

https://www.feistyduck.com/library/openssl-cookbook/online/ch-openssl.html#ftn.N100C4

## 의문

- *OpenSSL로 생성된 Certificate는 어떻게 유효한 certificate라고 검증할 수 있는가?*
  - *검증 안하고, 그냥 certificate가 OpenSSL에서 발급 받았다는 것을 확인한후, public key를 추출(?)*

## 개요

- Cryptographic libaray + TLS / SSL 프로토콜 오픈소스 툴킷(commercial use 가능)
  - SSL / TLS 사설 인증서 발급 가능

### Key and Certificate Management

- 웹 서버 TLS 지원 절차
  - ① strong private key생성
  - ② CSR(Certificate Signing Request) 생성 & CA에 전송
  - ③ CA로부터 주어진 certificate를 web server에 설치

#### ① strong private key생성

rsa key 생성 예시

```
// aes128 알고리즘과 pass phrase를 사용하여 암호화 되어있음
openssl genrsa -aes128 -out fd.key 2048

// pirvate key 내부 내용 보기
openssl rsa -text -in ~/.ssh/cat-project.pem
```

키 생성에서 선택해야 할 것

- Key algorithm
  - RSA, DSA, ECDSA
    - 웹 서버는 RSA
- Key size
  - 2048이상이 안전
- Passphrase
  - safely stored, transported, backed up
  - 대신 매번 비밀번호 쳐야해서 불편함
  - 보안상의 이점이 그다지 크지 않음
    - 어차피 unprotected private key가 production 환경에서는 memory에 올라가 있음

private key에서 public key 생성 가능

#### ② CSR(Certificate Signing Request) 생성 & CA에 전송 혹은 자신이 사인

CSR 생성

```sh
// CSR 생성
openssl req -new -key fd.key -out fd.csr

// CSR 확인
openssl req -text -in fd.csr -noout

// Create CSR from existing certificates
openssl x509 -x509toreq -in fd.crt -out fd.csr -signkey fd.key

// Create CSR directly(not interactive)
openssl req -new -config fd.cnf -key fd.key -out fd.csr
```

- CSR(Certificate Signing Request)
  - 개요
    - CA가 certificate에 사인하도록 요청
      - 요청하는 주체(entity)의 public key와 주체의 정보를 포함
    - 해당 CSR은 언제나 요청을 보내는 public key에 대응하는 private key로 서명됨

**Signing own certificate**

- CA로 부터 사인을 받지 않고 자신이 직접 사인을 함

```sh
// signing own certificate
openssl x509 -req -days 365 -in fd.csr -signkey fd.key -out fd.crt

// CSR creation and signing own certificate
openssl req -new -x509 -days 365 -key fd.key -out fd.crt

// CSR creation and signing down certificate and no asked question (-subj)
openssl req -new -x509 -days 365 -key fd.key -out fd.crt \
- subj "/C=GB/L=London/O=Feisty Duck Ltd/CN=www.feistyduck.com"

// Examining certificates
openssl x509 -text -in fd.crt -noout
```

다양한 extension이 존재 -> [확인](https://www.feistyduck.com/library/openssl-cookbook/online/ch-openssl.html#ftn.N100C4)

#### ③ CA로부터 주어진 certificate를 web server에 설치

nginx의 경우(예시)

```nginx
events {
  worker_connections 1024;
}

http {
    server {
        listen 443 ssl;
        ssl_certificate /etc/certs/cert.pem;
        ssl_certificate_key /etc/certs/key.pem;

        client_max_body_size 100M;

        error_log /var/log/nginx/error.log debug;
        access_log /var/log/nginx/access.log;

        location / {
            proxy_pass http://api-server:15080;
        }

        location /api {
            proxy_pass http://api-server:15080;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
}
```
