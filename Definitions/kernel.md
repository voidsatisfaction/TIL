# Kernel

- 의문
- General
  - inotify

## 의문

## General

### inotify

- 정의
  - filesystem을 확장하여, filesystem의 변화를 알아채고, application에 전달하는 Linux kernel subsystem
    - `dnotify`를 대체
- 특징
  - GNU C Library(`glibc`)에 필요한 라이브러리 인터페이스가 추가됨
- 사용
  - 웹 서버를 자동으로 re-load 해주는 라이브러리도 이것을 사용할듯?
- 한계
  - recursive watching directory가 안됨
    - inotify watch를 모든 서브디렉터리 마다 해줘야 함
  - 일부 이벤트는 report하지 않음
  - NFS와 같은 곳에서는 사용불가
    - 일부의 클라이언트의 change가 모든 클라이언트에게 즉시 broadcast되지 않음
  - rename event를 직접적으로 다룰 수 없음
    - 서로 다른 두 이벤트를 발행
