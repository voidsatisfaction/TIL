# 테라폼 cheat sheet

- 의문
- 개요

## 의문

## 개요

- `terraform plan`
  - `terraform plan -refresh=false`
    - `refresh`는 테라폼 현재의 tfstate의 형상과 실제 리소스의 형상을 비교하는 것이므로, false로 두면 그 형상은 냅두고, 로컬에서의 코드의 형상의 변화와 현재의 tfstate의 형상과 실제 리소스의 형상만 싱크 맞춰줌
  - `-refresh-only`
    - 위와 반대로, tfstate의 형상과 실제 리소스의 형상만 싱크를 맞춰줌
