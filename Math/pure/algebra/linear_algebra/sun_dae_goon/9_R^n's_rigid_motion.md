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
    - `||X||≥0 ∧ ||X|| <=> X=0`
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
    - *Triangle Inequality*
      - `||X+Y|| ≤ ||X||+||Y||`
        - *이거 어떻게 증명해?*
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

## 9.2 R^n공간의 Rigid Motion

## 9.3 Orthogonal Operator / Matrix

## 9.4 Reflection

## 9.5 O(2)와 SO(2)

## 9.6 O(3)와 SO(n)
