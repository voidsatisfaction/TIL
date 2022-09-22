# Github

- 의문
- 개요
- PR 오픈시 자동화
- 브랜치 머지시 자동화

## 의문

## 개요

## PR 오픈시 자동화

- 자동 리뷰어 등록
- 자동 레이블 등록

### 자동 리뷰어 등록

- [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
  - PR 오픈시 자동으로 리뷰어 등록
  - protected branch와 연계해서 코드오너가 반드시 approve해야만 하게 만들 수도 있음
- [github organization 세팅](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team)
  - organization을 이용해서 내부의 팀의 일부 사람에게 리뷰하도록 함(랜덤 어사인 가능)
- [auto-assign](https://github.com/kentaro-m/auto-assign/)
  - 깃허브 app
  - review나 assignees를 자동으로 추가 가능

### 자동 레이블 등록

- [레이블러 액션](https://github.com/actions/labeler)
  - 특정 경로의 파일이 수정되었는지의 여부에 따라서 레이블 등록

## 브랜치 머지시 자동화

- 자동 브랜치 방어

### 자동 브랜치 방어

- [protected branch](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#require-pull-request-reviews-before-merging)
