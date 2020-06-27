from typing import List
from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Way1: priority queue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        if len(lists) == 1 and lists[0] is None:
            return None

        min_heap = []
        sorted_list = ListNode()
        last_node_of_sorted_list = sorted_list

        for i, top_node in enumerate(lists):
            if top_node is None:
                continue
            heappush(min_heap, (top_node.val, i))
            lists[i] = top_node.next

        while len(min_heap) > 0:
            val, index = heappop(min_heap)

            new_node = ListNode(val=val)
            last_node_of_sorted_list.next = new_node
            last_node_of_sorted_list = new_node

            if lists[index] is not None:
                next_node = lists[index]

                next_node_val = next_node.val
                heappush(min_heap, (next_node_val, index))

                lists[index] = next_node.next

        return sorted_list.next

# Way2: Merge with divide and conquer
class Solution:
    def _merge_two_lists(self, list1: List[ListNode], list2: List[ListNode]) -> List[ListNode]:
        head = point = ListNode(0)

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                point.next = list1
                point = point.next
                list1 = list1.next
            else:
                point.next = list2
                point = point.next
                list2 = list2.next

        if list1 is None and list2 is None:
            return None

        if list1 is None:
            point.next = list2
        else:
            point.next = list1

        return head.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        if len(lists) == 1 and lists[0] is None:
            return None

        lists_num = len(lists)
        interval = 1
        while interval < lists_num:
            for i in range(0, lists_num-interval, interval*2):
                lists[i] = self._merge_two_lists(lists[i], lists[i+interval])
            interval *= 2

        return lists[0]

        

if __name__ == '__main__':
    pass