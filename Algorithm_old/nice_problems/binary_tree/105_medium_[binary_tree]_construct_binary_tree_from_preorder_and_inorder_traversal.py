from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Way1: always recreate preorder and inorder list
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)

        if n == 0:
            return None

        root_val = preorder[0]

        if n == 1:
            return TreeNode(val=root_val)

        inorder_root_index = inorder.index(root_val)

        root_node = TreeNode(val=root_val)
        root_node.left = self.buildTree(
            preorder[1:inorder_root_index+1],
            inorder[:inorder_root_index]
        )
        root_node.right = self.buildTree(
            preorder[inorder_root_index+1:],
            inorder[inorder_root_index+1:]
        )

        return root_node

# Way2: refer preorder and inorder list index only not recreating lists itselves
# AND use inorder_val_to_index_map for O(1) inorder root val index search
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build_tree_rec(preorder_left, preorder_right, inorder_left, inorder_right) -> TreeNode:
            if preorder_left > preorder_right:
                return None

            root_val = preorder[preorder_left]

            if preorder_left == preorder_right:
                return TreeNode(val=root_val)

            root_node = TreeNode(val=root_val)

            # inorder_root_val_index = None
            # for i in range(inorder_left, inorder_right+1):
            #     if inorder[i] == root_val:
            #         inorder_root_val_index = i
            #         break
            inorder_root_val_index = inorder_val_to_index_map[root_val]

            root_node.left = build_tree_rec(
                preorder_left + 1,
                preorder_left + 1 + (inorder_root_val_index - inorder_left) - 1,
                inorder_left,
                inorder_root_val_index - 1
            )
            root_node.right = build_tree_rec(
                preorder_left + (inorder_root_val_index - inorder_left) + 1,
                preorder_right,
                inorder_root_val_index + 1,
                inorder_right
            )

            return root_node

        inorder_val_to_index_map = {}
        for index, inorder_val in enumerate(inorder):
            inorder_val_to_index_map[inorder_val] = index

        return build_tree_rec(0, len(preorder)-1, 0, len(inorder)-1)