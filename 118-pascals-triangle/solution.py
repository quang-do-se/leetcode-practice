from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows + 1):
            row = [1] * i
            if i > 2:
                previous_row = res[len(res) - 1]
                for j in range(1, len(row) - 1):
                    row[j] = previous_row[j - 1] + previous_row[j]
            res.append(row)
        return res


sol = Solution()
print(sol.generate(1) == [[1]])
print(sol.generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])