# __main__

- 의문
- 개요
- 참고: `python -m 모듈이름`
- 문제

## 의문

## 개요

- 정의
  - 최상위 코드가 실행되는 스코프의 이름
- 특징
  - 모듈의 `__name__`은 표준 입력, 스크립트 또는 대화식 프롬프트에서 읽힐 때, '__main__'으로 설정됨

```py
if __name__ == '__main__':
  # 임포트 될 때에는 실행되지 않음
  # 스크립트로 실행되거나 python -m 으로 실행될 때 조건부로 동작하는 경우에 사용됨
  # 현재 디렉터리가 sys.path의 시작 부분에 추가됨?
```

## 참고: `python -m 모듈이름`

- 정의
  - 제공된 이름의 모듈을 `sys.path` 에서 검색하고 그 내용을 `__main__` 모듈로서 실행
- 특징
  - 현재 디렉터리가 `sys.path`의 시작 부분에 추가됨

## 문제

다음 코드는 `ModuleNotFoundError: No module named 'config.planmeca_config'; 'config' is not a package` 라는 에러를 내보냈었다.

```py
import multiprocessing

from waitress import serve

from app import initialize_app
from custom_types import ModelType

from config.abc_config import BaseConfig

if __name__ == "__main__":
    # This line is for pyinstaller one-file setting
    # https://github.com/pyinstaller/pyinstaller/wiki/Recipe-Multiprocessing
    multiprocessing.freeze_support()

    (app, model_worker_manager) = initialize_app(BaseConfig)

    model_worker_manager.register_model(0, ModelType.PANORAMA)

    model_worker_manager.initialize_models()
    model_worker_manager.watch_and_process_forever()

    serve(app, host='0.0.0.0', port=BaseConfig.APP_PORT)
```

- 원인
  - *??????????*
- 해결방법
  - 1 `from config.abc_config import BaseConfig` 코드 이전에 `sys.path.insert(0, config)`를 해줌
    - *근데 이미 해당 파일이 존재하는 디렉토리가 `sys.path`에 보면 추가되어있는데, 왜 이렇게 한다고 동작하는지 의문*
  - 2 `from config.abc_config import BaseConfig` 코드를 `if __name__ == '__main__'` 뒤에 배치
  - 3 `from config.abc_config import BaseConfig` 코드를 `from configs.abc_config ...`로 폴더명을 변경
