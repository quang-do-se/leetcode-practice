from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Breadth-First Traversal Binary Tree
# Ref: https://stackoverflow.com/questions/71420248/how-to-draw-the-binary-tree-for-this-input-1-2-2-3-null-null-3-4-null-null-4
class BinaryTree:
    @staticmethod
    def from_array(binary_tree_array: List[int]) -> Optional[TreeNode]:
        if len(binary_tree_array) == 0 or binary_tree_array[0] is None:
            return None

        i = 0
        root = TreeNode(binary_tree_array[i])
        queue = deque([root])

        while len(queue) > 0 and i < len(binary_tree_array):
            node = queue.popleft()

            i += 1
            if i < len(binary_tree_array) and binary_tree_array[i] is not None:
                node.left = TreeNode(binary_tree_array[i])
                queue.append(node.left)

            i += 1
            if i < len(binary_tree_array) and binary_tree_array[i] is not None:
                node.right = TreeNode(binary_tree_array[i])
                queue.append(node.right)

        if i < len(binary_tree_array):
            raise("Not a valid binary tree.")

        return root

    @staticmethod
    def to_array(tree: Optional[TreeNode]) -> List:
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

        while len(result) > 0 and result[-1] is None:
            result.pop()

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