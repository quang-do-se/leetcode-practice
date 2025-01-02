class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        size = len(nums)
        head_zero_pointer = -1

        for i in range(size):
            if nums[i] == 0:
                if head_zero_pointer == -1:
                    head_zero_pointer = i
            elif head_zero_pointer != -1 and i > head_zero_pointer:
                nums[head_zero_pointer] = nums[i]
                nums[i] = 0
                head_zero_pointer += 1


sol = Solution()
my_list = [0, 0, 1]
sol.moveZeroes(my_list)

print(my_list)