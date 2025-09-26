from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_dup = 0
        prev_number = nums[0]
        shift = 0
        n = len(nums)

        for i in range(1, n):
            if nums[i] == prev_number:
                current_dup += 1

                if current_dup > 1:
                    shift += 1
            else:
                current_dup = 0
                prev_number = nums[i]

            if shift > 0 and current_dup <= 1:   # or just `if shift > 0:`
                nums[i - shift] = nums[i]

        return n - shift


sol = Solution()
print(sol.removeDuplicates([1]) == 1)
print(sol.removeDuplicates([1, 1]) == 2)
print(sol.removeDuplicates([1, 1, 1]) == 2)
print(sol.removeDuplicates([1, 1, 1, 2, 2, 3]) == 5)
print(sol.removeDuplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4]) == 7)
