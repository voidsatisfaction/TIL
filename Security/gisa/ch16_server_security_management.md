# 16. 서버 보안 관리

- 의문
- 16.1 서버관리자의 업무
  - 보안 유지 관리
  - 서버관리자의 업무
- 16.2 로그 설정과 관리
  - 시스템 로그 분석
  - 윈도우의 로그 분석과 설정
  - 유닉스/리눅스의 로그 분석과 설정
- 16.3 공개 해킹도구에 대한 이해와 대응
- 16.4 서버보안용 S/W 설치 및 운영

## 의문

## 16.1 서버관리자의 업무

- 시스템 관리의 6가지 주제
  - AC(Access Control)
    - System
      - Authentication
        - 계정과 패스워드 관리
      - Authorization
        - 권한 관리
      - Session
        - 활성화된 세션(접속)에 대한 관리
    - Network
  - 자원 관리
  - 취약점 관리
  - 로그 관리

### 보안 유지 관리

- 개요
  - 시스템을 구축한 후에, 보안 유지 관리 해야함
- 해야할 보안 유지관리 프로세스
  - **정기적으로 백업 수행**
  - 로깅 정보를 감시 분석
  - 정기적으로 시스템 보안을 테스트
- 로깅
  - 이미 발생한 나쁜 일을 알려주는 반작용적 제어
  - 시스템 파괴 혹은 고장 시에 무슨 일이 발생했는지를 빠르고 정확하게 찾게 도와주고, 교정과 복구 노력에 집중 가능하게 함

### 서버관리자의 업무

- 시스템관리자 계정으로 작업하기
  - 방법
    - root계정으로 로그인
    - `su(switch user)`명령으로 root로 계정 바꾸기
      - 보안적으로 더 안전함
- 사용자 계정 관리
  - 위치
    - `/etc/passwd`
      - 사용자 계정
    - `/etc/shadow`
      - 사용자 비밀번호(암호화 됨)
  - 계정 사용 제한
    - 원격 접근권한 제어
      - `/etc/passwd` 파일에서 `/bin/bash`와 같은 셸을 삭제
    - 계정 사용기간 설정
      - `/etc/shadow` 파일에서 사용기간 또는 만료일 설정
- 자원 관리
  - 프로세스 관리
    - `ps`, `kill`, `wait`, `su`
    - `wait`
      - 프로세스가 끝나기를 기다리는 명령어
    - `nice`
      - 프로세스의 우선순위를 변경할 수 있는 nice값을 설정하는 명령어
  - 메모리 관리
    - `free`
      - 시스템의 실제 메모리와 스왑 메모리에 대한 사용 현황을 확인할 수 있는 명령어
  - 메일, 디스크 등의 관리
    - 리눅스에서는 디스크 사용량을 사용자 및 그룹별로 설정하기 위해서 `quota`사용
    - 메일 용량 크기 제한은 메일 스풀 디렉터리에 별도 파티션을 주고 그 파티션에 쿼터를 설정
    - `du`
      - 디스크 파일 사용량을 재귀적으로 보여줌
- 네트워크 관리
  - `ifconfig`
    - NIC 상태를 보여줌
  - `netstat -an`
    - 현 시스템에서 사용되는 통신 서비스의 상태
  - `top`
    - 시스템 자원(CPU, memory)등의 사용 현황
  - `ps -elf(-aux)`
    - 현 시스템에서 수행 중인 프로그램과 데몬 상태를 보여줌
  - `who, w`
    - 로그인되어 있는 사용자 보여줌
  - `snoop`
    - 네트워크를 흐르는 패킷을 캡쳐하여 분석
  - `nslookup`
    - 도메인에 대한 IP정보 및 도메인 네임과 관련된 여러 검색이 가능
  - `hostname`
    - 현 시스템에 할당된 호스트 이름을 보여줌
  - `traceroute`
    - 특정 호스트까지의 네트워크 라우팅 경로 및 경유하는 IP를 보여줌
  - `inetd`
    - 네트워크 슈퍼데몬인 inetd를 실행

## 16.2 로그 설정과 관리

### 시스템 로그 분석

- 로그에 대한 이해
  - 윈도우
    - Event라는 중앙 집중화된 로그를 수집하여 저장
    - 공격자는 대신 한 로그만 삭제
      - 보안 수준 낮음
  - Unix
    - 로그를 여러 곳에 산발적으로 저장
    - 공격자가 로그를 모두 찾아 지우기가 쉽지 않음

