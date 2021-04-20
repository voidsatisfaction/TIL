# 내적공간

- 10.1 Inner Product Space
- 10.2 Inner Product Space의 성질
- 10.3 Gram-Schmidt Orthogonalization
- 10.4 Standard Basis vs Orthonormal Basis
- 10.5 Inner Product Space의 Isomorphism
- 10.6 Orthogonal Group과 Unitary Group
- 10.7 Adjoint Matrix와 그 응용

## 의문

## 참고

- conjugate(anti)-linear
  - `∀a,b∈C, ∀x,y∈V f: V -> W, f(ax+by) = ^af(x) + ^bf(y)`

## 큰 그림

- Euclidean space의 추상화
- Inner product (가 정의된) space의 정의와 성질

## 10.1 Inner product space

- 배경
  - Euclidean space의 확장
    - `R^n ∧ dot product가 부여된 공간`
- `C^n의 (Hermitian) dot product`
  - `X = t(a1, ..., an), Y = t(b1, ..., bn) ∈ C^n, <X,Y> = tX・^Y = ∑_{i=1}^{n}(ai・^bi)`
    - complex conjugate가 필요한 이유는 '길이가' 0이거나, 허수인 `t(1+i, 1-i), t(i,0)`등을 방지하기 위함
  - 성질
    - `(X,Y) -> <X,Y>로 정의된 함수 <,>: C^n x C^n -> C는 다음을 만족`
      - `X,Y,Z∈C^n, c∈C`
        - `<X+Y,Z> = <X,Z> + <Y,Z>`
        - `<cX,Y> = c<X,Y>`
        - `<X,Y+Z> = <X,Y> + <X,Z>`
        - `<X,cY> = ^c<X,Y>`
      - `X,Y∈C^n, <X,Y> = ^<Y,X>`
      - `0≠X∈C^n => <X,X>∈R ∧ <X,X> > 0`
  - 추상화
    - dot product정의 자체가 아닌, 해당 성질로부터 새로운 theorem이 도출되는 경우가 많음
    - **그럼 애초에 이러한 성질을 만족하는 친구들을 정의하고 inner product이라고 부른다면?**
      - 이번 추상화의 핵심
      - inner product자체를 어떻게 연산하는지는 관심이 없음
    - `F^n`의 inner product
      - `F=C => Hermitian inner product`
      - F^n에서 한단계 더 추상화를 해보자
    - `V`의 inner product
- `V`의 inner product space
  - `F=R or F=C, V를 F-vector space라 하자(V가 무한 차원인경우에도 허용) 이때, 함수 <,>: VxV -> F가 ∀u,v,w∈V, c∈F에 대해, 다음 조건을 만족하면 <,>를 V의 inner product라 부르고, inner product가 주어진 V를 inner product space(내적공간)라고 부른다. (특별히, F=C인 경우에는 Hermitian inner product라 부른다)`
    - `1 <u+v,w> = <u,w> + <v,w>`
    - `2 <cv,w> = c<v,w>`
    - `3 <v,w> = ^<w,v>`
    - `4 v≠0 => <v,v>∈R ∧ <v,v> > 0 `
      - 이 조건을 강조해서 positive definite inner product라고도 부름
  - **R^n의 dot product, C^n의 dot product는 당연히 inner product**
  - 주의
    - `F=R일 때에는, complex conjugate는 없는 것으로 생각하면 됨`
      - inner product = symmetric bilinear form
    - `F=C일 떄에, <,>의 앞 자리에서는 linear이고, 뒷자리에서는 conjugate linear라고 말함`
    - `Inner product space의 F-subspace는 항상 inner product space`
