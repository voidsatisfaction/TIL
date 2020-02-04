# 6. 행렬식

- 의문
- Alternating Multilinear Form
- Symmetric Group

## 의문

## 6.1 Alternating Multilinear Form

- k-linear form
  - 정의
    - `V1, ..., Vk`가 벡터공간일 떄, 함수 `mu: V1 x ... x Vk -> F`가 모든 k개의 좌표에 대하여 linear 일 때, 즉, 임의의 `i = 1, ..., k`에 대하여 `mu(..., aui+bwi, ...) = a・mu(..., ui, ...) + b・mu(..., wi, ...) (ui, wi∈Vi, a,b∈F)`
      - 일반적으로 `V1 = ... = Vk = V`인 경우를 다루고, 이때의 `mu`를 k-linear form on V라 함
- alternating k-linear form
  - 정의
    - `V`가 벡터공간이고 `mu: V x ... x V -> F`가 k-linear form 이라고 하자. `∀v∈V, mu(..., v, ..., v, ...) = 0`를 만족
  - 성질
    - `mu: V x ... x V -> F`가 k-linear form 일 때, `∀v,w∈V, mu(..., v, ..., w, ...) = -mu(..., w, ..., v, ...)`
- 정리
  - **`det(In) = det(e1, ..., en) = 1`을 만족하는 alternating n-linear form `det: F^n x ... x F^n -> F`는 존재하고 유일하다. `det(A) = |A|`의 표기법도 사용한다**
    - `n=2`인 경우
    - `n=3`인 경우
- **결국 det가 존재하고 유일하다는 것** 을 보이는 것이 이번 장의 목표이며, 이를 보이기 위해서는 `det(e1, ..., en)` 과 같은 값을 분석할 수 있어야 한다. 여기서 det는 alternating n-linear form이므로, `det(e1, ..., ej, ..., ei, ..., en) = -det(e1, ..., ei, ..., ej, ..., en) = -|In| = -1 (by det의 정의)` 인 것을 효율적으로 보여줄 수 있어야 하며, 이를 가능하게 하는 것이 **symmetric group** 이다.

## 6.2 Symmetric Group

### Symmetric group

- 정의
  - `σ: {1, ..., n} -> {1, ..., n}`전체의 집합을 Tn으로 표기할 때, `Sn = { σ∈Tn | σ는 bijection }`
    - symmetric group의 원소는 permutation이라 부름
- 특징
  - `|Tn| = n^n, |Sn| = n!`

### Cycle notation

symmetric group의 다른 표현(그냥 함수의 대응을 눕혀서 나타낸 것)

![](./images/ch6/symmetric_group_expression1.jpeg)

cycle notation / transposition

![](./images/ch6/cycle_notation1.jpeg)

- 관찰
  - ① `σ`와 `τ`가 disjoint cycle => `σ◦τ = τ◦σ`
  - ② 임의의 permutation은 disjoint cycle들의 합성으로 나타낼 수 있고, 그 방법은 (합성의 순서를 제외하고) 유일하다
  - ③ `∀permutation`은 transposition들의 합성으로 나타낼 수 있다
    - `(i1, ..., ik) = (i1,ik)◦(i1,ik-1)◦...◦(i1,i3)◦(i1,i2)`
- 정의
  - 함수 `sgn: Sn -> {1, -1}, sgn(σ) = (-1)^r (단 σ는 r-개 transposition의 합성)`
    - *well-defined임을 증명*
      - but 주어진 permutation을 transposition들로 나타내는 방법은 여러가지가 있을 수 있으므로, well-defined가 아직 아니며,
      - `σ`를 transposition의 합성으로 나타낼 때 그 개수의 홀짝 여부가 불변이라는 것을 증명해야 함
  - even permutation & odd permutation
    - `σ∈Sn, sgn(σ)=1 => σ는 even permutation ∧ sgn(σ)=0 => σ는 odd permutation`
  - alternating group
    - `An = {σ∈Sn | sgn(σ)=1}`
