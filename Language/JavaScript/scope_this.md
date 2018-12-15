# JavaScript Scope and This

JavaScript의 scope는 매우 까다로운 개념이므로, 이곳에서 알기 쉽게 정리한다.

## 참고

- [everything-about-javascript-scope - scope에 대해 알고자 했던 모든 것](http://hochulshin.com/everything-about-javascript-scope/)
- [everything you wanted to know about javascript scope - toddmotto](https://toddmotto.com/everything-you-wanted-to-know-about-javascript-scope/)

## 목차

- scope이란 무엇인가?
- global/local scope이란?
- namespace란 무엇이며, scope과 어떻게 다른가?
- this 키워드는 무엇이며, scope에 어떻게 영향을 미치는가?
- function/lexical scope란 무엇인가?
- closure란?
- public/private scope이란 무엇인가?
- 어떻게 위의 모든 개념을 이해하고, 만들고 사용할 수 있는가?

## Scope이란 무엇인가?

js에서 작성된 코드를 둘러싼 환경. scope은 global과 local로 정의될 수 있다.

## Global scope

js코드를 작성하기 전에 항상 global scope에 있다. 먄약 우리가 하나의 변수를 선언하면 이것은 global scope에서 정의된다.

```js
var name = 'min';
```

```js
jQuery('.class');
```

global scope에서 jQuery에 접근하는 위의 코드는 `namespace`로써 설명할 수 있다. namespace는 일반적으로 가장 높은 수준의 scope를 refer한다.

위의 예에 jQuery는 global scope안에 있으며, 우리의 `namespace`이기도 하다. jQuery namespace는 global scope에서 정의되며, 그 안의 모든 jQuery library를 위한 namespace로서 동작한다.

## Local scope

global scope외의 scope을 의미. 일반적으로 하나의 global scope이 존재하고, 정의된 각각의 function은 자신만의 local scope을 가지고 있다. 다른 function 내에 정의된 function은 바깥 function에 연결된 local scope을 가지고 있다.

```js
var myFunction = function() {
  var name = 'Todd';
  console.log(name); // Todd
};
console.log(name) // name is not defined
```

## Function scope

**Javascript내의 모든 scope들은 function scope과 함께 만들어진다.** 블록에서 scope이 만들어지는 것이 아니므로 조심!

```js
// global scope
var myFunction = function() {
  // scope 1
  var myOtherFunction = function() {
    // scope 2
  }
};
```

## Lexical scope

하나의 function내에 다른 function이 있으면, 내부의 function은 외부의 function의 scope에 접근 할 수 있다. 이것을 **Lexical Scope**또는 **Closure**라 부르며, **Static Scope**라 부르기도 한다.

```js
// global scope(name에 접근 불가능)
var myFunction = function() {
  // scope 1
  var name = 'Todd';
  var myOtherFunction = function() {
      // scope 2: 'name' 변수에 접근 가능
  };
};
```

## Scope chain

정의된 function은 각각 자신만의 중첩된 scope을 가지고 있다. local scope을 가진 내부 function은 바깥 function과 연결되어있고 , 그 연결을 **scope chain**이라고 한다. function내의 변수를 resolve할 때, js는 변수를 찾을 때까지 가장 내부의 scope -> 바깥 scope -> 글로벌 scope까지 변수를 검색한다.

## Closure

Lexical scope와 강하게 연결되어 있는 개념이다. nested된 함수들을 이용해 만들어진 **protected variable space**를 의미한다.

```js
var sayHello = function(name) {
  var text = 'Hello, ' + name;
  return function() {
    console.log(text);
  }
};

var helloTodd = sayHello('Todd');
helloTodd(); // 'Hello, Todd'

sayHello('Kim')(); // 'Hello, Kim'
```

## Scope와 this

각 scope는 어떻게 function이 호출되냐에 따라 달라지는 this값을 바인드 하고 있다. 하지만 this값은 호출될 때에 따라 달라지는 경우도 있다.

default this는 가장 바깥의 global object인 `window`를 가리킨다.

```js
var myFunction = function() {
  console.log(this); // [object Window]
};
myFunction();

var myObject = {};
myObject.myMethod = function() {
  console.log(this); // Object { myObject }
};

var nav = document.querySelector('.nav');
var toggleNav = function() {
  console.log(this); // <nav> element
};
nav.addEventListener('click', toggleNav, false);
```

## this값의 변화

```js
var nav = document.querySelector('.nav'); // <nav class="nav">
var toggleNav = function() {
  console.log(this); // <nav> element
  setTimeout(function() {
    console.log(this); // [object Window]
  }, 1000)
};
```

이벤트 핸들러로부터 호출되지 않은 새로운 scope이 생성되었고, 그래서 default인 window object가 this의 값이 된 것이다. 이를 해결하기 위해서는 `lexical scope`를 이용한 바인딩을 한다.

```js
var nav = document.querySelector('.nav'); // <nav class="nav">
var toggleNav = function() {
  var that = this; // this의 값을 that변수에 저장해놓음
  console.log(this); // <nav> element
  setTimeout(function() {
    console.log(that); // <nav> element
  }, 1000)
};
```

## Call, Apply, Bind를 이용하여 scope 변경하기

### Call & Apply

call과 apply는 함수를 호출하는 데에는 동일하나, 인수 구분을 배열로 하는가 그냥 넘겨주는가의 차이이다.

`function.call(scope, arg1, arg2, arg3)`

`function.apply(scope, [arg1, arg2 ...])`

```js
var links = document.querySelectorAll('nav li');
for (var i = 0; i < links.length; i++) {
  (function() {
    console.log(this); // links[i] element
  }).call(links[i]);
}
```

### Bind

bind는 function을 호출하지 않는다. 대신 function을 호출하기 전에 this를 바인드 할 뿐이다.

```js
nav.addEventListener('click', toggleNav.bind(scope, arg1, arg2), false);
```

위와 같이 함수의 내부의 this의 scope를 변경시키며 함수 자체를 넘겨줄 수 있다.

## Arrow function

- 일반 함수는 런타임 리시버에 따라서 `this`의 문맥이 정해짐
  - 함수를 실행하는 리시버는 누구인가?
- Arrow function은 컴파일 타임에 lexical scope로 `this`의 문맥이 고정
  - 함수가 정의된 문맥은?

```js
function Period (hours, minutes) {
  this.hours = hours
  this.minutes = minutes
}
Period.prototype.format = () => { // 전역 문맥에 고정
  console.log(this === window) // true
  return this.hour + ' hours and ' + this.minutes + ' minutes'
}

var walkPeriod = new Period(2, 30)
walkPeriod.format() // undefined hours and undefined minutes
```

## Private및 Public Scope

js에는 명시적인 public/private키워드가 존재하지 않는다. 하지만 `module pattern`을 이용해서 public/private scope를 만들 수 있다.

### private scope를 만드는 방법

```js
(function() {
  var myFunction = function() {
    // ....
  };
})();

myFunction(); // myFunction is not defined
```

### module pattern

내부 function을 public으로 만들고 싶으면, module pattern(revealing module pattern)이라 불리는 패턴을 이용하면 function의 scope를 올바르게 정할 수 있다.

```js
var Module = (function() {
  return {
    myMethod: function() {
      console.log('myMethod has been called.');
    }
  };
})();

// module + 메소드의 호출
Module.myMethod();
Module.someOtherMethod();
```

위의 코드에서 알 수 있듯이, Module이라는 global scope에서 정의된 namespace에서 각 메소드에 접근 가능하다.

**Object 반환을 통한 module 패턴 구현**

```js
var Module = (function() {
  var _privateMethod = function() {

  };
  return {
    publicMethod: function() {

    }
  };
})();
```

위와 같이 private method와 public method를 분리시켜 사용할 수 있다.

**Object 스타일로 정의된 Object 반환을 통한 module 패턴 구현**

```js
var Module = (function() {
  var _privateMethod = function() {

  };
  var publicMethod = function() {

  };
  return {
    publicMethod: publicMethod,
    anotherPublicMethod: anotherPublicMethod
  };
})();
```
