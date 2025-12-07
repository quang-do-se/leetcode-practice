from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1

        return l


sol = Solution()
print(sol.findPeakElement([1]))
print(sol.findPeakElement([1, 2, 3, 1]))
print(sol.findPeakElement([0, 5, 4, 3, 4]))
print(sol.findPeakElement([4, 3, 2, 1, 5]))
