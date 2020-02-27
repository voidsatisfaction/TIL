# Pyinstaller

- 의문
- 개요
  - Pyinstaller가 dependency를 찾는 과정
  - Building to One Folder
  - Building to One File
  - Using a Console Window
  - Source Code 숨기기

## 의문

## 개요

- 실행 파일 생성 과정
  - 사용자에 의해 작성된 파이썬 스크립트를 읽음
  - 코드를 분석 & 파이썬 스크립트를 실행하기 위한 다른 모든 모듈과 라이브러리를 발견
    - *`import` 키워드만 발견해주는 것인가? 어떻게 하고 있는것일까?*
  - 사용중인 python interpreter를 포함한 해당 파일들을 다 복사
  - 하나의 실행파일 or 폴더로 빌드
- 배포했을 때, 그 파일을 받은 사용자는 python 환경이 구축되지 않아도 실행 가능(어차피 인터프리터도 같이 bundling하니까)
- 명령어
  - `pyinstaller (--onefile 등의 옵션) myscript.py`

### Pyinstaller가 dependency를 찾는 과정

- dependency찾기
  - pyinstaller는 모든 `import` 문을 recursive하게 찾으면서 해당 타겟 프로그램이 사용하는 완전한 모듈의 리스트를 구성
    - *`egg` distribution* 역시 pyinstaller는 감지해서 자동적으로 세팅함
- **dependency를 못찾는 경우**
  - 원인
    - 변수와 `__import__()`함수를 사용하는 경우
    - `imp.find_module()`함수를 사용하는 경우
    - **`sys.path`를 이용해서 런타임에 패스를 조작하는 경우**
  - 해결책
    - pyinstaller command line으로 additional file을 추가해줌
    - pyinstaller command line으로 additional import path를 추가해줌
    - pyinstaller가 처음으로 작성하는 `myscript.spec`파일을 편집
      - `spec`파일에서는 Pyinstaller에게 코드 모듈을 알려줄 수 있음
    - hook파일을 작성해서 Pyinstaller에게 hidden imports를 알려줄 수 있음
      - *hook파일이 뭐지? spec파일과 무엇이 다르지?*
  - 특정 데이터 파일에 의존하는 경우에도 pyinstaller가 spec file을 보고 그것들을 포함하도록 할 수 있음
  - 런타임에 파일을 include하기 위해서는, bundle에서 실행하는 것과 관계없이 절대적으로 path를 나타낼 수 있도록 하는것이 중요함
  - pyinstaller는 어느 OS에나 마찬가지로 존재할 것으로 예상되는 라이브러리를 include하지 않음

### Building to One Folder

- one-folder mode
  - `myscript.py`에 pyinstaller 적용
  - `myscript`폴더 생성
    - 모든 dependencies를 갖고 있음
    - `myscript(.exe)`라는 실행 파일도 생성
  - `myscript`폴더를 `myscript.zip`으로 압축 후 배포
  - 압축 해제 후 `myscript`실행 파일 실행
- 장점
  - 디버깅하기 쉬움
    - pyinstaller가 어떤 파일들을 collect했는지 볼 수 있음
  - 기존에 compile한것과 완전히 같은 dependency를 갖은 상태로 코드만 수정하면, 오직 executable만 업데이트 됨
- 단점
    - 다른 모듈 파일이 너무 많음
- 동작 원리
  - 유저가 pyinstaller로 번들된 실행파일 실행
  - pyinstaller bootloader 실행
    - 플랫폼(Windows, GNU/Linux, OS X) 기반의 binary 실행 프로그램
  - bootloader가 `myscript`폴더 속에 있는 모든 imported modules를 찾을 수 있는 임시 python environment를 생성
  - bootloader가 스크립트를 실행하기 위한 파이썬 인터프리터의 복사본을 실행함

### Building to One File

- one-file mode
  - pyinstaller가 스크립트와 모든 dependencies를 하나의 `myscript`라는 바이너리로 번들링함
- 장점
  - 유저는 단순히 실행파일을 실행하기만 하면 됨
- 단점
  - README 파일과 같은 관련파일은 별도로 베포되어야 함
  - 초기 실행이 폴더 버전보다 조금 느림
- 참고
  - **one-file mode로 compile하기 전에 one-folder모드로 컴파일해서 잘 번들링 되는지 확인하라**
- 동작 원리(bootloader가 핵심)
  - 실행자의 os 환경에 맞춰서 temp-folder location에 temp folder를 생성(`_MEIxxxxx`와 같은 이름)
  - 하나의 실행파일은 압축된 non-Python support files(e.g `.so`파일)뿐 아니라, 스크립트에서 사용하는 모든 파이썬 모듈들의 embedded archive를 포함함
  - bootloader는 서포트파일들을 압축해제하고, temporary folder에 복사본을 작성
    - 시간이 one-folder 버전보다 더 오래 걸리는 이유
    - 현재 pyinstaller는 file attributes를 보존하지 않음
  - temporary folder를 생성한 뒤로는, bootloader는 one-folder bundle과 완전히 같은 방식으로 진행함
    - 임시 python environment 생성 하고, 파이썬 인터프리터를 실행함
  - *bundled code가 삭제될 때, bootloader는 temporary folder도 같이 삭제*
    - *이게 무슨 소리?*
  - 참고
    - `/tmp` 폴더는 반드시 execution 옵션으로 mount해야 함
    - `_MEIxxxx`폴더는 프로그램이 크래시 나거나 killed될 때, 같이 삭제되지 않음
    - `--runtime-tmpdir`커맨드라인 옵션을 사용하면, `_MEIxxxx`폴더의 위치를 정할 수 있음
    - one-file executable에 관리자권한을 부여하면 안됨
      - 공격자가 bootloader가 준비하는 동안 shared libraries를 오염시킬 수 있음
    - `os.setuid()`를 사용하는 애플리케이션의 경우 에러가 나타날 수 있으므로 주의

### Using a Console Window

- default로, bootloader는 command-line console을 만들어서 `print`, `input()`과 같은 스크립트 속의 명령을 수행해서 보여줄 수 있음
  - 옵션을 제공해서 보여주지 않을 수 있음

### Source Code 숨기기

- 번들링된 앱은 source code를 포함하지 않음
  - 하지만, pyinstaller는 컴파일된 파이썬 스크립트(`.pyc`파일들)를 번들링 하고, 이 파일들은 원칙적으로 decompiled될 수 있음
- 철저하게 소스 코드를 숨기는 방법
  - 몇몇 모듈을 `Cython`으로 컴파일하고 pyinstaller로 Cython C 오브젝트 모듈들을 참조하도록 하고 그것들을 번들링함
  - python 바이트코드는 pyinstaller command line에서 encryption key를 기반으로 AES256를 이용하여 혼란스럽게 만들 수 있음(물론, key를 extract해서 다시 original bytecode를 생성하는것은 매우 쉬움)
