from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write_index = 1  # Start from the second element since the first element is always unique and in the correct position

        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[write_index - 1]:  # Compare with last written element
                nums[write_index] = nums[read_index]
                write_index += 1

        return write_index


sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums) == 5)
print(nums)

nums = [1,1,2]
print(sol.removeDuplicates(nums) == 2)
print(nums)

nums = [1]
print(sol.removeDuplicates(nums) == 1)
print(nums)

nums = []
print(sol.removeDuplicates(nums) == 0)
print(nums)