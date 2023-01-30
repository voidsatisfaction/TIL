# Terraform Language

- 의문
- 개요
- 파일과 디렉터리
  - Module
  - Dependency Lock File
- Variables and Outputs
  - Input Variables
  - Output Variables
  - Local Variables
- Expressions
  - 개요
- State
  - Purpose of Terraform State

## 의문

## 개요

```terraform
resource "aws_vpc" "main" {
  cidr_block = var.base_cidr_block
}

<BLOCK TYPE> "<BLOCK LABEL>" "<BLOCK LABEL>" {
  # Block body
  <IDENTIFIER> = <EXPRESSION> # Argument
}
```

기본 컨벤션

```terraform
resource "aws_instance" "example" {
  count = 2 # meta-argument first

  ami           = "abc123"
  instance_type = "t2.micro"

  network_interface {
    # ...
  }

  lifecycle { # meta-argument block last
    create_before_destroy = true
  }
}

```

- 개요
  - 인프라 오브젝트 resource를 선언하기 위해서만 사용
- 특징
  - 선언적으로 구성되며, 의존 순서는 테라폼 엔진이 알아서 결정해줌
- 기본 구성
  - Blocks
    - resource와 같은 오브젝트의 설정의 내용을 담는 컨테이너
  - Arguments
    - 블록 속에 나타나며, 이름에 값을 할당함
  - Identifiers
    - argument 이름, 블록 타입 이름등이 모두 identifiers
- 컨벤션
  - 위의 기본 컨벤션 코드 참조
  - *Avoid separating multiple blocks of the same type with other blocks of a different type, unless the block types are defined by semantics to form a family. (For example: root_block_device, ebs_block_device and ephemeral_block_device on aws_instance form a family of block types describing AWS block devices, and can therefore be grouped together and mixed.)*

## 파일과 디렉터리

- `.tf`, `.tf.json`
- `UTF-8`

### Module

- 개요
  - 하나의 디렉터리에 함께 놓여진 `.tf`, `.tf.json` 파일의 컬렉션
- 특징
  - 오직 하나의 디렉터리의 top-level 설정 파일만 포함
    - nesting된 디렉터리는 아예 다른 별도의 모듈로 간주되어, 같은 설정에 포함되지 않음
  - module call
    - 다른 모듈을 하나의 설정으로 명시적으로 include하는 방법(child module이 됨)
    - 이러한 child module은 로컬 디렉터리 혹은 terraform registry와 같은 외부에서 데려올 수 있음
- 루트 모듈
  - 테라픔은 컨텍스트를 루트 모듈에서 실행함
  - 테라폼 설정은 root 모듈과 child 모듈들로 구성됨

### Dependency Lock File

`terraform init -upgrade`로 새 버전으로 변경할 경우 file changes

```terraform
--- .terraform.lock.hcl 2020-10-07 16:44:25.819579509 -0700
+++ .terraform.lock.hcl 2020-10-07 16:43:42.785665945 -0700
@@ -7,22 +7,22 @@
 }

 provider "registry.terraform.io/hashicorp/azurerm" {
-  version     = "2.1.0"
-  constraints = "~> 2.1.0"
+  version     = "2.0.0"
+  constraints = "2.0.0"
   hashes      = [
-    "h1:EOJImaEaVThWasdqnJjfYc6/P8N/MRAq1J7avx5ZbV4=",
-    "zh:0015b491cf9151235e57e35ea6b89381098e61bd923f56dffc86026d58748880",
-    "zh:4c5682ba1e0fc7e2e602d3f103af1638f868c31fe80cc1a884a97f6dad6e1c11",
-    "zh:57bac885b108c91ade4a41590062309c832c9ab6bf6a68046161636fcaef1499",
+    "h1:bigGXBoRbp7dv79bEEn+aaju8575qEXHQ57XHVPJeB8=",
+    "zh:09c603c8904ca4a5bc19e82335afbc2837dcc4bee81e395f9daccef2f2cba1c8",
+    "zh:194a919d4836d6c6d4ce598d0c66cce00ddc0d0b5c40d01bb32789964d818b42",
+    "zh:1f269627df4e266c4e0ef9ee2486534caa3c8bea91a201feda4bca525005aa0a",
   ]
 }

```

- 개요
  - 외부 디펜던시들(Providers, Modules)이 테라폼과 그것들을 의존하는 프로젝트로부터 독립적으로 업데이트 될 수 있으므로, 어떤 버전을 사용할지 명시적으로 적어둘 필요가 있음
    - Providers
      - 외부 시스템과 상호작용하기 위한 테라폼 플러그인
    - Modules
      - 재사용할 수 있는 추상성을 제공하기위해서 테라폼 설정을 그룹으로 나누는 것
  - 버전의 기록
    - Version constratins
      - 잠재적으로 compatible한 것을 나타내기
    - lock파일
      - 실제로 사용하는 버전을 나타내기
      - provider 의존성만 트래킹 함
      - module 의존성을 트래킹하지 않아서 언제나 최신 모듈을 사용함
- 락 파일 위치
  - 각 root module의 `.terraform`폴더의 `.terraform.lock.hcl`파일
  - `terraform init`시에 생성되며, 버전 컨트롤 리포에 추가해야 함
- 설치 동작
  - `terraform init`
    - recorded selection이 없는 경우
      - version constratins에 맞는 최신 버전을 가져옴
      - lock파일을 업데이트
    - recorded selection이 있는 경우
      - lock파일에 있는 해당 버전을 가져옴
  - `terraform init -upgrade`
    - 현재 셀렉된 버전(락파일에 명시된)을 버리고 version constratins에 맞는 최신 버전을 가져옴
