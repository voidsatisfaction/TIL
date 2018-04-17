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

### ^

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

### .

- .
  - 모든 문자를 매칭함
  - 와일드카드
  - 단순히 점을 가르키고 싶으면 이스케이핑 하면 됨

- source
  - Regular expressions are powerful!!!
- case1
  - regex: .
  - fm: **R**egular expressions are powerful!!!
  - am: **Regular expressions are powerful!!!**
- case2
  - regex: ......
  - fm: **Regula**r expressions are powerful!!!
  - am: **Regular expressions are powerf**ul!!!
    - 마지막은 5개의 문자로 이루어져있으므로 선택되지 못함

- source
  - O.K.
- case1
  - regex: \\..\\.
  - fm: O**.K.**
  - am: O**.K.**

## 특정 문자

### \[\]

- \[\]
  - 대괄호 속 문자와 일치하는 문자를 발견하면 매칭
  - 순서는 상관 없음
  - 대괄호 속을 문자 하나로 봄
  - OR같은 느낌

- source
  - How do you do?
- case1
  - regex: [oyu]
  - fm: H**o**w do you do?
  - am: H**o**w d**o** **you** d**o**?
- case2
  - regex: [dH].
    - 이는 두개의 문자
  - fm: **Ho**w do you do?
  - am: **Ho**w **do** you **do**?
- case3
  - regex: [owy][yow]
  - fm: H**ow** do you do?
  - am: H**ow** do **yo**u do?

### -

- \-
  - 많은 문자를 단축해서 나타냄

- source
  - ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789
- case1
  - regex: [C-K]
  - fm: AB**C** ...
  - am: AB**CDEF ... K**LM ...
- case2
  - regex: [CDEFGHIJK]
  - fm: AB**C** ...
  - am: AB**CDEF ... K**LM ...
- case3
  - regex: [a-d]
  - fm: ... **a** ...
  - am: ... **abcd** ...
- case4
  - regex: [2-6]
  - fm: ... **2** ...
  - am: ... **23456** ...
- case5
  - regex: [C-Ka-d2-6]
  - fm: ... **C** ...
  - am: AB**CDEF ... K**LM ... **abcd** ... **23456** ...

- [^...]
  - 대괄호 속의 ^
  - 부정의 의미

- source
  - ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789
- case1
  - regex: [^CDghi45]
  - fm: **A**B ...
  - am: **AB**CD**EF ... **ghi**jk...23**45**6789**
- case2
  - regex: [^W-Z]
  - fm: **A**BC ...
  - am: **AB ... V**WXYZ**ab ...**

## 서브 패턴

### ()

- ()
  - 특정 문자열의 선택

- source
  - Monday Tuesday Friday
- case1
  - regex: (on|ues|rida)
  - fm: M**on**day Tuesday Friday
  - am: M**on**day T**ues**day F**rida**y
- case2
  - regex: (Mon|Tues|Fri)day
  - fm: **Monday** Tuesday Friday
  - am: **Monday** **Tuesday** **Friday**
- case3
  - regex: ..(id|esd|nd)ay
  - fm: **Monday** Tuesday Friday
  - am: **Monday** **Tuesday** **Friday**

## 수량자

### * + ?

- \*
  - 0 ~ 여러개
  - *앞의 문자가 여러개 있을 수도 있고 없을 수도 있음
- \+
  - 1 ~ 여러개
  - +앞의 문자가 1개 이상이 올 수 있음
- ?
  - 0 ~ 1
  - ?앞의 문자가 0개 혹은 1개만

- source
  - aabc abc bc
- case1
  - regex: a*b
    - b앞에 a가 0 ~ 여러개 있을 수 있음
  - fm: **aab**c abc bc
  - am: **aab**c **ab**c **b**c
- case2
  - regex: a+b
    - b앞에 a가 1 ~ 여러개 있을 수 있음
  - fm: **aab**c abc bc
  - am: **aab**c **ab**c bc
- case3
  - regex: a?b
    - b앞에 a가 0개 혹은 1개임
  - fm: a**ab**c abc bc
  - am: a**ab**c **ab**c **b**c

### * 수량자의 사용

- source
  - \-@- \*\*\* -- "*" -- \*\*\* -@-
- case1
  - regex: .*
  - fm: **\-@- \*\*\* -- "*" -- \*\*\* -@-**
  - am: **\-@- \*\*\* -- "*" -- \*\*\* -@-**
- case2
  - regex: -A*-
  - fm: \-@- \*\*\* **--** "*" -- \*\*\* -@-
  - am: \-@- \*\*\* **--** "*" **--** \*\*\* -@-
- case3
  - regex: [-@]*
  - fm: **\-@-** \*\*\* -- "*" -- \*\*\* -@-
  - am: **\-@-** \*\*\* -- "*" -- \*\*\* **-@-**

### + 수량자의 사용

- source
  - \-@@@- \* \*\* - - "*" - - \* \*\* -@@@-
- case1
  - regex: \\*+
  - fm: \-@@@- **\*** \*\* - - "*" - - \* \*\* -@@@-
  - am: \-@@@- **\* \*\*** - - "*****" - - **\* \*\*** -@@@-
- case2
  - regex: \-@+-
  - fm: **\-@@@-** \* \*\* - - "*" - - \* \*\* -@@@-
  - am: **\-@@@-** \* \*\* - - "*" - - \* \*\* **-@@@-**
- case3
  - regex: [^ ]+
    - 공백이 아닌것이 하나이상 있을 때 선택하라
  - fm: **\-@@@-** \* \*\* - - "*" - - \* \*\* -@@@-
  - am: **\-@@@- \* \*\* - - "*" - - \* \*\* -@@@-**

### ? 수량자의 사용

- source
  - --XX-@-XX-@@-XX-@@@-XX-@@@@-XX-@@-@@-
- case1
  - regex: -X?XX?X
  - fm: -**-XX**-@-XX-@@-XX-@@@-XX-@@@@-XX-@@-@@-
  - am: -**-XX**-@**-XX**-@@**-XX**-@@@**-XX**-@@@@**-XX**-@@-@@-
- case2
  - regex: -@?@?@?-
  - fm: **--**XX-@-XX-@@-XX-@@@-XX-@@@@-XX-@@-@@-
  - am: **--**XX**-@-**XX**-@@-**XX**-@@@-**XX-@@@@-XX**-@@-**@@-
