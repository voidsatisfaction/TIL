# Python

## 화이트 스페이스는 중요함

```python
listOfNumbers = [1, 2, 3, 4, 5, 6]

for number in listOfNumbers:
    print(number)
    if (number % 2 == 0):
        print("is even")
    else:
        print("is odd")

print ("all done")
```

## 모듈 불러오기

```python
import numpy as np

A = np.random.normal(30.0, 5.0, 10)
print (A)
```

## 리스트

- 가변

```python
x = [1, 2, 3, 4, 5, 6]
x[:4] # [1, 2, 3, 4]
x[3:] # [4, 5, 6]
x[-2:] # [5, 6]

x.extend([7, 8])
x # [1, 2, 3, 4, 5, 6, 7, 8]

x.append(9)
x # [1, 2, 3, 4, 5, 6, 7, 8, 9]

y = [10, 11, 12]
listOfLists = [x, y]

z = [3, 2, 1]
z.sort()
z # [1, 2, 3]

z.sort(reverse=True)
z # [3, 2, 1]
```

## 튜플

- 불변

```python
x = (1, 2, 3)
len(x) # 3

y = (4, 5, 6)
y[2] # 6

listOfTuples = [x, y]

(age, income) = "32, 120000".split(',')
age # 32
income # 120000
```

## 딕셔너리

```python
captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janeway"

print(captains["Voyager"]) # Janeway

print(captains.get("NX-01")) # None

for ship in captains: # key를 iterate
    print(ship + ": " + captains[ship])
```

## 함수

```python
def SquereIt(x):
    return x * x

print(SquereIt(2)) # 4

def DoSomething(f, x):
    return f(x)

print(DoSomething(SquereIt, 3)) # 9

print(DoSomething(lambda x: x * x * x, 3))
```

## 불린 식

```python
print(1 == 3) # False

print(True or False) # True

print(1 is 3) # False

if 1 is 3:
    print("How did that happen?")
elif 1 > 3:
    print("Yikes")
else:
    print("All is well with the world")
```

## Looping

```python
for x in range(10):
  print(x)

for x in range(10):
  if (x is 1):
      continue
  if (x > 5):
      break
  print(x)

x = 0
while (x < 10):
    print(x)
    x += 1
```
