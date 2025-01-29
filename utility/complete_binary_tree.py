from collections import deque
from typing import List, Optional, Self


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    @staticmethod
    def from_array(binary_tree_array: List[int], index = 0) -> Optional[Self]:
        if index > len(binary_tree_array) - 1 or binary_tree_array[index] is None:
            return None

        node = TreeNode(binary_tree_array[index])

        node.left = BinaryTree.from_array(binary_tree_array, index * 2 + 1)
        node.right = BinaryTree.from_array(binary_tree_array, index * 2 + 2)

        return node

    @staticmethod
    def to_array(tree: Optional[Self]) -> List:
        if tree is None:
            return []

        result = []

        queue = deque([(tree, 0)])

        while len(queue) > 0:
            node, index = queue.popleft()

            # Ensure the result list is large enough
            if index >= len(result):
                result.extend([None] * (index - len(result) + 1))

            result[index] = node.val

            if node.left is not None:
                queue.append((node.left, index * 2 + 1))
            if node.right is not None:
                queue.append((node.right, index * 2 + 2))

        return result