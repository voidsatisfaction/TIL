# 보안 용어의 정의

- General
  - Asset
  - Threat
  - Vulnerability
  - Threat Agent
  - Risk
  - Exposure
  - Countermeasure / Safeguard
  - Control
  - Session
- 공격과 방어
  - Xss, Csrf
- 암호학
  - 해시 함수
  - MAC
  - E2EE
- 접근 통제
  - Access Control
  - Authorization
  - Subject, Object, Access
- 웹
  - OWASP Top Ten
  - JWT

## General

### 자산(Asset)

- 정의
  - 조직이 보호해야 할 대상으로서 데이터 혹은 자산 소유자가 가치를 부여한 실체

### 위협(Threat)

- 정의
  - 보안에 해를 끼치는 행동이나 사건
    - 즉, 보안의 목적을 이루지 못하게 하는 것
- 분류
  - interception
    - 비인가된 당사자가 자산으로의 접근을 획득한 것을 의미(불법 복사, 도청) -> 기밀성에 영향
  - interruption
    - 시스템 자산이 손실되거나 손에 넣을 수 없거나 사용 불가능하게 된 것을 의미(하드웨어 파괴, 파일 삭제, 서비스 거부) -> 가용성에 영향
  - modification
    - 비인가된 당사자가 접근하여 그 내용을 변경(DB값 변경, 특정 프로그램 변경) -> 무결성에 영향
  - fabrication(위조)
    - 비인가된 당사자가 컴퓨팅 시스템상에 불법 객체의 위조 정보를 생성(네트워크 통신에 가짜 거래 정보를 만듦) -> 무결성에 영향

### 취약점(Vulnerability)

- 정의
  - 관리적, 물리적, 기술적 약점
    - 위협을 가할 때 이용할 수 있는 대상

### 위협 주체(Threat Agent)

- 정의
  - 취약점을 이용하는 존재

### 위험(Risk)

- 정의
  - 위협 주체가 취약점을 활용할 수 있는 가능성과 그와 관련된 비즈니스 영향
  - 자산(가치) x 위협 x 취약점

### 노출(Exposure)

- 정의
  - 위협 주체로 인해서 손실이 발생할 수 있는 경우
  - 취약점은 조직에 있어서 가능한 피해를 노출시킴

### 대책 / 안전장치(Countermeasure / Safeguard)

- 정의
  - 잠재적 위험을 완화시키기 위해 배치됨
  - 취약점을 제거하거나 위협 주체가 취약점을 이용할 수 있는 가능성을 감소시키기 위한 소프트웨어 설정, 하드웨어 장비, 또는 절차

### 시점별 통제(Control)

- 정의
  - 예방통제(Preventive Control)
    - 사전에 위협과 취약점에 대처하는 통제
  - 탐지통제(Detevtive Control)
    - 위협을 탐지하는 통제로, 빠르게 탐지할수록 대처하기에 용이
  - 교정통제(Corrective Control)
    - 이미 탐지된 위협이나 취약점에 대처하거나, 위협이나 취약점을 감소시키는 통제

### Session

- 정의
  - 통신의 주체(클라이언트, 서버)들 간에 구별 가능한 통신이 진행 중인 상태

### PIN(Personal Information Number)

- 정의
  - 개인 정보 번호
- 특징
  - 비밀번호와 같은 역할을 하나, 0 ~ 9 까지의 숫자로 적은 개수를 입력하는것이 다름
  - 주로, 손 안에 있는 기기의 잠금 기능에 사용됨

## 공격과 방어

### xss, csrf

- xss(Cross-Site Scripting)
  - 개요
    - 공격자가 client-side script를 취약점이 있는 웹 페이지에 삽입하여, 다른 유저들이 해당 스크립트를 실행하도록 하는 공격
  - 시나리오
    - localstorage
      - 다 털려버림
    - cookie
      - httponly 속성을 지정하면, js로 cookie접근 불가능
  - 방어
    - input과 같은 HTMLElement를 다룰때는, escape가 반드시 되도록 설정
    - react의 경우는, jsx를 사용하면 됨
      - 외부 html을 직접 embedding하지 않음
      - `dangerouslySetInnerHTML`을 되도록이면 사용하지 말자
