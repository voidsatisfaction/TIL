# Event loop

## 의문

## 개요

- Node.js 플랫폼이 kernel에 일감을 던져줘서 non-blocking I/O operation을 할 수 있도록 하게 해주는 것
  - JavaScript가 싱글스레드임에도 non-blocing으로 하게 해줌
  - 현대 커널들은 multi-threaded
    - 백그라운드에서 실행하고 끝나면 Node.js에 알려줘서 callback을 poll queue에 추가함

## 설명

Nodejs event loop overview diagram(each box is a phase of the event loop)

![](./images/nodejs_event_loop_overview1.png)

- Node.js가 시작
  - event loop를 initialize
  - async API call이나 schedule timer나 `process.nextTick()`과 같은 것을 호출하는 input script를 처리하고, event loop처리를 시작함
- c.f) libuv는 무슨 일을 하는가?
  - **Node.js의 event loop와 비동기 동작을 구현할 때 사용되는 C라이브러리**
- Event loop의 구조
  - 개요
    - phase로 이루어져 있음
      - 각 phase는 callback들의 queue를 갖음
    - event loop의 각각의 실행 사이에, node.js는 기다리는 비동기 I/O or timer가 있는지 체크하고, 아무것도 없다면 깔끔하게 shut down
      - *이벤트 루프가 shut down된다는 것은, 결국, 프로그램이 종료된다는 것을 의미하는가? 아니면, 프로그램은 종료가 안되었는데, 그냥 아무것도 실행을 안할경우에 이벤트 루프가 잠깐 종료가 된다는것인가?*
        - 전자가 맞는거 같긴한데.. (왜냐하면 코드의 실행도 이벤트루프에서 싱글스레드로 이루어지기 때문)
  - phase
    - 동작
      - event loop가 특정 phase로 진입
      - 해당 phase specific한 동작 수행
      - 해당 phase의 callback들을 queue가 비워질때까지 or 최대개수의 callback이 실행될때까지 수행
      - 다음 phase로 이동
    - 종류
      - timers
        - `setTimeout()`, `setInterval()`로 스케줄링된 콜백을 실행
      - pending callbacks
        - *next loop iteration으로 연기된* I/O callbacks을 실행
          - *정확히 무슨의미?*
      - idle, prepare
        - *내부적으로만 사용*
      - poll
        - 새 I/O 이벤트를 가져오고, I/O 관련 callback들을 실행
          - 거의 모든 callbacks을 실행함(close callback, timer 로 등록된 callback, `setImmediate()`)
      - check
        - `setImmediate()`의 callback이 실행
      - close callbacks
        - `socket.on('close', ...)`와 같은 close callback

### Timers phase

- 개요
  - timer는 callback이 실행될 수 있는, threshold를 설정하는 것
    - 정확한 시간이 아님
    - OS scheduling이나 다른 callback이 이것의 실행을 지연시킬 수 있음
    - 기술적으로는 poll phase가 timer가 언제 실행될지 제어

코드 예시

```js
const fs = require('fs');

function someAsyncOperation(callback) {
  // Assume this takes 95ms to complete
  fs.readFile('/path/to/file', callback);
}

const timeoutScheduled = Date.now();

setTimeout(() => {
  const delay = Date.now() - timeoutScheduled;

  console.log(`${delay}ms have passed since I was scheduled`);
}, 100);

// do someAsyncOperation which takes 95 ms to complete
someAsyncOperation(() => {
  const startCallback = Date.now();

  // do something that will take 10ms...
  while (Date.now() - startCallback < 10) {
    // do nothing
  }
});
```

- 코드 해설
  - event loop가 poll phase에 진입
    - 처음에는 `fs.readFile()`의 동작이 끝나지 않았으므로, 빈 큐만 존재
    - 가장 빠른 timer의 threshold가 도달할 때까지 기다림(100ms)
  - 95ms가 경과
    - `fs.readFile()`이 file읽기가 끝나고, 그것의 10ms짜리 콜백이 poll queue에 추가
    - 위의 콜백 실행
  - 105ms가 경과(콜백 실행 후)
    - poll queue에 아무것도 존재하지 않음
    - event loop는 가장 빠른 timer의 threshold가 도달했음을 알고, timers phase에 가서 timer의 콜백을 실행
    - 따라서 105ms에 timer의 콜백이 실행됨
  - c.f) poll phase가 event loop를 잠식하는것 방지
    - libuv에 hard maximum polling event제한이 존재

### Pending callbacks phase

- 개요
  - TCP 에러와 같은 시스템 동작 콜백을 실행하는 phase
- 예시
  - TCP소켓이 connect를 시도할 때, `ECONNREFUSED`를 받으면, 몇몇 *nix 시스템은 에러를 리포팅하기위해서 대기함
  - 이는 pending callbacks phase에 큐잉됨

### Poll phase

- 개요
  - 1 I/O를 위해서 얼마나 오래 block해야하는지, polling해야하는지 계산
  - 2 poll queue에 있는 이벤트 처리
- 동작
  - timer schedule이 없는 경우
    - poll queue가 비어있지 않은 경우
      - event loop가 해당 큐를 iterate하면서 callback을 동기적으로 실행
      - 큐안에 있는것 전부 or maximum hard limit개수만큼
    - poll queue가 비어있는 경우
      - `setImmediate()`가 스케쥴링 되어있는 경우
        - check phase로 진행해서 스케쥴링된 스크립트 실행
      - `setImmediate()`가 스케쥴링 되어있지 않은 경우
        - callback이 queue에 추가될 때 까지 대기하고, 즉각 실행
  - poll queue가 다 비어지면, timer를 체크해서, time threshold가 도달했는지 확인하고, 준비된 callback은 event loop가 timers phase로 진행하여 콜백을 실행

### Check phase

### Close callbacks phase

- 개요
  - 소켓이나 handle이 갑자기 close되는 경우, 'close'이벤트가 이 phase에 발생되며, 그렇지 않은 경우에 `process.nextTick()`으로 발생됨
