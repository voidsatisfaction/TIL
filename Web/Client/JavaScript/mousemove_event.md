# mousemove 이벤트 정리

## mousemove 이벤트란

- 마우스가 움직일 때 발생하는 이벤트
- 종류
  - clientX, clientY
    - 유저의 브라우저에서의 상대적 위치
    - 스크롤 무시
  - pageX, pageY
    - 전체 문서 기준 상대적 위치
    - 스크롤 포함
  - screenX, screenY
    - 클라이언트의 전체 스크린 기준 상대적 위치
    - 스크롤 무시
  - offsetX, offsetY (이는 mousemove이벤트에만 속하는 것이 아님)
    - 이벤트의 대상이 기준(이벤트가 걸려있는 객체 기준)
    - 버튼을 클릭하면, 버튼 클릭의 객체에서 어느정도 떠러져있는지 확인 가능
  - ...
