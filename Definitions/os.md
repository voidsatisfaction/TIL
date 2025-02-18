# OS 관련 정의

- 참고하면 좋은 자료
- 의문
- General
  - OS
    - 자원 관리
  - Device controller
  - Device driver
  - Booting
  - Firmware
  - BIOS
  - Buffer(data buffer)
  - POSIX
  - Everything is a file
  - Shell vs Terminal
  - Turing machine vs Modern computer
- Storage structure
- CPU
  - Computer System Architecture
- File system
  - File descriptor vs System open-file table vs Vnode Table
  - I/O multiplexing
    - select
    - poll
    - epoll
  - Partition
  - File system
  - Mount
  - Inode
  - Softlink vs Hardlink
  - file system types
    - UnionFS
- Process
  - Multiprogramming vs Multitasking
  - Program
  - Process
    - Daemon
    - Processor affinity
    - Process group
    - Pipeline
    - IPC
      - Signal
  - System Call
  - c.f) Interrupt
  - c.f) c.f) Green threads
- Memory
  - Address space
  - Virtual memory
  - Paging
  - Swap in and out
  - Memory segmentation
  - Overlay
  - OOM killer
  - Memory overcommitment
- Virtualization
  - OS-level virtualization
  - LXC
  - Virtualization
  - Server Virtualization
- Application Layer
  - deb

## 참고하면 좋은 자료

- [1. linux inside](https://0xax.gitbooks.io/linux-insides/content/SysCall/linux-syscall-2.html)

## 의문

- General
  - OS는 CPU architecture에 종속적인가?
    - 종속적이다
    - high level language가 아닌, 어셈블코드를 작성하는 부분이 존재
      - 인터럽트 관련이라던지
    - 모든 CPU 아키텍처가 Windows, Unix같은 general purpose OS를 서포팅 하는 것은 아님
  - linux 코드참조
    - https://github.com/torvalds/linux/tree/master/arch
- File system
  - *다음 설명은 참인가?*
    - 각 저장장치는 어떤 File system에 형식에 따라 데이터를 저장하는지 지정 가능(포맷)
    - 컴퓨터의 OS는 그 저장장치를 인식하면 지원하는 File system인지 확인한 후에, 지원한다면 해당 저장장치 내의 파일들에 접근 및 수정 가능
  - *unix-like os에서 장치 혹은 socket을 file로 관리한다는 것은 어떤것을 의미하는가?*
  - 우리가 그럼 commandline에서 보는 디렉터리 구조들과 같은 것들은 결국 정체가 무엇인가?
    - 하드 디스크 내부의 파일들의 메타 데이터
      - 우리는 데이터 저장장치의 Meta Area속에 존재하는 인덱싱된 파일 혹은 디렉터리의 메타 데이터를 보고 있는 것임
  - 파일 시스템의 부팅 영역이란
    - 무엇에 대한 부팅을 의미하는가? 컴퓨터? 아니면 저장장치? 애초에 부팅이 뭐지?
      - 컴퓨터의 부팅
  - *애초에 파일 시스템의 파일과 드리아브 크기 제한을 빵빵하게 만들면 될텐데 왜 제한이 빡빡하게 만들어서 계속 확장하게 되었는가?*
  - *구체적으로 Inode란 무엇인가?*
    - 무엇을 저장하는가?
- Memory
  - *Paging에 사용되는 TLB, Page Table역시 데이터를 저장해야 하는데, 해당 공간은 어디에서 나는가?*
    - *MMU?? 아니면 physical 메모리이긴 하나 별도 메모리에서 분리된 특수한 공간?*
- IPC
  - 인터럽트가 발생하면, 커널은 어떻게 하던 일을 멈추고 다음 동작을 행할 수 있는가?
    - 애초에 맞는 질문인건가?
      - 올바른 질문이 아님
    - 인터럽트는 OS 커널이 CPU에게 보내는 처리 요청 이벤트이다

## General

### OS(Operating System)

OS와 하드웨어의 도식

![](./images/os/os_and_hardwares1.png)

- 정의
  - 컴퓨터 하드웨어(자원)를 관리하는 소프트웨어
    - 컴퓨터 사용자와 컴퓨터 하드웨어 사이에서 중개자 역할을 함
    - 자원 할당자(관리자)
- 개요
  - 운영체제를 잘 이해하기 위해서는, 하드웨어의 구조를 잘 이해하는 것이 중요
    - c.f) 하드웨어
      - CPU, 메모리, 입출력 장치, 저장장치
  - 운영체제의 책임은 이러한 자원들을 프로그램에 할당하는 것
  - **일반적으로, 컴퓨터 시스템은 사용자의 문제 해결을 위한 도구인데, 자원 할당, 입출력 장치 제어와 같은 것은 OS에 위임**
    - **응용 프로그램은 오직 문제 해결에만 집중**
- 구성 요소
  - 커널
    - 항상 실행 중인 프로그램
  - 미들웨어 프레임워크
    - 응용 프로그램 개발을 쉽게 하는 기능을 제공
  - 시스템 프로그램
    - 시스템 실행 중에 시스템을 관리하는 데 도움이 되는 프로그램
    - *예시로 무엇이 있을까?*
- c.f) 컴퓨터 시스템의 구성
  - CPU, 구성요소, 공유 메모리 사이의 액세스를 제공하는 공통 버스, 장치 컨트롤러
    - *메인 메모리는 컨트롤러, 드라이버가 필요 없는건가?*
  - 장치 컨트롤러 마다 장치 드라이버가 존재
    - 장치 드라이버는 장치 컨트롤러의 작동을 잘 알고, 나머지 운영체제에 장치에 대한 일관된 인터페이스 제공
    - CPU와 장치 컨트롤러는 병렬로 실행
      - 메모리 사이클을 놓고 경쟁
    - 메모리 컨트롤러
      - 공유 메모리에 대한 접근을 질서 있게 하기 위해, 메모리에 대한 엑세스를 동기화함

#### 자원 관리

- 프로세스 관리
  - 사용자 프로세스와 시스템 프로세스의 생성과 제거
  - CPU에 프로세스와 스레드 스케줄하기
  - 프로세스의 일시 중지와 재수행
  - 프로세스 동기화를 위한 기법 제공
  - 프로세스 통신을 위한 기법 제공
- 메모리 관리
  - 메모리의 어느 부분이 현재 사용되고 있으며, 어느 프로세스에 의해 사용되고 있는지
  - 필요에 따라 메모리 공간을 할당하고 회수해야 함
  - 어떤 프로세스들을 메모리에 적재하고 제거할 것인가
- 파일 시스템 관리
  - 파일의 생성 및 제거
  - 디렉터리 생성 및 제거
  - 파일과 디렉터리를 조작하기 위한 프리미티브 제공
  - 파일을 보조저장장치로 매핑
  - 안정적인 저장 매체에 파일을 백업
- 대용량 저장장치 관리
  - 마운팅 언마운팅
  - 사용 가능 공간의 관리
  - 저장장소 할당
  - *디스크 스케줄링*
  - 저장장치 분할(partition)
  - 보호
- *캐시 관리*
  - 메모리 계층을 이용한 캐싱
    - 레지스터(컴파일러) - 캐시(하드웨어) - 메인메모리(OS) - 보조 메모리(OS)
  - 다중 프로그래밍 상황에서의 캐시 일관성 문제 해결
- 입출력 시스템 관리
  - 사용자에게 특정 하드웨어 장치의 특성 숨기기
    - 장치 드라이버만 장치 특성 인식

### Device controller

Device controller와 device driver의 관계

![](./images/os/device_controller_device_driver1.png)

OS <-> Device driver <---(bus)---> Device controller <--(socket)-(plug)--> Device

- 정의
  - CPU의 incoming, outcoming 시그널을 이해하는 하드웨어 유닛
- 개요
  - 하나의 디바이스는 플러그와 소켓으로 컴퓨터와 연결되어 있고, 소켓은 device controller와 연결되어있음
    - 즉, 컴퓨터에 붙은 하드웨어임
  - 시스템 내부의 bus와도 연결되어 있음
    - 이 bus는 결국 device driver와 연결되어 있음
  - local buffer가 존재
  - device를 담당함
- 장치 - OS 커뮤니케이션
  - 1 연결된 장치로부터 데이터를 받아, 컨트롤러 내부의 특별 레지스터(local buffer)에 임시적으로 저장
  - 2 device driver와 통신
  - 3 각각의 device controller마다, 대응하는 device driver가 있고, device controller는 device driver를 이용하여 특히, interrupt를 통해 OS와 통신
- 역할
  - OS로부터 커맨드를 받음
    - read, write 등
    - 각 device controller는 자신의 커맨드의 집합을 갖고 있음
  - 연속된 bit stream을 바이트 블록으로 변환
  - 에러 교정

### Device driver

결국, 드라이버를 만드는 제작사는, OS가 정한 인터페이스에 맞춰서 기능을 설계해야하는 것인가? - 그렇다

- 정의
  - 특정 하드웨어를 제어하기 위한 커널의 일부분으로 동작하는 프로그램
    - OS가 각각의 디바이스를 접근하게 하기위한 인터페이스 역할을 하는 소프트웨어
- 특징
  - 커널의 일부분이긴 하지만, 커널과 통합되는 경우에 여러 시나리오가 존재
    - 해당 드라이버 프로그램 자체가 커널 소스에 포함되어 컴파일
    - 별도로 컴파일된 파일(*.sys, *.o)형태로 존재하고, 부팅시 또는 필요시 해당 파일이 로드되어, 커널과 통합
  - 장치 컨트롤러의 작동을 잘 알고 있고, 나머지 운영체제에 장치에 대한 **일관된 인터페이스 제공**
    - 프로그램이 드라이버의 명령어 호출 -> 드라이버는 장치에 명령어를 전달 -> 장치가 드라이버에게 데이터를 되돌려 줌 -> 드라이버는 원래 요청한 프로그램의 명령어로 데이터를 다시 전달
  - 장치 드라이버는 장치 칩의 레지스터에 접근하여 하드웨어를 제어

Device driver와 interrupt의 관계

![](./images/os/device_driver1.png)

- 하드웨어에서 입력 받음
- 디바이스 컨트롤러에서 인터럽트 발생
- IRS 실행
  - device driver의 처리 함수 호출
  - 인터럽트 처리
- 인터럽트 처리 후 다시 유저모드로 복귀

### Booting(운영체제를 initializing(메모리에 올리는 것))

Booting process

![](./images/os/booting_process1.png)

Bootstrap

![](./images/os/bootstrap1.png)

