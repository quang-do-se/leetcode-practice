from collections import deque
from typing import List, Optional, Self

class BinaryTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_array(binary_tree_array: List[int], index = 0) -> Optional[Self]:
        if len(binary_tree_array) == 0:
            return None

        i = 0
        root = BinaryTree(binary_tree_array[i])
        queue = deque([root])

        while i < len(binary_tree_array) and len(queue) > 0:
            node = queue.popleft()

            i += 1
            if i < len(binary_tree_array) and binary_tree_array[i] is not None:
                node.left = BinaryTree(binary_tree_array[i])
                queue.append(node.left)

            i += 1
            if i < len(binary_tree_array) and binary_tree_array[i] is not None:
                node.right = BinaryTree(binary_tree_array[i])
                queue.append(node.right)

        if i < len(binary_tree_array):
            raise("Not a valid binary tree.")

        return root

    @staticmethod
    def to_array(tree: Optional[Self]) -> List:
        if tree is None:
            return []

        result = []
        queue = deque([tree])

        while len(queue) > 0:
            node = queue.popleft()
            if node is not None:
                result.append(node.val)

                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        i = len(result) - 1
        while result[i] is None and i > 0:
            result.pop()
            i -= 1

        return result


array = [None]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == array)

"""
array = [0]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == array)

array = [1]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == array)

array = [1, 2]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == array)

array = [1, None, 2]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == array)

array = [1,None,2,None,3]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == array)

array = [1,2,None,3]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == array)

array = [1,2,3]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == array)

array = [4,2,7,1,3,6,9]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == array)

array = [1,2,3,4,None,5,None,None,None,7]
print(BinaryTree.to_array(BinaryTree.from_array(array)) == array)
"""

# array = [1,None,2,None,None,None,4]  # Error