# 생성자 패턴(Constructor Pattern)

자바스크립트에서는 거의 모든것이 오브젝트임. 그래서 오브젝트의 생성자를 주목해야 함

- 오브젝트 생성
- 기본 생성자
- 프로토 타입을 이용한 생성자

## 오브젝트 생성

- 리터럴(문법 설탕)
- 컨스트럭터 직접적 호출

```js
const newObject = {};
const newObject = new Object();
```

### 키와 값

- 점 문법
- 대괄호 문법
- `Object.defineProperty`
- `Object.defineProperties`

```js
// 1
newObject.someKey = "hello world";

// 2
newOjbect["someKey"] = "hello world";

// 3
Object.defineProperty(newObject, "someKey", {
  value: "hi world",
  writable: true,
  enumerable: true,
  configurable: true,
});

// 4
Object.defineProperties(newObject, {
  "someKey": {
    value: "Hello world",
    writeable: true,
  },
  "anotherKey": {
    value: "Foo bar",
    writable: false,
  }
});
```

## 기본 생성자

- 생성자 함수가 존재
- 클래스도 존재(ECMA Script5 이후)

```js
function Car(model, year, miles) {
  this.model = model;
  this.year = year;
  this.miles = miles;

  this.toString = function () {
    return this.model + " has done " + this.miles + " miles";
  };
}

const civic = new Car("Honda Civic", 2009, 20000);
const mondeo = new Car("Ford Mondeo", 2010, 5000);

console.log(civic.toString());
console.log(mondeo.toString());
```

- 위 방법의 문제
  - 상속이 힘듬
  - `toString`메서드가 모든 오브젝트에서 재정의 됨

## 프로토타입을 이용한 생성자

- js의 함수들은 `prototype`이라는 속성을 갖음
  - 자바스크립트 생성자를 호출하면, 모든 생성자의 `prototype` 속성들이 새로운 오브젝트에서 사용 가능하게 됨
  - 다양한 `Car` 오브젝트들이 같은 프로토타입에 접근할 수 있게 됨

```js
function Car(model, year, miles) {
  this.model = model;
  this.year = year;
  this.miles = miles;
}

Car.prototype.toString = function() {
  return this.model + " has done" + this.miles + " miles";
};

const civic = new Car("Honda Civic", 2009, 20000);
const mondeo = new Car("Ford Mondeo", 2010, 5000);

console.log(civic.toString());
console.log(mondeo.toString());
```

`toString()`메서드는 모든 `Car` 오브젝트사이에서 공유됨
