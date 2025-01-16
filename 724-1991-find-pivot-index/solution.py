class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0
        total_sum = sum(nums)

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]

        return -1

sol = Solution()
print(sol.pivotIndex([1, 7, 3, 6, 5, 6]) == 3)
print(sol.pivotIndex([1, 2, 3]) == -1)
print(sol.pivotIndex([2, 1, -1]) == 0)
print(sol.pivotIndex([2, 3, -1, 8, 4]) == 3)
print(sol.pivotIndex([1, -1, 4]) == 2)
print(sol.pivotIndex([2, 5]) == -1)