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
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


sol = Solution()
print(sol.maxDepth(TreeNode.generateFromArray([3,9,20,None,None,15,7])) == 3)
print(sol.maxDepth(TreeNode.generateFromArray([1,None,2])) == 2)
print(sol.maxDepth(TreeNode.generateFromArray([])) == 0)
print(sol.maxDepth(TreeNode.generateFromArray([1])) == 1)