# Pyinstaller

- 의문
- 개요
  - Pyinstaller가 dependency를 찾는 과정
  - Building to One Folder
  - Building to One File
  - Using a Console Window
  - Source Code 숨기기
  - Understanding Pyinstaller Hooks
- 구체적 사용법
  - 옵션
  - Shortening the Command
  - Adding Files to the Bundle
  - Hidden import
  - Run-Time Information
  - Changing Runtime Behavior

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

### Understanding Pyinstaller Hooks

- hook
  - 개요
    - 특별한 니즈와 메서드를 적용하기 위한 pyinstaller extension
  - pysintaller에서의 hook 종류
    - runtime hook
    - analysis phase hook
      - 필요한 모듈 파일들을 찾는것 / 적당히 파일들을 배제하는데에 도움을 줌
      - 데이터 추가

analysis phase hook file 구조

```py
hiddenimports = [
    "dns.rdtypes.*",
    "dns.rdtypes.ANY.*"
]
```

analysis가 `import dns.rdate` or `from dns import rdata`를 보면, 이는 `hook-dns.rdata.py`를 호출하고, `hiddenimports` 값을 확인함.

그 결과 소스 프크립트 파일이 다음과 같은 코드를 포함한것 처럼 됨

```py
import dns.rdtypes.*
import dns.rdtypes.ANY.*
```

위와 같은 hidden imports가 프로젝트에서 필요할 경우, hook file(s)을 source file 근처에 두고, 그 위치를 `pyinstaller --additional-hooks-dir=... myscript.py` 와같이 지정해줘야 함

- 동작방식
  - anylsis가 import키워드를 감지
  - 대응하는 이름을 갖는 hook file을 찾음
  - 찾았으면, hook의 코드를 Python의 namespace로 편입
  - 편입과 동시에, 결과적으로 hook source code의 top level statements들이 실행됨
    - `import` / global names에 대한 할당 / 함수 정의 등
  - analysis가 위에서 실행된 코드로 인해 파생된 프로퍼티에 접근 가능
- Hook Global Variables
  - 대다수의 존재하는 hook은 다음의 global variables에 값을 할당하는 것으로 구성되어 있음
    - global variables에 hook을 할당하면, analysis는 번들이 생성되는데에 해당 값(훅)들을 적용함
  - 종류
    - `hiddenimports = ['_gdbm', 'socket', 'h5py.defs']`
      - 커맨드 라인에서 `--hidden-import`를 설정한 것과 같은 효과
      - hook된 모듈이 imported 될 때만 자동적으로 적용된다
    - `excludedimports = [modname_tkinter]`
      - hooked module 과 그 sub-module에서만 모듈을 사용하기 위해 지정할 수 있음
      - main scirpt에서 해당 모듈을 명시적으로 `import`하고 있지 않으면 번들에 해당 모듈을 포함시키지 않음
    - `datas = [ ('/usr/share/icons/education_*.png', 'icons') ]`
      - 앱과 번들하기위한 데이터
      - `(현재 데이터의 위치, 해당 데이터를 번들에 포함할때의 폴더 이름(위치는 sys._MEIPASS))`
      - 많은 디렉터리나 층이 복잡한 디렉터리의 경우
        - `datas = collet_data_files('submodule1')`
        - `datas += collet_data_files('submodule2')`
        - 와 같이 추가 가능
    - `binaries`
      - binaries로 앱과 함께 번들되는 파일이나 디렉터리
      - datas랑 같으나, dynamic library를 사용하는 지 pyinstaller가 확인하기 위해서 구별


## 구체적 사용법

`pyinstaller [options] script [script ...] | specfile`

- 바이너리화를 위한 스크립트를 여러개 지정할 수 있으나, output 바이너리를 실행할 경우 pyinstaller 커맨드에 스크립트가 적힌 순서대로 코드를 각각 실행한다.
- spec 파일을 수정한 후에 `pyinstaller myscript.spec`으로 실행할 수 있다

### 옵션

- 번들 생성
  - `--clean`
    - binary화 하기 전에 pyinstaller cache, temporary files를 지움
  - `--onefile, --onedir`
    - one-file 번들링일지, one-directory 번들링일지 정함
  - `--name`
    - 번들링할 앱과 스펙 파일의 이름을 정함
  - `--paths`
    - `import`할 파일의 위치를 탐색 (`PYTHONPATH`사용하는 것과 비슷한 느낌)
    - 스크립트 속에 `sys.path` 등을 써서 런타임에 패스를 조작해서 import하는 경우 추가해줄 필요가 있음
  - `--hidden-import`
    - *Name an import not visible in the code of the script(s).*
  - `--additional-hooks-dir`
    - 훅을 사용할 추가적인 path
  - `--runtime-hook`
    - custom runtime hook 파일의 경로를 지정
    - runtime hook은 런타임 환경의 특별한 기능을 세팅하기 위하여 다른 코드나 모듈이 실행되기 전에 실행되는, executable과 함께 번들링되는 코드
      - 윈도우즈 환경의 `multiprocessing` 모듈을 지원하기 위한 hook이 자동으로 들어가 있음
  - `--exclude-module`
    - 무시되는 파이썬 모듈을 설정 가능
- 디버깅
  - `--debug`
    - 부트로더가 번들링된 앱을 시작할 때, progress message를 보내도록 하여, missing imports를 찾는 것을 진단하는 데에 사용
- OS Specific
  - `--noconsole`
    - standard i/o 를 위한 console window를 제공하지 않음

### Shortening the Command

pyinstaller에는 다양한 옵션이 존재하여, 커맨드가 매우 길어지는 경우가 존재하며, 스크립트를 작성하면 편리함

