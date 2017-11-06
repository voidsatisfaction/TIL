# AbemaTV conference

Cyber agent인턴을 하다가 인사담당 분에게 직접 이번 컨퍼런스에 참여하고 싶다고 부탁했다. AbemaTV는 Cyber agent에서 운영하는 인터넷 TV인데, 현재 매우 큰 인기를 끌고 있다.

원래부터 컨퍼런스 전용 웹사이트 `connpass.co.jp`에 지원했으나 사람이 너무 많은 관계로 보결로 밀려났는데 인사담당 분에게 직접 문의하니까 참가가능으로 해주셨다. 미네기시씨에게 감사감사.

## 내용

### 1. GCP와 AbemaTV

GCP는 Google Cloud Platform으로, 주로 웹 서비스의 클라우드 플랫폼의 역할을 담당하는 서비스다. 개발자는 서버나 로드벨런서(LB)를 직접 설치할 필요 없이 GCP에서 제공하는 서비스를 각각 이용하므로써 원하는 서비스를 만들 수 있다.

AbemaTV에서도 Application기반 시스템과 분석기반 시스템에서 각각 GCP를 사용하고 있다. 특히 Application기반 시스템에서는 GKE과 GLB를 사용하고 있다고 한다.

- GCP의 Application서비스
  - GAE(Google App Engine): PAAS
  - `GKE`(Google Kubernates Engine): CAAS
  - GCE(Google Compute Engine): IAAS

`Kubernates`라는 컨테이너 관리 서비스를 사용한다면 GKE가 추천이라고 한다.

### 2. 전국에 장기 생중계를 해보다

프로그래밍 적인 내용 보다는 실제 현장에서 어떠한 식으로 생중계를 기획하고 찍는지에 관한 에피소드 소개.

무려 국보에서 생중계를 한 적도 있다고 한다(도대체 랜선은 어떻게 연결한걸까)

초기에는 Skype를 사용해서 연결하다가 LiveU라는 이스라엘산 최신기술을 이용해서 중계를 한다고 한다.

위성 중계차는 상상이상으로 비싸다.

### 3. AbemaTV와 화질에 관한 이야기

녹화방송은 매우 매니악한 분야이다. 화질 프로그래밍에 있어서 중요한 키워드 네가지

1. CODEC: Coder / Decoder (정보의 압축)
2. Container(file extension): 어떠한 식으로 정보를 압축했는가
3. Transcode: 코드의 변환
4. ~

원본(Master Data)의 품질을 보증하면서 디지털화 하는 것이 관건.

AbemaTV에서는 적합 영상 생성을 자동화 하고 있다.

음량도 매우 중요. `loudness war` 각각의 영상의 음량이 다르기 때문에 일정하게 유저가 듣기 좋은 크기로 맞추는 작업이 필요하다.

### 4. AbemaTV Mobile Client의 작업 방식

- 개발 방식: 스크럼, 개발1주일 QA1주일
- 우선도: S, A, B, C, D
- 회의: 스프린트 계획, 스프린트 리뷰 -> 되도록 디자인과 PM까지 알기 쉬운 언어로.
- 툴: Slack, JIRA, Confluence, Bitrise, Jenkins, Cmdshelf(자체개발)
- 개발 스타일: Pull request, code review, code custom, test, QA효율화(디버그 메뉴)

### 5. AbemaTV 디자이너의 Before After

반년동안 행했던 디자인 변경.

twitter링크와 관련된 AbemaTV의 다운로드율이 적은 문제 -> 유저가 원하는 방송이 나오도록 조정 -> 다운로드율 향상.

> 데이터는 의사결정에 있어서 매우 중요한 역할을 차지한다. 문제와 해결책 둘 다 데이터에서 찾을 수 있다.

### 6. AbemaTV의 Monitoring시스템

Helm, Promethus라는 툴을 쓴다고 한다.

내용이 어려워서 잘 이해하지 못했다.

### 7. Microservices on Client AbemaTV

AbemaTV의 클라이언트는 Nodejs의 grpc를 사용하는데, request timeout이 없어서 고생했다고 한다. 또한, 에러처리를 제대로 하지 않으면 크나큰 재양을 초래한다는 교훈을 얻었다.

CDN의 이용은 속도가 매우 빨라진다는 이점이 있으나, 아키텍쳐가 복잡해진다는 문제를 갖고 있다.

Server Side Rendering의 이용.

### 8. AbemaTV를 지탱하는 애플리케이션의 상냥함



## 느낀점
