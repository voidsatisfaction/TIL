from typing import List

class Solution:
  def splitArray(self, nums: List[int]) -> bool:
    if len(nums) < 7:
      return False

    sums, s = [], 0
    for num in nums:
      s += num
      sums.append(s)

    for i in range(1, len(nums)):
      if i > 1 and nums[i-1] == 0 and nums[i] == 0:
        continue
      if self._dfs(i+1, 1, sums[i-1], nums, sums):
        return True
    return False

  def _dfs(self, start: int, depth: int, targetSum: int, nums: List[int], sums: List[int]) -> bool:
    if start > len(nums)-1:
      return False

    if depth == 3:
      if sums[len(nums)-1]-sums[start-1] == targetSum:
        return True
      return False

    result, isConsecutiveZero = False, False
    for j in range(start+1, len(nums)-1):
      if nums[j] == 0:
        if not isConsecutiveZero:
          isConsecutiveZero = True
        else:
          continue
      if isConsecutiveZero:
        isConsecutiveZero = False
      if sums[j-1] - sums[start-1] == targetSum:
        result |= self._dfs(j+1, depth+1, targetSum, nums, sums)

    return result

print(Solution().splitArray([1,2,1,2,1,2,1,0,-1,1]))
print(Solution().splitArray([1,2,3,4,6,6,-6,6,6,10,0,2,2,2]))
