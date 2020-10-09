# 리눅스 커맨드

- 꿀 커맨드
  - ;, &, &&
  - apt vs apt-get
- 꿀 터미널 키
- git
- awk
- ln

## 꿀 커맨드

- `du --max-depth=1 -ahl .`
  - 현재 디렉토리에 존재하는 파일 / 폴더의 디스크 사용량을 확인
- `git log -p -1`
  - 마지막 1개의 커밋의 코드 diff를 볼 수 있음
- `lsof -i -nP`
  - `lsof`자체는 openfile을 보는 커맨드
  - 특정 포트를 사용하는 프로세스 확인
  - `lsof -i -nP | grep LISTEN`
    - 실질적으로 포트를 사용하고 있는 프로세스의 확인(민규샘 감사!)
- `find dir -name file -print`
  - dir에 있는 이름이 file인 파일을 프린트 하자
  - 참고) `locate`는 인덱싱을 주기적으로 함 훨씬 빠름 대신 최신 파일 / 폴더 미반영
- `sort`
  - 텍스트 파일의 라인들을 글자와 숫자의 순서에 따라 빠르게 정렬
- `passwd`
  - 비밀번호 변경
- `sed -i 's/kr.archive.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list`
  - stream editor
  - `/etc/apt/sources.list` 속의 내용에서 `kr.archive.ubuntu.com`을 `ftp.daum.net`으로 변경
- `less`
  - 파일이 아주 크거나 명령에 대한 출력 내용이 너무 길어 화면 스크롤링이 필요할 때 출력 프로그램으로 사용
  - `space`, `b`: 다음 페이지, 이전 페이지
  - `/검색`: 검색
- `xxd ~.dcm | less`
  - 바이너리 파일 읽기 + space로 한페이지씩 보기
- `systemctl`
  - `systemd`라는 프로세스 관리하고, 유닛으로 서비스를 제어하는 시스템 자원 통합 관리 도구를 제어하는 커맨드
    - 데몬 관리
  - `systemctl start <service>`
  - `systemctl stop <service>`
  - `systemctl status <service>`
  - `systemctl enable <service>`
    - 서비스 활성화
    - 컴퓨터가 restart되어도 자동으로 동작하도록(daemonize)함
  - c.f) `journalctl`
    - 데몬 프로세스가 제대로 구동되지 않는 경우에 로그를 볼 수 있는 명령어
    - `journalctl -xe`
- `time <command>`
  - 커맨드를 수행하는데에 걸리는 시간 측정
  - e.g)
    - `time wget https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.19.9.tar.xz`
    - output
      - real
        - 시작과 끝까지의 모든 시간
      - user
        - user mode에서 사용된 CPU time
      - sys
        - kernel mode에서 사용된 CPU time

### ;, &, &&

- ;
  - 앞의 명령어가 실패해도 다음 명령어가 실행
- &&
  - 앞의 명령어가 성공했을 때 다음 명령어가 실행
- &
  - 앞의 명령어를 백그라운드로 돌리고 동시에 뒤의 명령어를 실행

### apt(Advanced Package Tool) vs apt-get

- apt
  - end user들이 사용하기 편하게 만든 툴
    - `apt-get`과 같은 backward compatible이 존재하지 않음

## 꿀 터미널 키

- `CTRL-P`
  - 이전 명령 보기
- `CTRL-N`
  - 다음 명령 보기
- `CTRL-W`
  - 이전 단어 삭제
- `CTRL-Y`
  - 삭제한 텍스트 붙이기(`CTRL-W`로 부터)

## git

- `git log`
  - 개요
    - 현재 브랜치의 커밋을 보여줌
  - `git log --branches --graph`
    - 브랜치와 커밋의 정보를 그래프로 보여줌
  - `git log -p -1`
    - 현재 브랜치의 커밋 중에서 가장 마지막 까지의 커밋의 내용을 보여줌
- `git diff`
  - `git diff commit_hash1 commit_hash2`
    - commit1과 commit2사이의 코드 차이를 보여줌
- `git revert` vs `git reset`
  - `git revert <commit>`
    - 결과적으로 commit 하나의 내용을 되돌리는데, 해당 커밋의 역연산의 커밋을 함
  - `git reset <commit>`
    - 결과적으로 commit 하나의 내용을 되돌리는데, 커밋 자체가 없었던 것 처럼 함

## awk

- `awk 'NR == 2 { print $0; exit }' [FILE]`
  - 특정 레코드만 출력

## ln

- 심볼릭 링크
  - `ln -s source destination`
  - 특징
    - 단순히 원본 파일을 가리키도록 링크만 시켜줌(바로가기)
    - 원본 파일의 크기와 무관
- 하드 링크
  - `ln source destination`
    - -f 옵션은 이미 destination 파일이 존재하면 그 파일을 지우고 링크 파일을 생성시킴
  - 특징
    - 파일이 original파일의 inode를 가리키게 함
      - 원본파일과 다른 이름으로 존재하는 동일한 파일
      - 삭제해도 나머지가 남아있음
      - 원본 파일의 내용이 변경되면 자동으로 같이 변경
