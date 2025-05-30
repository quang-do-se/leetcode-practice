from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # snowball algorithm: https://leetcode.com/problems/move-zeroes/solutions/172432/the-easiest-but-unusual-snowball-java-solution-beats-100-o-n-clear-explanation/
        snowball = 0
        i = 0
        while i < len(nums):
            if nums[i] % 2 == 1:
                snowball += 1
            elif snowball > 0:
                nums[i], nums[i - snowball] = nums[i - snowball], nums[i]
            i += 1

        return nums


sol = Solution()
print(sol.sortArrayByParity([3,1,2,5,4]) == [2, 4, 3, 5, 1])  # Non stable
print(sol.sortArrayByParity([3,2,4]) == [2,4,3])
print(sol.sortArrayByParity([3,5,2,4,6,8]) == [2, 4, 6, 8, 3, 5])
print(sol.sortArrayByParity([0]) == [0])