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
  - 필요 지식
    - irreducible polynomial(기약 다항식)
      - 개요
        - degree가 1이상
          - `a∈F`는 기약다항식이라 부르지 않음
          - `~~ 소수에 1을 포함시키지 않는것과 같은 느낌`
      - 특징
        - `C[t]`의 irreducible polynomial은 일차식 뿐
        - `R[t]`의 irreducible polynomial은 일차식과 이차식 뿐
          - 그 이유는, factorization의 정의로 부터, polynomial factorization은 `R[t]`의 원소의 곱으로 표현되야 되므로...
          - `α가 f(t) = a0t^n + an-1t^(n-1) + ... + a1t + a0 (a0, ..., an ∈ R)의 근 => f(!α) = 0 (!α는 α의 켤레복소수(conjugate))`
          - `t^2-(α+!α)t+α!α ∈ R[t]`
            - `α, !α를 근으로 갖는 이차식`
            - **여기에, 대수학의 기본정리를 적용하면, 임의의 non-constant polynomial은 C에서 근을 갖으므로 계속해서 인수 분해 가능**
    - GCD(Greatest Common Divisor)의 성질
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
  - `A = (aij)∈Mmxn(C)`일 떄
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
      - `f(t)∈C[t] => !f(!A) = !f(A)`
      - `A가 invertible => !A가 invertible ∧ (!A)^-1 = !(A^-1)`

## 8.2 T-Invariant Subspace

선형변환을 적용하더라도, 변환 후의 벡터 공간의 범위가 기존의 벡터 공간을 넘지 않는 경우

원소의 개수 자체는 변할 수 있으나, 그 외의 '성질'들이 변하지 않는 부분 공간

- `W가 V의 T-invariant space(W는 T-stable)`
  - `T∈LM ∧ W≤V, T(W)≤W (결국, T(W)≤W≤V) (즉, T|W: W -> W가 의미가 있는 경우)`
    - *의미가 있다는게 무슨 의미인지*
    - `T∈Mnxn(F) => T = L_T, V=F^n으로 이해`
- 성질
  - `T∈LM, U,W가 V의 T-invariant subspace => U∩W 와 U+W도 T-invariant`
  - `T∈LM, W가 V의 T-invariant subspace, W의 기저 Bw를 V의 기저 Bv로 확장(Basis Extension Theorem)하면, [T]_Bv^Bv = ([T|w]_Bw^Bw *; 0 *)의 형태`
    - T|w의 characteristic polynomial은 T의 characteristic polynomial에 대한 결정적인 정보 제공
    - T|w의 minimal polynomial은 T의 minimal polynomial에 대한 큰 정보를 주지 못함
    - *T-invariant subspace를 생각하는 첫 번쨰 이유는, 무언가 T에 관해 알고 싶은 것이 있을 떄, `dimV`에 관한 귀납법을 사용할 수 있을 것이라는 idea떄문 이라고 할 수 있다*
      - 이게 정확히 무슨뜻인지?
- triangularization의 엉터리 귀납법
  - *이해가 지금은 잘 안된다*
- 활용
  - block diagonal matrix로의 decompose(분해)
    - `T∈LM, U,W가 T-invariant subspace, V=U⊕W, Bu, Bw는 U,W의 basis`
      - `=> Bv = Bu ∐ Bw`
      - `=> [T]_Bv^Bv = ([T|u]_Bu^Bu 0; 0 [T|w]_Bw^Bw)`
        - `[T]_Bv^Bv는 block diagonal matrix`
      - `=> φ_T(t) = φ_T|u(t)・φ_T|w(t) ∧ m_T(t) = l.c.m(m_T|U(t), m_T|w(t))`
      - 이 논의를 k-개의 T-invariant subspace들의 direct sum인 경우로 확장하면?
- 성질2
  - `T∈LM, f(t)∈F[t]일 떄`
    - `kerT, imT는 T-invariant`
      - `∃v∈V, s.t w = Tv`
    - `kerf(T), imf(T)는 T-invariant`
  - `T∈LM, W가 V의 T-invariant subspace => ∀f(t)∈F[t], W는 f(T)-invariant subspace`
  - `T∈LM, λ∈F => T의 eigen-space VT,λ는 T-stable`
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
    - `T∈LM, f(t),g(t)∈F[t]는 monic ∧relatively prime, E(t) = f(t)g(t) ∈ I_T => V = kerf(T) ⊕ kerg(T)`
      - `E(t) = m_T(t) => m_T|u(t) = f(t) ∧ m_T|w(t) = g(t)`
      - `E(t) = φ_T(t) => φ_T|u(t) = f(t) ∧ φ_T|w(t) = g(t)`
  - 주의
    - similar matrix의 invariant
      - `φ_T(t), m_T(t) => pi(t), ei, fi => dimWi, m_Ti(t), φ_Ti(t)`
      - **`Wi`자체는 similar matrix의 invariant가 아님**
- 연습문제
  - `A = (0 4 0 -2; 0 2 0 0; 0 -2 1 0; 1 0 1 3)`
    - `characteristic polynomial = (t-1)^2(t-2)^2`임을 보여라
    - `m_A(t)를 구하라`
    - `A`의 diagonalizability를 판정
    - `F^4`의 A에 관한 primary decomposition을 묘사하라
    - `primary decomposition`에 관한 `LA`의 행렬표현(block diagonal matrix의 형태)을 구하라

## 8.4 Diagonalizability

## 8.5 T-Cyclic Subspace

## 8.6 Cyclic Decomposition Theorem
