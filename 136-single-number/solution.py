from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res
    

sol = Solution()
print(sol.singleNumber([2,2,1]) == 1)
print(sol.singleNumber([4,1,2,1,2]) == 4)
print(sol.singleNumber([1]) == 1)