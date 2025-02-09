from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0

        for read in range(0, len(nums)):
            # An element should be counted as unique 
            # if it's the first element in the Array, or is different to the one before it (last written element).
            if read == 0 or nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1

        return write


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