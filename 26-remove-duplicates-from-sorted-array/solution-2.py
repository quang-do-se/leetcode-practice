from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 0

        for r in range(0, len(nums)):
            if r == 0 or nums[r] != nums[w - 1]:  # Compare read element with last written element
                nums[w] = nums[r]
                w += 1

        return w


sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums) == 5)
print(nums)

nums = [1,1,2]
print(sol.removeDuplicates(nums) == 2)
print(nums)

nums = [1]
print(sol.removeDuplicates(nums) == 1)
print(nums)

nums = []
print(sol.removeDuplicates(nums) == 0)
print(nums)