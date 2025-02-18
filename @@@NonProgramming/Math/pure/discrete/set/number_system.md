# 수의 체계

- 참고
- 의문
- 개요
- 자연수
  - 자연수
  - 자연수의 연산
  - 자연수의 순서관계
- 정수와 유리수
  - 정수
  - 체 & 순서체
  - 유리수
- 실수
  - 데데킨트 절단
  - 코시 수열
- 완비순서체

## 참고

- 집합과 수의 체계 - 계승혁

## 의문

- *연산이 제대로 정의되어있다는 것이 무슨 의미인가?*
- 정수 대수구조를 유리수 대수구조로 편입시킬 때, 사용하는 개념이 homomorphism인가?
  - 그러하다. 예를들어 정수를 유리수체로 편입 시킬때, monomorphism인 함수를 제시해서, 정수의 모든 성질(연산, 순서관계)를 유리수의 정수 부분집합에서 똑같이 사용할 수 있게 함.
  - 이렇게 하므로써, 유리수와 정수의 연산 역시 자연스럽게 행할 수 있음
- *잘 정의되어 있다*
  - 잘 정의되어 있다는것이 구체적으로 무엇을 의미하는가?
- *실수의 성질을 왜 공리라 부르는가?*
  - *애초에 공리란 무엇인가?*
- *다음 정리들은 왜 동치인가?(기본열 이용?)*
  - 사잇값 정리
  - 어떤 성질 M이 모든 실수에 대하여 성립하지는 않지만, 어떤 특정한 실수 u보다 작은 모든 실수에 대하여 성립한다고 가정하자. 이제, 실수 x보다 작은 모든 실수에 대하여 M이 성립하는 실수 x들을 생각하면, 이러한 수들 중에서 제일 큰 수가 존재한다.
  - 코시의 판정법
  - 완비성공리
    - 비어 있지 않은 실수 집합 `A⊆R`이 상계를 가지면 A는 반드시 최소상계를 가진다.
- *애초에 코시수열과 데데킨트 절단의 구성방식의 배경이나 유래는?*
  - 코시수열은 더더욱 이해가 안감. 어떤 배경이 있어서 코시는 저렇게 수열을 구성한 것인가?
    - 극한과 무한소의 개념과 관계가 있을수도?

## 개요

## 1. 자연수

### 자연수

자연수(0을 포함하지 않는)는 대수구조 상 반환(semiring)에 속함. 덧셈에 대한 가환 모노이드, 곱셈에 대한 모노이드, 분배 법칙이 성립

- 자연수 구성에 필요한 것들
  - 집합 A에 대한 새 집합A+
    - `A+ = A U {A}`
  - `0 = φ`
- 자연수
  - 정의
    - 페아노 공리계를 따르는 집합과 연산구조
      - 페아노 대수(Peano arithmetic)의 '약한' 조건으로 자연수를 구성할 경우, 자연수 구조는 더 이상 유일하지 않고, 여러가지 논스탠다드 모델이 등장한다. 게중에는 실수처럼 셀 수 없는 자연수 모델도 있다. >> 페아노 공리계만 만족하면 되므로
    - 다음 두 가지 성질을 가지는 집합 A들 전체의 교집합을 N으로 쓰고(왜 전체의 교집합일까? - e.g `A = {0, 1, ..., K} 원소 K는 K+ = K 가 되도록, +와 0을 정의`하면 이것은 0, 1, ... 이외의 특수한 원소가 들어가기 때문), 이 집합의 원소들을 자연수라 함
      - `φ∈F`
      - `A∈F => A+∈F`
  - 성질(페아노 공리계)
    - ① `0 ∈ N`
      - 0은 무정의 용어
    - ② `n ∈ N => n+ ∈ N`
    - ③ `∀n∈N, n+ ≠ 0`
      - **폰노이만의 자연수 구성을 취할 경우(`0 = φ, n+ = n U {n}`)** 자명
    - ④ `X ⊆ N, (0∈X ∧ n∈X => n+∈X) => X = N`
      - 귀납적 공리
      - 수학적 귀납법을 사용할 수 있는 근거
        - 자연수 `n∈N`에 관한 명제 `P(n)`이 있을 때, `P(n)`이 성립하는 자연수 `n∈N`들의 집합을 X라 두자.
        - `(P(0)≡t ∧ P(n) => P(n+1)) => X = N`
          - 왜냐하면 집합 X가 페아노 공리계의 ④ 성질을 만족하기 때문
    - ⑤ `m,n∈N, m+=n+ => m=n`
    - **공리계로 성질을 정해놓고 이 성질을 만족하면 자연수집합이라고 부를 수 있게 한 것?? >> 그렇다**
      - 자연수를 구성하기 위해 필요한 것
        - 0이 무엇인지 정의
        - n+가 무엇인지 정의
      - 자연수 구성 예시
        - 체르멜로: `0 = φ, n+(= n+1) = {n}`
        - 폰 노이만: `0 = φ, n+ = n U {n}`
        - 이걸 보면 마틴오더스키 선생님의 Functional Programming In Scala에서 자연수를 클래스로서 구성했던것이 생각남

