# Inversion Of Control

## 참고

- [마틴파울러 InversionOfControl](https://martinfowler.com/bliki/InversionOfControl.html)

## 내용

```ruby
# 자신의 코드가 프로그램의 흐름을 제어하는 예시
puts 'What is your name?'
name = gets
process_name(name)
puts 'What is your quest?'
quest = gets
process_quest(quest)
```

- 자신의 코드가 프로그램의 흐름을 제어함
  - 자신이 언제 `process_name`과 `process_quest` 메서드를 호출하는지 제어함

```ruby
#
require 'tk'
root = TkRoot.new()
name_label = TkLabel.new() {text "What is Your Name?"}
name_label.pack
name = TkEntry.new(root).pack
name.bind("FocusOut") {process_name(name)}
quest_label = TkLabel.new() {text "What is Your Quest?"}
quest_label.pack
quest = TkEntry.new(root).pack
quest.bind("FocusOut") {process_quest(quest)}
Tk.mainloop()
```

- 프로그램 흐름의 제어권을 다른 시스템(프레임워크)에 넘김
  - 위의 예에서는 `Tk.mainloop` 명령어로 넘겨버림
  - 그리고 그 시스템에서 언제 나의 메서드를 호출할지 정함
  - 프로그램 흐름이 역전(여기서는 이양)됨
  - 시스템이 나를 호출하며, 내가 프레임워크를 호출하지 않음
  - **할리우드 원칙 "Don't call us, we'll call you"**

## 프레임워크의 특징

- 유저가 정의한 메서드를 유저의 애플리케이션 코드에서 실행하는것이 아니라, 프레임워크 자체 내부에서 실행함
- 그래서, 애플리케이션 활동을 순차적으로 조정하는 역할을 가짐
- 이로 인해서 프렝미웍은 확장가능한 골격으로서의 힘을 갖게 함

## 라이브러리 vs 프레임 워크

- 라이브러리
  - 라이브러리는 본질적으로 사용할 수 이 함수의 집합으로 이루어짐. 보통 클래스로 구조화 됨
  - 각각의 호출은 어떠한 일을 하고 클라이언트에게 흐름의 제어를 돌려줌
  - 그래서 사용자가 그것을 호출해서 프로그램의 흐름을 제어할 수 있음
- 프레임워크
  - 프레임워크는 보다 행위적인 빌트인 코드를 갖으며, 추상적인 디자인을 내포함
  - 프레임워크를 사용하기 위해서, 자신의 행위를 다양한 프레임워크의 장소에 넣어주어야 함
    - 내 자신의 클래스를 서브클래싱 / 플러깅 해서 사용
  - 그래서 프레임워크는 삽입된 코드를 프레임워크의 라이프사이클에 맞게 실행시켜줌

## 삽입된 코드를 호출하는 법

- 위의 루비 예시에서는 Lambda를 인자로 넘겨줌
  - 이벤트를 감지하면 클로저 안에 있는 코드를 실행시켜줌
- .NET의 예시
  - 프레임워크가 이벤트를 정의하고, 클라이언트 코드가 그 이벤트들을 구독함
  - delegate를 이용하여 메서드를 이벤트와 바인딩함
- EJB의 예시
  - Interface를 이용해서, 클라이언트가 프레임워크의 작동을 위해서 반드시 구현해야 하는 코드를 정해놓음
- template method의 예시
  - 수퍼 클래스가 프로그램의 제어의 흐름을 정의
  - 서브 클래스가 그 흐름의 확장을 위해서 메서드를 오버라이딩하거나 수퍼클래스가 정의한 추상 매서드의 구현을 행함
  - 내가 구현한 자동화폐 거래시스템에서 `ArbitrageExec.do()` 가 template메서드이고, 그것을 각 거래소 마다 다르게 구현하기 위한 `createBuyHistory()`, `createSellHistory()`, `createOrUpdateCycleHistory()`가 추상 메서드이며 / 서브클래스는 이를 구체적으로 구현하고 있다.

## 혼동의 여지

- IoC는 IoC를 하는 방법론(의존성 주입 DI)와 헷갈려하는 사람들이 많음
  - DI는 하나의 IoC를 구현하기 위한 일반적인 수단임
