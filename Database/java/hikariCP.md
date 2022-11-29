# HikariCP

- 의문
- 개요

## 의문

## 개요

## 옵션

- `connection_timeout`
  - 풀에서 커넥션을 얻어오기전까지 기다리는 최대시간
  - default: 30s
- `idleTimeout`
  - default: 10m
  - 오직
- `maxLifeTime`
  - 커넥션 풀에서 살아있을 수 있는 커넥션의 최대 수명시간
  - 사용중인 커넥션은 maxLifeTime에 상관없이 제거되지 않음
  - 커넥션 벌 적용
    - 대량 커넥션 제거 방지
  - default: 30m
- `minimumIdle`
  - 아무것도 하지 않아도 해당 값 size로 커넥션을 유지해줌
  - default: `maximumPoolSize`와 같음
- `maximumPoolSize`
  - 풀에 유지시킬 수 있는 최대 커넥션 수. 풀의 커넥션 수가 옵션값에 도달하면 idle인 상태는 존재하지 않으
  - default: 10
- `poolName`
  - 풀의 이름을 지정
- `readOnly`
  - 풀이 커넥션을 획득할 때 read-only모드로 가져옴
    - DB가 지원해줘야 함
  - 일부 쿼리들의 최적화

## 성능 팁

-
