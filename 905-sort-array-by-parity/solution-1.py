from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        Two-pointer approach with opposite directions
        - Even numbers before the `left`
        - Odd numbers after the `right`
        
        if left == right:
        - They meet at an odd number or where `right` has less than 1 element (where all elements are even or 1 odd number at the end)

        `left` will always move to the next position that is not even (odd).
        If `leff` == `right`, all elements before `left` are even and all elements at `left` and after `right` are odd. 
        Therefore, it satisfies our requirements.
        """
        
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 == 1:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums


sol = Solution()
print(sol.sortArrayByParity([2,4,7]))
print(sol.sortArrayByParity([1,3,5]))
print(sol.sortArrayByParity([2,4,6]))
print(sol.sortArrayByParity([3,1,2,4]) == [4, 2, 1, 3])
print(sol.sortArrayByParity([0]) == [0])