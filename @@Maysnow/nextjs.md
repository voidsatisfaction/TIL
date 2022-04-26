# NextJS

- 의문
- 개요
  - nextjs가 제공하는 것들

## 의문

## 개요

- 개요
  - 빠른 웹 애플리케이션을 만들기 위한 building block을 주는 **리액트 프레임워크**
    - 자주 사용되는 building block을 리액트로 개발하면서 필요할때 가져다 쓸 수 있게 함
      - React만으로는 완전히 scalable하고 동작할 수 있는 애플리케이션을 만드는데에 많은 작업이 필요함
    - e.g) routing, data fetching, integrations, ...
- 웹 앱의 building block
  - UI
  - Routing
    - 애플리케이션의 서로 다른 부분들을 유저가 네비게이팅하는것
  - Data Fetching
  - Rendering
    - 언제, 어디서 static 혹은 dynamic 컨텐츠를 렌더하는지
  - Integrations
    - 어떤 서드파티 서비스를 사용하는지 (CMS, auth, payments)
  - Infrastructure
    - 어디에 앱을 배포하고, 저장하고, 실행하는지 (Serverless, CDN, Edge, etc)
  - Performance
  - Scalability
  - Developer Experience

### Nextjs가 제공하는 것들

- 개발 / 배포 환경
  - dev
    - DX향상
    - TypeScript, ESLint, 빠른 reload, ...
  - prod
    - UX향상
    - 퍼포먼스가 좋고, 접근이 쉬운 코드 생성
- 각 환경마다 다른 방식으로 컴파일, 번들링, 미니파이드, 코드 스플릿이 되어야 함
  - Nextjs는 자체 컴파일러가 있음
    - compilation
      - 개발자 친화적인 JSX, TS를 다양한 버전의 자바스크립트들로 변환
    - minification
      - 오직 실행되기 위한 정보만 코드에 저장하기 위함(퍼포먼스, 사이즈 이득)
    - bundling
      - 개발시에는 애플리케이션을 모듈이나 컴포넌트로 쪼개놓음, 그리고 해당 모듈의 의존 그래프는 매우 복잡함. 그러한 의존 관계를 해결하고 파일을 최적화된 번들로 병합하여 파일의 수를 줄이는 역할
    - code splitting
      - 애플리케이션의 번들을 보다 작은 구성요소로 쪼개서, 각 엔트리포인트(url혹은 페이지)마다 나누는 것
      - 애플리케이션의 초기 로드 타임의 개선을 목표로 함
        - 해당 페이지를 구성하는데에 필요한 코드만 로드
      - nextjs에서는 `pages/` 속에 있는 각각의 파일을 빌드타임에 자동적으로 코드 스플릿하여 js 번들로 만듬
      - 추가적으로
        - 페이지 사이에 공유되는 모듈은 또 다른 번들로 쪼개져, re-download를 막음
        - 첫 페이지 로드 이후에, nextjs는 유저가 갈만한 다른 페이지를 pre-load를 시작할 수 있음
        - dynamic import를 사용해서도 처음 로드된 코드와 별도로 수동으로 코드를 나눌 수 있음
- 빌드 타임
  - 개요
    - 애플리케이션 코드를 배포환경을 위해서 준비하는 스텝의 연속을 하는 기간을 말함
  - 특징
    - nextjs는 코드를 production-optimized 파일들로 변환함
      - 정적으로 생성된 페이지들의 HTML파일들
      - 서버에서 페이지를 렌더하기 위한 JS코드
      - 클라이언트에서 페이지를 상호작용하게 만들기 위한 JS코드
      - CSS 파일들
- 런타임
  - 개요
    - 애플리케이션이 생성되고 배포된 이후에, 유저의 리퀘스트에 대한 응답으로 애플리케이션이 동작할때의 기간을 말함
