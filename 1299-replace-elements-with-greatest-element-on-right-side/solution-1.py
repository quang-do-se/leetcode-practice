from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1

        for i in range(len(arr) - 1, -1, -1):
            cur = arr[i]
            arr[i] = max_val
            max_val = max(cur, max_val)

        return arr


sol = Solution()
print(sol.replaceElements([17,18,5,4,6,1]) == [18, 6, 6, 6, 1, -1])
print(sol.replaceElements([400]) == [-1])
print(sol.replaceElements([2,1]) == [1, -1])