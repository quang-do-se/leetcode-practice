class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = [0] * n

        output[0] = 1
        # Calculate left_sum
        for i in range(1, n):
            output[i] = output[i - 1] * nums[i - 1]

        right_sum = 1
        for i in range(n - 1, -1, -1):
            output[i] = right_sum * output[i]
            right_sum *= nums[i]

        return output

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]) == [24,12,8,6])
print(sol.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0])
print(sol.productExceptSelf([-1, 1]) == [1, -1])
print(sol.productExceptSelf([2, 1]) == [1, 2])