- 정의
  - 운영체제 프로그램을 메모리에 올리는 것
- 과정
  - ① 컴퓨터 전원버튼을 누르고, 메인보드에 전력이 들어오며, 메인보드에 부착된 장치들에게 전력이 공급
  - ② CPU가 ROM에 저장된 펌웨어인 BIOS(Basic Input/Output System)를 실행시킴
  - ③ 실행된 BIOS는 POST(Power On Self Test)즉, 컴퓨터 주변 하드웨어를 체크
    - POST
      - 컴퓨터를 킬 때, 문제가 있나 자가검사 하는 것
  - ④ BIOS가 부팅매체(하드디스크, USB, SSD, ...)를 선택하고, 부팅매체의 MBR(부팅 프로그램이 저장된 영역)에 저장된 부트로더를 RAM으로 읽어오는 Bootstrap을 실행
    - 부팅 우선순위가 존재함(e.g 하드디스크 -> USB -> CD -> Network -> ...)
    - MBR(Master Boot Record)
      - 모든 기억장치(USB, 하드디스크 등)은 첫 번째 섹터(512바이트)에 MBR영역을 갖고 있음
      - Primary partition에 대한 정보 4개를 기록할 수 있는 64바이트 공간 + 운영체제(커널) 코드를 복사해서 메모리에 올려주는 부트 로더가 저장
        - 부트 로더를 RAM 메모리에 올리는 것을 **부트스트랩 과정** 이라 함
  - ⑤ Bootstrap 과정으로 RAM에 Bootloader가 올라가고, 부트로더는 디스크에 있는 OS(커널) 코드를 복사해 RAM에 올려 OS 실행
    - Bootloader
      - 운영체제를 initializing(메모리에 올림) 해주는 역할
  - ⑥ OS가 부팅됨
    - 메모리에 커널이 올라가서 실행
    - `systemd` 시스템 프로그램에 의해, 커널 외부에서 시스템 데몬 제공

### Firmware

- 정의
- 특징
  - ROM과 같은 비휘발성 메모리에 저장해 사용
- 종류
  - BIOS, ...

### BIOS(Basic Input Output System)

- 정의
- 특징
  - 하드웨어들의 Input / Output을 관리하는 소프트웨어
  - 운영체제가 컴퓨터 하드웨어의 입출력을 컨트롤 할 경우에 사용

### Buffer(data buffer)

- 정의
  - 데이터를 한 장소에서 다른 장소로 이동시키는 동안, 임시적으로 저장하기 위해 사용되는 물리적 메모리 저장 장소
- 특징
  - 주로 queue를 이용해서 input, output의 timing을 조정함
- 예시
  - device에 관련
    - input device로 부터 데이터를 가져오기 전에 buffer에 데이터가 저장됨
    - output device로 데이터를 내보내기 전에 buffer에 데이터가 저장됨
  - 하나의 컴퓨터 안에서 process간에 데이터를 옮기기 위해서도 사용됨

### POSIX

- 정의
  - Portable Operating System Interface
  - **OS 사이의 compatibility를 유지하기 위하여 IEEE가 제정한 OS 인터페이스 표준**
- 정의 범위
  - API
  - Shells
  - Utility interfaces
- 윈도우와 POSIX
  - Cygwin
  - WSL(Windows Subsystem for Linux)

### *Everything is a file*

- 정의
  - Unix의 특징 중 하나
  - **다양한 범위의 input/output 자원은 filesystem name space를 통해서 노출된 simple streams**
    - documents, directories, hard-drives, modems, keyboards, printers, inter-process, network communications
- 특징
  - 같은 툴이나 유틸리티와 API가 다양한 범위의 자원으로 활용 가능
  - 다양한 파일 타입이 존재
  - **정확히는 Everything is a file descriptor가 맞음**
  - psudo, virtual filesystem들도 존재해서, file-like 구조로 시스템의 정보나 프로세스의 정보를 노출
    - mount됨
    - virtual filesystem의 예시
      - `/proc`
        - owner, access permissions등의 유닉스 파일 속성을 갖음

### Shell vs Terminal

- Shell
  - 터미널에 부착된, shell 인터프리터
- Terminal
  - 컴퓨터에 접속하기 위한 장치(프로그램)
- c.f) `docker run -it ...`
  - `-i`
    - container가 stdin을 받을 수 있도록 함
  - `-t`
    - 현재의 쉘을 conatiner의 terminal에 부착
      - 쉘을 터미널에 부착한다는게 무슨 의미인가?
        - 쉘은 쉘 스크립트를 실행하는 인터프리터. 그것을 터미널에 부착한다는 것
      - 터미널이 실행되면 해당 쉘 프로그램을 실행한다는 의미?
  - 예시
    - `-i`만 존재하는 경우
      - `-t`가 없으므로, 명령어를 치면 stdout은 나오나, 그것이 다소 이상하게 보임
    - `-t`만 있는 경우
      - `-i`가 없으므로, 명령어를 쳐도 container에 반영되지 않음

### Turing machine vs Modern computer

![](./images/os/turing_machine_vs_modern_computer1.png)

- 이론상의 컴퓨터
  - 튜링 머신
- 컴퓨터의 실제
  - 현대 컴퓨터

## Storage structure

저장장치 계층 구조

![](./images/os/storage_hierarchy_structure1.png)

## CPU

- Processor
  - CPU를 포함하는 물리적 칩
- CPU
  - 명령을 실행하는 하드웨어
- Core
  - 명령을 실행
  - 레지스터를 포함
- c.f) 특수목적 processor
  - 장치별 프로세서
    - 디스크, 키보드, 그래픽 컨트롤러
  - e.g) 디스크 컨트롤러 마이크로프로세서
    - 주 CPU로부터 연속된 요청을 받아들여 자기 고유의 디스크 큐와 스케줄링 알고리즘 구현
  - e.g) PC의 키보드
    - 키스트로크를 CPU에 전송할 코드로 변환하는 마이크로세서를 가지고 있음

### Computer System Architecture

- Single-Processor Systems
  - 개요
    - 1CPU - 1Core
- Multiprocessor Systems
  - Multiprocessor
    - 개요
      - NProcessor - 1CPU
    - 특징
      - N프로세서의 속도 향상의 비율은 N이 아님
      - 프로세서는 시스템 버스를 통해 물리 메모리 공유
  - Multicore
    - 개요
      - 1Processor - NCPU
    - 특징
      - 칩 내 통신이 칩 간 통신보다 빠름(효율적)
      - 적은 전력 사용
      - 칩 내 CPU간 캐시 공유 가능
      - N개의 다중코어 프로세서는 운영체제에게는 N개의 CPU로 보임
  - NUMA(Non-Uniform Memory Access)
    - 배경
      - CPU를 너무 많이 추가하면, 시스템 버스에 대한 경합이 병목이 되어 성능 저하 발생
    - 개요
      - 각 CPU에 작고 빠른 로컬 버스를 통해 액세스 되는 자체 로컬 메모리 제공
        - 버스에의한 경합이 발생하지 않음
      - 모든 CPU가 공유 시스템 연결로 연결되어, 모든 CPU가 하나의 물리 주소 공간을 공유
    - 장점
      - CPU추가에 따른 버스 경합 발생하지 않음
    - 단점
      - 한 CPU가 원격 메모리에 엑세스할때 오버헤드 발생
        - 운영체제가 CPU스케줄링, 메모리관리를 통해 단점 최소화
- Clustered Systems
  - 개요
    - 둘 이상의 독자적 시스템 또는 노드(머신)들을 연결하여 구성
  - 구조
    - 저장장치 공유
    - LAN으로 연결
  - 장점
    - 높은 가용성
      - 하나 이상의 시스템이 고장나더라도 서비스는 계속 제공
    - 병렬화 가능
  - c.f) Hadoop
    - 개요
      - 클러스터형 시스템에서 빅데이터의 분산 처리에 사용되는 공개 소스 소프트웨어 프레임워크
      - 작업은 클러스터의 노드에 할당
        - 병렬 계산을 관리하고, 결과를 통합
      - 노드 장애 감지 / 관리
    - 요소
      - 분산 파일 시스템
      - 클러스터 내 자원 관리, 노드에 작업 스케줄
      - MapReduce
        - 클로스터의 노드에서 데이터를 병렬 처리할 수 있게 함

## I/O structure(Interrupt)

- 종류
  - 인터럽트 구동 I/O의 형태
    - 소량의 데이터 이동하는 데에 좋음
  - **DMA(Direct Memory Access)**
    - 개요
      - device controller가 CPU의 개입 없이 직접 메모리 액세스(메모리에 저장, 혹은 메모리로부터 가져오기)
        - NVS(Non volatile Storage) I/O와 같은 대량 데이터 이동에 사용됨
    - 동작
      - device controller가 CPU의 개입 없이, 메모리로부터 자신의 버퍼 장치로 or 버퍼로부터 메모리로 데이터 블록 전체를 전송
      - 인터럽트는 블록 전송이 완료될 때 마다 발생(raise)
        - device controller가 전송 작업을 수행하고 있는 동안, CPU는 다른 작업 수행 가능
      - *구체적으로 어떤 원리로 동작하는것인가? CPU와 메모리 사용이 겹쳐버리면 어떻게하나?*

## File system

*파일 시스템에서 파일과 inode는 어떻게 연결되는가? 파일 이름은 어디에 저장되는가?*

### File descriptor vs System open-file table vs Vnode Table

파일 그 자체와, 파일로 연결을 open하는 것은 차이가 존재함

File descriptor, File table, Inode table1

![](./images/os/file_descriptor_file_table_inode1.png)

File descriptor, File table, Inode table2

![](./images/os/file_descriptor_file_table_inode2.png)

File descriptor, File table, Inode table3

![](./images/os/file_descriptor_file_table_inode3.png)

