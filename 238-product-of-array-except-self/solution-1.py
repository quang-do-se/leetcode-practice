from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n

        # Calculate suffix
        output[n - 1] = nums[n - 1]
        for i in range(n - 2, 0, -1):
            output[i] = output[i + 1] * nums[i]

        output[0] = output[1]

        # Calculate prefix just in time
        prefix = 1
        for i in range(n - 2):
            prefix *= nums[i]
            output[i + 1] = prefix * output[i + 2]

        output[n - 1] = prefix * nums[n - 2]

        return output


sol = Solution()
print(sol.productExceptSelf([1,2,3,4]) == [24,12,8,6])
print(sol.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0])
print(sol.productExceptSelf([-1, 1]) == [1, -1])
print(sol.productExceptSelf([2, 1]) == [1, 2])