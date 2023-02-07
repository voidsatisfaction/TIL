# Terraform Refactoring

- 의문
- 개요
  - moved 블록 방식
  - terraform state mv 방식

## 의문

## 개요

참고: https://ryaneschinger.com/blog/terraform-state-move/

- 테라폼을 root module에서 작업하다가, 재사용이 가능한 부분이 보이면 module화를 함
  - 기존의 terraform state와 새로운 모듈을 사용한 state의 싱크를 맞춰줘야 함
  - 기본적으로 테라폼 state는 오브젝트의 이동이나 새로 이름을 짓는것을 old address의 오브젝트의 삭제와 new address의 오브젝트의 생성으로 받아들임
- 방식
  - (자동 & 권장) `moved`블록을 통한 명시적인 리팩토링 히스토리 선언
    - 현재 존재하는 오브젝트의 old address를 new address인 것으로 매핑하게 함
  - (수동)`terraform state mv`를 사용하여, 기존의 terraform state의 리소스와 새로운 코드 형상의 리소스를 싱크

### moved 블록 방식

일반적인 예시

```tf
moved {
  from = aws_instance.a
  to   = aws_instance.b
}
```

모듈의 분리 리팩토링의 예시

```tf
module "x" {
  source = "../modules/x"

  # ...
}

moved {
  from = aws_instance.a
  to   = module.x.aws_instance.a
}
```

- `moved`블록의 삭제
  - 모든 히스토리를 보존하는 것을 추천함
  - 체이닝도 가능함

### terraform state mv 방식

- count기반의 코드의 경우
  - `terraform state mv aws_instance.instance[0] module.web.aws_instance.instance[0]` 이런식으로 옮겨주기 가능
- foreach기반의 코드의 경우
  - `terraform state mv aws_iam_user.user["joony"] module.iam_tada.aws_iam_user.user["joony"]`
