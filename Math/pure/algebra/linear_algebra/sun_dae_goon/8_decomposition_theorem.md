# 8. 분해정리

- 의문
- 정리
- 8.1 Polynomial
- 8.2 T-Invariant Subspace
- 8.3 Primary Decomposition Theorem
- 8.4 Diagonalizability
- 8.5 T-Cyclic Subspace
- 8.6 Cyclic Decomposition Theorem

## 의문

## 참고

- **Fundamental Theorem of Algebra**
  - `모든 non-constant polynomial f(t)∈C[t]는 (C에서) 근을 갖는다. (즉, 인수정리에 의해, f(t)∈C[t]는 C-위의 일차식들의 곱으로 인수 분해 된다)`

## 정리

## 8.1 Polynomial

- **인수분해(factorization)**
  - 개요
    - **곱이 정의된 집합내의 어떤 원소를 다른 원소들의 곱으로 표현하는 것**
      - 특히, 정수집합에서 어떤 주어진 정수를 소수들의 곱으로 표현하는 것은 소인수 분해라고 부름
      - e.g)
        - `15 = 3 x 5`
        - `x^2-4 = (x-2)(x+2)`
    - 대수적 오브젝트를 더 간단한 오브젝트의 곱으로 표현하는 방법
      - e.g)
        - 임의의 함수를 surjective함수와 injective함수로 합성해서 factor함
        - 행렬의 factorization
          - LUP factorization
  - 종류
    - integer factorization
      - multiplication은 쉬운데 역연산인 factorization은 알고리즘의 측면에서 효율적으로 구현하기 매우 어려움(RSA암호)
    - polynomial factorization
      - 개요
        - 인수분해는, polynomial의 root을 찾는 문제를 해당 polynomial의 factor들의 root를 찾는 문제로 환원시킴
        - F를 coefficient로 갖는 polynomial은 unique factorization property를 갖음
          - 이는 소인수 분해의 polynomial 버전
          - 소수 ~ irreducible polynomial
        - C를 coefficient로 갖는 polynomial은 unique factorization into linear polynomial을 갖게 함
    - matrix factorization
    - ...
  - 필요 지식
    - irreducible polynomial(기약 다항식)
      - 개요
        - degree가 1이상
          - `a∈F`는 기약다항식이라 부르지 않음
          - `~~ 소수에 1을 포함시키지 않는것과 같은 느낌`
        - 계수의 종류(`C`, `R` 등)에 따라서 기약 다항식의 범위가 달라짐
      - 특징
        - `C[t]`의 irreducible polynomial은 일차식 뿐
        - `R[t]`의 irreducible polynomial은 일차식과 이차식 뿐
          - 그 이유는, factorization의 정의로 부터, polynomial factorization은 `R[t]`의 원소의 곱으로 표현되야 되므로...
          - `α가 f(t) = a0t^n + an-1t^(n-1) + ... + a1t + a0 (a0, ..., an ∈ R)의 근 => f(!α) = 0 (!α는 α의 켤레복소수(conjugate))`
          - `t^2-(α+!α)t+α!α ∈ R[t]`
            - `α, !α를 근으로 갖는 이차식`
            - **여기에, 대수학의 기본정리를 적용하면, 임의의 non-constant polynomial은 C에서 근을 갖으므로 계속해서 인수 분해 가능**
    - *GCD(Greatest Common Divisor)의 성질*
      - *`f1(t), ..., fk(t) ∈ F[t]의 최대공약수를 d(t) => ∃g1(t), ..., gk(t)∈F[t] s.t d(t) = g1(t)f1(t) + g2(t)f2(t) + ... + gk(t)fk(t)`*
        - *이게 무슨 소리인지 사실 이해가 잘 안감*
    - relatively prime(서로 소)
      - `f1(t), ..., fk(t) ∈ F[t] 의 최대공약수가 1∈F[t] <=> f1(t), ..., fk(t)가 서로 소`
      - **생각해보면, 우리가 평소에 사용하는 소수라는 건 absolutely prime이구나...**