- file descriptor
  - 정의
    - Unix계열의 OS에서(POSIX), file이나 input/output 자원을 접근하기 위해서 사용하는 abstract handler(indicator)
    - file descriptor는 **per-process file descriptor table** 이라는 곳으로 인덱싱 되며, 각각의 file descriptor는 **(open)file table** 이라고 불리는 시스템 전체의 scope인 모든 프로세스에 의하여 open된 파일들을 담는 테이블과 연결이 됨
      - file table은 file의 mode를 기록(reading, writing, appending, other modes)
    - file table은 inode table과도 인덱싱되어서, 실제 파일이 어디있는지와도 대응이됨
    - e.g)
      - `pipe`, `network socket`
  - 특징
    - POSIX API에 포함됨
    - 음이 아닌 정수
      - `C File*`로 open된 file descriptor를 `int fileno(FILE* fp);` 함수로 가져올 수 있음
    - 유닉스 계열의 시스템에서는, 유닉스 파일 타입이라고 명명된 모든 것을 참조할 수 있음
      - regular files, directories, block, character device, unix domain sockets, named pipe 등
        - 그래서 `lsof`커맨드로 소켓등도 확인할 수 있는것임
    - 유닉스 계열 시스템에서의 fd에의 operations
      - fd의 생성
        - `open()`
        - `socket()`
        - `pipe()`
        - `epoll_create()`(linux)
        - ...
      - 하나의 fd에 대한 operation
        - `read()`, `write()`
        - `recv()`, `send()`
        - `fstat()`
        - `fchmod()`, `fchown()`
        - ...
      - 여러 fd에 대한 operation
        - `select()`
        - `poll()`
        - `kqueue()`
        - ...
      - fd-table에 대한 operation
        - `close()`
        - `dup()`
        - `fcntl()`
      - file locking
        - `flock()`
        - `fcntl() (F_GETLK, F_SETLK and F_SETLKW)`
        - `lockf()`
      - Sockets
        - `connect()`
        - `bind()`
        - `listen()`
        - `accept()`
        - `getsocketname()`
        - `getsocketopt()`

three standard POSIX file descriptors

|Integer value|Name|`<unistd.h>` symbolic constant|`<stdio.h>` file stream|
|-------------|----|-------------------------------|----------------------|
|0|(해당 프로세스의) Standard input|STDIN_FILENO|stdin|
|1|(해당 프로세스의) Standard output|STDOUT_FILENO|stdout|
|2|(해당 프로세스의) Standard error|STDERR_FILENO|stderr|

- system open-file table(file table)
  - 정의
    - 하나의 파일에 대한 connection을 트래킹 하기 위한 테이블(kernel에서 관리)
  - 특징
    - 각각의 엔트리는 connection status를 갖음
      - read, write
      - 파일의 current offset
      - vnode의 pointer
- vnode table
  - 정의
    - open file이나 device에 대한 엔트리를 갖는 테이블(kernel에서 관리)
    - 각 엔트리는 vunode라고 함
      - 파일에 대한 메타데이터, *pointers to functions that operate on the file.*
        - *정확히 어떤 함수의 포인터를 말하는 것인지*
  - 특징
    - inode의 copy를 갖음

각각의 개념은 reference count를 갖으며, reference count가 0이 되어야만 각각의 entry를 삭제 가능 >> 그래서 파일이 열린 상태에서는(다른 프로세스가 해당 파일을 참조하고 있음) 삭제가 불가능했던것임

*만약 파일을 close하지 않은 상태로 프로세스가 종료된다면 무슨 일이 벌어지는가? 그냥 system open-file table에 대응하는 entry를 process종료 전에 dereference시켜주는가?*

### **I/O multiplexing**

- 정의
  - **하나 이상의 I/O대상(file descriptor)이 준비가 될 때 kernel로부터 notification을 받는 것**
    - file descriptor의 이벤트 감지
    - *결국 커널 내부적으로는 무한 루프를 도는 것인지*
- 예시
  - I/O대상은 Unix의 경우에는 파일로 나타나는 모든 것
    - client가 다수의 file descriptor들을 다룰 때(stdin, stdout, network socket) - file
    - client가 다수의 socket을 다룰 때 - file
    - TCP server가 연결 listen과 생성된 client socket을 다룰 때 - file
    - 서버가 TCP, UDP를 동시에 다룰 때 - file
- 방식
  - `select`
    - `O(n)`
  - `poll`
    - `O(n)`
  - `epoll`
    - `O(1)`
  - *세 방식의 구체적인 차이는 무엇인가?*

### File descriptor

- 정의
  - **file을 포함한 input/output 자원을 위한 고유의 식별자**
    - e.g) file, directory, pipe, network socket, block(device driver)
- 구조
  - file descriptor <-> file table <-> inode table
- 특징
  - non-negative integer values
  - POSIX API에 포함
  - 각 Unix process는 3가지 file descriptor를 반드시 갖음(daemon빼고)
    - 0: standard input
    - 1: standard output
    - 2: standard error
  - **input, output을 행하기 위해서, system call을 사용하고, kernel이 process대신 접근함**
    - 유저 프로세스가 직접 file이나 inode table에 접근 불가
  - Linux에서는, 한 프로세스에서 열린 fd를 `/proc/PID/fd`에서 확인 가능

### Partition

- 정의
  - 하나의 물리적인 하드디스크에 논리적으로 분할 영역을 만드는 것
  - 하나의 하드디스크를 서로 별개의 하드디스크 처럼 쓰기 위해서 분할하는 것
- 특징
  - 파티션을 나누면 서로 다른 드라이브로 인식
    - C드라이브에 심각한 오류가 발생해도 D드라이브에 있는 파일들은 안전하게 보존 가능
    - 윈도우를 2개이상 설치해서 사용하는 멀티부팅 가능
    - 중요 데이터만 따로 보관 가능

### File system

- 정의
  - **저장장치의 파티션 내에서 클러스터 단위의 데이터를 배치하고 관리하기 위한 논리적 체계(저장장치의 파티션 별로 하나씩 둘 수 있음)**
    - 특정 데이터가 하드웨어 파티션 상에서 어디서부터 어디까지 저장된 것인지 파악
    - 사실상, 저장장치의 데이터를 인덱싱하는 것
      - 인덱싱 할 때, 키(파일 이름: case sensitivity, suffix의 길이)와 value(파일 내용 or 내용 크기 등)에 관한 스펙을 다 정해줌
    - 파일에 대한 메타데이터도 다 가지고 있고, 따로 관리
      - 메타데이터는 Unix-like 시스템에서 `inode`의 데이터 구조로 저장됨
      - *우리가 윈도우즈 탐색기로 파일들을 파악하는 것은 다 메타데이터로 하는 일(?)*
- 등장 배경
  - ① 클러스터와 블록개념의 도입
    - 하드 디스크를 단순히 실린더로 관리하면 큰 파일의 데이터를 읽고 쓰는데 너무 느린 문제가 발생
      - e.g) 10MB 파일 하드디스크로부터 읽기
        - 2 * 1024 * 10 개의 섹터(0.5KB)를 불러와야 함
    - **클러스터, 블록의 도입** (섹터들을 한 번에 여러 개를 읽는 기술 도입)
      - 섹터 한개 단위가아니라, 다수의 섹터 단위로 묶어서 읽고 저장
      - 대신, 한번에 여러 섹터를 읽으면 빈 섹터를 읽어버리는 경우가 존재(e.g 한 번에 4개의 섹터를 읽는데, 마지막엔 2개만 읽어도 충분한경우)
        - **Slack space**
      - 클러스터 => 윈도우 운영체제에서 사용되는 용어
      - 블록 => 유닉스 계열 운영체제에서 사용되는 용어
    - 블록(클러스터)를 몇 개의 섹터로 계싼하는 지는 파일 시스템 마다 다름!
    - **물리적으로는 클러스터, 또는 블록이라는 대응체가 없으므로, 블록이라는 것을 파일시스템이 소프트웨어적으로 계산해줘서 운영체제가 사용할 수 있는게 함**
      - 클러스터, 블록 이라는 단위를 계산해주는 것도 파일시스템의 역할 중 하나
    - 파일 시스템 덕분에 운영체제는 블록(클러스터) 단위로 데이터를 사용할 수 있는 것
      - 파일 시스템은 운영체제에 포함되어있음
  - ② 효율적으로 디스크의 데이터를 관리하는것의 필요성(파일의 삭제, 편집)
    - 섹터에 저장된 기존 파일의 크기가 더 커지면?
      - 같은 트랙에 데이터가 꽉 찼다면, 다른 빈 트랙에 넣어야 하는데, 컴퓨터가 다른 트랙의 어디에 저장되어있는지 어떻게 알 수 있는가?
    - 섹터에 저장된 기존 파일의 크기가 줄어들거나, 지워졌을 때는?
      - 트랙 중간중간에 빈 섹터가 생겨남
      - 디스크 모음의 필요성
- 역할
  - Each different filesystem provides the host operating system with metadata so that it knows how to read and write data. When the medium
  - 디스크의 데이터를 더 빠르게 읽고 저장할 수 있는 블록(클러스터)를 소프트웨어적으로 계산
  - 분산 저장된 연관 데이터들을 빠르게 찾게 해줌(인덱싱)
  - 디스크 조각(섹터) 모음과 같이 디스크 공간을 효율적으로 사용하게 해줌
- 블록(클러스터) 계산 방식(Addressing)
  - CHS(Cylinder-Head-Sector)
    - 물리적 주소 지정 방식
    - 실린더와 헤드 섹터 순으로 주소를 지정
    - 초창기에 사용
  - LBA(Logical Block Addressing)
    - 논리적 주소 지정 방식
      - 마치 3D 디스크 공간이 한 줄인양 할당이 됨
    - BIOS(Basic Input/Output System)
      - 실제 디스크 섹터 위치 <--> 논리적 섹터 위치 변환
    - 파일 시스템은 BIOS가 구현한 LBA를 이용해서 데이터를 효율적이게 관리하고 사용할 수 있게 블록(클러스터)계산
      - 블록(클러스터)은 LBA에서 논리적인 개념이 되어버림
    - 현재에도 사용중
    - **LBA에 의해서, 파일시스템은 섹터, 트랙, 실린더를 다루는 것이 아닌, 블록(클러스터) 기준으로 데이터를 다룸**

파일 시스템의 추상화 구조

![](./images/os/file_system_abstraction1.png)

- 파일시스템의 추상화 구조(Meta Area, Data Area)
  - Meta Area
    - 데이터에 대한 데이터들이 저장되는 장소(인덱싱)
      - Linux의 I-node
      - 데이터의 블록 위치를 효율적으로 파악 가능
  - Data Area
    - 데이터를 저장하는 장소
- 특징
  - 저장공간을 사용한다면 무조건 필요한 소프트웨어이며, 운영체제에 무조건 필수적으로 포함 되어야 함
  - 저장장치의 종류마다 각자의 파일 시스템을 사용
    - 파일 하나의 크기 제한, 전체 디스크에 대한 크기 제한, 파일에 대한 저장 방식 등이 다 다름
  - local data storage 뿐 아니라, Network protocol을 이용한 파일 시스템을 사용하여 원격 서버의 파일을 제어가능
  - 특정 유저나 유저의 그룹만 파일이나 폴더를 읽고 쓸 수 있게 설정 가능

