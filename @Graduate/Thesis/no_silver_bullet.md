# No silver bullet

## 서론

### 소프트웨어 개발

- 매우 복잡함
- 이제까지의 대처는 임시방편이 많았음

### 필자의 제안

- 이미 만들어진 소프트웨어가 있으면 새로 만들지말고 그것을 구입하라
- 소프트웨어의 요구사항을 만족하기 위해서 계속적이고 계획적으로 프로토타이핑을 하라
- 조직적으로 소프트웨어를 발전시켜라
  - 시스템에 더 많은 기능 추가
  - 사용
  - 테스트
- 차세대 설계자(designer)의 육성

## 본론

### 소프트웨어 공학의 비용 문제

- 소프트웨어 공학의 비용은 하드웨어 분야 에서처럼 쉽게 해결되지 않음
  - 여지껏 은탄환(silver bullet)은 없었음
    - 기술
    - 매니지먼트(관리)
    - 위 두 분야 어디에서도
  - 하지만 많은 혁신이 지금도 진행되고 있음
- 소프트웨어 공학의 문제와 그 본질을 생각할 필요가 있음
  - 비현실적인 이론에서 현실적인 이론으로

### 소프트웨어 공학의 본질적인 어려움

- 소프트웨어 공학의 진보가 느린 것이 아니라, 하드웨어 공학의 진보가 빠른 것임
- 소프트웨어 공학의 진보율을 알기 위해서는 소프트웨어 공학의 본질적인 어려움을 조사해야 함
  - 어려움의 종류
    - **본질적인 어려움**
    - 비 본질적인 어려움
  - 관념적인(conceptual) 구조의 명세, 설계, 테스팅이 본질적인 어려움. 단순히 작업하는 것은 비 본질적인 어려움임
  - 위의 명제가 참이면 은탄환은 존재하지 않는 것임

### 현대 소프트웨어 공학의 본질

#### 1. 복잡성(Complexity)

- 어떠한 다른 인간의 산물보다도 규모에 비해서 매우 복잡한 존재
- 다른 인간의 산물은 중복되는 구조가 존재
- 컴퓨터는 많은 상태(state)를 지닌 매우 복잡한 인간의 산물이나, 소프트웨어는 그보다도 더 많은 상태를 갖음
- 소프트웨어는 중복되는 로직은 하나의 서브루틴으로 합치므로 모든 로직이 다 다름
- 단순히 소프트웨어의 스케일업은 반복되는 같은 요소를 늘리는것이 아니라, 다른 **새로운 요소** 를 늘리는행위임(비 선형적인 복잡도 증가)
- 소프트웨어의 복잡성은 본질적인 성질이나, 이에 대한 기술(description)은 추상화됨
- 소프트웨어 제품 개발의 전형적인 문제들은 대개 본질적으로 규모에 비해 비선형적인 복잡도의 증가를 가져온다는 점
  - 이는 팀원끼리의 의사소통의 문제를 야기
    - 상태들에 대한 파악 힘듬
    - enumerating이 힘듬
  - 개발 코스트 증가
  - 사용하기 힘든 소프트웨어
  - 기능 추가 어려워짐
  - 상태들을 시각적으로 파악하기 힘듬

관찰에서 모델 예측
모델 예측에서 특징량 추정
특징량을 실험을 통해서 확인

복잡도가 본질에 포함되지 않아서 가능한 모델

#### 2. 호환성(Conformity)

- 물리학은 통일장이론을 찾으려고 노력함
- 소프트웨어 공학은 그러한 이론은 존재하지 않음
  - 소프트웨어 공학의 복잡성은 신이 아닌, 각각의 소프트웨어가 그저 다른 사람에 의해서 설계되었기 때문에 발생
  - 다른 인터페이스에 호환하게 하려면 자연스럽게 그 작용이 복잡성을 야기함

#### 3. 변동성(Changeability)

- 소프트웨어 제품은 변화의 압박에 지속적으로 시달림
  - 기존의 다른 인간의 산물은 만들어진 것을 변경하기 보다는, 대체함. 대체하는 주기도 매우 김
  - 부분적으로 소프트웨어는 다른 산물 보다 더 변경하기 쉬움. 그저 하나의 생각이기 떄문
- 성공적인 소프트웨어 역시 변함
  - 원래의 도메인에서 다른 도메인으로 확장 하기 때문(유저로부터의 요구)
  - 좋은 소프트웨어는 수명이 기므로 **다른 하드웨어와의 호환** 을 맞추기 위해서 변화
- 소프트웨어 제품은 문화적 맥락, 유저, 법, 하드웨어에 영향을 받음
  - 이들이 변하면 소프트웨어도 변화해야만 함

#### 4. 비가시성(Invisibility)

