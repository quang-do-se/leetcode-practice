from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            if nums[l] == val:
                r -= 1
                nums[l], nums[r] = nums[r], nums[l]
            else:
                l += 1
        print(f"l: {l}, r: {r}")
        return l


sol = Solution()
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
