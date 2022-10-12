# GameAnalytics

- 의문
- 개요
  - 이벤트 타입

## 의문

## 개요

- sdk를 프로젝트 안에 심는다

### 이벤트 타입

- Business
  - 실제 금액 거래 관련 이벤트
    - 인앱구매, 영수증 검수
- **Resource**
  - 가상 재화의 흐름 관리
    - source(획득)
    - sink(사용)
  - 우리 게임에서는
    - 리워드 광고로 인한 재화 획득
  - 코드 예시
    - `GameAnalytics.NewResourceEvent (GAResourceFlowType.Source, "Grenade", 2, "Looting", "BossKilled");`
- **Progression**
  - 레벨 라이프 사이클 관련
    - Start, Fail, Complete 이벤트들
  - 퀘스트 관련, 마일스톤 관련 등등
  - 주의
    - 한번에 한가지의 이벤트만 트래킹하면서 사용해야 함
  - 우리 게임에서는
    - 레벨 시작, 레벨 실패, 레벨 성공
  - 코드 예시
    - `GameAnalytics.NewProgressionEvent (GAProgressionStatus.Complete, "World_01", "Stage_01", "Level_Progress", 200); // with score`
    - `GameAnalytics.NewProgressionEvent (GAProgressionStatus.Start, "World_01", "Stage_01", "Level_Progress"); // without score`
- **Error**
  - stack trace나 커스텀 에러 이벤트
  - 우리 게임에서는
    - 일반적인 에러, 스택트레이스
  - 코드 예시
    - `GameAnalytics.NewErrorEvent (GAErrorSeverity.Info, "Could not find available server.");`
- Design
  - GUI 요소들의 트래킹, 튜토리얼 진행 상황, 위의 예시가 아닌 다른 이벤트들 기록
  - 주의
    - 너무 많은 eventId의 경우의 수가 생기지 않도록 해야 함
  - 형식
    - eventId: newUserTutorial:namedCharacter:complete
    - value: \[blank\]
  - 코드 예시
    - `GameAnalytics.NewDesignEvent ("Achievement:Killing:Neutral:10_Kills", 123);`
- **Ads**
  - 유저들이 광고와 어떻게 상호작용 했는지, 광고 퍼포먼스의 모니터링
  - 우리 게임에서는
    - 리워드광고
      - 컨티뉴
      - 보상+ 광고
    - 인터스티셜
      - n회 넘어가기당 1회 보기
    - 배너광고
      - 클릭했을 경우
- Impression
  - 다른 광고 네트워크로부터의 impression 데이터
