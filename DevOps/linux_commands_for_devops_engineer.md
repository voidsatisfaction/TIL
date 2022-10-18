# 데브옵스 엔지니어를 위한 리눅스 명령어

- 의문
- 네트워크 레이어 별 명령어
- 1 서버를 어떻게 접속하나요? 특별히 사용하는 도구나 방법이 있을까요?
- 2 IP를 확인하는 리눅스 명령어는 무엇인가요? 자신의 퍼블릭 IP는 어떻게 확인하나요?
- 3 웹사이트가 잘 동작하는지 체크할때 사용하는 명령어는? curl을 사용해본적은 있는지? 사용해보았다면 주로 어떨때 사용하는지?
- 4 도메인의 IP를 조회하는 명령어는?
- 5 웹서버 혹은 DB 같은 서버들을 확인하는 방법은?
- 6 내 서버가 잘 떠있는지, 현재 DB 커넥션 등을 확인하는 명령어는?
- 7 Linux에서 특정 프로세스를 확인하는 명령어는? java process id, option 등을 확인하고 싶으면?
- 8 Linux에서 CPU, Memory, Disk 등 시스템 정보등을 확인하는 명령어들은?
- 9 리눅스에서 서비스들은 어떻게 관리되고, 그와 연관된 명령어는?
- 10 리눅스 파일 권한 체계를 이해하고 있는지?
- 11 그밖의 명령어
- 12 라우팅이 잘 되는지 확인하는 커맨드
- 13 리눅스 배포판과 패키지 매니저

## 의문

## 네트워크 레이어 별 명령어

- Application
  - `ssh`
  - `curl`
- Transport
  - `netstat`
  - `ss`
- Internet(인터넷)
  - IP
    - `ifconfig`, `curl ifconfig.co`
  - DNS
    - `nslookup`
  - Routing
    - `traceroute`
    - `route`
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
  - 개요
    - 특정 URL의 명령어를
  - 설치
    - `apt install dnsutils`
  - 명령어
- 네트워크 통신시 DNS 조회 과정
  - `/etc/hosts`
  - `/etc/resolve.conf`
    - 네임서버 조회
    - 여기서 `search`로 host만 지정하더래도, 사용될 기본 도메인명을 지정 가능
      - e.g) k8s의 컨테이너 내부의 경우
        - `search default.svc.cluster.local svc.cluster.local cluster.local ap-northeast-1.compute.internal`
          - 그래서 컨테이너 내부에서 단순히 `curl gryphon-server`해도 response가능

## 5. 웹서버 혹은 DB 같은 서버들을 확인하는 방법은?

- `telnet`, `nc`
  - `telnet`
  - `nc`
- 잘못된 답변) `ping`

## 6. 내 서버가 잘 떠있는지, 현재 DB 커넥션 등을 확인하는 명령어는?

```
ss -ltp

State  Recv-Q(수신 소켓 버퍼 사이즈) Send-Q(송신 소켓 버퍼 사이즈)   Local Address:Port   Peer Address:Port      Process
LISTEN      0           4096                   0.0.0.0:15006                     0.0.0.0:*
LISTEN      0           100                    0.0.0.0:18080                     0.0.0.0:*          users:(("java",pid=6,fd=620))
LISTEN      0           4096                   0.0.0.0:15021                     0.0.0.0:*
LISTEN      0           100                    0.0.0.0:http-alt                  0.0.0.0:*          users:(("java",pid=6,fd=615))
LISTEN      0           4096                   0.0.0.0:15090                     0.0.0.0:*
LISTEN      0           4096                 127.0.0.1:15000                     0.0.0.0:*
LISTEN      0           4096                   0.0.0.0:15001                     0.0.0.0:*
LISTEN      0           4096                         *:15020                           *:*
```

- `netstat`(obsolete 라고 함)
  - 개요
  - 설치
  - 명령어
    - `netstat -lntpu`
    - `netstat -an | grep port`