FAT 파일 시스템의 구조

![](./images/os/file_system_fat_example1.png)

NTFS의 구조

![](./images/os/file_system_ntfs_example1.png)

ext2의 구조

![](./images/os/file_system_ext2_example1.png)

- 파일 시스템의 종류와 역사
  - FAT(File Allocation Table)
    - 종류 및 특징
      - FAT12
        - 2^12개수의 클러스터를 가질 수 있음
      - FAT32
        - USB에 자주 쓰임
        - 지원하는 최대 드라이브 크기는 32GB, 한 파일당 4GB
          - 4GB 이상 크기의 파일을 USB에 옮기려 하면, 파일 시스템을 바꿔야 함
    - 구조
      - Reserved Area
        - 예약된 행위 정보들이 들어있는 곳
        - Boot Block
          - 컴퓨터 부팅에 관련된 정보들이 들어있는 블록
        - FSINFO(File System INFOrmation) Block
          - 운영체제에게 알려줄 파일 시스템 정보가 있는 블록
        - 추가 예약 공간 블록
      - FAT Area
        - Meta Area
        - 파일에 얼마나 클러스터가 할당 됐는지 적혀있는 테이블(File Allocation Table)
          - 어떤 파일에 얼마나 많은 클러스터가 할당됐는지, 어디 있는지, 언제 수정되고 만들어졌는지 등의 정보 존재
      - Data Area
        - 데이터가 저장된 공간
  - NTFS(New Technology File System)
    - 특징
      - 디스크 크기 256TB
      - 한 파일 크기 제한 16TB
      - 디스크 복구 기능 존재
      - 서버용으로 사용 가능
    - 구조
      - VBR(Volume Boot Record)
        - 부팅에 관련된 정보들이 저장된 공간
      - MFT(Master File Table)
        - Meta Area
        - FAT Area와 유사
      - Data Area
        - 데이터가 저장된 공간
  - ext(extended file system)
    - 종류 및 특징
      - ext1
        - 2GB까지 용량 지원 파일 이름 255글자까지 지원
        - VFS 시스템 도입
          - 각각 파일 시스템의 정보들을 일관되게 가상적으로 같은 정보처럼 만들어서 운영체제에서 같이 사용할 수 있게 함
          - *구체적인 예시?*
        - 단편화 문제
          - 디스크 저장 공간 중간중간에 빈 공간이 생기는 현상
      - ext2
        - 2TB까지 용량 지원
        - 한 파일 크기 16GB까지 지원
        - i-node 기능 지원
        - 리눅스의 본격적인 파일 시스템 형태
        - 데이터를 저장하는 동안 전원이 끊기면 심각한 손상이 일어남
        - 블록 그룹 사용
          - 블록들의 집합
        - 구조
          - Boot Sector
            - 블록크기 까지는 필요 없는 부팅에 관한 정보들이 저장된 공간
          - Block Group
            - Super Block
              - 모든 블록에 해당되는 공통 정보들을 관리하는 블록
              - 블록의 크기, 총 블록의 개수, 블록 그룹의 개수, 블록 그룹 내 블록과 아이노드 개수
              - 중요하므로, 모든 블록 그룹의 맨 앞에 복사본을 만들어놓음. 사용은 첫번째 블록그룹에 속한 것만 함
            - Group Descriptor Table
              - 블록 그룹들의 데이터들이 어떻게 저장 됐는지 알려주는 데이터가 들어있음
                - Block Bitmap의 번호(위치)
                - Inode Bitmap의 번호(위치)
                - 블록 그룹안에 있는 빈 블록, 빈 디렉토리 수
                - Inode 수
                - Inode 테이블 번호(위치)
              - 모든 블록 그룹에 복사본이 존재
            - Block Bitmap
              - 사용되고 있는 블록이 몇개인지 기록
            - Inode Bitmap
              - 사용되고 있는 Inode가 몇개인지 기록
            - Inode Table
              - Inode들이 기록된 테이블
              - Inode한 개의 크기가 128Byte
            - DATA
      - ext3
        - 저널링 기술 도입
          - 디스크에 정보를 변경하기 전에 변경사항들을 저널이라고 부르는 로그 공간에 미리 기록
          - 디스크에 정보를 저장하던 도중에 전원이 끊겨도, 저널 로그를 보고 복구 가능
      - ext4
        - 1엑사 바이트 디스크 크기
        - 파일당 16테비 바이트 지원 2^40
  - XFS
    - 64비트 저널링 파일시스템
    - Redhat Linux 7버전 부터 기본 파일 시스템으로 채택
    - Centos 7 버전 부터 기본 파일 시스템으로 채택
    - 속도가 매우 빠름
- c.f) 포맷
  - 저장장치의 파일 시스템을 설정하여, 데이터 저장 장치를 준비하는 작업
  - 다만, 파일 시스템을 변경할 때, 저장 장치의 내용을 모조리 삭제하므로 보통은 이런 의미로 잘못되어 사용됨
- c.f) I-node
  - 개요
    - `ls -li` 이라는 명령어로 확인 가능
      - `i`는 i-node의 번호 조회
    - i-node list table에 i-node정보를 저장
  - 구성
    - 파일 형식
    - 파일 권한
    - 링크 수
    - 파일 소유주
    - 파일 그룹
    - 파일 크기
    - 파일이 만들어진 시간

### Mount

- 정의
  - OS가, storage device에 있는 파일과 디렉터리를, 유저가 컴퓨터의 파일 시스템을 통해서 접근할 수 있도록 만드는 과정
    - *근데 결국 디렉터리 구조에 편입시킨다는 것은 다른 파일 시스템(메인 파일 시스템??)과 연결 시킨다는것 아닌가?*
      - e.g) 리눅스에 usb를 연결 시키면, 특정 위치의 디렉터리가 생겨서 usb에 접근 가능(usb 내부의 경로도 인터페이스 변경 없이 터미널로 접근 가능)
- 과정
  - storage device에 접근 권한 획득
  - 인식
  - 읽기
  - 파일 시스템 구조와 메타데이터 processing
  - VFS(Virtual File System) 컴포넌트로 등록
- mount point
  - 새로 마운트 된 저장 장치 파티션의 VFS상의 location
    - *애초에 우리가 아는 절대경로 / 등은 그냥 VFS의 인터페이스?*
  - 마운트 프로세스가 끝나면 이 장소에서 파일과 디렉터리를 접근 가능
- unmount
  - OS가 mount point에 있는 파일과 디렉터리에 대한 모든 유저접근을 막음
  - 큐에 남아있는 유저데이터를 스토리지 디바이스에 넘겨줌
  - file system metadata를 refresh 해줌
  - 디바이스에 접근을 포기함
    - 안전한 디바이스 제거 가능하게 함

### Inode

*파일의 이름은 파일시스템의 어디에 저장되는것인지?*

- 정의
  - 유닉스 계통 파일 시스템에서 사용하는 자료구조
    - 정규 파일, 디렉터리 등 파일 시스템에 관한 정보를 가지고 있음
- inode에 포함된 정보
  - `ls -alh`의 필드
    - 파일 모드(16비트 플래그)
      - 파일 형식(-, d, b, c, p, ...)
      - *실행 플래그*
        - 이게 뭐야?
      - 소유자 rwx
      - 그룹 rwx
      - 다른 사용자 rwx
    - 소유자 아이디
    - 그룹 아이디
    - 파일 크기
    - 마지막 수정 시각
    - 파일 주소(39바이트)
  - 그 외
    - 링크 수
    - 마지막 접근 시각
    - 아이노드 수정 시각
- 특징
  - 파일들은 각자 1개의 inode를 가지고 있음
  - 일반적으로 파일 시스템을 생성할 때 전체 공간의 약 1%를 inode를 위해 할당
    - 따라서, 파일 시스템이 가질 수 있는 파일 최대 개수도 한정적(사실상 사용자가 느끼기에는 무한대로 생성가능)

### Softlink vs Hardlink

Simplified hardlink illustration

![](./images/os/simplified_hardlink1.png)

- Softlink
- Hardlink

Softlink storage

Early implementations of symbolic links stored the symbolic link information as data in regular files. The file contained the textual reference to the link's target, and the file mode bits indicates that the type of the file is a symbolic link.

This method was slow and an inefficient use of disk-space on small systems. An improvement, called fast symlinks, allowed storage of the target path within the data structures used for storing file information on disk (inodes). This space normally stores a list of disk block addresses allocated to a file. Thus, symlinks with short target paths are accessed quickly. Systems with fast symlinks often fall back to using the original method if the target path exceeds the available inode space. The original style is retroactively termed a slow symlink. It is also used for disk compatibility with other or older versions of operating systems.

Although storing the link value inside the inode saves a disk block and a disk read, the operating system still needs to parse the path name in the link, which always requires reading additional inodes and generally requires reading other, and potentially many, directories, processing both the list of files and the inodes of each of them until it finds a match with the link's path components. Only when a link points to a file in the same directory do "fast symlinks" provide significantly better performance than other symlinks.

The vast majority of POSIX-compliant implementations use fast symlinks. However, the POSIX standard does not require the entire set of file status information common to regular files to be implemented for symlinks. This allows implementations to use other solutions, such as storing symlink data in directory entries. - Wikipedia

### File system types

#### UnionFS

- 정의
  - 다른 file system과의 union mount를 구현한 Linux, FreeBSD, NetBSD용 파일 시스템
    - *여기서 다른 file system 이라는 것은 같은 UnionFS 계열의 FS를 말하는 것인가? 아니면 ext4 이런 파일 시스템도 지원이 가능하다는 것인가?*
  - c.f) union mount
    - 다수의 디렉터리를 하나의 디렉터리로 합쳐서, 결합된 컨텐츠 처럼 보이게 하는 것
    - *e.g) CD-ROM 또는 DVD 안에 있는 컨텐츠를 업데이트 할경우, CD의 마운트 포인트를 union mount에 있는 writable directory로 overlay할 수 있고, 그 다음에, union directory 속에 있는 파일들을 업데이트하면 결국에는 writable directory로 만드는 것과 같음*
      - *애초에 CD-ROM이 Read-only인데 파일 시스템을 overlay하고 union directory속의 내용을 바꾼다고 정말 내부 내용이 바뀌는가?*