- `T∈LM, φ_T(t)와 m_T(t)의 F-위의 monic irreducible divisor(약수)의 집합은 같다`
  - 증명1: motivation
    - *표기상의 subtle한 문제란?*
    - `m_T(t)가 R-위에서 minimal polynomial일 때, C-위에서도 minimal polynomial일까?`
      - R-위에서 minimal polynomial인 경우, 이차식도 포함이 되는 경우도 있으므로 항상 그렇다고 할 수는 없는 것 아닌가
        - 그런 이야기가 아니고, minimal polynomial의 계수가 실수인지 복소수인지에 대한 이야기
  - 증명2: fancy하나, 덜 motivative
- 새로운 표기법
  - `f(t)∈F[t], f(t) = αnt^n + ... + α1t + α0 (α0, ..., αn ∈ C)`일 때
    - `!f(t)∈C[t], !f(t) = !αnt^n + ... + !α1t + !α0`으로 정의
  - `A = (aij)∈Mmxn(C)`일 때
    - `!A = (!aij) ∈ Mmxn(C)`
  - 관련 성질
    - `f(t),g(t)∈C[t], α∈C`
      - `!(f+g)(t) = !f(t) + !g(t)`
      - `!(αf)(t) = !α!f(t)`
      - `!(fg)(t) = !f(t)!g(t)`
        - 결국 두 다항식의 대응되는 계수끼리만 곱하는걸 생각하면 되므로...
    - `A,B∈Mmxn(C), C∈Mnxr(C), α∈C`
      - `!(A+B) = !A+!B`
      - `!(αA) = !α!A`
      - `!(AC) = !A!C`
      - `!(tA) = t(!A)`
      - 위의 다항식에 대한 성질과 얼추 비슷한 느낌
    - `A∈Mnxn(C)`
      - `det(!A) = !det(A)`
      - `m∈N => !(A^m) = (!A)^m`
      - `f(t)∈C[t] => !(f(A)) = !f(!A)`
      - `A가 invertible => !A가 invertible ∧ (!A)^-1 = !(A^-1)`

## 8.2 T-Invariant Subspace

선형변환을 적용하더라도, 변환 후의 벡터 공간의 범위가 기존의 벡터 공간을 넘지 않는 경우

원소의 개수 자체는 변할 수 있으나, 그 외의 '성질'들이 변하지 않는 부분 공간

- `W가 V의 T-invariant space(W는 T-stable)`
  - `T∈LM ∧ W≤V, T(W)≤W (결국, T(W)≤W≤V) (즉, T|w: W -> W가 의미가 있는 경우)`
    - *의미가 있다는게 무슨 의미인지*
    - `T∈Mnxn(F) => T = L_T, V=F^n으로 이해`
- 성질
  - `T∈LM, U,W가 V의 T-invariant subspace => U∩W 와 U+W도 T-invariant`
  - `T∈LM, W가 V의 T-invariant subspace, W의 기저 Bw를 V의 기저 Bv로 확장(Basis Extension Theorem)하면, [T]_Bv^Bv = ([T|w]_Bw^Bw *; 0 *)의 형태`
    - T|w의 characteristic polynomial은 T의 characteristic polynomial에 대한 결정적인 정보 제공
    - T|w의 minimal polynomial은 T의 minimal polynomial에 대한 큰 정보를 주지 못함
    - *T-invariant subspace를 생각하는 첫 번쨰 이유는, 무언가 T에 관해 알고 싶은 것이 있을 때, `dimV`에 관한 귀납법을 사용할 수 있을 것이라는 idea때문 이라고 할 수 있다*
      - 왜지?
  - *triangularization의 엉터리 귀납법*
    - *이해가 지금은 잘 안된다*
- 활용
  - **block diagonal matrix로의 decompose(분해)**
    - `T∈LM, U,W가 T-invariant subspace, V=U⊕W, Bu, Bw는 U,W의 basis`
      - `=> Bv = Bu ∐ Bw`
      - `=> [T]_Bv^Bv = ([T|u]_Bu^Bu 0; 0 [T|w]_Bw^Bw)`
        - `[T]_Bv^Bv는 block diagonal matrix`
      - `=> φ_T(t) = φ_T|u(t)・φ_T|w(t) ∧ m_T(t) = l.c.m(m_T|U(t), m_T|w(t))`
      - 이 논의를 k-개의 T-invariant subspace들의 direct sum인 경우로 확장하면?
    - **그런데, 이 성질을 사용하려면, T-invariant subspace 이면서, direct sum으로 분해 가능한 V의 Subspace를 찾아야 하는데, 이는 어떻게 가능한가?**
      - primary decomposition theorem