- `ss`(socket statistics)
  - 개요
    - socket을 알아보는데 사용되는 툴
      - 설정이 없으면 established인 소켓만 보여줌
    - c.f) socket lifecycle
      - `LISTEN`
        - 소켓 연결을 기다리는 중
      - `ESTABLISHED`
        - 소켓 연결이 확립됨
  - 설치
    - `apt install iproute2`
  - 명령어
    - `ss`
      - established인 소켓 덤프
    - `ss -tl`
      - tcp이고 listening인 소켓 덤프

## 7. Linux에서 특정 프로세스를 확인하는 명령어는? java process id, option 등을 확인하고 싶으면?

- `ps`
  - c.f) 옵션 스타일
    - UNIX
      - 대시와 알파벳 그룹, `ps -ef`
        - 모든 프로세스를, full format으로 보여주기
      - `ps -wwef`
        - 모든 프로세스를, full format으로 보여주는데, 너무 긴 텍스트는 줄바꿈도 해서 보여줘
    - BSD
      - 대시 없는 알파벳 그룹, `ps aux`
        - 모든 프로세스를, 유저가 쉽게 볼 수 있도록, tty 없는 프로세스도 보여주기
    - GNU long options
      - 대시 두개가 붙음, `ps --tty`
  - 개요
    - 현재 프로세스들에 대한 스냅샷을 보여줌
  - 설치
  - 명령어
    - `ps -ef`
    - `ps aux`
      - `ps auxww`
        - 표시에서 줄넘어가는것까지 보여줌
      - `ps aux -T`
        - 스레드까지 보여줌

## 8. Linux에서 CPU, Memory, Disk 등 시스템 정보등을 확인하는 명령어들은?

- `htop`
  - 개요
    - 실시간으로 CPU, Memory, Swap 등의 다양한 메트릭을 볼 수 있는 커맨드
- `sar`
  - 개요
    - 시스템 모니터링 툴
- `free`
  - 개요
    - 현재 메모리 사용량을 알려줌
    - 메트릭
      - total
        - 전체 설치된 메모리
        - `/proc/meminfo`에서의 MemTotal
      - used
        - 유저공간에서 사용된 메모리
        - `total - free - buffers - cache`
      - free
        - 전혀 사용되지 않은 메모리
        - `/proc/meminfo`에서의 SwapFree
      - shared
        - 대게 `tmpfs`에 의해서 사용된 메모리
        - `/proc/meminfo`에서의 `Shmem`
      - buffers
        - 커널의 버퍼(디스크)에 의해서 사용된 캐시 메모리
          - 디스크 블록을 임시적으로 저장
          - write를 한꺼번에 한다던지, 디스크를 읽을때 사용한다던지
          - 디스크 IO를 줄인다던지
        - `/proc/meminfo`에서의 Buffers
      - cache
        - 파일 페이지 캐시나 slabs(커널에 의해서 사용되는 데이터 스트럭쳐를 저장하는데에 사용되는 메모리 공간)
          - 디스크로부터 파일을 읽기 위하여 만든 페이지 캐시
          - 다음에 같은 파일을 접근하면, 메모리로부터 직접적으로 빠르게 가져올 수 있음
          - 쓰기에도 사용됨
        - *그럼, disk와 파일의 차이는 무엇일까?*
      - buff/cache
        - 버퍼와 캐시의 합
      - available
        - 스왑하지 않고 새 애플리케이션을 시작하는 데 사용할 수 있는 메모리 양을 추정
          - 사용되고는 있는데, 캐시나 버퍼 같은 것들이어서 새로운 애플리케이션이 할당받아 스왑 없이 사용가능
- `df`
  - 개요
    - 파일 시스템 디스크 공간 사용 모니터링 커맨드
  - 명령어
    - `df`
      - 모든 마운트된 파일 시스템의 디스크 공간을 보여줌
    - `df -alh`
      - 모든 파일 시스템 중에서, 로컬 파일 시스템이고, 사람이 보기 쉽게 프린트하기
- `iostat`
  - 개요
    - CPU통계와 디바이스와 파티션에 대한 I/O 통계를 보여줌
      - CPU 사용 리포트
      - Device 사용 리포트

## 9. 리눅스에서 서비스들은 어떻게 관리되고, 그와 연관된 명령어는?

