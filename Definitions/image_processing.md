# 용어 정리

- pixel
- grayscale
- channel
- luminance
- shader
- 색상 용어
  - 명도
  - 채도
- viewport
- window

## General

- pixel
  - picture element
  - 이미지를 구성하는 최소 단위
- grayscale
  - image인데, 각각의 pixel의 값이 빛의 양(강도)을 나타내는 하나의 샘플(sampling)을 나타내는 것
  - 즉, 오직 intensity 정보만 갖고 있음
- channel
  - grayscale image인데, primary color(e.g RGB)중 하나로만 만들어진 것
- luminance(휘도)
  - **텔레비전이나 컴퓨터 등의 표시 화면으로부터 방사되는 빛의 밝기**
    - 인간이 느끼는 주관적 밝기와 비교적 잘 대응하도록 정해진 시각 자극의 강도
- shader
  - 화면에 출력할 픽셀의 위치와 색상을 계산하는 함수
- 색상 용어
  - **명도**
    - 색의 밝고 어두운 정도
    - 명도가 높으면 흰색에 가깝고, 낮으면 검은색에 가까움
  - 채도
    - 색의 강약 / 맑고 탁한 정도
    - 채도가 높으면 본래 색에 가깝고, 낮으면 흰/검 색에 가까움

![](./images/image_processing/window_and_viewport1.png)

- window
  - world coordinate에 속해있는 다각형의 area
- viewport
  - display device에 종속된 좌표계에서의 area ∧ 컴퓨터 그래픽스에서 다각형의 viewing region
    - window를 viewport에 매핑하여 사용자가 자신의 디바이스에서 적당한 크기로 해당 내용을 볼 수 있음
    - **world-coordinates window clipping -> window-to-viewport transformation -> viewport rendering**
  - physical-device-based 좌표계가 portable하지 않으므로, 정규화된 device coordinates로 알려진 소프트웨어 추상 계층이 viewport를 표현하는데에 상요됨
