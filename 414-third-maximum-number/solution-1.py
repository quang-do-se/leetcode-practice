from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1 = max(nums)
        m2 = m3 = min(nums)

        for v in nums:
            if v != m1 and v > m2:
                m2 = v

        for v in nums:        
            if v != m1 and v != m2 and v > m3:
                m3 = v

        return m1 if m2 == m3 else m3
    

sol = Solution()
print(sol.thirdMax([3,2,1]) == 1)
print(sol.thirdMax([5,7,2,3,1]) == 3)
print(sol.thirdMax([5,7,2,6,4]) == 5)
print(sol.thirdMax([1,2]) == 2)

