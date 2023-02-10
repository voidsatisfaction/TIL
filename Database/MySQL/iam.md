# MySQL IAM(Identity and Access Management)

- 의문
- 개요
  - 유저 생성
  - 권한 조회
  - 권한 부여

## 의문

## 개요

### 유저

- 생성
  - `CREATE USER 'username' IDENTIFIED BY 'password'`
    - `CREATE USER 'server-new-settlement-prod' IDENTIFIED BY 'password';`
    - 암호 생성할떄 참고할 랜덤 스트링
      - https://www.random.org/passwords/?num=100&len=24&format=html&rnd=new
- 삭제
  - `DROP USER 'username'@'server이름(%)'`

### 권한

- 조회
  - `SHOW GRANTS [ FOR username ]`
    - `SHOW GRANTS FOR 'server-new-settlement-prod'@'%'`
- 부여
  - `GRANT [USAGE] ON *.* TO 'server-new-settlement-prod'@'%';`
    - 아무런 실질적인 권한이 없음
  - `GRANT [ALL PRIVILEGES] ON tada.* TO 'server-new-settlement-prod'@'%';`
    - `tada`데이터베이스의 모든 테이블에 모든 권한을 부여
- 삭제
  - `REVOKE [권한] ON [DB].[TABLE] FROM 'username'@'server이름(%)'`
