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
        - When `nums[i] == val`, decrement `n` (shrinking the valid portion of the array) to leave space for swapping the `val` out of the array
        - Check if the new space with index `n` equals to the `value`
        - If `nums[n] == val`,  continue decrementing `n` until until `nums[n] != val` or `n <= i`
        - At this point, element at index `n` is not `val` and is ready for swapping
        - We then swap `nums[i]` with `nums[n]`
        - This effectively removes `val` from the valid portion of the array of length `n`.

        - If `nums[i]` does not match `val`, simply move `i` forward.

        The process continues until the left pointer `i` meets or exceeds the right pointer `n`.
        At this point, `i` or `n` represents the new length of the list, which excludes all occurrences of `val`.
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                n -= 1
                while nums[n] == val and n > i:
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
