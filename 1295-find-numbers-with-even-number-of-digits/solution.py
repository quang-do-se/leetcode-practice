from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count_even = 0
        for i in range(len(nums)):
            c = nums[i]

            count_digit = 0
            while c != 0:   # Can only handle positive integers
                c //= 10
                count_digit += 1

            if count_digit & 1 == 0:
                count_even += 1

        return count_even


sol = Solution()
print(sol.findNumbers([12,345,2,6,7896]) == 2)
print(sol.findNumbers([555,901,482,1771]) == 1)