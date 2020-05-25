from typing import List
from queue import Queue

# Way1: Next array from starting point
class TemperatureData:
    def __init__(self, temperature_list):
        self.list = temperature_list
        self.index = 0

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        temperature_to_count = {}
        
        for i, t in enumerate(T):
            if t in temperature_to_count:
                temperature_to_count[t].list.append(i)
            else:
                temperature_to_count[t] = TemperatureData([i])

        answer = []

        for i, t in enumerate(T):
            min_index = 30000

            for t_2 in range(t+1, 101):
                if t_2 in temperature_to_count:
                    temp_index_list = temperature_to_count[t_2].list
                    temp_index_index = temperature_to_count[t_2].index

                    if len(temp_index_list) <= temp_index_index:
                        continue

                    min_index = min(min_index, temp_index_list[temp_index_index] - i)

            if min_index != 30000:
                answer.append(min_index)
            else:
                answer.append(0)

            temperature_to_count[t].index += 1

        return answer

# Way2: Next array from end point

# Way3: Stack from end point
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [ 0 for _ in range(len(T)) ]
        stack = []

        for i in range(len(T)-1, -1, -1):
            while len(stack) > 0 and T[i] >= T[stack[-1]]:
                stack.pop()

            if len(stack) > 0:
                answer[i] = stack[-1]-i
 
            stack.append(i)

        return answer

if __name__ == '__main__':
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
