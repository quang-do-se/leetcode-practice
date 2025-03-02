from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        n = len(nums)
        sum = 0
        min_sub_len = n + 1

        while r < n:
            sum += nums[r]

            while sum >= target:
                min_sub_len = min(min_sub_len, r - l + 1)
                sum -= nums[l]
                l += 1

            r += 1

        return 0 if min_sub_len == n + 1 else min_sub_len


sol = Solution()
print(sol.minSubArrayLen(6, [1, 3, 1, 2, 4, 6]))
print(sol.minSubArrayLen(6, [7, 3, 1, 2, 4]))
print(sol.minSubArrayLen(11, [1,2,3,4,5]))
print(sol.minSubArrayLen(15, [1,2,3,4,5]))