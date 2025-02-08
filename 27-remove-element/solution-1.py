from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        We initialize `r = len(nums)` to ensure the algorithm correctly handles cases where no elements need to be removed.

        If `r` were set to `len(nums) - 1`, the maximum value of `l` would also be `len(nums) - 1` since the loop condition is `l < r`.
        This could lead to incorrect behavior in edge cases.

        For example, if no elements match `val`, `l` should naturally reach `len(nums)`, indicating all elements are valid.
        However, with `r = len(nums) - 1`, the loop might terminate too early, resulting in an incorrect output.
        """
        l = 0
        r = len(nums)
        while l < r:
            if nums[l] == val:
                r -= 1
                nums[l], nums[r] = nums[r], nums[l]
            else:
                l += 1

        return l


sol = Solution()


nums = [1]
print(sol.removeElement(nums, 1) == 0)
print(nums)

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