- 특징
  - 분리된 파일 시스템의 디렉터리와 파일들을(branches) 투명하게 overlay해서 하나의 일관성 있는 파일 시스템으로 만듬
    - 같은 경로에 있는 디렉터리의 컨텐츠들은 새 virtual fs의 하나의 통합된 디렉터리 안에서 같이 보이게 됨
  - branch들을 마운트 하는 경우에는, priority가 명시됨
    - 같은 브랜치가 같은 이름의 파일을 갖고 있다면, 우선순위가 높은쪽을 보게 됨
  - *각 브랜치는 read-only 혹은 read/write 파일 시스템이 될 수 있어서, 그 경우에는 merged copy는 특정한 real file system으로 보내짐*
    - *이게 무슨소리?*
    - Copy on Write
    - e.g) Live CDs
  - docker
    - *docker image의 레이어화를 시키기 위해서 사용됨*
      - *구체적으로 어떤 원리인지?*
      - 각 레이어마다 실행되고나서의 fs상의 이전레이어의 state와의 state diff를 저장?
- 다른 unionfs 구현체
  - aufs
  - overlayfs

## Process

### Multiprogramming vs Multitasking

- Multiprogramming
  - 개요
    - CPU가 항상 한 개는 실행할 수 있도록 하여, CPU의 이용률을 높이는 것
    - CPU가 I/O작업을 수행하거나 하드웨어에서의 작업을 기다릴 때, 자원을 다른 프로세스가 점유해서 사용할 수 있도록 함
  - 필요 기술
    - 프로세스들을 메모리에 미리 올려두기
- Multitasking
  - 개요
    - Multiprogramming의 논리적 확장으로, 프로세스 전환을 자주 발생시켜 사용자에게 빠른 응답 시간을 제공
  - 필요 기술
    - 메모리 관리
      - 가상 메모리
      - 디멘드 페이징
    - CPU 스케줄링
    - 파일 시스템 관리

### Program

- 정의
  - 컴퓨터가 태스크를 수행하도록 하는 set of instructions

### Process

- 정의
  - 하나 혹은 그 이상의 스레드에 의해서 실행되고 있는 컴퓨터 프로그램의 인스턴스
- 분류
  - fg
    - 사용자가 직접적으로 제어 하는 프로세스
  - bg
    - 사용자가 직접적으로 제어 하지 않는 프로세스

#### Daemon

- 정의
  - 사용자가 직접적으로 제어하지 않고, 부팅 때 자동으로 initialize되어, 백그라운드에서 동작하면서 여러 작업을 수행하는 프로그램
- 특징
  - 유닉스에서 부모 프로세스가 PID 1(init process) 이고, 제어하는 터미널이 없을 때, 그 프로세스를 데몬이라고 부름
    - 자식 프로세스를 fork 하여 생성 -> 자식을 분기한 자신을 죽임 -> init이 고아가 된 자식 프로세스를 자기 밑으로 데려감
  - MS 계열에서는 서비스라고 부름
- Daemon vs Service
  - Daemon
    - 최초 프로세스인 `init(or systemd)`가 initialize할 때, 실행하는 스크립트 디렉토리에 두면 바로 "데몬"이 됨
  - Service
    - `sc.exe`와 같은 프로그램으로 윈도우 API 함수를 이용해 등록해야 함

#### Processor affinity

- 동의어
  - CPU pinning, cache affinity
- 정의
  - process나 thread를 하나의 CPU나 복수개의 CPU 그룹으로 바인딩 하여, process나 thread가 지정된 CPU나 CPU 그룹에서만 실행되도록 하는 것
    - queue를 이용하여 구현
- 장점
  - processor를 고정시키므로써, cpu cache memory속의 캐시를 그대로 사용할 수 있게 함(퍼포먼스 향상)
- 단점
  - 로드 밸런싱을 해야함

#### Process group

- 정의
  - POSIX 준수 OS에서의 하나 혹은 하나이상의 프로세스들을 의미
- 기능
  - signal의 분배를 조정하는데에 사용됨
    - signal이 프로세스 그룹으로 보내지면, 그룹의 모든 프로세스로 해당 시그널을 보냄(broadcast)
- 참고) session
  - 정의
    - 하나나 하나이상의 프로세스 그룹의 컬렉션
  - 특징
    - 프로세스는 하나의 세션에서 다른 세션으로 migration불가

#### Pipeline

- *pipe는 왜, 어떻게 파일로 관리되는것인지?*
- *pipeline은 socket과 어떤 차이가 있는지?*
  - pipeline은 특정 호스트 안에서만 IPC가능하게 함
  - socket은 IPv4, IPv6를 사용해서 호스트 사이의 IPC를 가능하게 함
    - unix socket은 pipeline과 거의 비슷한 역할을 함

Pipeline

![](./images/os/pipeline1.png)

- 정의
  - Unix 계열 OS에서, *message passing* 을 사용하는 IPC(Inter-Process Communication)
  - standard stream에 의해서 process들의 집합이 체인된 것인데, 그리하여, 각각의 프로세스의 stdout이 다른 프로세스의 stdin으로 패싱됨
  - 두번째 프로세스는 첫번째 프로세스가 실행되고 있는 동안에 실행되며 concurrent한 성질을 갖음
- 종류
  - **anonymous pipes**
    - 하나의 프로세스에서 작성되는 데이터는 OS에 의해 다음 프로세스로 읽히기 전까지 buffer로 저장됨
    - uni-directional
    - shell 문법에서는 `|`로 구분
      - `process1 | process2 | process3`
      - `|`는, shell에게 왼쪽 커맨드의 stdout을 오른쪽 커맨드의 stdin으로 연결해주는 역할
    - 일반적으로 프로세스의 stderr는 pipe로 전달되지 않음
  - **named pipes**
    - 파일을 생성하므로써, 메시지가 프로세스 양방향으로 전달될 수 있음
    - 프로세스들이 끝나도 그대로 존재
    - python3의 `multiprocessing.Queue`가 named pipe를 사용해서 프로세스 사이의 데이터 송수신을 함
      - object가 queue에 놓임
      - object가 pickled됨
      - background thread가 pickled데이터를 pipe로 전달
        - 다수의 프로세스끼리 queue에 데이터를 주고 받을 때에는 항상 순서대로 전송 / 수신이 된다는 보장이 없음
        - *근데 굳이 왜 background thread를 사용해야 했을까?*
- 구현
  - 유닉스 계열의 시스템에서, *파이프라인의 모든 프로세스(파이프 라인의 모든 프로세스가 무슨 의미인지?)*는 동시에 시작되며, 스트림이 적절하게 연결되고, 스케줄러에 의해 관리되며, 다른 모든 프로세스가 machine에서 실행됨
  - buffering이 존재
    - 보내는 쪽이 5000bytes/s 로 보내고, 받는 프로그램이 100bytes/s로 받아도, 데이터가 상실되지 않음
      - 보내는 쪽의 데이터가 buffer에 일시적을 존재
      - 받는 쪽은 buffer로 부터 데이터를 받음
  - `netcat`, `socat`을 이용해서 socket과 연결도 가능

#### IPC(Inter-Process Communication)

- 정의
  - **OS가** 프로세스들이 데이터를 공유하는 방법을 제공하는 매커니즘
    - 주로 client-server 모델을 사용
- 접근
  - host 내부
    - File
      - 대부분의 OS
    - Socket
      - 대부분의 OS
      - network interface 사용
        - Stream-oriented(TCP)
        - Message-oriented(UDP)
    - Unix domain socket
      - POSIX / Windows 10
      - kernel 내부에서 커뮤니케이션 발생
        - domain socket은 file system을 주소공간으로 사용
    - Shared memory
      - POSIX / Windows
      - 다수의 프로세스가 같은 메모리 블록을 접근(shared buffer)
    - Pipe
      - Anonymous pipe
        - POSIX / Windows
        - stdin, stdout을 활용한 unidirectional data channel
        - 프로세스에 의해서 데이터가 작성되면, OS는 다른 프로세스가 다 읽을 때 까지 데이터 buffering함
      - *Named pipe*
        - POSIX / Windows
        - pipe가 file과 같이 간주됨(stdin, stdout 대신)
        - 프로세스들은 named pipe에 일반 파일처럼 write하거나 read함
    - Signal
      - 대부분의 OS
      - system message를 프로세스끼리 주고 받음
      - 데이터 전송 보다는, 명령을 내리기 위해서 사용
    - *Message queue*
      - 대부분의 OS
      - 프로세스들이 직접적으로 연결되지 않아도, message queue를 이용해서 읽고 쓸 수 있음
    - *Message passing*
      - RPC 등에서 사용
      - 다수의 프로그램이 message queue들을 이용해서 커뮤니케이션을 하고 non-OS managed channel을 이용하기도 함
        - concurrency 모델에서 사용됨
    - *Memory-mapped file*
      - 파일이 RAM과 매핑되어있고, memory 주소들을 바꿈으로써, 수정될 수 있음
  - host-to-host
    - Socket
      - 대부분의 OS
      - network interface 사용
        - Stream-oriented(TCP)
        - Message-oriented(UDP)
    - RPC

#### Signal(IPC)

- 정의
  - IPC의 제한된 형태이며, Unix, Unix-like나 POSIX-compliant 운영체제에서 사용됨
  - 프로세스 혹은 스레드에게 전송되는 비동기 notification
- 동작
  - 1 signal을 보냄
  - 2 OS가 타겟 프로세스의 일반적인 실행 흐름을 interrupt해서 signal 전달
    - *이 이야기는, 타겟 프로세스가 실행하고 있을때만 signal이 처리가 된다는 것인지? 아니면, signal이 있을때마다, interrupt가 발생해서, 해당 시그널을 해당 프로세스에서 처리하게 한다는 것인지?*
  - 3 프로세스가 signal handler를 등록했었으면, 해당 루틴이 실행되며, 그렇지 않은 경우에는 default signal handler가 실행됨
- 특징
  - 임베디드 프로그램은 IPC에 있어서 유용하게 사용함
    - 오버헤드가 적음
  - interrupt를 이용한 구현
- vs interrupt
  - 차이점
    - signal
      - kernel에 의해서 mediated(중재? 매개?)되며(via system call), process에 의해서 다뤄짐
        - 커널은 interrupt를 프로세스에 signal로써 넘겨줄 수 있음
        - e.g) `SIGSEGV`, `SIGBUS`, `SIGILL`, `SIGFPE`
      - OS커널과 process와의 커뮤니케이션
    - interrupt
      - CPU에 의해서 mediated되며, 커널에 의해서 다뤄짐
      - CPU와 OS커널과의 커뮤니케이션
- c.f) 코어 덤프
  - 컴퓨터 프로그램이 특정 시점에 작업 중이던 메모리 상태를 기록한 것
  - CPU레지스터, 메모리 관리 정보 포함
    - 오류 진단과 디버깅에 쓰임

