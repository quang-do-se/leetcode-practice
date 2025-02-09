from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        max = arr[i]
        arr[i] = -1
        i -= 1

        while i >= 0:
            right_max = max
            if arr[i] > max:
                max = arr[i]
            arr[i] = right_max
            i -= 1

        return arr


sol = Solution()
print(sol.replaceElements([17,18,5,4,6,1]) == [18, 6, 6, 6, 1, -1])
print(sol.replaceElements([400]) == [-1])
print(sol.replaceElements([2,1]) == [1, -1])