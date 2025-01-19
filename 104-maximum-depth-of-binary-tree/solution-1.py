from typing import Optional, Self

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def generateFromArray(binary_tree_array: list[int], index = 0) -> Self:
        node = None

        if index > len(binary_tree_array) - 1 or binary_tree_array[index] is None:
            return node

        if binary_tree_array[index] is not None:
            node = TreeNode(val = binary_tree_array[index])

        node.left = TreeNode.generateFromArray(binary_tree_array, index * 2 + 1)
        node.right = TreeNode.generateFromArray(binary_tree_array, index * 2 + 2)

        return node


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative approach
        if root is None:
            return 0

        stack = [(root, 1)]
        max_depth = 1

        while len(stack) > 0:
            node, current_depth = stack.pop()
            max_depth = max(max_depth, current_depth)
            if node.left is not None:
                stack.append((node.left, current_depth + 1))
            if node.right is not None:
                stack.append((node.right, current_depth + 1))

        return max_depth


sol = Solution()
print(sol.maxDepth(TreeNode.generateFromArray([3,9,20,None,None,15,7])) == 3)
print(sol.maxDepth(TreeNode.generateFromArray([1,None,2])) == 2)
print(sol.maxDepth(TreeNode.generateFromArray([])) == 0)
print(sol.maxDepth(TreeNode.generateFromArray([1])) == 1)