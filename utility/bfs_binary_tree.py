from collections import deque
from typing import List, Optional, Self

class BinaryTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def generate_from_array(binary_tree_array: List[int], index = 0) -> Optional[Self]:
        if len(binary_tree_array) == 0:
            return None
        
        i = 0
        root = BinaryTree(binary_tree_array[i])
        queue = deque([root])
        
        while i < len(binary_tree_array) and len(queue) > 0:
            node = queue.popleft()
            i += 1
            if i < len(binary_tree_array) and binary_tree_array[i] != None:
                left = BinaryTree(binary_tree_array[i])
                node.left = left
                queue.append(left)

            i += 1
            if i < len(binary_tree_array) and binary_tree_array[i] != None:
                right = BinaryTree(binary_tree_array[i])
                node.right = right
                queue.append(right)

        if i < len(binary_tree_array) or len(queue) > 0:
            raise("Not a valid binary tree.")
        
        return root

    @staticmethod
    def binary_tree_to_array(tree: Optional[Self]) -> List:
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
    

l = [1,None,2,None,4]
print(BinaryTree.binary_tree_to_array(BinaryTree.generate_from_array(l)))

""" l = [1,None,2,None,None,None,4]
print(BinaryTree.binary_tree_to_array(BinaryTree.generate_from_array(l))) """