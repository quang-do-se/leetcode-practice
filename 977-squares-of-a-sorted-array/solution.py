from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        i = n - 1
        left = 0
        right = n - 1

        while left <= right:
            if abs(nums[right]) > abs(nums[left]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            res[i] = square * square
            i -= 1

        return res
    

sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))
print(sol.sortedSquares([-7,-3,2,3,11]))

