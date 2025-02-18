# Pynetdicom

- 의문
- 중요한 개념
  - UIDs
  - DICOM Information Model
  - Network with DICOM
- 실전 예제

## 의문

- *애초에 normalized, composite IOD를 나눈 이유가 무엇인가?*
  - 둘의 차이가 구체적으로 무엇이지?

## 1. 중요한 개념

- 여기서 나오는 중요한 컨셉은, DICOM 전체에서 통용되는 개념인지? 아니면, Pynetdicom에서 임의로 정의한 것인지?
  - DICOM 전체에서 통용되는 개념

*Study와 Series의 차이는?*

### UIDs(Unique identifiers)

- `UID = <org root>.<suffix>`
  - `<org root>`
    - 유니크하게 기관을 특정할 수 있는 숫자
  - `<suffix>`
    - `<org root>`의 스코프에서 유니크해야하고, application에 의해서 생성됨
  - 최대 64문자

### DICOM Information Model

IOD / Services / SOP / SCS(Service Class Specification)의 관계

![](./images/network_with_dicom2.svg)

의료 이미지들의 커뮤니케이션에 관계된 정보의 구조와 조직을 정의

- Information Object Definition(IOD)
  - 개요
    - 객체 지향 추상 데이터 모델
      - e.g) Patient, Study, imaging Series, imaging Equipment
    - 오브젝트 사이의 관계를 정의하기 위해서 사용
      - Patient -> Studies(has a)
      - Study -> Series(has a)
    - 실제 IOD 인스턴스들의 커뮤니케이션은 SOP 인스턴스들을 통해서 이루어짐
  - 종류
    - composite
      - 관련 현실 오브젝트"들"의 정보를 포함
        - e.g) CT Image IOD는 Patient, Study, Series, Equipment 등의 오브젝트들을 포함
    - normalised
      - single class of 현실 오브젝트들을 나타냄. 하나의 엔티티를 나타냄
      - e.g) Print Job IOD
    - 위의 둘을 나눈 것은 어느정도 이해가 되는데, 왜 SOP에서도 Composite SOP Classes랑 normalized SOP Classes를 나누었는가?
- SOP(Service-Object-Pair) Classes
  - 구체적인 예시가 궁금함
    - pynetdicom에서는
      - `from pynetdicom.sop_class import PatientRootQueryRetrieveInformationModelFind \ ae.add_supported_context(PatientRootQueryRetrieveInformationModelFind)`
        - 와 같이 SCP나 SCU에서 SOP class를 직접 presentation context의 abstract syntax로 지정
        - ae객체에 presentational context지정
  - 개요
    - Service-Object Pair 클래스는 IOD와 DIMSE(DICOM Message Service Element) 서비스 그룹의 연합으로 정의 됨
      - DIMSE Service Group
        - 하나나 그 이상의 IOD에 적용가능한 operations / notifications을 나타냄(`STORE, GET, ...`)
  - 종류
    - Composite SOP Classes
      - Composite IOD들과 DIMSE-C 서비스 그룹의 결합
      - 종류
        - `C-STORE, C-GET, C-MOVE, C-FIND, C-ECHO`
      - 예시
        - CT Image Storage SOP Class(CT Image IOD + DIMSE C-STORE service(service는 데이터에 대한 오퍼레이션))
          - 하나의 CT Image Storage instance는 한명의 환자 CT스캔의 한조각의 정보를 저장
          - 완전한 스캔(하나의 시리즈)는 하나 또는 그 이상의 CT Image Storage SOP Class 인스턴스들로 구성(Study Instance UID와 Series Instance UID값은 동일하나, SOP Instance UID 값들은 다르다)
    - Normalised SOP Classes
      - Normalised IOD들과 DIMSE-N 서비스 그룹의 결합
      - 종류
        - `N-EVENT-REPORT, N-GET, N-SET, N-ACTION, N-CREATE, N-DELETE`
      - 예시
        - Print Job SOP Class(Print Job IOD + DIMSE N-EVENT-REPORT + N-GET 서비스들)
        - 프린트 job의 추상(하나나 그 이상의 필름이 프린트 되기위한)
  - 모든 DICOM SOP 클래스는 각자의 UID를 갖고 있음
