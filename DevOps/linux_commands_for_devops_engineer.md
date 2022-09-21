# 데브옵스 엔지니어를 위한 리눅스 명령어

- 의문
- 1 서버를 어떻게 접속하나요? 특별히 사용하는 도구나 방법이 있을까요?

## 의문

## 네트워크 레이어 별 명령어

- Application
  - `ssh`
  - `curl`
- Transport
- Internet(인터넷)
  - IP
    - `ifconfig`, `curl ifconfig.co`
  - DNS
    - `nslookup`
- Data Link
- Physical

## 1. 서버를 어떻게 접속하나요? 특별히 사용하는 도구나 방법이 있을까요?

- `ssh`
  - 그 원리를 알고 있는지
  - key 방식을 사용해봤는지
    - 어떤 파일을 사용하는지?
  - 대체 도구는 무엇이 있는지
  - 접근 제어는 어떻게 하는지
  - 포트 변경하기(well-known포트를 사용하지 않기)
    - `/etc/ssh/sshd_config`의 수정

## 2. IP를 확인하는 리눅스 명령어는 무엇인가요? 자신의 퍼블릭 IP는 어떻게 확인하나요?

- 사설 ip
  - `ifconfig`
- 퍼블릭 ip
  - `curl ifconfig.co`

## 3. 웹사이트가 잘 동작하는지 체크할때 사용하는 명령어는? curl을 사용해본적은 있는지? 사용해보았다면 주로 어떨때 사용하는지?

- `curl`
  - `-v`옵션
  - 헤더 지정, application/json

## 4. 도메인의 IP를 조회하는 명령어는?

- `nslookup`
- 조회 과정
  - `/etc/hosts`
  - `/etc/resolve.conf`
    - 네임서버 조회
    - 여기서 `search`로 host만 지정하더래도, 사용될 기본 도메인명을 지정 가능
      - e.g) k8s의 컨테이너 내부의 경우
        - `search default.svc.cluster.local svc.cluster.local cluster.local ap-northeast-1.compute.internal`
          - 그래서 컨테이너 내부에서 단순히 `curl gryphon-server`해도 response가능
