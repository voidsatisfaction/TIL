# Docker developement best practices

- 의문
- How to keep your images small
- Where and how to persist application data

## 의문

## How to keep your images small

- 적절한 베이스 이미지 사용
- **multistage build를 사용**
  - multistage build
    - 개요
      - 하나의 도커 파일에서 이미지를 넘나들며 artifact들을 전달하고 받아서 사용하는 방식
- 이미지의 레이어 수 줄이기
  - before
    - `RUN apt-get -y update`
    - `RUN apt-get install -y python`
  - after
    - `RUN apt-get -y update && apt-get install -y python`
- **공통 레이어를 공유하는 다수의 이미지는 base image를 만들어서 공유함**
  - 도커는 common layer를 만들어두면, 그것을 캐싱해서 사용함
- production image를 base image로 두고, testing, debugging tool 을 그 이미지 위에다가 올려서 진행하라
- 이미지를 생성할 때는, `prod`, `test`등과 같이 제대로 태깅하라

## Where and how to persist application data

- **application data를 storage driver를 사용해서 writable layer에 저장하는 것을 피애햐 함**
  - 컨테이너 사이즈 증가 & volumes, bind mounts를 사용하는 것 보다 I/O 관점에서 비효율
  - *컨테이너 안에 volume mount되지 않은 디렉터리에 application data를 두지 말라는 것인가?*
- bind mounts는 developement 모드일때만 사용
  - *bind mounts* 가 뭐지?
- `secrets`를 sensitive application data를 저장하는데에 사용
- `configs`를 sensitive 하지 않은 데이터를 저장하는데에 사용
