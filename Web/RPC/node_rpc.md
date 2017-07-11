# RPC with Nodejs

## Nodejs에서 Protocol Buffer를 사용하기 위한 방법

1. Protobuf.js를 사용하여 동적으로 코드 생성

2. protoc 컴파일러를 사용하여 정적으로 코드 생성

## 서비스 디자인

### 1. Proto파일

```proto3
service RouteGuide {
  // 단순히 클라이언트가 서버에게 요청하여 서버가 메세지를 읽는다.
  rpc GetFeature(Point) returns (Feature) {}

  // 클라이언트는 서버의 스트림 메세지를 끝까지 계속 읽는다.
  rpc ListFeatures(Rectangle) returns (stream Feature) {}

  // 클라이언트가 메세지를 끝까지 다 쓰면 서버가 그 메세지를 다 읽고 응답을 반환할때까지 기다린다.
  rpc RecordRoute(stream Point) returns (RouteSummary) {}

  // 양방향 스트리밍 RPC: 양쪽이 동시에 메세지를 읽고 쓰면서 통신한다(클라이언트, 서버 각각의 메세지의 순서는 보장된다)
  rpc RouteChat(stream RouteNote) returns (stream RouteNote) {}
}
```

### 2. proto파일에서 service descriptor가져오기

```js
var grpc = require('grpc');
var protoDescriptor = grpc.load(__dirname + '/route_guide.proto');
// example은 sub constructor의 examples네임스페이스에 접근
var example = protoDescriptor.examples;
```
### 3. 서버 만들기

`RouteGuide`서비스는 두가지 파트로 이루어져 있다.

1. 서비스 정의에 기반한 서비스 인터페이스의 도입 부분
2. 클라이언트 requests에 대한 responses를 돌려주는 서버의 작동 부분

#### 3-1. RouteGuide의 도입

이하는 server side에서 stub constructor를 도입한 경우이다.

```js
var routeguide = grpc.load(PROTO_PATH).routeguide;
```

가장 간단한 `getFeature`라는 서비스를 보자.

routeguide proto3을 보면,

**클라이언트로부터 Point타입의 메세지를 인자로 받아서, 그 응답으로 Feature타입의 메세지를 인자로 갖는 callback함수를 돌려준다.**

```js
// proto
rpc GetFeature(Point) returns (Feature) {}

// server
function checkFeature(point) {
  var feature;
  // Check if there is already a feature object for the given point
  for (var i = 0; i < feature_list.length; i++) {
    feature = feature_list[i];
    if (feature.location.latitude === point.latitude &&
        feature.location.longitude === point.longitude) {
      return feature;
    }
  }
  var name = '';
  feature = {
    name: name,
    location: point
  };
  return feature;
}
function getFeature(call, callback) {
  callback(null, checkFeature(call.request));
}

```

두번째로 서버사이드 streaming RPC인 `listFeatures`를 보자.

```js
// proto
rpc ListFeatures(Rectangle) returns (stream Feature) {}

// server
function listFeatures(call) {
  var lo = call.request.lo;
  var hi = call.request.hi;
  var left = _.min([lo.longitude, hi.longitude]);
  var right = _.max([lo.longitude, hi.longitude]);
  var top = _.max([lo.latitude, hi.latitude]);
  var bottom = _.min([lo.latitude, hi.latitude]);
  // For each feature, check if it is in the given bounding box
  _.each(feature_list, function(feature) {
    if (feature.name === '') {
      return;
    }
    if (feature.location.longitude >= left &&
        feature.location.longitude <= right &&
        feature.location.latitude >= bottom &&
        feature.location.latitude <= top) {
      call.write(feature);
    }
  });
  call.end();
}

//client
function runListFeatures(callback) {
  var rectangle = {
    lo: {
      latitude: 400000000,
      longitude: -750000000
    },
    hi: {
      latitude: 420000000,
      longitude: -730000000
    }
  };
  console.log('Looking for features between 40, -75 and 42, -73');
  var call = client.listFeatures(rectangle);
  call.on('data', function(feature) {
      console.log('Found feature called "' + feature.name + '" at ' +
          feature.location.latitude/COORD_FACTOR + ', ' +
          feature.location.longitude/COORD_FACTOR);
  });
  call.on('end', callback);
}

```

