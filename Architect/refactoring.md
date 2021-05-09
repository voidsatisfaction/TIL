# Refactoring

- 의문
- 나에게 보완이 필요한 점
- 마인드
- 정의
- [0] 테스트 구축하기
- [1] 리팩토링 예시

## 의문

## 나에게 보완이 필요한 점

- 리팩토링
  - 변수 인라인화
    - 무조건 변수로 할당시키고, 그것을 다루는게 좋다고 생각했음
      - 그런데, 생각해보면 어차피 임시변수이므로, 함수의 이름이 충분히 추상화된 상태라면 인라인으로 실행해도 문제없을듯
  - 함수 내부의 최종 결과물은 `result`라는 이름으로 하기
    - 생각해보면 참 알기 쉬움
  - 리팩토링의 모든 small step들이 작성된 test에 compatible해야함
  - 리팩토링을 너무 큰 호흡으로 생각해왔음
    - 할 수 있는 작은것들은 다 리팩토링 가능한 대상
    - 그냥 그때마다 하자
  - 리팩토링을 코드를 파악하는 용도로 사용 가능함
    - 캠핑 규칙에 따라, 처음왔을 때 보다 깨끗하게 치우고 가자
    - 자주보는 부분을 잘 리팩토링하자
      - 효과가 큼
- 테스트
  - 완벽하게 만드느라 테스트를 수행하지 못하느니, 불완전한 테스트라도 작성해 실행하는게 나음
  - 테스트에서 잘 통과가 되어도, 일부러 에러를 내보는 체크가 필요함
  - 픽스쳐(테스트에 필요한 데이터, 객체)는 중복을 피하라
    - but 픽스쳐는 하나의 테스트 유닛마다 다시 initialization해야 함
  - 버그가 발견되는 즉시, 버그를 잡는 테스트부터 작성하는 습관을 들이자
  - 테스트도 계속해서 발전시키자

## 마인드

- 선리팩토링 후성능
  - 리팩터링때문에 성능 문제가 생기면, 리팩터링을 마무리하고 나서 성능을 개선한다.
- 리팩토링은 잘게 나누어서 하라.
- 명료함이 진화할 수 있는 소프트웨어의 정수다.
- **언제나 코드베이스를 작업 시작 전보다 건강하게 만들어놓고 떠나야 한다.**
- 좋은 코드 = 수정하기 쉬운 코드
  - 수정할 위치 파악 용이
  - 오류 없이 빠르게 수정 가능

## 정의

- 정의
  - 명사
    - 관찰 가능한 행위를 변경하지 않은채로 보다 이해하기 쉽고, 변경하기 쉽도록 소프트웨어의 내부 구조를 변경하는 기법(명사)
  - 동사
    - 관찰 가능한 행위를 변경하지 않은채로 리팩토링 기법을 적용하는 것(동사)
- 목적
  - 오로지 경제적인 이유
    - 코드를 이해하고 수정하기 쉽게 만드는 것
      - 성능은 별개
    - 개발 속도를 높여서, 더 적은 노력으로 더 많은 가치를 창출하는 것
- 효과
  - 소프트웨어 설계의 개선
  - 소프트웨어 이해하기 쉬워짐
  - 버그를 쉽게 찾을 수 있게됨
  - 생산성 향상
- 언제 해야하나
  - 준비를 위한 리팩토링
    - 기능 추가를 위함
  - 이해를 위한 리팩토링
    - 코드를 이해하기 쉽게 만든다 & 코드에 대한 이해도를 높인다
  - 쓰레기 줍기 리팩토링
    - 간단히 수정할 수 있는것은 간단히 고침 & 시간이 걸리는 일은 짧은 메모만 남김
  - 계획된 리팩터링과 수시로하는 리팩터링
    - 수시로 기능 추가 / 버그 고치기 할 때 리팩터링을 해야 함
    - 계획된 리팩토링은 최소한으로 줄여야 함
  - 오래 걸리는 리팩토링
    - 주어진 문제를 몇 주에 걸쳐서 조금씩 해결하는 편이 효과적
    - 참고
      - 라이브러리 교체에는 추상 인터페이스를 호출하도록 만들고 교체하면 쉽게 교체 가능
  - 코드리뷰에 활용