- 체크섬 검증
  - 테라폼은 lock file에 기록해두었던 체크섬이랑 적어도 하나 이상은 일치하는지 각 패키지별로 체크함
  - trust on first use를 채택
    - 일단 처음에는 무조건 lock파일에 버전에 맞는 체크섬을 넣고 신뢰함
    - 나중에 한 번 이상 기록된 체크섬에 맞지 않는 provider가 등장하면 신뢰하지 않음
  - `terraform init -upgrade` 하면, `.terraform.lock.hcl`내의 provider 블록 내의 version, constraints, hashes도 변할 수 있음

## Variables and Outputs

- Input Variables
- Output Variables
- Local Variables

### Input Variables

```terraform
variable "image_id" {
  type = string
}

variable "availability_zone_names" {
  type    = list(string)
  default = ["us-west-1a"]
}

variable "docker_ports" {
  type = list(object({
    internal = number
    external = number
    protocol = string
  }))
  default = [
    {
      internal = 8300
      external = 8300
      protocol = "tcp"
    }
  ]
}
```

- 개요
  - 테라폼 모듈의 변수를 소스 코드를 직접 변경하지 않아도 변경할 수 있게 해줌
    - 모듈을 다른 테라폼 설정으로 공유할 수 있게 해주고, composable, reusable하게 해줌
- 특징
  - 모듈별 외부 설정법
    - root 모듈
      - CLI 옵션(`-var`)
      - 환경 변수
        - `TF_VAR_`를 prefix로 둠
      - `.tfvars`
    - child 모듈
      - `module`블록으로 값을 넘겨줄 수 있음

### Output Variables

```terraform
output "db_password" {
  value       = aws_db_instance.db.password
  description = "The password for logging in to the database."
  sensitive   = true
}
```

- 개요
  - 인프라의 정보를 커맨드라인에서 사용가능하고, 다른 테라폼 설정으로 사용할 수 있게 노출해줌
- 특징
  - child module이 리소스의 부분을 parent 모듈이 참조 가능하게 함
  - root 모듈이, CLI 아웃풋(`terraform apply`)으로 보여주도록 함
  - remote state를 사용할 경우, root 모듈 output이 `terraform_remote_state` 데이터 소스를 사용해서 접근가능하게 됨

### Local Variables

```terraform
locals {
  # Ids for multiple sets of EC2 instances, merged together
  instance_ids = concat(aws_instance.blue.*.id, aws_instance.green.*.id)
}

locals {
  # Common tags to be assigned to all resources
  common_tags = {
    Service = local.service_name
    Owner   = local.owner
  }
}
```

- 개요
  - 모듈의 지역변수로서, 외부에서 변경이 불가능한 변수
- 팁
  - 값이나 식이 반복되는 경우 && 미래에 변경될것 같은 경우에만 사용하기
  - 중앙 장소에서 value를 바꿀 수 있게 하기

## Expressions

### 개요

- 개요
  - configuration 내부에서 값을 평가하는 것
- 값의 타입
  - primitive type
    - `string`
      - 유니코드 문자열
    - `number`
      - 숫자, 부동소수점
    - `bool`
      - 불린 값
        - `true`는 "true"로 *필요에 의해서* 변환될 수 있음
          - *언제가 필요에 의한 것인지?*
  - complex type
    - collection type(dynamic, flexible)
      - `list(...)`
        - 같은 타입의 값의 리퀀스
      - `map(...)`
        - 이름이 붙은 레이블에 의해서 식별된 값들의 그룹
        - `{ "foo": "bar", "bar": "baz" }`
        - `{ foo = "bar", bar = "baz" }`
        - multi-line map에서는 키벨류값의 페어는 새 라인으로 충분함
          - `terraform fmt`가 수직적으로 equal sign을 맞춰줌
      - `set(...)`
        - 유니크한 값들의 컬렉션
    - structural type(static, schema)
      - `object(...)`
        - 각각이 각자의 타입을 갖는 이름을 갖는 attribute의 컬렉션
          - 리소스나 데이터블록을 선언하는데에 사용됨
        - 스키마
          - `{ <KEY> = <TYPE>, <KEY> = <TYPE>, ... }`
          - additional key에 대한 값들은 버려짐
      - `tuple(...)`
        - 각 엘리먼트가 각자의 타입을 갖는 엘리먼트의 시퀀스
        - 스키마
          - `[<TYPE>, <TYPE>, ...]`
          - 즉, 반드시 같은 원소의 개수를 만족해야 함
    - 특징
      - 유사한 complex type은 쉽게 서로 교환해서 사용 가능(`list/tuple/set`, `map/object`)
        - 테라폼이 알아서 비슷한 타입은 변환해줌
      - 가능하다면, 테라폼은 complex type내부의 element 값들을 recursive하게 타입변환을 함
      - e.g)
        - `list(string)`
          - `["a", 15, true]` -> `["a", "15", "true"]`
        - `map(string)`
          - `{name = ["Kristy", "Claudia", "Mary Anne", "Stacey"], age = 12}` -> `type mismatch error`
  - c.f) 타입이 아님
    - `null`
      - 값의 부재나 생략을 나타냄
        - 기본값을 사용하거나 인자가 반드시 필요한 경우 에러를 낼 수 있음
    - `any`
      - 타입의 placeholder이며, 테라폼이 하나의 실제 대체 가능한 타입을 찾으려고 함
