# HTTP통신 vs Socket통신

가장 큰 차이는 접속을 유지하는가? 이다.

## HTTP통신

서버가 html로 만들어진 문서를 유저에게 전달하는 것을 목적으로 만들어진 프로토콜

TCP / UDP 사용.

80번 포트

클라이언트 서버 request response

단발성 접속.

## Socket통신

웹을 통해 클라이언트와 서버간의 신속하고 보안이 유지된 양방향 통신.

HTTP기반의 핸드셰이크.

교환이 성공하면 이전에 설정된 TCP연결을 이용하여 Application layer의 프로토콜이 HTTP에서 Web Socket으로 업그레이드.

서버나 클라이언트가 강제로 접속을 헤제하기 전까지 접속 유지.
