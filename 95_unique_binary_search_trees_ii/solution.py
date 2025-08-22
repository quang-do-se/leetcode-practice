from typing import List, Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from bft_binary_tree import TreeNode, BinaryTree


class Solution:
    memo = {}

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.all_possible_BST(1, n)

    def all_possible_BST(self, start, end):
        if start > end:
            return [None]

        if (start, end) in self.memo:
            return self.memo[(start, end)]

        res = []
        for i in range(start, end + 1):

            left_list = self.all_possible_BST(start, i - 1)

            right_list = self.all_possible_BST(i + 1, end)

            for l in left_list:
                for r in right_list:
                    res.append(TreeNode(i, l, r))

        self.memo[(start, end)] = res

        return res


sol = Solution()

tree_list = sol.generateTrees(1)

for tree in tree_list:
    BinaryTree.visualize(tree)
