# HikariCP

- 의문
- 개요
- 옵션
- 성능 팁

## 의문

## 개요

## 옵션

- `connection_timeout`
  - 풀에서 커넥션을 얻어오기전까지 기다리는 최대시간
  - default: 30000(30s)
- `idleTimeout`
  - 풀에서 사용되지 않는 커넥션을 유지하는 기간
  - minimumIdle이 maximumPoolSize보다 작게 설정되어있을 때만 설정
  - default: 600000(10m)
- `maxLifeTime`
  - 커넥션 풀에서 살아있을 수 있는 커넥션의 최대 수명시간
  - 사용중인 커넥션은 maxLifeTime에 상관없이 제거되지 않음
  - 커넥션 별 적용
    - 대량 커넥션 제거 방지
  - default: 30m
- `minimumIdle`
  - 아무것도 하지 않아도 해당 값 size로 커넥션을 유지해줌
    - 그냥 디폴트로 두는게 좋음
  - default: `maximumPoolSize`와 같음
- `maximumPoolSize`
  - 풀에 유지시킬 수 있는 최대 커넥션 수. 풀의 커넥션 수가 옵션값에 도달하면 idle인 상태는 존재하지 않음
  - default: 10
- `poolName`
  - 풀의 이름을 지정
  - default: 자동 생성
- `readOnly`
  - 풀이 커넥션을 획득할 때 read-only모드로 가져옴
    - DB가 지원해줘야 함
  - 일부 쿼리들의 최적화
  - default: false
- `autoCommit`
  - 오토커밋 설정
  - default: true

## 성능 팁

- 공식 문서
  - `prepStmtCacheSize`
    - MySQL드라이버가 매 커넥션마다 캐싱하는 prepared statements의 개수
    - default: 25
    - 권장: 250-500
  - `prepStmtCacheSqlLimit`
    - 드라이버가 캐시할 수 있는 prepared SQL statement의 최대 길이
    - default: 256
    - 권장: 2048(hibernate같은 orm쓰는 경우에는 256은 터무니없이 부족)
  - `cachePrepStmts`
    - prepStmtCache를 활성화하려면 true로 해줘야 함
    - default: false
    - 권장: true
  - `useServerPrepStmts`
    - server-side prepared statement를 사용할지에 대한 여부
      - *단점이 없는지 체크해야 함*
    - default: false
    - 권장: true