### 윈도우의 로그 분석과 설정

- 해커에 대한 즉각적인 확인
  - 현재 로그인된 사용자를 확인하는것도 중요
  - `net session`
    - 자신의 시스템에 로그인한 IP / 로그인 계정 / 클라이언트 운영체제 / 세션의 수 / 로그인 후 경과한 시간 출력
  - `net session /delete`
    - 세션 끊기
  - `psloggedon`은 로컬로 로그인한 계정 정보도 함께 보여줌
    - `net`과 차이점이 무엇인지?
- 윈도우 시스템 이벤트 로그 종류
  - Application program log
  - Security log
    - 유효하거나 유효하지 않은 로그인 시도
    - 파일 생성, 열람, 삭제같은 리소스 사용에 관련된 이벤트 기록
  - System log
    - Windows 시스템 구성요소가 기록하는 이벤트
    - e.g)
      - 시스템 부팅시 드라이버가 로드되지 않는 경우와 같은 구성요소 오류를 이벤트에 기록
  - Directory service log
    - Windows Active Directory service에 발생하는 이벤트
  - File copy service log
    - Windows 파일 복제 서비스에서 발생하는 이벤트
  - DNS server log
    - Windows DNS 서비스에 발생하는 이벤트
- 감사 정책
  - 정의
    - **어떤 로그를 남길지를 정의한 규칙**
      - *감사 정책에서 설정한 로그는 어디에서 볼 수 있는걸까?*
  - 종류
    - 개체 액세스 감사
      - 특정 파일이나 디렉터리, 레지스트리 키, 프린터 등과 같은 객체에 접근을 시도하거나 속성 변경 등을 탐지
    - 계정 관리 감사
      - 신규 사용자, 그룹의 추가, 기존 사용자 그룹의 변경, 사용자의 활성화나 비활성화, 계정 패스워드 변경 등을 감사
    - 계정 로그인 이벤트 감사
      - 도메인 계정의 사용으로 인한 이벤트 감사
        - *도메인 계정이 뭐지?*
    - 로그인 이벤트 감사
      - 로컬 계정 접근 시 생성되는 이벤트 감사
    - 권한 사용 감사
      - 권한 설정 변경이나, 관리저 권한이 필요한 작업을 수행할 때 로깅
    - 디렉터리 서비스 엑세스 감사
    - 정책 변경 감사
      - 사용자 권한 할당 정책, 감사 정책 또는 신뢰 정책의 변경과 관련된 사항을 로깅
    - 프로세스 추적 감사
      - 사용자 또는 응용프로그램이 프로세스를 시작하거나 중지할 때 해당 이벤트 발생
    - 시스템 이벤트 감사
      - 시스템의 시동과 종료, 보안 로그 삭제 등 시스템의 주요한 사항에 대한 이벤트를 남김
- 로그 정책 설정
  - 제어판 - 관리도구 - 로컬 보안 정책 메뉴에서 로컬 정책 - 감사 정책에서 확인할 수 있음
  - 윈도우의 경우, 유닉스에 비해 로깅하는데 자원이 많이 소모됨
- 이벤트 로그 파일
  - `%Windows%¥system32¥config`폴더 아래에 있는 `.evt` 확장자를 가진 파일이며, 파일명은 이벤트 뷰어에서 보이는 로그파일명과 비슷함
  - 예시
    - Application program log
      - `AppEvent.Evt`
    - Security log
      - `SecEvent.Evt`
    - System log
      - `SysEvent.Evt`
  - 특징
    - 바이너리 형식이므로, 그냥 봐서는 모르고, 이벤트 뷰어 프로그램 등으로 열어서 봐야 함
    - 제어판 - 관리도구 - 이벤트 뷰어

### 유닉스/리눅스의 로그 분석과 설정

- 로그 디렉터리
  - `syslogd`
    - 중앙 집중적으로 로그를 관리하는 데몬
    - 이곳 이외에 다양한 장소에 로그 저장
- utmp(x) 로그
  - 정의
    - 현재 시스템에 로그인한 사용자의 상태를 출력
  - 로그 남기는 프로그램
    - `/etc/lib/utmpd`
  - 특징
    - 데이터는 `utmp.h`에서 정의된 구조체로 바이너리 형태로 저장
    - 커맨드로 확인 가능
      - `w`, `who`, `users`, `whodo`, `finger`등이 있음
