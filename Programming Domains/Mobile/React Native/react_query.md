# React Query

- 의문
- 개요
  - 기본 특징

## 의문

## 개요

### 기본 특징

- `useQuery`나 `useInfiniteQuery`의 쿼리 인스턴스는 디폴트로는 캐시 데이터를 stale하다고 판단함
  - 변경하려면, `staleTime`옵션을 줘야 함
  - c.f) stale 쿼리들이 백그라운드에서 자동적으로 refetch되는 경우
    - _New instances of the query mount_
    - 윈도우가 다시 포커싱 될 때
    - 네트워크가 다시 연결될 때
    - 쿼리가 refetch interval이 설정되었을 때
- 디폴트로 inactive 쿼리는 5분뒤에 가비지 컬렉팅 됨
  - 변경하려면, `cacheTime`을 `1000 * 60 * 5`와는 다르게 줘야 함
- 실패한 쿼리는 3회에 걸쳐서 exponential backoff delay로 재시도를 함
  - 변경하려면, `retry`와 `retryDelay`옵션을 변경해야 함
- 쿼리의 결과가 structually 공유되어서, 실제로 데이터가 변경되었는지 보고, 만약 변경되지 않았다면 데이터 reference는 그대로 변경되지 않은 채로 둠
  - `useMemo`, `useCallback`등의 최적화
