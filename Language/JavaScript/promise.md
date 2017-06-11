# Promise

아직은 아니지만 나중에 완료될 것으로 기대되는 표현

## Methods

### 1. Promise.all(iterable)

iterable내의 모든 프로미스가 통과되면 결정(resolve)

하나라도 거절되면 거절의 원인으로 프로미스 반환

### 2. Promise.race(iterable)

iterable내 프로미스중 하나라도 결정 or 거부되면 그 프로미스를 반환한다.