- csrf(Cross-Site Request Forgery)
  - 개요
    - 공격자가 미리 준비한 웹 사이트에서 사용자가 그 페이지를 열람하는 경우, 해당 사용자가 의도하지 않은 행위를 다른 웹사이트에 동작하게 하도록 함
      - 비밀번호 변경, 권한 설정 등
  - 시나리오
    - localstorage
      - 사용자가 접속한 사이트는 same origin이 아니므로 내부 내용이 털리지 않음
    - cookie
      - 다른 origin의 cookie는 털리지 않으나, 이 사이트에서 강제적으로 http리퀘스트를 사용자가 인증이 되어, 세션이 쿠키에 존재하는 사이트로 보내도록 하면, 쿠쿠키에 있는 session정보가 리퀘스트에 헤더에 자동으로 포함되므로, 원하지 않는 action을 취할 수 있음
  - 방어
    - 세션 저장소로 localstorage를 사용
    - cookie를 사용하되, csrf-token을 병용
      - 서버에서 referer를 참조해도 되나, 이것은 쉽게 변경이 가능

## 암호학

### 해시 함수

- 개요
  - 임의의 길이의 데이터를 고정된 길이의 데이터로 매핑하는 함수
    - `f: message -> digest`
      - message
        - 해시 함수의 input
      - digest
        - 해시 함수의 output
- 기능
  - 가변 길이의 키를 고정 길이 값으로 변환
  - 결과 값이 균일하게 분포되도록 키의 비트를 스크램블함
  - 결과 값을 테이블 크기보다 작거나 같은 값으로 매핑
- 좋은 해시 함수의 조건
  - 계산이 빨라야 함
  - 충돌이 적어야 함
- 응용
  - 해시 자료구조
  - HMAC
  - 암호화
    - 패스워드 등
- 종류
  - *MD5*
    - 왜 안쓰게 되었나?
  - SHA256
  - siphash
    - 파이썬 dict의 내장 해시로 사용
    - random seed값을 넣어줘서 dynamic하게 해시 값 생성
- 고정 범위 해시 함수 vs 변동 범위 해시 함수
  - 고정 범위 해시 함수
    - 특징
      - 만일, output이 32비트 정수로 고정 => array의 index로 매핑가능
      - 데이터 찾기에 사용되는 해시 함수들은 input의 chunk를 반복적으로 가공하여 해시 값을 생성
  - 변동 범위 해시 함수
    - 특징
      - 해시 테이블이 확장될 수 있도록 함
        - 정확히는 `hash_function(message, range: int)`
- 왜, 해시함수의 output은 고정된 길이로 할까?
  - hash 자료구조
    - 해시값을 고정된 array의 index로 둘 수 있음
  - 해시 값을 사용하는 알고리즘이 다루기 쉬움(길이가 고정되어있으므로)
    - data structure
    - file format
    - network protocl field

### MAC(Message Authentication Code)

MAC 사용 예제

![](./images/security/mac1.png)

- 정의
  - 메시지의 인증 및 무결성 보호에 쓰이는 작은 크기의 정보
    - **같은 MAC 값임을 확인하면, 동일한 private key를 가지고 있음을 authenticate한 것**
    - **또한, MAC 값이 같음을 확인하면, 메시지가 중간에 변조되지 않았다는 것이므로, 메시지의 무결성을 보장해주는 것이기도 함**
    - 암호화는 메시지에 대한 소극적 공격을 막을 수 있음
    - 적극적 공격을 막기 위해서는 메시지 인증 등의 방법이 필요
- 특징
  - MAC알고리즘은 비밀키를 입력받고 임의 길이의 메시지를 인증하고 MAC를 출력함

### E2EE(End-to-End Encryption)

- 정의
  - 커뮤니케이션을 하는 유저들만 메시지를 읽을 수 있는 커뮤니케이션 시스템
- 특징
  - Telecom providers, Internet providers 등이 감청하지 못하게 함
