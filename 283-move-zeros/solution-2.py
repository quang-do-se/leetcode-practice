from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


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