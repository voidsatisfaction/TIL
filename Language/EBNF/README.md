# EBNF(Extended Backus Naur Form)

- [EBNF - 위키피디아](https://ja.wikipedia.org/wiki/EBNF)

프로그래밍 언어의 문법(Specification)을 정의하기 의한 메타 언어. BNF를 확장한 것을 말한다.

## |: 또는

```
digit excluding zero = "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
digit = "0" | digit excluding zero;
```

## 생성규칙

- 종단기호: 문자나 숫자기호로 구성
- 비종단기호: 변수 같은 느낌

```
twelve = "1", "2";
three hundred twelve = "3", twelve;
```

## {}: 0번 이상의 반복

```
natural number = digit excluding zero , { digit };
```

## \[\]: 선택적 표현

```
integer = "0" | [ "-" ] , natural number;
identifier = alphabetic character , [ { alphabetic character | digit } ] ;
```

## (): 여러가지 옵션 중 반드시 하나를 선택하여야 할 때 사용.

```
assignment = identifier , ":=" , ( number | identifier | string ) ;
```
