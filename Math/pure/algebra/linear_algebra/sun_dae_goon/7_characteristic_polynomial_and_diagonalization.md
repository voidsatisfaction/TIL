# 7. 특성다항식과 대각화

- 7.1 Eigen-vector와 Eigen-value
- 7.2 Diagonalization
- 7.3 Caley-Hamilton Theorem
- 7.4 Minimal Polynomial
- 7.5 Direct Sum과 Eigen-space Decomposition

## 의문

## 7.1 Eigen-vector와 Eigen-value

- eigen-value, eigen-vector
  - `A∈Mnxn(F), ∃λ∈F ∧ ∃0≠X∈F^n AX = λX => X는 eigen-value λ를 갖는 A의 eigen-vector`
  - `L∈L(V,V), ∃λ∈F ∧ ∃0≠v∈V L(v) = λv => v는 eigen-value λ를 갖는 L의 eigen-vector`
  - 위의 두 정의는 우리의 철학이므로 그것을 하나로 합쳐도 됨(같은것은 정말 똑같다)
  - `T∈LM, ∃λ∈F ∧ ∃0≠v∈V Tv = λv => v는 eigen-value λ를 갖는 T의 eigen-vector`
    - `T∈LM => (T∈L(V,V) ∨ T∈Mnxn(F)) ∧ dimV = n ∧ I_V = I_n = I ∧ V≠0`
    - 어차피 둘이 같은거면, 그냥 하나로 치자
- 정리
  - `T∈LM ∧ v가λ에 대응하는 T의 eigen-vector일 때 다음이 성립`
    - `T가 invertible <=> 0이 T의 eigen-value가 아님`
    - `T가 invertible <=> v는 λ^-1에 대응하는 T^-1의 eigen-vector이다 (λ≠0)`
  - 선형미분 방정식의 출발점
    - `λ∈R, e^(λx)들은 differential operator D:C^∞(R) -> C^∞(R)의 eigen-vector임을 보여라`
- `주어진 T∈LM의 eigen-vector와 eigen-value찾기`
  - `Tv = λv`
  - `=> λv - Tv = 0`
  - `=> (λI-T)v = 0`
  - `=> det(λI-T) = 0`
    - 우리에 철학에서는 같은 것은 같으므로, `L∈L(V,V)의 determinant역시 존재하며, 대응하는 행렬의 determinant일 것`
- `L∈L(V,V)`의 determinant
  - `det(L) = det([L]_Bv^Bv) (Bv는 V의 임의의 기저)`
    - 이것은 well-defined 되어있음
    - similar matrix의 invariant(similar한 matrix의 공유하는 성질)
      - determinant
- 특성다항식(characteristic polynomial)
  - `T∈LM ∧ T혹은 [T]_Bv^Bv의 좌표를 aij로 표기할 때, T의 특성다항식 φ_T(t)∈F[t]를 φ_T(t) = det(tI-T) (t는 마치 scalar 인 것으로 생각)`
    - similar matrix의 invariant이므로, `L∈L(V,V)`까지 고려해도 well-defined
  - `T∈LM일 때, λ∈F가 T의 eigen-value <=> φ_T(λ) = 0`
    - `λI-T가 not invertible => ∃v∈V, v≠0 ∧ (λI-T)v = 0`
      - dimension theorem을 이용한 증명
      - RREF를 이용한 증명
- similar matrix의 invariant
  - isomorphic
    - rank
  - etc
    - determinant
    - characteristic polynomial
    - eigen-value
    - Trace
- eigen vector, eigen value 찾기
  - `F=R, F=C`어느쪽이냐에 따라서, characteristic polynomial의 root 개수가 달라지고, 이는 diagonalization에 큰 영향을 끼침
- Fundamental Theorem of Algebra
  - `모든 non-constant polynomial f(t)∈C[t]는 (C에서) 근을 갖는다. (즉, 인수정리에 의해, f(t)∈C[t]는 C-위의 일차식들의 곱으로 인수 분해 된다)`
- 보기
  - `φ_I(t) = (t-1)^n 이고, I는 eigen-value 1을 갖는다. 그리고 F^n의 모든 non-zero vector들이 eigen-vector가 된다`

## 7.2 Diagonalization

- 배경
  - Diagonalizable matrix를 정의하고, 우리의 철학에 의해서 diagonalizable linear operator도 저절로 정의됨
- diagonalizable matrix
  - `A∈Mnxn(F) s.t. ∃D∈Mnxn(F), D는 diagonal ∧ A~D`
- `A∈Mnxn(F)`일 때, 다음은 동치
  - `A가 diagonalizable`
  - `A의 eigen-vector들로 이루어진 F^n의 basis가 존재`
- diagonalizable linear operator
  - `L이 diagonalizable <=> ∃Bv∈V, Bv는 V의 기저 ∧ [L]_Bv^Bv가 diagonalizable matrix`
- diagonalizable
  - `T∈LM, T가 diagonalizable <=> ∃Bv∈V, Bv는 V의 기저 ∧ [T]_Bv^Bv가 diagonalizable matrix`
  - diagonalizability의 충분조건 하나
    - `T∈LM, φ_T(t)가 F에서 서로 다른 n개의 root를 가짐(n개의 eigen-value가 서로 다름) => T는 diagonalizable (dimV = n)`
    - `<=> T∈LM, v1, ..., vk가 T의 eigen-vector, vi의 eigen-vector λi들이 mutually distinct(λi≠λj if i≠j) => {v1, ..., vk}는 일차독립`
  - `A = (1 1; 0 1)`은 절대로 diagonalizable하지 않음
    - 만약, diagonalizable하다면, `A ~ I2`인데, `I2`는 오직 `I2`와만 similar
    - diagonalizability의 필요충분조건은 무엇일까?
    - diagonalizability를 말해주는 invariant는 무엇일까?
  - `T∈LM늬 diagonalizability를 결정해주는 invariant는 무엇인가?`

## 7.3 Caley-Hamilton Theorem

- 정의
  - `T∈LM, I_T = {f(t)∈F[t] | f(T) = 0}`
- `T∈LM => I_T ≠ {0}`
- Caley-Hamilton Theorem
  - `T∈LM => φ_T(T) = 0 (φ_T(t)∈I_T)`
    - 어거지 증명(잘못됨)
      - `φ_T(t) = det(t・I - T)`
      - `=> φ_T(T) = det(T・I - T) = det(0) = 0`
        - **`φ_T(t)의 계산은, det(t・I - T)∈F[t]를 전개해서 t에 대하여 evaluate를 해야함`**
    - Quotient space와 triangularization을 이용한 증명
    - T-cyclic subspce를 이용한 증명
    - Adjoint matrix를 이용한 증명
- 그 다음 motivation
  - `g(t)∈F[t], g(t) = φ_A(t)q(t) + r(t)`
    - `q(t)`는 몫, `r(t)`는 나머지
    - `g(A) = r(A)`
  - `A = (1, 0, 1; 0, 3, 0; 0, 0, 3)`
    - `=> φ_A(t) = (t-1)(t-3I)^2`
    - `=> φ_A(A) = (A-1)(A-3I)^2 = 0`
    - `=> (A-1)(A-3I) = 0`
    - `m(A)=0`인 최소 차수 다항식 `m(t)`찾기

## 7.4 Minimal Polynomial

## 7.5 Direct Sum과 Eigen-space Decomposition
