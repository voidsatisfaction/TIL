# Perl에 의한 Web애플리케이션 개발

## Hatena::Newbie

WAF의 실제 예시를 통해서 실제 웹 개발의 분위기를 알아보자

## 전제

- CPAN에는 WAF의 일부를 만들어 놓은 모듈이 많이 존재
  - 그것을 조합해서 사용하면 됨
  - 최근 하테나에서는 공통 WAF를 사용하지 않음
    - 프로젝트(상황) 에 따라서 다른 모듈을 조합함
- 'MVC패턴'이나 '웹 애플리케이션의 '중요한 부분'을 연수용 WAF인 Hatena::Newbie에서 배움

## 목차

- Hatena::Newbie란
- Intern::Bookmark란
- 북 마크 일람을 만들어보자
  - URI설계
  - Controller의 작성
  - View의 작성
  - Test의 작성
- 다른 기능도 만들어보자
- URI를 변경해보자

## Hatena::Newbie란

- 하테나 연수용 WAF
  - 연수용에는 어려운 부분을 되도록 없애, 간단히 읽을 수 있는 프레임워크로 작성
- perl-Intern-Bookmark와 perl-Intern-Diary는 이 프레임워크에 기초
- 하테나WAF의 역사
  - Hatena -> Hatena2 -> Ridge -> 특별히 정해진 프레임워크 없음

## Intern::Bookmark란

하테나 연수용 WAF의 Hatena::Newbie를 이용하여 작성한 Web애플리케이션의 예

### 디렉터리 구성

프레임워크 등도 전부 디렉터리에 들어있으므로 다소 많아보이나, 이하와 같은 구성으로 되어있음

```
$ tree perl-Intern-Bookmark/
perl-Intern-Bookmark/
├── cpanfile
├── db # DB設定ファイル
│   └── schema.sql
├── lib # Perlモジュール
│   └── Intern
│       ├── Bookmark
│       │   ├── Config
│       │   │   ├── Route
│       │   │   │   └── Declare.pm
│       │   │   └── Route.pm
│       │   ├── Config.pm
│       │   ├── Context.pm
│       │   ├── Engine
│       │   │   ├── API.pm
│       │   │   ├── Bookmark.pm
│       │   │   └── Index.pm
│       │   ├── Model
│       │   │   ├── Bookmark.pm
│       │   │   ├── Entry.pm
│       │   │   └── User.pm
│       │   ├── Request.pm
│       │   ├── Service
│       │   │   ├── Bookmark.pm
│       │   │   ├── Entry.pm
│       │   │   └── User.pm
│       │   ├── Util.pm
│       │   └── View
│       │       └── Xslate.pm
│       └── Bookmark.pm
├── README.md
├── script # 様々なスクリプトファイル
│   ├── app.psgi
│   ├── appup
│   ├── appup.pl
│   └── setup_db.sh
├── static # 静的ファイル(画像, css, js)
│   └── css
│       └── style.css
├── t # テスト置き場
│   ├── engine
│   │   ├── api.t
│   │   ├── bookmark.t
│   │   └── index.t
│   ├── lib
│   │   └── Test
│   │       └── Intern
│   │           ├── Bookmark
│   │           │   ├── Factory.pm
│   │           │   └── Mechanize.pm
│   │           └── Bookmark.pm
│   ├── model
│   │   ├── bookmark.t
│   │   ├── entry.t
│   │   └── user.t
│   ├── object
│   │   ├── config.t
│   │   ├── dbi-factory.t
│   │   └── util.t
│   └── service
│       ├── bookmark.t
│       ├── entry.t
│       └── user.t
└── templates # テンプレート(View)置き場
    ├── bookmark
    │   ├── add.html
    │   └── delete.html
    ├── bookmark.html
    ├── index.html
    └── _wrapper.tt
```

웹 애플리케이션으로서 중요하겨 여겨지는 `lib`내부의 구성요소는 다음과 같음:

- `lib/Intern/Bookmark.pm`
  - 컨트롤러의 중심을 만드는 dispatcher
- `lib/Intern/Bookmark/Config.pm`
  - 애플리케이션의 설정은 여기서
- `lib/Intern/Bookmark/Config/Route.pm`
  - 애플리케이션의 URI설정은 여기서
- `lib/Intern/Bookmark/Context.pm`
  - 애플리케이션의 컨텍스트 클래스
  - 요청, 응답, 라우팅등의 정보를 갖음
  - 1리퀘스트 마다 작성되어, 처리가 끝나면 파기됨
- `lib/Intern/Bookmark/Engine/Index.pm`
  - 컨트롤러
  - 안에 실제 처리를 작성
- `templates/index.html`
  - 뷰
  - HTML이나 템플릿 등을 사용해서 작성

#### 테스트 서버의 시작

```
$ script/appup
11:13:18 app.1      | Watching lib script/lib script/app.psgi for file updates.
11:13:19 app.1      | HTTP::Server::PSGI: Accepting connections at http://0:3000
# http://localhost:3000/ でアクセスできる
```

## 북 마크 일람을 만들어보자

### URI설계

만들기 전에 URI를 설계한다.

#### 북마크 애플리케이션의 요건

- 일람
- 표시
- 작성
- 삭제

이에 대응하는 URI는 다음과 같이 설계 가능:

### 컨트롤러를 쓰자

다음과 같은 URI설계에 있어서의 북마크 일람(`/`)을 예로하여, 컨트롤러를 작성해봅니다.

**일단은 Hello World부터**

일단은 URI와 컨트롤러의 묶음을 행합니다. `lib/Intern/Bookmark/Config/Route.pm`이 묶음의 역할을 담당하므로, 다음과 같이 작성합니다. 이것에 의하여 `/`에 액세스하면, `Intern::Bookmark::Engine::Index`의 `default`메서드에 처리가 가도록 됩니다.

```perl
# lib/Intern/Bookmark/Config/Route.pm

sub make_router {
    return router {
        connect '/' => {
            engine => 'Index',
            action => 'default',
        };
    };
}
```

다음으로 컨트롤러를 만듭니다. 앞서 지정한 컨트롤러에 처리를 작성합니다.

```perl
# lib/Intern/Bookmark/Engine/Index.pm

package Intern::Bookmark::Engine::Index;
use strict;
use warnings;

sub default {
  my ($class, $c) = @_;

  $c->res->content_type('text/plain');
  $c->res->content('Welcome to the Hatena world!');
}

1;
```

- `$class`: 컨트롤러의 클래스(`Intern::Bookmark::Engine::Index`)
- `$c`: 컨텍스트 오브젝트(`Intern::Bookmark::Context`의 인스턴스)
- `$c->res->content`로 출력내용을 직접 설정

**북마크 일람의 컨트롤러를 작성**

- `bookmark.pl`의 `list_bookmarks()`에 대응
- 컨트롤러가 해야 할 것들
  - 유저 북마크 일람을 취득
  - 취득한 북마크 일람을 출력(뷰에 넘김)

```perl
# lib/Intern/Bookmark/Engine/Index.pm

sub default {
  my ($class, $c) = @_;

  # 일단 유저는 tarao를 갖고옴
  my $user = Intern::Bookmark::Service::User->find_user_by_name($c->dbh, {
    name => 'tarao',
  })

  # 북마크의 일람을 취득
  my $bookmarks = Intern::Bookmark::Service::Bookmark->find_
}
```
