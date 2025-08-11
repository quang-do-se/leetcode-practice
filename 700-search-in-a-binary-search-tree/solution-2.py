from typing import Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from bft_binary_tree import TreeNode, BinaryTree


# Search a non binary search tree
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if root.val == val:
            return root
        
        candidate = self.searchBST(root.left, val)
        if candidate is not None:
            return candidate
        
        return self.searchBST(root.right, val)


sol = Solution()

print(
        BinaryTree.to_array(sol.searchBST(BinaryTree.from_array([4,2,7,1,3]), 2))
        == [2,1,3]
    )
print(
        BinaryTree.to_array(sol.searchBST(BinaryTree.from_array([4,2,7,1,3]), 5))
        == []
    ) 
print(
        BinaryTree.to_array(sol.searchBST(BinaryTree.from_array([4,2,7,1,3]), 2))
        == [2,1,3]
    )
print(
        BinaryTree.to_array(sol.searchBST(BinaryTree.from_array([18,2,22,None,None,None,63,None,84,None,None]), 63))
        == [63, None, 84]
    )    