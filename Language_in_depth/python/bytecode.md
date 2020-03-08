# Python Bytecode

- 더 공부하기
- 의문
- 개요
  - python의 동작방식
  - Inside the Python virtual machine
  - Accessing and understanding Python bytecode

## 더 공부하기

- [Inside The Pyhotn Virtual Machine](https://leanpub.com/insidethepythonvirtualmachine/read#leanpub-auto-introduction)

## 의문

- 저렇게 여러가지 stack이 존재하는데, 그럼 coroutine은 어떻게 구현하는 원리인가?

## 개요

- `.py`,
- `.pyc`
  - `bytecode`

### python의 동작 방식

- 소스 코드를 virtual machine을 위한, bytecode(`.pyc`)로 컴파일
  - python interpreter는 virtual machine의 한 구현체

파이썬 코드와 컴파일된 pyc파일 예시

```py
def hello():
    print("Hello, World!")
```

```
2           0 LOAD_GLOBAL              0 (print)
            2 LOAD_CONST               1 ('Hello World!')
            4 CALL_FUNCTION            1
            6 POP_TOP
            8 LOAD_CONST               0 (None)
           10 RETURN_VALUE
```

### Inside the Python virtual machine

- CPython
  - 개요
    - stack-based virtual machine 사용
  - 사용하는 stack종류
    - **call stack**
      - 함수 call 하나를 frame이라는 개념으로 생각하여 frame을 push
    - **evaluation stack**
      - 각 frame에 대해서, python function의 실질적인 실행이 일어나는 stack
      - 이 스택에서 실질적인 계산이 일어남
    - **block stack**
      - 특정 타입의 control structure 타입을 계속 트래킹하기 위한 stack
        - `loops, try/except, with` 과 같은 entry point에 들어가면 push되고, 그러한 데이터 스트럭쳐에서 나올 때 pop됨
      - python이 현재 어느 블록이 활성화 되어있는지 임의의 시점에서 쉽게 알 수 있게 해줌
- 예시
  - `my_function(my_variable, 2)` 의 바이트 코드 생성
    - `LOAD_NAME`명령어가 `my_function`을 보고, evaluation stack에 push
    - `LOAD_NAME`명령어가 `my_variable`을 보고, evaluation stack에 push
    - `LOAD_CONST`명령어가 2를 보고, evaluation stack에 push
    - `CALL_FUNCTION` 명령어
      - 인자값인 `my_variable`, 2를 evaluation stack에서 pop하고, 실행할 함수를 pop함
      - call stack에 새 프레임을 할당
      - 로컬 변수를 배치
      - `my_function`의 바이트 코드를 실행
      - 실행이 끝나면 frame이 pop되고, 기존의 frame에서 반환된 `my_function`의 값을 evaluation stack에 push

### Accessing and understanding Python bytecode
def hello():
   def hello2():
           a = 1
           return a
   b = hello2()
   return b

- `dis.dis(function)` (disassemble)
  - 함수의 bytecode를 분석가능하게 출력해줌

```py
def hello():
    print("Hello, World!")

hello.__code__
# <code object hello at 0x104e46930, file "<stdin>", line 1>

hello.__code__.co_consts
# (None, 'Hello, World!')

hello.__code__.co_varnames
# ()

hello.__code__.co_names
# ('print',)
```

```
2           0 LOAD_GLOBAL              0 (print)
            2 LOAD_CONST               1 ('Hello World!')
            4 CALL_FUNCTION            1
            6 POP_TOP
            8 LOAD_CONST               0 (None)
           10 RETURN_VALUE
```

- `__code__`
  - 개요
    - code object에 접근
  - `co_consts`
    - 함수 body에서 생기는 literal의 튜플
  - `co_varnames`
    - 함수 body에서 사용되는 local 변수의 이름들의 튜플
  - `co_names`
    - 함수 body에서 참조되는 local에 해당하지 않는 이름들의 튜플

### Putting bytecode to use

- bytecode를 이해하는 것의 장점
  - ① 코드에 대해서 깊이 생각하는 것에 도움이 됨
  - ② 파이썬에서 몇가지 팁에 대한 답을 찾을 수 있음
    - `{}`가 `dict()`보다 빠른 이유?
      - `dis.dis("{}"), dis.dis("dict()")`를 해보자
  - ③ stack-oriented programming에 대해서 유용한 관점을 제공
