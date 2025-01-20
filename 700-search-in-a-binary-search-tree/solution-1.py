from collections import deque
from typing import List, Optional, Self

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def generate_from_array(binary_tree_array: List[int], index = 0) -> Self:
        node = None

        if index > len(binary_tree_array) - 1 or binary_tree_array[index] is None:
            return node

        if binary_tree_array[index] is not None:
            node = TreeNode(val = binary_tree_array[index])

        node.left = TreeNode.generate_from_array(binary_tree_array, index * 2 + 1)
        node.right = TreeNode.generate_from_array(binary_tree_array, index * 2 + 2)

        return node

    @staticmethod
    def binary_tree_to_array(tree: Optional[Self]) -> List:
        if tree is None:
            return []

        array = []
        queue = deque([tree])

        while len(queue) > 0:
            node = queue.popleft()
            array.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return array


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None and root.val != val:
            if val < root.val:
                root = root.left
            else:
                root = root.right
        
        return root


sol = Solution()

print(
        TreeNode.binary_tree_to_array(sol.searchBST(TreeNode.generate_from_array([4,2,7,1,3]), 2))
        == [2,1,3]
    )
print(
        TreeNode.binary_tree_to_array(sol.searchBST(TreeNode.generate_from_array([4,2,7,1,3]), 5))
        == []
    )