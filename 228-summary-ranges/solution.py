from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)

        res = []
        
        left = 0
        right = 0

        while right < n:
            if right + 1 < n and nums[right + 1] == nums[right] + 1:
                right += 1
            else:
                if left == right:
                    res.append(f"{nums[left]}")
                else:
                    res.append(f"{nums[left]}->{nums[right]}")

                left = right + 1
                right = left

        return res
    

sol = Solution()
print(sol.summaryRanges([0,1,2,4,5,7]) == ['0->2', '4->5', '7'])
print(sol.summaryRanges([0,2,3,4,6,8,9]) == ['0', '2->4', '6', '8->9'])