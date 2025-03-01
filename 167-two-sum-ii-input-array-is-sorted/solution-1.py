from typing import List


class Solution:
    # Accepted solution but slow
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
            
        return [-1, -1]


sol = Solution()
print(sol.twoSum([2,7,11,15], 9) == [1, 2])
print(sol.twoSum([2,3,4], 6) == [1, 3])
print(sol.twoSum([-1,0], -1) == [1, 2])