# 자연언어처리

## 자연언어처리의 정의

## 팁

### Lemmatisation vs Stemming

- Lemmatization
  - 문장 속에서 다양한 형태로 활용된(inflected) 단어의 표제어(lemma)를 찾는 일
  - 표제어는 사전의 기본형
  - 단어가 문장 속에서 어떤 품사로 쓰였는지까지 판단한다.
- Stemming
  - 어형이 변형된 단어로부터 접사 등을 제거하고 그 단어의 어간을 분리해 내는 것
  - e.g
    - `stemmer`, `stemming`, `stemmed` -> `stem`
    - `fishing`, `fished`, `fisher` -> `fish`
    - `argue`, `argued`, `arguing`, `argus` -> `argu`
    - `argument`, `arguments` -> `argument`