### 자연수의 연산

> <참고> 자연수에서의 연산법칙을 비롯한 다양한 내용의 증명은 페아노공리계의 수학적귀납원리를 이용해서 증명하는 경우가 많다.

- 집합 X의 한 원소 `a∈X`과 함수 `f: X -> X`에 대하여, 다음성질을 만족하는 함수 `r : N -> X`가 유일하게 존재한다.(집합 X의 원소 r(0), r(1), ... 가 특정 점화식을 만족하도록 귀납적으로 정의할 수 있음을 보여줌)
  - `r(0) = a`
  - `∀n∈N, r(n+) = f(r(n))`

#### 더하기와 곱하기의 정의

더하기 곱하기 지수승을 recursive한 함수를 정의해서 정의함(recursion theorem)

- 더하기
  - 정의
    - 위의 정리를 적용하면, 각 자연수 `m∈N`에 대하여 다음을 만족하는 함수 `rm: N -> N`이 유일하게 존재함
      - `rm(0) = m, n∈N => rm(n+) = [rm(n)]+`
    - `m+n = rm(n), m,n∈N`
  - 자연수 집합에서 성립하는 연산법칙
    - 항등원
      - `n+0 = 0+n = n`
    - 결합법칙
      - `(m+n)+k = m+(n+k)`
    - 교환법칙
      - `m+n = n+m`
- 곱하기
  - 정의
    - 마찬가지로 위의 정리를 적용하여 유일한 δ함수를 정의
      - `δm : N -> N, δm(0) = 0, n∈N => δm(n+) = δm(n)+m`
    - `m,n∈N, mn = δm(n)`
  - 자연수 집합에서 성립하는 연산법칙
    - `n0 = 0n = 0`
    - 항등원
      - `n1 = 1n = n`
    - 결합법칙
      - `(mn)k = m(nk)`
    - 교환법칙
      - `mn = nm`
- 더하기와 곱하기의 분배법칙
  - `m(n+k) = mn+mk`
  - `(n+k)m = nm+km`
- 지수 연산
  - `m^(n+k) = m^n m^k`
  - `(mn)^k = m^k n^k`
  - `(m^n)^k = m^(nk)`

---

참고

a,b,c의 곱셈 `abc`라고 표현이 가능한 이유는 `(ab)c = a(bc)`가 성립하기 때문

### 자연수의 순서관계

순서관계를 정의하는 것 부터

- 순서관계 정의
  - `m,n∈N, m<=n <=> m∈n ∨ m=n`
    - 이것이 순서관계임을 증명
  - `m,n∈N, m<=n ∧ m≠n <=> m∈n`
    - `∵ ∀n∈N, n!∈n`
      - 잘 이해가 안됨
