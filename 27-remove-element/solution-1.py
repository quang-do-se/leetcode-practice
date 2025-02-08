from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of `val` from `nums` in-place and returns the new length.

        This algorithm uses a two-pointer approach:
        - `i` is a pointer for writing the correct elements, starting from the beginning
        - `n` represents the effective length of the array (excluding removed elements).

        The swapping mechanism:
        - When `nums[i] == val`, we swap `nums[i]` with `nums[n - 1]` since `n - 1` is the the last index of the array of length `n`.
        - After the swap, decrease `n` to exclude the swapped value.
        - This effectively removes `val` from the valid portion of the array of length `n`.
        - If `nums[i]` does not match `val`, we simply advance `i`.

        The process continues until the left pointer `i` meets or exceeds the right pointer `n`. 
        At this point, `i` or `n` represents the new length of the list, which excludes all occurrences of `val`.
        """

        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
                n -= 1
            else:
                i += 1

        return i


sol = Solution()


nums = [1]
print(sol.removeElement(nums, 1) == 0)
print(nums)

nums = [4, 5]
print(sol.removeElement(nums, 5) == 1)
print(nums)

nums = [3, 3]
print(sol.removeElement(nums, 3) == 0)
print(nums)

nums = [3,2,2,3]
print(sol.removeElement(nums, 3) == 2)
print(nums)

nums = [4,5,6]
print(sol.removeElement(nums, 3) == 3)
print(nums)

nums = [3,2,2]
print(sol.removeElement(nums, 3) == 2)
print(nums)

nums = [0,1,2,2,3,0,4,2]
print(sol.removeElement(nums, 2) == 5)
print(nums)
