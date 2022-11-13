# 프로메테우스(서버)

- 의문
- 개요
- 아키텍처
  - 스토리지(DB)

## 의문

## 개요

## 아키텍처

- Storage(DB)
  - local
  - remote(e.g RDB)
- Data Retrieval worker
  - pulling
  - save to storage
- HTTP Server
  - 쿼리를 받아서 데이터 돌려줌
  - PromQL 쿼리를 사용

### 스토리지(DB)

프로메테우스 서버의 데이터 디렉터리 구조

```
./data
├── 01BKGV7JBM69T2G1BGBGM6KB12
│   └── meta.json
├── 01BKGTZQ1SYQJTR4PB43C8PD98
│   ├── chunks
│   │   └── 000001
│   ├── tombstones
│   ├── index
│   └── meta.json
├── 01BKGTZQ1HHWHV8FBJXW1Y3W0K
│   └── meta.json
├── 01BKGV7JC0RY8A6MACW02A2PJD
│   ├── chunks
│   │   └── 000001
│   ├── tombstones
│   ├── index
│   └── meta.json
├── chunks_head
│   └── 000001
└── wal
    ├── 000000002
    └── checkpoint.00000001
        └── 00000000
```

- 메모리
  - 개요
    - 현재 최근 2시간 이내의 최신으로 들어오는 샘플들은 메모리에 저장(buffer)되고, 전체가 다 영속화되지는 않음
      - WAL(Write Ahead Log)를 두어서, 서비스 크래시에 대비함
  - c.f) WAL
    - 개요
      - 메모리에만 있는 2시간 이내의 최신 셈플들을 시스템 크래시에 대비해서 로컬 스토리지에 저장해둠
        - `wal`디렉터리에 128MB 세그먼트로
    - 특징
      - 해당 세그먼트들은 raw data이고, compact되지 않아서, regular block file보다 훨씬 크기가 큼
      - 프로메테우스는 적어도 2시간의 raw data를 저장하기 위해서 최소한 3개의 WAL을 준비해둠
- 로컬 스토리지
  - 개요
    - 프로메테우스의 로컬 시계열 데이터베이스는 매우 효율적인 포맷으로 로컬 스토리지에 저장
  - 데이터 구조
    - 최소 두시간 블록(`01BKGV7JBM69T2G1BGBGM6KB12`)
      - *윈도우 타임마다의 데이터 청크*(`chunks`)
        - *정확한 의미는?*
        - 512MB까지의 세그먼트 파일로 그루핑됨(default)
        - API로 인한 삭제시에는, chunk segment를 즉시 삭제하지 않고, tombstone files로 저장됨
      - 메타데이터 파일(`meta.json`)
      - 인덱스 파일(`index`)
        - 메트릭 이름과 레이블을 타임시리즈에 인덱싱한 것
  - 특징
    - 자동으로 스케일링 불가
    - RAID를 구성해서 스토리지 availability를 확보해야 함
    - 백업을 위한 스냅샷 사용 추천
  - 통합(compaction)
    - 첫 두시간 블록들은 백그라운드에 있는 더 긴 블록들과 통합됨
      - 통합된 블록은 `min(10%의 retention time 사이즈, 31일치 사이즈)`까지 크기가 됨
- 운영적 측면
  - 커맨드
    - `--storage.tsdb.path`
      - 데이터베이스 파일을 어디에 작성할 것인지(default `data/`)
    - `--storage.tsdb.retention.time`
      - 이전 데이터를 언제 지울지(default `15d`)
    - `--storage.tsdb.retention.size`
      - 보관할 스토리지블록들의 최대 바이트수
        - 오래된 것들부터 지워나감
        - WAL과 m-mapped head chunk도 사이즈에 고려하지만, 지워지는건 persistent block만
    - `--storage.tsdb.wal-compression`
      - WAL 압축, 약간의 CPU load를 추가하고, 사이즈를 거의 절반으로 줄임
  - 데이터 저장 샘플의 속도 줄이기
    - `needed_disk_space = retention_time_seconds * ingested_samples_per_second * bytes_per_sample`
      - fewer target / fewer series per target
      - increase scrape interval
  - 스토리지가 corrupt되었을 때
    - 1 개개의 블록 디텍터리를 지우기
      - 블록 디렉터리 하나 당 대략 두시간의 데이터가 지워지는 것(WAL도 마찬가지)
    - 2 WAL 디렉터리 지우기
    - 3 프로메테우스를 끄고, 모든 storage directory를 지우기

리모트 스토리지 지원

![](./images/remote_storage1.png)

- c.f) 리모트 스토리지 지원
  - 개요
    - 프로메테우스는 리모트 스토리지 시스템을 지원
  - 방식
    - 프로메테우스는 소화한 샘플들을 remote URL에 표준화된 형태로 작성 가능
    - 프로메테우스는 다른 프로메테우스 서버로부터 표준화된 형태로 샘플을 받을 수 있음
    - 프로메테우스는 표준화된 형태로 remote URL로부터 샘플 데이터를 읽을 수 있음
  - 특징
    - 결국은 모든 필요한 데이터를 가져와서 프로메테우스 서버에서 가공해야 함

타노스(Thanos)

- 개요
  - 오픈소스 고가용성 프로메테우스 장기 스토리지 기능
- 특징
  - 다양한 서버와 클러스터에 있는 프로메테우스 메트릭을 쿼리 가능하게 함
  - 무제한 보관
    - S3지원
  - 프로메테우스 생태계 지원(Grafana, ...)
  - 다운샘플링 & 데이터 통합
    - 긴 기간 쿼리 시 효율성 증대

### 서비스 디스커버리

- 개요
  - 수집할 메트릭 서비스를 찾는 방법
- 종류
  - File based
    - 스크래이핑 할 타겟을 JSON 파일로 관리
  - HTTP
    - 스크래이핑 할 타겟을 JSON resopnse로 관리
  - K8s
