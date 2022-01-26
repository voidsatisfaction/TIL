# 게임 개발

- 의문
- 1 유니티 인앱 리뷰
- 2 앱스토어 / 플레이스토어 지식

## 의문

## 1. 유니티 인앱 리뷰

- Android
  - 특징
    - SDK 사용
    - 현재는 테스트에서 1번만 보이는 버그가 존재
  - 참고
    - [인앱 리뷰 통합(Unity)](https://developer.android.com/guide/playcore/in-app-review/unity?hl=ko)
    - [Google Play Core 라이브러리](https://developer.android.com/guide/playcore?hl=ko#unity)
    - [play-unity-plugins](https://github.com/google/play-unity-plugins/releases)
- IOS
  - [Device.RequestStoreReview](https://docs.unity3d.com/ScriptReference/iOS.Device.RequestStoreReview.html)

## 2. 앱스토어 / 플레이스토어 지식

- Android
  - [공개, 비공개, 내부 테스트 설정](https://support.google.com/googleplay/android-developer/answer/9845334?hl=ko)
  - 키스토어
    - 앱 개발자에 대한 정보를 서명한 암호화 된 파일
      - 구글 플레이 스토어에 앱을 등록하기 위해서 사용되는 키(APK를 서명)

## 3. 데이터 플랫폼 지식

- GA(Game Analytics)
  - 특징
    - SDK 사용
  - 이벤트 형식
    - `key1:key2:key3`형태
  - 종류
    - Business
      - 인앱구매
    - Resource
      - 재화 흐름
    - Progression
      - 레벨 시도 / 시작 / 실패 / 끝
    - Error
      - 에러
    - Design
      - 임의의 다양한 로그
    - Ads
      - 광고 관련 로그
    - Impression
      - *다른 ad network로부터의 데이터*
      - ?

## 4. 광고 플랫폼 지식

- AppLovin - Max
  - [코드 참고](https://github.com/AppLovin/AppLovin-MAX-Unity-Plugin/blob/master/DemoApp/Assets/Scripts/HomeScreen.cs)
  - [AppLovin - Integration](https://dash.applovin.com/documentation/mediation/unity/getting-started/integration)
