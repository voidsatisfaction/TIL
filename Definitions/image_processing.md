# 용어 정리

- General
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
- Format
  - SVG(Scalable Vector Graphics)
- Medical image
  - Hounsfield scale(HU)

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

## Format

### SVG(Scalable Vector Graphics)

SVG의 예시

![](./images/image_processing/svg_example1.png)

- 정의
  - **XML 기반의 2차원 벡터 이미지 포맷**
    - XML 텍스트 파일로 이미지와 그 행동이 정의됨
- 특징
  - interactivity, animation 지원
  - XML 기반
    - 탐색, 인덱싱, 스크립트, 압축 가능
      - 압축은 `gzip`알고리즘 으로 한 경우, SVG 1.1 뷰어는 해당 이미지를 보여줄 수 있음(코덱이 존재하나봄)
    - 텍스트 에디터로 변경 가능
  - 현대 웹 브라우저는 svg 렌더링을 지원
  - 기존에 렌더링된 오브젝트에 그루핑, 스타일링, 트랜스포밍, 구성될 수 있음
  - SVG 그리기
    - XML 엘리먼트를 이용
    - SVG DOM을 이용
      - CSS를 이용해서 styling
      - JavaScript를 이용해서 scripting 가능
- 허용 그래픽 오브젝트
  - vector graphic shapes
  - bitmap images
  - text

## Medical image

- Hounsfield scale(HU)
  - 정의
    - raiodensity를 묘사하는 정량 척도
      - 주로 CT scan에서 많이 사용됨(CT number라고도 불림)
      - 물질마다 서로 다른 값을 가지고 있어서, 몸의 부위 볼 떄 특정 HU 값에서 방사선 이미지속의 특정 부위가 잘 보이도록 할 수 있음
        - e.g) 결절을 보기위한 HU값의 범위 존재
  - 특징
    - 물과, 공기를 기준으로 값을 상대적으로 결정 가능
  - 값 예시
    - Air => -1000
    - Fat => -120 to -90
    - Blood(Clotted) => +50 to +75
    - Lung => -700 to -600
    - Steel => +20,000
    - adrenal tumor이며 rediodensity가 10HU 이하인 경우, 거의 양성 adrenal tumor일 확률이 높음
