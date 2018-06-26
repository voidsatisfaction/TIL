# 컨트롤러의 구현

목차

- 웹
  - 웹 컴포넌트
  - 라우팅 정의
    - 경로변수
    - 리소스
    - 라우팅
    - 경로의 명명 규칙
  - 리퀘스트 핸들러
  - 로그인 상태의 관리
  - 문서 및 디버그
- CLI

여기까지로 코드상에서는 애플리케이션의 구현을 했습니다만, 아직 실제로 애플리케이션을 움직이기 위한 인터페이스(어댑터)가 없습니다. 어댑터는 인터페이스의 종류마다 준비해야하는 것으로, 웹 애플리케이션에서는 주로 HTTP서버로서 동작하기 위한 것과 CLI가 있습니다. 각각의 어댑터는 입력을 애플리케이션에 맞는 형식으로 변환하여, 애플리케이션으로 부터 반환된 결과를 인터페이스의 출력에 맞는 형태로 변환하는 것에 주력 해야하며, 이 레이어에 로직이 포함되서는 안됩니다.(Clean Architecture참조)

## 웹

웹 인터페이스의 어댑터로서의 역할은 입력을 적절히 변환하여 애플리케이션층에 전달하는 것입니다만, 이 프로젝트에서는 웹 API를 통일적으로 준비하는 등의 궁리가 필요합니다. 특히, API의 정의와 입출력의 검사 방법은 통일된 방법에 맞춰 나가는 것으로, 문서화, 디버그 등의 면에서 은혜를 얻을 수 있습니다.

### 웹 컴포넌트

웹 레이어의 컴포넌트는 `boston.web`이름 공간에 배치하여, Cake패턴으로 `boston.web.Web`에 통합합니다. `boston.web.Web`은 추상 클래스로, 테스트할 때, 로컬 서버, 프로덕션 환경 등 상황에 맞춰서 일부의 모듈을 교체하여 구체화 한 것이 사용됩니다.

```scala
abstract class Web extends WebStack with AppBase
  with Root
  with Static
  with Worker
  with User
  with Bookmark
  ...
  with ApiDocument // 이는 항상 마지막에 배치
```

웹 컴포넌트는 API의 덩어리 마다 별개로 나눕니다. 하나의 컴포넌트가 하나의 API엔드포인트만 갖는 경우도 있으며, 복수를 구현하는 경우도 있습니다. 엔드포인트를 구성하는 단위는 API도큐먼트의 페이지 단위 입니다.

웹 레이어를 구현하기 위해서 필요한 공통 기반은 `boston.web.WebStack`에 제공되어있으므로, 각 컴포넌트는 기본적으로 이 트레잇을 자기 타입 어노테이션(self type annotation)합니다. 물론, 이 이외에도 Cake패턴에 따라서 사용하는 애플리케이션층의 컴포넌트등도 지정합니다. 일부의 보조 트레잇은 `boston.web.Web`에 디폴트로는 믹스인 되지 않으므로, 이용하는 컴포넌트 마다 extends합니다.

- (1) 컴포넌트는 `boston.web.컴포넌트명` 으로 정의
  - 이 이름은 도큐먼트의 파일명 등의 API를 구성한 것의 이름으로서 사용됩니다.
- (2) `WebStack`을 자기타입 어노테이션
- (3) 의존하는 애플리케이션을 자기타입 어노테이션 함
- (4) 보조 컴포넌트는 직접 `extends`

```scala
package boston
package web

trait Bookmark extends VisitorHelper {             // (1), (4)
  self: WebStack                                   // (2)
      with application.BookmarkComponent           // (3)
      with application.BookmarkSearchComponent =>  // (3)

  ...
}
```

### 라우팅 정의

API엔드포인트를 정의하는 데에는, 엔드포인트의 경로 외에, 어떠한 리소스를 받으며 어떠한 리소스를 반환하는가 라는 정보를 작성해둡니다. 이러한 API문서의 자동생성에 사용되는 것 외에도, 특히 리퀘스트에 관해서는 입력 검사에도 이용되므로, 제대로 정의해야 합니다.(출력의 검사는 로컬 서버 및 테스트 환경에서만 실행됩니다)

경로변수의 패턴, 리소스, 검사 규칙 중에서 공통되는 것은 `boston.web.SharedResource`에 정의 합니다. 각 웹 컴포넌트에 특화한 정의는 각 컴포넌트 안에 기술합니다만, 정의 방법은 어느쪽이던 같습니다.

#### 경로 변수

경로 안에 있는 패턴에 일치하는 부분을 리퀘스트 핸들러 안에서 매개변수로서 이용하고 싶은경우, 경로변수를 정의 합니다. 경로 변수는 `Pattern`클래스를 `case object`로 `extends`한 것으로 정의합니다.

```scala
case object Url extends Pattern(".+")
```

다른 경로변수를 포함한 복합적인 경로변수를 정의하는 경우는 `NestedPattern`클래스를 `case object`로 `extends`합니다. 이 떄에, 복합적인 패턴의 작성에는 `path`보간자를 사용합니다. 이것에 의하여, 다른 경로변수를 패턴 문자열안에 삽입하는 것이 가능합니다.

```scala
case object UserId extends ...
case object UserService extends ...
case object User extends NestedPattern(path"(?:$UserService:)?$UserId")
```

경로변수에 지정한 패턴은, 엔드포인트의 구별이 가능하도록 되어있으면 크게 문제는 없습니다. 그러나, 그 경우에는 경로 변수의 검사 규칙을 나중에 작성하는 매개변수의 검사로 정의할 필요가 있습니다.

