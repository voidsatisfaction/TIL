# Node.js

- 의문
- 코드 분석

## 의문

- *왜 V8 엔진에 isolate라는 타입을 붙인거지?*
- *자바스크립트는 도대체 언제 어떤 코드에서 실행되는 것인가?*

## 코드 분석

- `node.cc`
  - `int Start(int argc, char* argv[]);`
    - 노드 실행하면 가장 먼저 실행되는 코드
    - `result.exit_code = main_instance.Run(env_info);`
- `node_main_instance.cc`
  - `int Run(const EnvSerializeInfo* env_info);`
  - `void Run(int* exit_code, Environment* env);`
    - environment를 load함
      - Libuv를 initialize함(event loop)
    - `*exit_code = SpinEventLoop(env).FromMaybe(1);`
- `embed_helpers.cc`
  - `Maybe<int> SpinEventLoop(Environment* env)`
    - `uv_run(env->event_loop(), UV_RUN_DEFAULT);`
      - libuv의 uv이벤트 루프를 실행
    - `platform->DrainTasks(isolate)`
      - 노드 플랫폼에서 *event loop에서 받아온 callback등을?* task를 실행
        - *이거 맞나*
- `node_platform.cc`
  - `void NodePlatform::DrainTasks(Isolate* isolate)`
    - `per_isolate->FlushForegroundTasksInternal()`
  - `bool PerIsolatePlatformData::FlushForegroundTasksInternal()`
    - `RunForegroundTask(std::move(task))`
      - foreground task들을 실행함
  - `void PerIsolatePlatformData::RunForegroundTask(std::unique_ptr<Task> task)`
    - current environment를 이용해서 task를 run함
    - `task->Run();`
      - 근데 v8로 코드를 실행하는건 어디에 나와있지?
