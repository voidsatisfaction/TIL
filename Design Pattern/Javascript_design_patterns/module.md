# 모듈 패턴(Module pattern)

모듈은 애플리케이션 아키텍처의 결합 조각. 깔끔하고 조직적으로 코드를 분리하기 위한 수단

- 종류
  - 오브젝트 리터럴 기법
  - 모듈 패턴
  - AMD 모듈
  - CommonJS 모듈
  - ECMAScript Harmony 모듈
- 목차
  - 오브젝트 리터럴
  - 모듈 패턴
    - 프라이버시
    - 예제
  - 모듈 패턴의 변화
    - 믹스인 임포트
    - 익스포트
    - 툴킷과 프레임웍 특유의 모듈 패턴 구현
      - Dojo
      - ExtJS
      - YUI
      - JQuery
    - 장단점
  - 모듈 패턴 드러내기
    - 장단점

## 오브젝트 리터럴

```js
const myModule = {
  myProperty: "SomeValue",

  myConfig: {
    useCaching: true,
    language: "en",
  },

  myMethod: function() {
    console.log("where int he world is Paul Irish today?");
  }

  myMethod2: function() {
    console.log("Caching is: " + ( this.myConfig.useCaching ) ? "enabled" : "disabled");
  },

  myMethod3: function(newConfig) {
    if (typeof newConfig === "object") {
      this.myConfig = newConfig;
      console.log(this.myConfig.language);
    }
  }
};

myModule.myMethod(); // Where int he world is Paul Irish today?
myModule.myMethod2(); // enabled;
myModule.myMethod3({
  language: "fr",
  useCaching: false
}); // fr
```

## 모듈 패턴

- 원래 클래스를 위한 프라이빗, 퍼블릭 캡슐화를 제공하기 위해서 정의된 방식
- 자바스크립트에서는 그것을 흉내내기 위한 개념
  - 글로벌 스콥에서 특정 부분(메서드, 변수)을 격리
  - 이름 공간의 오염과 충돌을 막아줌

### 프라이버시

- 모듈 패턴은 **클로저** 를 이용하여 사적 상태(privacy state) 혹은 조직의 캡슐화를 함
  - 파블릭, 프라이빗 메서드와 변수를 글로벌 스콥에 좌우 되지 않도록 래핑
- 애초에 자바스크립트 에서는 명시적으로 변수의 파블릭, 프라이빗을 지정해줄 수 없음
  - 그래서 함수 스콥을 이용해서 모방하는 것

### 예제

```js
const basketModule = (function() {
  const basket = [];

  function doSomethingPrivate() {
    // ...
  }

  function doSomethingElsePrivate() {
    // ...
  }

  return {
    addItem: function(values) {
      basket.push(values);
    },

    getItemCount: function() {
      return basket.length;
    }

    doSomething: doSomethingPrivate,

    getTotal: function() {
      var itemCount = this.getItemCount();

      let total = 0;
      while (itemCount--) {
        total += basket[itemCount].price;
      }

      return total;
    }
  };
})();

basketModule.addItem({
  item: 'bread',
  price: 0.5
});

basketModule.addItem({
  item: 'butter',
  price: 0.3
});

console.log(basketModule.getItemCount()); // 2

console.log(basketModule.getTotal()); // 0.8

console.log(basketModule.basket); // undefined

console.log(basket) // undefined
```

- 모듈 내에서만 사용할 수 있는 프라이빗 함수들을 갖을 수 있음. 다른 스코프에서는 접근할 수 없으므로 완전한 프라이빗
- 함수가 일반적으로 정의 되었으므로, 예외 처리를 보낸 함수를 call stack으로 확인할 수 있음
- 브라우저 환경에 따라 다른 함수들을 반환할 수 있음

## 모듈 패턴의 변화

### 믹스인 임포트

- 글로벌 모듈이 어떻게 다른 익명 함수의 모듈의 인자로 전해질 수 있는가(import)

```js
const myModule = (function (jQ, _) {
  function privateMethod1() {
    jQ(".container").html("test");
  }

  function privateMethod2() {
    console.log(_.min([10, 5, 100, 2, 1000]));
  }

  return {
    publicMethod: function() {
      privateMethod1();
    }
  };
}(jQuery, _));
```

### 익스포트

```js
const myModule = (function() {
  const module = {};

  const privateVariable = "Helo World";

  function privateMethod() {
    // ...
  }

  module.publicProperty = "Foobar";
  module.publicMethod = function() {
    console.log(privateVariable);
  };

  return module;
}());
```

### 툴킷과 프레임웍 특유의 모듈 패턴 구현

#### Dojo

- `dojo.setObject()`를 이용한 간편한 메서드
- e.g
  - 다음은 `store` 이름 공간의 하나의 오브젝트로서 `basket.core`를 선언하는 경우

```js
const store = window.store

if (![true](store.basket)) {
  store.basket = {};
}

if (!store.basket.core) {
  store.basket.core = {};
}

store.basket.core = {
  // ...rest of our logic
};
```

```js
import { store } from 'dojo';

store.setObject("basket.core", (() => {
  const basket = [];

  const privateMethod = () => {
    console.log(basket);
  };

  return {
    publicMethod: () => {
      privateMethod();
    }
  };
}()));
```

### 장점

- OOP의 관점에서 깔끔한 캡슐화가 가능
- private 사용 가능

### 단점

- 파블릭과 프라이빗 멤버를 다르게 접근하기 때문에, 가시성(visibility)를 변화 시키려면 각각의 장소도 변경해야 함
- 해당 오브젝트에 나중에 메서드를 추가할 경우, 프라이빗 멤버들(변수, 메서드)에 접근하지 못함
- 프라이빗 메서드의 경우, 유닛 테스트 하기가 힘듬. 단순히 버그가 있는 프라이빗 멤버들만 교체할 수 없고 파블릭 메서드를 모두 오버라이드 해야함
- 프라이빗 멤버들을 쉽게 확장하기 힘듬

## 모듈 패턴 드러내기

- 앞서의 구현은, 파블릭 메서드가 파블릭 멤버들을 참조할 떄 `this`를 사용해야 함
- 오브젝트 리터럴을 사용해야 함

```js
const myRevealingModule = (() => {
  let privateVar = "Ben Cherry",
      publicVar = "Hey there!";

  const privateFunction = () => {
    console.log("Name: " + privateVar);
  };

  const publicSetName = (strName) => {
    privateVar = strName;
  };

  const publicGetName = () => {
    privateFunction();
  }

  return {
    setName: publicSetName,
    greeting: publicVar,
    getName: publicGetName
  }
})();

myRevealingModule.setName("Paul kinlan");
```

### 장단점

- 장점
  - 코드가 보다 일관적으로 됨
  - 읽기 쉬움
- 단점
  - 프라이빗 함수가 파블릭 함수를 참조할 때, 파블릭 함수가 패치가 필요할 때 오버라이딩 될 수 없음
  - 프라이빗 변수들을 참조하는 파블릭 오브젝트 멤버역시 패치가 불가능 하게 됨
  - 기존의 모듈 패턴보다 더

p.s *도대체 여기서 말하는 패치란 무엇일까* -> 멤버 메서드를 구현을 변화시키지 않고 아에 새로운 것으로 치환하는것
