# Study Series Image

- 의문
- Study vs Series vs Image

## 의문

## Study vs Series vs Image

한명의 patient는 여러개의 study를 갖을 수 있음

- Study
  - patient가 여러 검사를 행한 날에 대한 기준
  - 하나의 dicom은 하나의 study를 갖음
- Series
  - 실전 case(case가 분리되는 이유는 modality에 기인)
    - case1
      - 하나의 series에 여러개의 image를 갖음, 즉 PACS에서는 뷰어가 이미지를 다수 rendering함
      - series: chest
      - image: PA, AP, LAT (등 여러장)
    - case2
      - 하나의 series에 하나의 image를 갖음, 즉 PACS에서는 뷰어가 이미지를 하나만 rendering함
      - series: chest PA, chest AP, chest LAT
      - image: series에 해당하는 이미지 한장
  - 하나의 dicom은 하나의 series를 갖음
- Image
  - 하나의 series는 여러개의 image를 "dicom표준 상" 갖을 수 있음
    - 그러나 대부분은 이미지도 하나만 갖음(e.g CT)
    - maybe modality의 문제
