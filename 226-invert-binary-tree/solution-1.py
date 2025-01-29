import os
import sys
from collections import deque
from typing import Optional

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from bft_binary_tree import TreeNode, BinaryTree

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        queue = deque([root])

        while len(queue) > 0:
            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return root


sol = Solution()
print(BinaryTree.to_array(sol.invertTree(BinaryTree.from_array([4,2,7,1,3,6,9]))) == [4,7,2,9,6,3,1])
print(BinaryTree.to_array(sol.invertTree(BinaryTree.from_array([2,1,3]))) == [2,3,1])
print(BinaryTree.to_array(sol.invertTree(BinaryTree.from_array([]))) == [])
print(BinaryTree.to_array(sol.invertTree(BinaryTree.from_array([1, 2]))) == [1, None, 2])
print(BinaryTree.to_array(sol.invertTree(BinaryTree.from_array([1, 2, None, 4]))) == [1,None,2,None,4])
print(BinaryTree.to_array(sol.invertTree(BinaryTree.from_array([1,None,2,None,4]))) == [1, 2, None, 4])