# 군

- 의문
- 큰 그림
- 11.1 Binary Operation과 Group
- 11.2 Group의 초보적 성질
- 11.3 Subgroup
- 11.4 학부 대수학의 반
- 11.5 Group Isomorphism
- 11.6 Group Homomorphism
- 11.7 Cyclic Group
- 11.8 Group과 Homomorphism의 보기
- 11.9 Linear Group

## 의문

## 큰 그림

## 11.1 Binary Operation과 Group

- Cartesian product(곱집합), Product(곱)
  - `X x Y = {(x,y) | x∈X, y∈Y}`
    - 원소는 ordered pair
- binary operation(이항연산)
  - `집합 X가 있을 때, 함수 *: X x X -> X를 X위의 이항연산이라고 부름`
  - 결합법칙
    - `∀x,y,z∈X, (xy)z = x(yz)`
      - `xyz`라는 표현이 의미를 갖음
      - 원소들이 '연산을 서로 먼저하겠다고 다투지 않는다' = 'compatible'하다
    - e.g)
      - `Mnxn(F)에 새로운 binary operation [-,-]을 [A,B] = AB - BA (A,B∈Mnxn(F))로 정의하면, [-,-]는 non-associative다`
- group
  - 정의
    - 이항연산 `*`를 갖는 집합 G가 다음 조건들을 만족하면 `(G,*)`를 group이라고 함
      - (group1) `∀x,y,z∈G, (xy)z = x(yz)`
      - (group2) `∃e∈G, ∀x∈G, xe = ex = x`
      - (group3) `∀x∈G, ∃~x∈G, x・~x = ~x・x = e`
    - *닫혀있음에 대한 설명이 이제까지 없었음에도 불구하고, 왜 닫혀있어야만 group이라고 할 수 있는지?*
    - associative binary operation에 대해서, identity를 가지며 모든 원소가 inverse를 갖는 집합
  - 성질
    - group2조건을 만족하는 e는 유일하고, 그것을 항등원(identity, identity element)라 부르고, G를 강조할 필요가 있으면 `e_G`로 표기함
  - finite & infinite group
    - finite group
      - 군 G가 finite set
      - G의 order
        - `|G|`
    - infinite group
      - 군 G가 infinite set
- commutative(abelian) group(가환군)
  - `G는 군 ∧ ∀x,y∈G, xy = yx`

## 11.2 Group의 초보적 성질

- 표기법
  - Multiplicative Notation
    - 항등원
      - `e=1`
    - `g^1 = g, g^2 = gg, g^3 = ggg, ...`
    - `g^0 = 1`
    - `g^-2 = g^-1・g^-1, g^-3 = g^-1・g^-1・g^-1, ...`
  - Additive Notation
    - 항등원
      - `e=0`
    - 역원
      - `(-g)`
    - `..., (-2)g = (-g) + (-g), (-1)g = -g, 0g = 0, 1g = g, 2g = g+g, ...`
    - `g - h = g + (-h)`
  - 관습
    - commutative group => multiplicative notation
    - abelian group => additive notation
    - 근데 그냥 관습일 뿐
  - commutator
    - `g,h∈G, ghg^-1h^-1 꼴의 원소`
    - `G가 commutative <=> 임의의 commutator = 1`
- Exponential Law
  - in Multiplicative Notation
    - `g^m・g^n = g^m+n`
    - `(g^m)^n = g^mn`
    - `G가 commutative => g^n・h^n = (gh)^n`
  - in Additive Notation
    - `mg + ng = (m+n)g`
    - `m(ng) = (mn)g`
    - `G가 abelian => ng + nh = n(g+h)`
    - 위의 Multiplicative Notation과 완전 동일
    - Z-module?
- Cancellation Law
  - `x,y,z∈G, (xy=xz => y=z) ∧ (xz=yz => x=y)`
- 연산표
- Group classification
  - `|G|=1`
  - `|G|=2`
    - `G = {1, x}`
      - `=> x^2 ≠ x => x^2 = 1`
    - `고정된 x∈G, λx: G -> G, λx(y) = xy (y∈G) => λx: G -> G는 bijection`
      - `= λx는 집합 G를 permute한다`
  - `|G|=3`
    - `G = {1, x, y}`
    - 연산표로 확인
    - 근데, associativity를 어떻게 확인할 수 있을까?
      - 이미(a priori) associativity가 보장되어있는 group의 존재를 안다면 아무 문제가 없다
        - 어차피 isomorphic하므로
      - 따라서, `μn = {α∈C | α^n = 1}`은 finite commutative group임은 매우 powerful한 결과
        - 이는, 복소수 집합 C의 존재라는 어마어마한 background가 필요함
- direct product
  - `G1, G2가 group, Cartesian product G1 x G2에 다음과 같이 componentwise binary operation을 정의하자 (g1, g2)・(h1, h2) = (g1h1, g2h2) (gi, hi∈Gi)`
    - `G1xG2`는 group
- *이 부분의 내용이 어려워서 일단 넘어감*
  - *복소수의 극형식?*

## 11.3 Subgroup

Group의 story와 vector space의 story를 비교하면서 읽자

- subgroup
  - `H ≤ G <=> H가 group G의 subset(H ⊆ G), G로부터 물려받은 binary operation에 관하여, H자신 group이 되는경우`
  - 다음 확인이 반드시 필요
    - `G의 identity element eG로, H의 identity element를 eH로 표기하면, eH = eG`
    - `h∈H, h의 G에서의 inverse를 h^-1로, H에서의 inverse를 h'로 표기하면, h'=h^-1 이다`
  - *근데, 왜, 벡터공간의 부분공간 W≤V에서는 0w = 0v를 확인할 필요가 없었는가?*

## 11.4 학부 대수학의 반

## 11.5 Group Isomorphism

## 11.6 Group Homomorphism

## 11.7 Cyclic Group

## 11.8 Group과 Homomorphism의 보기

## 11.9 Linear Group