- 방식
  - 메시지를 보내는 사람에 의해서 메시지가 암호화되나, 서버와 같은 서드파티는 복호화 할 수 없고, 그저 암호화된 채로 저장만 할 수 있음
  - 수신자는 암호화된 메시지를 받고, 복호화 가능
  - 키교환 메커니즘이 필요
    - 서로 public key를 교환해서 그 키로 암호화를 하는 방법
    - 한쪽이 대칭키를 생성하고, 상대편의 public key를 이용해서 대칭키를 encrypt함 상대편은 encrpyted된 대칭키를 본인의 private key로 decrypt해서 대칭키를 받음. 그리고 다른쪽에다가 잘 받았다고 메시지를 보냄
- 취약점
  - 백도어
    - 암호화 과정 자체를 공격하는게 아니고, 엔드포인트 자체를 공격(어쨌든 마지막은 decrypt되므로)

## 접근 통제

### Access Control

- 정의
  - 장소나 자원에 대한 접근(여기서 접근은 CRUD)의 선택적 제한
- 절차
  - authentication
  - policy definition phase(*이것은 미리 정해지는 것인가? 로그인시에 부여되면 policy가 defined되었다고 보는것인가?*)
    - access가 authorized되는 phase
    - authorization은 여기에 해당하는 기능
  - policy enforcement phase
    - access request가 승인되고 승인되지 않는 phase
- c.f) authorization
  - 자원에 접근하는 권한
- *예시(정확히 내가 이해한 것인지)*
  - MSA에서는 API Gateway와 authentication / authorization 서버를 사용해서 Access Control을 행함
  - 유저가 login을 하면, authentication server에서 subject의 identification을 authenticate를 하고, 유저별로, 그에 관련된 authorization token(certificate)를 부여(policy definition)
  - 유저는 해당 token(certificate)를 가지고, 다양한 서비스를 접근 가능함. 그러나, 특정 서비스 접근은 유저에게 부여된 authorization에 포함되지 않을 수 있는데, 그런 경우에는 permission deny를 API Gateway에서 반환함(policy enforcement)
  - 멀티로그인 방지(policy)와 같은 Access Control policy enforcement도 API Gateway에서 담당

### Authorization

- 정의
  - 자원에 대한 접근 권한을 지정하는 기능(access policy와 비슷)
    - authorize한다 == 접근 정책을 정의한다

### Subject, Object, Access

- Subject(주체)
  - 객체나 객체 내의 데이터에 대한 접근을 요청하는 능동적인 개체
- Object(객체)
  - 접근대상이 될 수동적인 개체 혹은 행위, 일어날 아이템
- Access(접근)
  - 주체와 객체 사이의 정보 흐름
    - CRUD 등의 행위를 하는 주체의 활동

## 웹

### OWASP(Open Web Application Security Project) Top Ten

- 1 Injection
  - SQL, NoSQL, LDAP 등
  - 공격자의 신뢰되지 않은 데이터가 인터프리터로 의도하지 않은 커맨드를 실행시키도록 하거나 올바른 인증 없이 데이터 접근할 수 있도록 함
  - CIA
- 2 Broken Authentication
  - 인증, 세션 관리와 같은 코드 구현이 잘못됨
    - 공격자가 password나 keys, tokens를 탈취하거나, 유저들의 id를 일시적 혹은 영구적으로 추측할 수 있음
  - CIA
- 3 Sensitive Data Exposure
  - 민감한 데이터 보호를 제대로 해두지 않음(경제, 건강, 프라이버시 정보 등)
    - 공격자는 데이터를 훔치거나 변경할 수 있음
  - CI
- 4 XML External Entities(XXE)
  - 오래전 혹은 잘못 설정된 XML 프로세서는 external entity reference를 XML 문서 내에서 evaluate함
    - external entity는 내부 파일들을 노출시키는데에 사용되거나, 내부 포트 스캐닝, 외부 코드 실행, DOS 공격에 사용됨
  - CIA
- 5 Broken Access Control
  - 인증된 유저에 대한 authorization 설정이나 제한이 제대로 설정되지 않음
    - 공격자는 인가되지 않은 기능 혹은 민감한 데이터를 보거나 다른 유저의 데이터를 수정할 수 있음
  - CIA
- 6 Security Misconfiguration
  - 잘못 혹은 충분치 않은 설정(open cloud storage, misconfigured HTTP headers, verbose error messages containing sensitive info)
  - 항상 모든 라이브러리, OS는 계속해서 업그레이드 해야 함
  - CIA
