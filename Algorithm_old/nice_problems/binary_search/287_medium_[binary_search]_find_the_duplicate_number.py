from typing import List

# Way1: binary search
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right, n = 1, max(nums), max(nums)

        while left <= right:
            mid = int((left+right)/2)

            num_of_mid = 0
            num_lower_than_mid = 0
            for num in nums:
                if num == mid:
                    num_of_mid += 1
                elif num < mid:
                    num_lower_than_mid += 1

            if num_of_mid > 1:
                return mid

            if num_lower_than_mid > mid-1:
                right = mid-1
            else:
                left = mid+1

# Way2: sort
# Way3: set
# Way4: ?!

if __name__ == '__main__':
    assert Solution().findDuplicate([1, 3, 4, 2, 2]) == 2
    assert Solution().findDuplicate([3, 1, 3, 4, 2]) == 3
    assert Solution().findDuplicate([1, 1]) == 1
    assert Solution().findDuplicate([1, 2, 2, 2, 2]) == 2