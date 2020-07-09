# Ch2. Data Models and Query Languages

- 의문
- Data model 개요
- Relational Model vs Document Model

## 의문

## Data model 개요

- 데이터 모델이 소프트웨어 개발에 가장 중요한 요소중 하나
  - 작성되는 소프트웨어의 관점에서 중요할 뿐 아니라
  - 문제 해결의 생각적 기반이 됨
- 대부분의 애플리케이션은 데이터모델의 추상화 계층으로 구현됨
  - 핵심
    - **각 레이어는 깔끔한 데이터 모델을 제공하므로써, 아래 레이어의 복잡도를 감춤**
  - 1 application level
    - 실 세상을 object, data structure, data structure를 다루는 api로 환원
  - 2 data structure level
    - 데이터 스트럭처를 JSON, XML document나 RDB의 table이나 graph model로 환원
  - 3 db engine level
    - JSON/XML/RDB/Graph 데이터를 메모리나 디스크나 네트워크상의 바이트로 환원
  - 4 hardware level
    - 바이트를 전자 전류, 빛의 pulse, 자기장 등으로 나타내도록 환원

## Relational Model vs Document Model

### Relational model

- 개요
  - 데이터는 relations으로 구성되고, 각 relation은 소팅되지 않은 tuple의 collection으로 구성됨
- 역사
  - 1960, 1970
    - Business Data Processing으로부터 시작
    - Transaction processing, Batch processing을 처리하기 위함
    - RDB이외의 데이터베이스는 개발자가 데이터베이스 속에 있는 데이터의 내부 표현까지 생각했어야 했음
    - **RDB의 목적은 깔끔한 interface 뒤로 구현을 숨기는 것이었음**
  - 2000년대 까지도 계속해서 dominant

### The Birth of NoSQL

- 배경
  - RDB보다 매우 높은 scalability를 갖고, 매우 높은 write throughput을 갖는 데이터 베이스의 필요성
  - 상업 DB 제품 보다 오픈소스에 대한 선호의 확산
  - 관계 모델에 의해서 잘 서포트되지 않는 특별한 쿼리의 지원 필요성
  - 관계 스키마의 제약에 대한 실망과, 보다 다이나믹하고 표현적인 데이터 모델의 필요성

### Object-Relational Mismatch

resume의 JSON document 표현

![](./images/ch2/representing_linkedin_profile_as_a_json_document1.png)

resume의 Tree 구조 표현

![](./images/ch2/one_to_many_relation_tree_structure1.png)

- 대부분의 애플리케이션의 개발이 object-oriented하게 되지만, SQL data model의 경우에는 관계형 테이블에 데이터가 저장되면, translation layer가 필요해짐
  - e.g) ORM(ActiveRecord, Hibernate)
  - 하지만 ORM도 Object-oriented model과 SQL data model 사이를 완전히 매우지는 못함
- 관계형 데이터베이스에서 1:다 관계를 다루는 방법(이력서의 예시)
  - positions, education, contact information을 전부 다 다른 테이블로 두고, foreign key 참조로 이어줌(JOIN사용)
  - XML, JSON 데이터 타입의 데이터를 하나의 행에 저장 가능
  - jobs, eductaion, contact info를 JSON이나 XML document로 encode하고, application이 structure와 content를 해석하도록 함
    - DB가 encoded column에 대해서 query하는것이 불가능해짐
- 1:다 관계는 Tree구조를 암시함
  - JSON으로 잘 나타낼 수 있음

### Many-to-one and Many-to-Many Relationships

- ID 사용의 이점
  - 사람에게 전혀 ID의 의미가 없기 떄문에, 변화할 필요가 없다는 점
  - ID가 나타내는 정보가 변화하여도 결국 ID는 계속 같은 채로 유지
    - 사람에게 의미가 있는 데이터의 경우, 미래에 변화한다면 전부다 바꿔야 하는 오버헤드 발생
  - normalization
    - duplication의 제거
