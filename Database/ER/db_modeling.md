# DB Modeling

- 의문
- 개요
- 실전 팁
  - Permission and Role
  - RDS 트리구조 데이터 저장

## 의문

## 개요

## 실전 팁

- redundant한 관계는 최대한 갖지 않는 것이 좋음
  - 즉, 많은 화살표(혹은 edge)는 필요 없다
- 암묵적인 로직 보다는 명시적인 field 추가
  - 예를들어, `user_id`라는 필드에 null값이 허용되는 경우, 해당 `user_id`가 `null`이면 `is_user`가 암묵적으로 `false`라고 생각하지 말고, 명시적으로 `is_user`라는 필드를 데이터베이스 column으로 두어서 모델을 보는 사람이 쉽게 파악할 수 있도록 한다
    - column 1개 추가 vs 명시성의 tradeoff

### Permission and Role

- 개념 정리
  - Permission
    - 개요
      - 특정 액션에 대한 권한
    - 예시
      - 게시글 생성 권한(C)
      - 게시글 읽기 권한(R)
      - 게시글 갱신 권한(U)
      - 게시글 삭제 권한(D)
      - ...
  - Role
    - 개요
      - Permission의 집합
    - 예시
      - admin role
        - 게시글 관리에 관한 모든 permission + 댓글관리에 관한 모든 permission 등...
      - middle admin role
        - 댓글 관리에 대한 모든 permission
- Permission과 Role의 테이블에서의 구현
  - Permission
    - `id`
    - `name`
    - `access`
    - `comment`
  - Role
    - `id`
    - `owner_uid`
    - `name`
    - `comment`
    - `permission`
      - permission의 집합을 uint10으로 표현한 값
      - e.g) 00001111 -> 게시글 CRUD가능 하지만 댓글 CRUD는 불가능
    - `show_type`
    - `updated_at`
  - 위의 테이블 뿐 아니라, Application level에서 uint(유저가 갖는 permission bits의 uint표현)를 각 비트 위치마다 permission으로 변환하는 코드가 필요

비트 위치에 따른 가능한 permission 매핑 코드 예시

```py
from enum import IntFlag, unique

def bit_shift(num):
    return 1 << num

@unique
class P(IntFlag):
    ACCESS = bit_shift(0) # 접근 가능한지
    ADMIN = bit_shift(1)
    USER_C = bit_shift(2)
    USER_V = bit_shift(3)
    USER_E = bit_shift(4)
    USER_D = bit_shift(5)
    ORG_C = bit_shift(6)
    ORG_V = bit_shift(7)
    ORG_E = bit_shift(8)
    ORG_D = bit_shift(9)
```

### RDS 트리구조 데이터 저장

- 예시
  - `Organization` table
    - `id`
    - `p_oid` >> 이 부분이 어떤 Organization(하나의 row)의 parent organization id
    - `type`
    - `wid`
    - `admin_uid`
    - `domain`
    - `name`
    - `address`
    - `phone_number`
    - `registration_num`
    - `created_at`
- 참고
  - 대신 데이터베이스에서 recursive한 참조 쿼리를 짜기 보다는, web service에서 직접 재귀 함수로 계속해서 가져오는 로직이 더 바람직
    - 데이터베이스는 가장 비싼 자원!
