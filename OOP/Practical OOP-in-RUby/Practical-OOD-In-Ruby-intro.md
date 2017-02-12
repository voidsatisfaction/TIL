# Practical Object-Oriented Design In Ruby

**현실 세계에서 얻는 지혜(절차형, 오브젝트지향)**

## Intro
- 객체 지향 디자인은 흑마술 같은 신비한 것이 아닌, 그냥 내가 모르는 것 일 뿐이니 너무 무서워 하지 말자.
- 현 상황을 최적화 시키는 것 보다, 앞으로 코드를 확장시켜나갈때를 위한 유지보수가 더 중요하다. **안정적 확장**

**OOD(Object Oriented Design)의 핵심**

- 객체와 디자인
  - Desining classes with *Single Responsibility*
  - *Dependencies* management
- 객체 사이의 인터페이스
  - Creating *Flexible Interfaces*
  - Reducing costs with *Duck typing*
  - Acquiring Behavior through *inheritance*
  - Sharing role behavior with *modules*
  - Combining objects with *composition*
- 테스트
  - Designing cost-effective tests

## Ch1 Object Oriented Design

- 디자인의 실전적 정의
  - 디자인은 코드 어레인지의 예술이다.
  - 현재의 퍼포먼스 향상 + 미래의 여지 두기(room for change) + 변화에 대한 비용절감

### 디자인의 도구들

*Principles* *Patterns*

- Principles
  - SOLID
    - Single Responsibility
    - Open-Closed
    - Liskov Substitution
    - Interface Segregation
    - Dependency Inversion
  - DRY
    - Don't Repeat Yourself
  - LoD
    - Law of Demeter
- Patterns
  - 실전적인 형식(커뮤니케이션)
  - Gof(Gang of Four)
  - 남용되는 경우가 있으므로 주의해야한다.

### OOP에 대한 간단한 설명

Objects + message (상호작용)
**Message가 Object보다 더 중요하다**

- Procedural Languages
  - 데이터와 행위의 분리
  - What you see is all you get

- Object-Oriented Languages
  - 데이터와 행위를 Object에 결합
  - Objects들은 서로의 행위를 메시지를 주고 받으면서(상호작용 하면서) 서로서로의 행위를 불러일으킨다(Objects들의 상호작용)
  - 같은 행위를 가진 Objects를 만들기 위해서 청사진과 같은 class(변수 + 메소드)를 정의한다.
  - 한 object가 많은 types를 갖을 수도 있다.
  - String Class(string instance를 생성하는 클래스)는 Class Class(클래스를 생성하는 클래스)의 인스턴스이다.

**이론보다 실전!!**
