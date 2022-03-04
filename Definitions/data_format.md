# 데이터 포맷

- General

## General

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
  - 필드 이름을 바꾸는 경우
    -
