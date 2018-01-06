# Scalar

스칼라는 펄(Perl)에서 가장 간단한 데이터 타입이다.

Perl의 스칼라는 `Number`, `String`으로 나뉜다.

## Numbers

모든 숫자형은 부동소수점 형식이다.

### 숫자 리터럴

```perl
# 부동소수점
1.25
7.25e45
-12e-24

# 정수
0
-40
123123
61298040283768
61_298_040_283_768

# 10진수가 아닌 수의 리터럴
0377 # 십진수의 255와 같고, 출력도 255로 됨
0xff # 십진수의 255와 같고, 출력도 255로 됨
0b11111111 # 255
```

### 숫자 연산자

```perl
10.2 / 0.3 # 34
10 / 3 # 3.33333..
10 % 3 # 1
10.5 % 3.2 # 1
2**3 # 8
```

## Strings

문자열은 문자(character)의 연속이다. 메모리를 초과할때 까지 문자열의 크기를 늘릴 수 있다. 문자열은 어떠한 문자의 합성으로도 생성 가능. 그러므로 바이트 데이터도 펄의 문자열로 읽어들여서 조작할 수 있다.

### 홑따옴표 문자열 리터럴

''는 문자열의 시작과 끝을 알린다.

홑따옴표 안의 \\는\\와'를 제외하면 전부 그냥 그대료 표시된다.

```perl
'hello\n' # hello\n으로 보임
'hello\\' # hello\로 보임
'hello\'' # hello'로 보임
```

### 겹따옴표 문자열 리터럴

- 겹따옴표 안의 \\는 문자를 이스케이프 할 수 있다.
- 겹따옴표 안의 변수는 그 값으로 치환된다.

### String Operators: 문자열 연산자

- 다음의 연산자들은 불변의(immutable)성질을 갖고 있다.
- 컨텍스트(context)개념에 유의.

```perl
"hello" . "world" # helloworld
"fred" x 3 # fredfredfred
5 x 4.8 # 5555, context의 개념
```

## C.f warnings, diagnotics

- warnings: 스크립트 파일에서의 주의사항(문법적 오류등)을 실행했을 때 나타내줌
- diagnostics: 위의 주의사항을 보다 자세하게 나타내줌

## Scalar Variables: 스칼라 변수

- `$(sigil) + perl identifier`로 구성되어 있음
- 무려 utf8의 변수 선언도 가능.
- `$`는 하나의 아이템 또는 스칼라 라는 의미를 갖는다.

```perl
use utf8;
$name
$Name
my $이랑 = "abc";
my $おはよう = "거대해달젤리";
print $이랑 . "\n"; # abc
print $おはよう . "\n"; # 거대해달젤리
```

```
$fred = 17;
$barney = 'hello';
$barney = $fred + 3;
$barney = $barney * 2;
```

## Binary Assignment Operators

- 기존의 값을 치환하는(mutable) 연산이다.

```perl
$fred += 5;
$barney *= 3;

$str = "hi";
$str .= " ";
```

### Interpolation of Scalar Variables into Strings

```perl
$what = "brontosaurus steak";
$n = 3;
print "fred ate $n $whats.\n"; # $whats라는 변수가 없으므로 에러
print "fred ate $n ${what}s.\n"; # $what이라는 변수와 s가 분리
```

## Code Point를 이용한 문자 생성

```perl
my $alef = chr(0x05D0);
my $alpha = chr(hex('03B1'));
my $omega = chr(0x03C9);

print "$alef $alpha $omega\n"; # א α ω

my $code_point = ord($alef);

print $code_point, "\n"; # 1488

print "\x{03B1} \x{03C9}" # α ω
```

## 비교 연산자

| 비교 | 숫자 | 문자 |
|-----|-----|-----|
| Equal | ==  | eq  |
| Not equal | != | ne  |
| Less than  | < | lt |
| Greater than  | > | gt |
| Less than or equal to | <= | le |
| Greater than or equal to  | >= | ge |

```perl
35 eq '35', "\n"; # true
' ' gt ''; # true
```

## Boolean Values

- 어떠한 스칼라 값도 조건문에서 사용할 수 있다.
- 펄은 Boolean이라는 데이터 타입이 없다.
  - 값이 숫자일 때: 0은 false, 다른 숫자는 true
  - 값이 문자열일 때: 빈 문자열 ''은 false, 다른 경우는 true ('0'은 false, 구분을 못하므로)
  - 값이 숫자나 문자열이 아닌 다른 형태의 스칼라일 때:
    - 이를 숫자나 문자열로 변환하고 다시 시행한다.
    - 즉, `undef`는 false이고 다른 모든 `참조(references)`는 true이다.
- !!을 사용해서 일반 스칼라값을 true false를 나타내는 값으로 만들 수 있음.

## STDIN

```perl
$line = <STDIN>;
```

- 한줄씩 `<STDIN>`를 이용해서 값을 입력받을 수 있다.
- 개행문자 \\n포함

### chomp

- 문자열에서 끝의 개행문자를 삭제해준다.
- 리턴값은 삭제된 문자의 개수(보통 1)
- 개행문자가 없으면 리턴값은 0이고 아무것도 하지 않음.

```perl
chomp($text = <STDIN>); # STDIN의 내용을 대입하고, 그 변수를 chomp함수의 인자로 넘겨준다.
```

## undef값

- 스칼라 변수가 정의되기 전에 갖는 값을 `undef`라 한다.
- 그러므로 정의되지 않은 스칼라변수를 사용해도 오류가 나지 않음.
  - 숫자인 것처럼 사용하면 0으로 작동
  - 문자열인 것처럼 사용하면 ""으로 작동
  - 하지만 `undef`자체는 숫자나 문자열이 아닌 완전 다른 종류의 스칼라 값이다.
- `use warnings`안에서는 오류가 난다.

## defined 함수

- 값이 `undef`인지 빈 문자열인지 구별하는 함수
- `<STDIN>`에서 EOF를 인지하는데에 사용되기도 한다.
