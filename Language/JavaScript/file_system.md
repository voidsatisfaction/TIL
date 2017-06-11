# File system

## 출처

- [fs: Stream의 개념과 Stream2의 차이](http://programmingsummaries.tistory.com/363)

## 파일 시스템 개요

Nonblocking system

언제나 sync / async의 모듈을 갖고 있음

```js
// 비동기의 경우
var fs = require('fs');

fs.readFile('./test.js',function(data, err) {
  if (err) {
    return console.log(err);
  }

  console.log('test file is loaded', data);
});

// 동기의 경우
var data = fs.readFileSync('./test.js');
```

## File stream

비동기로 파일을 불러오면 많은 리소스를 효율적으로 사용할 수 있으나,

대용량의 파일의 경우에는 파일 전체를 로드하기 전에 **메모리 버퍼를 절약**하고 싶을 수 있다.

### 1. 읽기 스트림

```js

// 데이터의 일부를 받을 때 마다 파일에 쓰게 된다.
var fs = require('fs');
var request = require('request');

var stream = request('http://i.imgur.com/dmetFjf.jpg');
var writeStream = fs.createWriteStream('test.jpg');

stream.on('data', function(data) {
  // 내가 얼마나 읽을지는 제어할 수 없다.
  writeStream.write(data);
  console.log('loaded part of the file');
});

stream.on('end' function() {
  writeStream.end();
  console.log('all parts are loaded');
});

stream.on('error' function(err) {
  writeStream.close();
  console.log('sth is wrong ...');
});

```

### 2. pipe

입력을 출력으로 리다이렉트 할 수 있게 해주는 것.

위의 코드는 아래와 같다.

```js

var fs = require('fs');
var request = require('request');

var stream = request('http://i.image.com/image.jpg');
var writeStream = fs.createWriteStream('test.jpg');

stream.pipe(writeStream);

```

pipe로 stream간에 read와 write event를 연결.

여러개의 파이프를 연결 할 수도 있다.

### 3. Readable and Writeable stream

읽는 타이밍이나 쓰는 타이밍에 얼마나 읽고 쓸지 제어할 수 있게 해준다.

```js
/* Readable 의 경우 */
// node.js v0.10 이상
var fs = require('fs');
var stream = fs.createReadStream('./testimg.jpg');
var writeStream = fs.createWriteStream('./output.jpg');

stream.on('readable', function () {
	// stream 이 읽을 준비가 됨
	var data = stream.read();
	writeStream.write(data);
});

stream.on('end', function () {
	writeStream.end();
});

/* Writeable의 경우 */
// node.js v0.10 이상 + 이 코드가 잘 이해가 안됨.
var fs = require('fs');

var stream = fs.createReadStream('./input.mp4');
var writeStream = fs.createWriteStream('./output.mp4');

var writable = true;
var doRead = function () {
	var data = stream.read();
	//만약 wriable이 false 를 리턴한다면, buffer가 꽉 차있다는 뜻이다.
	writable = writeStream.write(data);
}

stream.on('readable', function () {
	if(writable) {
		doRead()
	} else {
		// stream buffur가 꽉 찼으니 drain 이벤트가 발생할 때까지 대기
		writeStream.removeAllListeners('drain');
		writeStream.once('drain', doRead)
	}
});

stream.on('end', function () {
	writeStream.end();
});

```
