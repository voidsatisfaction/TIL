# 기저와 차원

- pre
  - 의문
  - 개요
- Linear Combination
  - 일차결합
  - 생성
- 일차독립과 일차종속
  - 일차독립
  - 정리(동치조건)
- Vector Space의 basis
  - 기저
  - 표준기저
  - 기저 B에 관한 v의 좌표
  - `A = (aij)∈Mnxn(F)가 가역 ∧ {v1,...,vn} = Bv(V의 기저) ∧ wj = sigma_i=1^n{aijxvi} (j=1,...,n) => Bv = {w1,...,wn}`
  - 일차결합 일차독립 연립방정식 과의 관계
- Basis의 존재
- Vector Space의 dimension

## 의문

- *일차 독립의 정의에서 `S = φ`인 경우는 항상 일차 독립인가?*
- *어떠한 벡터의 집합의 일차 독립을 판별할 때, 해당 집합과 isomorphic한 집합의 일차 독립성을 판별해서 판단해도 상관없는가?*

## 개요

벡터 공간이 다른 대수적 구조보다 좋은 점은 기저를 갖고 있다는 것 -> 그래서 벡터공간을 다른 대수적 구조보다 먼저 배움 -> 기저를 갖고 있으면 다루기 쉬움

## 3.1. Linear Combination

- 일차결합(F-linear combination)
  - 정의
    - `{v1,...,vn}`의 일차결합
      - `v1,...,vn∈V, a1v1+a2v2+...+anvn = sigma_i=1^n{aivi} 꼴의 벡터, (단, a1,...,an ∈ F)`
    - `S⊆V, (S가 무한집합인 경우), v∈V`가 S의 일차결합
      - `≡ ∃S0⊆S, v = sigma_i=1^n{aivi}, (단, v1,...,vn ∈ S0)`
    - 공집합의 일차결합 전체의 집합은 `{0}`
- 생성
  - `<S>`
    - `S⊆V, S를 포함하는 가장 작은 V의 subspace`
      - `S⊆<S>≦V`
      - `S⊆W≦V => <S>≦W`
    - S가 생성한 부분공간
  - `S⊆V, <S> = ∩(S⊆W≦V) W`
    - `<S>`의 존재성 / 유일성 증명
    - W의 집합족의 첨수집합 I≠φ
    - `S≠T`이어도, `<S> = <T>` 인 경우가 존재
  - `S⊆V, <S> = span(S)`
    - `<S> ⊆ span(S)`
    - `span(S) ⊆ <S>`

## 3.2 일차독립과 일차종속

일차결합, 일차독립, 일차종속의 개념 속에는 일차 연립방정식이 항상 숨어있음

**어떠한 정의를 분석할 때, 항상 well-defined인지 확인해야 함**

- 일차독립(F-linearly independent)
  - ① 유한집합 `{v1,...,vn}⊆V`가 다음 조건(`단, ai∈F`)을 만족하면 `{v1,...,vn}`을 일차독립인 부분집합이라고 부른다
    - `a1v1+a2v2+...+anvn = 0 => a1 = a2 = ... = an = 0`
  - ② `φ ≠ S ⊆ V`, S가 일차독립이면 S의 모든 (non-empty) finite subset이 일차독립.
    - well-defined이려면, 유한집합 S가 일차독립이면, S의 모든 non-empty subset이 일차독립임을 보여야 함
  - ③ `φ ≠ S ⊆ V`, S가 일차독립이 아니면 일차종속(F-linearly dependent)이라고 말함
- 정리
  - `{v1,...,vn}⊆V` 일 떄, 다음 세 조건은 동치
    - `{v1,...,vn}` 일차독립
    - `{v1,...,vn}` 의 일차결합으로 zero vector 0을 표현하는 방법은 하나 - `0v1 + ... + 0vn = 0` 뿐
    - `∃v∈V ∧ v가{v1,...,vn}의 일차결합으로 표현 => 그 표현법은 하나뿐`

## 3.3 Vector Space의 Basis

- 기저
  - 정의
    - `V가 vector space ∧ Φ≠B⊆V`에 대해서 다음을 만족하면 B를 V의 기저라고 함(basis, F-basis)
      - ① `<B> = V`
      - ② `B는 일차독립`
  - 정리
    - 다음 조건은 동치
      - B는 V의 basis이다
      - V의 모든 vector는 B의 linear combination으로 표현할 수 있고, 그 표현법은 하나뿐이다.
- 표준기저
  - 정의
    - i번쨰 좌표만 1이고 나머지는 0인 표준단위벡터 `ei∈F^n, ε = {e1,...,en}`는 F^n의 기저, 특히 표준기저임
      - `∵ t(a1,...,an) = a1e1 + a2e2 + ... + anen`
