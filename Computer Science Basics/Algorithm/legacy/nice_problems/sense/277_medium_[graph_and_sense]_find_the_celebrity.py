# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        if n <= 1:
            return -1

        candidate_node = 0
        for node in range(1, n):
            if knows(candidate_node, node) is True:
                candidate_node = node

        for node in range(0, n):
            if candidate_node == node:
                continue

            if not knows(node, candidate_node) or knows(candidate_node, node):
                return -1

        return candidate_node