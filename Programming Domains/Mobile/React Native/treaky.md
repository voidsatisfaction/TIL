# RN treaky parts

- 의문
- General
- 키보드

## 의문

## Genearl

- TextInput의 경우, multiline일때에는 return키는 반드시 엔터여야만 한다
  - `returnType`과 같은 property를 설정해도 원하는대로 동작하지 않음
  - 해결책
    - 받아들이자
- ScrollView에 포함된 TextInput에 focus되어있는 경우, ScrollView 외부의 엘리먼트는 focus를 잃지않고 잘 press가능하지만, ScrollView 내부의 엘리먼트를 press하는 경우에는 focus를 잃어버리는 문제가 발생한다
  - 해결책
    - TextInput이 focus되었을 때에는 텍스트 편집만 하는 것이라고 유저에게 주지시킨다(버튼을 숨기고, focus가 풀리면 버튼을 보이게 한다던지)

## 키보드

- 키보드가 올라오고 있을때에는 scroll view의 스크롤을 끝으로 내려보낸다던지 하는것이 불가능
  - 해결책
    - `keyboardDidShow`이벤트 이후에 0.3초 정도 딜레이를 주고 스크롤을 내리는 메서드를 호출
- position이 absolute로 고정된 컴포넌트를 KeyboardAvoidingView로 키보드로 안겹치게 할때, ios에서는 잘 되지 않음(avoiding이후에 다른 위치로 컴포넌트가 고정됨)
  - 해결책
    - `Keyboard.addListener('keyboardDidShow', (e) => {e.endCoordinates.height})`를 이용해서 height를 구하고, position을 동적으로 변화시켜주는 방식으로 해결
