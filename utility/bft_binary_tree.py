from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.col = 0
        self.row = 0


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


    @staticmethod
    def visualize(tree: Optional[TreeNode], do_print: bool = True) -> str:
        if tree is None:
            return ""

        stack = deque([(tree, False, 0)])
        tree_width = 0
        tree_depth = 0
        buffer_length = 2

        """
        Calculate node positions:
          - Global `tree_width` keeps track of the current position in the tree. Every node has its own unique column.
          - Using DFS to calculate the left most node's position first and increase the tree column position
        """
        while stack:
            node, visited, row = stack.pop()
            tree_depth = max(tree_depth, row)

            if node.left is None and node.right is None:
                node.col = tree_width
                node.row = row
                tree_width += len(str(node.val)) + buffer_length   # length of num + buffer length
                continue

            if not visited:
                if node.right is not None:
                    stack.append((node.right, False, row + 1))

                stack.append((node, True, row))

                if node.left is not None:
                    stack.append((node.left, False, row + 1))
            else:
                node.col = tree_width
                node.row = row
                tree_width += len(str(node.val)) + buffer_length   # length of num + buffer length


        """
        Draw node position
        Draw spaces and lines "_" and "|"
        """
        queue = deque([tree])
        row_length = {}
        print_row =  {}
        print_line = {}

        while queue:
            node = queue.popleft()

            if node.row not in print_row:
                print_row[node.row] = []
                row_length[node.row] = 0

            print_row[node.row].append(" " * (node.col - row_length[node.row]))
            row_length[node.row] += node.col - row_length[node.row]
            node_val_str = str(node.val)
            print_row[node.row].append(node_val_str)
            row_length[node.row] += len(node_val_str)

            if node.row not in print_line:
                print_line[node.row] = []


            # Print spaces and lines "_" and "|"
            if node.row >= tree_depth:
                continue

            if node.left is not None:
                while len(print_line[node.row]) < node.left.col:
                    print_line[node.row].append(" ")

                while len(print_line[node.row]) <= node.col:
                    print_line[node.row].append("_")

                print_line[node.row][node.col] = "|"
                queue.append(node.left)
            else:
                while len(print_line[node.row]) < node.col:
                    print_line[node.row].append(" ")

            if node.right is not None:
                while len(print_line[node.row]) <= node.right.col:
                    print_line[node.row].append("_")

                print_line[node.row][node.col] = "|"
                queue.append(node.right)


        # Finalize all draw components
        print_tree = []
        for level in range(len(print_row)):
            print_tree.append("".join(print_row[level]))
            print_tree.append("".join(print_line[level]))

        visualized_tree = "\n".join(print_tree)

        if do_print:
            print(visualized_tree)
        return visualized_tree




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




"""
array = [0,1,2,3,45555555555,5,6,7,None,4,7]
BinaryTree.visualize(BinaryTree.from_array(array))
array = [0,1]
BinaryTree.visualize(BinaryTree.from_array(array))
array = [0,None,1]
BinaryTree.visualize(BinaryTree.from_array(array))
array = [0]
BinaryTree.visualize(BinaryTree.from_array(array))
array = []
BinaryTree.visualize(BinaryTree.from_array(array))
"""

"""

print(BinaryTree.visualize(BinaryTree.from_array([0,1,2,3,4,5,6,7,None,4,7]), False) ==
'''\
                  0
      ____________|______
      1                 2
   ___|______        ___|___
   3        4        5     6
___|     ___|___           
7        4     7
''')

print(BinaryTree.visualize(BinaryTree.from_array([0]), False) == 
'''\
0
''')

print(BinaryTree.visualize(BinaryTree.from_array([]), False) == "")

print(BinaryTree.visualize(BinaryTree.from_array([6,5,5,4,6,None,6]), False) == 
'''\
         6
   ______|___
   5        5
___|___     |___
4     6        6
''')
"""