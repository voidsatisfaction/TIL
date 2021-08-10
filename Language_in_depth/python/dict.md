# Dict

- 의문
- 해시 함수
- dict의 구현

## 의문

## 해시 함수

- 개요
  - 임의의 길이의 데이터를 고정된 길이의 데이터로 매핑하는 함수
    - `f: message -> digest`
- 기능
  - 가변 길이의 키를 고정 길이 값으로 변환
  - 결과 값이 키 공간에 균일하게 분포되도록 키의 비트를 스크램블함
  - 키 값을 테이블 크기보다 작거나 같은 값으로 매핑
- 좋은 해시 함수의 조건
  - 계산이 빨라야 함
  - 충돌이 적어야 함
- 응용
  - 해시 자료구조
  - HMAC
  - 암호화
    - 패스워드 등
- 종류
  - *MD5*
    - 왜 안쓰게 되었나?
  - SHA256
  - siphash

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
- c.f) `hash()`
  - hashable한 자료구조를 input으로 넣어서, 정수인 해시값을 반환
  - *각 자료구조마다 다르게 구현되어있음*
  - string의 경우, unicodeObject로, siphash라는 알고리즘을 사용
- c.f) siphash
  - 개요
  - 특징
    - seedkey를 추가로 받아, 프로세스가 랜덤하게 seedkey를 생성하므로, 동일한 key에 다른 hash값을 생성
      - 슬롯 충돌 유도 힘듬
