# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def get_middle_node(left_node, right_node) -> ListNode:
            total_node_num = 1

            node = left_node
            while node is not right_node:
                total_node_num += 1
                node = node.next

            middle_node_num = int((total_node_num-1) / 2)

            middle_node = left_node
            while middle_node_num > 0:
                middle_node = middle_node.next
                middle_node_num -= 1

            return middle_node

        def merge_sorted_linked_list(linked_list_1: ListNode, linked_list_2: ListNode) -> ListNode:
            result_linked_list = ListNode()
            result_linked_list_last_node = result_linked_list

            while True:
                if linked_list_1 is None:
                    result_linked_list_last_node.next = linked_list_2
                    break
                elif linked_list_2 is None:
                    result_linked_list_last_node.next = linked_list_1
                    break
                else:
                    if linked_list_1.val <= linked_list_2.val:
                        result_linked_list_last_node.next = linked_list_1
                        linked_list_1 = linked_list_1.next
                    else:
                        result_linked_list_last_node.next = linked_list_2
                        linked_list_2 = linked_list_2.next

                    result_linked_list_last_node = result_linked_list_last_node.next


            return result_linked_list.next

        def sort_list_rec(left_node, right_node) -> ListNode:
            right_node.next = None

            if left_node is right_node:
                return left_node

            middle_node = get_middle_node(left_node, right_node)

            sorted_linked_list2 = sort_list_rec(middle_node.next, right_node)
            middle_node.next = None
            sorted_linked_list1 = sort_list_rec(left_node, middle_node)

            merged_sorted_linked_list = merge_sorted_linked_list(
                sorted_linked_list1,
                sorted_linked_list2
            )

            return merged_sorted_linked_list

        if head is None:
            return None

        right_node = head
        while right_node.next is not None:
            right_node = right_node.next

        return sort_list_rec(head, right_node)

class Solution(object):
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next
    
        tail.next = h1 or h2
        return dummy.next
    
    def sortList(self, head):
        if not head or not head.next:
            return head
    
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return self.merge(*map(self.sortList, (head, slow)))

if __name__ == '__main__':
    # linked_list = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    linked_list = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    result = Solution().sortList(linked_list)
    while result is not None:
        print(result.val)
        result = result.next