### System call(syscall, trap)

- 개요
  - 운영체제의 커널이 제공하는 서비스를, 응용 프로그램이 접근하기 위한 인터페이스
  - 프로그래밍 언어에서 지원하지 않는 기능에 대하여, 운영 체제의 루틴을 호출하여 이용하는 것
- 특징
  - 하드웨어 제어를 하는 모든 권한은 커널이 갖고 있음
    - 파일 시스템
      - 응용 프로그램이 직접 제어할 수 없음
      - 데이터를 가져오거나 쓰려면 커널 장치 드라이버와 연동이 되어야 함
      - 시스템 호출 방법을 사용해야 함
  - software interrupt로 취급 됨
    - interrupt(exception) handler가 system call의 타입별 동작을 수행
  - *동기적으로 실행?*
- 기능
  - 1 사용자 모드에 있는 응용 프로그램이 커널의 기능을 사용할 수 있도록 함
  - 2 시스템 호출을 하면 사용자 모드에서 커널 모드로 바뀜
    - *해당 스레드를 블로킹 하는것인가?*
  - 3 커널에서 시스템 호출을 처리하면 커널 모드에서 사용자 모드로 돌아가 작업을 계속 함
- 종류
  - 1 프로세스 제어
    - Signal
  - 2 파일 조작
  - 3 장치 관리
  - 4 정보 유지(Information maintenance)
  - 5 통신

System call 코드 예시

```c
char gbuff[100];

int main(int argc, char *argv[])
{
    int leng;
    int fp;

    fp = open("/dev/mydrv", ....);  // mydrv_open 호출
    gbuff[0] = 10;
    gbuff[1] = 20;
    leng = 2;
    write(fp, (void*) gbuff, leng);   // mydrv_write호출

    close(fp);                       // mydrv_release호출
    return 0;
}
```

- 실행
  - 응용 프로그램에서 `open(...)`함수를 실행하면 libc에서 제공한 `open`함수 속에서 인수 데이터를 레지스터에 넣고 소프트웨어 인터럽트(로 취급되어) 실행
    - 즉, `open(...)`함수는 시스템콜을 래핑한 c라이브러리
  - 소프트웨어 인터럽트에 의해, 인터럽트 벡터 숫자를 이용해 ISR이 있는 커널의 인터럽트 처리 위치를 찾아 해당 주소로 실행을 옮김
    - 모드 변경(커널 모드)
  - ISR 실행
    - 커널 속의 장치 목록에서 해당 장치를 찾고, 드라이버의 함수 `.open`에서 정의된 `mydrv_open(...)`이 호출됨
    - `mydrv_open()`함수의 return에 따라 커널의 함수 호출이 완료 -> 커널은 다시 해당 응용 프로그램을 스케줄링에 의해 활성화 하고 해당 프로세서로 전환
  - CPU는 다시 사용자 모드로 전환
  - *커널 모드일때, 컨텍스트 스위칭이 발생하는가?*
- 예외
  - 만약 `write`함수나 `read`함수의 호출에 의해, 커널의 함수가 호출된 후 return에 의해 종료되지 않으면, 응용 프로그램은 스케줄링에서 빠져 커널의 상태에 머물면서 블럭킹이 발생
    - 해당 드라이버의 인터럽트 등으로 블럭킹 해제 가능

### c.f) Interrupt

*인터럽트가 감지되면 무조건 그것부터 실행하는가? 그럼, 인터럽트를 엄청나게 발생시키는 악성코드가 심어져있으면 어떻게 하는가?*

*인터럽트 처리중에 인터럽트가 발생하면 어떻게 되는가?*

Q) kernel모드일 때에는 컨텍스트 스위칭이 일어나지 않는가? 즉, 다른 프로세스의 실행 흐름으로 넘어가지 않는 것인가?
A) 커널모드일 경우, 커널모드에서 수행되어야 할 작업을 CPU가 수행할 뿐

- 정의
  - 입출력 하드웨어나 소프트웨어 등의 장치에 예외상황이 발생하여 처리가 필요할 경우, CPU에게 알려 처리할 수 있도록 하는 것
    - 어떤 대상이 CPU에게 일을 처리해 달라고 요청하는 수단
    - 비동기 이벤트 처리
- 종류
  - 하드웨어 인터럽트
  - 소프트웨어 인터럽트(trap, exception)
    - 오류, 사용자 프로그램의 특정 요청 때문에 발생하는 소프트웨어 생성 인터럽트
    - 특정 요청은 주로 systemcall
  - I/O interrupt
    - 입출력의 종료나, 입출력의 오류에 의해 CPU의 기능이 요청되는 인터럽트
  - External interrupt
  - Restart interrupt
  - Program check interrupt
    - 프로그램 실행중 보호된 기억 공간 내에 접근하거나, 불법적인 명령 수행과 같은 프로그램의 문제가 발생한 경우 호출되는 인터럽트
  - Machine check interrupt
- 절차(raise - catch - dispatch - clear)
  - 하드웨어 이벤트 감지
  - 디바이스 컨트롤러가 인터럽트 발생(raise)
  - 현재 진행 중인 기계어 코드를 완료함
  - CPU가 인터럽트 요청 라인 선 감지(catch)
    - *이 선은 큐 형식인가?*
    - 인터럽트 요청 라인
      - 마스크 불가능 인터럽트 라인
      - 마스킹 가능 인터럽트 라인
  - CPU 특수레지스터 중, *하이로인터럽트 마스크 비트* 를 보고 마스크 되면 인터럽트 무시
  - 인터럽트 벡터 읽기
    - *이 인터럽트 벡터는 어디서 나는 것인가?*
  - ISR 주소값 얻기
  - ISR로 점프 & 자동 대피 저장
    - 현재 진행중인 프로그램의 PC(Program Counter)및 각종 레지스터 대피
      - 스택이나 *레지스터 블럭* 에 대피
        - *스택으로 대피시키면, 스택이 오염되는거 아닌가?*
      - *컨텍스트 스위칭은 아니라는데..?*
      - 일반적인 process의 context스위치 보다 값이 싼 동작
  - ISR 코드 실행(dispatch)
  - 일을 다 처리하면, 대피시킨 레지스터 복원
  - ISR 끝에 IRET 명령어에 의해 인터럽트가 해제(clear)
  - IRET 명령어가 실행되면, 대피시킨 PC값을 복원하여 이전 실행 위치로 복원
- 특징
  - CPU가 인터럽트를 감지하면, 지금 실행중인 기계어 코드를 완료하고 해당 인터럽트를 위한 처리 프로그램(ISR)으로 점프하여 해당 일을 수행
    - ISR(Interrupt Service Routine or Iterrupt Handler)
      - 인터럽트 처리를 위한 루틴(프로그램)
      - 현재 진행중인 프로그램의 레지스터 대피를 행하도록 코드 구성이 필요
  - 인터럽트는 주로 CPU 코어에 입력되고, 현재 진행중인 기계어 코드가 종료되면 실행
  - 인터럽트를 처리할 것인가는 CPU코어의 특수레지스터에 비트 마스크를 통해 선택적으로 수용
  - 리눅스 커널과 같은 운영체제에서는, 응용 프로그램의 저수준 입출력 함수가 실행 => 라이브러리 함수에 의해서 소프트웨어 인터럽트 실행 - system call
    - 시스템 콜 호출 -> 인터럽트 실행으로 ISR이 커널 레벨 작업 수행 -> 다시 유저 스페이스로 데이터 및 스레드 반환
      - 어라, 그런데 nodejs에서는 fileRead하면 그것이 non-blocking이라 다른 작업할 수 있지 않았나? 그런데 `open` system call을 호출하면 interrupt가 발생하여 동기적으로 CPU가 처리하는 것 아닌가?
        - **그 레벨까지 생각할 것이 아님**
          - non-blocking operation on I/O API(sockets, file manipulation)
          - selecting(O(n)) / polling(O(n)) / epoll(O(1))
        - fileRead -> libuv가 kernel에 해당 파일의 fd를 epoll시스템 콜의 인자로 넘겨줌 -> kernel이 epoll을 이용하여 작업이 끝났음을 알림 -> I/O poll phase에서 파일 읽기 이벤트가 끝났음을 감지 -> callback task 실행
          - 스레드풀을 되도록 사용하지 않고 fd를 이용한 non-blocking API를 사용하는 것이 포인트!
        - 사용자 모드
          - 사용자 앱에서 fileRead 함수 호출
            - open시스템 콜을 호출
        - 커널 모드
          - software interrupt발생으로 interrupt vector를 보고 ISR 실행
          - ISR은 파일 시스템 디바이스 드라이버에게 명령
            - 파일 시스템 디바이스 드라이버는 컨트롤러에게 읽으라고 명령
          - 그리고 CPU는 자신이 해야할 동작 함
          - 파일 시스템 컨트롤러가 DMA를 이용하여 메모리에 데이터 저장
          - 파일 시스템 컨트롤러가 인터럽트 raise
          - CPU는 인터럽트 catch
          - CPU는 ISR실행 (dispatch)
          - 다시 원래 실행하던 흐름으로 되돌아감 즉, 스케쥴링으로 인하여 다른 작업을 하고 있는 것임
            - 인터럽트 핸들링만 CPU가 처리
      - nodejs 자체는 libuv 이벤트루프 기반이고, 내부적으로 파일 조작, encryption이나 compression의 경우 thread pool을 사용하고, 나머지 동작(socket 등)의 경우 kernel의 API(syscall) 등을 사용하므로, non-blocking하게 실행
        - I/O multiplexing의 방법들인 select, kqueue, epoll은 kernel작업을 nonblocking으로 실행했을경우, 이벤트 루프가 해당 동작이 완료했음을 통지받기 위해서 사용
  - ISR은 C언어의 함수와는 다른 표현이 되어야 함
  - c.f) vs polling
    - CPU가 대상을 주기적으로 감시하여 상황이 발생하면 해당 처리 루틴을 실행해 처리
- c.f) 인터럽트 체인
  - 인터럽트 벡터의 주소 개수보다 많은 장치(ISR)가 존재
  - 인터럽트 벡터의 각 원소는 인터럽트 핸들러 리스트의 헤드
    - 처리 가능한 핸들러가 발견될 때까지 상응하는 리스트의 핸들러가 하나씩 호출
- c.f) 인터럽트 우선순위 시스템
  - 우선순위가 높은 인터럽트가 낮은 인터럽트보다 먼저 처리되도록

### c.f) Green threads(virtual threads)

