# Secret

- 의문
- 개요

## 의문

## 개요

- 정의
  - 암호, 토큰 또는 키와 같은 소량의 중요한 데이터를 포함하는 오브젝트
    - 팟의 명세나, 컨테이너 이미지에 중요 정보를 포함시키지 않기 위함
  - 팟의 생성과 독립적
  - 컨피그맵과 유사하나, 기밀 데이터를 보관하기 위함
- 특징
  - etcd에 암호화하지 않은 상태로 저장됨
    - 즉, API acess권한이 있는 모든 사용자 또는 etcd에 접근할 수 있는 모든 사용자가 시크릿 조회 및 수정 가능
    - 암호화 기능 활성화 / 시크릿 RBAC 규칙 활성화 / 주체(principal) 제한

### 사용

- 컨테어너에 볼륨 내의 파일로 사용
- 컨테이너 환경 변수로 사용
- *팟 이미지를 가져올 떄, kubelet에 의해 사용*
  - 이게 구체적으로 어떻게 사용된다는 것?

### 시크릿 다루기

```yaml
apiVersion: v1
data:
  username: YWRtaW4=
  password: MWYyZDFlMmU2N2Rm
kind: Secret
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: { ... }
  creationTimestamp: 2020-01-22T18:41:56Z
  name: mysecret
  namespace: default
  resourceVersion: "164619"
  uid: cfee02d6-c137-11e5-8d73-42010af00002
type: Opaque

---
# 파일 형태로 사용
# 일단 mysecret이라는 시크릿이 존재해야 함
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: redis
    volumeMounts:
    - name: foo
      mountPath: "/etc/foo"
      readOnly: true
  volumes:
  - name: foo
    secret:
      secretName: mysecret
      optional: false # 기본값임; "mysecret" 은 반드시 존재해야 함

---
# 환경변수 형태로 사용
apiVersion: v1
kind: Pod
metadata:
  name: secret-env-pod
spec:
  containers:
  - name: mycontainer
    image: redis
    env:
      - name: SECRET_USERNAME
        valueFrom:
          secretKeyRef:
            name: mysecret
            key: username
            optional: false # 기본값과 동일하다
                            # "mysecret"이 존재하고 "username"라는 키를 포함해야 한다
      - name: SECRET_PASSWORD
        valueFrom:
          secretKeyRef:
            name: mysecret
            key: password
            optional: false # 기본값과 동일하다
                            # "mysecret"이 존재하고 "password"라는 키를 포함해야 한다
  restartPolicy: Never
```

- 생성
  - 방법
    - kubectl 명령
    - 환경 설정 파일을 사용
    - kustomize를 사용하여 생성
  - 제한
    - 이름 및 데이터
      - `data`및 `stringData`필드를 명시 가능
      - `data`
        - 모든 키에 해당되는 값은 base64로 인코딩된 문자열이어야 함
          - 팟에서 사용할 때에는 kubelet이 팟의 컨테이너에 디코드된 데이터 제공
      - `stringData`
        - base64로의 문자열 변환이 적합하지 않은경우
        - 추후에 `data`필드로 합쳐짐. `stringData`필드에 지정된 값이 우선적으로 사용됨
    - 크기
      - 개별 시크릿의 크기는 1MiB
        - API서버 및 kubelet 메모리를 고갈시키지 않기 위함
- 사용
  - 시크릿을 파일로 사용하기
    - 자동 업데이트
      - 볼륨이 시크릿의 데이터를 포함하고 있는 상태에서 시크릿이 업데이트되면, 쿠버네티스는 이를 추적하고, 최종적으로 일관된(eventually-consistent) 접근 방식을 사용하여 볼륨 안의 데이터를 업데이트 함
        - *but 시크릿을 `subPath` 볼륨 마운트로 사용하는 컨테이너는 자동 시크릿 업데이트를 받지 못함*
        - kubeleet이 시크릿의 현재 키 및 값 캐시를 유지함
  - 시크릿을 환경 변수 형태로 사용하기
- 타입
  - 개요
    - 여러 종류의 기밀 데이터를 프로그래밍 방식으로 용이하게 처리하기 위해 사용
  - 종류
    - Opaque
      - 임의의 사용자 정의 데이터
    - kubernetes.io/service-account-token
      - *서비스 어카운트 토큰*
    - kubernetes.io/dockercfg
      - 직렬화된 `~/.dockercfg`파일
    - kubernetes.io/dockerconfigjson
      - 직렬화된 `~/.docker/config.json` 파일
    - kubernetes.io/basic-auth
      - basic 인증을 위한 자격 증명
    - kubernetes.io/ssh-auth
      - ssh를 위한 자격 증명
    - kubernetes.io/tls
      - tls 클라이언트나 서버를 위한 데이터
    - bootstrap.kubernetes.io/token
      - 부트스트랩 토큰 데이터