- 7 Cross-Site Scripting XSS
  - 적절한 validation이나 escaping 없이 신뢰할 수 없는 데이터를 웹 페이지에 포함할 때 발생
    - 공격자는 스크립트를 희생자의 브라우저에서 실행시켜, 유저의 세션을 갈취하거나, 웹 사이트를 훼손하거나, 유저를 유해한 사이트로 리다이렉트 시킴
  - CA
- 8 Insecure Deserialization
  - 안전하지 않은 deserialization을 행할 때 발생
    - 공격자가 remote code execution을 할 수 있도록 함
    - replay attack, injection attacks, privilege escalation attacks을 가능하게 함
  - CIA
- 9 Using Components with Known Vulnerabilities
  - 취약점이 있는 라이브러리, 프레임워크, 그 외 소프트웨어 모듈과 같은 컴포넌트를 사용할 때 발생
    - 공격자가 데이터를 손실 시키거나, 서버 자체를 빼앗을 수 있음
  - IA
- 10 Insufficient Logging & Monitoring
  - 공격자가 다른 공격을 계속하게 하거나, 다른 시스템을 공격하게 하거나, 함부로 데이터를 추출, 변경, 삭제하게 할 수 있음
  - 보안 공격이 시작되고나서 대부분의 시스템의 경우, 200일이 지나서야 공격 자체를 탐지 하였다
    - 심지어, 내부적으로 발견한것이 아니고, 외부의 제3자에 의해서 발견된 경우가 많음
  - Accountability

### JWT(JASON Web Token)

- 정의
  - 몇가지의 claim을 assert하는 JSON를 포함하는 payload를 갖는 데이터를 생성하는 표준
    - claim + signature
- 구조
  - Header
    - `{'alg': 'HS256', 'typ': 'JWT'}`
  - Payload
    - `{'loggedInAs': 'admin', 'iat': 1422779638}`
  - Signature
    - `HMAC-SHA256(base64urlEncoding(header) + '.' + base64urlEncoding(payload), secret)`
      - MAC(메시지 보내는 주체의 Authenticity, Integrity 보장)
- 결과물
  - `token = base64urlEncoding(header) + '.' + base64urlEncoding(payload) + '.' + base64urlEncoding(signature)`
  - `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dnZWRJbkFzIjoiYWRtaW4iLCJpYXQiOjE0MjI3Nzk2Mzh9.gzSraSYS8EXBxLN_oWnFSRgCzcmJmMjLiuyu5CSpyHI`
- 특징
  - token의 디자인
    - compact
    - URL-safe
    - SSO(Single-Sign-On) context에서 사용 가능
- 기본 필드(claims)
  - header
    - `typ`
      - token type
    - `cty`
      - content type
    - `alg`
      - MAC algorithm
  - payload
    - `iss`
      - Issuer
    - `sub`
      - Subject
    - `aud`
      - Audience
    - `exp`
      - Expiration Time
    - `nbf`
      - Not Before
    - `iat`
      - Issued at
    - `jti`
      - JWT ID
- 단점
  - 강제로 session을 invalidate하게 할 수 없음
    - 그렇게 하려면, 서버쪽에 결국 session을 저장하는 storage를 만들어야 함
    - 근데 그렇게 하면, JWT의 장점이 사라짐
- 취약점
  -

#### User Authentication을 위해서 사용되는 경우 access token의 expiration 문제

- 문제
  - 너무 expiration이 길어도, Spoofing, Replay attack에 취약함
- 해결
  - Sliding Session 전략
    - 개요
      - 세션을 지속적으로 이용하는 유저에게 자동으로 만료 기한을 늘려주는 방법
      - 유저가 액션을 취하면 세션 기한을 늘려줌
  - Refresh Token 전략
    - 개요
      - 로그인을 할 때에 AccessToken과 함께, 그에 비해 긴 만료 시간을 갖는 RefreshToken을 클라이언트에 함께 발급
      - Client는 Accesstoken이 만료되었다는 에러를 받음 => 새 access token발급 요청(with Refresh token)
