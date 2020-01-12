# Pynetdicom

- 의문
- 중요한 컨셉

## 의문

## 중요한 컨셉

*여기서 나오는 중요한 컨셉은, DICOM 전체에서 통용되는 개념인지? 아니면, Pynetdicom에서 임의로 정의한 것인지?*

*Study와 Series의 차이는?*

- UIDs(Unique identifiers)
  - `UID = <org root>.<suffix>`
    - `<org root>`
      - 유니크하게 기관을 특정할 수 있는 숫자
    - `<suffix>`
      - `<org root>`의 스코프에서 유니크해야하고, application에 의해서 생성됨
    - 최대 64문자
- DICOM Information Model
  - Information Object Definition(IOD)
    - 객체 지향 추상 데이터 모델
      - e.g) Patient, Study, imaging Series, imaging Equipment
    - 오브젝트 사이의 관계를 정의하기 위해서 사용
      - Patient -> Studies(has a)
      - Study -> Series(has a)
    - 종류
      - composite
        - 관련 현실 오브젝트"들"의 정보를 포함
          - e.g) CT Image IOD는 Patient, Study, Series, Equipment 등의 오브젝트들을 포함
      - normalised
        - single class of 현실 오브젝트들을 나타냄
        - e.g) Print Job IOD
  - SOP Classes
    - *구체적인 예시가 궁금함*
    - Service-Object Pair 클래스는 IOD와 DIMSE(DICOM Message Service Element) 서비스 그룹의 연합으로 정의 됨
    - 종류
      - Composite SOP Classes
        - Composite IOD들과 DIMSE-C 서비스 그룹의 결합
        - 예시
          - CT Image Storage SOP Class(CT Image IOD + DIMSE C-STORE service *(서비스가 결합되었다는건 무슨의미?)*)
            - 하나의 CT Image Storage instance는 한명의 환자 CT스캔의 한조각의 정보를 저장
            - 완전한 스캔(하나의 시리즈)는 하나 또는 그 이상의 CT Image Storage SOP Class 인스턴스들로 구성(Study Instance UID와 Series Instance UID값은 동일하나, SOP Instance UID 값들은 다르다)
      - Normalised SOP Classes
        - Normalised IOD들과 DIMSE-N 서비스 그룹의 결합
        - 예시
          - Print Job SOP Class(Print Job IOD + DIMSE N-EVENT-REPORT + N-GET 서비스들)
          - 프린트 job의 추상(하나나 그 이상의 필름이 프린트 되기위한)
    - 모든 DICOM SOP 클래스는 각자의 UID를 갖고 있음
  - Service Classes
    - 하나의 DICOM Service 클래스는 하나나 그 이상의 AE(Application Entity)들이 커뮤니케이션하는 서비스와 관련있는 SOP 클래스들의 그룹을 정의
    - 서비스는 SOP 클래스 인스턴스들의 storage(Storage Service Class), DICOM connectivity의 verification(Verification Service Class), querying and SOP 인스턴스들의 retrieval(Query/Retrieve Service Class), 이미지의 printing(Print Management Service Class)과 다른것들을 포함
    - Service Class User / Service Class Provider 는 AE 서비스 클래스 안에 있는 서비스들을 사용하거나 제공하는 것으로 구별됨
  - Application Entities(AE)
    - DICOM AE는 DICOM 표준, IODs, service classes, dataset encoding/decoding을 지원
