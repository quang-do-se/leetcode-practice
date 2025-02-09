from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # Editorial solution
        N = len(arr)
        if N < 3:
            return False

        i = 0

        # walk up
        while i+1 < N and arr[i] < arr[i + 1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N - 1:
            return False

        # walk down
        while i+1 < N and arr[i] > arr[i + 1]:
            i += 1

        return i == N - 1


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