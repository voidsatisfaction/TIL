# Lists and Arrays

리스트(list)는 순서가 있는 **스칼라의 모음(collection)** 이다. 배열(array)은 리스트를 포함하는 변수이다. 리스트는 데이터이고, 배열은 그 데이터를 저장하는 변수를 말한다. 배열에 속하지 않은 리스트 값을 갖을 수 있으나, 모든 배열은 반드시 리스트를 갖고 있다(적어도 빈 리스트라도)

리스트와 배열은 많은 연산을 공유하나, 다르다는 사실을 절대 잊으면 안된다.

각각의 요소는 분리된 스칼라 값이다. 그리고 순서가 있다(첫 요소에서 마지막 요소까지에 속함) 가장 첫 요소는 0을 인덱스로 갖음. 각각의 요소는 스칼라 값(숫자, 문자열, 레퍼런스, undef)이다.

배열과 리스트는 사용 가능한 메모리 이내라면 어떠한 개수의 요소도 갖을 수 있다.

"no unnecessary limits"

c.f 리스트가 스칼라의 모음이기 때문에 다음을 조심해야한다:

```perl
@array = (
  (1, 2, 3),
  (4, 5, 6),
);
# (1, 2, 3, 4, 5, 6)
```

컨택스트가 이미 스칼라라고 인지하기 때문에 위와 같은 현상이 일어난다. 그러므로 배열의 배열을 만들기 위해서는 다음과 같이 해야한다.

```perl
my $array = [
  [1, 2, 3],
  [4, 5, 6],
];

my $first = @$array[0];
my $second = @$array[1];

print @$first, "\n", @$second, "\n";

# 123
# 456
```

## 배열 요소에의 접근

스칼라에대한 접근이기 때문에 `$`를 사용해서 접근해야 한다.
```perl
@fred = (1, 2, 3);
$fred[0]; # 1
$fred[1.5]; # 2
$fred[123_456]; # undef
```

## 특별한 배열 인덱스

```perl
@fred = (1, 2, 3);
$fred[99] = 'hi'; # 97개의 undef생성
$fred[-1] # hi
$fred[-100] # 1
$fred[$#fred] # hi
$fred[-200] # error!
```

## 리스트 리터럴

```
(1, 2, 3) # (1, 2, 3)
(1, 2, 3,) # (1, 2, 3)
()
(1..100) # 1 ~ 100, .. 연산자

(1..5) # (1, 2, 3, 4, 5)
(1.7..5.7) # 위와 같음
(5..1) # ()
(0, 2..6, 10, 12) # (0, 2, 3, 4, 5, 6, 10, 12)
($m..$n) # $m에서부터 $n까지의 숫자로 이루어진 리스트
(0..$#rocks) # 모든 rocks의 인덱스들
```

## qw 단축키(shortcut)

- 반복되는 단순한 단어들의 리스트가 자주 사용되므로 만들어진 단축키
- `qw(fred barney betty wilma dino)`
- qw는 quoted words의 준말.
  - qw는 홑따옴표 문자열로 받아들여진다.
  - white space는 무시된다.

```perl
qw(
  fred
  barney
  betty
  wilma
  dino
)
qw! fred barney betty wilma dino !
qw[ fred barney betty wilma dino ]
# 위의 예는 모두 같은 리스트값을 갖는다.

qw {
  /sr/dict/words
  /home/rootbeer/.ispell_english
}
# 위의 예는 여러 구분자를 사용하는 것의 장점을 나타낸다.
# 만약 /만 qw의 구분자가 될 수 있다면 리스트를 이용해서 유닉스 파일시스템을 제어하는 것이 꽤나 귀찮았을 것이다.
```

## 리스트 할당

```perl
($fred, $barney, $dino) = ("flintstone", "rubble", undef);
($fred, $barney) = ($barney, $fred); # 값을 치환하기 쉽게 된다.
($betty[0], $betty[1]) = ($betty[1], $betty[0]); # 배열 속의 값을 치환

($fred, $barney) = qw< flintstone rubble slate granite >; # 뒤의 두개의 값은 무시됨
($wilma, $dino) = qw[flintstone]; # $dino는 undef

($rocks[0], $rocks[1], $rocks[2], $rocks[3]) = qw/ talc mica feldspar quartz /;

# 배열 변수의 활용
@rocks = qw/ bedrock slate lava /;
@tiny = ();
$dino = "granite";
@quarry = (@rocks, "crushed rock", @tiny, $dino); # (bedrock, slate, lava, crushed rock, granite)

@copy = @quarry; # 값을 deepcopy해감.
@copy[0] = "babo";
print @copy, "\n"; # babo...
print @quarry, "\n"; # bedrock...
```

## pop, push, shift, unshift 연산자

pop은 다음과 같다:

```perl
@array = 5..9;
$fred = pop(@array); # 9
$barney = pop(@array); # 8
pop @array;
```

push는 다음과 같다:

```perl
push(@array, 0);
push @array, 8;
push @array, 1..10; # 10개의 새 요소가 추가
```

shift와 unshift는 다음과 같다:

```perl
@array = qw# dino fred barney #;
$m = shift(@array);
$n = shift @array;
shift @array;
unshift(@array, 5);
unshift @array, 4;
@others = 1..3;
unshift @array, @others; # (1, 2, 3, 4, 5)
```

## splice 연산자

배열 가운데의 요소를 삭제하는 데에 쓰인다. `splice 배열변수 시작인덱스 지울개수 대체할리스트`

```perl
@array = qw( pebbles dino fred barney betty );
@removed = splice @array, 2; # @removed qw(fred barney betty), @array qw(pebbles dino)
```
