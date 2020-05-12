from typing import List
from functools import reduce

class Solution:
  def smallestRange(self, nums: List[int]):
      # revert sort each list inside list
      nums = [ numList[::-1] for numList in nums ]
      
      sorted_all_nums = []
      for numList in nums:
        for num in numList:
          sorted_all_nums.append(num)

      ansLeft, ansRight = -1e5, 1e5
      for left in sorted(list(set(sorted_all_nums))):
        right = -1e5

        for numList in nums:
          while len(numList)>0 and numList[-1]<left:
            numList.pop()

          if len(numList) == 0:
            return [ansLeft, ansRight]

          right = max(right, numList[-1])

        if right-left < ansRight-ansLeft:
          ansRight, ansLeft = right, left

      return [ansLeft, ansRight]


print(Solution().smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))
print(Solution().smallestRange([[4,10,15,24,26]]))