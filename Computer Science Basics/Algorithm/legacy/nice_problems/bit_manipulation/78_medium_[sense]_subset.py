from typing import List

"""
Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).
"""

# mathematical solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]

        for num in nums:
            answer = answer + [ answer_element + [num] for answer_element in answer ]

        return answer

# dfs solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(index, path):
            answer.append(path)
            for i in range(index, len(nums)):
                dfs(i+1, path + [nums[i]])

        dfs(0, [])

        return answer

# bit manipulation
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        for i in range(1<<len(nums)):
            temp = []
            for j in range(len(nums)):
                if i & 1 << j:
                    temp.append(nums[j])
            answer.append(temp)
        
        return answer

if __name__ == '__main__':
    print(Solution().subsets([]))
    print(Solution().subsets([1]))
    print(Solution().subsets([1,2,3]))