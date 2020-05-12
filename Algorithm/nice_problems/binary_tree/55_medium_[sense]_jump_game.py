from typing import List

# timeout! O(n^2)
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         visited_index_set = set()
        
#         stack = [0]
#         while not len(stack) == 0:
#             index = stack.pop()

#             if index + nums[index] >= len(nums)-1:
#                 return True

#             for i in range(index, index + nums[index] + 1):
#                 if not i in visited_index_set:
#                     visited_index_set.add(i)
#                     stack.append(i)

#         return False

# O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_max_index = 0
        for index, num in enumerate(nums):
            max_index_candidate = index+num
            if index > current_max_index:
                return False
            
            if max_index_candidate >= len(nums)-1:
                return True

            if max_index_candidate > current_max_index:
                current_max_index = max_index_candidate

# O(nlogn)
class MaxSegmentTree:
    def __init__(self, array):
        self._n = len(array)
        self._array = array
        self._tree = [0] * (4*self._n)

        def init_rec(node, start, end) -> None:
            if start == end:
                self._tree[node] = self._array[start]
                return self._tree[node]

            self._tree[node] = max(
                init_rec(node*2, start, int((start+end)/2)),
                init_rec(node*2+1, int((start+end)/2)+1, end)
            )

            return self._tree[node]

        init_rec(1, 0, self._n-1)

    def get_max(self, left, right) -> int:
        def get_max_rec(left, right, node, start, end):
            if left > end or right < start:
                return 0
            if left <= start and right >= end:
                return self._tree[node]

            mid = int((start+end)/2)
            
            return max(
                get_max_rec(left, right, 2*node, start, mid),
                get_max_rec(left, right, 2*node+1, mid+1, end)
            )

        return get_max_rec(left, right, 1, 0, self._n-1)


    def update(self, index, value):
        def update_rec(index, value, node, start, end) -> int:
            if index < start or index > end:
                return self._tree[node]

            if start == end:
                self._tree[node] = value
                return self._tree[node]

            mid = int((start+end)/2)

            self._tree[node] = max(
                update_rec(index, value, 2*node, start, mid),
                update_rec(index, value, 2*node+1, mid+1, end)
            )
            return self._tree[node]

        update_rec(index, value, 1, 0, self._n-1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index_num_sum_list = [ i+num for i, num in enumerate(nums) ]

        mst = MaxSegmentTree(index_num_sum_list)
        current_max_index = 0
        while True:
            candidate_max_index = mst.get_max(0, current_max_index)
            if candidate_max_index >= len(nums)-1:
                return True
            
            if candidate_max_index == current_max_index:
                return False

            current_max_index = candidate_max_index

if __name__ == '__main__':
    print(Solution().canJump([2, 3, 1, 1, 4]))
    print(Solution().canJump([3, 2, 1, 0, 4]))
    print(Solution().canJump([0, 0]))
    print(Solution().canJump([0]))
    print(Solution().canJump([0,1,0,0,0,0,0,0,0,0,5,1]))