- 언제 하지 말아야 하나
  - 굳이 수정할 필요가 없을 때
  - 리팩토링하는 것 보다 처음부터 새로 만드는게 편할 때
- 문제
  - 새 기능 개발 속도 저하
    - 리팩토링은 오로지 경제적인 이유로 하는 것임, 장기적으로는 더 빨라지므로 하는게 나음
  - 코드 소유권
    - 코드는 개인이 아니라 팀이 소유하게 해서, 누구나 수정 가능하도록 하자
    - 공개 API는 기존 함수는 그대로 유지하되, 함수 본문에서 새 함수를 호출하도록 함
  - 브랜치
    - CI형태로 하루에도 몇번씩 마스터에 머지 가능하도록
  - 테스트
    - 꼭 작성하자
  - 레거시 코드
    - 레거시 코드를 파악할 때, 리팩토링이 매우 도움이 됨
    - 대신, 테스트 보강이 필요
- 시너지
  - 테스트 + CI + 리팩토링 + (YAGNI)
- 특징
  - 프로그램의 작동 방식을 더 쉽게 파악할 수 있도록 코드를 여러 함수와 프로그램 요소로 재구성
    - 구조부터 바로잡자
    - **프로그램이 새로운 기능을 추가하기에 편한 구조가 아니라면, 먼저 기능을 추가하기 쉬운 형태로 리팩터링하고 나서 원하는 기능을 추가하자**
  - 기능 추가와 리팩토링은 별도 진행
    - 기능 추가를 할 때에는 기능 추가만
    - 리팩토링을 할 때에는 리팩토링만
- 리팩토링 절차
  - [0] 코드 파악 & 개선점 찾기
  - [1] 테스트 코드 작성
    - 자가 진단이 가능해야 함
    - 리팩터링할 때 매우 중요함
    - 작은 수정이 있는 리팩터링 후에는 항상 테스트하자
      - 그래야 변경 범위가 적음
  - [2] 기능 쪼개기
    - 일단 로직을 쪼개놓으면 리팩토링을 하기에 수월하고 코드가 읽기 쉽게 변함
  - [3] 단계 쪼개기

## [0] 테스트 구축하기

### 테스트 코드의 가치

- 테스트 suite는 강력한 버그 검출 도구로, 버그를 찾는 데 걸리는 시간을 대폭 줄여준다.
- TDD로 진행하자
  - 테스트 작성 -> 코딩 -> 리팩터링
  - 구현보다 인터페이스에 집중하게 된다는 장점

### 테스트 방식

- 실패해야 할 상황에서는 반드시 실패하게 만듦
- 자주 테스트해야 함
  - 최소한 몇분 간격으로 테스트
- 테스트는 위험 요인을 중심으로 작성해야 함
  - **흠 그런데, 그렇게 되면 깨진 유리창 효과 때문에 테스트가 정착되지 않은 환경에서는 사람들이 테스트를 작성하지 않게 될 수도..?**
  - **경계 조건 검사하기**
    - 이런 부분을 집중적트로 테스트해야 함
    - 프로그램을 망가뜨릴 작정으로 테스트해야 함
- 완벽하게 만드느라 테스트를 수행하지 못하느니, 불완전한 테스트라도 작성해 실행하는게 낫다

## [1] 리팩토링 예시

- 극단에서 공연 요청이 들어오면, 연극의 장르와 관객 규모를 기초로 비용을 책정.
- 비극과 희극만 공연.
- 공연료와 별개로 포인트를 지급해서 다음번 의뢰 시 공연료 할인 가능

데이터