경로 변수는 매개변수로서 추출하는 경우나 검사의 대상으로서 다루는 경우는 쿼리 매개변수와 같이 취급하도록 되므로, 쿼리 매개변수와 충돌하지 않도록 변수명을 대문자로 시작하도록 합시다.

#### 리소스

리소스는 `Resource.define()`로 정의합니다. 각 리소스는 JSON Schema로 정의합니다. JSON Schema의 설정에 포함된 것이외로, `example`을 지정해 두면, 문서의 코드 예에 기재됩니다.

- (1) resource(name) = ... 기법을 사용하기 위한 `import`
- (2) JSON Schema를 정의하는 DSL을 위한 `import`
- (3) 컴포넌트 안의 리소스의 경우는 `private`로 함
- (4) `object`는 오브젝트 타입의 JSON Schema를 정의 합니다
  - **필드 이름을 sname_case로 한다**
    - JSON은 전부 sname_case로 변환되기 때문
    - 리소스의 검사는 JSON이 된 상태에서 처리 되므로
- (5) 설명이나 예시를 작성
- (6) 예는 실제로 이 리소스를 반환할 떄의 오브젝트를 `toJsonNode`로 serialize하면 좋다
- (7) JSON Schema의 일부를 다른 리소스 내용으로 하는 경우는 `ref("#/resource/리소스이름")`으로 지정함
- (8) 모든 필드를 필수로 함
  - 타입마다 옵션을 지정 가능
  - 지정 가능한 옵션은 IDE의 보완 등으로 확인하면 좋음
- (9) 복수의 리소스도 같게

#### 라우팅

API의 엔드포인트는 `defineWith(resources) {}`블록 안에 HTTP메서드명에 의한 경로 보간자를 호출하는 것으로 정의를 작성하여, `this.defineAPIs()`를 호출하는 것으로 정의를 등록합니다. `defineWith()`에 지정하는 리소스는 컴포넌트 안에서 정의한 리소스에서, `SharedResource`의 것은 자동적으로 포함하므로 지정할 필요는 없습니다.

- (1) `defineWith()`에서 만든 정의는 등록만 할 수 있으면 좋으므로 `private`
- (2) 이 장소에서 JSON Schema를 작성하는 경우나 `ref()`로 리소스를 지정하는 경우를 위하여 `import`
- (3) `메서드"/api/경로" as (옵션) from/to 요청 핸들러`의 형태로 정의
  - 경로는 경로 변수를 그대로 넣을 수 있음
  - 문서에 표시되기 때문에 타이틀이나 검사 규칙을 옵션으로 지정
  - `GET`이나 `DELETE`는 `from`으로, `PUT/POST`는 `to`로 리퀘스트 핸들러를 지정
- (4) 리퀘스트의 검사 규칙을 검사 대상 마다 지정
  - `headers`: 헤더(옵션 타입)
  - `parameters`: 경로 매개변수와 쿼리 매개변수(오브젝트 타입)
  - `body`: 리퀘스트 바디
- (5) 리스폰스의 검사 규칙을 리스폰스 스테이터스와 대성 마다 지정
  - `headers`: 헤더(오브젝트 타입)
  - `body`: 리퀘스트 바디
- (6) `this.defineAPIs()`로 API정의를 등록
  - `this.`붙여서 호출(정의한 곳의 컴포넌트의 추적용으로 확장 메서드화 되어있기 때문에 필요)
  - 이 메서드의 호출 마다 API문서의 페이지가 작성됨

```scala
private val routes = defineWith(resources) {              // (1)
  import Schema.DSL._                                     // (2)

  GET"/user/$User/bookmarks/?" as (                       // (3)
    title = "GET bookmark list of a user",
    request = Request(                                    // (4)
      parameters = ref("#/resources/limit_offset")
    ),
    response = Response.Map(                              // (5)
      Status.OK -> Response(body = bookmarkList),
      Status.BadRequest -> Response(body = ref("#/resources/error"))
    )
  ) from getBookmarkList                                  // (3)

  ...

  PUT"/user/my/bookmark/$Url" as (                        // (3)
    title = "PUT bookmark item",
    request = Request(                                    // (4)
      headers = ref("#/resources/header_operator_id"),
      body = ref("#/resources/bookmark_content")
    ),
    response = Response.Map(                              // (5)
      Status.OK -> Response(body = ref("#/resources/bookmark_item")),
      Status.BadRequest -> Response(body = ref("#/resources/error")),
      Status.Forbidden -> Response(body = ref("#/resources/error"))
    )
  ) to putBookmarkItem                                    // (3)

  ...
}

this.defineAPIs(routes)                                   // (6)
}
```

#### 경로의 명명규칙

이 프로젝트에서는 엔드포인트의 경로는 원칙으로 `/접두사[/변수]`및 그것을 반복한 것으로 합니다. 접두사는 그 경로에서 표현한 리소스의 종류로, 리소스가 단수이면 단수형, 복수이면 복수형으로 나타냅니다(github api방식). 경로가 `/접두사[/변수]`의 반복의 경우, 이 규칙은 최후의 접두사에 적용됩니다.

`/접두사[/변수]`의 반복은, 리소스에 친자관계(소유관계)가 있는 경우에 상위의 것으로 묶은 것 중에서 하위의 것을 특정하는 경우 사용합니다. 전형적인 예로서는, `/user/유저ID`의 다음으로 하위 리소스를 표현하는 경로를 계속하는 것으로 유저에 연결된 정보를 나타내는 경우가 그 예입니다.

접두사가 두 단어 이상의 어구인 경우는
