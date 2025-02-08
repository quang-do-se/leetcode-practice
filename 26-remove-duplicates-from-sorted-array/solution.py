from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = r = 0
        prev = None
        for r in range(len(nums)):
            if nums[r] != prev:
                nums[w] = prev = nums[r]
                w += 1
        return w
    

sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums))
print(nums)


nums = [1,1,2]
print(sol.removeDuplicates(nums))
print(nums)

nums = [1]
print(sol.removeDuplicates(nums))
print(nums)