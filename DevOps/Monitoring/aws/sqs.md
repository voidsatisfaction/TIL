# SQS 지표

- 의문
- 개요

## 의문

## 개요

클라우드 워치의 모니터링 지표 예시(피크시)

![](./images/sqs/cloud_watch1.png)

클라우드 워치의 모니터링 지표 예시(NumberOfMessagesSent)

![](./images/sqs/cloud_watch2.png)

클라우드 워치의 모니터링 지표 예시(NumberOfMessagesReceived)

![](./images/sqs/cloud_watch3.png)

클라우드 워치의 모니터링 지표 예시(ApproximateNumberOfMessagesVisible)

![](./images/sqs/cloud_watch4.png)

클라우드 워치의 모니터링 지표 예시(ApproximateNumberOfMessagesDelayed)

![](./images/sqs/cloud_watch5.png)

- `ApproximateAgeOfOldestMessage`(초)
  - 개요
    - 대기열에서 가장 오래된 비삭제 메시지의 대략적인 사용 기간
      - 3회 이하로 수신한 두 번째로 오래된 메시지를 가리킴
  - 특징
    - 독약 메시지(여러 번 수신되었지만 삭제되지 않음)의 사용 기간은 포함되지 않음
    - 대기열에 리드라이브 정책이 있는 경우, 태스크 생성 ~ 데드레터 큐로 이동할때까지의 기간이 표시됨
    - 만약, 특정 task가 consume되지 않고 receive이후 표류하면, `ApproximateAgeOfOldestMessage`는 해당 태스크의 ack가 되기 전까지 계속해서 증가한다
- `ApproximateNumberOfMessagesDelayed`
  - 개요
    - 지연되어 즉시 읽을 수 없는 메시지의 수
  - 특징
    - 애초에 지연 큐로 구성되었을 경우에 발생
    - 혹은 지연 파라미터와 함께 전송되었을때 발생
- `ApproximateNumberOfMessagesNotVisible`
  - 개요
    - 이동중인 메시지의 수
  - 특징
    - 클라이언트에게 전송되었으나, 아직 consume되지 않았음
    - visibility window의 끝에 도달하지 않은 메시지
    - USE method에서 Utilization을 나타냄
- `ApproximateNumberOfMessagesVisible`
  - 개요
    - 대기열에서 가져올 수 있는 메시지의 수
  - 특징
    - USE method에서 Saturation을 나타냄
- `NumberOfEmptyReceives`
  - 개요
    - 메시지를 반환하지 않은 `ReceiveMessage API` 호출의 수
      - 기본적으로, sqs는 롱폴링을 하는데, 해당 폴링의 결과로 메시지를 받지 않은 경우의 수를 일컬음
      - sqs를 watching하는 worker가 많으면 많을수록 증가한다
- `NumberOfMessagesDeleted`
  - 개요
    - 큐에서 consume된 메시지의 개수
- `NumberOfMessagesReceived`
  - 개요
    - `ReceiveMessage`작업에 대한 호출로 반환된 메시지의 수
  - 특징
    - `NumberOfMessagesSent`보다 값이 클 수 있다(재시도로 인한)
    - 특정 기간동안의 sum값이므로(누적값이나 현재 상태에 대한 값이 아님), 예를들어 1분마다 하나의 태스크가 visibility timeout으로 인해서 계속해서 receive되는 경우에는, 1분당 sum값일 경우 계속해서 1을 나타낸다.
      - 이는 일반적이지 않음. 보통은 위의 경우에 0에서 잠깐 1로 올라갔다가 consume이 되므로 다시 0으로 될 것이다
- `NumberOfMessagesSent`
  - 개요
    - 큐에 추가된 메시지의 수
- `SentMessageSize`
  - 개요
    - 큐에 추가된 메시지의 크기