- 기저 B에 관한 v의 좌표
  - 정의
    - 유한 집합 `B = {v1,...,vn}`이 V의 F-basis라고 하자.
    - `v∈V, v = a1v1 + a2v2 + ... + anvn`으로 표현될 때,
    - `t(a1,...,an)∈F^n`를 기저 B에 관한 v의 좌표 라고 부르고
    - `[v]B = t(a1,...,an)`으로 표기함
  - 주의
    - `B = {v1, ..., vn}`는 순서가 고정된 기저(ordered basis)
      - 일반적으로 기저라는 용어는, 순서가 고정된 기저를 의미
  - 보기
    - `X∈F^n => [X]ε = X`
    - `B = {v1,...,vn}`이 V의 basis라고 할 때 다음이 성립
      - `v,w∈V, [v+w]B = [v]B + [w]B`
      - `v∈V, a∈F, [av]B = a[v]B`
    - 예제
      - `{v,w}`가 V의 일차독립인 부분집합일 떄, `{v,w}`와 `{2v+5w, v+3w}`는 V의 subspace `<v,w>`의 basis가 된다.
- Vector space의 subspace도 벡터 공간이므로 basis를 생각할 수 있음
- `A = (aij)∈Mnxn(F)가 가역 ∧ {v1,...,vn} = Bv(V의 기저) ∧ wj = sigma_i=1^n{aijxvi} (j=1,...,n) => Bv = {w1,...,wn}`
  - 증명
    - 부분집합
    - 일차독립
    - span이 V임을 보임
      - Bv의 원소가 `{wj}`의 일차결합으로 나타낼 수 있다는 것을 보이면 충분
        - 그 이유는?
  - 특수 케이스
    - `A = (aij)∈Mnxn(F)가 가역 => {[A]^1,...,[A]^n} = BF^n(F^n의 기저)`
      - 앞 명제의 `V = F^n`, `vi = ei`
- 일차결합, 일차독립, 기저와 연립방정식의 관계
  - `A∈Mmxn(F),`
    - ① `{[A]^1,...,[A]^n}이 일차독립 <=> AX=0이 tirivial solution만을 갖음`
    - ② `<[A]^1,...,[A]^n> = BF^m(F^m의 기저) <=> ∀B∈F^m, AX = B 가 해를 갖음`
    - ③ `{[A]^1,...,[A]^n} = BF^m(F^m의 기저) <=> ∀B∈F^m, AX = B 가 unique solution을 갖음`
- basis가 무한인 경우
  - Polynomial space `F[t]`는 infinite basis `{t^i∈F[t] | i≧0}`를 갖음

## 3.4 Basis의 존재

- 배경
  - 주어진 vector space V의 basis를 찾기
- 과정
  - `V=0`이면 V는 basis를 갖지 않음
  - `V≠0 => ∃v1∈V, v1≠0`
  - if `<v1> = V => Bv = {v1}`
  - if `<v1> ≠ V => ∃v2, v2!∈<v1>`
    - `{v1, v2}는 일차 독립`
    - `<v1,v2> = V => {v1,v2} = Bv`
  - if `<v1,v2> ≠ V => ∃v3, v3!∈<v1,v2>`
    - ...
  - 위의 과정으로 V의 기저를 완성하지 못하더라도, 일차독립인 부분집합을 계속 확장할 수 있음
  - 무한 기저를 갖는 경우에는, 위의 과정을 유한번을 해서 기저를 찾을 수 없음
- 정리
  - `S⊆V`를 V의 일차독립인 부분집합이라고 하고, `v!∈S`일 때 다음조건은 동치
    - ① `SU{v}`는 일차독립
    - ② `v!∈<S>`
- **모든 non-zero vector space는 basis를 갖는다**
  - Zorn's Lemma의 결과
  - Axiom of Choice
    - Axiom은 true false의 문제가 아니라, 다른 axiom과 모순이 없기만 하면 된다.

## 3.5 Vector Space의 Dimension

- 차원 정의를 위한 준비
  - `Vector space V`가 basis B와 C를 가지면 `|B| = |C|(집합의 cardinality)`이다
    - `|B| < ∞`의 경우
      - 아래의 보조정리에 의하여 자명
    - `|B| = |C| = ∞`의 경우
      - 초한 귀납법(transfinite induction)이라는 논리학의 기술을 사용
  - `Vector space V`가 finite basis `B = {v1,...,vn}`를 갖는다고 하자. 이때, 만약 `C = {w1,...,wm}⊆V ∧ n<m => C는 linearly dependent`
- 정리
  - `A∈Mmxn(F), m<n => AX = 0이 non-trivial solution을 갖는다`
