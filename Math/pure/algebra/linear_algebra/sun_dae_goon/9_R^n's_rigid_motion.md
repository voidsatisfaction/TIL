# 9. R^n의 Rigid Motion

- 의문
- 큰 그림 정리
- 9.1 R^n공간의 Dot Product와 Euclidean Norm
- 9.2 R^n공간의 Rigid Motion
- 9.3 Orthogonal Operator / Matrix
- 9.4 Reflection
- 9.5 O(2)와 SO(2)
- 9.6 O(3)와 SO(n)

## 의문

- *Euclidean space의 거리, 사이각 등의 개념은 선형대수학적으로 정의되는 것인가? 아니면, 다른 수학 분야에서는 다르게 정의할 수 있는가?*

## 큰 그림 정리

Rigid motion = 길이와 거리가 변하지 않는 '딱딱한' 운동

- `R^n`공간에 dot product 연산 부여
  - 기하적 구조 생성
    - norm
    - 사이각
    - 거리
    - 수직

## 9.1 R^n공간의 Dot Product와 Euclidean Norm

- `Euclidean space`
  - dot product가 주어진 R^n공간
    - dot product는 R^n 공간에 기하적인(topological) 구조를 줌
      - dot product가 정의됨 -> norm이 정의 됨 -> 사이각, 거리, 수직 등이 정의됨
      - 근데, 우리의 스토리에서는 `<X,Y> = ||X||·||Y||cosθ`가 항상 성립한다고 얼버무리고 넘어감
        - 이걸 어떻게 스토리상에서 설정파괴하지 않고 연역적으로 증명할 수 있을까?
- `Euclidean geometry`
  - Euclidean space를 공부하는 것
- `R^n의 dot product`
  - `X=t(a1, ..., an), Y=t(b1, ..., bn), <X,Y> = tX·Y = ∑_{i=1}^{n}(ai·bi)`
    - dot product은 bilinear form
  - 성질
    - `R^n x R^n -> R로 가는 함수 (X,Y) -> <X,Y>는 R^n의 bilinear form`
    - `X,Y∈R^n => <X,Y> = <Y,X>`
    - `X∈R^n => <X,X> ≥ 0 ∧ <X,X>=0 <=> X=0`
  - 연습문제
    - `X∈R^n, ∀Y∈R^n, <X,Y>=0 => X=0`
- `X의 Euclidean norm`
  - `X∈R^n, ||X|| = √<X,X>`
    - 벡터의 길이(크기)
  - 성질(`X∈R^n, c∈R`)
    - `||X||≥0 ∧ ||X||=0 <=> X=0`
    - `||cX|| = |c|·||X||`
    - `||(1/||X||)・X|| = 1`
    - unit vector
      - norm이 1인 벡터
  - 사이각
    - `<X,Y> = ||X||·||Y||cosθ`
      - *`R^2`이 아닌경우는?*
    - vector X, Y의 사이각 θ의 정의
      - 두 벡터 X, Y가 generate하는 R^n의 2-dimensional subspace `<X> ⊕ <Y> = R^2`이므로
      - `R^2`에서 사이각을 재면 된다(`0≤θ≤π`)
        - *그래서 사이각이 뭔데?*
        - X,Y가 정의되는 공간에서 사이각을 잰다는 말인듯
    - 코시 슈바르츠 부등식
      - `|<X,Y>| ≤ ||X||·||Y||`
        - 등호가 성립할 필요충분조건은?
    - Triangle Inequality
      - `||X+Y|| ≤ ||X||+||Y||`
        - 양변을 제곱
  - 거리(metric)
    - `X와 Y사이의 거리 = ||X-Y||`
    - 성질
      - `||X-X|| = 0`
      - `||X-Y|| = ||Y-X||`
      - `||X-Y|| ≤ ||X-Z|| + ||Z-Y||`
  - 수직(orthogonal, perpendicular)
    - `X,Y∈R^n, X⊥Y <=> X,Y는 서로 수직 <=> <X,Y>=0`
    - `S,T⊆R^n, S⊥T <=> S,T는 서로 수직 <=> ∀X∈S,∀Y∈T, <X,Y>=0`
    - 성질
      - `X,Y∈R^n, 다음이 동치`
        - `X⊥Y`
        - `||X+Y||^2 = ||X||^2 + ||Y||^2 (Pythagoras의 정리)`
        - `||X+Y|| = ||X-Y||`
          - 살짝 신기하다
  - orthogonal subset & orthonormal subset
    - orthogonal subset
      - `non-zero vector {X1, ..., Xm}, ∀1≤i≠j≤m, Xi⊥Xj`
    - orthonormal subset
      - `orthogonal subset ∧ ∀1≤k≤m, ||Xk||=1`
    - orthogonal basis
      - `R^n의 basis Bv가 orthogonal subset`
    - orthonormal basis
      - `R^n의 basis Bv가 orthonormal subset`
      - 주어진 orthogonal basis로부터 언제나 orthonormal basis를 만들 수 있음
    - 연습문제
      - `R^n의 orthogonal subset {X1, ..., Xm}은 일차독립`
      - `Bv = {X1, ..., Xn}이 R^n의 orthonormal basis <=> ∀1≤i,j≤m, <Xi,Xj> = δij`
  - `S^⊥`(S perp) & orthogonal complement
    - `S^⊥`
      - `S⊆R^n, S^⊥ = {X∈R^n | ∀Y∈S, X⊥Y}`
    - orthogonal complement
      - `W≤R^n, W^⊥를 W의 orthogonal complement`
    - 성질
      - `S^⊥는 R^n의 subspace`
      - `S^⊥ = <S>^⊥`
      - `Bw^⊥ = W^⊥`
        - 임의의 벡터가 W에 수직이기 위해서는 W의 basis Bw에 수직이기만 하면 충분
    - motivation
      - `0^⊥ = R^n ∧ (R^n)^⊥ = 0`
      - `W≤R^n => W ∩ W^⊥ = 0`
      - `W≤R^n => W ≤ (W^⊥)^⊥`
        - `W≤R^n => W = (W^⊥)^⊥`인가?
    - 질문
      - `∀W≤R^n, dimW^⊥ = n-dimW`인가?
        - `=> dim(W^⊥)^⊥ = n - (n - dimW) = dimW`
        - `=> R^n = W ⊕ W^⊥`

