# 쉘 스크립트와 환경변수

- 참고
- 의문
- 개요
  - 커맨드

## 참고

- https://askubuntu.com/questions/205688/whats-the-difference-between-set-export-and-env-and-when-should-i-use-each

## 의문

## 개요

test.txt

```
line one
line two
```

- 기본적으로 쉘 스크립트는 전역 환경변수를 참조 가능
  - 만약 전역 환경변수가 `GREP_OPTIONS='-v'`가 설정되어있는 경우
  - `grep one test.txt` -> line two
- 지역 환경변수는 다음과 같이 사용 가능
  - `GREP_OPTIONS='-v' grep one test.txt` -> line two
  - 이건 적용안됨
    - `GREP_OPTIONS='-v'`
    - `grep one test.txt` -> line one

### 커맨드

- `set`
  - 로컬 환경변수를 설정하는 함수
  - `set GREP_OPTIONS='-v'`
    - bash에서는 생략 가능
- `export`
  - 전역 환경변수를 설정하는 함수
  - `export GREP_OPTIONS='-v'`
