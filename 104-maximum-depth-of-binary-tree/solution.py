from typing import Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from tree_node import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursion approach
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


sol = Solution()
print(sol.maxDepth(TreeNode.generate_from_array([3,9,20,None,None,15,7])) == 3)
print(sol.maxDepth(TreeNode.generate_from_array([1,None,2])) == 2)
print(sol.maxDepth(TreeNode.generate_from_array([])) == 0)
print(sol.maxDepth(TreeNode.generate_from_array([1])) == 1)