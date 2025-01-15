class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = nums[0]
        for i in range(1, n, 1):
            prefix[i] = prefix[i - 1]  * nums[i]

        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1]  * nums[i]
        
        output = [0] * n

        output[0] = suffix[1]

        for i in range(0, n - 2):
            output[i + 1] = prefix[i] * suffix[i + 2]

        output[n - 1] = prefix[-2]

        return output

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]) == [24,12,8,6])
print(sol.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0])
print(sol.productExceptSelf([-1, 1]) == [1, -1])
print(sol.productExceptSelf([2, 1]) == [1, 2])