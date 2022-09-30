# Yaml

- 의문
- 개요
- 문법
  - object
  - 쿠버네티스 파일로 보는 예시
  - 멀티라인 예시
  - 헬름 예시
  - 컴포넌트의 분리

## 의문

## 개요

- 개요
  - 데브옵스 툴에서 많이 사용됨
- 특징
  - 읽기 쉬움
  - JSON의 superset
    - 따라서, JSON을 yaml로 변환 가능
  - line separation
  - indentation
- 예시
  - docker-compose
  - kubernetes

## 문법

yaml validator를 사용해서 문법 오류를 체크하자

### object

```yaml
# comment here
# microservice 오브젝트
microservice:
  app: user-authentication
  port: 9000
  version: 1.7

microservices:
  # 리스트
  - app: user-authentication
    port: 9000
    version: 1.7
  - app: shopping-cart
    port: 9002
    versions:
      - 1.9
      - 2.0
      - 2.1
  - app: shopping-cart
    port: 9002
    versions: [1.9, 2.0, 2.1] # simple data type일 경우만 가능

# 멀티라인
multilineString: |
  this is a multiline string
  and this is the next line
  next line

# 싱글라인
singlelineString: >
  this is a single line string,
  that should be all on one line.
  some other stuff

# 환경변수
command:
  - /bin/sh
  - -ec
  - >-
    mysql -h 127.0.0.1 -u root -p$MYSQL_ROOT_PASSWORD -e 'SELECT 1'
```

- 문자열
  - "" or '' 써도되고 안써도 됨
  - 특수 문자 쓸때는 "" 있어야 함
    - e.g) "\n"

### 쿠버네티스 파일로 보는 예시

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  containers:
    - name: nginx-container
      image: nginx
      ports:
        - containerPort: 80
      volumeMounts:
        - name: nginx-vol
          mountPath: /usr/nginx/html
    - name: sidecar-container
      image: curlimages/curl
      comand: ["/bin/sh"]
      args: ["-c", "echo Hello from the sidecar container; sleep 300"]
```

### 멀티라인 예시

```yaml
kind: configMap
metadata:
  name: mosquitto-config-file
data:
  mosquitto.conf: |
    log_dest stdout
    log_type all
    log_timestamp true
    listener 9001
  command:
    - sh
    - -c
    - |
      #!/usr/bin/env bash -e
      http () {
        local path="${1}"
        ...
      }
      http "/app/kibana"
```

### 헬름 예시

```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ .Values.service.name }} # placeholder (템플릿 변수)
spec:
  selector:
    app: {{ .Values.service.app }}
  ports:
    - protocol: TCP
      port: {{ .Values.service.port }}
      targetPort: {{ .Values.service.targetport }}
```

### 컴포넌트의 분리

하나의 파일에서 컴포넌트를 분리하는 법

```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ .Values.service.name }} # placeholder (템플릿 변수)
spec:
  selector:
    app: {{ .Values.service.app }}
  ports:
    - protocol: TCP
      port: {{ .Values.service.port }}
      targetPort: {{ .Values.service.targetport }}

---

apiVersion: v2
kind: Service
metadata:
  name: {{ .Values.service.name2 }} # placeholder (템플릿 변수)
spec:
  selector:
    app: {{ .Values.service.app2 }}
  ports:
    - protocol: TCP
      port: {{ .Values.service.port2 }}
      targetPort: {{ .Values.service.targetport2 }}
```
