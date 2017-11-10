# ducks적용

## 참고

[Ducks official](https://github.com/erikras/ducks-modular-redux)

## ducks란?

ducks는 actionTypes와 actionCreator와 reducer를 따로따로 분리하지 말고 한 곳에 넣어 모듈화 시키고자 하는 방식이다.

원래 redux는 action types랴 actionCreator이랴 reducer등등 여기저기 흩어져있는 redux관련 정보나 함수들을 정신없이 찾아다녀야 하지만
ducks를 적용하면 파일 하나 하나에 actionCreator actionTypes reducer가 모두 들어있기 때문에 코드가 정말 알기 쉬워지고 actionTypes를 reducer랑 actionCreator에 동시에 적용할 수 있어서 개발하기 확실히 편해진다.

## ducks 장점

앞서 언급했듯이 흩어져있는 세가지 정보와 함수들을 하나로 모듈화 시키므로써 더욱 알기 쉽게 개발할 수 있게 된다.

## ducks 단점

`bindActionCreator`이라는 redux api를 사용할 경우(dispatch를 자동으로 실행하는 actions를 생성하는 api) 모든 ducks에 있는 actions를 `ducks/index.js`로 모을 경우에 문제가 발생한다.

action들을 import를 할 때 `*`를 사용해서 하는경우에는 reducer함수도 `*` 에 같이 딸려나오므로, actions에 `default`라는 네임스페이스가 리듀서함수에 의해서 차지되게 된다.

이는 혹시나 나중에 충돌을 일으킬 수 있으므로 이는 반드시 개선되어야 하는데 다음과 같은 세가지 방법이 있다고 판단한다.

1. 그냥 `bindActionCreator`를 사용하지 않는다.
2. `bindActionCreator`는 사용하되 `ducks/index.js`에서 actions를 `*`로 모으로 모은 오브젝트에서 reducer만 지워준다.
3. `bindActionCreator`는 사용하되 각각의 ducks파일에서 actions를 object로 한 번 더 묶어서 export해준다.

1같은 경우는 `bindActionCreator`를 사용하지 않는대신 클라이언트사이드에서 코드를 변경해야 하는 여지가 매우 크게 증가한다. 그래서 각하.

2와 같은 경우는 나중에 혹시 reducer와 actionCreator이외의 다른 것들을 export할때 하나하나 지워줘야 하므로 유지보수 코스트가 매우 크게 증가한다. 그래서 이것도 각하.

3은 일부의 클라이언트 코드와 일부의 ducks간의 코드만 변경해주면 되므로 가장 바람직하다고 생각했고 채택하였다. 그러나 언제나 `~actons.actionCreator`와 같은 형식으로 `actionCreator`를 사용해야 하므로 다소 귀찮은 점이 있다.

예

```js

import busy, { busyActions } from './busy';
import session, { sessionActions } from './session';
import me, { meActions } from './me';
import myprojects, { myprojectActions } from './myprojects';
import messages, { messageActions } from './messages';
import designs, { designActions } from './designs';

import { accountActions } from './accounts';
import * as routeActions from './route';

const rootReducer = {
  busy,
  session,
  me,
  myprojects,
  messages,
  designs,
};

export const actionCreators = Object.assign({},
  accountActions,
  sessionActions,
  busyActions,
  routeActions,
  meActions,
  myprojectActions,
  messageActions,
  designActions,
);

export default rootReducer;

```
