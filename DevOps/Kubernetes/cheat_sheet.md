# k8s 치트시트

- 의문
- 개요
  - k8s
  - helm

## 의문

## 개요

- 여기서 사용되는 `k`는, `kubectl`의 줄임말

### k8s

- 디플로이먼트 재시작
  - `k rollout restart deployment [deplyment_name]`
- 디플로이먼트 롤백
  - `k rollout history deployment/[deployment_name]`
  - `k rollout undo deployment/[deployment_name] --to-revision=?`
- 이벤트 시간순대로 보여주기
  - `k get events --sort-by='.metadata.creationTimestamp' -A`
- curl팟 생성하기
  - `kubectl run -it mycurlpod --image=curlimages/curl sh`

### helm

- 헬름 릴리스 버전 업그레이드
  - `helm upgrade --install [release] [chart] -f [value-file] --namespace ... --version ...`
- 헬름 릴리스 롤백
  - `helm history [release]`
  - `helm rollback [release] [revision]`