- wtmp(x) 파일
  - 정의
    - 사용자의 로그인, 로그아웃, 시스템 재부팅 정보 담음
  - 로그 남기는 프로그램
    - `wtmpd`
  - 특징
    - `/usr/include/utmp.h` 파일의 구조체를 그대로 사용해서 바이너리 형태로 저장
    - 커맨드로 확인 가능
      - `last`
        - 올바로 로그인 된경우에 로그가 남음
- **loginlog(Unix/SunOS), btmp(Linux)**
  - 다소 소름..?
    - ssh bruteforce attack 볼 수 있음
  - Linux
    - 정의
      - 실패한 모든 로그를 남김
    - 특징
      - `/var/log/btmp` 바이너리 파일
  - Unix(SunOS)
    - 정의
      - 5회 이상 실패 시 실패한 로그 남김
    - 특징
      - `/var/adm/loginlog` 텍스트 파일
- lastlog
  - 정의
    - 가장 최근에 성공한 로그인 기록을 담고 있는 로그 파일
  - 특징
    - `lastlog` or `finger` 명령 사용, 바이너리 파일
- sulog(Unix/SunOS)
  - 정의
    - `su`에 대한 로그
  - 특징
    - `su root`, `su -root`는 모두 관리자 계정 권한으로 변경했기 때문에 `su`로그에 남으며, `/var/adm/sulog` 파일에 텍스트 형식으로 남음
      - 텍스트 파일의 권한은 600으로 설정되어있음
- acct/pacct(process account) 로그
  - 정의
    - 시스템에 로그인한 모든 사용자가 수행한 프로그램에 대한 정보를 저장하는 로그
  - 특징
    - `/usr/adm/pacct`, binary, `acctcom` or `lastcomm`
    - 사용자가 로그인했다가 로그오프할 때까지 입력한 명령과 연결에 이용한 터미널의 종류와 시간 등을 저장
    - 해커 추적 목적이 아닌, 대형 시스템을 여러 사용자가 비용을 지불하는 형식으로 공유할 경우, 각 사용자에 대한 요금을 부과하기 위해 사용됨
      - pacct는 시스템 자원을 비교적 많이 소모하며, 기본적으로 동작하지 않음
- `.sh_history` or `.hash_history`
  - 정의
    - 실행한 명령에 대한 기록
  - 특징
    - `~/.bash_history`, text, `history`
      - 파일은 600 권한이지만, 공격자에게 많은 정보를 주므로 위험
- FTP 파일 전송 로그(xferlog)
  - 정의
    - FTP로그 파일로서 proftpd 또는 vsftpd 데몬들의 서비스 내역을 기록하는 파일
  - 특징
    - 공격자가 FTP 서비스를 이용해 시스템에서 어떤 파일을 복사했는지, 또 어떤 파일을 시스템에 복사해두었는지 찾아내야 할 때 유용
    - 파일을 전송한 날짜와 시간, 접근 시스템 IP, 전송한 파일을 확인할 수 있음
- HTTPD Log(Access_log, Error_log)
  - apache
    - `/usr/local/apache/logs`
  - nginx
    - ...
- `dmesg`
  - 정의
    - 리눅스가 부팅될 때 출력되는 모든 메시지를 기록.
  - 특징
    - 부팅 시의 에러나 조치사항을 살펴보기 위해서 실행
- messages
  - 정의
    - 시스템의 가장 기본적인 시스템 로그파일
    - 시스템 운영에 대한 전반적인 메시지 저장
      - 시스템 데몬들의 실행상황과 내역
      - 사용자들의 접속정보
      - TCP Wrapper 접근 제어 정보
- secure
  - 정의
    - 사용자의 원격접속, 원격 로그인 정보를 기록하고 있는 로그파일
  - 특징
    - `/var/log/auth.log`, text
    - tcp_wrapper(xinetd)의 접속제어에 관한 로그파일은 언제, 누가, 어디에서 어떻게 접속했는가에 대한 로그 기록

### 유닉스/리눅스 시스템 로그 설정(/etc/syslog.conf)

- 개요
  - 유닉스에서는 `syslog`라는 오래된 표준 인터페이스(API)에 의해 로그를 생성하고 관리함
  - `syslogd`는 데몬으로 자동으로 실행되는데, 프로세스의 initialize 시에, `/etc/syslog.conf`를 읽어서 어떤 로그를 어디에 남길지를 결정하게 됨
