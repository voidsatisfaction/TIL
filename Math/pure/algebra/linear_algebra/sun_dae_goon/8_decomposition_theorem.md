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

## 정리

## 8.1 Polynomial

- 인수분해(factorization)
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
      - multiplication은 쉬운데 역연산인 factorization은 알고리즘의 측면에서 매우 어려움(RSA암호)
    - polynomial factorization
      - 개요
        - 인수분해는, polynomial의 root을 찾는 문제를 해당 polynomial의 factor들의 root를 찾는 문제로 환원시킴
        - F를 coefficient로 갖는 polynomial은 unique factorization property를 갖음
          - 이는 소인수 분해의 polynomial 버전
          - 소수 ~~ irreducible polynomial
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

## 8.3 Primary Decomposition Theorem

## 8.4 Diagonalizability

## 8.5 T-Cyclic Subspace

## 8.6 Cyclic Decomposition Theorem