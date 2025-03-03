from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex + 1)

        for row in range(2, rowIndex + 1):
            for i in range(row - 1, 0, -1):
                res[i] = res[i - 1] + res[i]

        return res


sol = Solution()
print(sol.getRow(4))