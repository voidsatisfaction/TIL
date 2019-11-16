from typing import List

class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
    return self._bstFromPreorderRec(preorder, 0, len(preorder)-1)

  def _bstFromPreorderRec(self, preorder: List[int], parentNodeIndex: int, endIndex: int) -> TreeNode:
    if parentNodeIndex is None:
      return None
    treeNode = TreeNode(preorder[parentNodeIndex])

    left, right = self._getLeftRightChildNodeIndex(preorder, parentNodeIndex, endIndex)

    if left is None and right is None:
      treeNode.left = None
      treeNode.right = None
    elif left is None:
      treeNode.left = None
      treeNode.right = self._bstFromPreorderRec(preorder, right, endIndex)
    elif right is None:
      treeNode.left = self._bstFromPreorderRec(preorder, left, endIndex)
      treeNode.right = None
    else:
      treeNode.left = self._bstFromPreorderRec(preorder, left, right-1)
      treeNode.right = self._bstFromPreorderRec(preorder, right, endIndex)

    return treeNode

  def _getLeftRightChildNodeIndex(self, preorder: List[int], parentNodeIndex: int, endIndex: int) -> (int, int):
    left, right = None, None

    i = parentNodeIndex+1
    while i<=endIndex:
      if preorder[i] > preorder[parentNodeIndex]:
        right = i
        break

      if i == parentNodeIndex+1:
        left = i

      i += 1

    return left, right