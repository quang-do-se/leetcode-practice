from collections import deque
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        dup_count = 0
        hold = deque()

        i = 0
        while i < len(arr):
            if dup_count > 0:
                hold.append(arr[i])
                arr[i] = 0
                dup_count -= 1
                i += 1
                continue

            if hold:
                hold.append(arr[i])
                arr[i] = hold.popleft()

            if arr[i] == 0:
                dup_count += 1
            i += 1


sol = Solution()
arr = [1,0,2,3,0,4,5,0]
sol.duplicateZeros(arr)
print(arr == [1, 0, 0, 2, 3, 0, 0, 4])

arr = [0,2,0,0,5,0]
sol.duplicateZeros(arr)
print(arr == [0, 0, 2, 0, 0, 0])

arr = [0,0,0]
sol.duplicateZeros(arr)
print(arr == [0, 0, 0])

arr = [0,0,1,0,0]
sol.duplicateZeros(arr)
print(arr == [0, 0, 0, 0, 1])

arr = [1,2,3]
sol.duplicateZeros(arr)
print(arr == [1, 2, 3])

arr = [0]
sol.duplicateZeros(arr)
print(arr == [0])