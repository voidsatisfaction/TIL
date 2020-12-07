# Detect cycle and its entrance on a linked list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Way1: hashmap
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited_node_map = {}

        node = head

        while True:
            if node is None:
                break

            if node in visited_node_map:
                break

            visited_node_map[node] = True

            node = node.next

        return node

# Way2: Two pointer
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None or head.next.next is None:
            return None

        pointer1, pointer2 = head.next, head.next.next
        intersection_point = None
        while True:
            if pointer2.next is None or pointer2.next.next is None:
                return None

            if pointer1 is pointer2:
                # If pointer1 and pointer2 intersect, it is cycle
                intersection_point = pointer1
                break

            pointer1 = pointer1.next
            pointer2 = pointer2.next.next

        # Make new pointer(pointer4) which starts from head node
        # From intersection point, and new pointer
        # If two pointer meets on same spot, it is starting point of cycle
        # (There is a mathemtatical proof)
        pointer3 = intersection_point

        pointer4 = head
        while True:
            if pointer3 is pointer4:
                return pointer3

            pointer3 = pointer3.next
            pointer4 = pointer4.next

        

        