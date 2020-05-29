# SQL Alchemy

- 개요
- flush vs commit

## 개요

## flush vs commit

- `flush()`
  - 기능
    - DB의 transactional buffer에 관련 액션 임시적으로 저장
      - 아직 완벽히 persist하게 반영되지는 않음
    - sqlalchemy에서는 설정이 `autoflush=True`로 되어있음
  - 예시
    - `session.add(instance)` 한뒤에, `session.flush(instance)`한 뒤에, `instanceModel.all()`하면 flush한 오브젝트를 포함해서 전부 fetch
- `commit()`
  - 기능
    - 데이터를 persist 시킴
    - 트랜잭션의 한 세션이 끝나고 새로운 transaction 세션 시작 가능

### Transactional memory

- 정의
  - atomic한 방법으로 그룹의 명령을 불러오고 저장 해서 concurrent programming을 간단하게 만드려는 방식
    - 특히 shared memory에 대한 처리
- 특징
  - low-level thread synchronization에 비해서 더 높은 추상화로 구현
