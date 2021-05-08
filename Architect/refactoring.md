# Refactoring

- 의문
- 나에게 보완이 필요한 점
- 마인드
- 정의
- [1] 리팩토링 예시

## 의문

## 나에게 보완이 필요한 점

- 변수 인라인화
  - 무조건 변수로 할당시키고, 그것을 다루는게 좋다고 생각했음
    - 그런데, 생각해보면 어차피 임시변수이므로, 함수의 이름이 충분히 추상화된 상태라면 인라인으로 실행해도 문제없을듯
- 함수 내부의 최종 결과물은 `result`라는 이름으로 하기
  - 생각해보면 참 알기 쉬움
- 리팩토링의 모든 small step들이 작성된 test에 compatible해야함

## 마인드

- 잘 다듬어진 코드여야 성능 개선 작업도 훨씬 수월하다.
  - 리팩터링때문에 성능 문제가 생기면, 리팩터링을 마무리하고 나서 성능을 개선한다.
- 리팩토링은 잘게 나누어서 하라.
- 명료함이 진화할 수 있는 소프트웨어의 정수다.
- **언제나 코드베이스를 작업 시작 전보다 건강하게 만들어놓고 떠나야 한다.**
- 좋은 코드 = 수정하기 쉬운 코드
  - 수정할 위치 파악 용이
  - 오류 없이 빠르게 수정 가능

## 정의

- 정의
  - 관찰 가능한 행위를 변경하지 않은채로 보다 이해하기 쉽고, 변경하기 쉽도록 소프트웨어의 내부 구조를 변경하는 것(명사)
  - 관찰 가능한 행위를 변경하지 않은채로 리팩토링을 적용하는 것(동사)
  - 프로그램의 작동 방식을 더 쉽게 파악할 수 있도록 코드를 여러 함수와 프로그램 요소로 재구성
    - 구조부터 바로잡자
    - **프로그램이 새로운 기능을 추가하기에 편한 구조가 아니라면, 먼저 기능을 추가하기 쉬운 형태로 리팩터링하고 나서 원하는 기능을 추가하자**
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
