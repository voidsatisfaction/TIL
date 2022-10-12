# Binary Search

## 참고

## 정의

배열이 정렬되어있을 때, 반씩 잘라나가면서 값을 찾는 방식

## 예시

## 코드

```c++
// 그림을 한 번 그려보는 것을 추천.
// 1 2 3 4 5에서 5를 찾을때랑, 2를 찾을때를 해보세요. 또, 2.5를 찾을때랑 4.5를 찾을때
bool binarySearch(vector<int>* nums, int t)
{
  // 낮은쪽과 높은쪽을 정함
  int left = 0;
  int right = (*nums).size() - 1;
  while(left <= right)
  {
    int mid = (left + right) / 2;

    if((*nums)[mid] == t)
      return true;

    if((*nums)[mid] > t) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return false;
}
```