- 포맷
  - `facility.priority; facility.priority action(logfile-location)`
    - 어떤 facility에 대해서 priority의 경우에 해당하는 상황이 발생하였을 때, action(log file)에 그 기록을 남겨라
  - facility
    - \*
      - 모든 서비스
    - auth
      - login, su 처럼 사용자 권한을 사용하거나 변경
    - console
      - 콘솔에 일반적으로 나타나는 메시지
    - cron
      - 시스템 스케쥴러에서 보내는 메시지
    - daemon
      - 별도의 핸들러가 없는 모든 시스템 데몬의 로그
    - ftp
      - FTP데몬의 전송
    - kern
      - 커널 메시지
    - ntp
      - Network Time Protocol이 보내는 메시지
        - 유닉스 시스템 시간을 일정하게 서로 맞추기 위한 프로토콜
    - security
      - 각종 보안 시스템이 보내는 메시지
    - user
      - 사용자 프로그램에 대한 로깅
  - priority
    - 메시지 우선순위 or log level
  - action
    - 로그를 어디에 남길 것인지 결정
      - 로그 파일
      - 콘솔
        - `/dev/console`
      - 원격 로그 서버
        - `@192.168.197.133`
      - user
        - 지정된 사용자의 스크린으로 메시지를 보냄
      - \*
        - 현재 로그인되어 있는 모든 사용자의 스크린으로 메시지를 보냄
- 설정 예시
  - `*.info;mail.none;news.none;authpriv.none /var/log/messages`
    - 모든 서비스에 대한 info 수준 이상의 로그를 `/var/log/messages` 로그 파일에 기록하되, mail, news, authpriv 서비스에 대해서는 로그 파일을 기록하지 말라는 의미
    - 세미콜론은 or을 의미

### 로그 관리

- 로그 모니터링(실시간 분석)
  - `tail -f /var/log/messages`
  - utmp, wtmp, lastlog등 바이너리 형식의 로그파일들은 cat, vi등의 텍스트 편집기를 통해서 확인 불가
- 로그 순환
  - `logrotate`는 시스템 로그 파일에 대해서 로테이트, 압축, 또는 메일을 발송해주는 리눅스 시스템 로그파일 관리기

## 16.3 공개 해킹도구에 대한 이해와 대응

### 크래킹 S/W

- 크래킹 개요
  - 악의적인 목적을 가지고 시스템에 침입하는 행위 or 쉐어웨어 프로그램을 정식버전으로 변환하는 행위
- 크래킹 S/W 사례
  - John the Ripper
    - 패스워드 점검도구(Windows, Linux, Mac)
  - pwdump
    - 윈도우 패스워드 dump 도구
  - L0phtCrack
    - 패스워드 취약점 점검도구로, 원격 및 로컬 서버나 PC에 대하여 패스워드 점검하는데 유용
  - ipccrack
    - 사용자 계정 패스워드를 원격지에서 추측하여 취약점 점검 도구
  - chntpw
    - 물리적 접근이 가능한 시스템에서 패스워드 리셋시키는 프로그램
  - ERD Commander
    - 윈도우 시스템에서 패스워드를 복구해야 하는 경우에 사용

### 키로그 S/W

- 개요
  - 설치된 컴퓨터에서 키보드로 입력한 정보를 로그로 남기는 프로그램
  - 기능이 업데이트된 경우, 윈도우를 이용한 프로그램 사용, 인터넷 익스플로러를 이용한 인터넷 접속 정보 등도 로그로 남김
- 키보드 해킹방지 프로그램
  - 사용자의 키보드 입력 자체를 보호하여 사용자가 입력하는 정보를 제3자가 알아볼 수 없도록 해주는 프로그램
    - *키로그가 SYSTEM이나 루트권한으로 실행되고 있으면, 결국 복호화 가능한것 아닌가? or low level의 키 event가 획득가능한 것 아닌가?*

## 16.4 서버보안용 S/W 설치 및 운영

### 취약점 분석 도구

- 취약점 분석 개요
  - 일정한 보안 수준을 유지하기 위해서 정기적으로 수행해야 함
  - 새로운 소프트웨어나 서비스가 추가되는 경우 or 새로운 장비를 구입하여 네트워크를 확장했을 경우에도 취약점 분석이 필요
