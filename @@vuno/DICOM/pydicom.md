# Pydicom

- 의문
- 개요
- pydicom의 핵심 요소
- pydicom 코드 예시
- Pixel Data를 다루는 경우

## 의문

## 개요

- DICOM 파일들(의학적 이미지, 레포트, 방사선치료 오브젝트)을 다루기 위한 파이썬 패키지
- 복잡한 DICOM 파일을 쉽고 파이썬 스럽게 다룰 수 있게 함
- 파일을 수정하고 다시 DICOM 포맷 파일로 수정할 수 있게 함

## pydicom의 핵심 요소

- Dataset
  - 딕셔너리를 래핑한 것
    - 구성
      - key: DICOM tag
      - value: DataElement instance
    - 특징
      - dict의 대부분의 메서드를 사용할 수 있음
      - iteration할 때는, dict와는 다르게, value를 추출함
- `dataset.DataElement
  - 저장하는 것
    - tag
      - DICOM tag
    - VR
      - DICOM value representation
      - 숫자, 문자열의 포맷
    - VM
      - value multiplicity
      - 대부분은 1로 설정되어 있으나, 좌표에서 사용됨
    - value
      - 실제 값
      - 숫자, 문자열, Sequence
  - `dataset.DataElement`의 value가 될 수 있는 것들
    - 1 number, string, etc
    - 2 a list of regular values(e.g a 3-D coordinate)
    - 3 a Sequence instance
      - Sequence는 list로 표현
- Tag
  - 유저 코드에서 직접적으로 사용되지 않음
    - DICOM 키워드를 사용하여 할당하거나 dataelement를 읽을 때 자동적으로 생성되기 때문
  - python int의 확장판
    - 1 DICOM tag가 4바이트가 되도록 강제함
      - `(group, element)` 의 형태
    - 2 DICOM keywod나 (group, element)와 같은 형식의 tuple로 생성가능
    - 3 group, element로 이루어짐
    - 4 `is_private` 속성은 해당 태그가 private인지 체크(그룹 번호가 홀수)
- Sequence
  - python list의 확장
    - list의 대부분의 메서드가 구현

## pydicom 코드 예시

```py
import pydicom
from pydicom.data import get_testdata_files

filename = get_testdata_files("rtplan.dcm")[0]
ds = pydicom.dcmread(filename)

