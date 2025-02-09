from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        index = 1

        # Check increasing:
        increase_count = 0
        for i in range(index, len(arr)):
            if arr[i - 1] >= arr[i]:
                break
            else:
                increase_count += 1
            index += 1

        # arr is not a mountain
        # if it does not go up at the beginning
        # or it only goes up (there is no downward slope since we reach the end of the array)
        if increase_count == 0 or index >= len(arr):
            return False

        # Check decreasing:
        decrease_count = 0
        for i in range(index, len(arr)):
            if arr[i - 1] <= arr[i]:
                return False
            else:
                decrease_count += 1
            index += 1

        return True


sol = Solution()
print(sol.validMountainArray([2,1]) == False)
print(sol.validMountainArray([3,5,5]) == False)
print(sol.validMountainArray([0,3,2,1]) == True)
print(sol.validMountainArray([0,1,0]) == True)
print(sol.validMountainArray([0,1]) == False)
print(sol.validMountainArray([0,2,3,4,5,2,1,0]) == True)
print(sol.validMountainArray([0,2,3,3,5,2,1,0]) == False)
print(sol.validMountainArray([0,1,2,1,2]) == False)
print(sol.validMountainArray([0,1,2]) == False)