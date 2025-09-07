from typing import List, Optional

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from bft_binary_tree import TreeNode, BinaryTree

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        if root.left:
            res += self.inorderTraversal(root.left)
        
        res.append(root.val)

        if root.right:
            res += self.inorderTraversal(root.right) 

        return res
    

sol = Solution()
# BinaryTree.visualize(BinaryTree.from_array([1,None,2,3]))

print(sol.inorderTraversal(BinaryTree.from_array([])) == [])
print(sol.inorderTraversal(BinaryTree.from_array([1])) == [1])
print(sol.inorderTraversal(BinaryTree.from_array([1,None,2,3])) == [1, 3, 2])
print(sol.inorderTraversal(BinaryTree.from_array([1,2,3,4,5,None,8,None,None,6,7,9])) == [4, 2, 6, 5, 7, 1, 3, 9, 8])



