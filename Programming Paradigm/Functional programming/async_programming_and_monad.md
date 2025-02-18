# 모나드와 비동기 프로그래밍

- 콜백
- 프로미스

[참고 - Callback에서 Future로](http://seoh.blog/2015/05/28/callback-to-future-functor-applicative-monad/)

[참고 - promise_monad](https://gist.github.com/MaiaVictor/bc0c02b6d1fbc7e3dbae838fb1376c80)

[참고 - Monad Programming with Scala Future](http://tech.kakao.com/2016/03/03/monad-programming-with-scala-future/)

## 콜백

자바스크립트 계열의 언어에서 비동기 프로그래밍을 시행할 경우, 가장 원시적인 방법은 콜백을 이용하는 것이다.

```js
function async1(fn) {
  const val = 3
  setTimeout(() => {
    fn(val);
  }, 1 * 1000);
}

async1((v) => {
  console.log(v); //1초뒤 3을 출력
});
```

하지만 컬백을 사용할 경우 다음과 같은 문제가 발생한다

- 컬백으로 프로그램의 흐름을 제어할 경우 컬백 지옥이 발생. 그 결과 프로그램이 복잡해짐.
- 컬백은 아무런 값도 반환하지 못하므로 언제나 부작용을 내포함. 그 결과 프로그램이 복잡해짐.
- **결국 프로그램의 규모가 커지면 흐름 제어가 복잡해지는 문제가 생김**

컬백은 아무런 값도 반환하지 못하므로 비동기 프로그래밍이 포함되면 프로그램 자체가 컬백 함수 내부에서 완결되어야 한다. 이는 점점 내부비대화를 야기하는데, 이것을 막기 위해서는 값을 어떻게든 반환할 수 있도록 제어하는게 중요하다(동기 프로그래밍 처럼)

컬백은 마치 블랙홀과 같다!

```js
const result = async1() // 어떻게든 이렇게 값을 반환할 수 있도록 하는게 바람직
console.log(result);
```

## 프로미스

컬백에서 한단계 발전된 비동기 프로그래밍 방식은 프로미스의 활용이다. 프로미스는 비동기 프로그래밍의 결과에서 나온 값을 래핑해서 값을 재활용 하면서 쓰는 방식이다.

```js
// future monad

```
