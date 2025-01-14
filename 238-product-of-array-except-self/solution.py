class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [nums[0]] * len(nums)
        suffix = [nums[len(nums) - 1]] * len(nums)

        for i in range(1, len(nums), 1):
            prefix[i] = prefix[i - 1]  * nums[i]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1]  * nums[i]
        
        output = []

        output.append(suffix[1])

        for i in range(0, len(nums) - 2):
            output.append(prefix[i] * suffix[i + 2])

        output.append(prefix[-2])

        return output

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]) == [24,12,8,6])
print(sol.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0])
print(sol.productExceptSelf([-1, 1]) == [1, -1])
print(sol.productExceptSelf([2, 1]) == [1, 2])