# Generic

## 참고

- [제네릭이란 무엇일까? - 꿈꾸는 프로그래머](http://slaner.tistory.com/122)

## 제네릭이란

형식 매개 변수. 즉 형식(type)을 동적으로 설정할 수 있다.

평범한 인터페이스

```cs
// 타입이 이미 정해져 있다.
interface INonGenericInterface {
    Int32 Add(Int32 num);
    Int32 Sub(Int32 num);
    Int32 Mul(Int32 num);
    Int32 Div(Int32 num);
}
```

제네릭을 사용한 인터페이스

```cs
// 타입이 정해지지 않았다.
interface IGenericInterface<T> {
    T Add(T num);
    T Sub(T num);
    T Mul(T num);
    T Div(T num);
}

// 이렇게 사용할 수 있다. T => Int32로 변함
IGenericInterface<Int32> int32GenericInterface;
```