- 취약점 분석 도구
  - SATAN(Security Analysis Tool for Auditing Networks)
    - 개요
      - 해커와 똑같은 방식으로 시스템에 침입, 보안상의 약점을 찾아 보완할 수 있는 네트워크 분석용 보안 관리 도구
    - 특징
      - 해커에게 노출될 수 있는 약점을 사전에 발견 / 보완 가능
      - GUI로 되어있음
  - SARA
    - 개요
      - SATAN 기반 취약점 분석도구
  - SAINT
    - 개요
      - 유닉스 플랫폼 기반 네트워크 취약점 분석도구
    - 특징
      - HTML 보고서 기능
      - 원격 취약점 점검 기능
  - COPS
    - 개요
      - 유닉스 플랫폼 기반 시스템 내부 존재 취약점 점검 도구
      - 취약 패스워드 체크
  - Nessus
    - 개요
      - 클라이언트-서버 구조로, 클라이언트의 취약점을 점검하는 기능 존재
    - 특징
      - 서버에 nessus 데몬과 각종 취약점 점검 플러그인 등이 설치되며, 취약점을 점검하고 결과를 조회할 수 있는 인터페이스 제공
      - 클라이언트(웹 브라우저 등)는 nessus 데몬에 접속하여 대상 시스템에 대한 취약점 점검을 실시
      - 사용이 자유롭고 플러그인 업데이트 등이 쉬움
      - HTML등 여러 형태로 결과를 리포트 해줌
  - nmap(network mapper)
    - 개요
      - 포트 스캐닝 도구
    - 특징
      - 스텔스 모드 존재

### 무결성 점검

- 파일 무결성 점검
  - 개요
    - 정상적인 상태의 디렉터리 및 파일 정보를 백업하고 있다가 점검 수행 시점에서의 정보와 백업한 정보를 비교하여 변경된 사항을 점검하는 도구
  - 종류
    - tripwire(linux/unix)
  - 특징
    - MD5, SHA, CRC-32 등의 다양한 해시 함수를 지원하고, 파일에 대한 데이터베이스를 만들어 이를 통해 공격자들에 의한 파일들의 변조 여부 판별
    - 시그니처 역시 반드시 보호되어야 함(공격자는 파괴하려고 함)
    - 데이터 파일 보호에는 적절하지 않음
      - 데이터 파일은 자주 변경이 되기 때문에 자주 재계산되어야 함
  - 동작 방식
    - 최초 설정파일에 등록된 파일 및 디렉터리의 해시값을 생성하여 데이터베이스에 저장
    - 주기적으로 트립와이어가 동작하면서 기존 데이터베이스에 저장된 해시값과 현재 각 파일 및 디렉터리의 해시값을 비교
    - 비교 결과 값이 다를 경우, 변경 내역을 출력하여(리포트) 관리자가 이를 확인

### 스캔 탐지

- 스캔 탐지 도구
  - mscan
  - sscan
  - portsentry
    - 개요
      - 실시간으로 포트 스캔을 탐지하고 대응하기 위한 프로그램
    - 특징
      - 정상적인 스캔과 stealth scan탐지 가능
      - 스캔로그 남기기
      - 공격호스트를 `/etc/hosts.deny`파일에 기록하여 자동 방어
      - 공격 호스트를 경유하여 오는 모든 트래픽을 자동 재구성하는 기능 존재

### 침입탐지 및 방화벽

- 네트워크 모니터링 및 침입탐기 도구
  - Snort
    - 개요
      - 실시간 트래픽분석과 IP 네트워크에서의 패킷 처리를 담당하는 공개 소스 네트워크 침입탐지시스템(IDS - Intrusion Detection System?)
    - 기능
      - 프로토콜 분석, 콘첸트 검색 및 조합 작업 가능.
      - 버퍼 오버플로우
      - 은폐형 포트 스캔
      - CGI 공격
      - SMB probe
      - OS fingerprinting 시도와 같은 다양한 공격 감지 가능
    - 특징
      - 유연한 언어 사용으로 트래픽 분석
      - 모듈화된 탐지 엔진 지원
- 방화벽
  - TCP-Wrapper
    - 개요
      - 네느워크 서비스에 관련한 트래픽을 제어하고 모니터링 할 수 있는 UNIX 기반의 방화벽 툴
    - 특징
      - 임의의 호스트가 서비스 요청 -> 화이트리스트 확인 -> 호스트명 서비스명을 로그에 남김 -> 허가된 시스템에는 서비스를 제공하고, 허가되지 않은 경우에는 접속 차단
  - IPchain/IPtable
    - IPtable
      - 개요
        - 패킷 필터링 방화벽
      - 특징
        - 네트워크를 통과하는 모든 것이 패킷의 형태를 가지며, 패킷의 앞부분에는 패킷이 어디서 왔는지 어디로 향하는지, 어떤 프로토콜을 이용하는지 등과 같은 정보를 가지고 있음