- **symmetric group** 의 다른 관점
  - **permutation matrix**
    - 정의
      - `I_σ = [I]_Bv^Bv_σ`
        - `Bv = {v1, ..., vn}`이 V의 ordered basis ∧ `σ∈Sn`, 새로운 ordered basis `Bv_σ = {v_σ(1), ..., v_σ(n)}`을 생각하자.
        - 이 때, (nxn) transition matrix `[I]_Bv^Bv_σ`를 `σ`에 대응하는 permutation matrix라 부름
    - 예시
      - `σ=(1,3,2), I_σ = 1번째열을 3번쨰 열의 값으로 치환 ∧ 2번째 열을 1번째 열의 값으로 치환 ∧ 3번째 열을 2번째 열의 값으로 치환`
        - `(t(0,0,1) t(1,0,0) t(0,1,0))`
    - 성질
      - `σ=(i,j) => I_σ = I_[i]<->[j]`
        - i열과 j열 자리 바꾸기
    - 관찰(`σ,τ∈Sn`)
      - ① I_σ의 j-th column은 `e_σ(j)`즉, `I_σ = (e_σ(1), ..., e_σ(n))`
      - ② `A∈Mnxn(F) => A・I_σ = ([A]^σ(1), ..., [A]^σ(n))`
      - ③ `I_σ・I_τ = I_σ◦τ`
      - ④ `(I_σ)^-1 = I_(σ^-1) = t(I_σ)　∴I_σ ∈ O(n) (O(n)은 orthogonal group)`
      - ⑤ `I_σ = I_τ => σ = τ`
      - ③, ④, ⑤ 는 **symmetric group Sn과 Mnxn(F)의 subset `{I_σ ∈ Mnxn(F) | σ∈Sn}`이 곱셈에 관하여 같은 구조** 를 갖고 있음을 말하고 있음
        - *곱셈에 대한 같은 구조라는게, 곱셈에 대하여 bijection인 isomorphism이 존재한다는 것인가?*
        - 행렬과 선형사상이 같은 것이라면, permutation에 대응하는 선형사상도 있어야 할 것
  - **permutation operator**
    - 정의
      - `Bv = {v1, ..., vn}`이 V의 고정된 ordered basis이고, `σ∈Sn`일 때
      - Linear Extension Theorem을 이용하여, 선형사상 `P_σ: V -> V`를 `P_σ(vi) = v_σ(i) (i=1, ..., n)`인 `P_σ`
    - 주의
      - `P_σ`는 ordered basis `Bv`의 선택에 dependent함
    - 관찰(`σ,τ∈Sn`)
      - ① `[P_σ]_Bv^Bv = I_σ`
      - ② `P_σ◦P_τ = P_(σ◦τ)`
      - ③ `(P_σ)^-1 = P_(σ^-1)`
      - ④ `P_σ = P_τ => σ = τ`
  - 결론
    - *symmetric group `Sn`과 permutation matrix, permutation operator 는 모두 곱셈에 관하여 같은 구조를 갖고 있음을 알 수 있다*
      - 같은 구조가 뭔데?
- `L∈L(V,V)`일 때, `[L]_Bv^Bv`와 `[L]_Bvσ^Bvσ`를 비교해 보자 (`Bv = {v1, ..., vn}`이 V의 ordered basis이고, `σ∈Sn`)
  - ① `[L]_Bvσ^Bvσ = [I]_Bvσ^Bv・[L]_Bv^Bv・[L]_Bv^Bvσ = (I_σ)^-1・[L]_Bv^Bv・I_σ`
  - ② `σ = (1,2)∈S3, [L]_Bv^Bv = (aij) (aij∈F), [L]_Bvσ^Bvσ = [L]_Bv^Bv`를 첫번째 열과 두번째 열을 바꾸고, *첫번쨰 행과 두번쨰 행을 바꾼 것과 같음* (행과 열의 변환은 순서 상관 없음 - 결합법칙)
  - ③ `[L]_Bv^Bv = diag(λ1, λ2, λ3) (λi∈F) => [L]_Bvσ^Bvσ = diag(λ2, λ1, λ3) = diag(λσ(1), λσ(2), λσ(3))`
    - `λi∈F, (i,i)-성분이 λi인 (nxn)-대각행렬을` `diag(λ1, ..., λn)`으로 표기한다
    - *`ai∈F ∧ σ∈Sn, diag(a1, ..., an) ~ diag(a_σ(1), ..., a_σ(n))`임을 증명*
      - 여기에서 `~`기호는 무엇을 뜻하는가?

## 6.3 Determinant의 정의 1

*매우 어려운 구간*

**`det(In) = det(e1, ..., en) = 1`을 만족하는 alternating n-linear form `det: F^n x ... x F^n -> F`는 존재하고 유일하다.** 의 증명을 해보자!!

- 구체적 예시
  - `A = M3x3(F), det(A) = det(a11e1+a21e2+a31e3, a12e1+a22e2+a32e3, a13e1+a23e2+a33e3) = a11det(e1, ...) + a21det(e2, ...) + a31det(e3, ...) (∵ det is n-linear form)`
  - `(e3, e2, e4, e1) -> (e3, e2, e1, e4) -> (e1, e2, e3, e4)`
    - determinant의 논의 에서나온 위의 분석
    - `σ = (1, 3, 4), (1,3)◦((1,4)◦σ) = id` or `σ = (1,4)^-1◦(1,3)^-1 = (1,4)◦(1,3)` 이고
    - 따라서 `det(e3, e2, e4, e1) = (-1)^2・det(I) = sgn(σ)・det(I) = 1`
      - *여기에서 `det(e3, e2, e4, e1)`이 도출된 배경은?*
- 관찰
  - ① `D: Mnxn(F) -> F`가 위의 정리의 조건을 만족한다면, `A∈Mnxn(F)`이고 `σ∈Sn`일 때, 다음이 성립
    - *`D([A]^σ(1), ..., [A]^σ(n)) = sgn(σ)・D([A]^1, ..., [A]^n) = sgn(σ)・D(A)`*
    - *이거 왜죠?*
  - ② `D(e_σ(a), ..., e_σ(n)) = sgn(σ)`
- 정리
  - `det: Mnxn(F) -> F`는 다음과 같이 주어진다
    - `det(A) = |A| = det(aij) = sigma_{σ∈Sn}{sgn(σ)・a_σ(1),1・a_σ(2),2 ... a_σ(n),n}`
      - 애초에 이건 어떻게 증명? - 일단 3x3 matrix까지는 손으로 해봤으나...
        - 그 증명이 바로 옆 페이지에 나옴(꿀잼)
        - 그러니까 귀납적(혹은 직관적 혹은 천재적?!)으로 미리 `det`의 식을 예측하고 이 식이 `det`의 조건을 만족함을 보인 후에, uniqueness를 보이는 식으로 전개