예시 코드

```
// linux(sh)

pyinstaller --noconfirm --log-level=WARN \
  --onefile --nowindow \
  --hidden-import=secret1 \
  --hidden-import=secret2 \
  --upx-dir=/usr/local/share/ \
  myscript.spec

// Windows(BAT)
pyinstaller --noconfirm --log-level=WARN ^
  --onefile --nowindow ^
  --hidden-import=secret1 ^
  --hidden-import=secret2 ^
  --upx-dir=/usr/local/share/ ^
  myscript.spec
```

### Adding Files to the Bundle

- 번들에 파일을 추가하려면, 파일들의 리스트를 만들고, *`Analysis` call*(import 분석단계) 에 제공해야 함
- Single folder bundling의 경우
  - 추가된 파일이 executable과 함께 지정한 경로로(`--add-data=filename:.`) 폴더로 들어감
    - `:` 앞의 경로가 현재 옮기고 싶은 파일, `:` 뒤의 경로가 해당 파일을 옮길 위치(. 은 `sys._MEIPASS` (`app.exe`가 존재하는 장소))
- Single file bunding의 경우
  - 추가된 파일이 executable과 함께 지정한 경로로(`--add-data=filename:.`) 폴더로 들어감
    - `:` 앞의 경로가 현재 옮기고 싶은 파일, `:` 뒤의 경로가 해당 파일을 옮길 위치(. 은 `sys._MEIPASS` (`_MEIxxxx`가 존재하는 장소))
- runtime에 추가된 데이터 파일을 참조하기
  - pyinstaller로 번들된 앱의 경우, `sys._MEIPASS`가 존재

### Hidden import

- 번들링 후 실행하면 런타임에서 import 에러가 생기는 경우
- hidden import 문제
  - 번들링의 analysis phase에서 import가 보이지 않는 문제
- 원인
  - 코드가 다음과 같은 형태로 import기능을 사용하는 경우
    - `__import__`
    - `imp.find_module()`
    - `exec`
    - `eval`
  - Python/C API 를 사용해서 import하는 경우
- 해결 방법
  - build 할 때, 옵션으로 `--debug=imports` 플래그를 추가
  - 위에서 알아낸 정보를 바탕으로 `--hidden-import=` 커맨드 옵션 추가

### Run-Time Information

- bootloader가 `sys.frozen` 속성에 값을 설정하고, 번들 폴더의 상대 경로를 `sys._MEIPASS`에 설정
  - `sys._MEIPASS`
    - one-folder bundle의 경우: 해당 폴더가 존재하는 경로
    - one-file bundle의 경우: bootloader에 의해서 생성된 임시 폴더의 경로
  - `sys._MEIPASS`를 이용해서 번들링할 때 같이 지정한 data-file 등에 접근할 수 있음
- bootloader가 모듈의 `__file__` 속성을 번들 폴더에서 상대적으로 올바른 장소로 설정함
  - `mypackage.mymodule` 를 import할 경우의 `__file__ == sys._MEIPASS + 'mypackage/mymodule.pyc'`
- `sys.excutable`, `sys.argv[0]`
  - `sys.excutable`
    - 파이썬 인터프리터의 위치, 번들링을 했을 경우, bootloader의 위치
  - `sys.argv[0]`
    - 파이썬의 첫번째 arg(일반적으로 상대경로 인자), executable의 상대경로 인자
    - 심볼릭 링크를 사용하면, 해당 심볼릭 링크의 상대경로 인자(executable의 경로는 심볼릭 링크를 사용해도 변함없음)
  - main script
    - 메인스크립트 자체의 위치는 executable이 존재하는 곳의 위치와 같다

pyinstaller one-file로 아래 파일을 번들링 했을 경우 그 output

```py
import sys
import os
frozen = 'not'
if getattr(sys, 'frozen', False):
    # we are running in a bundle
    frozen = 'ever so'
    bundle_dir = sys._MEIPASS
else:
    # we are running in a normal Python environment
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
print('we are', frozen, 'frozen') # we are ever so frozen
print('bundle dir is', bundle_dir) # bundle dir is /var/folders/8d/1b5ql5dd6cvd33rj84bbp7kr0000gn/T/_MEIi0uKqf
print('sys.argv[0] is', sys.argv[0]) # ./dist/test (../dist 에서 실행)
print('sys.executable is', sys.executable) # /Users/yeongyumin/Desktop/private/pyinstaller/dist/test (파이썬 인터프리터의 위치)
print('os.getcwd is', os.getcwd()) # /Users/yeongyumin/Desktop/private/pyinstaller (현재 워킹 디렉터리 위치)
```

### Changing Runtime Behavior

- runtime hook의 사용
  - 개요
    - main script를 실행하기 전에 environment를 조작(decorator 같은 느낌)
      - 기존의 main script 코드를 수정하지 않고, environment를 조작
  - 사용 방법
    - ① `--runtime-hook=hook.py` 옵션을 사용
    - ② pyinstaller의 Analysis phase 후에, pyinstaller install 폴더에 있는 `loader/rthooks.dat` 파일(python dict형태)을 봐서 analysis phase에 탐지 되었던 모듈이 파일에 존재할 경우, 해당 모듈 이름과 같은 훅을 번들링할 앱의 hook으로 등록
      - 즉, pyinstaller팀이 미리 등록해둔 훅
  - 훅의 적용 순서
    - 유저가 지정한 커스텀 훅 -> `rthooks/rthooks.dat` -> 메인 스크립트
  - 응용
    - override functions / variables from some modules
      - 윈도우즈 환경의 `multiprocessing`의 경우
