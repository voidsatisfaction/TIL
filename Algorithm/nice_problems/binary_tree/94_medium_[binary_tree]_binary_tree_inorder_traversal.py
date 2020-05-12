from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []

        def inorder_traversal_rec(node: TreeNode) -> None:
            if node is None:
                return

            inorder_traversal_rec(node.left)
            answer.append(node.val)
            inorder_traversal_rec(node.right)

        inorder_traversal_rec(root)

        return answer

# Iterative solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []
        stack = []
        current_node = root

        while current_node is not None or len(stack) > 0:
            while current_node is not None:
                stack.append(current_node)
                current_node = current_node.left

            current_node = stack.pop()
            answer.append(current_node.val)
            current_node = current_node.right

        return answer

# Morris Traversal