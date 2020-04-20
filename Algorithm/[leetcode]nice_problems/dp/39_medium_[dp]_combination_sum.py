from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = []
        for i in range(target+1):
            dp.append([])

        candidates.sort()
        for n in range(1, target+1):
            combinations = []
            for candidate in candidates:
                val = n - candidate

                if val < 0:
                    break
                elif val == 0:
                    combinations.append([n])
                elif len(dp[val]) == 0:
                    continue
                else:
                    for combination in dp[val]:
                        if combination[-1] <= candidate:
                            combinations.append(combination + [candidate])

            dp[n] = combinations

        return dp[target]

if __name__ == '__main__':
    print(Solution().combinationSum([2,3,6,7], 7))
    print(Solution().combinationSum([2,3,5], 8))
    print(Solution().combinationSum([8,7,4,3], 11))