from typing import List

"""
Apply a filter of < last element to each element, and we get a boolean array

nums:    [1, 2, 3, 4, 5]; last element = 5
filter:  [T, T, T, T, T]

nums:    [3, 4, 5, 1, 2]; last element = 2
filter:  [F, F, F, T, T]

nums:    [4, 5, 1, 2, 3]; last element = 3
filter:  [F, F, T, T, T]

Now the problem becomes finding the first T which can easily solved with binary search.

https://algo.monster/problems/min_in_rotated_sorted_array
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        return nums[left]


sol = Solution()
print(sol.findMin([0, 1, 2, 3, 4]))
print(sol.findMin([1, 2, 3, 4, 0]))
print(sol.findMin([2, 3, 4, 0, 1]))
print(sol.findMin([3, 4, 0, 1, 2]))
print(sol.findMin([4, 0, 1, 2, 3]))
