from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        curr = prev = is_zero_seen = 0

        for e in nums:
            if e == 0:   # Update for every zero
                is_zero_seen = 1

                if curr > 0:
                    max_ones = max(max_ones, curr + prev + is_zero_seen)

                prev, curr = curr, 0
            else:
                curr += 1
        
        max_ones = max(max_ones, curr + prev + is_zero_seen)
        
        return max_ones


sol = Solution()
print(sol.findMaxConsecutiveOnes([0, 1, 1, 1]) == 4)
print(sol.findMaxConsecutiveOnes([1, 1, 1, 1]) == 4)
print(sol.findMaxConsecutiveOnes([1, 1, 1, 0]) == 4)
print(sol.findMaxConsecutiveOnes([1, 1, 0, 1]) == 4)
print(sol.findMaxConsecutiveOnes([1, 1, 1, 0, 1, 1]) == 6)
print(sol.findMaxConsecutiveOnes([1, 1, 1, 0, 0, 1, 1]) == 4)
print(sol.findMaxConsecutiveOnes([1, 1, 0, 0, 1, 1, 1, 1]) == 5)
print(sol.findMaxConsecutiveOnes([0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0]) == 7)
print(sol.findMaxConsecutiveOnes([0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0]) == 7)