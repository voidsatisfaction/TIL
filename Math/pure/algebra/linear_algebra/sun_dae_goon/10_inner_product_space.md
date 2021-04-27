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
  - 다양한 Inner product space

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
  - `S,T⊆V, ∀v∈S,∀w∈T, <v,w>=0 <=> S⊥T <=> S와 T는 서로 수직`
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
- orthongonality
  - 참고
    - `⊥`는 동치관계가 아니다
  - orthogonal subset
    - `V의 non-zero vector들 {vi| i∈I}가 mutually perpendicular이면(∀i≠j∈I, vi ⊥ vj), {vi| i∈I}를 V의 orthogonal subset이라 부름`
  - orthonormal subset
    - `orthogonal subset ∧ vi들이 모두 unit vector`
  - orthogonal basis
    - `V의 basis B가 orthogonal subset`
  - orthonormal basis
    - `V의 basis B가 orthonormal subset`
  - 흥미로운 연습문제
    - *Complex-valued function `fn∈C^0[0,2π]를 fn(x) = e^inx = cos(nx) + i・sin(nx) (n∈Z, x∈[0,2π])로 정의하면 {fn | n∈Z}는 C^0[0,2π]의 orthonormal subset`*
      - *어떻게 증명하지?*
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
        - *아닌 이유는, `F=C일때, inner product가 두번째 좌표에서는 conjugate linear이기 때문`*
          - *정확히 왜일까 한 번 증명을 고대로 해보자*
  - *주의* (이 부분 다시 읽기)
    - 자명한 R-vector space isomorphism `r: R^2 -> C, r(t(a,b)) = a + ib (a,b∈R)`을 사용해 `R^2, C`를 R-vector space로서 identify할 수 있다.
    - *그러면 complex conjugate는 R^2의 관점에서는 reflection이므로, R-linear이지만, C의 관점에서는 C-linear가 아님*
      - *정확히 무엇이 말하고 싶은 것일까?*
    - *역으로, C-linear rigid motion on C는 모두 R-linear rigid motion on R^2가 됨*
      - *실제로, C-linear rigid motion on C는 R^2관점에서 보면 모두 rotation*
- F=R일 때는 어떨까?
  - V의 orthonormal basis의 존재조차 모르고 있는 형편

## 10.3 Gram-Schmidt Orthogonalization

임의의 finite dimensional inner product space에서 orthonormal basis를 찾을 수 있다

- Gram-Schmidt Orthogonalization
  - `V가 inner product space이고 {v1, ..., vr}을 V의 linearly independent subset이라고 하자.`
    - `1. w1=v1으로, 그리고 2≤i≤r, wi = vi - (<vi,wi-1>/<wi-1,wi-1>)・wi-1 - ... - (<vi,w1>/<w1,w1>)・w1 으로 inductively 정의하면 <v1, .., vr> = <w1, ..., wr> ∧ {w1, ..., wr}은 V의 orthogonal subset`
    - `2. 따라서, {(1/||w1||)・w1, ..., (1/||wr||)・wr}은 orthonormal subset`
    - `3. 특별히 r = dimV => {(1/||w1||)・w1, ..., (1/||wr||)・wr}은 orthonormal basis`
  - 의미
    - 유한 차원 inner product space의 orthonormal basis의 existence가 보장됨
- 따름정리
  - `V가 유한차원 inner product space ∧ W≤V => W자신이 inner product space이므로, W도 orthonormal basis를 갖음`
    - **`V = W ⊕ W^⊥`**
    - `dimV = dimW + dimW^⊥`
- 연습문제(`V가 유한 차원 inner product space ∧ U,W ≤ V`)
  - `W = (W^⊥)^⊥`
  - `(U+W)^⊥ = U^⊥ ∩ W^⊥`
  - `(U ∩ W)^⊥ = U^⊥ + W^⊥`
- rank theorem의 증명
  - `F=R일 때의 rank theorem의 증명`
    - `AX=0`의 solution space에 대한 새로운 해석 필요
    - `A∈Mmxn(R)의 row space <t[A]_1, ..., t[A]_m>은 연립방정식 AX＝0의 solution space의 orthogonal complement 즉, ker(LA) = {X∈R^n | AX=0} = <t[A]_1, ..., t[A]_m>^⊥이고 따름정리에 의해 dimker(LA) = n - row rank of A`
  - `F=C일 때의 rank theorem의 증명`
    - 표기
      - `W^conj = {^X∈C^n | X∈W}`
        - `W^conj ≤ C^n`
        - `dim(W^conj) = dim(W)`
    - *`연립방정식 A^X=0의 solution space를 W = {X∈C^n | A^X=0} ≤ C^n 으로 표기하면...`*
      - *증명이 아직 이해가 잘 안됨*

## 10.4 Standard Basis vs Orthonormal Basis

- 배경
  - Euclidean space의 standard basis역할을 대신할 inner product space의 기저는?
