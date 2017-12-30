# Linux기초

## 1. ssh사용법

[생활코딩: SSH](https://opentutorials.org/module/432/3738)

아마존 웹 서비스(AWS)의 EC2나 Light-Sail등의 IaaS(Infrastructure as a Service)를 사용하다 보면, 로컬 환경에서 원격 환경으로 커맨드라인 인터페이스를 이용해서 접속해야할 때가 있다.

그럴 때 사용되는 기술이 바로 SSH(Secure SHell)이다.

- SSH는 원격지에 있는 컴퓨터를 안전하게 제어하기 위한 프로토콜
- SSH클라이언트와 SSH서버로 나뉜다.
- Telnet은 암호화가 되어있지 않은 방식이나, SSH는 RSA암호가 적용되어 있다.
- 주로 Unix 계열의 운영체제를 원격에서 운영하기 위한 방법이므로 윈도우는 클라이언트 운영체제로 사용할 수 있다.
- Mac이나 Unix계열의 컴퓨터는 이미 SSH클라이언트와 서버가 미리 설치되어 있다.
- Linux의 경우에는 `Open SSH`를 설치해야 한다.

예시
```sh
ssh -i (keyfile) username@host
# ssh -i example.pem voidsatisfaction@123.456.78.9
```

## 2. sudo

예전의 컴퓨터는 비쌌으므로 하나의 컴퓨터를 많은 사람들이 공유할 수 있도록 했다. 즉 Unix계열의 운영체제에서는 다중사용자 시스템이 있었다. 그래서 각각의 사용자가 다른 사용자가 만든 파일을 쉽게 제어할 수 없도록 권한(permission)을 달리 부여했다. 가장 높은 권한의 유저를 `root user`라고 하는데, `sudo`는 루트권한 유저의 권한을 잠시 빌리는 것이다.

## 3. 패키지 매니저(apt)

스마트폰의 앱스토어와 같은 역할. 프로그램(패키지)를 검색하고 쉽게 설치 할 수 있도록 도와준다.

- `apt-get update`: 패키지 매니저에서 설치할 수 있는 패키지 목록을 최신상태로 갱신
- `apt-cache search 검색어`: 로컬 패키지 매니저가 보유하는 목록에서 다운로드 가능한 패키지를 찾아준다.
- `apt-get install 패키지`: 패키지를 설치
- `apt-get remove 패키지`: 패키지를 삭제

## 4. 파일 다운로드

- wget
  - `wget -O 저장파일이름 url`
- git
  - `git clone 깃허브의url`

## 5. 왜 CLI(Command Line Interface)를 사용하는가?

- CLI가 GUI보다 메모리 사용량이 적음
- CLI는 자동화가 가능(순차 실행이 가능)
- 파이프라인 기능
  - 프로그램의 출력을 다른 프로그램의 입력으로 준다.
  - `ls --help | grep sort | grep file`

## 6. IO Redirection

유닉스에서는 프로그램을 `프로세서`라고 한다. 그리고 기본적으로는 아래와 같은 구성을 갖고 있다:

![unix programs](./images/unix_program.jpg)

- `ls -al > result.txt`
  - `ls`의 결과를 `result.txt`라는 파일로 리다이렉션
  - `>`는 표준출력을 리다이렉션 할 수 있도록 한다.
  - `2>`는 표준에러를 리다이렉션 할 수 있도록 한다.
  - c.f) `ls -al >> result.txt`는 result.txt파일의 내용에 추가하는 것이다.
- `cat < hello.txt`
  - hello.txt의 내용을 표준입력을 이용하여 cat의 입력으로 받는다.
  - c.f) `cat hello.txt`는 커맨드라인 인자(commandline argument)로 전달하는 것이다.
- `ls -al > /dev/null`
  - 아무것도 일어나지 않는다(null)

Q) 파이프랑 리다이렉션의 차이는?

## 7. Shell vs Kernel

![Unix shell kernels](./images/unix_shell_kernel.jpg)

![Unix shell kernels2](./images/unix_shell_kernel_2.jpg)

쉘: 사용자의 명령을 해석하는 곳 => 커널에게 API를 이용해서 전달
커널: 해석된 명령을 하드웨어에 전달

- 쉘과 커널을 분리하므로써, 여러가지 종류의 쉘을 이용해서 커널을 제어할 수 있게된다.
  - bash vs zsh

쉘도 하나의 프로그램이다.

## 8. Shell Script

쉘 스크립트는 복잡한 쉘 명령을 순차적으로 실행할 수 있도록, 스크립트 파일로 남겨둔 것을 말한다.

```sh
# backup
#!/bin/bash

if ! [ -d bak ]; then
   mkdir bak
fi
```

위의 스크립트는 `chmod +x backup`을 통해서 실행가능하게 선언해줘야 한다. `#!/bin/bash`는 리눅스에게 bash로 실행할 수 있는 스크립트라는 것을 알려주는 것이다.

환경변수를 지정하기 위해서는 다음과 같이 하면 된다.

```sh
# filename = .env
#!/bin/bash

export ABC=123
```

그리고 OS에서 `source .env`나 `sh .env`를 해주면 된다.
