# SSH 포트포워딩을 이용해서 3306포트 차단 우회하기

## 배경

내가 다니는 대학교에서 보안상의 이유로 3306포트를 막아두었다. 그래서 데이터베이스 개발이 매우 힘들었는데, 내가 토이프로젝트를 돌리는 aws lightsail과 ssh 포트포워딩을 이용해서 aws rds의 mysql에 접속할 수 있었다.

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

## 감상

- 이것으로 학교가 3306포트 자체를 차단하고 있다는 사실을 알게 되었음
- 해킹을 하려면 어떻게든지 할 수 있구나.. 라는 것을 깨달음
