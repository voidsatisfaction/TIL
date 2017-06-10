# Nodejs로 크롤링 하기

Nodejs를 이용한 크롤링 방식.

## 사용 가능한 툴

- 가상브라우저
  - phantom.js
  - nightmare(electron)
- http통신
  - default http / https
  - request
  - request-promise
- 파싱 툴
  - htmlparser2

## 분류 및 방법

이하는 케이스별 분류

|케이스|인증|내용|
|----|-----|----|
|1|X|http|
|2|O|http|
|3|X|https|
|4|세션(JSP)|https|

### 1. http + 비인증의 경우

가장 쉬운케이스이다.

가상브라우저로 파싱해도 되고, http리퀘스트로 파싱해도 된다.

### 2. http + 인증이 있는 경우

인증의 형태를 확인하고, http리퀘스트

### 3. https + 비인증의 경우

nodejs 내장 모듈인 https를 사용하거나, request, request-promise를 사용하면 https통신가능.

가상 브라우저를 사용하는 것도 효과적

### 4. https + 세션

1. 세션을 유지하기 위해 가상 브라우저를 띄워놓고(nightmare) 그 세션정보를 갖고 있는 https통신을 한다.

e.g. Book roll 의 경우 JAVA의 JSESSIONID를 갖고있음. 브라우저 연결이 끊기면 세션정보도 끊기므로 가상 브라우저를 띄우고 세션정보를 이용.

그런데 한번에 엄청나게 많은 https리퀘스트를 보내면 도중에 끊기는 경우(원인이 아직 잘 모르겠음)가 발생하므로, setTimeout함수에 난수를 걸어서 적절하게 request를 분배하는 것이 필요.

2. **Http Keep Alive사용??**

정확히 되는지 안되는지 잘 모르겠다.
