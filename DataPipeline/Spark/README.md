# 스파크

- 의문
- 스파크
- 스파크RDD
- 스파크SQL

## 의문

## 스파크

### 개요

- 빅데이터 분산처리 프레임워크
  - 매우 큰 데이터 집합을 대상으로 빠르게 처리 작업을 수행
  - 다른 분산 컴퓨팅 툴과 조율해서 데이터 처리 작업 분산 처리
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

### 아키텍처

스파크 클러스터 다이어그램

![](./images/spart_cluster_overview.png)

- 구성 요소
  - cluster manager
    - driver와 executor를 중재(리소스 매니징)
    - 하둡 YARN, Kubernetes 등
  - driver
    - 사용자의 코드를 여러 작업자 노드로 배분할 수 있는 여러 작업으로 변환
  - executor
    - 코드가 실행되면서 할당된 작업 수행
- 동작
  - 스파크 애플리케이션(SparkContext단위)은 클러스터에서 독립된 프로세스의 집합으로 동작
    - 메인 프로그램(driver program)의 `SparkContext`오브젝트에 의해서 조율됨
      - 애플리케이션들에게 자원을 할당해주는 역할도 함
  - `SparkContext`는 다양한 타입의 cluter manager와 결합할 수 있음
  - 결합이 되면, `SparkContext`는 애플리케이션 코드(JAR or Python file)를 executor에 보냄
  - `SparkContext`가 executor에게 태스크를 보내서 실행하게 함
- 특징
  - 각 애플리케이션은 자신만의 executor processes를 갖음
    - 전체 애플리케이션동안 살아있고, 멀티 스레드에서 태스크 수행
    - 스파크 애플리케이션끼리는 격리되어 있으며, 데이터가 공유되려면 external storage system을 사용해야함(S3 같은 것들)
  - Spark는 주어진 cluster manager와는 agnostic함
  - driver 프로그램은 생애주기동안 executor들의 들어오는 연결을 받을 수 있어야 함(네트워크 주소로 접근가능해야 함)
  - driver 프로그램이 executor들에게 태스크를 스케쥴링 하므로, worker node에 최대한 물리적으로 가까이 존재해야 함
    - 되도록이면 같은 LAN
    - 원격으로 cluster에게 요청을 보내고 싶으면, worker node와 가까운 위치에 위치한 driver에 RPC를 열어서 operation을 submit하는게 나음
- 원리
  - 사용자의 데이터 처리 명령을 DAG로 만듬
    - 어느 작업이 어느 노드에서 어느 순서로 실행되는지 결정
  - 드라이버 코어 프로세스가 스파크 애플리케이션을 여러 작업으로 분할해 다수의 executor프로세스로 분배하면 executor프로세스가 작업 수행
    - executor는 애플리케이션의 필요에 따라서 확장 / 축소 가능

### Submit

- 개요
  - 스파크 애플리케이션은 `spark-submit`스크립트를 사용해서 어떤 타입의 클러스터에든 제출 가능
    - 이 이야기는, 클러스터 구성만 하면, 알아서 실행을 나눠서 잘 해준다는 느낌

### 데이터 구조

- 과거
  - RDD(Resilient Distributed Data)
- 최신
  - Dataframe
  - Dataset

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
  - 데이터 집합 조인, 필터링, 샘플링, 집계 가능

### 스파크SQL

- 개요
  - 정형 데이터 프로세싱을 위한 스파크 모듈
  - DataFrame이라는 프로그래밍적 추상화를 제공하고, 분산 SQL 엔진의 역할도 함
