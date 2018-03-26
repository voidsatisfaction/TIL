# BlockChain Technology

## 요약

- 블록체인이란
  - 기록들의 분산 데이터베이스
  - 모든 거래의 공적 ledger
  - 실행된 디지털 이벤트
  - 이러한 행위에 참여하는 모든이에게 공유
- 인정
  - 각각의 공적 leger에서의 거래는 그 시스템에 있는 참가자의 다수의 동의에 의해서 확정된다(verified)
  - 한 번 데이터가 기록되면 영원히 지워지지 않음
  - 모든 거래의 확실하고 인증받은 기록을 포함하는 것이 블록체인
  - 탈중앙화된 P2P 디지털 통화인 비트코인이 블록체인 기술의 대표적 예시
- 주요 가설
  - 블록체인은 디지털 온라인 세계의 **분산 동의(distributed consensus)** 시스템을 구축함
  - 이는 참여자가 공적 ledger에서의 되돌릴 수 없는 디지털 기록을 생성한 다는것을 확실히 알도록 함
  - 민주적 오픈, 성장할 수 있는 디지털 경제를 탈중앙화해서 보장
  - 경제적 / 비경제적 분야에서 문제 없이 잘 돌아가고 있음

## 서론

- 블록체인
  - 분산된 동의 모델(distributed consensus model)
- 현재 상황
  - 디지털 경제는 특정 신뢰 기관(trusted authority)에 기반해있음
    - e.g) 페북에 올린 글이 페북에 의해서 친구에게만 공유된다고 간주됨
    - 은행이 외국의 가족에게 돈이 잘 전달되었다는걸 보장
  - 즉, 제3의 기관에 의해서 디지털 안전과 프라이버시가 보장됨
  - 하지만 제3의 기관도 언제든지 조작되고 해킹될 수 있음
- 블록체인의 의의
  - **분산 동의** 에 의하여 과거와 현재의 어떠한 거래도 보증될 수 있음
  - **분산 동의** 와 **익명성** 이 블록체인 기술의 핵심 특징
  - 대표적 예시
    - 스마트 계약(Smart contract)
      - 계약을 자동으로 맺어줌
    - 스마트 자산(Smart Property)
      - 자산이나 재산을 스마트 계약을 통해서 소유권을 제어함
      - **비트코인은 화폐가 아니라, 돈의 소유권을 제어하는 모든 것이다.**
    - 경제적 / 비경제적 분야에서 모두 응용가능
      - 디지털 자산 그자체가 아닌, 디지털 자산의 지문(fingerprint)를 남겨놓는 것으로 익명성과 프라이버시를 둘다 성취할 수 있음

## 1장: 블록체인 기술

### 비트코인의 짧은 역사

- 사토시 나카모토라는 사람에 의해 2008년 논문에서 등장
- 암호 화폐(cryptocurrencies)는 중앙화된 신뢰 기관을 거치지 않고 오직 암호에 의해서 안전한 거래를 담보하는 모든 네트워크와 거래의 매개체를 지칭

### 블록체인의 기술은 어떻게 동작하는가?

비트코인을 예시로 들지만, 블록체인 기술은 어떠한 온라인 디지털 자산거래에도 적용 가능함

- 인터넷 상거래는 거래를 중재하고 보호할 수 있는 신뢰할 수 있는 제3의 금융 기관과 밀접한 관계가 있음
- 일정한 비율의 잘못은 피할 수 없음 그래서 중재자가 필요함 => 높은 거래비용의 원인

비트코인의 경우 암호적 증명(cryptographic proof)을 이용함

- 거래 예시
  - 각각의 거래는 디지털 서명(signature)으로 보호됨
  - 각각의 거래는 보내는 사람의 비밀키로 서명되어서 수신자의 공개키로 보내짐
  - 암호 화폐의 주인은 비밀키의 소유권을 증명해야 함
  - 디지털 화폐를 받는 주체는 그 디지털 화폐의 소유권이 보내는 사람에게 있었다는 걸, 보내는 사람의 공개키로 확인함(왜냐하면 보내는 사람의 비밀키로 서명해 놓지 않으면 보내는 사람의 공개키로는 인증을 확인할 수 없기 때문 - 저 사람이 비밀키의 소유자가 맞다!)
- 이러한 각각의 거래는 비트코인 네트워크의 모든 노드에게 전파되고 확인 작업 후에 공적 장부(ledger)에 기록됨
- 모든 거래는 공적 장부에 기록되기 전에 반드시 확인되어야 함
  - 확인 되어야 하는 내용
    - 1 특정 거래에서 암호화폐를 보내는 사람이 그 암호화폐를 소유하고 있다는 점
    - 2 특정 거래에서 암호화폐를 보내는 사람이 그/그녀의 계정에 충분한 양의 암호화폐를 소유하고 있다는 점, 암호 화폐를 지불하는 사람의 계정을 그의 공개키로 항상 확인해야 함
- 하지만 이중 지불(double-spending)의 문제가 발생
  - 한 사람이 복수의 거래를 일시에 행할 경우, 어떠한 거래가 먼저 발생한 것인지 반드시 알아야 함