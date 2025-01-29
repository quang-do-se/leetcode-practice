from typing import Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from complete_binary_tree import BinaryTree


class Solution:
    def maxDepth(self, root: Optional[BinaryTree]) -> int:
        # Recursion approach
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


sol = Solution()
print(sol.maxDepth(BinaryTree.from_array([3,9,20,None,None,15,7])) == 3)
print(sol.maxDepth(BinaryTree.from_array([1,None,2])) == 2)
print(sol.maxDepth(BinaryTree.from_array([])) == 0)
print(sol.maxDepth(BinaryTree.from_array([1])) == 1)