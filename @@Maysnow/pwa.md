# PWA

- 의문
- 개요
  - PWA 조건
- PWA를 모바일 앱으로 배포하기

## 의문

## 개요

[awesome-pwa](https://github.com/hemanth/awesome-pwa)

### PWA 조건

- **Discoverable**
  - 검색 엔진에서 발견 가능해야 함
- **Installable**
  - 디바이스의 홈 스크린이나 앱 런쳐에 설치가능해야 함
- **Linkable**
  - URL을 보내서 공유 가능해야 함
- **Network independent**
  - 오프라인이나 network connection이 좋지 않아도 동작해야 함
- **Progressively enhanced**
  - 과거 버전의 브라우저에서도 사용가능해야 하나, 최신 버전에서 가장 잘 동작해야 함
- **Re-engageable**
  - 새 컨텐츠가 사용가능할때 언제든지 noti를 보낼 수 있음
- **Responsively designed**
  - 어떤 해상도의 디바이스에서도 사용가능 함
- **Secure**
  - 유저와 앱과 서버 및 서드파티와의 연결이 안전해야 함

위의 조건을 다양한 기술로 구현할 수 있으면 그것이 PWA

- 기술(사파리는 일부 기능 제한존재)
  - Service Workers
  - Web App Manifest
  - Web Push API
  - Notifications API
  - Cache API
  - Web Storage & IndexedDB

## Feature how to

- **Installable**
  - manifest 파일에 정보를 포함시킴
    - 정보
      - 앱 title
      - 모바일 OS에서 앱을 나타내는 사용되는 다른 크기의 아이콘들의 경로
      - 로딩 또는 스플래시 화면에서 사용할 배경 색상 등
    - 최소 요구 사항
      - required
        - `name`과 적어도 하나 `src`, `size`, `type`을 포함하는 아이콘
      - optional
        - `description`, `short_name`, `start_url`

### 필수 구성 요소

## PWA를 모바일 앱으로 배포하기

- 배포
  - https://www.pwabuilder.com/
- Playstore
  - [참고1](https://marshallku.com/web/tips/pwa%EB%A5%BC-%EC%8A%A4%ED%86%A0%EC%96%B4%EC%97%90-%EC%B6%9C%EC%8B%9C%ED%95%98%EA%B8%B0)
- Appstore
  - 불가능
