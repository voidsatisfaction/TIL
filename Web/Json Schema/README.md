# JSON 스키마기초

## 참고

- [JSON-Schema - mcchae](https://github.com/mcchae/JSON-Schema/blob/master/JSON-Schema.md)

## JSON 스키마란?

애초에 JSON(JavaScript Object Notation)이란, Javascript를 이용한 경량의 데이터 교환 형식이다.

자료형은 다음과 같은 것들이 존재한다.

- object
- number
- string
- boolean
- null

```js
// 다음은 예제 JSON데이터 이다.

{
  "name": "George Washington",
  "birthday": "February 22, 1732",
  "address": "Mount Vernon, Virginia, United States"
}

{
  "first_name": "George",
  "last_name": "Washington",
  "birthday": "1732-02-22",
  "address": {
    "street_address": "3200 Mount Vernon Memorial Highway",
    "city": "Mount Vernon",
    "state": "Virginia",
    "country": "United States"
  }
}
```

JSON schema는 XML스키마와 유사하게 JSON 으로 표현된 JSON 객체의 검증을 하기 위한 표현 방법이다.

### JSON 스키마가 비어있을 경우

```js
{} // 모든 자료형이 검증에 성공
```

### JSON 스키마 선언

```js
{ "$schema": "http://json-schema.org/schema#" } // 단순 JSON 데이터인가, 스키마인가 확인

{ "id": "http://yourdomain.com/schemas/myschema.json" } // id를 스키마에 고유하게 지정 가능. 각각은 공유 URL을 지정.
```

### type 키워드

- string
- number
- object
- array
- boolean
- null

이상의 여섯가지 자료형이 존재한다.

```js
{ "type": "string" }
// "I'm a string" => o
// 42 => x

{ "type": ["number", "string"] }
// 42 "Life, the universe, and everything" => o
// ["hi", "heelo"] => x
```

### string

```js
{
  "type": "string"
  "minLength": 2,
  "maxLength": 3
}
// "AB" => o
// "ABC" => o
// "A" => x
// "ABCD" => x

{
  "type": "string",
  "pattern": "^(\\([0-9]{3}\\))?[0-9]{3}-[0-9]{4}$"
}
// "555-1212" => o
// "(888)555-1212" => o
// "(888)555-1212 ext. 532" => x
// "(800)FLOWERS" => x

// format을 사용하면 시각, 이메일등과 같이 일반적으로 사용되는 문자열 검증도 할 수 있다.
// 실제로는 이 부분이 완전하게 구현되지 않은듯하다.
```

### number / integer

```js
{ "type": "integer" }
// 42 => o
// -1 => o
// 3.14 => x
// "42" => x

{ "type": "number" }
// 42 => o
// -1 => o
// 3.14 => o
// "42" => x

{
  "type": "number",
  "multipleOf": 10
}
// 0 => o
// 10 => o
// 23 => x

{
  "type": "number",
  "minimum": 0,
  "maximum": 100,
  "exclusiveMaximum": true
}
// -1 => x
// 0 => o
// 10 => o
// 99 => o
// 100 => x

```

### object

```js
{ "type": "object" }
```
