# Shell Options

## 의문

## 개요

- `set`
  - 쉘이 동작하는 방식을 옵션을 통해 컨트롤 하는 방법
  - 설정된 옵션은 `$-`특수 변수에 저장됨
- 옵션 종류
  - `set --`
    - 현재 설정되어 있는 positional parameters를 전부 삭제
  - `set -`
    - xtrace, verbose 옵션을 끔
  - `-a`
    - 설정한 함수, 변수들이 자동으로 export되어서 child process에서 사용 가능하게 됨
  - `-C`
    - redirection에 의해서 파일이 overwrite되지 못하도록 함
  - `-e`
    - script 실행중에 명령이 에러로 종료하면 exit
      - `if`, `while`, `until`, `||`, `&&`같은 분기문에서는 예외
