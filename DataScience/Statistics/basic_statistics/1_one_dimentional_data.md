# 일차원 데이터

- 개체 & 데이터 & 일차원 데이터
- 일차운 데이터의 분석
  - 그래프 / 대표값
  - 기술 통계학
- 일차원 데이터 분석의 그래프적 관점
- 일차원 데이터 분석의 대표값적 관점
  - 대표값
  - 분포의 척도

---

- 통계데이터는 무엇인가를 이야기 하고 있는 것이므로, 전람회에서 그림을 보듯이 일단은 전체를 주망하여, 서서히 자세히 바라보아야 함

## 개체 & 데이터 & 일차원 데이터

- 개체
  - 관측되는 대상
- 데이터
  - 개체의 관측값들을 모아둔 것
  - (x1, x2, x3, ... xn) 와 같은 벡터로 표현 가능
- 일차원 데이터
  - 각 객체에 대하여 얻어진 데이터 중 한 종류의 데이터만 주목한 것

개체 -> 데이터 -> 다차원 데이터(관계) / 일차원 데이터(기술 통계)

## 일차원 데이터의 분석

- 일차원데이터의 분석
  - 그래프
    - 커뮤니케이션의 방법
  - 대표값
    - 보다 객관적인 분석
- 기술통계학
  - 집단으로서의 특징을 기술하기 위하여, 관측 대상이 된 각 개체에 대하여 관측하여 얻게 된 데이터를 정리 / 요약하는 방법
  - 관측
    - 넓게 조사나 실험
  - 데이터
    - 개체의 관측값을 모은 것
    - (x1, x2, x3 ... ) 등으로 표현
    - 그 특성중 하나의 특성에 집중하여서, 그것의 모든 개체 즉 집단에 관한 정리 / 요약을 하면 그것이 1차원 데이터 분석
      - 2종류 이상의 특성과 그 **관계** 는 다차원 분석

## 일차원 데이터 분석의 그래프 적 관점(도수분포와 히스토그램)

- 관측값을 얻으면 가장 먼저 도수분포표나 히스토그램 작성
  - 계급
    - 관측값이 갖을 수 있는 값을 분류한 것
  - 도수
    - 계급당 관측값의 개수
  - 계급값
    - 계급을 대표하는 값
    - 보통은 계급의 최대, 최소, 중간값
  - 상대도수
    - 데이터 전체를 1로 했을때, 각 계급에 속하는 관측값 개수의 전체에서의 비율
    - **데이터의 크기가 다른 복수의 데이터 분포를 비교**
  - 누적도수 / 누적 상대도수
    - 도수를 가장 아래의 계급에서 부터 순서대로 더해나갈 때의 도수 혹은 상대도수의 누적 합
    - e.g 소득의 경우 450만엔 미만의 세대가 전체의 몇 퍼센트인지? 가 중요함
- 히스토그램
  - 히스토그램은 어떠한 일차원 데이터에 대하여 각 계급마다의 도수를 가시화 한 것
  - 형태
    - 오른쪽(왼쪽)에 기울어진 그래프
      - 오른쪽으로 길게 늘어진 그래프(값이 왼쪽으로 치우쳐짐)
    - 쌍봉형(bimodal)
      - 성질이 다른 데이터가 섞여있을 가능성 높음
      - 그럴때는 데이터를 적절히 분류해서 단봉형(unimodal)로 만들어줌
      - e.g 남여를 섞어놓은 신장 그래프
  - 주의
    - 계급의 수, 계급 폭
    - 계급수
      - **스타제스 공식**
      - 계급수 k = 1 + log2(n)
    - 계급폭
      - 도수가 몰린 계급을 보고 판단
  - bar chart
    - 개체당 각 종류의 데이터의 관측값을 가시화 한 것
- 로렌츠 곡선
  - 사업소 수(%) 에 대한 종업자 수 (%)
  - 대도시 인구 수 (%)에 대한 소유 토지 면적(%)
  - 불평등도를 나타냄

