import math
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Should read: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/editorial/#approach-3-using-logarithm
        count_even = 0
        for i in range(len(nums)):
            k = math.floor(math.log10(nums[i])) + 1
            if k & 1 == 0:
                count_even += 1

        return count_even


sol = Solution()
print(sol.findNumbers([12,345,2,6,7896]) == 2)
print(sol.findNumbers([555,901,482,1771]) == 1)