- 정리
  - 공집합이 아닌 자연수의 집합에는 최소 원소가 있음
    - 비어 있지 않은 자연수들의 집합은 최소 원소를 가짐
      - 임의의 두 자연수 `m,n∈N`에 대하여 `m<=n`혹은 `n<=m`이 성립한다.
  - 공집합이 아닌 자연수의 집합에는 최대 원소가 있음
    - 위로 유계이며 비어 있지 않은 자연수들의 집합 `A⊆N`는 최대 원소를 가짐
  - 자연수는 큰 수에서 작은수로 뺄셈이 가능
    - `m,n∈N, n>=m <=> ∃k∈N, n=m+k ∧ (m+k=m+l => k=l)`
    - `m+k <= m+l <=> k<=l`
    - `mk <= ml <=> k<=l (단, m≠0)`
  - 자연수의 나머지 정리
    - `m,l∈N, 0<m<=l, ∃n,r∈N, l = mn+r, (0<=r<m) ∧ (mn+r = mk+s => n=k ∧ r=s)`

## 2. 정수와 유리수

### 정수

- 정수
  - 접근
    - `m,n∈N, n<=m => m=n+k인 k가 유일하게 존재`
      - 그러한 `k`를 `m-n`으로 씀
    - `m<n`인 경우에도 `m-n`이 뜻을 가지게끔 수의 범위를 넓히자
      - `m-n = (m,n)`
    - `N x N = {(m,n) | m,n∈N}`
      - `m>=n`제한 없앰
      - 관계정의
        - `(m,n) ~ (m',n') <=> m+n' = n+m'`
          - `~`는 동치관계
          - `m>k,n>=k => (m,n) ~ (m-k, n-k)`
  - 정의
    - `Z = N x N/~`
      - Z의 원소를 정수라 부름
      - `Z = {[n,0], [0,0], [0,n] | n∈N}`
        - `[1,0]`은 정수 1
        - `[0,5]`는 정수 -5에 대응(왜냐면 (0,5) = 0-5)
  - 관계정의
    - `[m,n] >= [k,l] <=> m+l >= n+k`
      - `>=`는 순서관계
    - 관계에 관한 정리
      - `비어있지 않은 Z의 부분집합 A가 위로 유계 => A는 최대원소 가짐`
      - `비어있지 않은 Z의 부분집합 A가 아래로 유계 => A는 최소원소 가짐`
- 정수의 연산
  - 덧셈
    - `[m,n]+[k,l] = [m+k,n+l]`
    - 결합법칙, 항등원, 역원, 교환법칙 존재 / 성립
  - 곱셈
    - `[m,n]・[k,l] = [mk+nl,ml+nk]`
    - 결합법칙, 항등원, 교환법칙 존재 / 성립
- 정수의 표기
  - `f: N -> Z, f(n) = [n,0]`
    - f는 단사함수
    - `m,n∈N`
      - `f(m+n) = f(n)+f(m)`
      - `f(mn) = f(n)f(m)`
      - `m>=n <=> f(m) >= f(n)`
  - f가 성립하므로, `[n,0], [0,0], [0,n]`표기 대신 `n, 0, -n`으로 쓸 수 있음

### 체 & 순서체

- 체
  - 정의
    - 더하기 연산법칙
      - ① `∀a,b,c∈F, a+(b+c) = (a+b)+c`
      - ② `∃e∈F, ∀a∈F, a+e = e+a = a ∧ (a+e' = e'+a = a => e' = e)`
        - 이를 0이라고 하고, 더하기의 항등원이라 함
      - ③ `∀a∈F, ∃x∈F, a+x = x+a = 0 ∧ (a+x' = x'+a = 0 => x' = x)`
        - `x = -a`라 쓰고, a의 역원이라고 함
      - ④ `∀a,b∈F, a+b = b+a`
    - 곱하기 연산법칙
      - ⑤ `∀a,b,c∈F, a(bc) = (ab)c`
      - ⑥ `∃1∈F, ∀a∈F, a・1 = 1・a = a ∧ (a・1' = 1'・a = a => 1' = 1) ∧ 1 ≠ 0`
      - ⑦ `∀a∈F \ {0}, ∃x∈F, ax = xa = 1`
        - `a^-1` 혹은 `1/a`이라 쓰고 곱하기에 관한 a의 역원이라 함
      - ⑧ `∀a,b∈F, ab = ba`
    - 더하기 연산과 곱하기 연산의 관계
      - ⑨ `∀a,b,c∈F, a(b+c) = ab+ac`
