# 설정

- 의문
- timeout 설정

각 설정은 자주 사용되는 순으로 나열

## 의문

## timeout 설정

- `connection_timeout`
  - MySQL 서버 접속시에 접속실패 메시지를 보내기까지 대기하는 시간
- `wait_timeout`
  - 활동하지 않는 TCP/IP, UNIX 소켓 커넥션(Client program을 사용하는 경우)을 닫기 전까지 대기하는 시간
- c.f) `interactive_timeout`
  - interactive모드(mysql client의 interactive mode)에서의 timeout
- `innodb_lock_wait_timeout`
  - innodb 트랜잭션이 row lock을 해소하기전까지 대기하는 시간
