# 데이터 포맷

- General
  - 호환성
    - 하위 호환성
    - 상위 호환성
  - Protocol buffer

## General

### 호환성

- 하위 호환성
  - 새 제품이 별도의 수정없이 상대 이전버전에서 그대로 쓰일 수 있는것
    - 내가 새 버전이 되어도, 다른쪽이 수정없이 그대로 쓰일 수 있는것
- 상위 호환성
  - 나의 이전 제품이 상대 새 버전에서 그대로 쓰일 수 있는것
    - 내가 그대로여도, 다른쪽이 새 버전이 될 때도 그대로 쓰일 수 있는것

### Protocol buffer

Protocol buffer workflow

![](./images/data_format/protocol_buffer_concept1.png)

- 개요
  - 언어, 플랫폼 중립적, 구조화된 데이터 직렬화 가능한 데이터 포맷
- 특징
  - JSON보다 작고, 빠르고, 네이티브 언어 바인딩 제공
  - 프로토콜버퍼 컴파일러가 존재해서, 프로그래밍 언어에 맞춘 코드 생성
    - 파서, 빌더, 인터페이스 등
  - forward compatibility, backward compatibility를 고려한 설계
- 장점
  - structured, record-like, typed, language-neutral, platform-neutral, extensible
  - 커뮤니케이션 프로토콜에 사용(e.g gRPC)
  - 데이터 스토리지에서 사용
- 다른 솔루션이 더 나을경우
  - 프로토콜 버퍼는, 전체 메시지를 한번에 메모리로 로드될 수 있음
    - 몇 메가바이트를 초과하는 데이터는 다른 솔루션을 고려하는게 나을 수 있음
    - 직렬화된 복사본이 여러개 생성되어, 메모리 사용 스파이크를 칠 수 있음
  - 프로토콜 버퍼가 직렬화될 경우, 같은 데이터여도 서로 다른 바이너리 직렬화결과가 나올 수 있음
    - 완전히 파싱하지 않고서는 두 메시지를 비교 불가
      - 프로토콜 버퍼의 데이터 직렬화 방식을 보면 이유를 암
  - 메시지는 압축되지 않음
    - 물론 zip, gzip과 같은 압축을 사용할 순 있지만, 특수 목적 압축 알고리즘(JPEG, PNG)이 적절한 데이터 포맷이 있음
  - 비 객체지향 언어에서는 잘 서포팅되지 않음
  - `.proto`파일을 보지 않으면, 프로토콜 버퍼 메시지의 완전한 해석이 어려움
    - 메시지 자체가 self-descriptive하지 않음
- 정의 문법
  - 필드 속성
    - optional, repeated, *singular*
  - 데이터 타입
    - message, enum, oneof, map
    - scalar value types
      - string, int32, ...
    - Any
      - `.proto`정의가 없이도 메시지를 임베딩 가능
  - 필드 번호
    - 재사용하거나, 변경하면 안됨
      - 하위호환성
        - 새 버전에서 이전 버전에서 사용하던 필드 번호를 그대로 사용해버리면, 이전 버전에서 데이터 deserialization을 잘못할 여지 존재
- default values
  - strings
    - empty string
  - bytes
    - empty bytes
  - bools
    - false
  - numeric types
    - zero
  - enums
    - first defined enum value
      - 0
  - repeated fields
    - empty list
  - message fields
    - 언어에 따라 다름
  - 주의
    - scalar message field가 default로 설정되면, 직렬화되지 않음
- Packages
  - 이름 충돌을 막기 위함

Best practices

```protobuf
// reserve를 이용한 필드 번호 재사용 방지로 하위호환성제공
message Foo {
  reserved 2, 15, 9 to 11;
  reserved "foo", "bar"; // JSON serialization의 경우 필드재사용 막음
}
```

- 메시지 타입의 업데이트 방법(하위호환성 유지)
  - 필드 넘버를 업데이트 하지말라(필드넘버는 영구할당)
  - 필드 추가하는 경우
    - old message format을 새 코드가 파싱할 경우
      - 존재하지 않는 필드는 default값이 세팅됨
    - new message format을 옛 코드가 파싱할 경우
      - unknown 필드로 간주되고, 3.5버전 이상에서는 유지되고, 출력에 포함되나 그 미만버전에서는 무시됨
        - `JsonFormat.parser().ignoringUnknownFields()!!`이런식으로 unknownfield를 이그노어 할 수 있음
  - 필드를 삭제하는 경우
    - 삭제해도 되는데, 필드 넘버는 재사용하면 안됨
      - 하지만 JSON으로 serialization하는 경우, 그냥 삭제할 수 없음

RPC 예시

```protobuf
service SearchService {
  rpc Search(SearchRequest) returns (SearchResponse);
}
```

- GRPC
  - 개요
    - 특별한 protocol buffer 컴파일러 플러그인을 사용해서 관련된 RPC 코드를 생성가능
- JSON
  - 개요
    - canonical json encoding도 가능
  - 특징
    - JSON에서 파싱할 경우, JSON에서 값이 missing이거나 null일 때, default 값으로 protocol buffer에 파싱됨
    - protocol buffer에 한 필드가 default값을 가지면, JSON-encoded 데이터는 그 데이터를 생략함(저장 공간 최적화)
      - 이는 설정으로 default value를 그대로 돌려주도록 설정 가능
      - 이렇기 때문에, protobuf를 canonical json으로 serialize하는 경우는 deserialize하는 곳에서도 반드시 protobuf를 사용해야함
        - 그래야 default value를 가져올 수 있으니
  - 옵션
    - default 값도 출력하기
      - 기본 설정은 default값은 출력하지 않음
    - unknown 필드는 무시하기
      - 기본 설정은 파서가 unknown필드는 *reject(에러인가?)*하는데, 무시하도록 설정 가능
    - proto field이름을 lower 케멀 케이스 대신에 사용하기
      - 기본 설정은 lower 케멀 케이스로 변환해서 필드로 사용
    - 문자열 대신 정수를 enum의 값으로 하기
- 자주 사용되는 proto 옵션
  - 파일 레벨
    - `java_package`
      - 컴파일러가 생성한 Java/Kotlin 클래스에 패키지 이름을 설정함
    - `java_outer_classname`
      - 컴파일러가 생성한 파일의 클래스와 파일 이름을 변경
    - `java_multiple_files`
      - false면, 프로토 파일에 대응하는 오직하나의 java 파일이 생성되고, 모든 top-level messsage, service, enumeration들이 바깥 클래스 속으로 네스팅됨
  - 메시지 레벨
    - `deprecated`
- Protocol buffer java
  - 특징
    - 메시지 빌더는 immutable
      - `setter()`의 반환값은 같은 빌더
    - reflection 기능 존재
