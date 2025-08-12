from typing import List


class Solution:
    def __init__(self):
        self.memoiz = {0: [1], 1: [1, 1]}

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex in self.memoiz:
            return self.memoiz[rowIndex]

        previous_row = self.getRow(rowIndex - 1)
        
        current_row = [1]
        for i in range(1, rowIndex):
            current_row.append(previous_row[i - 1] + previous_row[i])
        current_row.append(1)

        self.memoiz[rowIndex] = current_row

        return current_row
            


sol = Solution()
print(sol.getRow(3))    