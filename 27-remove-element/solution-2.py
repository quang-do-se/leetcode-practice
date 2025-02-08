from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of `val` from `nums` in-place and returns the new length.

        This algorithm uses a two-pointer approach:
        - `i` serves as the write pointer, iterating through the array.
            - Elements before `i` are in correct position
        - `n` represents the effective length of the array (excluding removed elements).

        The swapping mechanism:
        - If `nums[i] == val`, decrement `n` to shrink the valid portion of the array, making room to move val out.
        - Check if `nums[n] == val`. If so, continue decrementing `n` until `nums[n] != val` or `i >= n`.
        - Once `nums[n]` is a valid element (not `val`) and is outside the valid portion of length `n`, it is ready for swapping.
        - Swap `nums[i] == val` with `nums[n]`, effectively moving `val` out of the valid portion of length `n`.
        - This ensures all occurrences of `val` are removed from the first `n` elements of the array.

        - If `nums[i]` does not match `val`, simply move `i` forward.

        The process continues until the left pointer `i` meets or exceeds the right pointer `n`.
        At this point, `i` or `n` represents the new length of the list, which excludes all occurrences of `val`.
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                n -= 1
                while nums[n] == val and i < n:
                    n -= 1

                nums[i], nums[n] = nums[n], nums[i]
            else:
                i += 1

        return i


sol = Solution()

nums = [0, 1, 2, 3, 4, 2]
print(sol.removeElement(nums, 2) == 4)
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
