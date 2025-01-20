from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        writer = 0

        # Move non-zero elements to the front
        for reader in range(len(nums)):
            if nums[reader] != 0:
                nums[writer] = nums[reader]
                writer += 1

        # Fill the remaining positions with zeroes
        for write_zero in range(writer, len(nums)):
            nums[write_zero] = 0


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