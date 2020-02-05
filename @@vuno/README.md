# @@VUNO

- 의문
- 알아두면 좋은 용어들
  - Research
  - Medical term
  - Domain
    - ASR
    - Signal

## 의문

- *ASR과 NLP의 차이는?*

## 알아두면 좋은 용어들

### Research

[참고](http://www.cbgstat.com/method_sensitivity/sensitivity.php)

- 민감도(sensitivity) & 특이도(specificity)
  - 개념
    - Sensitivity
      - **질병이 있는 사람을 얼마나 잘 찾아 내는가에 대한 값**
      - 양성(질병이 있는 개체)에 대해 양성이라고 진단하는 비율
    - Specificity
      - **정상인 사람을 얼마나 잘 찾아 내는가에 대한 값**
      - 음성에 대해 음성이라고 판단하는 비율
  - 특징
    - 좋지 않은 진단 방법일 경우 한 쪽이 증가하면 다른 한 쪽이 감소
      - 민감도와 특이도 둘 다 높은 진단 방법을 찾는 것이 관건
    - 질병인지 아닌지 이미 정답을 알고 있는 개체(이미 잘 알려진 진단 방법(gold standard))를 이용하여 새로운 진단 기기의 성능을 시험하는 상황에서 필요한 개념
      - True Positive(TP)
        - 새로운 진단 방법(양성 - 질병), 실제(양성)
        - **새로운 진단 방법이 양성으로 판단했는데, 그것은 진짜로 맞는 결과다**
      - True Negative(TN)
        - 새로운 진단 방법(음성 - 정상), 실제(음성)
      - False Positive(FP)
        - 새로운 진단 방법(양성), 실제(음성)
      - False Negative(FN)
        - 새로운 진단 방법(음성), 실제(양성)
    - 수식
      - Accuracy
        - `(TP + TN) / (TP + FP + FN + TN)`
          - gold standard와 얼마나 유사한 판단을 했는가
          - *FP, FN가 비슷한 cost를 가질 때 유용*
            - *무슨소리고 왜?*
      - Precision
        - `TP / (TP + FP)`
      - Sensitivity(Recall)
        - 환자라고 판명한 사람 중 진짜 환자인 사람 / 실제로 환자인 사람의 수
          - `TP / (TP + FN)`
      - Specificity
        - 정상인이라고 판명한 사람 중 진짜 정상인인 사람 / 실제로 정상인인 사람의 수
          - `TN / (TN + FP)`
      - F1 score
        - `2 * Recall * Precision / (Recall + Precision)`
          - Precision과 Recall의 weighted average
            - 1에 가까울 수록 낮은 false positives, 낮은 false negative
          - uneven class distribution을 갖을 때, accuracy보다 유용
          - Recall과 Precision의 조화평균
    - 질병의 특징에 따라서 민감도를 높일 것인지 특이도를 높일 것인지를 고려하기도 함
      - 매우 심각한 질병 => 민감도를 높임 대신 재검사를 실시해서 FP를 줄임

### Medical term

- clinician
  - 임상의
- CAD(Computer-Aided Detection)
  - 개요
    - 소프트웨어를 이용하여 영상의학 진단에 도움을 주는 프로그램
- EMR(Electronic Medical Record) & EHR(Electronic Health Record) & EPR(Electronic Patient Record)
  - 개요
    - 디지털 형태로 체계적으로 수집되어 전자적으로 저장된 환자 및 인구의 건강정보
    - 포함되는 데이터
      - 병력, 약물복용 및 알레르기, 예방접종 상태, 검사실 검사결과, 영상의학 이미지, 생체징후, 나이, 성별, 청구정보
- ECG(Electrocardiogram)
  - 개요
    - 심전도. 심장의 전기적 활동을 해석한 것

X-ray PA vs AP

![](./images/x-ray-pa-ap.jpg)

- X-Ray
  - Chest PA(Posterior Anterior) vs Chest AP(Anterior Posterior)
    - Chest PA
      - 흉부 X-ray를 뒤에서 앞으로 찍음
      - 먼 거리에서 촬영하기 때문에 상이 작고 선명하게 촬영
      - 반듯이 서 있을 수 있는 경환자 or 일반인에게 시행
    - Chest AP
      - 흉부 X-ray를 앞에서 뒤로 찍음
      - 가까운 거리에서 촬영하기 때문에 상이 크고 흐릿하게 촬영
        - portable X-ray 기기 사용하기 때문에 먼 거리 촬영 어려움
      - 반듯이 설 수 없고 검사실까지 거동할 수 없는 중환자 or 소아 환자에게 시행 -> 누운자세 or 반좌위 자세로 촬영

### Domain

ASR시스템의 통계적 모델링

![](./images/asr_statistical_modeling1.png)

ASR시스템의 구조

![](./images/asr_system_structure1.png)

Backend processing의 Decoding 프로세스는 주로 train된 AM / LM을 사용하여 최적의 output character sequence를 얻는 것

AM에서의 deep learning 등장

![](./images/asr_gmm-hmm-to-dnn-hmm.png)

#### ASR(Automatic Speech Recognition)

- AM(Acoustic Model)
  - 개요
    - Acoustic Model로서, 음성 신호와 음소 또는 음성을 구성하는 다른 언어 단위간의 관계를 나타내기 위해 음성 인식에 사용됨
    - 오디오 녹음 및 해당 녹음의 transcription으로부터 학습
    - 소리의 통계적 표현을 생성하여 각 단어를 구성
      - *통계적 표현이 무엇일까*
    - `p(O|W)`를 계산 하는 것
      - 모드에 대한 음성 파형을 생성할 확률을 계산
      - 오버 헤드의 상당 부분을 차지하며, 시스템 성능을 결정함
        - (GMM-HMM (Gaussian Mixture Model - Hidden Markov Model))기반 AM이 전통적인 음성 인식 시스템에서 널리 사용
        - DNN-HMM(Deep Neural Network - Hidden Markov Model)
            - GMM-HMM 과 비쇼하여 TIMIT dataset에서 우수한 성능을 보임
            - Convolutional Neural Network / Recurrent Neural Network 의 사용으로 AM modeling을 크게 향상
            - LSTM 활용
- LM(Language Model)
  - 개요
    - 언어의 단어단어 시쿼스 모델링
- 최신 음성 인식 시스템
  - AM과 LM을 둘다 활용하여 음성의 통계적 특성을 나타냄
  - AM과 LM이 결합되어, input으로 주어진 오디오 세그먼트에 해당되는 top-ranked 단어 시퀀스를 얻는 역할을 함
    - *무슨 뜻?*
- 목적
  - **입력 waveform sequences를 해당 단어 또는 character sequences에 매핑**
    - *채널 디코딩* 또는 패턴 분류 문제로 간주 될 수 있음

#### Signal

- EWS(Early Warning Score)
  - 개요
    - 환자의 병세의 정도를 빨리 판단하기 위하여 사용되는 의료 서비스들이 사용하는 가이드
    - vital sign에 기반
      - respiratory rate, oxygen saturation, temperature, blood pressure, pulse/heart rate, AVPU response
  - 배경
    - 1990년대 후반에 많은 연구들이 병원 내에서 특정 vital sign이 비정상적으로 증가하게 되면 cardiac arrest(심정지)나 in-hospital deterioration이 나타난다는 연구결과들이 나타남
  - 최적의 사용
    - 특정 지표는 심정지 위험도를 급격히 증가시키는 것을 확인
    - 반드시 정해진 지표는 없고, 추가할 수 있음
  - 종류
    - **MEWS(Modified)**
      - 일반적으로 다양한 치료 상황에서 많은 사람들의 요구조건을 맞춘 디자인
    - PEWS(Paediatric Early Warning System)
      - 나이 16세 이하의 환자들을 대상으로 디자인
    - MEOWS(Modified Early Obstetric Warning Score)
      - 임산부 여성 환자들을 대상으로 디자인
    - NEWS & NEWS2(National)
      - UK 국가의 기준으로 디자인
- DEWS
  - 개요
    - MEWS에 비해서 DEWS가 더 효과적일까?(Sensitivity, Specificity)

#### BoneAge

#### Pathology

- 병리학
  - 개요
    - 질병이나 상처의 원인과 결과를 연구하는 의학 분야
      - 세포, 조직, 장기의 표본을 육안이나 현미경 등을 이용하여 검사해, 그것들이 질병에 침범되었을 때에 어떤 변화를 나타내는지에 대해서 연구하는 학문
    - 해부학 및 조직학과 밀접한 관련이 있음
    - 병원에서 병리의사는 병리학적 지식을 바탕으로 임상의사들에게 병을 알려주는 역할을 함
      - 기초의학과 임상의학의 중간자
      - 임상의사에 의해 채취된 인체의 표본으로 병리검사를 시행하여 정확한 진단에 이르게 하여 환자의 치료방향을 결정하는데 근거를 제공
    - 법의학도 병리학에 기반을 두고 있음
