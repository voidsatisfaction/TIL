# Threading Multiprocessing Real World Problem

- 의문
- 웹 서비스 안에서 연산량이 엄청나게 많은 일을 조직적으로 처리하기

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
from queue import Queue
import multiprocessing
import threading
import random
import sys
import traceback

class DICOM:
    def __init__(self, binary_data, meta_data):
        self._binary_data = binary_data
        self._meta_data = meta_data

class JobManager:
    def __init__(self):
        self._input_queue = Queue()
        self._output_queue = multiprocessing.Queue()
        self._running_processes_map = {}
        self._idle_process_counts = 3 # 3개의 process를 사용(3코어)

    def watch_and_predict_forever(self):
        while True:
            if not self._input_queue.empty() and self._idle_process_counts > 0:
                job = self._input_queue.get()
                self._delegate_prediction(job)

            if not self._output_queue.empty():
                prediction_result = self._output_queue.get()
                self._process_prediction_result(prediction_result)

            time.sleep(0.1)

    def set_job(self, job):
        self._input_queue.put(job)

    def _process_prediction_result(self, prediction_result):
        self._idle_process_counts += 1
        print(prediction_result)

    def _delegate_prediction(self, job):
        # register pid on running_process_map
        # decrease idle_process_number
        p = multiprocessing.Process(
            target=self._predict,
            args=(job['dicom'],)
        )

        self._idle_process_counts -= 1
        print(p)

        p.start()


    def _predict(self, dicom):
        current_process = multiprocessing.current_process().name
        try:
            # To see how it handles error case
            print(f'predicting...{current_process}')
            random_num = random.random()
            if random_num > 0.8:
                raise Exception('Unexpected Error Occured!')

            # Some very very long operation..
            for _ in range(int(1e8)):
                continue
            print('prediction finished')

            # Return result to parent thread
            self._output_queue.put({ 'pid': current_process, 'result': 'FINISHED' })
            print('signal out')
        except:
            _, value, _ = sys.exc_info()
            print(value)
            traceback_string = traceback.format_exc()
            print(traceback_string)

            # Return error to parent thread
            self._output_queue.put({
                'pid': current_process,
                'result': 'ERRORED',
                'traceback': traceback_string
            })


if __name__ == '__main__':
    job_manager = JobManager()

    job_manager_thread = threading.Thread(
        target=job_manager.watch_and_predict_forever
    )

    job_manager_thread.start()

    for _ in range(10):
        job_manager.set_job({ 'dicom': DICOM(b'asdfmlwem', { 'name': 'hoho', 'age': 123 }) })

```