- 소프트웨어는 비가시적이고, 가시화 할 수 없음
  - 애초에 한 장소 안에서 구현되지 않음
  - 소프트웨어의 구조는 하나의 다이어그램으로 표현이 불가능
    - 제어의 흐름
    - 데이터 흐름
    - 의존성 패턴
    - 시간 흐름
    - 네임스페이스 관계
    - 위의 것들은 평면적이지도, 계층적이지도 않음
  - 사람고 사람이 커뮤니케이션 하는것을 힘들게 함

### 과거의 비 본질적인(accidental) 어려움을 해결한 혁신의 사례

#### 1. 고 수준의 언어

- 소프트웨어의 생산성과 의존가능성과 간단함을 가장 강력하게 개선한 방법
- 비 본질적인 복잡성의 개선
  - 저 수준의 제어에 대해서 추상화
    - 프로그래머가 신경쓸 필요가 없음
  - 추상화된 프로그램을 만들 때 필요한 모든 블럭을 제공

#### 2. 시간 분할 방식(Time-sharing)

- 즉각적인 프로그램의 결과를 볼 수 있게 함
- 프로그램의 개관 이해에 큰 도움
- 계속해서 집중해서 개발할 수 있게 도와줌
- 인간이 지각할 수 있는 100 밀리초 보다 빠른 응답속도는 의미가 없을 것

#### 3. 프로그래밍 환경의 통일화

- Unix와 Interlisp와 같은 최초의 통일된 프로그래밍 환경이 소프트웨어 개발의 생산성을 크게 높여주었음
- 다양한 사람들과 함께 프로그래밍을 할 경우에 예상되는 문제들을 해결

### 은탄환에 대한 희망

앞으로의 은탄환은 어떠한 본질적인 문제를 다루어야 하며, 어떠한 식으로 발전해야 하는가?

- Ada와 다른 고수준 언어의 진보
  - 언어의 사상이 소프트웨어의 현대적인 디자인, 모듈화, 추상 데이터 타입, 계층적 구조화를 도와줌
  - 하지만 은탄환은 될 수없음
- 객체 지향 프로그래밍
  - 추상 데이터 타입, 구조적 데이터 타입인 클래스를 이용한 강한 추상화
    - 그러한 추상화된 데이터 타입의 컨셉은, **객체의 타입은 객체에 알맞은 값의 집합과 연산(operation)의 집합으로 정의되어야만 한다는 것**
      - 저장 장소의 모양은 숨겨져야만 함
      - e.g `private`타입
  - 인터페이스
  - **은폐없는 계층**, **계층 없는 은폐**
  - 설계자가 소프트웨어의 **설계를 표현** 하는데에 큰 도움을 줌
  - 객체 지향 프로그래밍의 한계
    - 아직 **본질적인 소프트웨어 설계 자체의 복잡성** 이라는 문제는 해결해주지 못함
- 인공지능
  - AI의 정의의 혼란
    - AI1: 기존에는 인간의 지성에 의해서 해결될 수 있는 문제들을 컴퓨터가 해결하는 것. 문제가 한 번 해결되면 더이상 AI라고 불리지 않음
    - AI2: 규칙 기반, 휴리스틱 프로그래밍에 속하는 기술들의 집합을 사용하는 것. 인간이 어떠한 문제를 해결하는 방식처럼 프로그램이 그 문제를 해결하도록 하는 것
    - 애초에 문제 기반의 기술이기 때문에 무엇이 새로운 것인지 알기 애매함
  - 전문가 시스템(Expert systems)
    - 1980년대 당시 가장 발달된 AI기술
    - 많은 양의 데이터를 넣어서 규칙 기반의 추론을 통하여 결론과 조언을 도출하는 프로그램. 결과 뿐 아니라 어떠한 논리로 그러한 결과가 도출되었는지 사용자에게 제시
    - 추론 엔진은 많은 적용이 가능하므로 기존의 알고리즘 기반의 문제해결과는 차별화
    - 애플리케이션 복잡성과 프로그램 그 자체를 분리한 것에 중요한 포인트가 있음
- 자동화 프로그래밍
  - 문제의 명세(specification)로부터 문제를 해결해줄 수 있는 프로그램을 생성하는 프로그램
  - 고수준의 언어로 프로그래밍을 행하는 것의 다른 말
    - 이는 해결책의 하나의 방식이지, 문제의 해결방법이 아님
  - 비교적 적은 매개변수가 존재하고, 이미 해결방법이 존재하는 문제에 대해서는 적용가능
  - 일반적인 보다 넓은 세계에서, 특히 일반적인 소프트웨어 시스템에 적용하는것은 불가능
