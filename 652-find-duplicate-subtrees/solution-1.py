import os
import sys

from typing import List, Optional

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from bft_binary_tree import TreeNode, BinaryTree

# Slow solution - due to string building and searching
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.count_map = {}
        self.result = []
        self.serialize_node(root)

        return self.result

    def update_map(self, serialized_tree: List[str], node: Optional[TreeNode]):
        hash_key = tuple(serialized_tree)
        if hash_key in self.count_map:
            if self.count_map[hash_key] == 1:
                self.result.append(node)
            self.count_map[hash_key] += 1
        else:
            self.count_map[hash_key] = 1


    def serialize_node(self, node: Optional[TreeNode]) -> str:
        if node == None:
            return "()"

        serialized_left_node = self.serialize_node(node.left)
        serialized_right_node = self.serialize_node(node.right)

        serialized_tree = f"({serialized_left_node}{node.val}{serialized_right_node})"

        self.update_map(serialized_tree, node)
        return serialized_tree


sol = Solution()

# sol.findDuplicateSubtrees(BinaryTree.from_array([0,1,2,None,3,4,5]))
# sol.findDuplicateSubtrees(BinaryTree.from_array([2,2,2,None,3,None,3]))

result = sol.findDuplicateSubtrees(BinaryTree.from_array([7,6,8,7,7,7,7,6,8,8,8,6,8,6,6,5,5,7,9,7,9,7,None,7,7,9,9,None,None,7,7,4,6,None,6,6,None,8,None,6,8,None,None,None,None,6,8,8,6,None,8,None,None,6,8,8,8,3,5,7,7,None,None,5,7,7,None,None,None,None,None,7,None,None,None,None,None,5,5,None,None,None,None,None,None,None,9,None,9,None,4,None,None,8,6,6,None,4,None,6,8,6,None,None,None,None,6,4,6,8,8,None,None,None,None,7,7,5,7,None,None,None,None,None,None,7,None,5,None,5,None,None,5,5,None,None,None,7,None,6,6,None,8,4,None,6,None,None,None,None,6,None,None,6,6,None,None,None,None,None,7,5,None,None,None,None,None,None,None,5,7,5,5,None,None,8,None,6,None,None,None,8,6,6,6,None,None,None,None,5]))
for node in result:
    BinaryTree.visualize(node)