- complex-valued function과 그의 적분
  - `f: R -> C를 real variable의 complex-valued function`
    - `f(x) = f1(x) + i・f2(x) (x∈R)`
      - `f1, f2`는 real-valued function
    - `int_{a}^{b}(f(x))dx = int_{a}^{b}(f1(x))dx + i・int_{a}^{b}(f2(x))dx (a,b∈R)`
  - 적분과 inner product
    - `<f(t),g(t)> = int_{0}^{1}(f(t)・^g(t))dx (f(t),g(t) ∈ C[t])`
      - `C[t]`의 inner product
  - Fourier Analysis의 시작
    - `C^0[0,2π] = {f: [0,2π] -> C | f는 연속}`
      - `C^0[0,2π]는 C-vector space`
      - `<f,g> = (1/(2π))・int_{0}^{2π}(f(x)・^g(x))dx (f,g∈C^0[0,2π])`
        - `C^0[0,2π]의 inner product`
- trace form
  - `<A,B> = tr(tA・^B) (A,B∈Mnxn(F))`
- inner product space의 다양한 예시
  - Real numbers
    - `<x,y> = xy (x,y∈R)`
  - Euclidean vector space
    - `<x,y> = tx・y (x,y∈R^n)`
  - Complex coordinate space
    - `<x,y> = tx・^y (x,y∈C^n)`
  - Hilbert space
    - `<f,g> = int_{a}^{b}(f(t)・^g(t))dt (f,g∈F[t])`
  - Random variables
    - `<X,Y> = E(XY)`
  - Real matrices
    - ??
  - Vector spaces with forms

## 10.2 Inner Product Space의 성질

- trivial한 관찰로 부터 시작
  - `v∈V, ∀w∈V, <v,w>=0 => v=0`
    - *왜 항상 이 관찰로 부터 시작하는걸까?*
- norm
  - `v∈V, ||v|| = √(<v,v>)`
  - vector의 길이(크기)
  - positive definiteness조건은 norm을 정의하기 위한 것
  - 성질(`v∈V, c∈F`)
    - `||v||≥0 ∧ (||v||=0 <=> v=0)`
    - `||cv|| = |c|・||v||`
      - complex number c의 absolute
        - `|c| = √(c・^c) = √((Re c)^2 + (Im c)^2)`
    - `v≠0 => ||(1/||v||)・v|| = 1`
      - norm이 1인 벡터 = unit vector
    - Parallelogram Law
      - `||v+w||^2 + ||v-w||^2 = 2(||v||^2 + ||w||^2)`
- 사이각
  - 예를들어, `C^2`의 두 vector v와 w의 사이각은 좀 어색한 개념
  - but, Cauchy-Schwarz Inequality, Triangle Inequality는 여전히 유효
    - *왜?*
- orthogonal(perpendicular)
  - `v,w∈V, <v,w>=0 <=> v⊥w <=> v와 w는 서로 수직(perpendicular or orthogonal)`
  - `S,T⊆V, ∀v∈S, w∈T, <v,w>=0 <=> S⊥T <=> S와 T는 서로 수직`
  - 성질(`(v⊥w)`)
    - `||v+w||^2 = ||v||^2 + ||w||^2 (Pythagoras의 정리)`
    - `||v+w|| = ||v-w||`
  - Cauchy-Schwarz Inequality
    - `|<v,w>|≤||v||・||w|| (등호가 성립할 충분조건은 {v,w}가 일차종속)`
      - 증명이 신박하다
      - `v,w∈V ∧ w≠0 => (v - (<v,w>/<w,w>)・w) ⊥ w`
  - Triangle Inequality
    - `||v+w|| ≤ ||v|| + ||w||`
      - 이 증명 역시 신박하다
      - `z = c + id ∈ C, Re(z) = c => z+^z = 2Re(z) ∧ Re(z) ≤ |z|`
- 거리
  - v와 w사이의 거리 = `||v-w||`
  - 성질(`v,w,u∈V`)
    - `||v-v|| = 0`
    - `||v-w|| = ||w-v||`
    - `||v-w|| ≤ ||v-u|| + ||u-w||`