- `F^n의 dot product와 standard basis의 특징`
  - `X∈F^n => Z = ∑_{i=1}^{n}(<X,ei>・ei) (즉, [X]_ε의 i번째 좌표는 <X,ei>)`
  - `X,Y∈F^n => <X,Y> = t[X]_ε・^[Y]_ε`
    - standard basis가 그토록 결정적인 역할을 할 수 있었던 이유는 위 특징들 때문
- V의 inner product는 사실상 dot product와 다름이 없다
  - `Bv = {v1, ..., vn}이 inner product space V의 orthogonal basis면 다음이 성립`
    - `v∈V => v = ∑_{i=1}^{n}((<v,vi>/<vi,vi>)・vi) (즉, [v]_Bv의 i-번째 좌표는 <v,vi>/<vi,vi>)`
  - `Bv = {v1, ..., vn}이 inner product space V의 orthonormal basis면 다음이 성립`
    - `v∈V => v = ∑_{i=1}^{n}(<v,vi>・vi) (즉, [v]_Bv의 i-번째 좌표는 <v,vi>)`
    - `v,w∈V => <v,w> = t[v]_Bv・^[w]_Bv`
- Fourier coefficient
  - `Bv = {vi | i∈I}가 inner product space V의 orthonormal subset`
    - `v의 i-th Fourier coefficient = <v,vi> (v∈V)`
      - 이를 Bv에 관한 v의 i-번째 좌표로 생각
    - 만약, Bv가 V의 orthogonal subset => `<v,vi>/<vi>`를 Bv에 관한 v의 i-th Fourier coefficient라 부름
- Closest Vector Problem
  - `W≤V, v∈V`, v에 가장 가까운 W의 vector찾기
    - e.g) PCA
  - 논의
    - `v∈V, v의 W-성분(W에 내린 수선의 발)은 무엇일까?`
    - `V = W ⊕ W^⊥ ∧ w∈W와 w'∈W^⊥가 유일하게 결정되는데 w, w'는 어떻게 구할 수 있을까?`
      - Gram-Schmidt Orthogonalization Process를 이용하여, subspace W의 orthonormal basis `{v1, ..., vm}`을 찾음
      - v의 W-성분 w는 다름아닌 `w = <v,v1>v1 + ... + <v,vm>vm (w' = v-w)`
  - `W가 inner product space V의 finite dimensional subspace ∧ {v1, ..., vm}을 W의 orthonormal basis라 하자. v∈V => ∃w∈W, ∃w'∈W^⊥ s.t v=w+w' ∧ w, w'는 유일 ∧ w = <v,v1>v1 + ... + <v,vm>vm`
    - *증명?*
  - Closest Vector Problem의 해답
    - 위 관찰의 w는 v에 가장 가까운 W의 vector가 된다
    - *증명?*
  - 따름정리
    - `Bv = {v1, ..., vn}이 inner product space V의 orthonormal basis, v = ∑_{i=1}^{n}(aivi) (ai∈F) => ||v||^2 = ∑_{i=1}^{n}(|ai|^2) = ∑_{i=1}^{n}(|<v,vi>|^2)`
  - Bassel's Inequality
    - `Bv = {v1, ..., vn}이 inner product space V의 orthonormal subset => ∀v∈V, ∑_{i=1}^{n}(|<v,vi>|) ≤ ||v||^2`
  - `∑_{n=1}^{n}(1/(n^2)) ≤ π^2/6`의 증명
    - `fn∈C^0[0,2π], fn(x) = e^inx = cos(nx) + i・sin(nx) (n∈Z, x∈[0,2π])`
    - `{fn | n∈Z}는 C^0[0,2π]는 orthonormal subset`
    - `f∈C^0[0,2π]`로 두면

## 10.5 Inner Product Space의 Isomorphism

유한차원 inner product space는 본질적으로 하나뿐

- inner product를 보존하는 isomorphism
  - Gram-Schmidt Orthogonalization => f.d.v.s inner product space V의 orthonormal basis = `Bv = {v1, ..., vn}`
  - `α_ε^Bv: V -> F^n, α_ε^Bv(vi) = ei`
    - `<α_ε^Bv(vi), α_ε^Bv(vj)> = δ_ij = <vi, vj> (1≤i,j≤n)`
    - `<α_ε^Bv(v), α_ε^Bv(w)> = <v,w>`
  - α_ε^B는 inner product를 보존하는 isomorphism
    - `α_ε^Bv`는 vector space의 isomorphism이면서 동시에 inner product의 구조도 그대로 옮겨줌
