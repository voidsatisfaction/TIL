from typing import List

# Input: [2,2,1]
# Output: 1

# Input: [4,1,2,1,2]
# Output: 4

class Solution1:
  def singleNumber(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]

    start_index, end_index = 0, len(nums)-1

    while True:
      if start_index == end_index:
        return nums[start_index]

      pivot = nums[start_index]

      # partition
      i = start_index
      j = end_index
      k = start_index

      while i <= j:
        if nums[i] > pivot:
          self._swap(nums, i, j)
          j -= 1
        elif nums[i] == pivot:
          i += 1
        else:
          self._swap(nums, i, k)
          i += 1
          k += 1

      left_num = ((k-1)-(start_index-1))
      right_num = end_index-(k+1)

      if i-k == 1:
        return pivot
      elif left_num % 2 == 0:
        start_index = k+2
      else:
        end_index = k-1


  def _swap(self, nums: List[int], i, j) -> None:
    nums[i], nums[j] = nums[j], nums[i]

class Solution2:
  def singleNumber(self, nums: List[int]) -> int:
    result = 0
    for num in nums:
      result ^= num

    return result

print(Solution1().singleNumber([4,1,2,1,2]))
print(Solution1().singleNumber([2,2,1]))

print(Solution2().singleNumber([4,1,2,1,2]))
print(Solution2().singleNumber([2,2,1]))