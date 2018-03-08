# TypeScript

## 목차


## 사상

- 큰 시스템을 안전하고 빠르게 만들기 위한 툴
- 타입 시스템은 선택적

## 기본 타입

- 불린(Boolean)
  - `let isDone: boolean = false;`
- 숫자
  - `let decimal: number = 6;`
- 문자열
  - `let color: string = "blue";`
- 배열
  - `let list: number[] = [1, 2, 3];`
  - `let list: Array<number> = [1, 2, 3];`
- 튜플(Tuple)
  - 고정된 길이를 가진 배열
  - 타입은 지정 가능
  - 고정된 길이를 넘어서는 지정한 타입을 유니온 타입으로 해서 확인
  - `let x: [string, number]; x = ["hello", 10];`
- 이넘(Enum)
  - 숫자 값을 문자열로 추상화해 집합으로 표현
    - `enum Color {Red = 1, Green = 2, Blue = 4}`
    - `let c: Color = Color.Green // 2`
  - 이넘의 숫자값으로 이름값(키)을 알 수 있음
    - `let colorName: string = Color[2]; // 'Green'`
- Any
  - 애플리케이션을 작성할 때 알 수 없는 타입 변수를 나타낼 때 씀
  - 동적 컨텐츠
    - 제3자 라이브러리로부터의 값
  - 컴파일 타임 체크하지 않음
  - 오브젝트(Object) 타입은 메서드를 사용할 수 없음(값의 할당만 인정)
  - `let list: any[] = [1, true, "free"];`
  - `list[1] = 100;`
- Void
  - 아무런 타입이 존재하지 않는 것
  - 변수에 선언하면 `undefined`나 `null`만 할당 가능
- Null과 Undefined
  - 기본적인 설정에서는 모든 다른 타입의 서브타입임
    - `number`에도 `null`과`undefined`를 할당 가능
  - `--strictNullChecks`를 설정하면 다른 타입에 `null`과 `undefined`를 할당할 수 없음
- Never
  - 절대로 일어나지 않는 값의 타입을 나타냄(함수의 리턴값)
  - 케이스
    - 항상 예외를 일으키는 함수
    - 리턴하지 않는 함수
- 타입 단언(Type assertions)
  - 타입 스크립트보다 사용자가 더 타입에 대해서 잘 알 때 사용
    - e.g 어떠한 엔티티가 현재의 타입보다 더 확정적인(specific)타입인 경우
  - 컴파일러에 의해서만 사용
  - 사용
    - `let strLength: number = (<string>someValue).length;`
    - `let strLength: number = (someValue as string).length;`
    - jsx에서는 as스타일의 타입 단언만 가능

## 인터페이스

- 값을 가지는 모양을 체크
  - 덕 타입핑, 구조적 서브타이핑
  - go의 인터페이스 처럼 따로 명시적으로 계승하지 않아도 됨
- 제3자 코드와의 계약(contracts)을 정의하는 강력한 방법

### 첫 인터페이스 예

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

### 선택적 속성

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
