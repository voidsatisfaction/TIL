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
  - `det(In) = det(e1, ..., en) = 1`을 만족하는 alternating n-linear form `det: F^n x ... x F^n -> F`는 존재하고 유일하다. `det(A) = |A|`의 표기법도 사용한다
    - `n=2`인 경우
    - `n=3`인 경우

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
