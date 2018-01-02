# Symbol tables: 심볼 테이블

Key-value pair abstraction

## 필요한 API

associative array abstraction

키로 인덱스를 구성하고 그것에 값을 대응시킨다.

- put(key Key, val Value)
- get(key Key) Value
- delete(key Key)
- contains(key Key) bool
- isEmpty() bool
- size() int
- keys() Iterable< Key >

## 특징

- Comparable 타입을 사용하면 편하다(키를 정렬하는 경우도 있음)
- 키는 immutable type을 이용한다.
- Frequency counter에 응용가능
  - 어떠한 단어가 하나의 파일에 몇 번 나타났는가?

## c.f 같음(Equality) 테스트

- Optimization for reference equality
- Check against null
- Check that two objects are of the same type and cast
- Compare each significant field:
  - if field is primitive type use `==`
  - if field is an object, use `equals()`: recursively
  - if field is an array, apply to each entry: recursively

## 간단한 심볼 테이블

링크드 리스트에 키-값 을 페어로 하는 데이터를 저장.

- 검색: 모든 키값을 보면서 같은 키를 찾음 `O(n)`
- 삽입: 모든 키값을 보면서 같은 키를 찾은 다음에, 같은 키가 없으면 가장 앞에 새로운 키-값을 추가. `O(n)`

## 정렬된 심볼 테이블

링크드 리스트에서 키를 기준으로 정렬함.

- 검색: 이진탐색을 이용하므로 `O(logn)`
- 삽입: 삽입하려면 삽입하려는 요소의 키보다 큰 심볼 테이블의 다른 요소들을 뒤로 밀어야 하므로 이는 `O(n)` -> 이곳이 문제!

### 사용 가능한 API

일반적인 심볼 테이블이 이용할 수 없는 유용한 API를 갖을 수 있다.

- min(): 가장 작은 키에 대응하는 값은?
- max()
- select(n): n번째 키에 대응하는 값은?
- ceiling(key Key) Key: key보다 큰 key들 중에서 이후의 가장 작은 key는?
- floor(key Key) Key: key보다 작은 key들 중에서 가장 큰 key는?

## 이진 탐색 트리 응용 심볼 테이블

[이진 탐색 트리 참고](../Tree/Binary_search_tree/README.md)

모든 API의 효율이 `O(h)`이며 여기서, h는 트리의 높이를 말한다(Iteration을 제외)

## 편향 레드블랙트리를 응용한 심볼 테이블

[편향 레드블랙트리 트리 참고](../Tree/Binary_search_tree/README.md)

모든 API의 효율이 `O(logn)`