- Service Classes
  - 결론: IOD와 함께 SOP를 구성하기 위한, operation의 집합
    - 하나의 DICOM Service 클래스는 하나나 그 이상의 AE(Application Entity)들이 커뮤니케이션하는 서비스와 관련있는 SOP 클래스들의 그룹을 정의
  - 서비스는 SOP 클래스 인스턴스들의 storage(Storage Service Class), DICOM connectivity의 verification(Verification Service Class), querying and SOP 인스턴스들의 retrieval(Query/Retrieve Service Class), 이미지의 printing(Print Management Service Class)등 다른 operation들을 포함
  - Service Class User / Service Class Provider 는 AE 서비스 클래스 안에 있는 서비스들을 사용하거나 제공하는 것으로 구별됨

### Network with DICOM

![](./images/network_with_dicom1.png)

- Application Entities(AE)
  - DICOM AE는 DICOM 표준, IODs, service classes, dataset encoding/decoding을 지원하는 애플리케이션
  - DICOM 네트워킹에서는 AE들이 `AE Title`로 구별됨
- Presentation Contexts
  - 정의
    - AE들이 서로 서포트하도록 동의하는 서비스들의 집합에, 커뮤니케이션 하기위한 association 교섭을 하는 동안에 사용됨
      - AE사이에 서로 이러이런걸 지원하자 하는 교섭에서 사용
    - 각 Presentation Context는 다음으로 구성
      - Abstract Syntax
      - Transfer Syntaxes
      - *ID value*
        - *이건 뭐지?*
        - DICOM데이터 셋인듯
  - 특징
    - association requestor는 하나의 association당 여러개의 presentation contexts를 제안할 수 있음(최대 128)
    - presentation context구성
      - 1개의 Abstract Syntax
        - 적어도 어떤 데이터로 커뮤니케이션할지는 정해야 하는것은 trivially
      - 1개 이상의 Transfer Syntaxes
    - requestor는 여러개의 contexts를 같은 Abstract Syntax로 제안할 수 있음
    - association acceptor는 각 presentation context에 대해서 동의하거나 거절할 수 있음. 하지만 오직 하나의 Transfer Syntax가 presentation context마다 받아들여질 수 있음
    - acceptor는 받아들인 presentation context에 대해서 하나의 suitable Transfer Syntax를 선택한다
- Abstract Syntax
  - 정의
    - 결론: 어떤 데이터에 대해서 communication할까? (Presentation Contexts - required)
      - e.g) `1.2.840.10008.5.1.4.1.1` - CT Image Storage
    - 데이터 요소들의 집합의 명세이자 그것들의 associated semantics이다.
    - 각각의 Abstract Syntax는 UID형식의 Abstract Syntax Name에 의해서 구별됨
  - 데이터 지정
    - 일반적으로 DICOM과 함께 사용된 Abstract syntax names는 공적으로 지정된 SOP 클래스 UIDs(따라서, Abstract Syntax는 SOP 클래스 그 자체)이나, private abstract syntaxes역시도 사용을 허가함
      - 그래서 pynetdicom에서는...
        - `from pynetdicom.sop_class import PatientRootQueryRetrieveInformationModelFind \ ae.add_supported_context(PatientRootQueryRetrieveInformationModelFind)`
        - 위와 같이 SOP를 abstract context로 지정
- Transfer Syntax
  - 정의
    - 결론: 어떻게 인코딩 된 데이터에 대해서 communication할까? (Presentation Contexts - optional)
      - e.g) `1.2.840.10008.1.2.4.50` - JPEG Baseline
    - 하나나 그 이상의 Abstract Syntaxes에 의해 정의된 데이터 엘리먼트를 나타내는 인코딩 룰의 집합을 정의
    - transfer syntaxes의 negotiation은 서포트할 수 있는 encoding 기술을 AE가 커뮤니케이션 할 수 있도록 허락함(byte ordering / compression등)
- Association
  - 정의
    - peer AE들이 서로 커뮤니케이션 하기 위해 Association을 확립해야 함
  - 절차
    - ① Requestor(association을 시작하는 AE)가 list of proposed presentation contexts와 association negotiation items를 포함하는 `A-ASSOCIATE`메시지를 Acceptor(peer AE)에게 보냄
    - ② The acceptor는 request를 받고 다음과 같이 응답함
      - acceptance
        - association 확립
      - rejection
        - no association
        - 컨텍스트가 지원되지 않거나, Requestor가 자신을 identify하지 않아서 리젝 될 수 있음
      - abort
        - no association
        - *rejection / abort의 차이?*
