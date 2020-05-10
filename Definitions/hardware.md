# 하드웨어 용어 모음집

- 의문
- General
  - Bus
  - Hard-disk

## 의문

## General

### Bus

- 정의
  - 컴퓨터나 컴퓨터들 사이에서 데이터를 전달하는 커뮤니케이션 시스템
    - wire, optical fiber 부터, software나 communication protocol을 포함
  - 초기 컴퓨터 버스는, 다수의 하드웨어 연결을 갖는 parallel electrical wires 였으나, 지금은 하나의 parallel electrical bus로서 논리적으로 같은 기능을 수행하는 물리적인 처리기 혹은 처리 방식을 말함

### Hard-disk

하드웨어의 모습 및 구성

![](./images/hardware/hard_disk1.png)

플래터

![](./images/hardware/flatter1.png)

섹터

![](./images/hardware/sector1.png)

트랙

![](./images/hardware/track1.png)

액츄에이터

![](./images/hardware/actuator1.png)

실린더

![](./images/hardware/cylinder1.png)

- 구성
  - Flatter
    - 정의
      - 데이터를 저장하는 장소
    - 특징
      - 위 아래, 둘다 저장 가능(그래서 Actuator도 위 아래로 달려있음)
    - 구성
      - Sector
        - 디스크의 데이터 저장 최소 단위 0.5KB(일반적으로)
      - Track
        - 플래터내 반지름이 같은 섹터들
          - 헤드가 지나치는 길이라 트랙이라 부르는 것
      - Cylinder
        - 하드 디스크내에 존재하는 모든 플래터의 같은 반지름의 트랙들의 집합
  - Actuator
    - 정의
      - Flatter에 있는 데이터를 읽고, Flatter에 데이터를 쓰기위한 장치
    - 구성
      - Head
      - Arm
  - Spindle
    - 정의
      - Flatter를 회전시키는 장치
    - 구성
      - 스핀들 모터
    - 특징
      - 스핀들 모터가 플래터를 돌리는데, 계속해서 플래터를 돌림
      - 액추에이터의 헤드가 필요한 정보가 있는 섹터가 지나가려는 순간 순식간에 해당 섹터에서 정보를 빼감
      - 액추에이터의 헤드는 해당 트랙에 원하는 정보가 없으면 다른 트랙으로 수직으로 이동
    - 성능
      - RPM(Revolutions Per Minute - 분당 회전률)
        - 높을 수록 하드디스크 내용을 읽고 쓰는게 빠름
- 데이터 저장 방식
  - 전제
    - 디스크는 현재 위치에서 순차적으로 근처에 데이터를 저장한다
  - 방식
    - 첫번째 플래터 위편 섹터에 데이터 채움
    - 첫번째 플래터 아래편 섹터에 데이터를 채움
    - 두번째 플래터 위편 섹터에 데이터 채움
    - 두번째 플래터 아래편 섹터에 데이터를 채움
    - ...
    - 모든 높이의 플래터를 다 채우고나면 실린더를 회전시켜서 다음 위치로 이동