## 9.2 R^n공간의 Rigid Motion

- Rigid motion
  - `R^n공간에서 물체의 모습을 변화시키지 않는 운동 = 거리와 크기를 보존하는 운동`
  - 역으로 rigid motion에 의해 보존되는 성질을 공부하는 것 = Euclidean geometry
- isometry
  - 함수 `M: R^n -> R^n`이 조건 `||M(X)-M(Y)|| = ||X-Y|| (X,Y∈R^n)`을 만족
  - 예시
    - translation(평행이동)
      - `T_Y: R^n -> R^n, T_Y(X) = X+Y`
        - translation by Y
        - T_Y는 bijection
        - `(T_Y)^-1 = T_(-Y)`
    - rotation(회전이동)
      - `Rθ = (cosθ -sinθ; sinθ cosθ), Rθ = L_Rθ: R^2 -> R^2`
        - Rθ는 bijection
        - `(Rθ)^-1 = R-θ`
    - reflection(대칭이동)
      - `S = (1 0; 0 -1), Ls = S`
        - S는 bijection
        - `S^-1 = S`
  - 성질(`M: R^n -> R^n이 R^n의 rigid motion`)
    - `M은 injective`
    - `M은 연속함수`
      - *?!*
    - `R^n의 rigid motion은 항상 bijection`
      - *`R^n`의 rigid motion은 linear map?*
        - 어떻게 증명하지?
  - 성질2
    - `R^n의 rigid motion의 합성은 rigid motion`
    - `R^n의 bijective rigid motion의 역함수는 rigid motion`
    - `L = T_{-M(0)}∘M => L(0)=0 ∧ M = T_M(0)∘L`
- 우리의 주장
  - `L(0)=0 인 R^n의 rigid motion L은 linear map`
    - 이 주장의 증명은 지금까지 공부한 추상적인 언어가 우리의 고향 R^n에서 매우 강력한 툴이 되었음을 보여 줌
    - 애초에 `L(0)≠0`인 rigid motion이 있다?
      - translation?!
  - `L(0)=0인 R^n의 rigid motion L의 성질`
    - `||L(X)|| = ||X||`
    - `∀X∈R^n, <L(X),L(X)> = <X,X>`
    - `∀X,Y∈R^n, <L(X),L(Y)> = <X,Y>`
    - `Bv가 R^n의 orthonormal basis => L(Bv)도 R^n의 orthonormal basis`

## 9.3 Orthogonal Operator / Matrix

## 9.4 Reflection

## 9.5 O(2)와 SO(2)

## 9.6 O(3)와 SO(n)
