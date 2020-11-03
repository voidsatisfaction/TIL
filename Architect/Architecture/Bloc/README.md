# Bloc

- 의문
- Why?
- Core Concepts
  - Streams
    - Stream events를 받는 법
    - Stream의 종류
    - stream을 가공하는 methods
    - stream을 수정하는 methods
  - Cubit
  - Bloc

## 의문

## Why?

view와 business logic의 분리

- Core value
  - Simple
    - 다양한 레벨의 개발자도 쉽게 이해 가능
  - Powerful
    - 작은 컴포넌트의 조합으로 복잡한 애플리케이션 제작 가능
  - Testable
    - 애플리케이션의 모든 부분을 테스트 가능 -> Reliable
- 특징
  - state 변화를 오직 한가지 방법으로만 가능하게 함
    - state 변화를 predictable하게 함

## Core Concepts

### Streams

- 정의(dart)
  - sequence of asynchronous events
  - 사실상 async generator
- 특징
  - Future vs Stream
    - 개요
      - **pull vs push**
    - Future
      - 자신이 요청해서 다음 이벤트를 받음 pull
    - Stream
      - 이벤트가 준비되면 자신에게 stream이 event가 준비되었다고 push

#### Stream events를 받는 법

Stream events를 받는 법

```dart
Future<int> sumStream(Stream<int> stream) async {
  var sum = 0;
  await for (var value in stream) {
    sum += value;
  }
  return sum;
}

// async generator
Stream<int> countStream(int to) async* {
  for (int i = 1; i <= to; i++) {
    yield i;
  }
}

main() async {
  var stream = countStream(10);
  var sum = await sumStream(stream);
  print(sum); // 55
}
```

Stream을 이용한 error handling

```dart
import 'dart:async';

Future<int> sumStream(Stream<int> stream) async {
  var sum = 0;
  try {
    await for (var value in stream) {
      sum += value;
    }
  } catch (e) {
    return -1;
  }
  return sum;
}

Stream<int> countStream(int to) async* {
  for (int i = 1; i <= to; i++) {
    if (i == 4) {
      throw new Exception('Intentional exception');
    } else {
      yield i;
    }
  }
}

main() async {
  var stream = countStream(10);
  var sum = await sumStream(stream);
  print(sum); // -1
}
```

#### Stream의 종류

- Single subscription streams
  - 개요
    - 더 큰 전체의 부분인 이벤트들의 sequence를 포함하는 스트림
  - 특징
    - 이벤트들은 올바른 순서와, missing이 없이 전달되어야 함
    - 한 번에 모든 스트림데이터를 가져옴
  - 예시
    - file
    - web request
- Broadcast streams
  - 개요
    - 한번에 한개씩 다루어질 수 있는 개개의 메시지를 다루기 위한 스트림
  - 특징
    - 해당 스트림을 언제든지 listen 가능
    - 하나 이상의 listener 존재 가능
    - subscription cancel한 후 다시 subscribe가능
  - 예시
    - 브라우저의 마우스 이벤트

#### stream을 가공하는 methods

stream을 가공하고, result를 반환

```dart
Future<T> get first;
Future<bool> get isEmpty;
Future<T> get last;
Future<int> get length;
Future<T> get single;
Future<bool> any(bool Function(T element) test);
Future<bool> contains(Object needle);
Future<E> drain<E>([E futureValue]); // ???
Future<T> elementAt(int index);
Future<bool> every(bool Function(T element) test);
Future<T> firstWhere(bool Function(T element) test, {T Function() orElse});
Future<S> fold<S>(S initialValue, S Function(S previous, T element) combine);
Future forEach(void Function(T element) action);
Future<String> join([String separator = ""]);
Future<T> lastWhere(bool Function(T element) test, {T Function() orElse});
Future pipe(StreamConsumer<T> streamConsumer); // ????
Future<T> reduce(T Function(T previous, T element) combine);
Future<T> singleWhere(bool Function(T element) test, {T Function() orElse});
Future<List<T>> toList();
Future<Set<T>> toSet();
```

- 뭐하는 거지?
  - `drain()`
  - `pipe()`

#### stream을 수정하는 methods

original stream을 기반으로 new stream을 반환

```dart
Stream<R> cast<R>();
Stream<S> expand<S>(Iterable<S> Function(T element) convert);
Stream<S> map<S>(S Function(T event) convert);
Stream<T> skip(int count);
Stream<T> skipWhile(bool Function(T element) test);
Stream<T> take(int count);
Stream<T> takeWhile(bool Function(T element) test);
Stream<T> where(bool Function(T event) test);

// argument can be async function
Stream<E> asyncExpand<E>(Stream<E> Function(T event) convert);
Stream<E> asyncMap<E>(FutureOr<E> Function(T event) convert);
Stream<T> distinct([bool Function(T previous, T next) equals]);

// Error handling
Stream<T> handleError(Function onError, {bool test(error)});
Stream<T> timeout(Duration timeLimit,
    {void Function(EventSink<T> sink) onTimeout});

// generalized "map" for stream
// take several incoming events to produce an output event
Stream<S> transform<S>(StreamTransformer<T, S> streamTransformer);

// low-level method
// all other stream functions are defined in terms of listen()
StreamSubscription<T> listen(void Function(T event) onData,
    {Function onError, void Function() onDone, bool cancelOnError});
```

Stream Error handling예시

```dart
Stream<S> mapLogErrors<S, T>(
  Stream<T> stream,
  S Function(T event) convert,
) async* {
  var streamWithoutErrors = stream.handleError((e) => log(e));
  await for (var event in streamWithoutErrors) {
    yield convert(event);
  }
}
```

Transformer 예시

```dart
import 'dart:convert';
import 'dart:io';

Future<void> main(List<String> args) async {
  var file = File(args[0]);
  var lines = utf8.decoder
      .bind(file.openRead())
      .transform(LineSplitter());
  await for (var line in lines) {
    if (!line.startsWith('#')) print(line);
  }
}
```

- `listen()` method
  - 개요
    - stream을 listening할 수 있도록 함
  - 특징
    - listen하기 전 까지는 비활성화
    - listen하면 => event를 producing하는 것을 나타내는 `StreamSubscription` 오브젝트가 반환됨
      - Iterable이 단순한 오브젝트의 컬렉션이나, iterator가 실제의 iteration을 하는것과 유사함
    - `StreamSubscription`은 subscription을 pause, resume, cancel할 수 있도록 함
- 뭐하는 거지?
  - `cast()`
  - `expand()`

### Cubit

![](./images/cubit1.png)

- 정의
  - `Bloc` 클래스의 베이스로 사용되는 특별한 타입의 `Stream`
  - 일종의 observable
    - `listen()`으로 subscribe(listen, observe)가능
- 특징
  - state 변화를 트리거링할 수 있는 함수를 노출함
  - state는 `Cubit`의 output이고, application의 상태의 일부를 나타냄
    - UI 컴포넌트는 state를 푸시받고, 자체적으로 일부만 current state기반으로 redraw함

### Bloc