```js
// plays.json
{
  'hamlet': {'name': 'Hamlet', 'type': 'tragedy'},
  'as-like': {'name': 'As You Like It', 'type': 'comedy'}
}

// invoices.json
[
  {
    'customer': 'BigCo',
    'performances': [
      {
        'playID': 'hamlet',
        'audience': 55
      },
      {
        'playID': 'as-like',
        'audience': 35
      }
    ]
  }
]
```

### 리팩토링 전 코드

공연료 청구서를 출력하는 코드

```js
function statement(invoice, plays) {
  let totalAmount = 0;
  let volumeCredits = 0;
  let result = `customer: ${invoice.customer}\n`;
  const format = new Intl.NumberFormatat(...);

  for (let perf of invoice.performances) {
    const play = plays[perf.playID];
    let thisAmount = 0;

    switch (play.type) {
      case 'tragedy':
        thisAmount = 40000;
        if (perf.audience > 30) {
          thisAmount += 1000 * (perf.audience - 30);
        }
        break;
      case 'comedy':
        thisAmount = 30000;
        if (perf.audience > 20) {
          thisAmount += 10000 + 500 * (perf.audience - 20);
        }
        thisAmount += 300 * perf.audience;
        break;
      default:
        throw new Error(`Undefined genre: ${play.type}`);
    }

    volumeCredits += Math.max(perf.audience - 30, 0);

    if ('comedy' === play.type) volumeCredits += Math.floor(perf.audience / 5);

    result += `  ${play.name}: ${format(thisAmount/100)} (${perf.audience/5} seats)\n`;
    totalAmount += thisAmount;
  }

  result += `  total: ${format(totalAmount/100)}\n`;
  result += `  volume credits: ${volumeCredits}\n`;
  return result;
}
```

- 위 코드의 문제
  - 청구 내역을 HTML형태로 출력하는 기능이 추가된다면?
  - 다양한 극을 다룰 수 있도록 하려면?
    - 기존 계산로직이 수정된다면?
- 위 케이스에서 리팩토링 절차
  - [1] `statement()`함수 테스트 코드 작성
  - [2] `switch`문의 로직(무조건 코드를 분석해서 얻을 수 있는 정보)을 함수로 추상화
    - 함수 추출하기
    - 커밋
    - 명확한 이름 사용(**좋은 코드라면 하는 일이 명확하게 들어나야 한다**)
      - `thisAmount`라는 불명확한 이름 대신에, `result`라는 이름으로 변경
      - `perf`라는 불명확한 이름 대신에, `aPerformance`라는 이름으로 변경
  - [3] `const play = plays[perf.playID]`의 임시 변수 대신 질의 함수 만들기
  - [4] `const play = playFor(perf)`로 되어있는 것들을 변수인라인하기 적용
    - 어차피 같은 것을 지칭하고, 인라인으로 하는것이 더 의미가 명확할 수 있음
  - [5] `volumeCredits`를 계산하는 로직을 함수로 추상화 & 변수명 명시적으로 바꾸기
  - [6] `format` 부분의 임시 변수를 함수로 추상화 하기 `usd(aNumber)`
    - 이름을 최대한 명시적으로 짓자
  - [7] `volumeCredits` 변수를 `result`를 갱신하는 로직과 별도로 따로 둔다.
    - 여기서 한 발 더 나아가, `totalVolumeCredits()`라는 함수로 코드를 추상화한다.

### 중간 점검 코드1

```js
function statement(invoice, plays) {
  let result = `customer: ${invoice.customer}\n`;
  for (let perf of invoice.performances) {
    result += `  ${playFor(perf).name}: ${usd(amountFor(perf))} (${perf.audience}seats)\n`;
  }
  result += `total amount: ${usd(totalAmount())}\n`;
  result += `total volume credits: ${totalVolumeCredits()}\n`;
  return result;

  // 사용되는 함수들이 정의되어 있음
}
```

- 위 케이스에서의 리팩토링 절차(테마: 계산 단계와 포맷팅 단계 분리하기)
  - [1] `statement()`의 로직을 계산하는 단계(중간데이터를 생산하는 단계)와 render하는 단계로 나누기
  - [2] 반복문을 파이프라인으로 변경
    - 더 알기 쉬움
  - [3] 중간 데이터를 생산하는 단계를 `createStatementData(invoice, plays)`로 추상화
    - `createStatementData()`를 다른 파일에 분리해서 저장