- c.f) `systemd`
  - 개요
    - 부팅시 가장 먼저 실행되는 프로그램(PID=1)으로, 시스템을 초기화하고 환경을 설정해줌
    - `initd`기능 + 시스템 총 관리 데몬
  - 특징
    - 부팅시 다른 프로세스들을 병렬적으로 실행
      - `.target` 설정 파일들을 이용해서 데몬 실행
    - 부팅시 프로그램 실행하는 기능 이외에 다양한 기능 존재
    - *unit이라는 엔티티로 나눠서 관리*
    - systemd 패밀리
      - `systemd`
      - `systemd-journald`
        - 데몬 프로세스들의 출력, 로그 저장 데몬
      - `systemd-logind`
        - 사용자 로그인, 세션 등 관리 데몬
      - `systemd-udevd`
        - 장치 관리자 데몬
- `service`
  - 개요
    - `/etc/init.d`에 있는 파일을 대상으로 동작하며, 기존의 init 시스템과 결합
    - Unix와 Linux계열의 다양한 서비스 프로그램의 래퍼
      - CentOS7에서는 자동으로 `systemctl`로 리다이렉트
      - CentOS6이하에서는 직접 `/etc/init.d`스크립트를 실행
      - 대신 기능은 한정적
  - 명령어
    - `service [name] start/restart/stop/status`
- `sysctl`
  - 개요
    - CentOS7이후 표준 `/lib/systemd`파일들을 대상으로 동작하며, 그쪽에 존재하지 않으면 `/etc/init.d`로 fall back
  - 명령어
    - `systemctl start/restart/stop/status [name]`

## 10. 리눅스 파일 권한 체계를 이해하고 있는지?

- `chmod`
  - 개요
  - 명령어
- `chown`
  - 개요
  - 명령어

## 11. 그밖의 명령어

- `cd`, `cp`, `mv`, `ls`
- 리눅스의 부팅 프로세스
  - `/etc/profile`
  - `/etc/rc*`
  - `cloud-init`
- 파일 시스템 관련
  - `fdisk`, `lvm`, `mkfs`
- 패키지 repo관련
  - `yum`, `apt`

## 12. 라우팅이 잘 되는지 확인하는 커맨드

- `traceroute`
  - 개요
    - IP 패킷이 주어진 호스트로 잘 가는지 트래킹
      - IP 프로토콜의 TTL필드를 사용해서 목적지 호스트까지의 각각의 게이트웨이(라우터)에서 ICMP TIME_EXCEEDED 응답을 끌어냄
      - 처음에는 작은 TTL 패킷을 보내고, 디폴트 최대 30TTL까지 늘려서 보내봄
  - 특징
    - *는 타임아웃까지 아무런 응답이 없는 경우
  - 설치
    - `apt install traceroute`

## 13. 리눅스 배포판과 패키지 매니저

- 리눅스 배포판(패키지 형식 / 패키지 관리자)
  - 개요
    - 리눅스 커널을 중심으로 여러 시스템 소프트웨어 및 응용 소프트웨어를 같이 묶어서 구성한 운영체제
      - 패키지 매니저, 개말 툴 체인, 각종 유틸리티 프로그램, 데스크톱 환경을 포함
  - 계열(생략된 것들도 많음)
    - 페도라(`.rpm` / `yum`)
      - 레드햇 계열
        - 레드햇 엔터프라이즈
        - Cent OS
      - AWS Linux
    - 데비안(`.deb` / `apt`)
      - 우분투 계열
        - 우분투
      - 칼리 리눅스
      - 라즈베리 파이 OS
    - 아치(`tar.gz, tar.xz` / `pacman`)
      - 아치 리눅스
- 패키지 관리
  - 데비안
    - 리스팅
      - `apt list`
    - 삭제
      - `apt remove`
        - 패키지 삭제(o), 환경설정 삭제(x)
      - `apt purge`
        - 패키지 삭제(o), 환경설정 삭제(o)
      - `apt autoremove`
        - 사용되지 않는 패키지 삭제
          - 리눅스 헤더파일들 삭제할때도 쓰임
  - 페도라
    - 리스팅
      - `yum list installed [패키지 이름]`
    - 삭제
      - `yum remove [패키지 이름]`
