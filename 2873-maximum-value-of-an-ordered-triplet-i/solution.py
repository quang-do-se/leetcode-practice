from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)

        max_total = 0
        for i in range(n):
            max_sub = 0
            for j in range(i + 1, n):
                if nums[i] <= nums[j]:
                    continue
                else:
                    sub = nums[i] - nums[j]
                    if sub > max_sub:
                        for k in range (j + 1, n):
                            total = sub * nums[k]

                            if total > max_total:
                                max_total = total
                        max_sub = sub

        return max_total



sol = Solution()
print(sol.maximumTripletValue([12,6,1,2,7]) == 77)
print(sol.maximumTripletValue([1,10,3,4,19]) == 133)
print(sol.maximumTripletValue([1,2,3]) == 0)