이번에는 writeable한 call object를 클라이언트가 server의 listFeatures service에 넘겨준다.

서버는 계속해서 feature를 작성하고 다 작성하면 `end()`를 불러준다.

마지막으로 RouteChat()이라는 양방향 streaming RPC를 보자.

```js
// proto
rpc RouteChat(stream RouteNote) returns (stream RouteNote) {}

// server
function routeChat(call) {
  call.on('data', function(note) {
    var key = pointKey(note.location);
    /* For each note sent, respond with all previous notes that correspond to
     * the same point */
    if (route_notes.hasOwnProperty(key)) {
      _.each(route_notes[key], function(note) {
        call.write(note);
      });
    } else {
      route_notes[key] = [];
    }
    // Then add the new note to the list
    route_notes[key].push(JSON.parse(JSON.stringify(note)));
  });
  call.on('end', function() {
    call.end();
  });
}

//client
function runRouteChat(callback) {
  var call = client.routeChat();
  call.on('data', function(note) {
    console.log('Got message "' + note.message + '" at ' +
        note.location.latitude + ', ' + note.location.longitude);
  });

  call.on('end', callback);

  var notes = [{
    location: {
      latitude: 0,
      longitude: 0
    },
    message: 'First message'
  }, {
    location: {
      latitude: 0,
      longitude: 1
    },
    message: 'Second message'
  }, {
    location: {
      latitude: 1,
      longitude: 0
    },
    message: 'Third message'
  }, {
    location: {
      latitude: 0,
      longitude: 0
    },
    message: 'Fourth message'
  }];
  for (var i = 0; i < notes.length; i++) {
    var note = notes[i];
    console.log('Sending message "' + note.message + '" at ' +
        note.location.latitude + ', ' + note.location.longitude);
    call.write(note);
  }
  call.end();
}

```

하나의 `routeChat`라는 함수를 이용하여 두가지의 스트리밍을 할 수 있다(client -> server, server -> client)

#### 3-2. 서버를 시작한다.

먼저 서버를 생성한다.

```js
function getServer() {
  var server = new grpc.Server();
  server.addProtoService(routeguide.RouteGuide.service, {
    getFeature: getFeature,
    listFeatures: listFeatures,
    recordRoute: recordRoute,
    routeChat: routeChat
  });
  return server;
}
var routeServer = getServer();
routeServer.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
routeServer.start();
```

1. `RouteGuide` service descriptor로부터 Server constructor를 생성한다.
2. serviceMethods를 도입한다.
3. 서버의 인스턴스를 생성한다.
4. `address`와 `port`를 지정하여 클라이언트의 request를 들을 수 있도록 한다.
5. RPC서버를 시작하기 위하여 `start()`함수를 실행한다.

### 4. 클라이언트 만들기

#### 4-1 stub생성

service메소드를 실행하기 위해서는 stub를 생성해야한다.

```js
new RouteGuide('localhost:50051', grpc.credentials.createInsecure());
```

#### 4-2 service methods 호출

service methods는 기본적으로 비동기처리 된다. 따라서 이벤트를 이용하거나 콜백을 이용해서 결과값을 얻는다.

**가장 간단한 모델**

```js

var point = {latitude: 409146138, longitude: -746188906};
stub.getFeature(point, function(err, feature) {
  if (err) {
    // process error
  } else {
    // process feature
  }
});

```

**RPCs 스트리밍**

서버의 스트리밍의 경우 `request`와 `callback`을 넘겨주는 대신,

`request`만을 넘겨주고 Readable stream object만 돌려받는다.

클라이언트는 `Readable`의 `data` 이벤트를 사용하여 서버의 responses를 읽는다.

서버의 모든 Feature message가 전송되고 나면은 `end`이벤트가 발동된다.

그리고 서버가 status를 전송했을 떄, `status`가 발동된다.

```js
var call = client.listFeatures(rectangle);
  call.on('data', function(feature) {
      console.log('Found feature called "' + feature.name + '" at ' +
          feature.location.latitude/COORD_FACTOR + ', ' +
          feature.location.longitude/COORD_FACTOR);
  });
  call.on('end', function() {
    // The server has finished sending
  });
  call.on('status', function(status) {
    // process status
  });
```