- Association Negotiation and Extended Negotiation
  - 개요
    - 표준 association negotiation은 일반적으로 presentation contexts에 의해서 제공된 매커니즘을 통한, abstract syntax/transfer syntax 컴비네이션들에 peer AE들이 동의하는 것을 포함
    - 그러나 다른 경우, 그들이 선택적으로 필요로 하거나 서포트하는 서비스들과 기능들에 대한, 보다 자세한 정보를 AE들 사이에서 교환할 필요가 있을 수 있음
    - 그럴 경우에 additional user information items을 association request동안에 보냄으로써 니즈를 달성할 수 있음
      - Asynchronous Operations Window Negotiation
      - SCP/SCU Role Selection Negotiation
      - SOP Class Extended Negotiation
      - SOP Class Common Extended Negotiation
      - User Identity Negotiation
    - 위와 같은 items은 요청된 서비스 클래스에 따라 조건부로 필요함. 위와같은 추가적인 items이 포함된 Association negotiation은 extended negotiation이라고 함

## 2. 실전 예제

### Query retrieve service examples

#### SCP

```py
import os

from pydicom import dcmread
from pydicom.dataset import Dataset

from pynetdicom import AE, evt
from pynetdicom.sop_class import PatientRootQueryRetrieveInformationModelFind

# IOD: PatientRootQueryRetrieveInformationModel
# Service: Find(DIMSE Services)

instances = []

def handle_find(event):
    # event의 identifier가 dataset
    ds = event.identifier

    fdir = '/Users/yeongyumin/Desktop/public/DICOM-prac/lib/python3.7/site-packages/pydicom/data/test_files'

    # instance가 존재하지 않으면 memory에 캐싱
    if len(instances) == 0:
        print("worked")
        for fpath in os.listdir(fdir):
            full_filename = os.path.join(fdir, fpath)

            ext = os.path.splitext(full_filename)[-1]
            # dcm파일 중에 읽을 수 있는 애들만 instances로 mount
            if ext == '.dcm':
                try:
                    instances.append(dcmread(full_filename))
                except:
                    print('exception: ' + full_filename)

    # QueryRetrieveLevel이 지정되어 있지 않으면(쿼리에 어디까지 정보를 제공할 것인지 결정) Failed 반환
    if 'QueryRetrieveLevel' not in ds:
        # Failure
        print('Failed T-T')
        # yield??
        yield 0xC000, None
        return

    if ds.QueryRetrieveLevel == 'PATIENT':
        if 'PatientName' in ds:
            matching = [
                # 애초에 DICOM Dataset에 PatientName이라는 필드가 없을 수도 있음
                inst for inst in instances if 'PatientName' in inst and inst.PatientName == ds.PatientName
            ]

    for instance in matching:
        if event.is_cancelled:
            yield (0xFE00, None)
            return

        identifier = Dataset()
        identifier.PatientName = instance.PatientName
        identifier.QueryRetrieveLevel = ds.QueryRetrieveLevel

        yield (0xFF00, identifier)

handlers = [(evt.EVT_C_FIND, handle_find)]

ae = AE()

# 서포트 가능한 컨텍스트만 등록
ae.add_supported_context(PatientRootQueryRetrieveInformationModelFind)

# request가 왔을 때 핸들링할 핸들러 지정
ae.start_server(('', 11112), evt_handlers=handlers)
```

#### SCU

```py
from pydicom.dataset import Dataset

from pynetdicom import AE
from pynetdicom.sop_class import PatientRootQueryRetrieveInformationModelFind

ae = AE()

# association을 위한 presentaion context에 abstract syntax / transfer syntax 추가
ae.add_requested_context(PatientRootQueryRetrieveInformationModelFind)

ds = Dataset()
ds.PatientName = 'Lestrade^G'
ds.QueryRetrieveLevel = 'PATIENT'

assoc = ae.associate('127.0.0.1', 11112)

# connection이 확립되고 나서 메시지를 주고 받을 수 있음
if assoc.is_established:
    responses = assoc.send_c_find(ds, PatientRootQueryRetrieveInformationModelFind)

    for (status, identifier) in responses:
        if status:
            print('C-FIND query status: 0x{0:04x}'.format(status.Status))

            if status.Status in (0xFF00, 0xFF01):
                print(identifier)
        else:
            print('Connection timed out, was aborted or received invalid response')

else:
    print('Association rejected, aborted or never connected')
```