- **기하학의 생성**
  - **거리의 개념이 주어진 inner product space마다 기하학이 하나씩 생기는 셈**
- orthonormal basis
  - orthogonal subset
    - `V의 non-zero vector들 {vi| i∈I}가 mutually perpendicular이면(∀i≠j∈I, vi ⊥ vj), {vi| i∈I}를 V의 orthogonal subset이라 부름`
  - orthonormal subset
    - `orthogonal subset ∧ vi들이 모두 unit vector`
  - orthogonal basis
    - `V의 basis B가 orthogonal subset`
  - orthonormal basis
    - `V의 basis B가 orthonormal subset`
  - 흥미로운 연습문제
      - Complex-valued function `fn∈C^0[0,2π]를 fn(x) = e^inx = cos(nx) + i・sin(nx) (n∈Z, x∈[0,2π])로 정의하면 {fn | n∈Z}는 C^0[0,2π]의 orthonormal subset`
- Euclidean space의 경우에는 orthonormal basis의 존재가 자명하였지만, inner product space에서는 전혀 자명하지 않음
- 질문
  - `V가 (유한 차원) inner product space, W≤V => W의 orthonormal basis를 항상 찾을 수 있는가?`
- orthonormal complement
  - `S⊆V, S^⊥ = {v∈V | ∀w∈S, v ⊥ w}`
    - 여기서 특히 `W≤V, W^⊥를 W의 orthogonal complement라 함`
  - 성질(`S⊆V, W≤V ∧ Bw가 W의 기저`)
    - `S^⊥는 V의 subspace`
    - `S^⊥ = <S>^⊥`
    - `Bw^⊥ = W`
  - 성질2
    - `0^⊥=V ∧ V^⊥=0`
    - `W≤V => W∩W^⊥=0`
    - `W≤V => W≤(W^⊥)^⊥`
- 질문
  - `V가 f.d.v.s ∧ W≤V => dimW^⊥ = dimV - dimW ??`
- rigid motion
  - `M: V -> V가 조건 ||M(v)-M(w)|| = ||v-w|| (v,w∈V)을 만족하면 M을 V의 rigid motion이라 함`
    - 이것을 정의로 명명하지 않은 것은 앞으로는 inner product space의 rigid motion이라는 표현을 자주 사용하지 않겠다는 뜻
      - *왜??*
  - 우리의 아쉬움
    - `V가 유한차원 inner product space => V의 rigid motion은 항상 translation과 linear rigid motion의 합성으로 쓸 수 있는가?` or `0을 0으로 보내는 rigid motion은 linear인가?`
      - `F=C`일 때에는 아니오
        - `M: V -> V, M은 M(0)=0인 rigid motion일 때, <M(v),M(w)> ≠ <v,w> 이기 때문`
          - 이 성질이 정해주는 것은 무엇일까?
        - 아닌 이유는, `F=C일때, inner product가 두번째 좌표에서는 conjugate linear이기 때문`
  - 주의
    - 자명한 R-vector space isomorphism `r: R^2 -> C, r(t(a,b)) = a + ib (a,b∈R)`을 사용해 `R^2, C`를 R-vector space로서 identify할 수 있다.
    - 그러면 complex conjugate는 R^2의 관점에서는 reflection이므로, R-linear이지만, C의 관점에서는 C-linear가 아님
    - 역으로, C-linear rigid motion on C는 모두 R-linear rigid motion on R^2가 됨
      - 실제로, C-linear rigid motion on C는 R^2관점에서 보면 모두 rotation
- F=R일 때는 어떨까?
  - V의 orthonormal basis의 존재조차 모르고 있는 형편

## 10.3 Gram-Schmidt Orthogonalization



## 10.4 Standard Basis vs Orthonormal Basis

## 10.5 Inner Product Space의 Isomorphism

## 10.6 Orthogonal Group과 Unitary Group

## 10.7 Adjoint Matrix와 그 응용
