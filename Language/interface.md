# 인터페이스

- 값을 가지는 모양을 체크
  - 덕 타입핑, 구조적 서브타이핑
  - go의 인터페이스 처럼 따로 명시적으로 계승하지 않아도 됨
- 제3자 코드와의 계약(contracts)을 정의하는 강력한 방법

## 첫 인터페이스 예

```typescript
interface LabelledValue {
  label: string;
}

function printLabel(labelledObj: LabelledValue) {
  console.log(labelledObj.label);
}

let myObj = { size: 10, label: "Size 10 Object" };
printLabel(myObj);
```

- 명시적으로 오브젝트가 그 인터페이스를 만족한다고 선언 할 필요가 없음
- 오직 형태만 상관 있음

## 선택적 속성

- 모든 인터페이스의 속성이 반드시 필요한 것은 아님
  - e.g 선택 가방(option bags)패턴
- 인터페이스에 나와있지 않는 속성은 사용할 수 없음

```ts
interface SqureConfig {
  color?: string;
  width?: number;
}

function createSquare(config: SquareConfig): {color: string; area: number} {
  let newSquare = {color: "white", area: 100};
  if (config.color) {
    newSquare.color = config.color;
  }
  if (config.width) {
    newSquare.area = config.width * config.width;
  }
  return newSquare;
}

let mySquare = createSquare({color: "black"});
```

## 읽기 전용 속성

- 오브젝트가 생성될 떄만 수정 가능한 속성
- `readonly`라벨을 사용
  - readonly: 속성(property)에 사용
  - const: 변수에 사용

```ts
interface Point {
  readonly x: number;
  readonly y: number;
}

let p1: Point = { x: 10, y: 20 };
p1.x = 5; // error!
```

- `ReadonlyArray<T>`

```ts
let a: number[] = [1, 2, 3, 4];
let ro: ReadonlyArray<number> = a;
ro[0] = 12; // error!
ro.push(5); // error!
ro.length = 100; // error!
a = ro; // error!
a = ro as number[]; // ok
```
