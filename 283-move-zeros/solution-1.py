from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero_index = 0  # Points to the next position for a non-zero value

        # Move non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_index] = nums[i]
                last_non_zero_index += 1

        # Fill the remaining positions with zeroes
        for i in range(last_non_zero_index, len(nums)):
            nums[i] = 0


sol = Solution()

list = [0,1,0,3,12]
sol.moveZeroes(list)
print(list == [1, 3, 12, 0, 0])

list = [1]
sol.moveZeroes(list)
print(list == [1])

list = [1, 0]
sol.moveZeroes(list)
print(list == [1, 0])