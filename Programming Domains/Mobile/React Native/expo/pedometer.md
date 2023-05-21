# Pedometer

- 개요
- 구현

## 개요

- 걸음수를 세어주는 API
  - 참고
    - https://docs.expo.dev/versions/latest/sdk/pedometer/
    - https://github.com/expo/expo/issues/16605
    -

## 구현

- ios
  - 코드 작성하면 사용 가능
- android
  - `app.json`에서 `android.permissions`에 `ACTIVITY_RECOGNITION`을 추가해주기
    - *`com.google.android.gms.permission.ACTIVITY_RECOGNITION`로 하면 되는지 확인 필요*
  - react native의 `PermissionsAndroid.request`로 권한(`PermissionsAndroid.PERMISSIONS.ACTIVITY_RECOGNITION`) request하기
    - *이것도 의미가 있긴한지는 체크해봐야 함*
