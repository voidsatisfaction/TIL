# Hacking

- Web Hacking
  - Client-side
    - XSS
  - Server-side
- Reverse Engineering
- System Exploitation
- Cryptography Fundamental

## Web Hacking

### Client-side

#### XSS(Corss Site Scripting)

- 개요
  - 서버의 응답에 공격자가 삽입한 악성 스크립트가 포함되어 사용자의 웹 브라우저에서 해당 스크립트가 실행되는 취약점
  - 임의의 악성 스크립트를 실행하여, 사용자 쿠키 또는 세션을 탈취해 사용자의 권한을 얻거나 사용자의 페이지를 변조하는 등의 공격 수행 가능
- 공격의 조건
  - **1 입력 데이터에 대한 충분한 검증 과정이 없어야 함**
  - **2 서버의 응답 데이터가 웹 브라우저 내 페이지에 출력시 충분한 검증이 없어야 함**
- 종류(스크립트의 전달 방식 차이)
  - Stored XSS
    - 악성 스크립트가 서버 내에 존재하는 데이터베이스 또는 파일 등의 형태로 저장되어 있다가 사용자가 저장된 악성 스크립트를 조회하는 순간 발생하는 형태의 XSS
      - e.g) 게시판 서비스에서 게시물 조회시
    - 파급력은 서비스의 형태와 접근성, 해당 서비스를 통해 얻을 수 있는 정보 행위에 따라 다름
  - Reflected XSS
    - 악성 스크립트가 사용자의 요청과 함께 전송되는 형태
      - 사용자가 요청한 데이터가 서버의 응답에 포함되어 HTML등의 악성 스크립트가 그대로 출력되어 발생
    - 변조된 데이터가 사용자의 요청으로 전송되는 형태를 유도해야 함
      - e.g) Click Jacking, Open Redirect
    - e.g) 게시물 조회시, 서버는 조회 한 결과를 응답에 출력 + 사용자가 조회한 내용을 포함하기도 함
- 공격의 결과
  - 쿠키 및 세션 탈취
  - 페이지 변조
  - 위치 이동(피싱)
- Mitigations
  - Server-side Mitigations
    - 사용자 입력값 HTML Entity Encoding을 이용해 태그로 인식하지 않도록 escape
      - URI Query, POST Body, User-Agent, Referer와 같은 사용자로부터 입력된 모든 값에 적용해야 함
    - 사용자 입력값에 HTML을 지원하는 경우 화이트리스트 필터링을 해야 함
      - `bleach`라이브러리 이용
    - 로그인 세션에 로그인한 IP주소나 국가를 적어두고, 접속한 국가가 변경된 경우 탐지
  - HTTPOnly flag 사용
    - Javascript에서 해당 쿠키에 접근하는 것을 방지(세션쿠키에 저장)
    - XSS취약점이 발생해도 공격자가 알아낼 수 없음
  - Content Security Policy(CSP) 사용
    - `Content-Security-Policy: <지시어>; ...`
      - `Content-Security-Policy: default-src 'self' *.dreamhack.io`
        - 모든 리소스(이미지 파일, 스크립트 파일 등)의 출처가 현재 도메인이거나 `*.dreamhack.io`도메인일 경우만 허용
        - CDN이 해킹되면 무력화
      - `<meta http-equiv="Content-Security-Policy" content="script-src 'sha256-5jFwrAK0UV47oFbVg/iCCBbxD8X1w+QvoOUepu4C2YA='">`
        - script태그 안의 자바스크립트 코드의 해시를 알아내고 CSP 설정하여 `alert(1)`을 성공적으로 호출한 예시
    - 사이트에서 로드하는 리소스들의 출처 제한
  - X-XSS-Protection Header
    - 최신 브라우저에서는 사용하지 않는다 함

### Server-side

## Reverse Engineering

## System Exploitation

## Cryptography Fundamental