- 성질2
  - `T∈LM, f(t)∈F[t]일 때`
    - **`kerT, imT는 T-invariant`**
      - `∃v∈V, s.t w = Tv`
    - **`kerf(T), imf(T)는 T-invariant`**
  - `T∈LM, W가 V의 T-invariant subspace => ∀f(t)∈F[t], W는 f(T)-invariant subspace`
  - `T∈LM, λ∈F => T의 eigen-space VT,λ는 T-stable`
    - primary decomposition theorem의 기반
  - `T∈LM, W≤V가 T-stable subspace =>`
    - `∀f(t)∈F[t], f(T|w) = f(T)|w`
    - `g(t)∈F[t], W=kerg(T) => g(t)는 m_T|w(t)의 배수`
  - `S,T∈LM, ST = TS => kerS, imS 는 T-stable`

## 8.3 Primary Decomposition Theorem

임의의 행렬・선형사상의 characteristic polynomial과 minimal polynomial의 각 monic relatively prime polynomial의 항의 커널공간으로 분해가 가능

그러한 분해를 바탕으로 `[L]_Bv^Bv`를 적용하면 block diagonal형태로 만들 수 있음

- 표기법
  - `T∈LM, φ_T(t) = p1(t)^e1 ... pk(t)^ek, m_T(t) = p1(t)^f1 ... pk(t)^fk`로 F-위에서 인수 분해된다고 하자
    - `pi(t)들은 F[t]의 relatively prime monic irreducible polynomial ∧ 1≤fi≤ei`
      - `Wi = kerpi(T)^ei, Ti = T|wi (i=1, ..., k)`
- Primary Decomposition Theorem
  - `T∈LM`
    - `V = kerp1(T)^e1 ⊕ kerp2(T)^e2 ⊕ ... ⊕ kerpk(T)^ek`
    - `V = kerp1(T)^f1 ⊕ kerp2(T)^f2 ⊕ ... ⊕ kerpk(T)^fk`
    - 다음이 성립
      - `Wi = kerpi(T)^ei = kerpi(T)^fi`
      - `m_Ti(t) = pi(t)^fi`
      - `φ_Ti(t) = pi(t)^ei (dimWi = ei ・ deg(pi))`
  - 보조정리
    - `T∈LM, f(t),g(t)∈F[t]는 monic ∧ relatively prime, E(t) = f(t)g(t) ∈ I_T => V = kerf(T) ⊕ kerg(T)`
      - `E(t) = m_T(t) => m_T|u(t) = f(t) ∧ m_T|w(t) = g(t)`
      - `E(t) = φ_T(t) => φ_T|u(t) = f(t) ∧ φ_T|w(t) = g(t)`
  - 주의
    - similar matrix의 invariant
      - `φ_T(t), m_T(t) => pi(t), ei, fi => dimWi, m_Ti(t), φ_Ti(t)`
      - **`Wi`자체는 similar matrix의 invariant가 아님**
        - `Wi = kerpi(T)^ei ≠ kerpi(L)^ei`
- 연습문제
  - `A = (0 4 0 -2; 0 2 0 0; 0 -2 1 0; 1 0 1 3)`
    - `characteristic polynomial = (t-1)^2(t-2)^2`임을 보여라
    - `m_A(t)를 구하라`
    - `A`의 diagonalizability를 판정
    - `F^4`의 A에 관한 primary decomposition을 묘사하라
    - `primary decomposition`에 관한 `LA`의 행렬표현(block diagonal matrix의 형태)을 구하라

## 8.4 Diagonalizability

