# Threading Multiprocessing Real World Problem

- 의문
- 웹 서비스 안에서 연산량이 엄청나게 많은 일을 조직적으로 처리하기
  - 주의사항

## 의문

## 웹 서비스 안에서 연산량이 엄청나게 많은 일을 조직적으로 처리하기

- 요구사항
  - 웹 서버위에서 동작해야 함
  - 여러 CPU / GPU를 사용하여 멀티 프로세싱 실현
  - 에러 핸들링이 잘 되어야 함
  - 도중에 동작이 멈춰서는 안됨
  - 실제 계산 프로세스 외에는 불필요한 오버헤드는 지양

해결하기 위한 코드

```py
import time
import queue
import multiprocessing
import threading

from custom_types import Status

def get_current_process_name():
    return multiprocessing.current_process().name

# Job은 ProcessJobManager에게 job을 등록할 때, 사용하는 job 클래스
class Job:
    def __init__(self, function, args=(), callback=None, callback_args=()):
        self.function = function
        self.callback = callback
        self.args = args
        self.callback_args = callback_args

# JobResult는 ProcessJobManger가 job을 수행하고 나서, job에서 등록한 callback으로 넘겨주는 job 결과에 대한 정보
class JobResult:
    def __init__(self, process_name: str, status: Status, data=None, traceback=None, duration=None):
        self.process_name = process_name
        self.status = status
        self.data = data
        self.duration = duration
        self.traceback = traceback

# ProcessJobManger가 특정 시점에 spawn한 process(task-runner)에 관한 정보
# callback 함수와 그 arguments를 함꼐 등록해서, process가 task를 다 끝냈을 때, 해당 process에 대응하는 callback을 실행할 수 있도록 함
class ProcessInfo:
    def __init__(self, process: multiprocessing.Process, callback=None, callback_args=()):
        self.process = process
        self.callback = callback
        self.callback_args = callback_args

# job 등록은 여러 스레드로부터 set_job을 통해서 thread-safe하게 받음(Queue.queue 이용)
# job 처리는, CPU or GPU bound problem을 해결하기 위해서, child process를 start해서 작업
class ProcessJobManager:
    def __init__(self, process_count=1, daemon=True):
        self._input_queue = queue.Queue()
        self._output_queue = multiprocessing.Queue()
        self._running_process_info = {} # pname, callback

        self._idle_process_count = process_count # 3개의 process를 사용(3코어)

        self._my_thread = threading.Thread(
            target=self._watch_and_process_forever,
            daemon=daemon
        )

    def watch_and_process_forever(self):
        self._my_thread.start()

    def set_job(self, job: Job):
        self._input_queue.put(job)

    def get_output_queue(self):
        return self._output_queue

    def _watch_and_process_forever(self):
        while True:
            if not self._input_queue.empty() and self._idle_process_count > 0:
                job = self._input_queue.get()
                self._delegate_job_to_process(job)

            if not self._output_queue.empty():
                job_result = self._output_queue.get()
                self._process_job_result(job_result)

            time.sleep(0.2)

    def _delegate_job_to_process(self, job: Job):
        # register pid on running_process_map
        # decrease idle_process_number
        p = multiprocessing.Process(
            target=job.function,
            args=job.args
        )

        pname = p.name
        self._running_process_info[pname] = ProcessInfo(
            p,
            callback=job.callback,
            callback_args=job.callback_args
        )

        self._idle_process_count -= 1

        p.start()

    def _process_job_result(self, job_result: JobResult):
        pname = job_result.process_name

        finished_process = self._running_process_info[pname].process
        callback = self._running_process_info[pname].callback
        callback_args = self._running_process_info[pname].callback_args

        finished_process.terminate()
        del self._running_process_info[pname]

        if callback is not None:
            callback(job_result, *callback_args)

        self._idle_process_count += 1

if __name__ == '__main__':
    from process_job_functions import DICOM, predict, after_predict

    job_manager = ProcessJobManager(process_count=3, daemon=True)
    job_manager.watch_and_process_forever()

    for i in range(10):
        job = Job(
            predict,
            args=(job_manager, DICOM(f'abcd{i}', 'meta data test')),
            callback=after_predict
        )
        job_manager.set_job(job)

    while True:
        pass
```

- 한계
  - Model이 소유하는 GPU 자원 역시 job manager가 직접 관리하던가, GPU 자원을 매니징 하는 오브젝트를 Dependency Injection 하는 방식으로 다뤄야 하는데, 이는 본래의 Job manager의 본분에 어긋남으로 어떻게 이 문제를 해결해야 할지 생각해봐야 함

### 주의 사항

1. Process communication을 할 때, thread를 인스턴스 변수로 갖는 class의 instance는 pickle화 되지 못함(그러한 인스턴스는 `multiprocessing.queue`에 원소로 put될 수 없음)
2. multi-processing을 실행시킬 때(`p.start()`), wrapper된 함수들은 pickle화 시킬 수 없다
