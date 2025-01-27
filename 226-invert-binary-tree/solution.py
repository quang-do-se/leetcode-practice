import os
import sys
from typing import Optional

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from tree_node import TreeNode

        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        old_left = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(old_left)
        return root
    

sol = Solution()
print(TreeNode.binary_tree_to_array(sol.invertTree(TreeNode.generate_from_array([4,2,7,1,3,6,9]))) == [4,7,2,9,6,3,1])
print(TreeNode.binary_tree_to_array(sol.invertTree(TreeNode.generate_from_array([2,1,3]))) == [2,3,1])
print(TreeNode.binary_tree_to_array(sol.invertTree(TreeNode.generate_from_array([]))) == [])
print(TreeNode.binary_tree_to_array(sol.invertTree(TreeNode.generate_from_array([1, 2]))) == [1, None, 2])
print(TreeNode.binary_tree_to_array(sol.invertTree(TreeNode.generate_from_array([1, 2, None, 4]))) == [1,None,2,None,None,None,4])
