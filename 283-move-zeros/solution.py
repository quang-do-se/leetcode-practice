from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        head_zero_pointer = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                if head_zero_pointer == -1:
                    head_zero_pointer = i
            elif head_zero_pointer != -1:
                nums[head_zero_pointer] = nums[i]
                nums[i] = 0
                head_zero_pointer += 1


sol = Solution()
my_list = [0,1,0,3,12]
sol.moveZeroes(my_list)

print(my_list == [1, 3, 12, 0, 0])