### 중간 점검 코드2

`statement.js`

```js
import createStatementData from './createStatementData.js';

function statement(invoice, plays) {
  return renderPlainText(createStatementData(invoice, plays));
}

function renderPlainText(data) {
  let result = '...';
  return result;
}

function htmlStatement(invoice, plays) {
  return renderHtml(createStatementData(invoice, plays));
}

function renderHtml(data) {
  let result = '<h1> ... </h1>';
  return result;
}
```

`createStatementData.js`

```js
export default function createStatementData(invoice, plays) {
  const result = {};
  result.customer = invoice.customer;
  result.performances = invoice.performances.map(enrichPerformance);
  result.totalAmount = totalAmount(result);
  result.totalVolumeCredits = totalVolumeCredits(result);
  return result;
}

function enrichPerformance(aPerformance) {
  const result = Object.assign({}, aPerformance);
  result.play = playFor(result);
  result.amount = amountFor(result);
  result.volumeCredits = volumeCredits(result);
  return result;
}

function amountFor(aPerformance) {
  let result = 0;
  switch (aPerformance.play.type) {
    case 'trgedy':
      // ...
      break;
    case 'comedy':
      // ...
      break;
    default:
      throw new Error(`Unknown genre: ${aPerformance.play.type}`)
  }
  return result;
}

function volumeCreditsFor(aPerformance) {
  let result = 0;
  // ...
  return result;
}

// 그외의 많은 함수들
```

- 사족
  - 사실 위 코드의 문제라고 생각되는 점은, `enrichPerformance()`에서 result를 구성하는데에 있어서 구성 순서가 중요하다는 점이다.
    - 순서에 의존하는게 영 꺼림칙
- 위 케이스에서의 리팩토링 절차(테마: (조건부 로직을) 다형성을 활용해 코드 재구성하기)
  - [1] `amountFor(aPerformance)`, `volumeCreditsFor(aPerformance)`를 `PerformanceCalculator`클래스로 로직을 옮김
  - [2] 생성자를 팩토리 함수로 바꾸기
  - [3] polymorphism적용하기

### 최종 점검 코드

`createStatementData.js`

```js
export default function createStatementData(invoice, plays) {
  const result = {};
  result.customer = invoice.customer;
  result.performances = invoice.performances.map(enrichPerformance);
  result.totalAmount = totalAmount(result);
  result.totalVolumeCredits = totalVolumeCredits(result);
  return result;
}

function enrichPerformance(aPerformance) {
  const calculator = createPerformanceCalculator(
    aPerformance,
    playFor(aPerformance)
  );
  const result = Object.assign({}, aPerformance);
  result.play = calculator.play;
  result.amount = calculator.amount;
  result.volumeCredits = calculator.volumeCredits;
  return result;
}

function createPerformanceCalculator(aPerformance, aPlay) {
  switch (aPlay.type) {
    case 'tragedy': return new TragedyCalculator(aPerformance, aPlay);
    case 'comedy': return new ComedyCalculator(aPerformance, aPlay);
    default:
      throw new Error(`Unknown genre: ${aPlay.type}`);
  }
}

class PerformanceCalculator {
  constructor(aPerformance, aPlay) {
    this.performance = aPerformance;
    this.play = aPlay;
  }

  get amount() {
    throw new Error('subclass responsibility');
  }

  get volumeCredits() {
    return Math.max(this.performance.audience - 30, 0);
  }
}

class TragedyCalculator extends PerformanceCalculator {
  get amount() {
    let result = ...

    return result;
  }
}

class ComedyCalculator extends PerformanceCalculator {
  get amount() {
    let result = ...

    return result;
  }

  get volumeCredits() {
    return super.volumeCredits + Math.floor(this.performance.audience / 5);
  }
}
```