- 순서체(체 위의 순서 도입)
  - 양수 개념 도입
    - `S∈F, -S = {-a | a∈S}`
  - 정의
    - `∃P∈F, P≠φ`
      - ① `a,b∈P => a+b, ab∈P`
      - ② `F = P U {0} U (-P)`
      - ③ `P∩{0} = φ ∧ P∩-P = φ ∧ {0}∩-P = φ`
    - **체 F에 비어있지 않은 부분집합 P가 존재하여 위의 조건을 만족하면 그러한 F를 순서체라 함**
    - **P의 원소를 양수라 함**
  - 순서관계 정의
    - `a,b∈F, a-b∈P <=> a가 b보다 크다 <=> a>b <=> b<a`
    - `a<=b <=> b-a∈P ∨ a=b`
  - 관찰
    - 정수의 집합은 체1 - 체6 과 체8 - 체9 가 성립
    - 0을 제외한 자연수 전체의 집합을 `PZ ⊆ Z`라 두면, 체순의 정의 요건 1-3이 성립한다.
  - 정리
    - `∀a,b,c∈F(순서체)`
      - `a>=b, a<=b => a=b`
      - `a<=b, b<=c => a<=c`
      - `a+b < a+c <=> b<c`
      - `a>0, b<c => ab < ac`
      - `a<0, b<c => ab > ac`
      - `a^2 >= 0, 특히 1 > 0`
      - `0 < a < b => 0 < 1/b < 1/a`
      - `a,b > 0 => (a^2<b^2 <=> a<b)`
- 절댓값
  - 정의(`a∈F`)
    - `|a| = a (a>=0) or -a (a<0)`
  - 정리
    - `∀a,b,c∈F`
      - `|a|>=0 ∧ |a| = 0 <=> a = 0`
      - `|ab| = |a||b|`
      - `b>=0 => (|a|<=b <=> -b<=a<=b)`
      - `||a|-|b|| <= |a±b| <= |a| + |b|`
        - *앞 부등식을 어떻게 증명할까?*
      - `|a-c| <= |a-b| + |b-c|`

### 유리수

- 유리수
  - 배경
    - 정수의 체7성질(곱셈에 대한 역원)을 만족시키기 위한 확장
    - 확장 방식은 자연수에서 정수로 확장한 것과 비슷한 방식
  - 정의
    - 동치관계
      - `Z x (Z\{0}), (a,b)~(c,d) <=> ad=cb`
    - `Q = Z x (Z\{0}) / ~`
- 유리수의 연산
  - 덧셈
    - `[a,b] + [c,d] = [ad+cb, bd]`
    - 항등원
      - `0* = [0, 1]`
  - 곱셈
    - `[a,b]・[c,d] = [ac, bd]`
    - 항등원
      - `1* = [1, 1]`
  - 유리수는 체이다.
- 유리수와 순서체
  - `Pz`를 `Z`의 양수집합이라 하면 `Z = Pz U {0} U -Pz`
  - `Z x (Z \ {0})`
    - `= {0} x (Z \ {0}) U Pz x Pz U (-Pz) x Pz`
      - `∵ (a,b) ~ (-a,-b)`
    - 임의의 유리수는 위의 세 집합에 속하는 원소들을 대표원으로 하는 동치류에 의하여 결정됨
  - `Pq = {[a,b] | (a,b) ∈ Pz x Pz}`라고 정의
    - 유리수의 양수의 집합
    - **Pq에 정의로 인하여 Q는 순서체의 성질을 만족**
  - 순서관계 역시 주어짐
    - `[a,b] >= [c,d] <=> [a,b]-[c,d] ∈ Pq ∨ [a,b]=[c,d]`
