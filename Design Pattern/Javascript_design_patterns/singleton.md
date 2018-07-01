# 싱글톤 패턴(singleton pattern)

- 클래스의 인스턴스화를 딱 하나의 오브젝트로만으로 제한
- 클래스와 인스턴스가 존재하지 않으면 새로 인스턴스를 만드는 하나의 메서드를 구현후 그 오브젝트의 레퍼런스를 반환
- **정적 클래스(static class)와의 차이**
  - 인스턴스화를 지연 평가할 수 있음
  - 인스턴스화 할 때 상황에 맞는 다른 정보들을 참조할 수 있음
- 구현은 글로벌 이름 공간에서 격리되나 이름 공간을 공유하는 리소스

## 구현

```js
const mySingleton = (() => {
  let instance;

  const init = () => {
    // singleton

    // private method and variables
    const priavetMethod = () => {
      console.log("I am private");
    };

    let privateVariable = "Im also private";
    let privateRandomNumber = Math.random();

    return {
      // public method and variables
      publicMethod: () => {
        console.log("The public can see me!");
      },
      publicProperty: "I am also public",
      getRandomNumber: () => {
        return privateRandomNumber;
      }
    }
  }

  return {
    getInstance: () => {
      // 기존에 함수 스코프 환경에 존재하지 않아야만 새로 생성
      if (!instance) {
        instance = init();
      }
      return instance;
    }
  };
})();

// usage
const singleA = mySingleton.getInstance();
const singleB = mySingleton.getInstance();
console.log( singleA.getRandomNumber() === singleB.getRandomNumber() ); // true
console.log( singleA === singleB ); // true
```

- 싱글톤 오브젝트의 조건
  - 하나의 클래스에 대응하는 반드시 하나의 인스턴스만 존재할 것. 그리고 잘 알려진 엑세스 포인트에서 접근 가능할 것
  - 인스턴스는 서브클래싱으로 확장 가능할것. 그리고 클라이언트는 코드 변경 없이 확장된 인스턴스를 사용가능 할 것
    - 아래는 두번째 예시

```js
mySingleton.getInstance = () => {
  if (this._instance === null) {
    if (isFoo()) {
      this._instance = new FooSingleton();
    } else {
      this._instance = new BasicSingleton();
    }
  }
  return this._instance;
};
```

## 활용

- 실제로 시스템의 다른 요소들과 상호작용할 때, 정확히 하나의 오브젝트만 필요할 때에 사용

```js
const SingletonTester = (() => {
  const Singleton = (options) => {
    options = options || {};

    this.name = "SingletonTester";
    this.pointX = options.pointX || 6;
    this.pointY = options.pointY || 10;
  };

  let instance;

  const _static = {
    name: "SingletonTester",

    getInstance: function(options) {
      if (instance === undefined) {
        instance = new Singleton(options);
      }
      return instance;
    }
  }

  return _static;
})();

const singletonTest = SingletonTester.getInstance({
  pointX: 5
});

console.log(singletonTest.pointX); // 5
```

## 고찰

- 자바스크립트에서 싱글톤 패턴이 필요하게 되면, 디자인 자체를 다시 생각해봐야 함
  - 싱글톤의 존재는 시스템의 모듈이 서로 강하게 결합되어서, 로직들이 코드상에 지나치게 흩어져 있는 것을 나타내기도 함
  - 싱글톤 자체를 테스팅 하기 힘듬
    - 숨겨진 의존
    - 많은 인스턴스를 생성할 수 없음
  - 멀티스레드 환경에서는 두 스레드가 동시에 `getInstance()`를 실행해서 두 객체를 생성할 수도 있음
- 추천 글
  - https://www.ibm.com/developerworks/webservices/library/co-single/index.html
  - http://misko.hevery.com/2008/10/21/dependency-injection-myth-reference-passing/
