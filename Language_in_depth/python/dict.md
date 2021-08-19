# Dict

- 의문
- dict의 구현

## 의문

## dict의 구현

- 개요
  - hash tables로 구현됨
  - hash collision을 극복하기 위한 방법
    - **open addressing**
  - 해시 테이블
    - 각 slot에는 하나의 entry만 저장 가능
    - entry
      - hash, key, value의 조합(C struct으로 구현)
  - 첫 dict는 8개의 slot으로 이니셜라이징
  - entries를 table에 추가
    - `i = hash(key) & mask`
    - if) 슬롯이 비어있는 경우, entry를 추가
    - if) 슬롯이 차 있는 경우
      - => hash와 key를 동시에 비교(`==`)
        - if) 둘다 일치 => 새 entry를 해당 slot에 넣음
        - if) hash나 key가 일치 안함 => random probing함
  - entries를 table에서 찾기
    - `i = hash(key) & mask`
    - random probing
  - dict의 2/3이 꽉차면, resizing함
    - 리사이징하면, 기존에 있던 엔트리들은 그 주소 그대로 있는것인지? 아니면, 그것들 전부다 주소를 바꿔주는지?
      - 기존에 있던 엔트리들은 그 주소 그대로 재사용
    - 만약 hash table이 주소를 100까지 갖고 있고 siphash의 값은 10만이 넘어가는 output이라면, dict가 resize될 때 나머지로 주소값을 정해주는 것인지?
      - 그렇다
- c.f) `hash()`
  - hashable한 자료구조를 input으로 넣어서, 정수인 해시값을 반환
  - *각 자료구조마다 다르게 구현되어있음*
    - string의 경우, unicodeObject로, siphash라는 알고리즘을 사용
- c.f) siphash
  - 개요
  - 특징
    - seedkey를 추가로 받아, 프로세스가 랜덤하게 seedkey를 생성하므로, 동일한 key에 다른 hash값을 생성
      - 슬롯 충돌 유도 힘듬
    - input의 길이에 선형적으로 비례해서 해시함수의 계산복잡도 상승
