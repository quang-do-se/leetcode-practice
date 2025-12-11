from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) - 1
        l = 0
        r = n

        # Find lower bound
        # Find first True for nums[i]>=3
        while l < r:
            m = l + (r - l) // 2

            if nums[m] < target:
                l = m + 1
            else:
                r = m

        lower_bound = l if nums and nums[l] == target else -1

        l = 0
        r = n

        # Find upper bound
        # Find last True for nums[i]<=3
        while l < r:
            m = l + (r - l + 1) // 2

            if nums[m] > target:
                r = m - 1
            else:
                l = m

        upper_bound = l if nums and nums[l] == target else -1

        return [lower_bound, upper_bound]


sol = Solution()
print(sol.searchRange([1, 3, 3, 3, 4, 5, 6, 7], 3))
print(sol.searchRange([1, 2, 2, 3], 3))
print(sol.searchRange([1, 2, 2, 2], 3))
print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))