ds
'''
#으로 시작되는 내용은 나의 주석
# DICOM 태그 숫자 / DICOM 키워드          / Value Representation(VR) / 값

# (0008) => 메타데이터
(0008, 0012) Instance Creation Date              DA: '20030903'
(0008, 0013) Instance Creation Time              TM: '150031'
(0008, 0016) SOP Class UID                       UI: RT Plan Storage
(0008, 0018) SOP Instance UID                    UI: 1.2.777.777.77.7.7777.7777.20030903150023
(0008, 0020) Study Date                          DA: '20030716'
(0008, 0030) Study Time                          TM: '153557'
(0008, 0050) Accession Number                    SH: ''
(0008, 0060) Modality                            CS: 'RTPLAN'
(0008, 0070) Manufacturer                        LO: 'Manufacturer name here'
(0008, 0080) Institution Name                    LO: 'Here'
(0008, 0090) Referring Physician's Name          PN: ''
(0008, 1010) Station Name                        SH: 'COMPUTER002'
(0008, 1040) Institutional Department Name       LO: 'Radiation Therap'
(0008, 1070) Operators' Name                     PN: 'operator'
(0008, 1090) Manufacturer's Model Name           LO: 'Treatment Planning System name here'

# (0010) => 환자데이터
(0010, 0010) Patient's Name                      PN: 'Last^First^mid^pre'
(0010, 0020) Patient ID                          LO: 'id00001'
(0010, 0030) Patient's Birth Date                DA: ''
(0010, 0040) Patient's Sex                       CS: 'O'
(0018, 1020) Software Version(s)                 LO: 'softwareV1'
(0020, 000d) Study Instance UID                  UI: 1.22.333.4.555555.6.7777777777777777777777777777
(0020, 000e) Series Instance UID                 UI: 1.2.333.444.55.6.7777.8888
(0020, 0010) Study ID                            SH: 'study1'
(0020, 0011) Series Number                       IS: "2"
(300a, 0002) RT Plan Label                       SH: 'Plan1'
(300a, 0003) RT Plan Name                        LO: 'Plan1'
(300a, 0006) RT Plan Date                        DA: '20030903'
(300a, 0007) RT Plan Time                        TM: '150023'
(300a, 000c) RT Plan Geometry                    CS: 'PATIENT'

# Sequence는 둘 이상의 데이터를 표현할 때 사용하는 데이터 타입
(300a, 0010)  Dose Reference Sequence   2 item(s) ----
   (300a, 0012) Dose Reference Number               IS: "1"
   (300a, 0014) Dose Reference Structure Type       CS: 'COORDINATES'
   (300a, 0016) Dose Reference Description          LO: 'iso'
   (300a, 0018) Dose Reference Point Coordinates    DS: ['239.531250000000', '239.531250000000', '-741.87000000000']
   (300a, 0020) Dose Reference Type                 CS: 'ORGAN_AT_RISK'
   (300a, 0023) Delivery Maximum Dose               DS: "75.0000000000000"
   (300a, 002c) Organ at Risk Maximum Dose          DS: "75.0000000000000"
   ---------
   (300a, 0012) Dose Reference Number               IS: "2"
   (300a, 0014) Dose Reference Structure Type       CS: 'COORDINATES'
   (300a, 0016) Dose Reference Description          LO: 'PTV'
   (300a, 0018) Dose Reference Point Coordinates    DS: ['239.531250000000', '239.531250000000', '-751.87000000000']
   (300a, 0020) Dose Reference Type                 CS: 'TARGET'
   (300a, 0026) Target Prescription Dose            DS: "30.8262030000000"
   ---------
(300a, 0070)  Fraction Group Sequence   1 item(s) ----
   (300a, 0071) Fraction Group Number               IS: "1"
   (300a, 0078) Number of Fractions Planned         IS: "30"
   (300a, 0080) Number of Beams                     IS: "1"
   (300a, 00a0) Number of Brachy Application Setups IS: "0"
   (300c, 0004)  Referenced Beam Sequence   1 item(s) ----
      (300a, 0082) Beam Dose Specification Point       DS: ['239.531250000000', '239.531250000000', '-751.87000000000']
      (300a, 0084) Beam Dose                           DS: "1.02754010000000"
      (300a, 0086) Beam Meterset                       DS: "116.003669700000"
      (300c, 0006) Referenced Beam Number              IS: "1"
      ---------
   ---------
(300a, 00b0)  Beam Sequence   1 item(s) ----
   (0008, 0070) Manufacturer                        LO: 'Linac co.'
   (0008, 0080) Institution Name                    LO: 'Here'
   (0008, 1040) Institutional Department Name       LO: 'Radiation Therap'
   (0008, 1090) Manufacturer's Model Name           LO: 'Zapper9000'
   (0018, 1000) Device Serial Number                LO: '9999'
   (300a, 00b2) Treatment Machine Name              SH: 'unit001'
   (300a, 00b3) Primary Dosimeter Unit              CS: 'MU'
   (300a, 00b4) Source-Axis Distance                DS: "1000.00000000000"
   (300a, 00b6)  Beam Limiting Device Sequence   2 item(s) ----
      (300a, 00b8) RT Beam Limiting Device Type        CS: 'X'
      (300a, 00bc) Number of Leaf/Jaw Pairs            IS: "1"
      ---------
      (300a, 00b8) RT Beam Limiting Device Type        CS: 'Y'
      (300a, 00bc) Number of Leaf/Jaw Pairs            IS: "1"
      ---------
   (300a, 00c0) Beam Number                         IS: "1"
   (300a, 00c2) Beam Name                           LO: 'Field 1'
   (300a, 00c4) Beam Type                           CS: 'STATIC'
   (300a, 00c6) Radiation Type                      CS: 'PHOTON'
   (300a, 00ce) Treatment Delivery Type             CS: 'TREATMENT'
   (300a, 00d0) Number of Wedges                    IS: "0"
   (300a, 00e0) Number of Compensators              IS: "0"
   (300a, 00ed) Number of Boli                      IS: "0"
   (300a, 00f0) Number of Blocks                    IS: "0"
   (300a, 010e) Final Cumulative Meterset Weight    DS: "1.00000000000000"
   (300a, 0110) Number of Control Points            IS: "2"
   (300a, 0111)  Control Point Sequence   2 item(s) ----
      (300a, 0112) Control Point Index                 IS: "0"
      (300a, 0114) Nominal Beam Energy                 DS: "6.00000000000000"
      (300a, 0115) Dose Rate Set                       DS: "650.000000000000"
      (300a, 011a)  Beam Limiting Device Position Sequence   2 item(s) ----
         (300a, 00b8) RT Beam Limiting Device Type        CS: 'X'
         (300a, 011c) Leaf/Jaw Positions                  DS: ['-100.00000000000', '100.000000000000']
         ---------
         (300a, 00b8) RT Beam Limiting Device Type        CS: 'Y'
         (300a, 011c) Leaf/Jaw Positions                  DS: ['-100.00000000000', '100.000000000000']
         ---------
      (300a, 011e) Gantry Angle                        DS: "0.0"
      (300a, 011f) Gantry Rotation Direction           CS: 'NONE'
      (300a, 0120) Beam Limiting Device Angle          DS: "0.0"
      (300a, 0121) Beam Limiting Device Rotation Direc CS: 'NONE'
      (300a, 0122) Patient Support Angle               DS: "0.0"
      (300a, 0123) Patient Support Rotation Direction  CS: 'NONE'
      (300a, 0125) Table Top Eccentric Angle           DS: "0.0"
      (300a, 0126) Table Top Eccentric Rotation Direct CS: 'NONE'
      (300a, 0128) Table Top Vertical Position         DS: ''
      (300a, 0129) Table Top Longitudinal Position     DS: ''
      (300a, 012a) Table Top Lateral Position          DS: ''
      (300a, 012c) Isocenter Position                  DS: ['235.711172833292', '244.135437110782', '-724.97815409918']
      (300a, 0130) Source to Surface Distance          DS: "898.429664831309"
      (300a, 0134) Cumulative Meterset Weight          DS: "0.0"
      (300c, 0050)  Referenced Dose Reference Sequence   2 item(s) ----
         (300a, 010c) Cumulative Dose Reference Coefficie DS: "0.0"
         (300c, 0051) Referenced Dose Reference Number    IS: "1"
         ---------
         (300a, 010c) Cumulative Dose Reference Coefficie DS: "0.0"
         (300c, 0051) Referenced Dose Reference Number    IS: "2"
         ---------
      ---------
      (300a, 0112) Control Point Index                 IS: "1"
      (300a, 0134) Cumulative Meterset Weight          DS: "1.00000000000000"
      (300c, 0050)  Referenced Dose Reference Sequence   2 item(s) ----
         (300a, 010c) Cumulative Dose Reference Coefficie DS: "9.9902680e-1"
         (300c, 0051) Referenced Dose Reference Number    IS: "1"
         ---------
         (300a, 010c) Cumulative Dose Reference Coefficie DS: "1.00000000000000"
         (300c, 0051) Referenced Dose Reference Number    IS: "2"
         ---------
      ---------
   (300c, 006a) Referenced Patient Setup Number     IS: "1"
   ---------
(300a, 0180)  Patient Setup Sequence   1 item(s) ----
   (0018, 5100) Patient Position                    CS: 'HFS'
   (300a, 0182) Patient Setup Number                IS: "1"
   (300a, 01b2) Setup Technique Description         ST: ''
   ---------
(300c, 0002)  Referenced RT Plan Sequence   1 item(s) ----
   (0008, 1150) Referenced SOP Class UID            UI: RT Plan Storage
   (0008, 1155) Referenced SOP Instance UID         UI: 1.9.999.999.99.9.9999.9999.20030903145128
   (300a, 0055) RT Plan Relationship                CS: 'PREDECESSOR'
   ---------
(300c, 0060)  Referenced Structure Set Sequence   1 item(s) ----
   (0008, 1150) Referenced SOP Class UID            UI: RT Structure Set Storage
   (0008, 1155) Referenced SOP Instance UID         UI: 1.2.333.444.55.6.7777.88888
   ---------
(300e, 0002) Approval Status                     CS: 'UNAPPROVED'

# 태그 관련

>>> from pydicom.tag import Tag
>>> t1 = Tag(0x00100010) # all of these are equivalent
>>> t2 = Tag(0x10,0x10)
>>> t3 = Tag((0x10, 0x10)) # (group, element)
>>> t4 = Tag("PatientName")
>>> t1
(0010, 0010)
>>> t1==t2, t1==t3, t1==t4
(True, True, True)

'''

# get

ds.PatientName
ds[0x10, 0x10].value
# DataElement instance를 반환하므로 .value가 필요, 직접 tag name으로 참조는 하지 않는것이 좋음(DICOM keyword가 pydicom dict에 없는 경우에만 사용)

# set

ds.PatientID = "12345"
ds.SeriesNumber = 5
ds[0x10,0x10].value = 'TestMan'

# sequence

ds.BeamSequence[0].BeamName
ds[0x300a,0xb0][0][0x300a,0xc2].value

# DICOM keyword이름을 까먹을 경우
# pat을 포함하는 DICOM keyword를 검색
ds.dir("pat")

# DICOM키워드를 이용해 Data Element를 가져옴
data_element = ds.data_element("PatientName")
data_element.VR, data_element.value

# pixel data에 접근
pixel_bytes = ds.PixelData

# 위보다 더 좋은 코드
pix = ds.pixel_array
pix
```

## Pixel Data를 다루는 경우

- `ds.PixelData`
  - raw bytes를 반환
- `ds.pixel_array`
  - numpy array를 반환