- 그래픽 프로그래밍
  - 컴퓨터 그래픽을 소프트웨어 설계에 응용
  - 이미 언급했듯이, 흐름 차트(flow chart)는 소프트웨어 구조를 추상화하는 좋지 못한 추상화
  - 애초에 소프트웨어는 가시화 시키기 매우 어려움
    - 너무나도 다양한 추상화가 되어있기 때문
    - 하드웨어칩(VLSI)는 2차원 레이어의 추상화일 뿐
- 프로그램 증명(verification)
  - 시스템 설계 단계에서 에러들을 제거할 수 있는 은탄환이 있는가?
  - 생산성 / 의존가능성이 극적으로 증가할 수 있는가?
  - 증명에 사용되는 수학적 증명이 잘못되어있을 수 있음
    - 노동의 감소에는 영향을 미침
  - 프로그램 증명의 명세에 맞춘 프로그램만 프로그램 증명 검사를 행할 수 있음
- 프로그래밍 환경과 툴
  - 버그 잡아주기
  - 프로그래머가 기억해야만 하는 데이터를 저장하는 데이터베이스
- 워크 스테이션
  - 많은 일들을 해줄것이지만 은탄환은 아님

## 유망한 은탄환 후보의 관념적 본질

- 많은 소프트웨어의 복잡성을 다루는 기술 / 관리가 나오고 있고 지속적인 개선이 이루어지고 있음
- 생산성 공식: `소프웨어 생산량 = 시그마(빈도 x 시간)`
- 위의 기본적인 공식에 준거하여 본질적인 해결책을 생각해 봄

### 1. 만들기 보다는 사라

- 소프트웨어는 복제하는데에 비용이 들지 않음 대부분의 비용은 개발 비용
- 소프트웨어 시장의 애플리케이션 비용 자체도 저렴함(1980년 당시)

### 2. 요구 사항 상세화와 빠른 프로토타이핑

- 소프트웨어 시스템을 만드는데에 힘든 부분은 **정확히 무엇을 만들까** 라는 질문에 대답을 명확히 하는 것
- **클라이언트는 자신이 정확히 무엇을 원하는지 모름**
  - 애초에 반드시 구체화 되어야하는 문제들에 대해서 별로 생각해본 적이 없음
  - 몇번씩 자기자신이 직접 현대 소프트웨어 제품을 직접 만들어보지 않으면 자신이 주문하는 소프트웨어의 명세를 정확히 알지 못하고 전달하지 못함
- 그렇기 때문에 **요구사항을 반복적으로 빠르게 포로토타이핑** 하는 소프트웨어 시스템 / 관리가 소프트웨어 공학의 본질적인 문제를 해결하기 위한 하나의 방법이 될 수 있음
  - e.g) agile, kanban, loosely coupled 아키텍처, 오픈소스, ci툴, 테스트

### 3. 점진적 개발 - 단순한 쌓아올림(build)이 아닌 성장

- 이제까지 쌓아올림(build)이라고 생각했던 소프트웨어 제품 생성을 다른 관점에서 보아야 함
  - 세상은 너무 빠르게 변하고, 소프트웨어는 항상 변화해야 함
  - 애초에 잘못 개발될 확률이 매우 높음
- **소프트웨어는 단순히 죽은 인간의 산물이 아니라, 살아있는 생물과 같음**
  - 매우 다양하고, 자기 방어적이고, 자기 갱신적인 뇌의 상호작용
  - 그러므로, 프로그램은 쌓아올림이 아니라 **성장** 하는 것임
- 소프트웨어는 성장하듯이, 점진적으로 개발해야 함
  - 처음에는 하나의 기능만 어느정도 수행하게
  - 그 다음부터 하나하나 담금질을 해나감(필요한 기능 추가, 모듈 분리 등등..)
  - 프로토 타이핑을 쉽게 해줌
  - 동작하는 시스템을 항상 체험하므로, 개발자의 열정도 상승
  - 생산성에서 큰 차이를 보임

### 4. 좋은 설계자

- 좋은 설계 관습은 배울 수 있음
- 좋은 설계는 좋은 설계자로부터 나옴
  - 보다 빠르고, 작고, 간단하고, 깨끗하고, 적은 노력으로 생산가능한 제품 구조를 만들 수 있음
- 좋은 설계자를 양성하자
  - 좋은 설계자는 매우매우 드물게 존재
  - 그들은 반드시 좋은 대우를 받아야 함
- 좋은 설계자를 양성하는 방법
  - 시스템적으로 가능한 빨리 최고 설계자를 찾아내자. 가끔은 경험이 적어도 매우 큰 자질을 갖고 있는 경우도 있음
  - 설계자 후보에게 커리어 멘토를 붙여주고, 커리어 관리를 해줌
  - 설계자 후보를 어떻게 육성시킬것인지 구체적인 계획을 세우고 실천함. 리더쉽도 키워줘야 함
  - 설계자들이 서로 소통하며 자극할 수 있는 기회를 제공해야함