- 정의
  - 런타임 라이브러리나, VM에 의해서 스케쥴링 되는 스레드
    - OS가 아님
  - 예시
    - golang의 goroutine
    - cpython의 greenlet
      - *cpython의 greenlet은 어떻게, I/O타임에 실행 흐름을 yield하는 타이밍을 알까?*
- 특징
  - OS의 능력에 의존하지 않고, 멀티스레드 환경을 emulate
  - user space에서 관리됨
    - kernel space가 아님
    - 그렇기 때문에, native thread support가 없는 환경에서도 사용 가능
  - *green thread가 blocking system call을 하는경우, 모든 green thread를 블로킹함*
    - asynchronous I/O를 해야만 함

### Context switch

- 정의
  - process나 thread의 상태를 저장해서 나중에 복원하고 실행을 재개할 수 있도록 하는 프로세스
    - 다수의 프로세스가 하나의 CPU를 사용할 수 있도록 하여 multitasking을 가능하게 함
- 특징
  - computationally intensive
  - 프로세스를 스위칭 하는데에는 특정 시간이 필요함
    - 레지스터(SP, PC), 메모리맵 저장 및 로딩
    - 페이지 테이블
    - *green thread에서도 일어남 최소한의 context를 저장하고 로딩함*
      - e.g) goroutine
  - pre-emptive multitasking 시스템에서는, 실행중인 process가 time slice를 초과하면 interrupt를 해서, context switch를 행함
- process context switch vs thread context switch
  - process context switch
    - 개요
      - 같은 OS안에서 프로세스를 컨텍스트 스위칭 하는 것
    - PCB(Process Control Block)
      - 프로세스의 작업 상태를 저장할 수 있는 공간
      - 프로세스가 context switch되는 경우, PCB에 해당 Thread 정보들도 저장됨
      - 저장 대상
        - 레지스터, memory map, page tables, kernel 자원, cpu cache들 등
  - thread context switch
    - 개요
      - 하나의 같은 프로세스안에서 스레드를 컨텍스트 스위칭 하는 것
    - 특징
      - process context switch보다 효율적
    - TCB(Thread Control Block)
      - 스레드의 작업 상태를 저장할 수 있는 공간
        - OS가 관리 or 라이브러리에 의해 관리
      - 저장 대상
        - PC, SP, registers만 스위칭하면 됨
    - *cpython의 경우 어떤식으로 context switch가 되는것일까?*

## Memory

Memory abstraction example

![](./images/os/memory_abstraction1.png)

*Memory segmentation / paging / virtual memory / swap 개념들 사이의 관계?*

- 메모리 관리 역사
  - plain physical memory
  - overlays
  - segmentation
  - paging

### Address space

virtual address space and physical address space

![](./images/os/virtual_address_space_and_physical_address_space1.png)

- 정의
  - 논리적 혹은 물리적인 entity에 대응할 수 있는 주소들의 범위
    - 반드시 memory에만 해당하는 것이 아님. DNS - IP - MAC 이런식으로 네트워크 address space를 분리할 수 있음
  - space이므로, 수학적인 대수구조로 생각하면 mapping도 쉽게 의미 유추 가능
- 특징
  - 다양한 layer끼리의 mapping and translation
    - higher-level address는 lower-level address로 매핑되어야 함
      - e.g)
        - logical disk위에 있는 fs는 linear한 주소를 absolute LBA sector 주소(Cylinder-Head-Sector 등)로 바꿔야 함
        - DNS - IP - MAC address space 매핑
  - virtual - physical address translation
    - virtual address space의 서로 다른 pages를 page file 혹은 메인 메모리의 physical address로 매핑

### Virtual memory

![](./images/os/virtual_memory1.png)

- 정의
  - memory 관리 기술 s.t. 실제로 주어진 머신에서 사용가능한 메모리 자원의 idealized abstraction
  - 결과적으로, 유저에게는 매우 큰 main memory가 있는 것 처럼 보임
- 개요
  - OS는 프로그램이 사용하는 memory address(virtual address)를 컴퓨터 메모리의 실제 physical address로 매핑함
  - 일반적으로 하드웨어 MMU(Memory Management Unit) 라는 하드웨어 서포트가 필요함
    - CPU에 존재하는 address를 변환해주는 하드웨어
      - virtual addresses <-> physical addresses
  - OS 내부의 소프트웨어는 실제 메모리의 크기보다 더 큰 virtual address space를 사용할 수 있도록 하는 기능도 있음
- 장점
  - 프로그램이 다른 프로그램과 공유가 되는 메모리공간을 다루는 복잡도로부터 해방
    - kernel이 다루도록 함
  - 실제 메모리의 fragmentation을 숨김
  - memory isolation
    - 보안 강화
  - paging
    - 실제 물리적으로 사용가능한 메모리보다 더 많이 메모리 사용 가능
- 단점
  - Embedded system과 같은 특수 목적의 컴퓨터 시스템은, 반응속도가 느린 등의 단점이 생김
  - MMU와 같은 하드웨어를 내장해야 하므로, 비용 문제
- 역사
  - 과거의 컴퓨터 메인프레임은 Virtual memory 기능이 없었음
  - 1960, 1970 년대에는 메모리가 매우 비쌌음
    - virtual memory가 널리 퍼진 계기
  - 현대 OS에서는 각 프로세스마다 그에 대응되는 virtual address space를 갖음
    - 옛날 OS에서는 모든 프로세스를 하나의 virtualized memory로 이루어진 address space에서 실행

#### Paged virtual memory

- 개요
  - 거의 모든 현재의 virtual memory 구현은 virtual address space를 page(연속된 virtual memory address의 블록들)로 분리함
  - page는 적어도 4KB의 크기이며, 보다 더 큰 페이지 사이즈를 사용할 수 있음

### Paging

*페이징 기술을 사용하면, 각 프로세스마다 virtual memory를 사용하게 되는데, 어떻게 buffer overflow공격이 가능한 것인지? 자신의 process 내부의 virtual address의 값을 바꾸는 것인지?*

결국 페이징이라는 것은, 프로그램이 virtual memory를 사용할 수 있도록 하는 방법론인데, 그 virtual memory속의 page는 physical memory 혹은 disk의 같은 크기의 page와 1:1매칭되는 unit이고, virtual memory는 linear하게 구성됨

- 정의
  - 메인 메모리에서 사용하기 위해, secondary storage(디스크)로부터 데이터를 가져오거나 거기에 데이터를 저장하는 메모리 관리 scheme
- 특징
  - OS가 관장
  - OS는 page라고 불리는 secondary storage로부터 같은 크기의 블록 데이터를 갖고 옴
  - virtual memory 구현에 매우 중요함
    - 실제 물리적 메모리 보다 더 많은 메모리를 프로그램이 사용가능하게 함
  - 하나의 process의 virtual address space는 여러개의 page의 구성으로 이루어져 있음
- page fault
  - 경우의 수
    - 1 해당 virtual address에 변환이 불가능한 경우(invalid)
      - OS는 segmentation fault signal을 해당 프로그램을 보냄
        - *paging인데 왜 segmentation fault인가? memory segmentation과는 전혀 다른 의미인가?*
    - 2 RAM(Physical memory)에 존재하지 않는 페이지를 프로세스가 참조하려 할 때 나는 에러
      - 다른 page를 위하여 일시적으로 disk로 해당 page 저장
        - backing store은 다음과 같이 불림
          - swap partition (if it is a disk partition)
          - swap file (if it is a file)
          - page file (if it is a file)
      - control을 해당 프로그램에서 os로 넘김
      - physical memory가 가득 차지 않은 경우
        - page를 disk로부터 가져와서 physical memory로 넣어줌
        - page가 physical memory에 저장되고, page table, TLB가 업데이트 됨
        - 다시 instruction 실행
      - physical memory가 가득 차 있는 경우
        - 하나 혹은 그 이상의 physical memory의 페이지가 paged out되어서 여유 공간을 만들어야 함
        - page table은 기존에 physical memory에 존재하던 page들이 더 이상 존재하지 않는다고 마킹함
        - TLB 업데이트
          - paged out된 페이지를 제거함
          - 새로운 페이지를 TLB에 등록
      - *page frame?*

the structure of page table

![](./images/os/page_table1.png)

page table translation process

![](./images/os/mmu_translation_process1.png)

- page table
  - 정의
    - OS의 virtual address - physical address매핑을 저장하는 장소
      - 각각의 mapping은 PTE(Page Table Entry) 라고 불림
  - 개요
    - program이 마치 linear한 메모리를 사용할 수 있는 것처럼 virtual address를 다룰 수 있게 하고, 해당 virtual address를 physical address로 매핑함
      - 매핑을 가능하게 해주는 하드웨어는 MMU
  - 구조
    - TLB(Translation Lookaside Buffer)
      - 최근에 사용된 매핑 캐시를 저장
      - *associative cache*
  - virtual address - physical address translation(mapping)
    - virtual address가 physical address로 변환 시도
    - TLB를 탐색
      - 존재하면 physical memory address를 반환
    - Page walk
      - MMU나 OS TLB miss handler가 Page table을 확인해서 매핑이 존재하는지 확인
    - 존재하면 TLB에 작성해야 함
    - 다시 처음 시도했던 변환을 처음부터 다시 시도(TLB 서칭이 다시 일어남)
- page supervisor
- pinned pages

### Swap in and out

- 개요
  - swap out
    - 프로세스가 사용하는 메모리를 메인메모리에서 디스크로 저장함
  - swap in
    - 프로세스가 사용하는 메모리를 디스크에서 메인메모리로 불러옴

### Memory segmentation

*segmentation fault와 관련이 있는가?*

- 정의
  - 컴퓨터의 primary memory를 segment나 section들로 분리하는 메모리 관리 기술
- 특징
  - 메모리 위치에 대한 참조는 세그먼트임을 나타내는 값과 offset을 가지고 이루어짐
  - x86-64 아키텍처에서는 레거시 시스템이 되었음
    - 대신 memory-paging을 사용함
    - 그래도 backward compatibility를 이유로 서포트 자체는 함
- 장점
  - process간의 memory를 격리시켜서 system의 reliability를 높임

### Overlay

- 정의
  - 프로그램 코드나 다른 데이터의 블록을 기존에 메인메모리에 저장되어 있던 것을 덮어씌우는 프로세스
- 특징
  - 컴퓨터의 메인 메모리보다 더 큰 메모리를 차지하는 프로그램을 동작할 수 있게 하는 방법(Paging과는 다른)
    - *더 필요하면 기존에 자신이 사용하던 메모리도 덮어씌워서?!*

### OOM killer(Linux)