- 정수 구조를 유리수 구조로 대응(편입)
  - 함수 `f: Z -> Q, f(a) = a* = [a,1]`에 대해서
    - 함수 `f`는 단사함수
    - `f(a+b) = f(a)+f(b)`
    - `f(ab) = f(a)f(b)`
    - `a >= b <=> f(a) >= f(b)`
  - 결국 더하기, 곱하기 및 순서에 관한 한 `Z`는 `Q`의 부분집합
    - 정수집합의 구조(연산 및 관계)를 Q집합에 대응시킴(단사 대응)
      - *함수 f는 monomorphism*
      - *이러한 과정 전체?* 는 natural embedding이라고 부름
- 자연수 / 정수 / 유리수 구조를 순서체로 대응(편입)
  - 자연수를 순서체로 편입
    - 자연수의 집합과 순서체의 집합 사이에 monomorphism이 존재함을 보이자
    - `r: N -> F`
      - `r(0) = 0`
      - `r(n+1) = r(n+) = r(n) + 1 (n∈N)`
      - 존재성 / 유일성은 이미 보장
      - 좌변의 더하기는 N의 더하기, 우변의 더하기는 F의 더하기, 우변의 0, 1은 F에 대한 항등원
      - 성질
        - 단사함수
        - `r(n+m) = r(n)+r(m), m,n∈N`
          - 자연수의 `n+m`은 체의 `r(n)`과 `r(m)`의 합과 대응
        - `r(nm) = r(n)r(m), m,n∈N`
        - `r(n)∈PF, (n=1,2,...)`
  - 정수를 순서체로 편입
    - `r: Z -> F`
      - `r(n) = r(n) (n∈N)`
        - 좌변의 r은 `r: Z -> F`
        - 우변의 r은 `r: N -> F`
          - 위에 정의한 함수
      - `r(-n) = -r(n) (n∈N)`
  - 유리수를 순서체로 편입
    - `r: Q -> F`
      - `r(a/b) = r(a)/r(b), (a,b)∈Zx(Z\{0})`
      - 성질
        - 단사함수
        - `r(n+m) = r(n)+r(m), m,n∈N`
        - `r(nm) = r(n)r(m), m,n∈N`
  - 위의 결과로인한 정리
    - *아래의 성질을 만족하는 함수 `r: Q -> F`가 유일하게 존재한다.(어떻게 증명하지?)*
      - 단사함수
      - `∀r,s∈Q`
        - `r(r+s) = r(r)+r(s)`
        - `r(rs) = r(r)r(s)`
      - `r(P_Q) = r(Q)∩P_F`
    - 임의의 순서체 F가 유리수체 Q를 포함할 뿐 아니라, 두 순서체의 연산과 순서를 구별할 필요가 없음
- 아르키메데스의 성질
  - 정의
    - 순서체 F에 대하여 다음은 동치이다
      - ① `x>0 => ∃n∈N\{0}, x>1/n`
      - ② `y>0 => ∃n∈N\{0}, y<n`
      - ③ `집합N⊆F는 위로 유계가 아니다`
      - ④ `∀x,y>0, ∃n∈N\{0}, y<nx`
  - 예시
    - 유리수체는 아르키메데스의 성질을 만족한다.
  - 의의
    - (간단히 말해서) 대수적 집합 내에 무한히 크거나, 무한히 작은 원소가 없는 것을 의미
    - 아무리 작은 원소라도 그것을 유한번 더해서 어떤 크기의 원소보다도 커질 수 있다면 아르키메데스 성질을 가지고 있다고 볼 수 있다.

### 실수

