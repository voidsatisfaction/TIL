# Perl 기초문법과 상념

개인적으로 Hatena라는 회사에서 Perl이라는 언어를 사용하게 되었다. 대학원생 아르바이트로서 1년동안의 장기 계약으로 프로젝트에 참여하게 됐는데, Hatena Bookmark라는 서비스가 Perl과 Scala로 되어있었다. 개인적으로 Scala에 흥미가 많던 나는, 되도록이면 Scala쪽 일을 하길 희망했으나(정말 간절하게) 현 상황에서 가장 필요한 일들은 Perl쪽에 많다고 하니 어쩔 수 없이 Perl을 배우게 되었다. 사실 썩 기분이 좋지는 않았다.

이대로 공부하면 의욕이 떨어질 것 같아 가장 먼저 *왜 내가 Perl을 배워야 하고 배운다면 어떤 것이 좋은지* 를 가볍게 살피고자 한다.

그렇지 않으면 나의 멘탈이 많이 흔들릴 것 같기 때문이다. 그래도 개인적으로 Hatena는 "일본 관서의 웹 회사라면 Hatena"라고 할 정도로 정말 기술력으로는 유명한 기업이기 때문에 비단 언어 뿐 아니라, 인프라나 설계능력 아름다운 코드를 쓰는 능력을 차근차근 배워나갈 생각을 하면 이정도 고난(?)은 아무것도 아닌 듯 하다. 결국 내 마음먹기 달린거겠지.

내가 좋아하는 고든램지 역시 처음 요리를 시작할때 "어떠한 식재료를 보고 겁 먹지 않을 정도의 실력"을 목표로 삼았던 것 처럼, 나 역시 Perl이라는 이름에 겁먹지 않고 아래와 같이 내가 평소에 생각했던대로 묵묵히 새로운 세계를 걸어나가려 한다.

> 프로그래밍 언어는 결국 문제 해결을 위한 도구이다.

p.s 참고로 이 글을 쓰고 있는 지금은 2017년 12월 25일. 크리스마스 입사라 Hatena는 나에게 절대 잊을 수 없는 회사가 될 것 같다.

## 5일정도 사용해보고 난 후기

- 생각보다 재미있다!!! 진짜 재미는 있다.

## 철학

Perl: Practical Extraction and Report Language

TIMTOWTDI(There Is More Than One Way To Do It)

## Perl의 장점

Perl is Humble Language.

- 어떠한 운영체제에서도 사용 가능(Portability)
- 프로토타이핑(Prototyping)
- 인터프리팅 언어이면서도 안정적(Interpreting language)
  - Perl은 먼저 바이트코드로 완벽하게 번역하므로, 재앙에 맞닥드리지 않을 가능성이 크다.
- 완전성(Complete)
  - awk의 정규식, sed의 치환 편집, C와 유사한 구조, sh의 단순함.
- 효율적(Efficiency)
  - 사용하기 쉬으므로 생선적인 언어이다.
- C언어에 삽입할 수 있고, C언어를 이용해서 확장할 수 있다(Embeddable, Expandable)
- TCP/IP 네트웍 처리 가능
- 내장 디버거 기능
- CPAN에는 웬만한 것이 다 있다.
- 텍스트 데이터를 다루는 데에 환상적이다.
- 배우기 힘들지만 사용하기 쉽다.

## 기본 정리

### 기본 데이터 타입

- Scalar(스칼라)
  - 하나의 값, 문자열/숫자/레퍼런스, `$calar`
- Array(배열)
  - `@rray`
  - 값을 얻을 때는 `$array[1]`이런 식으로(스칼라가 된다)
- Hash(해시)
  - `%ash`

### Cpan vs Cpanm vs Carton

- CPAN(The Comprehensive Perl Archive Network)
  - 루비의 rubygems.org와 같은 것
  - 모듈을 찾거나 도큐멘트나 소스코드를 읽을 수 있다.
  - [meta::cpan](https://metacpan.org/)이 사이트에서 보는 것을 추천
- cpanm(cpanminus)
  - 루비의 gem커맨드와 같은 것
  - CPAN으로부터 모듈을 취득하여 인스톨을 할 수 있는 툴
- Carton
  - 루비의 Bundler와 같은 것
  - CPAN모듈의 의존성을 해결해주는 툴
  - cpanfile(Gemfile과 같은 것)에 쓰여진 모듈을 의존성을 고려하면서 인스톨 해준다.

## 팁(하테나 연수 피드백)

### 서브 루틴에서 배열이나 해시를 돌려주는 경우

Perl에서 배열이나 해시를 서브루틴에서 돌려줄때는 레퍼런스로 돌려준다. 안그러면 shallow copy가 일어나기 때문에, 살짝 오버헤드가 발생한다.

### 해시에 지정된 키가 없는 경우 에러 핸들링

- `croak`을 사용한 방법
- `undef`를 반환하게 한 다음, 알아서 핸들링 하기

croak의 경우 에러 핸들링은 `Test::Exception`에서 `throws_ok`나 `dies_ok`를 이용해서 한다.

### 클래스 내의 accesor에 관한 팁

- MySQL에서의 DateTime은 문자열
- 펄에서는 이를 DateTime인스턴스로 변환하고 싶어함(더 유연한 처리를 위해)
- 근데 단순히 `Class::Accessor::Lite`를 사용해서 `created`를 정의하면 그냥 문자열만 돌아옴
- 그래서 따로 `created`라는 인스턴스 메소드를 정의. 아래를 참고:

```perl
my $user = Intern::しおり::Model::User->new(user_id => 'xxx', name => 'test', created => '2018-01-11 11:08:00');
$user->created; #=> DateTime의 인스턴스가 되길 원함!
```

- 또한 Perl은 패키지 안에 같은 이름의 메소드를 정의할 수 없으므로 다음과 같이 하면 에러가 난다.

```perl
package Intern::しおり::Model::User;

use Class::Accessor::Lite (
    ro  => [ qw(user_id name created) ],
    new => 1,
);

sub created {
  # ...
}

1;
```

- 덧붙여 설명하자면 아래와 같은 코드 작성은 메모화를 위한 관습이다.
  - 샘플 코드는 `||=` 이나, 과거 버전(5.10미만)에서는 [Defined-or-operator](https://perldoc.perl.org/perlop.html#Logical-Defined-Or) 를 사용할 수 없었으므로, undef의 경우만 값을 넣고 싶으면 `//`를 써야한다.

```perl
$self->{_created} //= # 何か処理
```

### DDP: 오브젝트 내부를 시원하게 간결하게 봐 보자

DDP: Data::Dumper보다 더 오브젝트 데이터를 쉽게 볼 수 있는 방법

```perl
use DDP;
p $abc; # utf8 + CodeRef + 보기편한 형식
```

### 리스트에 관한 유용한 메서드

- 참고: http://d.hatena.ne.jp/minesouta/20070914/p1
- `use List::Util qw(first, max, min, maxstr, minstr, shuffle, reduce)`
