from typing import List

# Way1: dp with dfs (typical 1/0 knapsack)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def dfs(index, current_sum, dp) -> int:
            state = (index, current_sum)
            if state in dp:
                return dp[state]

            if index == len(nums):
                if current_sum == S:
                    dp[state] = 1
                else:
                    dp[state] = 0

                return dp[state]
            
            num = nums[index]
            dp[state] = dfs(index+1, current_sum+num, dp) \
                + dfs(index+1, current_sum-num, dp)

            return dp[state]

        if len(nums) == 0:
            return 0

        dp = {}

        return dfs(0, 0, dp)