- inner product space isomorphism
  - V와 V'이 F-위의 inner product space, `φ: V -> V', φ는 vector space isomorphism ∧ <φ(v),φ(w)> = <v,w> (v,w∈V)`
    - `φ`는 혼동이 없는 이름바꾸기
  - `φ`가 inner product isomorphism일 필요충분조건
    - `φ`는 F-vector space isomorphism
    - 그냥 inner product를 취한 것이나, φ로 이름을 바꾸어 inner product를 취한 것이나 같다
  - 결론
    - 이름만 다르고 사실상 같은 inner product space는 그 성질이 같다
      - 성질
        - inner product space로서의 성질로, {덧셈 상수곱 inner product}에 의해서 묘사되는 성질
        - `{논리 기호, 함수 등의 집합 기호, 덧셈, 상수곱, inner product}`로 묘사된 성질은 isomorphic한 inner product space들이 공유
- R위의 유한차원 inner product의 rigid motion(`V가 R-위의 유한 차원 inner product space`)
  - `L(0)=0인 V의 rigid motion L은 linear map`
  - `=> V의 rigid motion M은 translation과 linear rigid motion의 합성으로 쓸 수 있음`
  - `=> V의 rigid motion은 항상 bijection`

## 10.6 Orthogonal Group과 Unitary Group

orthogonal operator, orthogonal matrix, orthogonal group의 개념을 inner product space로 일반화

- orthogonal group & unitary group
  - orthogonal group(`F=R인 경우`)
    - `V가 inner product <,>가 주어진 R-위의 inner product space일 때`
    - `O(V) = O(V,<,>) = {L∈L(V,V) | ∀v,w∈V, ||Lv - Lw|| = ||v-w||}`
      - orthogonal group on V with respect to `<,>`
  - orthogonal operator
    - O(V)의 원소
  - unitary group(`F=C인 경우`)
    - *왜 unitary라고 부르는 걸까?*
    - `V가 Hermitian product <,>가 주어진 R-위의 inner product space일 때`
    - `U(V) = U(V,<,>) = {L∈L(V,V) | ∀v,w∈V, ||Lv - Lw|| = ||v-w||}`
      - unitary group on V with respect to `<,>`
  - unitary operator
    - U(V)의 원소
  - 주의
    - `<,>1, <,>2가 V의 inner product일 때, O(V,<,>1)과 O(V,<,>2)가 같을 필요가 없다`
    - L은 가역
- orthogonal matrix & unitary matrix
  - `C^n의 경우`
    - (complex) unitary group
      - `C^n에 (Hermitian) dot product가 주어졌을 때`
      - `U(n) = {A∈Mnxn(C) | LA ∈ U(C^n, dot product)} = {[L]_ε^ε∈Mnxn(C) | L∈U(C^n, dot product)}`
    - (complex) unitary matrix
      - U(n)의 원소
  - `V와 <,>로부터 얻어진 orthogonal group(F=R)`
    - `On(R,<,>) = {[L]_Bv^Bv∈Mnxn(R) | L∈O(V,<,>)}`
  - `V와 <,>로부터 얻어진 unitary group(F=C)`
    - `Un(C,<,>) = {[L]_Bv^Bv∈Mnxn(C) | L∈U(V,<,>)}`
    - **위와 같은 표기법을 사용하려면, 먼저 위 표기법이 orthonormal basis와는 무관함을 보여야 함**
      - 즉, **`Bv와 Bw가 각각 F=R,C일 떄, {[L]_Bv^Bv∈Mnxn(R) | L∈O(V,<,>)} = {[L]_Bw^Bw∈Mnxn(R) | L∈O(V,<,>)}`가 성립하는 것을 먼저 증명해야 함**
- **`On(R,<,>)과 Un(C,<,>)의 정의는 V의 orthonormal basis의 선택과는 무관하다`**
  - 따름 명제
    - `B가 dot product가 주어진 Euclidean space R^n의 임의의 orthonormal basis => O(n) = {[L]_B^B ∈ Mnxn(R) | L∈O(R^n)}`
      - R^n의 표준기저가 아닌 새로운 orthonormal basis를 생각 = 새로운 직교좌표계를 생각한다는 뜻
      - 그런데, R^2의 rotation은 직교좌표계를 바꾸어도 여전히 R^2의 rotation
        - *무슨 의미?*
  - *증명?*
- `V가 inner product <,>가 주어진 n-dimensional inner product space ∧ L∈L(V,V)일 때, 다음이 동치`
  - `1 ∀v,w∈V, ||Lv - Lw|| = ||v-w||`
  - `2 ∀v∈V, ||Lv|| = ||v||`
    - `2' ||v|| = 1 => ||Lv|| = 1 (L은 unit vector를 보존)`
  - `3 ∀v∈V, <Lv,Lv> = <v,v>`
  - `4 ∀v,w∈V, <Lv,Lw> = <v,w>`
  - `5 Bv가 V의 orthonormal basis => L(Bv)도 V의 orthonormal basis`
    - `5' ∃Bv⊆V인 orthonormal basis s.t L(Bv)가 V의 orthonormal basis`
-

## 10.7 Adjoint Matrix와 그 응용
