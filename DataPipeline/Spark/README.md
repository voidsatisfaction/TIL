# 스파크

- 의문
- 스파크
- 스파크SQL

## 의문

## 스파크

- 개요
  - 빅데이터 분산처리 프레임워크
    - 매우 큰 데이터 집합을 대상으로 빠르게 처리 작업을 수행
    - 다른 분산 컴퓨팅 툴과 조율해서 데이터 처리 작업 분산 처리
- 아키텍처
  - 구성 요소
    - cluster manager
      - driver와 executor를 중재
      - 하둡 얀
    - driver
      - 사용자의 코드를 여러 작업자 노드로 배분할 수 있는 여러 작업으로 변환
    - executor
      - 코드가 실행되면서 할당된 작업 수행
  - 원리
    - 사용자의 데이터 처리 명령을 DAG로 만듬
      - 어느 작업이 어느 노드에서 어느 순서로 실행되는지 결정
- 데이터 구조
  - RDD(Resilient Distributed Data)
  - Dataframe
  - Dataset
- 매니지드 솔루션
  - Amazon EMR
  - GCP Dataproc
  - Azure HDInsight
- Spark vs Hadoop
  - 기본적으로 이 비교는 다소 부적절
    - 하둡 배포판에 스파크가 포함됨
      - *그럼 정확하게 어떤 관계인가?*
  - Spark이점
    - 속도
      - 인메모리 데이터 엔진을 통해 특정 상황에서 MapReduce보다 100배 더 빠르게 작업 가능
      - 단계간에 디스크에 상태를 써야하는 다단계 작업에서 성능차이가 두드러짐
    - 개발자 친화적 API
      - 분산 처리 엔진이 갖는 복잡함의 대부분을 간단한 메서드 호출 뒤로 숨김

개발자 친화적인 코드 예시

```scala
/* 문서의 단어 수를 세는 코드(맵리듀스는 50줄짜리) */
val textFile = sparkSession.sparkContext.textFile(“hdfs:///tmp/words”)
val counts = textFile.flatMap(line => line.split(“ “))
                      .map(word => (word, 1))
                      .reduceByKey(_ + _)
counts.saveAsTextFile(“hdfs:///tmp/words_agg”)
```

### 스파크RDD(Resilient Distributed Database)

- 개요
  - 컴퓨팅 클러스터 전역으로 분할할 수 있는 불변성 객체 모음을 나타내는 프로그래밍 추상화
    - 클러스터 전반에서 분할되어 병렬 배치 프로세스로 처리가 가능
      - 속도
      - 확장성
- 특징
  - 간단한 텍스트 파일, SQL 데이터베이스, NoSQL 스토어, 아마존 S3버킷을 비롯해 다른 많은 방법으로 만들 수 있음

### 스파크SQL

- 개요
  - 정형 데이터 프로세싱을 위한 스파크 모듈
  - DataFrame이라는 프로그래밍적 추상화를 제공하고, 분산 SQL 엔진의 역할도 함
