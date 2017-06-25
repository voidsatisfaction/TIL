# Same Origin Policy

host, scheme, port가 다른 경우에 제한.

## 내용

html과 그 속의 iframe의 host, scheme, port가 같아야한다.

다르면, 해킹의 위험성 있음(e.g. iframe으로 다른 페이지를 보여주면서 ajax로 아이디 비밀번호를 해킹 서버로 보낸다던지)

이는 iframe안의 요소를 js로 조작할 수 있기 때문에 그렇다(일반 dom취급)
