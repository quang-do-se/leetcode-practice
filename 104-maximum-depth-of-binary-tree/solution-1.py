from typing import Optional
from collections import deque
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from tree_node import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative approach
        if root is None:
            return 0

        stack = deque()
        stack.append((root, 1))
        max_depth = 1

        while len(stack) > 0:
            node, current_depth = stack.popleft()
            max_depth = max(max_depth, current_depth)
            if node.left is not None:
                stack.append((node.left, current_depth + 1))
            if node.right is not None:
                stack.append((node.right, current_depth + 1))

        return max_depth


sol = Solution()
print(sol.maxDepth(TreeNode.generate_from_array([3,9,20,None,None,15,7])) == 3)
print(sol.maxDepth(TreeNode.generate_from_array([1,None,2])) == 2)
print(sol.maxDepth(TreeNode.generate_from_array([])) == 0)
print(sol.maxDepth(TreeNode.generate_from_array([1])) == 1)