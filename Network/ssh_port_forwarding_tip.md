# SSH 포트포워딩을 이용해서 3306포트 차단 우회하기

- ssh란?
- ssh 포트포워딩을 사용하게 된 배경
- 방법
- ssh 포트포워딩 편하게 하기
- ssh 포트포워딩으로 방화벽 우회하기
- 감상

## 참고

- [SSH: The Secure Shell: The Definitive Guide](https://docstore.mik.ua/orelly/networking_2ndEd/ssh/ch03_03.htm)

## ssh(Secure Shell)란?

- 개요
  - 안전성이 담보되지 않은 네트워크에서 안전하게 네트워크 서비스를 운영하기 위한 암호화 네트워크 프로토콜
    - 기밀성 / 무결성 보장
  - 서버 - 클라이언트 아키텍처
  - 22번 포트 사용
  - Unix 계열의 운영체제 시스템에 주로 접근하도록 사용되나, Windows 10이 OpenSSH를 기본 ssh 클라이언트로 사용하므로 Windows 10도 접근 가능
  - 텔넷등 안전하지 못한 원격 쉘 프로토콜을 대체하기 위하여 만들어짐
    - 다른 프로토콜은 암호화가 되어있지 않았음
- 원리
  - 공개 키 암호를 사용해서 원격 컴퓨터를 인증함
  - 방법1
    - 네트워크 연결을 암호화 하는데에 public-private key 페어를 사용하고, 로그인에는 password를 사용하는 방법
  - 방법2
    - 로그인 자체를 public-private key만 사용
      - 따라서 미지의 public키를 받아들일 때는 항상 조심해야 함
      - 공격자의 public 키를 받아들이게 되면, ssh를 통해서 해킹할 수 있음
- 키 관리
  - 유닉스 계열의 시스템은 `~/.ssh/authorized_keys`파일에 허가된 public key들을 둠
    - 이 파일은 owner나 root를 제외하고는 writable하지 않아야지 ssh 프로그램에 의해서 사용됨
    - `-rw------- 1 ubuntu ubuntu  405 Feb 25 07:36 authorized_keys`
  - 일반적으로 local에서 private key를 제시하고 remote에 그에 일치하는 public key가 존재하면, 패스워드는 필요 없으나, 추가적인 보안을 위해서는 private key자체를 비밀번호로 잠글 수 있음
  - `ssh-keygen` 유틸리티는 퍼블릭과 프라이빗 키를 쌍으로 생성할 수 있음
- 활용
  - remote machine 접근
  - *tunneling*
  - *forwarding TCP ports*
  - *X11 connection*
  - SSH file transfer(SFTP), secure copy(SCP) 프로토콜을 이용한 파일 옮기기
  - 클라우드 컴퓨팅의 접속 문제를 해결해줌
  - **SOCKS 프로토콜을 서포트 하는 SSH clients에 암호화 프록시 연결을 통하여 웹 서핑**
- SSH2
  - SSH1에 비해서 보안 발전
    - *Diffie-Hellman key exchange*
  - SSH1에 비해서 무결성 보증 발전
    - MAC(message authentication codes)
  - SSH1에 비해서 기능 발전
    - 단일 SSH 연결에서 원하는 만큼 shell sessions를 실행 가능
- OpenSSH
  - SSH2 구현체
  - 보통 프로그램으로는 OpenSSH를 사용(대부분의 운영체제에 내장되어있음)
  - 원격 동작
    - `ssh`, `scp`, `sftp`
  - 키 관리
    - `ssh-add`, `ssh-keysign`, `ssh-keyscan`, `ssh-keygen`
  - 서비스
    - `sshd`, `sftp-server`, `ssh-agent`

## ssh 포트포워딩을 사용하게 된 배경

내가 다니는 대학교에서 보안상의 이유로 3306포트 패킷을 막아두었다. 그래서 데이터베이스 개발이 매우 힘들었는데, 내가 토이프로젝트를 돌리는 aws lightsail과 ssh 포트포워딩을 이용해서 aws rds의 mysql에 접속할 수 있었다.

## 방법

1. rds의 security group에서 lightsail(혹은 ec2)의 ip로 데이터베이스 접속하는것을 허용해줌
2. lightsail의 외부로부터의 ssh접속을 허용해줌
3. lightsail의 `/etc/ssh/sshd_config`에서 `GatewayPorts yes`를 추가
4. 로컬 PC에서 sudo ssh -L 3306:RDS의엔드포인트:3306 ec2-user@lightsail글로벌ip주소 -i lightsail비밀키 (개인적으로 Sequel Pro를 사용하는 것을 추천합니다)

## ssh 포트포워딩 편하게 하기

- [참고](https://qiita.com/lasta/items/41e95a2fdded18c34dae)

매번 일일이 `-i`와 같은 설정을 하는 것은 귀찮으므로 `~/.ssh/config`에 다음과 같은 설정을 함

- `.ssh/config`는 다음과 같은 문제를 해결할 수 있음
  - SSH접속할 떄 마다 비밀키 지정 하는것이 귀찮은 문제
  - 호스트명과 유저명을 매번 쓰는 것은 귀찮음
  - 다단계 SSH의 작성법을 까먹는 문제

```
Host           phost1
HostName       host1.hoge.fuga
User           user
GatewayPorts   yes
LocalForward   10025 localhost:10025
IdentityFile   ~/.ssh/id_rsa

Host           phost2
HostName       host2.hoge.fuga
User           user
GatewayPorts   yes
LocalForward   10025 host2.hoge.fuga:25
ProxyCommand   ssh -CW %h:%p phost1
IdentityFile   ~/.ssh/id_rsa
```

위는 ssh포트포워딩을 나타냄

## ssh포트 포워딩으로 방화벽 우회하기

- 참고
  - https://thevaliantway.com/2012/10/useful-terminal-commands-part-02-ssh-d-flag/
- switchy sharp라는 크롬 확장 애플리케이션
- ssh

```
ssh -D (바인딩 할 포트번호) -i (ssh키) (다른 호스트)
```

위의 커맨드를 실행하면 로컬에서 위의 바인딩 할 포트번호로 가는 모든 트래픽이 ssh 터널을 통하여 다른 호스트로 포워딩 되고

다른 호스트에서 그 트래픽을 처리하고 그 결과(응답)를 로컬로 보내준다.

방화벽이 있는 네트웍에서(ssh포트는 막히지 않은) ssh포트 포워딩을 통해서 우회하는 것이 가능하다.

인터넷의 경우는, 크롬 확장기능의 `switchy sharp`를 추가해서 SOCKS Host를 localhost로 두고, 포트를 위의 바인딩 할 포트번호로 설정하면

브라우징이 가능해진다.

ssh의 실행이 중단되면 터널링도 없어지니 주의

## ssh -L, -D 차이

- `ssh -L 10000:google.com:80`
  - 로컬 포트 10000을 염
  - 해당 포트로 보내는 모든 데이터는 ssh 터널을 통해서 server로 감
  - 해당 데이터를 서버가 decryption
  - server에서 google.com:80 으로 접속한 것 처럼 됨
- `ssh -R 1234:google.com:80`
  - remote의 1234 포트를 염
  - 해당 포트로 보내는 모든 데이터는 local server에 ssh서버로 터널을 통해서 전송
  - 해당 데이터를 decryption
  - 그 후 데이터를 google.com:80에 다시 보냄
- `ssh -D 10000`
  - 로컬 포트 10000을 염
  - 웹 브라우저가 switchysharp등의 프로그램을 이용해서 SOCKS4, SOCKS5 proxy로 `localhost:10000`을 사용하게 하면, 모든 브라우저 리퀘스트가 ssh tunnel을 타게 됨
  - 그리고 그 요청은 public internet에서 ssh server에서 request로 보낸 것 처럼 됨

## 감상

- 이것으로 학교가 3306포트 자체를 차단하고 있다는 사실을 알게 되었음
- 해킹을 하려면 어떻게든지 할 수 있구나.. 라는 것을 깨달음
