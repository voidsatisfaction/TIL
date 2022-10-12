# Hair Hit 포스트 모템

- 의문
- 개선점: 아키텍처
  - 1 게임씬은 하나로 가져가자
  - 2 참고할만한 프로젝트 구조
  - 3 인게임 데이터는 암호화하자
  - 4 각종 유니티 훅을 사용해보자
- 개선점: 좋은 툴

## 의문

- *외부 유니티 패키지 같은 경우에는 코드를 직접 넣는게 좋은건지? 아니면 그냥 코드째로 버전관리 하는게 좋은지?*
- *유니티는 싱글스레드로 돌아가고 있는것으로 아는데, 싱글톤 클래스에 락을 넣은 이유는?*
- *IL2CPP란?*

## 개선점: 아키텍처

### 1. 게임씬은 하나로 가져가자

- 씬이 여러개가 있으면 유지보수가 힘들다
  - 특히 일부 씬에서 프리펩이 잘못 넣어져있으면 심각한 에러가 발생한다.

### 2. 참고할만한 프로젝트 구조

이 구조가 좋다는 보장은 없음

- Datas
  - 인게임에서 사용되는 다양한 데이터들
    - Q) 이러한 데이터들은 서버에서 받아오면 되는거같은데, 왜 서버를 통하지 않았는지?
- Project
  - Assets
    - Animations
    - Editor
      - post build, version manager
    - Font
    - Resources
      - Data
        - 암호화한 인게임에서 필요한 데이터 파일들
      - Prefabs
        - Area
        - FX
        - Manager
        - SpriteContainer
        - UI
          - Ingame
          - Popup
          - Tutorial
    - Scenes(충격적이다 이렇게 간단히 하다니)
      - Init.unity
      - Title.unity
      - Ingame.unity
    - Sound
      - BGM
      - SFX
    - Textures(이미지 등)
    - **Scripts**
      - **여기가 핵심**
  - Packages
  - ProjectSettings
  - UserSettings

### 3. 인게임 데이터는 암호화하자

- 당연한건데 이번에는 아직 안해두었다
  - *blowfish알고리즘과 AES256알고리즘의 차이?*

### 4. 각종 유니티 훅을 사용해보자

- `InitializeOnLoadAttribute`
  - Dimain reload시에 해당 어트리뷰트가 있는 클래스의 컨스트럭터가 실행됨

## 개선점: 좋은 툴

- Beebyte Obfuscator
  - 리버스 엔지니어링 방지
  - pyarmor가 생각나는 친구
