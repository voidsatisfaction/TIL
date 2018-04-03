# 정규표현식(Regular Expression)

- [생활코딩 - 정규표현](https://opentutorials.org/course/909/5143)

이 문서는 반드시 렌더링된 마크다운으로 봐야함(이스케이프 문자 때문에)

## 정의

- 문자열을 처리하는 방법
- 특정한 조건의 문자를 '검색'하거나 '치환'하는 과정을 매우 간편하게 처리 할 수 있도록 하는 수단

## 정규표현식 기본 패턴

- 정규 표현식은 대소문자 구별
- 정규 표션식의 서치 패턴은 화이트 스페이스를 포함해서(스페이스, 탭, 새 줄) 시그니피컨트(significant)하다

## 위치와 이스케이핑

- ^who
  - 소스의 시작이 who로 시작되는지 판별
- who$
  - 소스의 끝이 who로 끝나는지 판별
- \\
  - 원래 갖고 있던 특수문자의 의미를 없애줌
  - 이스케이핑

- source
  - $12$ \\-\\ $25$
- case1
  - regex: ^$
  - match(x)
- case2
  - regex: \\$
  - first match: **$**12$ \\-\\ $25$
  - all match: **$**12**$** \\-\\ **$**25**$**
- case3
  - regex: ^\\$
  - fm(first match): **$**12$ \\-\\ $25$
  - am(all match): **$**12$ \\-\\ $25$
- case4
  - regex: \\$$
  - fm: $12$ \\-\\ $25**$**
  - al: $12$ \\-\\ $25**$**
- case5
  - regex: \\\\
  - fm: $12$ **\\**-\\ $25$
  - am: $12$ **\\**-**\\** $25$

## 모든 문자

- .
  - 모든 문자를 매칭함
  - 와일드카드

- source
  - Regular expressions are powerful!!!
- case1
  - regex: .
  - fm: **R**egular expressions are powerful!!!
  - am: **Regular expressions are powerful!!!**
