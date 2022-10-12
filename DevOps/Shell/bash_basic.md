# Bash

## Shell config files

### 1. /bin/bash

The bash executable

### 2. /etc/profile

The systemwide initialization file, executed for login shells

### 3. ~/.bash_profile

The personal initialization file, executed for login shells

> 로그인 쉘을 실행할 때 실행된다.

### 4. ~/.bashrc

The individual per-interactive-shell startup file

> 로그인 쉘이 아닌 새로운 쉘이 시작될 떄마다 실행된다. 그러므로 overhead를 줄이기 위해서 최대한 가볍게 유지되어야만 한다.

### 5. ~/.bash_logout

The individual login shell cleanup file, executed when a login shell exits

### 6. ~/.inputrc

Individual readline initialization file

### 참고: .bash_profile and .bashrc in OSX

OSX는 새로운 쉘을 실행할 때 마다 login shell이 실행되므로
.bashrc가 새로운 로그인 쉘을 실행할때마다 실행되도록 하려면

`[ -r ~/.bashrc ] && source ~/.bashrc`

위의 커맨드를 `.bash_profile`에 넣어야 한다.
