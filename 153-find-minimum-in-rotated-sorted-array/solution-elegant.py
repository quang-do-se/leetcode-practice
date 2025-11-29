from typing import List

"""
Think of this as applying a boolean filter based on the last element.

Define a predicate: nums[i] <= last element

nums:    [1, 2, 3, 4, 5]; last element = 5
filter:  [T, T, T, T, T]

nums:    [3, 4, 5, 1, 2]; last element = 2
filter:  [F, F, F, T, T]

nums:    [4, 5, 1, 2, 3]; last element = 3
filter:  [F, F, T, T, T]

Our task is now: **find the index of the first True**.
That's a standard "first True" binary search problem on a
sorted boolean array of the form [F ... F, T ... T].

Binary search invariants:

- If nums[m] > nums[h]:
    - nums[m] is in False region (the left, rotated part).
    - All elements at indices <= m are also False.
    - We can safely move `l` to `m + 1`.

- Else (nums[m] <= nums[h]):
    - nums[m] is in the True region (the right, sorted part).
    - So index m could be the first True, or it might be to the left.
    - We move `h` to `m` to keep m in the search range.

We stop when l == h; at that point l (or h) points to
the first True, i.e., the index of the minimum element.
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1

        while l < h:
            m = (l + h) // 2
            if nums[m] > nums[h]:
                l = m + 1
            else:
                h = m

        return nums[h]  # or nums[l]


sol = Solution()
print(sol.findMin([0, 1, 2, 3, 4]))
print(sol.findMin([1, 2, 3, 4, 0]))
print(sol.findMin([2, 3, 4, 0, 1]))
print(sol.findMin([3, 4, 0, 1, 2]))
print(sol.findMin([4, 0, 1, 2, 3]))
