from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper([], nums)

    def helper(self, prefix: List[int], remaining: List[int]) -> List[List[int]]:
        if remaining == []:
            return [prefix]

        result = []

        for i in range(len(remaining)):
            result += self.helper(prefix + [remaining[i]], remaining[:i] + remaining[i + 1:])

        return result


sol = Solution()
print(sol.permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
print(sol.permute([0, 1]) == [[0, 1], [1, 0]])


"""
Be careful with list concatenation

>>> [1] + 2
TypeError: can only concatenate list (not "int") to list

>>> [1] + [2]
[1, 2]

>>> [[1]] + [2]
[[1], 2]

>>> [[1]] + [[2]]
[[1], [2]]
"""