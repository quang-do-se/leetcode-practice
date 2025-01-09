class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return self.helper([], nums)

    def helper(self, prefix: list[int], remaining: list[int]) -> list[list[int]]:
        if remaining == []:
            return [prefix]

        result = []

        for i in range(len(remaining)):
            result += self.helper(prefix + [remaining[i]], remaining[:i] + remaining[i + 1:])

        return result

sol = Solution()    
print(sol.permute([1, 2, 3]))
print(sol.permute([0, 1]))


"""
>>> [1] + 2
TypeError: can only concatenate list (not "int") to list
>>> [1] + [2]
[1, 2]
>>> [[1]] + [2]
[[1], 2]
>>> [[1]] + [[2]]
[[1], [2]]
"""