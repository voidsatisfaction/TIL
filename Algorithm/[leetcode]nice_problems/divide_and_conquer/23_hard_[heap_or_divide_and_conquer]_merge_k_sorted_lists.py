from typing import List
import heapq

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

# use heap
class Solution:
  def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    minHeap = []
    for i, listNode in enumerate(lists):
      if listNode is None:
        continue
      heapq.heappush(minHeap, (listNode.val, i))

    answer = ListNode(None)
    answerTemp = answer

    while len(minHeap) > 0:
      minNode = heapq.heappop(minHeap)

      val, index = minNode

      answerTemp.next = ListNode(val)
      answerTemp = answerTemp.next

      if lists[index].next is not None:
        lists[index] = lists[index].next

        nextMinNode = lists[index]

        heapq.heappush(minHeap, (nextMinNode.val, index))

    return answer.next

# use devide & conquer
class Solution2:
  def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    interval = 1
    while interval <= len(lists):
      i = 0
      while i+interval <= len(lists)-1:
        lists[i] = self._merge(lists[i], lists[i+interval])
        i += 2*interval
      interval *= 2

    if len(lists) > 0 and lists[0]:
      return lists[0]
    else:
      return None

  def _merge(self, listNode1: ListNode, listNode2: ListNode) -> ListNode:
    resultNode = ListNode(None)
    tempNode = resultNode

    while listNode1 or listNode2:
      if listNode1 is None:
        tempNode.next = ListNode(listNode2.val)
        listNode2 = listNode2.next
      elif listNode2 is None:
        tempNode.next = ListNode(listNode1.val)
        listNode1 = listNode1.next
      else:
        if listNode1.val <= listNode2.val:
          tempNode.next = ListNode(listNode1.val)
          listNode1 = listNode1.next
        else:
          tempNode.next = ListNode(listNode2.val)
          listNode2 = listNode2.next
      
      tempNode = tempNode.next

    return resultNode.next

# Solution2().mergeKLists([ListNode(1)])