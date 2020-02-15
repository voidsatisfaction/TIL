# Sockets

- 의문
- Sockets
- 역사
- 소켓의 동작
- 소켓의 사용

## 의문

- socket은 OSI 7 layer에서 어떤 layer에 해당할까?
- pub-sub랑 socket통신과의 차이점? 애초에 pub-sub는 뭐지?

## [Sockets - Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html)

- 종류
  - INET(e.g IPv4) sockets
    - STREAM(e.g TCP) sockets
  - blocking, non-blocking sockets
- 주의
  - 소켓이라는 말 자체가 문맥에 따른 여러가지의 미묘하게 다른 것들을 의미
  - client socket(client only)과 server socket(client + server sockets)의 분리

## 역사

- IPC(Inter-Process Communication)
  - socket을 이용한 통신이 가장 인기 있는 방식
    - 특히 cross-platform communication의 경우
  - INET과 socket의 조합으로, 임의의 기계들과 쉽게 커뮤니케이션 가능함
- 그 외의 IPC 방식
  - 하나의 머신에서 사용하는 경우
    - `pipes`
    - `shared memory`
    - `AF_INET` socket 등

## 소켓의 동작

임의의 웹 페이지에 접속 하는경우, 우리의 브라우저는 아래와 같은 행위를 함

**클라이언트의 경우**

```py
# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("www.python.org", 80))
```

- `connect`가 완료되면, 소켓은 페이지의 텍스트를 받기 위한 request를 보내기 위해서 사용될 수 있음. 그리고 같은 소켓은 응답을 읽고, **파괴** 됨.
- Client socket은 일반적으로 하나의 exchange혹은 작은 연속된 exchanges을 위해서만 사용됨

**서버의 경우**

```py
# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind((socket.gethostname(), 80))
# become a server socket
serversocket.listen(5)
```

- `socket.gethostname()`을 사용하여, 바깥에서도 볼 수 있게 함
  - `s.bind(('localhost', 80))` or `s.bind(('127.0.0.1', 80))`을 사용해도 이는 서버소켓이나, ip주소에서 보이듯이 local machine에서만 볼 수 있음 `s.bind(('',80))`은 기계가 갖게 되는 어떤 주소라도 도달할 수 있는 것을 나타냄
- `listen(5)`는 소켓 라이브러리가 최대 5개의 request를 queue up 할 수 있는 것을 나타냄(그 이상 넘어가면 refuse함)

```py
while True:
  # accept connections from outside
  (clientsocket, address) = serversocket.accept()
  # now do something with the clientsocket
  # in this case, we'll pretend this is a threaded server
  ct = client_thread(clientsocket)
  ct.run()
```

- 위의 루프가 동작할 수 있도록 하는 일반적인 방법
  - ① `clientsocket`을 다루기 위한 새 스레드를 dispatching or 새 프로세스 생성
  - ② non-blocking socket을 사용하도록 앱 자체를 재구성하기
  - ③ `select`를 사용하여 active한 `clientsocket`들과 server socket를 *multiplex하기*
    - *multiplex하기가 무엇인지*
- 위의 것들은 모두 server socket의 역할
  - **데이터를 전달하지도 않고, 받지도 않고 그저 외부의 client소켓과 연결되는 서버에서의 client 소켓들을 생성할 뿐!**
  - server socket에 의해서 생성된 client socket
    - 각각의  `clientsocket`은 다른 client socket이 호스트와 포트에 맞춰서 `connect()`를 시행하는 것에 대한 response로 생성됨
- `clientsocket`을 만들자마자, 다른 connections를 listening 하기 위해서 바로 돌아감(루프)
- server측 `clientsocket`과 client측 `clientsocket`은 자유롭게 데이터를 주고 받을 수 있고, **동적으로 할당받은 포트를 사용하고 이 포트들은 재사용된다**

## 소켓의 사용

- start
  - 웹 브라우저의 `clientsocket`과 웹 서버의 `clientsocket`은 "peer to peer" 대화를 행함
  - **대화의 protocol을 정해야만 함**
    - 일반적으로는 request나 signon을 송신함과 함께 커뮤니케이션 시작. 이는 socket 자체의 룰은 아님
- communication
  - `send`, `recv`
    - *network buffers* 에서 동작
    - `send`, `recv`는 건네준 모든 바이트들을 반드시 다뤄야 하는 것은 아님
      - network buffers를 제어하는 것이 주 목표
    - 일반적으로, associated network buffers이 filled(`send`)될 때나 emtied(`recv`)일 때 반환함(네트워크 버퍼라는 터널이 꽉차면 보내고, 다 비워지면 받았다고 인식)
      - **`send`의 경우에는 얼마나 send할 지는 못정하고, `recv`가 얼마나 receive 했는지에 의존함. 즉 recv 쪽에서 받은 만큼만 sent할 수 있음**
    - 그리고 나서, 얼마나 많은 바이트를 다뤘는지 확인 시켜줌
    - 사용자가 직접 메시지가 완전히 다뤄질 때 까지 계속 호출해주어야 함
    - `recv`가 0 바이트를 반환하면 다른쪽이 connection을 close했다는 것을 의미
      - 더이상 해당 connection으로 데이터를 받을 수 없음
    - 예시
      - HTTP 프로토콜은 소켓을 오직 하나의 transfer로만 사용함
        - client는 request를 보내고 response를 읽음
        - 소켓은 버려짐
          - client는 0 byte를 수신함으로써, response의 끝을 탐지할 수 있음
  - 재사용
    - socket이 connection close하는 조건은, `send`, `recv`가 0 bytes를 반환하는 것
      - 따라서 connection이 close되지 않으면, `recv`를 계속 기다리게 될 것임
  - 소켓의 메시지
    - 클라이언트와 서버가 서로 고정 길이로 합의 or delimited or 크기가 얼마인지 알려주어야 함 or 연결을 종료하므로 써 끄거나
      - 이것을 정하는 것은 전적으로 프로토콜을 정의하는 사용자 마음
  - (참고)`read`, `write`
    - *file과 같은 느낌(JAVA)*
    - *`send`, `recv`와의 차이는?*
    - 소켓에 `flush`를 해야함
    - *이것들은 buffered된 file이라고 생각하면 됨*
      - 이 뭔소리?

