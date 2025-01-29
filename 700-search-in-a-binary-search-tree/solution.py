from typing import Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from complete_binary_tree import TreeNode, BinaryTree


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        else:
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