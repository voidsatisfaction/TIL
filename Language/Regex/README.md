# 정규표현식(Regular Expression)

- [생활코딩 - 정규표현](https://opentutorials.org/course/909/5143)

이 문서는 반드시 렌더링된 마크다운으로 봐야함(이스케이프 문자 때문에)

## 실전 예시

```js
const pinNumber = html.match(/[0-9]+-[0-9]+-[0-9]+-[0-9]+/i)[0]; // 문화상품권 핀번호 e.g 1234-5678-9012-345678
```

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

## 수량자2

### {n}

정확히 몇개를 나타내는지 지정

- source
  - One ring to bring them all and in the darkness bind them
- case1
  - regex: .{5}
  - fm: **One r** ing to bring them all and in the darkness bind them
  - am: **One ring to bring them all and in the darkness bind the**m
- case2
  - regex: [els]{1,3}
  - fm: On**e** ring to bring them all and in the darkness bind them
  - am: On**e** ring to bring th**e**m a**ll** and in th**e** darkn**ess** bind th**e**m
- case3
  - regex: [a-z]{3,}
  - fm: One **ring** to bring them all and in the darkness bind them
  - am: One **ring** to **bring** **them** **all** **and** in **the** **darkness** **bind** **them**

### ? * + 를 {n}으로 나타낼 수 있음

- source
  - AA ABA ABBA ABBBA
- case1
  - regex: AB*A
  - fm: **AA** ABA ABBA ABBBA
  - am: **AA** **ABA** **ABBA**
- case2
  - regex: AB{0,}A
  - fm: **AA** ABA ABBA ABBBA
  - am: **AA** **ABA** **ABBA**
- case3
  - regex: AB+A
  - fm: AA **ABA** ABBA ABBBA
  - am: AA **ABA** **ABBA** **ABBBA**
- case4
  - regex: AB{1,}A
  - fm: AA **ABA** ABBA ABBBA
  - am: AA **ABA** **ABBA** **ABBBA**
- case5
  - regex: AB?A
  - fm: **AA** ABA ABBA ABBBA
  - am: **AA** **ABA** ABBA ABBBA
- case6
  - regex: AB{0,1}A
  - fm: **AA** ABA ABBA ABBBA
  - am: **AA** **ABA** ABBA ABBBA

### 여러가지 표현

수량자뒤에 ? -> 가장 적은 단위를 표현

*?의 경우는 그냥 수량자 0이됨(*가 0 ~ 다수 이므로 여기에서 가장 적은 단위는 0)

- source
  - One ring to bring them all and in the darkness bind them
- case1
  - regex: r.*
  - fm: One **ring to bring them all and in the darkness bind them**
  - am: One **ring to bring them all and in the darkness bind them**
- case2
  - regex: r.*?
  - fm: One **r**ing to bring them all and in the darkness bind them
  - am: One **r**ing to b**r**ing them all and in the da**r**kness bind them
- case3
  - regex: r.+
  - fm: One **ring to bring them all and in the darkness bind them**
  - am: One **ring to bring them all and in the darkness bind them**
- case4
  - regex: r.+?
  - fm: One **ri**ng to bring them all and in the darkness bind them
  - am: One **ri**ng to b**ri**ng them all and in the da**rk**ness bind them
- case5
  - regex: r.?
  - fm: One **ri**ng to bring them all and in the darkness bind them
  - am: One **ri**ng to b**ri**ng them all and in the da**rk**ness bind them
- case6
  - regex: r.??
  - fm: One **r**ing to bring them all and in the darkness bind them
  - am: One **r**ing to b**r**ing them all and in the da**r**kness bind them

실제 활용

- source
  - <div>test</div><div>test2</div>
- case1
  - regex: <div>.+</div>
  - m: <div>test</div><div>test2</div>
  - 탐욕적인 수량자(greedy quantifier)
    - 가능하면 가장 큰 덩어리를 찾으려 함
- case2
  - regex: <div>.+?</div>
  - m: <div>test</div>
  - 게으른 수량자(lazy quantifier)
    - 가능하면 가장 작은 덩어리를 찾으려 함

## 경계

### 단어

\\w는 [A-z0-9_]와 같음

- source
  - A1 B2 e3 d_4 e:5 ffGG77--___--
- case1
  - regex: \\w
  - fm: **A**1 B2 e3 d_4 e:5 ffGG77--___--
  - am: **A1** **B2** **e3** **d_4** **e**:**5** **ffGG77**--**___**--
- case2
  - regex: \\w*
  - fm: **A1** B2 e3 d_4 e:5 ffGG77--___--
  - am: **A1** **B2** **e3** **d_4** **e**:**5** **ffGG77**--**___**--
- case3
  - regex: [a-z]\w*
  - fm: A1 B2 **e3** d_4 e:5 ffGG77--___--
  - am: A1 B2 **e3** **d_4** **e**:5 **ffGG77**--___--
- case4
  - regex: \\w{5}
  - fm: A1 B2 e3 d_4 e:5 **ffGG7**7--___--
  - am: A1 B2 e3 d_4 e:5 **ffGG7**7--___--
- case5
  - regex: [A-z0-9_]
  - fm: **A**1 B2 e3 d_4 e:5 ffGG77--___--
  - am: **A1** **B2** **e3** **d_4** **e**:**5** **ffGG77**--**___**--

### 단어2

\\W는 [^A-z0-9_]과 같음(w의 정반대의 의미)

- source
  - AS_34:AS11.23 @#$%12^*
- case1
  - regex: \\W
  - fm: AS_34 **:** AS11.23 @#$%12^*
  - am: AS_34 **:** AS11 **.** 23 **@#$%** 12 **^***

### 숫자

 \\d는 [0-9]와 같음(digit)

 - source
   - Page 123; published: 1234 id=12#24@112
 - case1
   - regex: \\d
   - fm: Page **123**; published: 1234 id=12#24@112
   - am: Page **123**; published: **1234** id=**12**#**24**@**112**
 - case2
   - regex: \\D
   - fm: **P**age 123; published: 1234 id=12#24@112
   - am: **Page** 123 **; published:** 1234 **id=**12 **#** 24 **@** 112

### 단어 경계

\\b 단어가 시작하는 지점과 끝나는 지점을 기준으로 나눠줌

- source
  - Ere iron was found or tree was hewn, When young was mountain under moon; Ere ring was made, or wrought was woe, It walked the forests long ago.
- case1
  - regex: \b.
  - fm: **E**re iron was found or tree was hewn, When young was mountain under moon; Ere ring was made, or wrought was woe, It walked the forests long ago.
  - am: **E**re **i**ron **w**as **f**ound or tree was hewn, When young was mountain under moon; Ere ring was made, or wrought was woe, It walked the forests long ago.
  - am: Ere iron was found or tree was hewn, When young was mountain under moon; Ere ring was made, or wrought was woe, It walked the forests long ago. (모든 단어의 가장 앞 글자 표현)
- case2
  - regex: \b\w+\b
  - fm: **Ere** iron was found or tree was hewn, When young was mountain under moon; Ere ring was made, or wrought was woe, It walked the forests long ago.
  - am: **Ere** **iron** **was** **found** or tree was hewn, When young was mountain under moon; Ere ring was made, or wrought was woe, It walked the forests long ago.(모든 단어 선택)

\\B \\b의 반대 의미

- source
  - cat concat
- case1
  - regex: \\B.
  - fm: c**at** concat
  - am: c**at** **concat**
- case2
  - regex: \\bcat
  - fm: **cat** concat
  - am: **cat** concat
- case3
  - regex: cat\\b
  - fm: **cat** concat
  - am: **cat** con**cat**

### 문자열의 가장 첫부분을 매칭함

\\A는 문자열의 가장 앞만 매칭 가능(^는 새 줄이 생길때 마다 매칭)
\\Z는 문자열의 가장 끝만 매칭 가능($는 새 줄이 생길떄 마다 매칭)

- source
  - Ere iron was found or tree was hewn, When young was mountain under moon; Ere ring was made, or wrought was woe, It walked the forests long ago.
- case1
  - regex: \\A...
  - fm: **Ere** iron was found or tree was hewn, When young was mountain under moon; Ere ring was made, or wrought was woe, It walked the forests long ago.
  - am: **Ere** iron was found or tree was hewn, When young was mountain under moon; Ere ring was made, or wrought was woe, It walked the forests long ago.
- case2
  - regex: ...\\Z
  - Ere iron was found or tree was hewn, When young was mountain under moon; Ere ring was made, or wrought was woe, It walked the forests long a **go.**
  - Ere iron was found or tree was hewn, When young was mountain under moon; Ere ring was made, or wrought was woe, It walked the forests long a **go.**

## Assertions

(?=<pattern>)은 문자열을 검색할때 pattern을 쓰고, 문자열을 매칭할때는 고려하지 않음

- source
  - AAAX---aaax---111
- case1
  - regex: \\w+(?=X)
  - fm: **AAA**X---aaax---111
  - am: **AAA**X---aaax---111
- case2
  - regex: \\w+
  - fm: **AAAX**---aaax---111
  - am: **AAAX**---**aaax**---**111**
- case3
  - regex: \\w+(?=\\w)
  - fm: **AAA**X---aaax---111
  - am: **AAA**X--- **aaa** x---**11** 1
