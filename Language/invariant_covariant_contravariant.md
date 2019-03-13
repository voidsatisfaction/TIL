# 무공변성 공변성 반공변성

## 표기법

- `A <: B`
  - A가 B의 서브타입
- `A -> B`
  - 함수 타입으로, 함수의 인자 타입은 A이며 반환 타입은 B

## 공변성(Covariance)

- `Greyhound <: Dog <: Animal`
  - `Greyhound`는 `Dog`의 서브타입
  - `Dog`는 `Animal`의 서브타입
- `Dog -> Dog`의 서브타입이 될 수 있는 경우는?
  - 1: `Greyhound -> Greyhound`
  - 2: `Greyhound -> Animal`
  - 3: `Animal -> Animal`
  - 4: `Animal -> Greyhound`

## 반공변성(Contravariance)

## 무공변성(Invariance)
