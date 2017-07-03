# OAuth

## OAuth란?

## Github OAuth

[Github OAuth참조](https://developer.github.com/apps/building-integrations/setting-up-and-registering-oauth-apps/about-authorization-options-for-oauth-apps/)

[Github OAuth 단계별 처리](https://gist.github.com/iamssen/5402578)

### 1. Github OAuth의 적용 방법

1. [가장 먼저 어플리케이션을 Github에 Developer applications로 등록한다](https://github.com/settings/developers)
2. `get https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={http://...}`와 같은 형태로 어플리케이션 등록 정보를 바탕으로 앱 승인 주소로 날려보내면 클라이언트는 이 주소를 방문하므로써, 이 계정으로 계속하시겠습니까? 와같은 질문을 받는다. **여기서 주의해야하는 점은, scope에 대한 parameter가 정해지지 않으면 일반적으로 public repo의 열람만 가능하니까, scope=repo등과 같은 지정이 꼭 필요하다!!**
3. 2에서 승인하면 `https://cryptic-oasis-80377.herokuapp.com/?code=1870aae893b58cba036b`과 같은 형태로 code를 보내준다.
4. 그 코드를 이용하여 서버는 `post https://github.com/login/oauth/access_token`에 정보를 요청한다.
5. 정상적으로 요청이 처리되면 status 200으로 `{ access_token: ~~. token_type: ~~ }`와 같이 정보를 받을 수 있다.
6. 받은 token을 바탕으로 여러 API에 접근이 가능해진다.

### 2. 간편하게 Github API의 확인 방법

`curl -X DELETE -u voidsatisfaction:cc2f3ee9044083ec111a6527f853a89923c54c85 https://api.github.com/repos/facebook/react/subscription` 이와 같은 curl로 쉽게 API작동하는지 확인할 수 있다.
