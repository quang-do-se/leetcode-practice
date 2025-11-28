from typing import List

"""
Apply a filter of < last element to each element, and we get a boolean array

[3,4,5,1,2] => filter( < last element) => [F, F, F, F, T, T]

Now the problem becomes finding the first T which can easily solved with binary search.

https://algo.monster/problems/min_in_rotated_sorted_array
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        boundary_index = -1

        while left <= right:
            mid = (left + right) // 2

            # if mid <= last element, then belongs to lower half
            if nums[mid] <= nums[-1]:
                boundary_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return nums[boundary_index]


sol = Solution()
print(sol.findMin([0, 1, 2, 3, 4]))
print(sol.findMin([1, 2, 3, 4, 0]))
print(sol.findMin([2, 3, 4, 0, 1]))
print(sol.findMin([3, 4, 0, 1, 2]))
print(sol.findMin([4, 0, 1, 2, 3]))
