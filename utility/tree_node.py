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

        pre = []

        queue = deque([(tree, 0)])
        last_node = 0

        while len(queue) > 0:
            node, index = queue.popleft()
            pre.append((node, index))

            if node.left is not None:
                left_index = index * 2 + 1
                queue.append((node.left, left_index))
                last_node = left_index
            if node.right is not None:
                right_index = index * 2 + 2
                queue.append((node.right, right_index))
                last_node = right_index

        post = [None] * (last_node + 1)
        for e in pre:
            node, index  = e
            post[index] = node.val

        return post