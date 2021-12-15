# CPU

- 의문
- General
  - Rosetta(software)

## 의문

## General

### Rosetta(software)

- 정의
  - macOS를 위한 dynamic binary translator 소프트웨어
    - 서로 다른 명령 집합 아키텍처 사이의 애플리케이션 호환 레이어
- 종류
  - Rosetta
  - Rosetta2
    - 개요
      - 인텔 프로세서로부터 애플 실리콘으로 전환하기 위한 부품
      - Intel 애플리케이션이 Apple silicon 맥에서 동작할 수 있도록 함
    - 특징
      - JIT translation support
        - 앱 자체가 JIT(런타임, 가상화)를 사용하는 경우
      - AOT(Ahead-of-time) compilation
        - 앱이 그 자체로 완결성을 갖는 경우
        - 첫 실행시에 기계어 변환을 함
    - 단점
      - 몇몇 어셈블리어를 포함한 소프트웨어는 자동화되어서 번역되지 않을 수 있음
    - 동작
      - 실행파일이 오직 intel 명령어로만 구성되어 있는 경우에서 출발
      - macOS는 자동적으로 Rosetta를 기동하고, translation을 행함
      - translation이 끝나면, 원래 장소에 있는 번역된 실행파일을 기동함
        - 이때, 살짝 느림
