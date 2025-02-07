from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] == val:
                while nums[r] == val and r >= 0:
                    r -= 1

                if r > l:
                    nums[l], nums[r] = nums[r], nums[l]
                else:
                    break

            l += 1

        return l


sol = Solution()
nums = [3,2,2,3]
print(sol.removeElement(nums, 3))
print(nums)


nums = [4,5,6]
print(sol.removeElement(nums, 3))
print(nums)

nums = [3,2,2]
print(sol.removeElement(nums, 3))
print(nums)

nums = [0,1,2,2,3,0,4,2]
print(sol.removeElement(nums, 2))
print(nums)
