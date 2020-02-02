# cornerstone js

- 개요
- 컨셉

## 개요

- 웹 기반 medical imaging platform
  - DICOM 파일의 웹 뷰어 역할
    - 히트맵 표현
    - viewport 조작 등이 가능

## 컨셉

- Enabled Elements
  - interactive medical image를 보여주는 `div`태그
  - 이미지 출력 과정
    - ① cornerstonejs 라이브러리 import(script tag or commonjs import)
    - ② 하나 혹은 그 이상의 image loaders(cornerstone이 pixel data를 업로드하기 위해서 사용하는) js 파일을 참조
    - ③ DOM에 이미지를 표시하기 위한 DOM element를 추가
    - ④ CSS를 사용해서 해당 element를 원하는 width와 height에 맞춰서 위치를 배치시킴
    - ⑤ `enable()` api를 호출해서 element가 이미지를 표시하는 것을 준비시킴
    - ⑥ `loadImage()` 를 호출해서 image를 로드함
    - ⑦ `displayImage()`를 호출해서 loaded image를 표시함
  - cornerstone tools library를 사용해서 windowing, pan, zoom, measurements를 수행할 수 있음
  - cornerstoneWADOImageLoader를 사용해서 WADO로부터 직접 데이터 uri를 제공받아서 데이터를 표시할 수 있음
    - 대신 그 떄에는 [여기](https://github.com/cornerstonejs/cornerstoneWADOImageLoader/blob/master/src/imageLoader/wadouri/register.js)에서 지정된 `dicomweb`, `wadouri`, `dicomfile`을 scheme으로 갖는 imageID를 생성해야 함
- Image Ids
  - 개요
    - cornerstone이 표시할 하나의 이미지를 특정하는 URL
    - cornerstone은 url의 scheme을 보고 어떤 이미지를 로드할 지 결정함
      - 동시에 다른 프로토콜을 써서 다양한 방법으로 데이터를 가져올 수 있게 함
    - image loader가 URL의 컨텐츠와 포맷을 결정함
  - 예시
    - `wadouri://localhost:5000/static/images/123.dicom`
- Image Loaders
  - 개요
    - ImageId를 인자로 받고 그에 대응하는 Image Load Object를 반환하는 js function
      - Image Load Object는 Promise를 포함
