from typing import List

class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

    return self._recBuildTree(inorder, postorder)

  def _recBuildTree(self, inorder, postorder) -> TreeNode:
    if not inorder or not postorder:
      return None

    left, right = 0, len(postorder)-1

    tn = TreeNode(postorder[right])

    inorderRightIndex = inorder.index(postorder[right])

    tn.left = self._recBuildTree(inorder[:inorderRightIndex], postorder[:inorderRightIndex])
    tn.right = self._recBuildTree(inorder[inorderRightIndex+1:], postorder[inorderRightIndex:right])

    return tn

Solution().buildTree([9,3,15,20,7], [9,15,7,20,3])

