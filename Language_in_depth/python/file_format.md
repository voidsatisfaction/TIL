# Python file format

## 개요

- `.py`
  - 정의
    - 일반적인 파이썬 스크립트 파일
- `.pyc`
  - 정의
    - compiled script
  - 구성
    - magic number
      - 4bytes
        - 2bytes는 유니크한 숫자
        - 2bytes는 `0d0a`
      - *이거 뭐하는 거임?*
      - marshalling code가 변하면 변하는 코드
        - **파이썬 버전마다 유니크한 코드**
    - modification timestamp
      - 4bytes
      - source file의 유닉스 수정 타임스탬프
        - 소스가 바뀌면 recompile하기 위함
    - code object
- `.pyo`
  - 정의
    - 파이썬 optimized pyc파일(Python3.5 이전에만)
      - Python 3.5부터는 pyc파일만 사용
- `.pyd`
  - 정의
    - C/C++ 헤더와 대응되는 Cython스크립트
- `.pyi`
  - 정의
    - Stub file
- `.pyz`
  - 정의
    - Python script archive
    - ZIP으로 압축된 Python script
- `.pywz`
  - 정의
    - MS-Windows를 위한 Python script archive
    - *왜 따로 있는 것일까?*

### 참고: pyi(Stub file)

*Python의 type checker는 무엇을 지칭하는 것인지?*

- 정의
  - type checker에 의해서만 사용되는 type hint를 포함하는 파일
    - runtime에는 사용되지 않음
- 사용 예시
  - Extension modules
  - Third-party modules인데, 타입 힌트가 적용되지 않은 경우
  - Standard library인데, 타입힌트가 작성되지 않은 경우
  - Python2와 3에서 compatible해야하는 모듈들
  - Modules that use annotations for other purposes
  - *뭔가 별로 안와닿음. 왜 필요한건지? 그냥 코드에다가 type hinting하면 안돼?*
    - 원작자는 type hint를 추가하고 싶지 않은데, 제3자가 type hint를 하고싶은 경우에 유효
- 특징
  - Python module과 같은 문법으로 작성
    - `@overload` 데코레이터
  - type checker
    - stub file에 있는 function signature만 check해야 함
      - function body는 `...`로 표현해둠
    - stub file이 발견되면, real module은 읽지 말아야 함
  - stub file이 실제 module file과 같은 디렉터리에 놓일 수 있도록 `.pyi` 확장자를 써야 함

### 참고: pyz(Python script archive)

- 정의
  - version 2.6이후에 python은 directory나 zip-format archive를 실행할 수 있게 되었음
  - zip파일이나 directory를 인터프리터의 첫번째 인자로 넣어서 실행시킬 경우, 인터프리터는 디렉터리를 `sys.path`에 추가하고, `__main__`모듈을 실행함
- 구조
  - `__main__.py`파일이 archive의 root directory에 존재해야 함
  - shebang support(OS)
    - `#!/usr/bin/env python3`
    - `# Python application packed with zipapp module (binary contents of archive)`
