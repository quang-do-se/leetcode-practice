class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        last_non_zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[last_non_zero_index]
                nums[last_non_zero_index] = nums[i]
                nums[i] = temp
                last_non_zero_index += 1


sol = Solution()
my_list = [0, 0, 1]
sol.moveZeroes(my_list)

print(my_list)