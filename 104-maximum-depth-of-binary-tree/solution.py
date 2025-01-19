from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        maxLeft = 0
        if root.left != None:
            maxLeft = self.maxDepth(root.left)

        maxRight = 0
        if root.right != None:
            maxRight = self.maxDepth(root.right)

        return 1 + max(maxLeft, maxRight)


node = TreeNode(TreeNode(), TreeNode())
sol = Solution()
print(sol.maxDepth(node))


