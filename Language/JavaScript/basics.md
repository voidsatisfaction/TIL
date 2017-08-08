# Javascript Basic

## Traits

### 1. Loosely Typed Language

- Primitive types(value)
  - booleans
  - numbers
  - strings
- Other types(reference)
  - functions
  - objects(arrays)
  - null
  - undefined

### 2. Functions As First-Class Objects

First-Class Citizen

- Stored in variavbles
- Passed into other functions as arguments
- Passed out of functions as return values
- Constructed at run-time

Scope

- Function-level scope
- Lexical scope

```js
// lambda function example
(function() {
  var foo = 10;
  var bar = 2;
})();

var baz = (function(foo, bar) {
  return foo * bar;
})(10, 2);

// closure
var baz;

(function() {
  var foo = 10;
  var bar = 2;
  baz = function() {
    return foo * bar;
  };
})();

baz(); // 20
```

### 3. The Mutability of Objects

자바스크립트에서는 모든것이 object(세가지의 primitive datatypes제외. 심지어 세가지 타입도 objects로 바로 덮어씌워진다) 게다가, 모든 objects들은 **mutable**이다. 함수도 object이기 때문에 다음과 같은 일도 가능하다.

```js
function displayError(message) {
  displayError.numTimesExecuted++;
  alert(message);
}
displayError.numTimesExecuted = 0;
```

class와 objects를 그것들이 initiated된 이후에 변경할 수 있다.

```js
function Person(name, age) {
  this.name = name;
  this.age = age;
}

Person.prototype = {
  getName: function() {
    return this.name;
  },
  getAge: function() {
    return this.age;
  }
}

var alice = new Person('Alice', 30);
var bill = new Person('Bill', 30);

Person.prototype.getGreeting = function() {
  return 'Hi ' + this.getName() + '!';
}

alice.displayGreeting = function() {
  console.log(this.getGreeting()); // Hi Alice!
}

alice.displayGreeting();
console.log(bill.getGreeting()); // Hi Bill!
```

js에서는 런타임에 모든것을 바꿀 수 있다.

### 4. Inheritance

js에서는 object-based(prototype) inheritance를 사용한다. 하지만 class-based inheritance의 구현도 가능하다.
