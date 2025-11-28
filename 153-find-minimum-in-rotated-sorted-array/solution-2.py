from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1

        while l < h:
            m = (l + h) // 2
            if nums[m] > nums[h]:
                l = m + 1
            else:
                h = m

        return nums[l]


sol = Solution()
print(sol.findMin([0, 1, 2, 3, 4]))
print(sol.findMin([1, 2, 3, 4, 0]))
print(sol.findMin([2, 3, 4, 0, 1]))
print(sol.findMin([3, 4, 0, 1, 2]))
print(sol.findMin([4, 0, 1, 2, 3]))