- 실수란 무엇인가
  - 실수 자체를 내재적으로 무엇인가를 생각하기 보다는, **실수의 성질, 즉, 실수와 연산과 순서간의 상호 관계** 를 생각하는 것이 중요함
  - 그러한 실수의 성질을 만족하는 집합이 존재하는지(구성할 수 있는지) 밝히는 것도 중요
    - `F에 연산이 주어짐 = FxF -> F인 함수가 주어짐`
  - 그러한 실수는 또한 유일한가?
- 실수의 공리
  - 체 공리
  - 순서 공리
    - 부분집합 중 양수집합 P가 존재한다와 동치
  - 완비성 공리
    - **공집합이 아닌 실수의 진부분집합이 상계(upper bound)를 가지면 상한(least upper bound)이 존재한다.**
      - *상한이 존재한다고 해서 반드시 그 상한으로 인해서 실수가 유리수의 빈틈을 매웠다고 할 수 있는가?*
    - 유리수가 가진 빈틈을 다 메꾸어서 완전하게 갖추어진 수

실수는 결국 위의 공리를 전부 만족시키는 대수구조를 말하는데, 완비성 공리를 만족시키는 방법은 여러가지가 존재하고(데데킨트 절단, 코시수열 등), 그 방법에 의해서 생성된 실수는 결국 같기 떄문에, 완비순서체는 유일함이 증명되고 그것이 실수가 되는 것이다.

#### ① 데데킨트 절단

- 데데킨트 절단
  - `a⊆Q`가 다음 성질들을 만족하면, 데데킨트 절단 혹은 그냥 절단이라 함
    - ① `a≠φ, a≠Q`
      - 이 조건을 완화하면 확장된 실수 체계를 얻을 수 있음
    - ② `p∈a, q∈Q, q<p => q∈a` (a는 아래로 닫힌 집합)
    - ③ `p∈a => ∃r∈a, p<r` (a는 최대원소가 없음)
- 데데킨트 절단으로 R을 구성
  - 데데킨트 절단 전체의 집합을 `R`이라 씀
    - 이 집합의 원소, 즉 데데킨트 절단을 `실수`라 부름
    - 예시
      - `r* = {p∈Q | p<r} (r∈Q)`
      - `a = {p∈Q | p≦0} U {p∈Q | 0<p, p^2<2}`
        - 데데킨트 절단으로 루트2를 나타낸 것
        - 이 a가 절단임을 보이자
  - 절단의 오른쪽
    - 절단a에 대하여 `a^c = Q\a`라 두면, 다음이 성립
      - `p∈a, q∈a^c => p<q, r∈a^c, r<s => s∈a^c`
    - `a, a^c`는 Q를 수직선 위의 점들로 생각하면 왼쪽과 오른쪽으로 분할
      - 왼쪽 집합은 (절3)에 의하여 최댓값을 가지지 않는 것으로 간주
