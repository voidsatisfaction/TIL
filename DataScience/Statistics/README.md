# 통계 기초

- 좋은 자료들
- 통계학
  - 통계학 vs 데이터 과학
  - 통계적 사고관
  - 통계 데이터와 통계 수법
  - 통계데이터의 분석 프로세스

## 좋은 자료들

- [통계청](http://kostat.go.kr/portal/korea/index.action)
  - [통계청 저널 통계 연구(논문)](http://kostat.go.kr/understand/info/info_pct/1/1/index.action)
  - [직장 내 성희롱 피해 대응방식에 관한 연구](http://kostat.go.kr/file_total/eduSri/23-4-04.pdf)
- [헬로 데이터 과학](http://www.hellodatascience.com/?p=690)
- [권재명님 블로그](https://dataninja.me/)

## 통계학

- 통계
  - 의의
    - **현 현상을 파악 / 미래를 예측 / 의사 결정의 도구**
  - **현상의 법칙성을 파악**
  - 넓게 주어져 있는 데이터를 정리하여, 유용한 정보(information)을 이끌어내는 학문
    - 데이터의 성질에 따라서 분류
- 근대 통계
  - 인간 중심의 통계학
  - 기술통계학
    - 수집한 데이터를 묘사, 설명
  - 통계적추측
    - 수집한 데이터에서 새로운 것을 추론, 예측
- 현대 통계
  - 과학적 추론
  - 다양한 분야에 접목
- 부분이 올바르게 선택되어있다면, 그것으로부터 전체를 아는 것이 논리적으로 가능.
  - 부분은 전체의 일부일 뿐이나, 전체를 반영
  - 부분과 전체의 갭을 매우는 것은 **확률(논리 장치)**

### 통게학 vs 데이터 과학

- 통계학은 학문
- 데이터 과학은 행동
  - 모형을 세워서, 잡음 속에 숨어 있는 신호, 즉, 진실을 파악해 내는, 객관적이고 합리적인 진실을 추구하는 학문
  - 탄탄한 통계적 지식 + 컴퓨터 툴(코딩 머신러닝) + 현실에 적용
  - 업무
    - 자료 분석 / 자료 준비 / 커뮤니케이션
  - 결국은 다른 분야를 도와주는 도우미
    - 어떤 비즈니스 문제를 풀어야 하는가?
    - 어떤 데이터가 있는가?
    - 필요한 데이터를 어떻게 취득할 수 있는가?
    - 데이터를 어떻게 가공할 수 있는가?
    - 어떤 데이터가 필요한지?

### 통계적 사고관(세계관)

- 예시
  - 통계적 사고관이 있는 사람
    - 데이터 = 신호(truth, 진실) + 잡음
  - 통계적 사고관이 없는 사람
    - 데이터 = 신호(truth)
- 통계적 사고관 이란
  - 1 `데이터 = 신호 + 잡음` 이라는 이해
    - 데이터는 100% 진실이 아니다.
  - 2 불확실성을 인정
    - 불확실성을 명시하는 겸손한 학문
  - 3 관측된 데이터는 여러가지 값들 중 하나라고 생각
    - 평행 우주론과 비슷
    - e.g) CEO중에 키큰 사람들이 많다
      - 해당 사람이 키큰 사람으로 태어난 평행우주
      - 해당 사람이 키작은 사람으로 태어난 평행우주
      - 등에서 몇개의 우주에서 이 사람이 CEO가 되는가

### 통계 데이터와 통계 수법

- 데이터의 성질에 따라서 다른 통계 수법이 존재
- 1) 양적 데이터와 질적 데이터
  - 양적 데이터
    - 수치를 직접 측정하는 것들
  - 질적 데이터
    - 수치를 직접 관측하는 것이 아님
- 2) 1차원 데이터와 다차원 데이터
  - 1차원 데이터
    - e.g 학생 한 명 한 명에 대한 신장 조사
    - **도수분포표를 그리거나, 평균과 같은 대표값이나 분산을 구해서 분석을 함**
  - 다차원 데이터
    - e.g 학생 한 명 한 명에 대한 신장과 체중 조사: 2차원 데이터
    - e.g 학생 한 명 한 명에 대한 신장과 체중과 성별 조사: 3차원 데이터
    - **속성간의 상호관계의 분석이 중요**
    - 분할표를 사용해서 **상관/회귀 분석**
- 3) 시계열 데이터와 크로스 섹션(cross section)데이터
  - 시계열 데이터
    - 동일 대상을 다른 시점에 관측한 값으로부터 생기는 데이터
  - 크로스 섹션 데이터
    - 서로 다른 대상에 대해서 조사나 실험을 행해서 관측값을 얻은 경우의 데이터

### 통계데이터의 분석 프로세스

**데이터 수집보다 데이터를 바탕으로 분석할 가설을 세우는 것이 먼저임**

- 분석을 행할 가설을 세움
- 데이터 수집
  - 자연과학: 실험(experiment)
  - 사회과학: 조사(survey)
  - 보통은 비용때문에 기존의 가공된 통계자료를 사용하는 경우도 많음
  - 통계자료
    - 제1의 통계
      - 통계 자료를 작성할 목적으로 조사를 하는 경우
      - 국가 조사보고
    - 제2의 통계
      - 통계 자료를 작성할 목적이 아닌데 모인 데이터 통계
      - e.g 범죄통계, 무역통계
    - 2차 통계
      - 통계 자료로부터 가공해서 작성된 통계자료
      - e.g 물가지수
- 데이터 분석
  - 컴퓨터를 이용한 분석
- 피드백
  - 분석한 데이터를 바탕으로 정보를 얻어서 새로운 가설을 세우거나 기존 가설 수정
- 주의
  - 데이터의 정의
  - 통계 수법의 선택
  - 결과의 표현
