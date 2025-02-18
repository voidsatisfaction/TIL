# 13. 클라이언트 보안

사용자의 입장에서 보안에 신경써야 하는 요소들

- 의문
- 13.1 악성 소프트웨어(악성 코드)
- 13.2 인터넷 활용 보안

## 13.1 악성 소프트웨어(악성 코드)

### 개요

- 유해 프로그램
  - 컴퓨터 프로그램이 의도적 / 비의도적으로 실행되면서 **기밀성, 가용성, 무결성** 등의 보안속성을 침해할 경우 유해 프로그램으로 간주
- 악성 프로그램
  - 의도적으로 컴퓨터의 보안을 침해할 목적으로 작성된 프로그램을 **악성 프로그램** 이라 함
- 악성 프로그램 특성 비교

|구분|컴퓨터 바이러스|트로이목마|웜|
|---|-----------|-------|--|
|자기 복제|O|X|O|
|형태|파일이나 부트섹터 등 감염 대상 필요|유틸리티로 위장하거나 유틸리티 안에 코드 형태로 삽입|독자적으로 존재|
|전파 경로|사용자가 감염된 파일을 옮김|사용자가 다운로드|네트워크를 통해 스스로 전파|
|주요 증상|시스템 및 파일 손상|PC성능 저하, 좀피 PC|네트워크 성능 저하|

- 분류
  - 독립형 vs 기생형
    - 기생형
      - 바이러스, 논리폭탄, 백도어
    - 독립형
      - OS에 스케쥴링 되어서 구동됨
      - 웜(자기 복제 기능만 갖음), 좀비 프로그램(해커 공격에 PC를 감염시키기 위한 프로그램)
  - 자기 복제 여부
    - 바이러스성 악성코드
      - 웜, 바이러스
    - 비바이러스성 악성코드
      - 트로이목마, 백도어
  - 악성코드를 운반하는 payload의 분류
    - 시스템 파괴(오염)
      - 논리 폭탄, stuxnet, 랜섬웨어
    - 공격 에이전트
      - 좀비, 봇
    - 정보 유출
      - 키로거, 피싱, 스파이웨어
    - 잠입(스텔스)
      - 백도어, 루트킷

### 바이러스

- 개요
  - 다른 프로그램을 변형시키도록 하여, 감염 시키는 프로그램
- 세대별 분류
  - 1세대 원시형(Primitive Virus)
    - 코드의 변형이나 변화 없이 고정된 크기를 가지며, 주로 기억장소에 상주해서 부트 영역이나 파일을 감염
  - 2세대 암호화 바이러스(Encryption Virus)
    - 백신 프로그램이 진단할 수 없도록 바이러스 프로그램의 일부 또는 대부분을 암호화시켜 저장
  - 3세대 은폐형 바이러스(Stelth Virus)
    - 기억장소에 존재하면서 감염된 파일의 기리가 증가하지 않은 것처럼 보이게 하며, 백신 프로그램이 감염된 부분을 읽으려고 할 때 감염되기 전의 내용을 보여줘 바이러스가 없는 것처럼 백신 프로그램이나 사용자를 속임
  - 4세대 갑옷형 바이러스(Armour Virus)
    - 여러 단계의 암호화와 다양한 기법 동원으로 바이러스 분석 어렵게 하고, 백신 프로그램 개발 지연
  - 5세대 매크로 바이러스(Macro Virus)
    - 매크로 기능이 있는 MS사 오피스 제품군 이외에 Visio, 오토캐드 등 VBS(Visual Basic Script)를 지원하는 자양한 프로그램에서 활동
      - 비중이 가장 높음
- 매크로 바이러스
  - 데이터 파일 중에 명령어를 실행시키는 MS워드나 엑셀 등에 붙어서 그 파일이 열릴 때 실행됨
  - 위협적인 이유
    - 플랫폼과 무관
    - 대부분 문서는 감염 시키나, 코드 실행부분은 감염시키지 않음
    - 전자메일 등을 통하여 쉽게 전파
    - 실행 파일보다 주의를 덜하기 때문에 피해가 큼
  - PDF 문서도 자바스크립트를 실행할 수 있으므로 공격 대상
- 바이러스 방지책
  - 안티 바이러스 방법
    - 해결책은 예방
    - 그 다음으로 좋은 해결책은 다음을 수행
      - Detection(탐지)
        - 증상
          - 파일 사이즈 증가
          - 갱신 타임스탬프의 변경
          - 저장장치의 잔여공간이 단시간 내에 급격히 변경
          - 디스크 접근횟수의 급격한 증가
      - Identification(식별)
      - Removal(제거)
  - Antivirus Filtering Method
    - signature scanning
      - 특정 바이러스만이 가진 유일한 형태의 signature를 찾아내는 방법
      - 명령어의 나열을 찾는 등
    - behavioral virus scaning
      - 바이러스가 수행 중에 어떤 행동을 보이는지를 추적
      - 웜에 대한 대처능력