- R에 대한 구조 구성
  - 순서관계
    - 데데킨트 절단으로 구성된 R에 순서관계를 부여하고, 순서공리를 만족함을 증명
      - 두 절단 a,b에 대하여
        - `a≦b <=> a⊆b`
        - `a<b <=> a⊂b`
      - 임의의 실수 `a,b∈R`에 대하여 다음중 한 명제가 성립하고 두 명제가 동시에 성립하지 않음
        - `a>b, a=b, a<b`
          - *데데킨트 절단은 반드시 하나의 수를 기준으로 왼쪽 오른쪽으로 분할하는가?? 데데킨트 절단의 성질만으로 증명 가능한가?*
        - `Pr = {a∈R | a>0*}`
        - 위의 정리는 (체순2) 및 (체순3)이 성립함을 말해줌
          - `a>0, a=0, a<0` 세 부류의 절단집합으로 나눌 수 있으니까
      - 데데킨트 절단으로 구성된 R이 완비성공리를 만족함을 증명
        - **비어 있지 않은 집합 `A⊆R`가 위로 유계이면 A는 상한을 가진다**
  - 연산
    - 개요
      - 데데킨트 절단으로 구성된 R에 덧셈과 곱셈연산을 부여하고, 체공리를 만족함을 증명
        - 연산을 정의할 때에는 닫혀있는지 꼭 확인
    - 덧셈
      - `a+b = {s+t∈Q | s∈a, t∈b}`
        - 결합법칙
        - 항등원
        - *역원*
          - `a∈R에 대하여, b = {p∈Q | r>p, -r!∈a 인 r∈Q가 존재}`
            - 수직선 위에 그려보면 어떤 집합인지 파악하기 용이
          - *역원이 데데킨트 절단임을 증명 / a+b=0임을 보이기가 이해가 안됨*
        - 교환법칙
    - 곱셈
      - `∀a,b∈Pr, ab = {p∈Q | ∃r∈a∩Pq, s∈b∩Pq s.t. p≦rs} (Pq는 Q의 양수집합)`
        - `ab = 0* U {rs | 0≦r∈a, 0≦s∈b}`
          - *어떻게 증명하지?*
      - `ab`의 정의
        - `0* (a = 0* or b = 0*)`
        - `-(-a)b (a∈-Pr, b∈Pr)`
        - `-a(-b) (a∈Pr, b∈-Pr)`
        - `(-a)(-b) (a∈-Pr, b∈-Pr)`
          - 위에서 양수의 곱셈만 정의 했으므로, 음수를 양수로 변환 후(덧셈에 관한 역원) 곱셈을 계산하고 다음으로 전체의 역원을 구함
      - 연산법칙
        - 결합법칙
        - 항등원
          - `1*`가 항등원임을 보여야 함
        - *역원*
          - `a∈Pr에 대해서, r = 0* U {0} U {q∈Pq | r>q, 1/r!∈a 인 r∈Pq이 존재한다}`
        - 교환법칙
        - (덧셈과 곱셈의) 분배법칙
- 데데킨트절단 기반 실수체계에 유리수체계를 편입(embedding)
  - `φ: Q -> R, φ(r) = r*`
    - `r* = {q∈Q | q<r}`
      - `φ(-r) = -φ(r)`
  - φ는 monomorphism
    - `φ`는 단사사상
    - `φ(r+s) = φ(r)+φ(s)`
    - `φ(rs) = φ(r)φ(s)`
      - 환준동형사상
    - `r <= s ⇒ φ(r) <= φ(s)`
      - 순서보전사상

#### ② 코시 수열과 실수

코시수열의 시각화

![](./images/ns_cauchy_sequence.png)

- 용어 설명
  - 수열
    - `x: N -> X`
      - X의 수열
  - 수렴
    - `순서체 F의 수열 x: N -> F, a∈F, ∀e∈P_F(임의의 양수 순서체의 집합), ∃n∈N s.t. i≧n => |x(i)-a| < e`
      - x가 `a∈F`로 수렴
      - `∀`기호가 `∃`기호보다 명제에서 먼저 위치함에 주의. 즉 임의의 순서체의 원소 e에 따라서 위의 명제를 만족하는 자연수 n이 존재하면 그것이 수렴
  - 코시 수열
    - 개요
      - `∀e∈P_F, ∃n∈N s.t. i,j≧n => |x(i)-x(j)| < e`
  - 기본열
    - 유리수의 코시 수열
    - e.g
      - `∀r∈Q, r*(i)=r, i∈N => r*은 기본열`
        - `r*: N -> Q`
  - 유계수열
    - `순서체 F의 수열 x, ∃M∈F, ∀i∈N |x(i)|≦M`
- 정리
  - 순서체 F의 수열 `x: N -> F`가 수렴하면 코시 수열이다. 또한, 임의의 코시 수열은 유계이다.
    - *임의의 코시 수열은 유계이다* 라는 명제 증명?
- 코시수열로 R을 구성
  - `a ~ b <=> (i>n => |a(i)-b(i)|<e (a,b는 기본열, e>0인 임의의 유리수)) 인 n을 잡을 수 있다`
    - 동치관계
  - 실수
    - R = `F/~`
      - R의 원소들(`[a], [b]`)을 실수라 함