왜 페이징을 안쓰고 그냥 메모리를 죽여버리는지? >> 페이징과 스와핑까지 사용하고 남은 공간이 없을 때 kill함

*시스템에 현재 동작하는 모든 프로세스의 메모리 사용량이 피지컬 메모리를 상회해서 그런가?*

- 정의
  - 시스템의 가용 메모리가 매우 적을때, Linux 커널이 프로세스를 동작시키기 위한 메모리 확보를 하기 위해서, 여타 프로세스를 죽이는 프로세스
- 배경
  - 일반적으로 프로세스가 시작하면, 커널에 메모리를 요청하는데, 그 요청은 프로세스가 초기에 사용하는 양 보다 더 많음
    - redundant memory(over allocation)
    - e.g)
      - 시스템은 8GB메모리 공간이 존재하는데, 커널은 8.5GB를 해당 프로세스에 할당할 수 있음
  - 일반적으로는 문제를 일으키지 않으나, 프로세스들이 요청한 메모리를 다 사용하면서, physical memory가 모든 프로세스를 돌리기 위해 충분하지 않은경우에 문제가 생김
    - *그냥 메모리 스왑하면 안돼?*
      - *스왑 공간 제한도 다 차서 그런가?*
- 삭제할 bad 프로세스 선택
  - 특징
    - 1 kernel은 필요한 최소한의 메모리만 확보함
    - 2 Try to reclaim a large amount of memory
      - *??? 1이랑 모순되는 내용?*
    - 3 적은 양의 메모리를 사용하는 프로세스는 죽이지 않음
    - 4 최소한의 숫자의 프로세스만 kill
    - 5 *Some meticulous algorithms that elevate the sacrifice priority on processes the user wants to kill*
  - 선정
    - 리눅스 `proc_oom_score(seq_file, pid_namespace, pid, task)` 함수 호출
      - *여기서 나오는 seq_file, pid_namespace, pid, task란 무엇인가?*
      - `oom_badness(task_struct, totalpages)`
        - 이곳에서 프로세스의 OOM score결정
- 프로세스 삭제
  - 삭제할 프로세스가 생긴 경우에는, OOM-Killer가 `oom_kill_task()`함수 실행
    - 해당 프로세스에 `SIGKILL` 시그널을 보냄
    - 커널 로그도 남김(Print a warning-level message)
  - 주로 DB, Apache, 등의 프로세스가 죽을 떄가 많음 or task worker
- 관련 설정
  - OOM-killer 자체
    - `sudo -s sysctl -w vm.oom-kill = 1`
      - enable
      - 0은 disable
      - temporary
      - permanent
        - `/etc/sysctl.conf`파일에 `vm.oom-kill = 1`을 텍스트로 넣어둬야 함
    - `echo 0 > /proc/sys/vm/panic_on_oom`
      - disable
  - Memory overcommit(`vm.overcommit_memory`)
    - 0
      - kernel이 overcommit할지 말지 결정함(Heuristic)
    - 1
      - 항상 overcommit 허용
    - 2
      - 제한적 overcommit 허용
      - `commit 최댓값 = Swap 영역 + 물리 메모리 * vm.overcommit_ratio`
  - Swappiness(`/proc/sys/vm/swappiness`)
    - 값이 클 수록 OOM killer가 프로세스를 죽일 확률이 적어지나, 전반적인 작업속도 성능이 나빠짐
    - 값이 적어지면 OOM killer가 프로세스를 죽일 확률이 높아지나, 전반적인 작업속도 성능이 향상됨

### Memory overcommitment

*실제 필요한 메모리 사용량 > swap + physical memory 인 경우에 OOM-killer가 동작하는 것인지?*

- c.f) Memory commitment
  - 정의
    - **프로세스는 메모리 공간을 할당받았다고 생각하지만, 실제로는 물리 메모리 어느 곳에도 할당되어지지 않은 상태**
- 정의
  - 실제 physical machine보다 더 많은 메모리를 virtual computing device(or process)에 할당하는 것을 다루는 개념(physical machine의 메모리 양보다 더 많은 양의 메모리를 commit하는 것)
    - 이것이 가능한 이유는, 할당받은 virtual machine혹은 process는 반드시 할당 받은 메모리를 일정 시점에 다 소비하지 않아도 되기 때문
    - e.g)
      - 4GB의 물리적 메모리를 갖는 호스트 내에 4개의 VM이 1GB의 메모리를 갖는 경우에는, 실제로 VM이 겨우 500MB 밖에 메모리를 사용하지 않는경우, 추가적인 VM을 생성할 수 있음
- 특징
  - 메모리 사용이 급증하면, Memory swapping이 사용됨
    - swapping은 실제 메모리를 사용하는 것 보다 느림
  - `vm.overcommit_memory` 변수의 값에 따라 다름
    - 0
      - kernel이 overcommit할지 말지 결정함(Heuristic)
    - 1
      - 항상 overcommit 허용
      - OOM 에러가 날 가능성 존재(risky)
    - 2
      - 제한적 overcommit 허용
      - `commit 최댓값 = Swap 영역 + 물리 메모리 * vm.overcommit_ratio`
      - PostgreSQL에서 추천되는 옵션
- 사용 예시
  - VM
  - `fork()`
    - 일시적으로 부모 프로세스의 모든 메모리 주소 공간만큼의 메모리 확보가 필요함

## Virtualization

- 종류
  - OS-level virtualization
  - Application virtualization

### OS-level virtualization

OS-level virtualization

![](./images/os/os_level_virtualization1.png)

- 정의
  - **kernel이 다수의 격리된 user space instance를 허락하는 OS 패러다임**
    - user space는 kernel space와 대비되는 개념
- user space instance를 부르는 이름
  - containers, Zones, virtual private servers, partitions, virtual environments, virtual kernels, jails
    - 위의 user space instance에서 동작하는 프로그램은 진짜 computer의 user space처럼 보이게 됨
    - 그러나, 컨테이너에 할당된 컨텐츠와 장치만 볼 수 있음
- 참고) container의 정의
  - **OS-level virtualization에서의 user space instance**
- 동작
  - **OS-virtualization(containerization) 에서는 전체 OS의 일부의 자원들만 할당된 컨테이너 에서 프로그램을 동작시킬 수 있음**
  - 각각의 컨테이너는 임의의 개수의 컴퓨터 프로그램을 포함함
  - 이러한 프로그램들은 concurrently, separately 동작하고 서로서로 상호작용하기도 함
  - c.f) application virtualization
    - 하나의 프로그램이 파일 시스템만 격리된 곳에 놓여짐
- 사용
  - virtual hosting 환경
    - 제한된 하드웨어 자원을 서로 신뢰하지 못하는 다수의 유저들사이에 안전하게 할당시킬 때
  - 서버 하드웨어의 통합
    - 여러 호스트에 존재하는 하드웨어 자원의 통합
  - improved security
- 특성
  - 오버헤드
    - full virtualization보다는 적은 오버헤드
      - OS 레벨 virtual partition에 있는 프로그램들은 OS의 일반적인 system call 인터페이스만 사용하며, emulation이나 중간의 virtual machine이 존재하지 않음
  - 유연성
    - 다른 virtualization 접근 방식보다 유연하지는 않음
      - guest OS를 호스트 OS와 다른 것으로 *호스팅* 할 수 없음
        - *근데 docker는 windows docker에서 linux호스팅 가능하지 않나?*
  - 스토리지
    - file-level *copy-on-write(COW)* 메커니즘 제공하는 경우도 존재
      - 파티션끼리 기본 fs는 공유되고, 파티션들은 파일을 수정할 때, 자신들의 카피를 만듬
    - block-level copy-on-write 보다 공간 복잡도에 효율적이고 캐시하기에 간단함
      - whole-system virtualization에서 채용

### LXC(Linux Container)

- 정의
  - **다양한 격리된 Linux system(container)을 하나의 Linux kernel을 사용하는 컨트롤 호스트 위에 동작시키는 OS level의 virtualization**
- 원리
  - **cgroups**
    - 자원의 제한과 우선순위 부여
      - CPU, memory, block I/O, network, ...
      - virtual machine이 필요 없음
    - Linux kernel이 제공하는 기능
  - **namespace isolation**
    - OS의 environment에 대한 application의 뷰를 완전히 격리
      - process tree, networking, user IDs, mounted fs 등
  - LXC는 위의 두 기술의 결합

### Virtualization

- 정의
  - 가상의 무엇인가를 만드는 기술
- 구체적 예시
  - NAT(Network Address Translation)
    - 존재하지 않는 IP를 가상으로 만들어서 배정
  - VPN(Virtual Private Network)
    - 같은 공용 통신망을 통해 통신을 하지만, 패킷을 암호화해서 주고 받아, 마치 사설 네트워크를 만드는 것과 같은 기술
  - RAID, LVM

### Server Virtualization

- 정의
- 사용하는 이유
  - 서버의 자원을 효율적으로 최대한 사용하기 위함
- 구현에 따른 분류
  - 전 가상화(Bare-metal/hypervisor)
    - 개요
      - 순수한 하드웨어 위에 운영체제나 BIOS가 아닌 Hypervisor가 있는 구조로 이루어지는 가상화
        - 하이퍼바이저는 가상머신을 만들고 관리하는 프로그램
    - 특징
      - VM의 입장에서 하드웨어 자원은 무조건 하이퍼바이저를 통해서 사용 가능
  - 반(더 진보한) 가상화(Para-virtualization)
    - 개요
      - 전 가상화와 달리, VM이 하드웨어 자원을 직접적으로 사용 가능
  - 호스트 기반 가상화
    - VMware나 VirtualBox와 같은 가상화 구현 프로그램을 이용한 가상화
- 세대 별 분류(기술 수준)
  - 1세대
    - 하나의 물리적인 서버에 하이퍼바이저로 여러 개의 가상머신을 생성하는 수준
    - 예시
      - VirtualBox
  - 2세대
    - 다수의 물리적인 서버의 자원들을 하나로 묶어서 서버 풀을 구성하고 관리할 수 있는 수준
      - 특정 서버에 문제가 생겼을 때, 문제 있던 서버에서 실행중이던 가상머신들을 다른 정상 작동하고 있는 서버로 옮기는 실시간 마이그레이션 기술 사용
  - 3세대
    - 다른 하이퍼바이저끼리도 서버 풀을 구성하고 관리가 가능
    - 예시
      - OpenStack, CloudStack, Eucalyptus, OpenNebula, ...

## Application Layer

### deb

- 정의
  - Linux distribution Debian과 해당 관련 리눅스 배포판의 software package format의 확장자