- 차원의 정의
  - ① 벡터공간 V가 F-basis B를 가질 때, B의 원소수(cardinality) `|B|`를 V의 차원이라 부르고, `dim_F{V} = dimV`로 표기한다.
    - `dim0 = 0`
  - ② `dimV`가 유한이면, 우리는 V를 유한 차원(finite dimensional) 벡터공간 이라고 부른다(무한이면 무한차원)
  - dimension이 well-defined되어 있으려면
    - 임의의 벡터공간은 기저를 갖고 있다
    - `B, C`가 영벡터공간이 아닌 임의의 벡터공간 V의 기저이면, `|B| = |C|`
- Basis Extension Theorem
  - S가 V의 linearly independent sub-set이면 S를 포함하는 V의 basis가 존재한다.
    - V의 subspace `<S>`의 basis S를 V전체의 basis로 확장할 수 있다는 뜻
    - 위의 정리가 모든 non-zero vector space가 basis를 갖는다는 정리를 포함
  - V가 f.d.v.s(finite dimensional vector space)이고, `W ≦ V`라고 하자. 만약 `{w1,...,wr}`이 W의 기저이면 이를 확장하여 V의 기저 `{w1,...,wr,v1,...,vs}`를 찾을 수 있다(단, s≧0)
- 정리
  - Non-zero vector space V의 subset S, `<S> = V => S에 포함되는 V의 기저가 존재`
- 따름정리
  - V가 f.d.v.s이고 `W≦V` 일 때,
    - W도 f.d.v.s이고, `dimW ≦ dimV`
    - `dimW = dimV => W = V`
  - `S⊆V ∧ |S| = dimV < ∞`이면 다음 조건은 동치이다
    - ① S는 V의 기저이다
    - ② S는 일차독립이다
    - ③ `<S> = V`
    - 의미
      - 차원과 같은 개수의 원소를 갖는 집합은 일차독립인 것이나 전체를 생서한다는 것 둘 중하나만 보여도 기저임을 확인할 수 있음

## 3.6 우리의 철학

- f.d.v.s의 dimension들
  - `dim F^n = n`
  - `dim Pn(F) = n+1`
  - *`C-vector space C^n`은 동시에 `R-vector space`로도 볼 수 있고, `dim_R C^n`*
  - `dim Mmxn(F) = mn = dim F^mn`
- isomorphism과 기저
  - `φ: V -> W`가 isomorphism일 떄, B가 V의 기저이면, `φ(B)`는 W의 기저이고, 따라서 `dimV = dimW`이다.
- 우리의 철학
  - ① 같은 것은 같다(isomorphism의 철학)
    - 이름만 다르고 사실상 같은 벡터공간은 그 '성질'이 같다
    - 성질
      - 덧셈과 상수곱에 의해 묘사되는 성질
      - `φ: V -> W`가 isomorphism이고 `S,T⊆V, V1,V2≦V`
        - `φ(S∩T) = φ(S)∩φ(T)`
        - `<S> ≠ V => <φ(S)> ≠ W`
        - `T가 일차독립이면, φ(T)도 일차독립`
        - `dim<S> = dim<φ(S)>`
        - `V = V1 + V2 => W = φ(V1) + φ(V2)`
        - **이러한 성질들을(일차종속, 일차독립, 기저, 차원 등) isomorphism에 의해 보존되는(invariant) 성질이라고 부름**
    - **벡터공간의 공부 = isomorphism에 의해 불변인 성질들의 공부**
    - isomorphism에 의해 보존되지 않는 성질들
      - V의 원소는 행렬들이다
      - V에는 수박이라는 벡터가 있다
      - 벡터 v의 길이는 3이다
      - 벡터 v,v를 곱하면 w이다
      - 벡터 v를 미분하면 w가 된다
      - **벡터의 길이나 곱셈등은 벡터공간의 성질이 아니다.**
  - ② 같은 것은 정말 똑같다(Identification의 철학)
    - 만약 이름만 다르다면, (강제로) 이름을 고쳐서 이름도 같게 만들면 된다.
    - 예시
      - `vw = φ^-1(φ(v)φ(w))` or `φ(vw) = φ(v)φ(w) (v,w∈R^4)`
        - 벡터의 곱셈을 우선 `φ`로 이름을 바꾸어 곱한(행렬의 곱셈) 후 다시 `φ^-1`로 이름을 바꾼 벡터를 `vw`로 정의하면 벡터의 곱셈을 말할 수 있음
        - 행렬 `M2x2(R)`의 곱셈구조를 `R^4`로 옮겨 놓았다고 말할 수 있음
    - 주의
      - 벡터공간 V와 W를 identify할 때는 어떤 isomorphism에 의해서 identify하고 있는지 분명히 밝혀야 함
  - **이러한 isomorphism의 철학과 identification의 철학을 자유자재로 구사할 수 있도록 훈련하라!**
