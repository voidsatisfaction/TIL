# Python datetime 공략

- 목차
  - 자주 쓰는 datetime 오브젝트 모음
    - datetime
    - date
    - time
    - timedelta
  - timezone

## 자주 쓰는 datetime 메서드

### datetime

- 일시
  - 날짜와 시간

```py
import datetime

now = datetime.datetime.now()

print(now) # 2018-02-02 18:31:13.2713

print(now.year) # 2018

print(now.hour) # 18

now_str_iso = now.isoformat() # 2018-08-17T16:29:02.397588 보통은 db에 넣을때 많이 씀

now_str_custom = fromDatetime.strftime('%Y-%m-%d %H:%M:%S') # 사용자가 지정한 형식대로 datetime을 표현한 문자열이 생김

# datetime object -> date object
print(now.date()) # 2018-08-17
```

### date

- 날짜

```py
today = datetime.date.today()

print(today) # 2018-02-02

print(today.year) # 2018

print(today.month) # 2

print(today.day) # 2
```

### time

- 시간

```py
t = datetime.time(12, 15, 30, 2000)

print(t) # 12:15:30.002000

print(t.hour) # 12 minute second
```

### timedelta

- 시간차 / 경과시간
  - datetime 오브젝트를 `-`하면 `timedelta`오브젝트가 생성됨

```py
now = datetime.now()
now_before = datetime(2018, 5, 2)

td = now - now_before
print(td) # 107 days, 16:49:26.991962

print(td.days) # 107
print(td.seconds) # 60566
print(td.microseconds) # 991962

print(td.total_seconds) # 9305366.991962

datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

# timedelta를 이용해서 날짜 문자열 리스트 만들기
n = 5
from_datetime = datetime.datetime.now()

l = []
for i in range(n):
  l.append((from_datetime + datetime.timedelta(days=i)).strftime('%Y-%m-%d'))

print(l) # ['2018-08-17', '2018-08-18', '2018-08-19', '2018-08-20', '2018-08-21'] 오늘을 포함한 앞으로 5일간

# strptime은 문자열에서 datetime object로 변화시켜줌
date_str = '2018/2/1 12:30'
date_dt = datetime.datetime.strptime(date_str, '%Y/%m/%d %H:%M')
print(date_dt)
# 2018-02-01 12:30:00
```
