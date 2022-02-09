# 게임 개발

- 의문
- 1 유니티 인앱 리뷰
- 2 앱스토어 / 플레이스토어 지식
- 3 데이터 플랫폼 지식
- 4 광고 플랫폼 지식
- 5 트러블 슈팅
  - 5.1 Unity IOS Resolver에서 xcworkspace 생성되지 않는 이슈
- 6 HTTPS 사설인증서 허용하도록 하기

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

- Google play store
  - [공개, 비공개, 내부 테스트 설정](https://support.google.com/googleplay/android-developer/answer/9845334?hl=ko)
  - 키스토어
    - 앱 개발자에 대한 정보를 서명한 암호화 된 파일
      - 구글 플레이 스토어에 앱을 등록하기 위해서 사용되는 키(APK를 서명)

### 인앱구매

- 개요
  - 디지털 재화와 돈을 거래하는 것
- 특징
  - 재화는 일반적으로 string id를 갖음
- 재화 종류
  - subscription
  - consumable
    - 여러번 살 수 있는 것
  - non-consumable
    - 한번만 살 수 있는 것

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
- Mediation Debugger
  - MAX이외의 adnetwork를 붙인 이후에, 정말로 광고가 잘 나오는지 확인하기 위한 디버거
    - https://dash.applovin.com/documentation/mediation/unity/testing-networks/mediation-debugger#within-the-app

## 5. 트러블 슈팅

### 5.1 Unity IOS Resolver에서 xcworkspace 생성되지 않는 이슈

```
iOS framework addition failed due to a CocoaPods installation failure. This will will likely result in an non-functional Xcode project.

After the failure, "pod repo update" was executed and succeeded. "pod install" was then attempted again, and still failed. This may be due to a broken CocoaPods installation. See: https://guides.cocoapods.org/using/troubleshooting.html for potential solutions.

pod install output:
```

- [해결](https://phillip5094.github.io/ios/unity/Unity-iOS-Resolver%EC%97%90%EC%84%9C-xcworkspace-%EC%83%9D%EC%84%B1%EB%90%98%EC%A7%80-%EC%95%8A%EB%8A%94-%EC%9D%B4%EC%8A%88/)

## 6. HTTPS 사설인증서 허용하도록 하기

```cs
// file1
IEnumerator GetRequest(string uri){
    UnityWebRequest request = UnityWebRequest.Get(uri);
    request.certificateHandler = new AcceptAllCertificatesSignedWithASpecificKeyPublicKey();
    yield return request.SendWebRequest ();
    if (request.isNetworkError)
    {
        Debug.Log("Something went wrong, and returned error: " + request.error);
    }
    else
    {
        // Show results as text
        Debug.Log(request.downloadHandler.text);
    }
}

// file2
using UnityEngine.Networking;
using System.Security.Cryptography.X509Certificates;
using UnityEngine;
// Based on https://www.owasp.org/index.php/Certificate_and_Public_Key_Pinning#.Net
class AcceptAllCertificatesSignedWithASpecificKeyPublicKey : CertificateHandler
{
  // Encoded RSAPublicKey
  private static string PUB_KEY = "mypublickey";
  protected override bool ValidateCertificate(byte[] certificateData)
  {
     X509Certificate2 certificate = new X509Certificate2(certificateData);
     string pk = certificate.GetPublicKeyString();
     if (pk.ToLower().Equals(PUB_KEY.ToLower()))
         return true;
     return false;
  }
}
```
