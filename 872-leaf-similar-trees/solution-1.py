from typing import Optional, Self, List

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
        return self.find_leaf_nodes(root1) == self.find_leaf_nodes(root2)

    def find_leaf_nodes(self, root: Optional[TreeNode]) -> List:
        # Iterative approach
        if root is None:
            return []

        leaf_nodes = []
        queue = [root]

        while len(queue) > 0:
            node = queue.pop()

            if node.left is None and node.right is None:
                leaf_nodes.append(node.val)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return leaf_nodes


sol = Solution()
print(
    (
        sol.find_leaf_nodes(TreeNode.generate_from_array([3,5,1,6,2,9,8,None,None,7,4]))
        == sol.find_leaf_nodes(TreeNode.generate_from_array([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]))
    )
    == True)
print(
    (
        sol.find_leaf_nodes(TreeNode.generate_from_array([1,2,3])) 
        == sol.find_leaf_nodes(TreeNode.generate_from_array([1,3,2]))
    )
    == False)