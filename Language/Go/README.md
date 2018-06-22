# GO Lang

## Go의 등장

- 사상
  - **Simplicity**
  - **Scalability**

Google내의 기존 언어를 사용한 시스템의 복잡성에 대한 고통. 한 곳을 고치면 다른 곳이 탈나고 다른곳을 고치면 또 다른 곳이 탈나는 악순환.

> Simplicity is the key to good software

결국 단순함을 가장 중요시해서 태어난 언어이다. 결국 승리하는 것은 단순한 것 이니까.

1. 단순함을 중시하는 코드 문화
2. 타입시스템
3. 동시성
4. 풍부한 내장 라이브러리(Convention)

## Go의 기원

### Go의 조상과 물려받은 것들

- C
  - expression syntax, control-flow, basic data types, call-by-value parameter passing, pointers ...  passing, pointers ...
  - 효율적인 기계어로의 컴파일과 현 OS와의 자연스러운 조화
- Pascal
  - package, module imports, declarations
- CSP
  - concurrency, channel

... 그외에 scheme의 lexical scope, APL의 iota, go만의 독자적인 defer등이 있다.