## 일차원 데이터 분석의 대표값 적 관점

### 대표값

- 분포를 대표하는 값. 수량적 개념. 계산할 수 있고 커뮤니케이션 할 수 있는 장점
- **위치를 나타내는 지표**
- 평균(mean)
  - 산술평균
    - 도수분포표에서는 **시그마(계급값 * 도수) / 총도수** 로 구함(근사값)
    - 그러나 위 아래가 뚫린 도수분포표에서는 계산할 수 없음
      - 방법1: 이상값(outlier)로 취급해서 무시(비율이 적을때만)
      - 방법2: 계급값을 적당히 주어줌
        - 아래: 0
        - 위: 그전 계급값들의 폭과 같은 수준
  - 기하평균
    - 집값이 5년간 매년 21.8%, 30.%, 53.6%, 50.0%, 12.9%상승하면 매년 평균 몇퍼센트 상승한 것인가?
      - root5(1.218 * 1.305 * 1.536 * 1.50 * 1.129) == 1.328
      - 평균 매년 32.8%상승한 것
  - 조화평균
    - 버스가 어떠한 거리를 갈떄는 시속 25km 올때는 시속 15km로 왕복하면 평균시속은?
    - 18.75km/h
- 중앙값(median)
  - 관측값을 작은 순부터 나열했을때 가운데에 있는 값
  - 짝수개의 데이터가 존재할 경우는 m번째와 m+1번쨰의 평균을 중앙값으로 함
  - 평균과 다르게 outlier의 영향을 받지 않음
  - 데이터가 많은 경우는 데이터 정렬에 시간이 많이 걸리므로 도수분포표에서 계급사이의 값들이 선형적으로 증가된다고 가정하고 게산
- 분위점(percentile)
  - 관측값을 작운 순부터 나열했을때 작은 순서로부터 100p%(0<=p<=1)에 있는 값을 100p퍼센타일(percentile)혹은 (백)분위점이라 함
  - 제1 사분위점 Q1: 25%
  - 제2 사분위점 Q2: 50%
  - 제3 사분위점 Q3: 75%
- 최빈값(mode)
  - 데이터 분포에서 가장 많이 등장하는 데이터
  - 도수분포표에서는 도수가 가장 큰 계급의 계급값
- 미드레인지(mid-range)
  - 최대값과 최솟값 사이의 범위의 중간값

### 분포의 척도

- 분포의 위치 뿐 아니라 **형태를 나타내는 지표** 가 필요함
- **위치의 지표(대표값)와 분포의 지표를 알아내면 대강 그래프를 그릴 수 있음**
- 범위(range)
  - 분포가 존재하는 범위
- 사분위편차(quartile deviation)
  - `Q = 1/2*(Q3 - Q1)`
  - 제3 사분위점과 제1 사분위점의 간격의 절반
- 평균편차(mean deviation)
  - `d = 1/n(|x1-mean| + |x2-mean| + ... )`
  - 원래 측정 단위 유지
- 분산(variance)
  - `S^2 = 1/n((x1-mean)^2 + (x2-mean)^2 + ...)`
  - 측정 단위 변화
- 표준편차(standard deviation)
  - `S = root(S^2)`
  - 평균편차보다 이론적으로 다루기 쉬움
- 변동계수(coefficient of variation)
  - e.g 1965년 현 평균소득 26.6만엔이고 표준편차가 7.5, 1975년 현 평균소득 117.5만엔 이고 표준편차가 23.8만엔이면 지역간 소득격차가 커졌다고 할 수 있는가?
    - 이렇게 평균이 커지면 표준편차도 커지는 문제가 발생
  - cv = s/mean
  - 계산해보면 오히려 지역격차는 줄어듬
- 표준득점
  - 평균: 0, 표준편차: 1로 변환
  - `z = (xi - mean) / s`
- 편차치득점
  - 평균: 50
  - 표준편차: 10
  - `T = 10*zi(표준득점) + 50`
