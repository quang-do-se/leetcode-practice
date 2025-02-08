from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of `val` from `nums` in-place and returns the new length.

        This algorithm uses a two-pointer approach:
        - `l` (left pointer) scans the array from the beginning.
        - `r` (right pointer) represents the effective length of the array (excluding removed elements).

        The swapping mechanism:
        - When `nums[l] == val`, we swap `nums[l]` with `nums[r - 1]` since `r - 1` is the the last index of the array of length `r`.
        - After the swap, decrease `r` to exclude the swapped value.
        - This effectively removes `val` from the valid portion of the array of length `r`.
        - If `nums[l]` does not match `val`, we simply advance `l`.

        The process continues until the left pointer `l` meets or exceeds the right pointer `r`. 
        At this point, `l` or `r` represents the new length of the list, which excludes all occurrences of `val`.
        """

        l = 0
        r = len(nums)
        while l < r:
            if nums[l] == val:
                nums[l], nums[r - 1] = nums[r - 1], nums[l]
                r -= 1
            else:
                l += 1

        return l


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
