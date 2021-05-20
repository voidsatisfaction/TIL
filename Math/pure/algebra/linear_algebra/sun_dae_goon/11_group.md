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

## 11.3 Subgroup

## 11.4 학부 대수학의 반

## 11.5 Group Isomorphism

## 11.6 Group Homomorphism

## 11.7 Cyclic Group

## 11.8 Group과 Homomorphism의 보기

## 11.9 Linear Group
