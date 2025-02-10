from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        Two-pointer approach with same direction

        All even elements are before `write` index.
        """

        write = 0

        for read in range(len(nums)):
            if nums[read] % 2 == 0:
                if read > write:
                    nums[read], nums[write] = nums[write], nums[read]
                write += 1

        return nums


sol = Solution()
print(sol.sortArrayByParity([2,4,6,7,8,9]))
print(sol.sortArrayByParity([1,3,5]))
print(sol.sortArrayByParity([2,4,6]))
print(sol.sortArrayByParity([3,1,2,4]))
print(sol.sortArrayByParity([0]) == [0])