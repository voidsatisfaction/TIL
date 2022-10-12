# Generator

## Async Code and Its Problem

햄버거 가계의 예를 생각하면, 동기와 비동기가 무엇인지 잘 알 수 있다.

### Callback Hell

```js
// Call back hell!
async1(function(x) {
  async2(function(y) {
    async3(function(z) {
       // ...
    });
  });
});
```

콜백지옥은 프로그램을 이해하기 힘들게 만들고, 에러가 나기 쉽게 한다.

그래서 보통 Promise를 이용해서 문제를 해결해왔으나, ES6부터는 제너레이터가 언어레벨로 사용가능하기 때문에 Generator로 콜백지옥의 문제를 해결할 수 있다.

## Generators 101

### Creating Generators

```js
export function* gen() {
  return 'first generator';
};

const generatorResult = gen();
console.log(generatorResult.next().value); // first generator
```

`next()`함수를 이용해서 제너레이터에 대한 값을 얻을 수 있다.

### Caveats of Generators

1. `next()`함수를 계속 써서 값을 가져올 수 있는게 아니다. Generator는 수열과 같아서 한 번 항이 소비되면 다시 소비할 수 없다.
2. 혹시 다시 소비하고 싶으면, 새로 제너레이터 인스턴스를 하나 생성해야 한다.
3. 또한 서로 다른 Generator instance는 서로다른 state를 갖고 있을 수 있다.(next함수를 몇번 호출했느냐에 따라 다름)

### yield New Keyword

```js
export function* generatorSequence() {
  yield 'first';
  yield 'second';
  yield 'third';
}

generatorResult.next()) // { value: 'first', done: false });
generatorResult.next()) // { value: 'second', done: false });
generatorResult.next()) // { value: 'third', done: false});
generatorResult.next()) // { value: undefined, done: true});
```

`yield`는 generator function의 실행을 정지시키고, **그 결과를 호출한 쪽으로 반환한다(return과 비슷함 만일 yield옆에 expression이 놓인다면 평가한 뒤에 그 값을 반환함)** 또한 어디서 반환했는지 상태를 기억한다(그 뿐 아니라, 함수 내부의 모든 상태를(메모리에) 기억함)

제러네리터는 결국 값의 수열이다(sequence of values) 그리고, 모든 `yield`키워드를 가진 generator들은 lazy evaluation order로 실행된다.

### c.f lazy evaluation

코드를 실행하라고 하기 전까지 실행하지 않는것을 의미한다. 여기서는 `generatorSequence`함수가 generator가 lazy evaluated되는것을 보여준다.

### done Property of Generator

```js
generatorResult.next()) // { value: 'first', done: false });
```

위에서 `done`속성은 제너레이터 수열이 전부 소진되었는지 확인해주는 역할을 한다.

```js
for(let value of generatorSequence()) {
  console.log(value);
  // first
  // second
  // third
}
```

위와 같이 결과 값이 출력된다.(ES6에서의 문법)

### Passing Data to Generators

```js
export function* sayFullName() {
  var firstName = yield;
  var secondName = yield;
  yield firstName + secondName;
}

const fullName = sayFullName();

fullName.next() // { value: undefined, done: false };
fullName.next('anto') // { value: undefined, done: false };
fullName.next('aravinth') // { value: 'antoaravinth', done: false };
fullName.next() // { value: undefined, done: true };
```

외부에서 generator에 값을 넘겨줄 때에는, 일단 처음에 `next()`를 실행한다. 그러면, 제너레이터 안의 `yield`가 있는 곳에서 제너레이터의 작동이 멈춘다. 그리고 그 다음에 `next('anto')`를 실행하면, 'anto'라는 값을 넘겨주고 `yield`가 나올때까지 코드를 실행한다. ....

## Using Generators to Handle Async Calls

Generator에 값을 넘겨주는게 왜 강력한지에 대하여.

### Generators for Async - A Simple Case

```js
let generator;
const getDataOne = () => {
  setTimeout(() => {
    generator.next('dummy data one');
  }, 1 * 1000);
};

const getDataTwo = () => {
  setTimeout(() => {
    generator.next('dummy data two');
  }, 1 * 1000);
};

function* main() {
  const dataOne = yield getDataOne();
  const dataTwo = yield getDataTwo();
  console.log(dataOne);
  console.log(dataTwo);
}

generator = main();
generator.next();
// dummy data one
// dummy data two
```

1. 위의 경우에서는 먼저, main을 위한 generator instance를 생성해둔다.
2. `generator.next()`로 제너레이터인 main함수를 호출한다.
3. 호출한 main함수는 실행모드로 되는데 첫번째 줄에서 `yield`를 확인한다.
4. 일단 `getDataOne()`을 실행한 후에 정지 모드에 들어간다.
5. `getDataOne()`안에 `generator.next('dummy data one')`이 있으므로, 정지된 `yield`를 재개한다.
6. 일단 `getDataTwo()`를 실행한 후에 `yield`가 있으므로 정지 모드에 들어간다.
7. `getDataTwo()`안에 `generator.next('dummy data two')`가 있으므로, 정지된 `yield`를 재개한다.
8. dataOne, dataTwo를 출력한다.

Q) 뭔가 `next()`를 실행하면, `yield`의 오른쪽을 먼저 실행하고 바로 멈추는 느낌?

### 주의!! 비록 `yield`가 제너레이터 속의 statement를 멈추게 하지만, 이것이 호출한곳을 멈추게 하지 않는다(caller is not blocked)

### Generators for Async - A Real-World Case

```js
function httpGetAsync(url, callback) {
  return https.get(url,
    function(response) {
      let body = '';
      response.on('data', (d) => {
        body += d;
      });
      response.on('end', () => {
        let parsed = JSON.parse(body);
        callback(parsed);
      });
    }
  );
}

function request(url) {
  httpGetAsync(url, (response) => {
    generator.next(response);
  });
}

function* main() {
  try {
    const picturesJson = yield request('https://www.reddit.com/r/pics/.json');
    const firstPictureData = yield request(picturesJson.data.children[0].data.url + '.json');
    console.log(firstPictureData);
  } catch(e) {
    console.error(e);
  }
  done();
}

const generator = main();
generator.next();
```

Looks like synchronous code, but it works in asynchronous fashion!

### Generator 구문 해석하기

```js
function* generator(n) {
  let i = 0;
  while(i < n) {
    yield i;
    i += 1;
  }
}

for (let n of generator(5)) {
  console.log(n);
}
```

1. for 문이 실행되며, 먼저 generator 함수가 호출된다.
2. generator 함수는 일반 함수와 동일한 절차로 실행된다.
3. 실행 중 while 문 안에서 yield 를 만나게 된다. 그러면 **return 과 비슷하게 함수를 호출했던 구문으로 반환**하게 된다. 여기서는 첫번재 i 값인 0 을 반환하게 된다. 하지만 반환 하였다고 generator 함수가 종료되는 것이 아니라 그대로 유지한 상태이다.
4. x 값에는 yield 에서 전달 된 0 값이 저장된 후 print 된다. 그 후 for 문에 의해 다시 generator 함수가 호출된다.
5. 이때는 generator 함수가 처음부터 시작되는게 아니라 yield 이후 구문부터 시작되게 된다. 따라서 i += 1 구문이 실행되고 i 값은 1로 증가한다.
6. 아직 while 문 내부이기 때문에 yield 구문을 만나 i 값인 1이 전달 된다.
7. x 값은 1을 전달 받고 print 된다. (이후 반복)
