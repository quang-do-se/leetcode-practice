from typing import Generator, Optional, Self, List

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


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return list(self.find_leaf_nodes(root1)) == list(self.find_leaf_nodes(root2))

    def find_leaf_nodes(self, root: Optional[TreeNode]) -> Generator[Optional[TreeNode]]:
        # Recursive approach
        if root is not  None:
            if root.left is None and root.right is None:
                yield root.val

            yield from self.find_leaf_nodes(root.left)
            yield from self.find_leaf_nodes(root.right)


sol = Solution()

print(
        sol.leafSimilar(
            TreeNode.generate_from_array([3,5,1,6,2,9,8,None,None,7,4]),
            TreeNode.generate_from_array([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
        ) == True
    )

print(
        sol.leafSimilar(
            TreeNode.generate_from_array([1,2,3]),
            TreeNode.generate_from_array([1,3,2])
        ) == False
    )