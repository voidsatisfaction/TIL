# DB security

- 의문
- Postgresql Port open && 기본계정 사용으로 인한 대참사

## Postgresql Port open && 기본계정 사용으로 인한 대참사

- 문제
  - 도커 컨테이너안에서 이상한 프로그램이 실행되고 있는 현상 발견
    - 다행히도 치명적인 악성코드는 아니었음
- 원인
  - Postgresql이 동작하는 컨테이너의 Port가 인터넷상에 오픈되어 있었음
    - 방화벽 Open
    - 도커상에서 Open
  - Postgresql의 기본계정(master)인 postgres유저가 비밀번호 설정없이 오픈되어 있었음
  - Postgresql의 `COPY`를 사용한 프로그램 실행이 가능
    - `COPY (SELECT 1) TO PROGRAM '/bin/echo hi';`
- 해결
  - 컨테이너 port는 닫자
    - 개발환경에서만 열어두자
  - Postgresql의 postgres 유저에 패스워드를 지정하거나 아에 다른 계정을 사용한다.