- 예방법
  - 신뢰성 있는 업체의 상업 소프트웨어 사용
  - 첨부파일은 신중하게
  - 바이러스 스캐너를 이용하여 정기 검진 및 업데이트
  - Windows Script Host, ActiveX, VBScript, JavaScript는 비활성화
  - 정책을 세우고 교육을 함

### 웜

- 개요
  - 자신을 복제하여 네트워크 연결을 통해서 컴퓨터에서 컴퓨터로 복제본 전송
    - 메일/IMS, 파일 공유, 원격 실행, 원격 파일 전송, 원격 로그인, 모바일 코드 등을 통해서 전파
- 웜의 실행
  - 전파된 시스템에서 시스템의 접근 권한 확보하고 자신을 실행 시키려 함
    - buffer overflow, format string, SQL injection, PHP Injection 등 공격 가능한 시스템의 취약성 이용
      - *format string, SQL injection은 봇이 어떻게 이용한다는 것인지?*
- 대응
  - 웜 확산이 이루어지면 네트워크 활동이 활발해지므로, 네트워크 활동과 사용을 모니터링하면 기본적인 방어 형태 갖출 수 있음
    - Inbound, Outbound 네트워크 모니터링 필요

### 트로이 목마

- 개요
  - 자신의 실체를 드러내지 않으면서 다른 프로그램의 한 유형인 것 처럼 가장하여 활동하는 프로그램
- 특징
  - 패치 파일, 안티-바이러스 소프트웨어, 소프트웨어 최신 버전 등과 같이 유틸리티 프로그램으로 가장하여 설치하게 함
  - 자기 복제 하지 않고, 다른 파일 감염 시키거나 변경 하지 않음
  - 그 대신
    - admin 권한을 부여받음
    - 데이터 파괴
    - 원격 조정
    - 키로거
- 참고
  - 스파이웨어
    - 민감한 정보를 수집하여, 주기적으로 원격지의 특정한 서버에 보내는 프로그램
  - 애드웨어
    - 자동으로 광고를 생성하는 소프트웨어

## 13.2 인터넷 활용 보안

### 쿠키

- 정의
  - 사용자가 인터넷 웹 사이트에 방문할 때 생기는 4KB 이하의 파일
- 용도
  - 사이트 개인화
    - 사용자의 성향 파악을 위한 데이터 저장
  - 장바구니 시스템
  - 웹 사이트 이용방식 추적
  - 타깃 마케팅
    - 광고 대행업체는 제3의 쿠키를 사용자 컴퓨터에 저장하고 사용자의 이용 정보를 수집
      - 실제 domain과 다른 domain의 쿠키 생성
    - 수집한 사용자의 데이터 판매
    - *3rd party cookie*
      - 특정 페이지에 들어가서 광고의 이미지를 request로 가져올 때, response로 cookie설정
- 구조
  - `Set-Cookie: name=value; expires=[Date]; domain=[Domain]; path=[Path]; [secure]`
  - 필드 설명
    - exires
      - 쿠키는 기본적으로 브라우저가 종료될 때까지는 데이터 사용가능. 유효 기간을 설정하면, 브라우저가 종료되어도 지정한 기간 동안은 사용 가능하게 됨
    - path
      - 쿠키 데이터를 생성한 웹 페이지에서만 데이터를 읽을 수 있으나, path를 지정해주면 해당 path 이하에서는 그 쿠키 데이터를 공유 가능
    - domain
      - 도메인 단위에서 쿠키를 읽고 쓰는 권한 설정
  - HTTP 쿠키 관련 보안 설정
    - httpOnly
      - js를 통해 해당 쿠키에 접근하는 것을 차단해주는 속성
      - XSS 공격에 대응하기 위함
    - secure
      - HTTPS 통신일 경우에만 해당 쿠키를 전송
        - HTTP일 때에는 쿠키 전송하지 않음
      - 쿠키에 대한 Confidentiality를 보장
- 취약점
  - XSS 공격
    - 자바스크립트가 사용자의 컴퓨터에서 실행되는 것을 노려서, `document.cookie`라는 명령어로 공격자가 쿠키 유출
  - Sniffing 공격
    - 쿠키가 암호화되지 않을 경우, 평문 노출
  - 공용 PC에서 쿠키 값 유출
    - 하드 디스크에 저장되므로, 간단히 접근 가능

### 세션

- 정의
  - 개별 클라이언트 상태 정보를 서버에 저장하는 기술
    - 서버는 세션 ID를 부여하고, 쿠키를 이용하여 클라이언트와 서버 간에 주고 받음
- 취약점
  - Session ID Hijacking
