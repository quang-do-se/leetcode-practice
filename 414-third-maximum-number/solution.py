from math import inf
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1 = m2 = m3 = -inf

        for v in nums:
            if v == m1 or v == m2 or v == m3:
                continue

            if v > m1:
                m3 = m2
                m2 = m1
                m1 = v
            elif v > m2:
                m3 = m2
                m2 = v
            elif v > m3:
                m3 = v                

        return m1 if m3 == -inf else m3
    

sol = Solution()
print(sol.thirdMax([3,2,1]) == 1)
print(sol.thirdMax([5,7,2,3,1]) == 3)
print(sol.thirdMax([5,7,2,6,4]) == 5)
print(sol.thirdMax([1,2]) == 2)
