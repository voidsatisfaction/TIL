# Why use design pattern?

## PROS

### 1. Maintainability

모듈을 loosely coupled하게 관리할 수 있게 해준다. 그래서 리팩토링도 쉽게 할 수 있고, 다른 불필요한 모듈을 지울 수 있다. 대규모 팀 개발에서 매우 유용하다.

### 2. Communication

디자인 패턴은 objects의 서로다른 타입들을 다룰 수 있는 공통 언어적 성격을 갖는다. 그래서 추상화된 대화가 가능하게 한다.

### 3. Performance

몇몇 patterns들은 speed를 매우 개선해주고, 클라이언트가 실행해야 하는 코드의 양을 줄여준다(e.g. `flyweight`, `proxy`)

## CONS

### 1. Complexity

신참 프로그래머에게는 가혹한 코드의 난이도.

### 2. Performance

몇몇 패턴은 성능을 향상시키지만, 대부분의 패턴은 살짝 overhead를 준다. 그러므로 프로젝트에 따라서 이러한 overhead가 크게 다가올 수 있다.

**결국, 적재적소에 사용할 줄 아는 안목을 기르는 것이 가장 어렵고 중요하다고 할 수 있다.**