- R에 대한 구조 구성
  - 순서관계
    - `[a]>[b] <=> ∃d∈Pq, ∃N∈N, i≧N, a(i)-b(i)>d`
      - *well-defined?*
    - 임의의 실수 `[a],[b]∈R`에 대하여 다음 중 한 명제가 성립하고, 두 명제가 동시에 성립하지 않는다
      - `[a]>[b], [a]=[b], [a]<[b]`
        - *증명*
    - `Pr = {[a]∈R | [a]>0*}`
      - *\[0\*\] 이어야 하는 것 아닌가?*
  - 연산
    - 덧셈(`+`)
      - 정의
        - `[a]+[b] = [a+b], a+b: N -> Q, (a+b)(i)=a(i)+b(i)` *well-defined?*
          - `a+b`가 기본열임을 보여야 함
      - 연산법칙
        - 결합법칙
        - 항등원
          - `0*`
            - *\[0\*\]이 아니라, 왜 0*이 항등원이 되는것인가?*
        - 역원
          - a에 대한 역원 `-a: N -> Q, (-a)(i) = -(a(i))`
            - *\[a\]가 실수인데, 왜 a에 대한 역원이라는 표현을 사용하는지?*
        - 교환법칙
    - 곱셈(`x`)
      - 정의
        - `[a][b] = [ab]`
      - 연산법칙
        - 결합법칙
        - 항등원
          - `1*`
        - 역원
          - a에 대한 역원 `b: N -> Q, b(i) = 1/a(i)`
            - *기본열의 유한개의 항을 바꾸어도 그 동치류는 변하지 않음을 증명*
            - 위로 유계이며 비어있지 않은 자연수의 집합은 최대 원소를 갖는다
        - 교환법칙
- 기타 정리 & 개념
  - `[a],[b]∈R, ([a]>[b] => ∃r∈Q, [a]>[r*]>[b])`
  - 부분수열
    - 정의
      - 함수 `i: N -> N, i(k)<i(k+1) (k∈{0}UN)`에 대하여 함수와 수열의 합성`x◦i: N -> F (x: N -> F)`를 부분수열 이라고 함
      - 순서체 F의 수열 x가 `a∈F`로 수렴하면, x의 모든 부분수열이 a로 수렴함은 자명
    - 도움정리
      - 순서체 F의 코시 수열 x의 한 부분수열 `x◦i`가 점 `a∈F`로 수렴하면 x도 `a∈F`로 수렴한다
  - *`n∈N, [an]∈R`이고, `f: N -> R, f(n)=[an]`이 R의 코시수열이라면, 이 수열은 R안에서 수렴한다*
    - 증명이 어려움
- 코시수열 기반 실수체계에 유리수체계를 편입(embedding)
  - `φ: Q -> R, φ(r) = [r*]`
    - `r*: N -> Q, r*(i) = r`
  - φ는 monomorphism
    - `φ`는 단사사상
    - `φ(r+s) = φ(r)+φ(s)`
    - `φ(rs) = φ(r)φ(s)`
    - `r <= s ⇒ φ(r) <= φ(s)`
      - 순서보전사상
      - *`r∈Pq <=> r\*∈Pq`*
        - 과 동치인가?

### 완비순서체

위의 두가지 실수의 구성 방법의 결과가 사실상 같음

- 완비순서체의 정의
  - 순서체 F가 다음 성질을 가지면 완비순서체라 한다
    - (완1) `A!=φ, A⊆F가 위로 유계 => A는 상한을 가짐`
    - (완2) `A!=φ, A⊆F가 아래로 유계 => A는 하한을 가짐`
    - (완3) 임의의 코시 수열 `x: N -> F`가 F안에서 수렴한다
- 완비순서체의 성질
  - *완비순서체 F는 아르키메데스 성질을 만족한다.*
  - `x,y∈F(완비순서체), x<y => ∃r∈Q(⊆F), x<r<y`