- `T∈LM, 이 diagonalizable <=> T의 minimal polynomial m_T(t)가 F위에서 일차식으로 인수분해됨 ∧ multiple root를 갖지 않음 = ∀i={1, ..., k}, deg(pi)=1 ∧ fi=1`
  - `T∈LM이 diagonalizable => eigen-space decomposition과 primary decomopsition은 같다`
    - 이미 7장의 direct sum 부분에서 `T가 diagonalizable <=> V가 eigen-space decomposition으로 이루어져 있음` 이 증명되어 있음
  - diagonalizability를 결졍해주는 invariant는 m_T(t)
  - 따름정리
    - `T∈LM, T가 diagonalizable ∧ W가T의 invariant subspace => T|w도 diagonalizable`
- 정의
  - `T,S∈LM, V의 하나의 기저 Bv에 관해 [T]_Bv^Bv 와 [S]_Bv^Bv가 모두 대각행렬이면 T,S가 simultaneously diagonalizable`
- 차원에 관한 귀납법을 사용하여 증명하는 명제
  - *`T,S∈LM, TS=ST, T,S는 diagonalizable => T,S는 simultaneously diagonalizable`*
  - 연습문제
    - *`I가 index set ∧ {Ti | i∈I} ⊆ LM, if ∀i≠j∈I, TiTj = TjTi ∧ Ti가 각각 diagonalizable => {Ti | i∈I}는 simultaneously diagonalizable`*

## 8.5 T-Cyclic Subspace

- T-cyclic space
 - `V는 T-cyclic space <=> T∈LM, ∃v∈V s.t V = {f(T)v | f(t)∈F[t]}`
   - `V = F[T]v = {f(T)v | f(t)∈F[t]}`
 - 성질
   - `Bv = {v, Tv, ..., T^(n-1)v}`
     - 증명
       - 애초에 `deg(m_T(t)) = n`임을 어떻게 가정할 수 있는가?
     - `V=F[t]v, g(t)∈F[t]가 g(T)v=0 => g(T)=0`
   - `φ_T = m_T`
     - `n = dimV = deg(φ_T) = deg(m_T)`
   - `[T]_Bv^Bv = m_T(t)에 대응하는 companion matrix`
 - 따름정리
   - `T∈LM, T가 companion matrix로 표현됨 => V는 T-cyclic`
     - T-cyclic vector space의 ordered basis와 `[T]_Bv^Bv`로 부터 나온 V의 ordered basis인 Bv가 같으면 둘은 같은 벡터공간
 - 연습문제
   - `ψ(t)∈F[t] (ψ(t)는 monic ∧ deg(ψ)≥1), ψ(t)를 characteristic polynomial로 가지는 행렬은?`
     - 존재성
     - 유일성
- T-cyclic subspace
  - `T∈LM, W는 V의 T-invariant subspace ∧ W가 (T|w)-cyclic <=> W는 V의 T-cyclic subspace`
- T-cyclic subspace와 T-invariant subspace의 연결
  - `T∈LM, 0≠w∈V, F[t]w = {f(T)w | f(t)∈F[t]} = <w, Tw, T^2w, ...>`
    - `F[t]w`는 V의 T-invariant subspace
    - `F[t]w`는 V의 T-cyclic subspace
    - *`F[t]w`는 w를 포함하는 V의 가장 작은 T-invariant subspace*
