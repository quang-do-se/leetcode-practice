from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)

        max = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] <= nums[j]:
                    continue
                else:
                    sub = nums[i] - nums[j]

                    for k in range (j + 1, n):
                        total = sub * nums[k]

                        if total > max:
                            max = total

        return max



sol = Solution()
print(sol.maximumTripletValue([12,6,1,2,7]))
print(sol.maximumTripletValue([1,10,3,4,19]))
print(sol.maximumTripletValue([1,2,3]))