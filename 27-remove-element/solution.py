from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = w = 0

        for r in range(len(nums)):
            if nums[r] != val:
                nums[w] = nums[r]
                w += 1
        return w


sol = Solution()

nums = [4, 5]
print(sol.removeElement(nums, 5) == 1)
print(nums)

nums = [3, 3]
print(sol.removeElement(nums, 3) == 0)
print(nums)

nums = [3,2,2,3]
print(sol.removeElement(nums, 3) == 2)
print(nums)

nums = [4,5,6]
print(sol.removeElement(nums, 3) == 3)
print(nums)

nums = [3,2,2]
print(sol.removeElement(nums, 3) == 2)
print(nums)

nums = [0,1,2,2,3,0,4,2]
print(sol.removeElement(nums, 2) == 5)
print(nums)
