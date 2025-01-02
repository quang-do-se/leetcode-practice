class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


sol = Solution()
my_list = [0,1,0,3,12]
sol.moveZeroes(my_list)

print(my_list)