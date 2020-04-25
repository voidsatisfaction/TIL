# Package distribution & Setuptools

## 의문

## 개요

- Package distribution
  - https://packaging.python.org/tutorials/packaging-projects/#uploading-your-project-to-pypi
    - 참조
- Setuptools 개요
  - `distutils`라는 파이썬 모듈 빌드와 설치를 지원하는 라이브러리의 확장 라이브러리
    - 다른 패키지에 의존성을 갖는 경우에도 지원

## 주요 기능

- Python Eggs
  - 임포트 가능한 싱글파일 배포 형식
- 소스 트리에 있는 모든 패키지를 자동 include
  - *해당 패키지가 import 해서 사용하는 의존 패키지들을 패키징 할 때, 자동으로 include 해준다는 건가?*
- 메인 파일의 개수에 맞춰서 `.exe`파일 생성 가능
  - 대신, local python 설치에 의존함(pyinstaller의 대체품이 아님)
- transparent cython support
- deploy developement mode
  - *`sys.path`에서 접근 가능하나, 소스 체크아웃으로부터 직접적으로 수정 가능*
  - *`pip install`한 뒤에, 소스 코드 수정해도 바로 적용된다는 것인지?*
