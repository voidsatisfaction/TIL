# 2021 Opensource Contributon

## 멘토님의 팁

- General
  - 구체적인 목표를 세워라
    - 어떤 라이브러리의 어떤 모듈을 구현할 것인지, 개선할 것인지?
  - 아낌없이 물어보라
    - 도움을 많이 요청하면 요청할 수록 이득을 본다
  - 질문을 public한 창구에 하라
  - 뭔가 하는데 막힌다
    - 시간을 정하고, 답이 안나오면 질문해라
- 언어 공부
  - Rust '그 책'을 계속 처음부터 천천히 읽지말고, 빠르게 한번 훑어라
  - 그러면 어디에 무엇이 있는지 아니까 다음에 모르는 개념이 나올때마다 빠르게 찾아볼 수 있다
  - 그다음에 나중에 정독하면 내용 정리가 됨

## 질문

- 왜 RustPython이 시작되었는가? CPython도 있는데
  - 1 CPython의 경우, reference count를 수동으로 갱신한다
    - 버그 확률이 높음
  - 2 웹 어셈블리 서포트
  - 3 GIL이 없음
    - 그런데, 오히려 GIL이 없어서 자료구조마다 lock을 해야하니까 있는것보다 성능은 더 안좋음(?!)
- 왜 폴더에서 VM이라는 이름을 사용할까?
  - interpreter를 vm으로 표현하나봄
  - 바이트 코드를 읽고 실행시켜서?

## 2021.07.31. 깃 기초 교육

깃 기능(도구)들은 개발하는 시나리오에 맞춰서 생각해보라

- 깃 프로젝트를 읽어보자
  - `git shortlog -sn (-- 폴더/파일)`
    - 해당 폴더나 파일의 커밋이 많은 사람들과 커밋수를 보여줌
  - `git show commitid`
    - 해당 커밋의 자세한 내용 보여줌
  - `git log -p`
    - 코드 수정내역까지 자세히 보기 보여줌
  - `git log --oneline --no-merges --after=2020-01-01 -- mnist/`
    - 한줄로 merge커밋 제외한 2020-01-01이후의 mnist폴더의 커밋 로그 보여줌
- 커밋 팁
  - 커밋 타이틀의 첫 단어를 잘 선택하는게 좋다
    - update(x), fix(o)

### 오픈소스 개발참여 준비 Git 설정하기

- 깃허브 캐싱 데이터 삭제
  - `git config --global --unset credential.helper`
  - `git config --system --unset credential.helper`
- commit 저자 정보 설정
  - `git config --global user.email "내 이메일"`
  - `git config --global user.name "내 이름"`

### 브랜치

- `git branch -D <브랜치이름>`
  - 브랜치 제거
- `git stash`
  - `git stash pop`
