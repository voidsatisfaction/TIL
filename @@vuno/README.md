# @@VUNO

- 알아두면 좋은 용어들

## 알아두면 좋은 용어들

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
          - uneven class distribution을 갖을 때, accuracy보다 유용
          - Recall과 Precision의 조화평균
    - 질병의 특징에 따라서 민감도를 높일 것인지 특이도를 높일 것인지를 고려하기도 함
      - 매우 심각한 질병 => 민감도를 높임 대신 재검사를 실시해서 FP를 줄임
- clinician
  - 임상의
