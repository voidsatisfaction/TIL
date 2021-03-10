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

## 7.3 Caley-Hamilton Theorem

## 7.4 Minimal Polynomial

## 7.5 Direct Sum과 Eigen-space Decomposition