- T-cyclic subspace of V generated by w
  - `F[t]w s.t T∈LM, 0≠w∈V, F[t]w = {f(T)w | f(t)∈F[t]} = <w, Tw, T^2w, ...>`
  - `W = F[t]w, m_w(t) = m_(T|w)(t)`
    - `m_w(t)`는 minimal polynomial of w in V
  - 연습문제
    - *`T∈LM, 0≠w∈V, I_w = {f(t)∈F[t] | f(T)w = 0} => m_w(t)는 I_W에 속하는 다항식 중 최저차수의 non-zero monic polynomial ∧ f(t)∈I_w => f(t)는 m_w(t)의 배수`*
  - 성질
    - `T∈LM, 0≠w∈V, W = F[t]w`이면 다음이 성립
      - `m_w(t) = φ_T|w(t)`
      - `Bw = {w, Tw, ..., T^(m-1)w}는 W의 기저 (단, m = dimW = deg(m_w))`
      - `[T|w]_Bw^Bw는 m_w(t)에 대응하는 companion matrix`
      - `m_T(t)는 m_w(t)의 배수`
  - 연습문제
    - *`T∈LM, {v1, ..., vn} = Bv => m_T(t)=l.c.m. (m_v1(t), ..., m_vn(t))`*
  - *Caley-Hamilton Theorem의 두번째 증명*
    - `φ_T(t)와 m_T(t)를 정의`
    - `m_w(t)의 정의`
    - `minimal polynomial의 존재성`
    - *`m_w(t) = φ_T|w(t) 증명`*
      - minimal polynomial은 어떻게 구하는가?
    - `F[t]w는 T-invariant subspace이므로, φ_T(t)가 m_w(t)의 배수`
      - `W≤V, Bw를 basis extension theorem으로 Bv로 확장시키고, [T]_Bv^Bv하면...`
    - `=> ∀w∈V, φ_T(T)w = 0`
    - `=> φ_T(T)=0`

## 8.6 Cyclic Decomposition Theorem

- Cyclic Decomopsition Theorem
  - `T∈LM`
    - `let) m_T(t) = p(t)^f (p(t)는 monic irreducible polynomial) => ∃U1, ..., Uh≤V, V = U1 ⊕ ... ⊕ Uh (U1, ..., Uh는 T-cyclic subspace)`
    - `φ_T|Uj(t) = m_T|Uj(t) = p(t)^rj (j = 1, ..., h), f = r1 ≥ r2 ≥ ... ≥ rh ≥ 1 을 만족하는 h와 r1, ..., rh는 유일하게 결정된다`
      - essence
      - ?!
  - 참고
    - 선형대수에서 polynomial이 주인공 행세 하는 것은 `V를 F[t]-module`로 볼 수 있어야 부드러워 짐
    - Quotient space의 개념을 배우고 Cyclic decomposition theorem을 배워야 증명의 point를 알 수 있음
    - Fundamental Theorem of Finitely Generated Abelian Groups, Fundamental Theorem of Finitely Generated Modules over PID 를 배우고 나면, Cyclic Decomposition Theorem은 후자의 특수한 경우
      - Cyclic Decomposition Theorem을 생각하게된 motivation의 학습은 나중으로 미룸
  - 의의
    - `T∈LM, V를 T-cyclic subspace`들로 분해 가능
      - `T의 행렬을 companion matrix들로 이루어진 block diagonal matrix`의 꼴로 나타낼 수 있음
    - `h`와 `r1, ..., rh`의 uniqueness
      - essence
      - Ui들은 unique하지 않을 수 있지만, `h`와 `ri`들은 유일하게 결정됨
    - `A ~ B`의 invariant들의 부분집합은?
      - `D = {pi(t), hi, rij | 1≤i≤k, 1≤j≤hi}`
        - similar matrix의 invariant
          - `A ~ B => A ~~ B => 임의의 T에서 D는 unique => T를 LA, LB로 둬도 D는 unique => D는 similar matrix의 invariant`
        - *T의 행렬 표현을 완전히 결정해줌 (아직 이해가 안감)*
          - `ei·deg(pi) = dimWi = ∑_{j=1}^{hi}(rij)·deg(pi)`
            - *`dimWi = ∑_{j=1}^{hi}(rij)·deg(pi)`는 왜 성립하는거지?*
          - `=> ei = ∑_{j=1}^{hi}rij, dimWi, dimV = ∑_{i=1}^{k}dimWi`복원
          - Primary Decomposition Theorem
            - `[Ti]_Bi^Bi`들로 이루어진 block diagonal matrix와 similar
          - Cyclic Decomposition Theorem
            - `각각의 diagonal matrix [Ti]_Bi^Bi들이 다시 [Ti]_Bi^Bi ~ block matrix of companion matrix`
          - 두 squre matrix `A,B∈Mnxn(F), A~B인지 여부를 결정해주는 invariant들의 집합 = {pi(t), hi, rij}`
- *Jordan canonical form*
  - 일단 이전 내용을 이해하고 공부해야 할 듯
