from typing import Generator, Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from complete_binary_tree import BinaryTree


class Solution:
    def leafSimilar(self, root1: Optional[BinaryTree], root2: Optional[BinaryTree]) -> bool:
        return list(self.find_leaf_nodes(root1)) == list(self.find_leaf_nodes(root2))

    def find_leaf_nodes(self, root: Optional[BinaryTree]) -> Generator[Optional[BinaryTree]]:
        # Recursive approach
        if root is not  None:
            if root.left is None and root.right is None:
                yield root.val

            yield from self.find_leaf_nodes(root.left)
            yield from self.find_leaf_nodes(root.right)


sol = Solution()

print(
        sol.leafSimilar(
            BinaryTree.generate_from_array([3,5,1,6,2,9,8,None,None,7,4]),
            BinaryTree.generate_from_array([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
        ) == True
    )

print(
        sol.leafSimilar(
            BinaryTree.generate_from_array([1,2,3]),
            BinaryTree.generate_from_array([1,3,2])
        ) == False
    )