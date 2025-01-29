import os
import sys
from typing import Optional

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from bft_binary_tree import TreeNode, BinaryTree

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


sol = Solution()
print(BinaryTree.to_array(sol.invertTree(BinaryTree.from_array([4,2,7,1,3,6,9]))) == [4,7,2,9,6,3,1])
print(BinaryTree.to_array(sol.invertTree(BinaryTree.from_array([2,1,3]))) == [2,3,1])
print(BinaryTree.to_array(sol.invertTree(BinaryTree.from_array([]))) == [])
print(BinaryTree.to_array(sol.invertTree(BinaryTree.from_array([1, 2]))) == [1, None, 2])
print(BinaryTree.to_array(sol.invertTree(BinaryTree.from_array([1, 2, None, 4]))) == [1,None,2,None,4])
print(BinaryTree.to_array(sol.invertTree(BinaryTree.from_array([1,None,2,None,4]))) == [1, 2, None, 4])