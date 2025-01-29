from typing import Optional, List
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from complete_binary_tree import BinaryTree


class Solution:
    def leafSimilar(self, root1: Optional[BinaryTree], root2: Optional[BinaryTree]) -> bool:
        return self.find_leaf_nodes(root1) == self.find_leaf_nodes(root2)

    def find_leaf_nodes(self, root: Optional[BinaryTree]) -> List:
        # Recursive approach
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [root.val]

        leaf_nodes = []
        if root.left is not None:
            leaf_nodes += self.find_leaf_nodes(root.left)

        if root.right is not None:
            leaf_nodes += self.find_leaf_nodes(root.right)

        return leaf_nodes


sol = Solution()

print(
        sol.leafSimilar(
            BinaryTree.from_array([3,5,1,6,2,9,8,None,None,7,4]),
            BinaryTree.from_array([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
        ) == True
    )

print(
        sol.leafSimilar(
            BinaryTree.from_array([1,2,3]),
            BinaryTree.from_array([1,3,2])
        ) == False
    )