# Linux device

- 의문
- 장치 파일

## 의문

- *그냥 장치에 대한 부분이 잘 이해가 되지 않는다 ㅠ*

## 개요

새로운 장치가 주어지면, 커널이 사용자 공간과 어떤 방식으로 상호 소통하는지 이해하는 것이 중요

- udev
  - 사용자 공간 프로그램이 자동적으로 새로운 장치를 설정하고 사용할 수 있게 해줌
  - 커널이 udev를 통해서 메시지를 사용자 공간 프로세스에 전송하는 방법, 어떤일을 하는지에 대한 것까지 기본적인 운영에 대해서 살펴봄

## 3.1 장치 파일

- 유닉스 시스템상의 장치의 조작
  - 커널이 장치 I/O 인터페이스를 사용자 프로세스에 파일처럼 제공
    - *파일 처럼이라는 것은 파일이 아니라는 이야기인가? 정확히 정체가 무엇인가?*
- 위치
  - `/dev`
- 장치 파일 타입
  - Block
    - 데이터 접근이 가능한 장치
    - 프로세스는 커널의 도움으로 장치 안의 어떤 블록이든지 임의로 접근 가능
      - 주장치 번호와 부장치 번호 존재(`ls -alh`에서 날짜 앞 번호 두개)
      - 주장치 번호가 같으면 둘 다 같은 하드 디스크의 파티션이다
    - 예시
      - `sda1`
  - Character
    - 문자 장치는 데이터 스트림과 함께 작동
    - 문자를 읽거나 문자 장치로 문자 기록 가능
    - 문자장치는 크기를 갖지 않음
    - 읽거나 쓸 때, 커널이 장치상에서 읽고 쓰는 작업을 수행
    - e.g)
      - 프린터
  - Pipe
    - named pipe와 비슷함
      - 한 프로세스의 출력을 다른 프로세스의 입력으로 연결해주는 파이프의 하나
      - **파이프 역할을 하는 파일이 존재하여 이 파일을 통해 데이터가 전달**
  - Socket
    - 프로세스 간의 소통을 위해 사용되는 특수 목적의 인터페이스
    - `/dev` 디렉터리 외부에서도 볼 수 있음
- 참고
  - 모든 장치들이 장치 파일을 갖는 것은 아님
  - 네트워크 인터페이스는 장치 파일을 갖지 않음
    - 문자 장치를 이용해서 커뮤니케이션이 가능하나, 이는 매우 어려움

## 3.2 sysfs 장치 경로

### `/dev`의 단점

- 장치에 대해서 약간의 정보만 제공
- 장치들이 발견되는 순서에 따라서 커널이 장치들을 배정
  - 리부팅하면 다른 이름을 갖게 될 수도 있음

### sysfs

- 개요
  - 하드웨어 속성들을 근거로 연결된 장치들을 일정한 관점으로 볼 수 있도록 함
    - `/sys/devices`
  - 정보를 살피고 장치를 관리할 수 있게 함

## 3.3 dd

- 장치 블록 일부 복사
- `dd if=/dev/zero of=new_file bs=1024 count=1`
  - if=입력 파일
  - of=출력 파일
  - bs=블록 사이즈(한번에 어느정도 크기의 바이트의 데이터를 읽고 작성하는가)
  - count=복사되는 총 블록의 수

## 3.4 장치 이름 요약

- 장치 찾기
  - `udevadm`
    - `udevadm info --query=all --name=/dev/sda`

### 하드 디스크: `/dev/sd*`

- 개요
  - 하드 디스크는 대부분 `/dev/sda`, `/dev/sdb` 등, sd를 접두어로 가진 장치 이름을 갖는 경우가 많음
  - 커널은 `/dev/sda1`, `/dev/sda2`처럼 디스크상의 파티션들에 대하여 개별적인 장치 파일을 생성
- `sd`
  - SCSI(Small Computer System Interface) 프로토콜 디스크를 나타냄
    - USB도 통신을 위해 이 프로토콜 사용
- 참고
  - 리눅스는 드라이버들이 장치를 접하게 되는 순서에 따라서 장치에 장치 파일들을 할당

### 터미널: `/dev/tty*`, `/dev/pts/*`, `/dev/tty`

- terminal
  - 사용자 프로세스와 I/O 장치 간의 문자들을 옮기는 장치
- psudo terminal
  - 실제 터미널 I/O 기능을 이해하는 모조 터미널
- `/dev/tty1`
  - 첫 번쨰 가상 콘솔
- `/dev/pts/0`
  - 첫 번째 의사 터미널 장치
- `/dev/pts`
  - 전용 파일 시스템
- `/dev/tty`
  - 현재 프로세스의 제어 터미널
