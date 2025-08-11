from collections import deque
from typing import List, Optional, Self


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    @staticmethod
    def from_array(binary_tree_array: List[int]) -> Optional[Self]:
        if len(binary_tree_array) == 0 or binary_tree_array[0] is None:
            return None

        root = TreeNode(binary_tree_array[0])
        queue = deque([(root, 0)])

        while len(queue) > 0:
            node, index = queue.popleft()

            left_index = index * 2 + 1
            if left_index < len(binary_tree_array) and binary_tree_array[left_index] is not None:
                node.left = TreeNode(binary_tree_array[left_index])
                queue.append((node.left, left_index))

            right_index = index * 2 + 2
            if right_index < len(binary_tree_array) and binary_tree_array[right_index] is not None:
                node.right = TreeNode(binary_tree_array[right_index])
                queue.append((node.right, right_index))

        return root

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



""" 
array = [None]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == [])

array = [0]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == array)

array = [1]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == array)

array = [1, 2]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == array)

array = [1, None, 2]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == array)

array = [1,None,2,None,3]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == [1,None,2])


array = [1,2,3]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == array)

array = [1,2,None,3]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == array)

array = [1,None,2,None,None,None,3]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == array)


array = [4,2,7,1,3,6,9]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == array)

array = [1,2,3,4,None,5,None,None,None,7]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == [1,2,3,4,None,5]) 
"""
