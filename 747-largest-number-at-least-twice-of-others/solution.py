from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = (-1, -1)   # (val, index)
        second_largest = (-1, -1)

        for i in range(len(nums)):
            if nums[i] > largest[0]:
                second_largest = largest
                largest = (nums[i], i)
            elif nums[i] > second_largest[0]:
                second_largest = (nums[i], i)
            
        return largest[1] if largest[0] >= second_largest[0] * 2 else -1


sol = Solution()
print(sol.dominantIndex([3,6,1,0]) == 1)
print(sol.dominantIndex([3,6,1,4,0]) == -1)
print(sol.dominantIndex([1,2,3,4]) == -1)