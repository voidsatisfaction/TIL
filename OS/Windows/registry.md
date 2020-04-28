# 윈도우 레지스트리

- 의문
- 개요
  - 구조
  - c.f) Windows Registry가 Linux에 대응하는 대상

## 의문

## 개요

- 정의
  - MS Windows 32/64 버전과 모바일에서 **운영체제나 애플리케이션의 설정을 담고 있는 데이터베이스**
    - 모든 하드웨어, 운영 체제 소프트웨어, 대부분의 비운영 체제 소프트웨어, 사용자 PC 선호도 등에 대한 정보와 설정이 포함
    - e.g
      - 사용자가 제어판 설정 등을 변경 -> 변경 사항들이 레지스트리에 반영되어 저장
    - 참고
      - 이전에 윈도우 프로그램에 대한 구성 설정을 담는 데에, 각 프로그램마다 `INI`파일이 사용되었으나, 이러한 파일들이 시스템 여러 곳에 퍼짐으로써 찾기 힘들었는데, 그래서 윈도우 레지스트리가 도입

### 구조

- 개요
  - 기본적으로 트리구조
    - 노드 = 키
    - 칠드런 = 서브키 or 값
  - 키, 값으로 이루어져 있음
- 구성
  - 키
    - 키는 폴더와 비슷함
    - 키는 서브키를 가질 수 있음
    - 예시
      - `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows`
        - `HKEY_LOCAL_MACHINE`키의 `Software`서브키의 `Microsoft`서브키의 `Windows`라는 서브키
  - 값
    - 키 안에 들어 있는 이름/자료
    - 종류
      - `REG_NONE` 종류 없음
      - `REG_SZ` 문자열 값
      - `REG_BINARY` 이진값(임의의 데이터)
      - `REG_DWORD/REG_DWORD_LITTLE_ENDIAN` 32비트 정수 (리틀 엔디언)
      - ...
  - 하이브
    - 수많은 논리를 구분하는 구분자 역할
    - **HKEY**로 시작
      - `HKCU`, `HKLM` 등과 같이 줄임말을 사용
    - 응용프로그램의 경우 설정 항목 검색
      - `HKEY_CURRENT_USER\Software\제조업체이름\응용 프로그램 이름\버전 번호\설정 이름` 이후
      - `HKEY_LOCAL_MACHINE\Software\제조업체이름\응용 프로그램 이름\버전 번호\설정 이름` 검색
    - 설정 항목 기록
      - `HKEY_LOCAL_MACHINE` 부터 기록 혹시 로그인한 사용자가 관리자가 아니라 기록하지 못한경우
      - `HKEY_CURRENT_USER` 에 기록
    - 종류
      - `HKEY_CLASSES_ROOT(HKCR)`
      - `HKEY_CURRENT_USER(HKCU)`
        - 현재 로그인한 사용자의 설정
      - `HKEY_LOCAL_MACHINE(HKLM)`
        - 컴퓨터의 모든 사용자의 설정
      - `HKEY_CURRENT_CONFIG`
        - 실행 시간에 수집한 자료를 담고 있음
        - 디스크에 영구 저장(x)

### 편집

- 수동 편집
  - `regedit.exe` or `regedit32.exe`를 실행
    - 레지스트리 편집에 앞서 백업 권장
- `.REG` 파일
  - 키를 제거하려면 `[...]`앞에 하이픈 추가
    - e.g) `[-HKEY_LOCAL_MACHINE\...]`

`.REG` 파일의 예시

```reg
REGEDIT4

[HKEY_CURRENT_USER\Software\Battle.net\Configuration]
"Battle.net Gateways"=hex(7):31,30,30,31,00,30,31,00,62,6e,65,74,64,2e,66,69,\
73,68,62,61,74,74,6c,65,2e,6e,65,74,00,2d,39,00,\
46,69,73,68,20,53,65,72,76,65,72,00,66,62,73,74,\
65,73,74,2e,70,65,72,6c,2e,73,68,00,2d,39,00,46,\
69,73,68,20,54,45,53,54,20,53,65,72,76,65,72,00,\
75,73,77,65,73,74,2e,62,61,74,74,6c,65,2e,6e,65,\
74,00,38,00,55,2e,53,2e,20,57,65,73,74,00,75,73,\
65,61,73,74,2e,62,61,74,74,6c,65,2e,6e,65,74,00,\
36,00,55,2e,53,2e,20,45,61,73,74,00,61,73,69,61,\
2e,62,61,74,74,6c,65,2e,6e,65,74,00,2d,39,00,41,\
73,69,61,00,65,75,72,6f,70,65,2e,62,61,74,74,6c,\
65,2e,6e,65,74,00,2d,31,00,45,75,72,6f,70,65,00,\
00

[HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\Main]
"Window Title"=""
"Start Page"="http://www.a-experience.com/RedirectAd.html"%
```

- Commandline 편집
- API 이용
  - `RegOpenKey`, ..., `RegLoadKey` 등등

### c.f) Windows Registry가 Linux에 대응하는 대상

1:1 매칭은 아니다

- config
  - `/etc`
    - machine specific configs
  - `home`
    - 유저에 국한된 세팅은 dotfile 형태로 저장
  - 등등...
