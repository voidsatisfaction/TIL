from typing import List

class Solution:
  def sortColors(self, num: List[int]) -> List[int]:
    if len(num) == 0:
      return num

    a,b,c = (0,0,len(num)-1)
    while a <= c:
      if num[a] == 0:
        self._swap(num, a, b)
        a += 1
        b += 1
      elif num[a] == 1:
        a += 1
      else:
        self._swap(num, a, c)
        c -= 1

    return num

  def _swap(self, num, i, j) -> None:
    (num[i], num[j]) = (num[j], num[i])

print(Solution().sortColors([2,0,2,1,1,0]))
print(Solution().sortColors([2]))
print(Solution().sortColors([2, 1, 0]))