소켓 통신의 예시

```py
class MySocket:
    """demonstration class only
      - coded for clarity, not efficiency
    """

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)
```

- 위의 코드의 발전
  - 타입 명시 방식
    - 메시지의 첫 캐릭터를 메시지 타입을 나타내도록 함
    - 각 타입은 고정된 길이를 갖는 것을 알고 있음
  - delimited route 방식
    - 임의의 chunk size를 받도록 함(4096, 8192가 네트워크 버퍼 사이즈로 보통 괜찮음)
    - 그리고 delimiter를 기반으로 수신받은 데이터를 스캐닝함
- 주의
  - One complication to be aware of: if your conversational protocol allows multiple messages to be sent back to back (without some kind of reply), and you pass recv an arbitrary chunk size, you may end up reading the start of a following message. You’ll need to put that aside and hold onto it, until it’s needed.
  - 메시지를 그것의 길이로 prefixing 하는것은 더 복잡하게 한다
    - 이유로는, 5글자 numeric character의 경우에는, 한번의 `recv`에서 모두 받을 수 없을 수도 있기 때문(high network loads에서)
    - `send`자체도 항상 한번에 다 보낼 수 없는 경우도 있음

## 소켓의 연결 끊기

- `shutdown()`
  - 데이터를 더이상 송신하지 않는다는 or listening하지 않는다는 명시적인 의사 전달 방식
  - One way to use shutdown effectively is in an HTTP-like exchange. The client sends a request and then does a shutdown(1). This tells the server “This client is done sending, but can still receive.” The server can detect “EOF” by a receive of 0 bytes. It can assume it has the complete request. The server sends a reply. If the send completes successfully then, indeed, the client was still receiving.
  - 일반적인 socket libraries에서는 명시적인 `shutdown`은 필요하지 않음
- 주의
  - python은 socket을 gc할 때, 자동적으로 `close`가 필요하면 해주는데, 이것에 의존하지 말고 명시적으로 `close`하는 것이 바람직하다

## 소켓이 죽을 경우

- blocking 소켓을 사용할 때 최악의 경우는, 반대편 소켓이 `close`없이 죽어버렸을 때 자신의 소켓은 계속해서 hang하는 경우
  - TCP는 reliable protocol이기 때문에, 오랜시간 hang하고 있음
- 스레드를 사용하는 경우라면, 해당 스레드는 완전히 죽은것과 다름 없음
  - 하지만 이러한 스레드를 kill 하면 프로세스 자체가 이상하게 될 수도 있음(자원 공유)

## Non-blocking Sockets

- blocking socket
  - **when you call recv() to read from a stream, control isn't returned to your program until at least one byte of data is read from the remote site.**
  - **The same is true for the write() API, the connect() API, etc. When you run them, the connection "blocks" until the operation is complete.**
- 파이썬
  - `socket.setblocking(0)`으로 non-blocking으로 만들 수 있음
- blocking socket과 가장 큰 메커니즘 적인 차이는, `send`, `recv`, `connect`, `accept`가 아무것도 하지 않은 채로 반환할 수 있다는 점
  - return code, error codes를 체크하는 것은 매우 힘듬

### `select`의 사용

select의 사용

```py
ready_to_read, ready_to_write, in_error = \
  select.select(
    potential_readers,
    potential_writers,
    potential_errs,
  )
```

- `select`
  - parameter
    - 읽으려고 하는 모든 소켓들의 리스트
    - 쓰려고 하는 모든 소켓들의 리스트
    - 에러를 체킹하는 것들
    - timeout
      - select 자체가 blocking이므로(1분정도 넉넉하게 주어주자)
  - return
    - readable, writable, error 전용의 socket들
    - 각각의 리스트는 parameter로 제공한 소켓들의 부분집합
    - 종류
      - readable
        - 그 소켓의 `recv`가 무엇인가를 반환할 확률이 매우 높다(?)
          - you can be as-close-to-certain-as-we-ever-get-in-this-business that a recv on that socket will return something.
        - `serversocket`이 들어가는 장소
      - writable
        - 임의의 적절히 건강한 소켓은 writable로 반환될 것임
        - 왜냐하면 writable로의 반환은 outbound network buffer space가 사용 가능하다는 뜻
      - error
  - blocking 소켓들에게도 편리한 기능 제공
    - block할지 말지 결정할 수 있는 방법을 제공
    - buffer에 무엇인가가 존재할 경우 readable을 반환
