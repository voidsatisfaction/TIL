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

## 감상

- 이것으로 학교가 3306포트 자체를 차단하고 있다는 사실을 알게 되었음
- 해킹을 하려면 어떻게든지 할 수 있구나.. 라는 것을 깨달음
