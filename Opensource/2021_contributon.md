# 2021 Opensource Contributon

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
